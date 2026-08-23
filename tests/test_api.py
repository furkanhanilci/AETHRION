"""Tests for the FastAPI surface.

**The defensive paths are the point of this file (finding L4, closed).** Every
mechanism that exists to refuse something is exercised here: the token gate and
its unconfigured case, the ``Host`` check, the ``ZoteroUnavailable`` → 503
handler, the ``ProjectionError`` → 422 handler, the loopback refusal in
``Settings.from_env``, the path-traversal refusal and ``library_type``
validation.

The plan's own Definition of Done requires that "security, data and policy
negative tests have passed", and for a long time none existed — which meant the
line was satisfied by nothing at all.

``zotero_write_enabled`` is still a constant and is still asserted below, but it
is no longer the *evidence* for the read-only claim. That lives in
``tests/test_zotero.py``, where a transport raises on any non-``GET`` and is
itself proven able to raise (finding **H3**).
"""
import asyncio

import httpx
import pytest

from airl_bridge.database import Database
from airl_bridge.main import create_app
from airl_bridge.zotero import normalize_item


async def _request(app, method: str, path: str, **kwargs) -> httpx.Response:
    async with app.router.lifespan_context(app):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport, base_url="http://testserver"
        ) as client:
            return await client.request(method, path, **kwargs)


async def _get(app, path: str) -> httpx.Response:
    return await _request(app, "GET", path)


def test_health_is_local_and_read_only(settings):
    app = create_app(settings)
    response = asyncio.run(_get(app, "/health"))

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["zotero_write_enabled"] is False


def test_sources_starts_empty(settings):
    app = create_app(settings)
    response = asyncio.run(_get(app, "/v1/sources"))

    assert response.status_code == 200
    assert response.json() == []


def test_search_get_categories_and_duplicates(settings, zotero_item):
    database = Database(settings.database_path)
    database.initialize()
    first, raw = normalize_item(zotero_item, settings)
    second_item = {
        **zotero_item,
        "key": "EFGH5678",
        "data": {**zotero_item["data"], "key": "EFGH5678"},
    }
    second, second_raw = normalize_item(second_item, settings)
    database.upsert_sources([(first, raw), (second, second_raw)])
    app = create_app(settings)

    search = asyncio.run(_get(app, "/v1/sources/search?q=reproducible"))
    get_one = asyncio.run(_get(app, f"/v1/sources/{first.airl_id}"))
    categories = asyncio.run(_get(app, "/v1/categories"))
    duplicates = asyncio.run(_get(app, "/v1/duplicates"))

    assert search.status_code == 200
    assert len(search.json()) == 2
    assert get_one.json()["zotero_key"] == "ABCD1234"
    assert categories.json()[0]["display_name"] == "01 - Journal Articles"
    assert duplicates.json()[0]["source_count"] == 2


# --- finding M1: the two controls, and why they are two ---------------------

AUTH = {"X-AIRL-Token": "test-token"}


def test_a_mutating_endpoint_refuses_without_a_token(settings):
    """A custom header is not on the CORS safelist, so a cross-site page cannot
    send it without a preflight — which is the whole CSRF defence."""
    app = create_app(settings)
    for path in ("/v1/ingest/zotero", "/v1/project/obsidian", "/v1/sync"):
        response = asyncio.run(_request(app, "POST", path))
        assert response.status_code == 401, path


def test_a_mutating_endpoint_refuses_a_wrong_token(settings):
    app = create_app(settings)
    response = asyncio.run(_request(
        app, "POST", "/v1/sync", headers={"X-AIRL-Token": "not-the-token"}))
    assert response.status_code == 401


def test_an_unconfigured_token_refuses_rather_than_opening(settings):
    """Failing open on missing configuration is how a mandatory control becomes
    optional in practice while remaining mandatory on paper."""
    from dataclasses import replace

    app = create_app(replace(settings, api_token=""))
    response = asyncio.run(_request(app, "POST", "/v1/sync", headers=AUTH))
    assert response.status_code == 503
    assert "not configured" in response.json()["detail"]


