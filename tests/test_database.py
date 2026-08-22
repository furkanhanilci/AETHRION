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


def test_unchanged_source_is_not_rewritten(settings, zotero_item):
    """An `unchanged` count must be backed by nothing having been written.

    `synced_at` is rendered into every Obsidian note as `generated_at`, so
    refreshing it on an unchanged record rewrote the whole vault on every timer
    run while the run reported that nothing had changed.
    """
    database = Database(settings.database_path)
    database.initialize()
    source, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(source, raw)])
    first_synced_at = database.get_source(source.airl_id).synced_at

    later, later_raw = normalize_item(zotero_item, settings)
    assert later.synced_at > first_synced_at, "fixture must be re-normalised later"
    result = database.upsert_sources([(later, later_raw)])

    assert result == {"inserted": 0, "updated": 0, "unchanged": 1}
    assert database.get_source(source.airl_id).synced_at == first_synced_at


def test_unchanged_content_still_reconciles_a_moved_zotero_version(settings, zotero_item):
    """The upstream version is not part of the content hash, so it is the one
    thing an unchanged record still reconciles — without touching `synced_at`."""
    database = Database(settings.database_path)
    database.initialize()
    source, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(source, raw)])
    first_synced_at = database.get_source(source.airl_id).synced_at

    bumped = {**zotero_item, "version": 9, "data": {**zotero_item["data"], "version": 9}}
    bumped_source, bumped_raw = normalize_item(bumped, settings)
    result = database.upsert_sources([(bumped_source, bumped_raw)])

    assert result["unchanged"] == 1
    stored = database.get_source(source.airl_id)
    assert stored.zotero_version == 9
    assert stored.synced_at == first_synced_at
