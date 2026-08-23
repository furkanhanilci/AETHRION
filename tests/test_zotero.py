"""Source identity, the read-only boundary, and pagination.

The key identity property: ``airl_id`` derives from the Zotero binding, not from
the title, so editing a title does not mint a new identity. Everything
downstream — projection file names, duplicate reporting, future claim lineage —
depends on that stability.

The other two properties here were audit findings until this file could prove
them. **H3** is the important one: "this system never writes to Zotero" is the
framework's strongest security claim, and it was asserted by a hard-coded
constant, so the artifacts that appeared to verify it were testing
``False is False``.
"""
import asyncio

import httpx
import pytest

from airl_bridge.zotero import InvalidZoteroItem, ZoteroClient, ZoteroUnavailable, normalize_item


def test_normalize_item_uses_stable_binding(settings, zotero_item):
    first, _ = normalize_item(zotero_item, settings)
    changed = {**zotero_item, "data": {**zotero_item["data"], "title": "New title"}}
    second, _ = normalize_item(changed, settings)

    assert first.airl_id == second.airl_id
    assert first.content_hash != second.content_hash


def test_content_hash_is_minted_through_the_contract_core(settings, zotero_item):
    """Finding H4: the bridge and the contract core define one digest, not two.

    They used to define two — a bare 64-character digest in the contract and a
    ``sha256:``-prefixed one in the bridge — and because nothing imported
    anything, neither side could discover it.
    """
    from airl_framework.contracts import content_digest

    record, _ = normalize_item(zotero_item, settings)
    assert record.content_hash.startswith("sha256:")
    assert content_digest(b"probe").startswith("sha256:")


def test_child_item_is_rejected(settings, zotero_item):
    attachment = {
        **zotero_item,
        "data": {**zotero_item["data"], "itemType": "attachment"},
    }
    with pytest.raises(InvalidZoteroItem):
        normalize_item(attachment, settings)


def test_zotero_client_requests_api_v3(settings, zotero_item):
    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["Zotero-API-Version"] == "3"
        assert request.url.path.endswith("/api/users/0/items/top")
        return httpx.Response(200, json=[zotero_item])

    client = ZoteroClient(settings, transport=httpx.MockTransport(handler))
    items, complete = asyncio.run(client.fetch_top_items(limit=1))
    assert items[0]["key"] == "ABCD1234"
    assert complete is False, "asking for 1 and getting 1 is not a complete walk"


# --- finding H3: the read-only boundary, proven behaviourally ---------------

class WriteAttempted(AssertionError):
    """Raised by the transport if anything but a GET is issued."""


def read_only_transport(responder) -> httpx.MockTransport:
    """A transport that fails the test on any method other than GET.

    This is the whole of H3's fix. `zotero_write_enabled` is a constant that a
    reader is invited to trust; this is a control that can actually refuse, and
    it is driven through the real client rather than asserted about it.
    """
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method != "GET":
            raise WriteAttempted(
                f"the Zotero client issued {request.method} {request.url} — "
                f"the read-only boundary is the framework's strongest security "
                f"claim and this is what breaking it looks like")
        return responder(request)
    return httpx.MockTransport(handler)


def test_the_client_issues_only_gets(settings, zotero_item):
    client = ZoteroClient(settings, transport=read_only_transport(
        lambda _: httpx.Response(200, json=[zotero_item])))
    items, _ = asyncio.run(client.fetch_top_items(limit=1))
    assert items


def test_a_full_sync_issues_only_gets(settings, tmp_path, zotero_item):
    """The property driven through the whole flow, not just the client.

    A boundary that holds in one method and leaks in another is not a boundary,
    so the assertion is made against every request the sync makes.
    """
    from airl_bridge.database import Database
    from airl_bridge.obsidian import ObsidianProjector
    from airl_bridge.service import BridgeService

    methods: list[str] = []

    def responder(request: httpx.Request) -> httpx.Response:
        methods.append(request.method)
        if request.url.params.get("start") in (None, "0"):
            return httpx.Response(200, json=[zotero_item])
        return httpx.Response(200, json=[])

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    service = BridgeService(
        database,
        ZoteroClient(settings, transport=read_only_transport(responder)),
        ObsidianProjector(settings),
    )
    asyncio.run(service.ingest_zotero())
    assert methods and set(methods) == {"GET"}


def test_the_read_only_transport_can_actually_fail(settings):
    """The control must be observable failing, or it proves nothing.

    Without this, `test_a_full_sync_issues_only_gets` passes just as happily
    against a transport that never checks anything.
    """
    transport = read_only_transport(lambda _: httpx.Response(200, json=[]))

    async def attempt() -> None:
        async with httpx.AsyncClient(transport=transport) as client:
            await client.post("http://127.0.0.1/api/users/0/items")

    with pytest.raises(WriteAttempted):
        asyncio.run(attempt())


# --- finding H1: pagination, and the completeness signal --------------------

def paged(pages: list[list[dict]], total: int | None = None):
    def handler(request: httpx.Request) -> httpx.Response:
        start = int(request.url.params.get("start", 0))
        index = start // 100
        body = pages[index] if index < len(pages) else []
        headers = {"Total-Results": str(total)} if total is not None else {}
        return httpx.Response(200, json=body, headers=headers)
    return httpx.MockTransport(handler)


def item(key: str) -> dict:
    return {"key": key, "version": 1,
            "data": {"key": key, "itemType": "journalArticle", "title": key}}


def test_pagination_walks_past_the_first_hundred(settings):
    """The defect: one call capped at 100, and a run recorded as SUCCEEDED."""
    first = [item(f"K{n:04d}") for n in range(100)]
    second = [item(f"K{n:04d}") for n in range(100, 137)]
    client = ZoteroClient(settings, transport=paged([first, second]))
    items, complete = asyncio.run(client.fetch_top_items())
    assert len(items) == 137
    assert complete is True


def test_an_exact_multiple_of_the_page_size_terminates(settings):
    """The off-by-one that a short-page rule has to get right.

    200 items in two full pages: the walk only knows it is done when the third
    page comes back empty.
    """
    pages = [[item(f"K{n:04d}") for n in range(100)],
             [item(f"K{n:04d}") for n in range(100, 200)], []]
    client = ZoteroClient(settings, transport=paged(pages))
    items, complete = asyncio.run(client.fetch_top_items())
    assert len(items) == 200 and complete is True


def test_a_total_results_disagreement_refuses_rather_than_reconciling(settings):
    """The cross-check that stops a partial walk being called complete.

    This matters because a complete walk authorises the deletion reconciliation.
    Calling a partial walk complete would withdraw every source it did not reach.
    """
    client = ZoteroClient(settings, transport=paged(
        [[item("K1"), item("K2")]], total=900))
    with pytest.raises(ZoteroUnavailable) as caught:
        asyncio.run(client.fetch_top_items())
    assert "Total-Results" in str(caught.value)


def test_a_missing_total_results_header_is_not_an_error(settings):
    """Zotero's local API does not always send it.

    A client that *requires* a header to know it has finished stops working the
    day the header stops arriving, so termination is decided by a short page and
    the header is only ever a cross-check.
    """
    client = ZoteroClient(settings, transport=paged([[item("K1")]]))
    items, complete = asyncio.run(client.fetch_top_items())
    assert len(items) == 1 and complete is True