def test_an_unrecognised_host_is_rejected(settings):
    """The DNS-rebinding defence, which protects the READS.

    Rebinding turns `attacker.example` into `127.0.0.1` after the page loads,
    and the browser then treats `GET /v1/sources` as same-origin. A token on the
    mutating endpoints does nothing about that, which is why this is a separate
    control from the one above.
    """
    app = create_app(settings)

    async def call() -> httpx.Response:
        async with app.router.lifespan_context(app):
            transport = httpx.ASGITransport(app=app)
            async with httpx.AsyncClient(
                transport=transport, base_url="http://attacker.example"
            ) as client:
                return await client.get("/v1/sources")

    response = asyncio.run(call())
    assert response.status_code == 421
    assert "AIRL_ALLOWED_HOSTS" in response.json()["detail"]


def test_a_known_host_passes(settings):
    app = create_app(settings)
    assert asyncio.run(_get(app, "/v1/sources")).status_code == 200


# --- the error handlers, which were reachable by nothing --------------------

def test_zotero_unavailable_becomes_503(settings):
    app = create_app(settings)
    app.state.service.zotero.transport = httpx.MockTransport(
        lambda _: (_ for _ in ()).throw(httpx.ConnectError("refused")))
    response = asyncio.run(_request(app, "POST", "/v1/ingest/zotero", headers=AUTH))
    assert response.status_code == 503
    assert "unavailable" in response.json()["detail"]


def test_a_projection_error_becomes_422(settings):
    from dataclasses import replace

    broken = replace(settings, obsidian_vault=settings.obsidian_vault / "absent")
    app = create_app(broken)
    response = asyncio.run(_request(app, "POST", "/v1/project/obsidian", headers=AUTH))
    assert response.status_code == 422
    assert "does not exist" in response.json()["detail"]


def test_ready_reports_the_zotero_failure_rather_than_500(settings):
    app = create_app(settings)
    app.state.zotero.transport = httpx.MockTransport(
        lambda _: (_ for _ in ()).throw(httpx.ConnectError("refused")))
    assert asyncio.run(_get(app, "/ready")).status_code == 503


def test_an_unknown_source_is_404_not_500(settings):
    app = create_app(settings)
    assert asyncio.run(_get(app, "/v1/sources/SRC-ZOT-NOPE")).status_code == 404


# --- finding L4: the configuration refusals --------------------------------

def test_a_non_loopback_bind_is_refused(monkeypatch):
    from airl_bridge.config import Settings

    monkeypatch.setenv("AIRL_API_HOST", "0.0.0.0")
    with pytest.raises(ValueError, match="loopback"):
        Settings.from_env()


def test_a_generated_dir_escaping_the_vault_is_refused(monkeypatch):
    from airl_bridge.config import Settings

    monkeypatch.setenv("AIRL_API_HOST", "127.0.0.1")
    monkeypatch.setenv("AIRL_OBSIDIAN_GENERATED_DIR", "../../etc")
    with pytest.raises(ValueError, match="safe path"):
        Settings.from_env()


def test_an_absolute_generated_dir_is_refused(monkeypatch):
    from airl_bridge.config import Settings

    monkeypatch.setenv("AIRL_API_HOST", "127.0.0.1")
    monkeypatch.setenv("AIRL_OBSIDIAN_GENERATED_DIR", "/tmp/anywhere")
    with pytest.raises(ValueError, match="safe path"):
        Settings.from_env()


def test_an_unknown_library_type_is_refused(monkeypatch):
    from airl_bridge.config import Settings

    monkeypatch.setenv("AIRL_API_HOST", "127.0.0.1")
    monkeypatch.setenv("AIRL_ZOTERO_LIBRARY_TYPE", "everything")
    with pytest.raises(ValueError, match="users or groups"):
        Settings.from_env()
