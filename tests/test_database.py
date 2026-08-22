"""Tests for the canonical V0 registry.

The important assertion is idempotency: re-ingesting the same Zotero item must
produce ``unchanged``, never a duplicate row. That property is what makes the
30-minute timer safe to run unattended.

Not covered: deletion and tombstoning (they do not exist — finding **H2**), and
connection lifetime (finding **M8**).
"""
from airl_bridge.database import Database
from airl_bridge.zotero import normalize_item


def test_upsert_is_idempotent(settings, zotero_item):
    database = Database(settings.database_path)
    database.initialize()
    source, raw = normalize_item(zotero_item, settings)

    first = database.upsert_sources([(source, raw)])
    second = database.upsert_sources([(source, raw)])

    assert first == {"inserted": 1, "updated": 0, "unchanged": 0}
    assert second == {"inserted": 0, "updated": 0, "unchanged": 1}
    assert database.count_sources() == 1
    assert database.list_sources()[0].doi == "10.1234/example"


def test_content_change_updates_existing_binding(settings, zotero_item):
    database = Database(settings.database_path)
    database.initialize()
    source, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(source, raw)])

    changed = {**zotero_item, "data": {**zotero_item["data"], "title": "Changed title"}}
    changed_source, changed_raw = normalize_item(changed, settings)
    result = database.upsert_sources([(changed_source, changed_raw)])

    assert result["updated"] == 1
    assert database.list_sources()[0].title == "Changed title"
    assert database.list_sources()[0].airl_id == source.airl_id


def test_get_search_and_category_counts(settings, zotero_item):
    database = Database(settings.database_path)
    database.initialize()
    source, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(source, raw)])

    assert database.get_source(source.airl_id) == source
    assert database.get_source("SRC-ZOT-NOT-FOUND") is None
    assert database.search_sources("reproducible")[0].airl_id == source.airl_id
    assert database.search_sources("10.1234/example")[0].airl_id == source.airl_id
    assert database.list_category_counts() == [("journalArticle", 1)]
