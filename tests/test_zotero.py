"""Tests for source identity and normalisation.

The key property: ``airl_id`` derives from the Zotero binding, not from the
title, so editing a title does not mint a new identity. Everything downstream —
projection file names, duplicate reporting, future claim lineage — depends on
that stability.

Not covered: the read-only boundary itself (finding **H3**) and pagination
behaviour (finding **H1**), because neither has an implementation to test.
"""
import asyncio

import httpx
import pytest

from airl_bridge.zotero import InvalidZoteroItem, ZoteroClient, normalize_item


def test_normalize_item_uses_stable_binding(settings, zotero_item):
    first, _ = normalize_item(zotero_item, settings)
    changed = {**zotero_item, "data": {**zotero_item["data"], "title": "New title"}}
    second, _ = normalize_item(changed, settings)

    assert first.airl_id == second.airl_id
    assert first.content_hash != second.content_hash


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
    items = asyncio.run(client.fetch_top_items(limit=1))
    assert items[0]["key"] == "ABCD1234"
