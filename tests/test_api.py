"""Tests for the FastAPI surface.

⚠️ **Coverage limit (audit finding L4).** Only ``GET`` endpoints are exercised
here. None of the three ``POST`` endpoints is tested, and neither are the
defensive paths: the ``ZoteroUnavailable`` → 503 handler, the ``ProjectionError``
→ 422 handler, the loopback refusal in ``Settings.from_env``, the path-traversal
refusal, or ``library_type`` validation.

In other words **every defensive mechanism in the service is currently
untested**, which directly contradicts the plan's Definition of Done ("security,
data and policy negative tests have passed").

⚠️ ``test_health_reports_readonly_boundary`` asserts
``zotero_write_enabled is False`` against a **hard-coded constant** — it proves
nothing (finding **H3**). The real test is a ``MockTransport`` that raises on any
non-``GET`` method, driven through the whole sync flow.
"""
import asyncio

import httpx

from airl_bridge.database import Database
from airl_bridge.main import create_app
from airl_bridge.zotero import normalize_item


async def _get(app, path: str) -> httpx.Response:
    async with app.router.lifespan_context(app):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport, base_url="http://testserver"
        ) as client:
            return await client.get(path)


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
