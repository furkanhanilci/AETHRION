"""Tests for the canonical V0 registry.

The important assertion is idempotency: re-ingesting the same Zotero item must
produce ``unchanged``, never a duplicate row. That property is what makes the
30-minute timer safe to run unattended.

Also covered here, each a former audit finding: deletion as a **tombstone**
rather than a disappearance (**H2**), refusal on an identifier collision
(**L2**), and a session that closes its connection rather than merely committing
it (**M8**).
"""
import pytest

from airl_bridge.database import Database
from airl_bridge.zotero import normalize_item


def test_upsert_is_idempotent(settings, zotero_item):
    database = Database(settings.database_path)
    database.initialize()
    source, raw = normalize_item(zotero_item, settings)

    first = database.upsert_sources([(source, raw)])
    second = database.upsert_sources([(source, raw)])

    assert {k: v for k, v in first.items() if k in ("inserted", "updated", "unchanged")} == {"inserted": 1, "updated": 0, "unchanged": 0}
    assert {k: v for k, v in second.items() if k in ("inserted", "updated", "unchanged")} == {"inserted": 0, "updated": 0, "unchanged": 1}
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

    assert {k: v for k, v in result.items() if k in ("inserted", "updated", "unchanged")} == {"inserted": 0, "updated": 0, "unchanged": 1}
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


# --- finding H2: deletion is a tombstone, not a disappearance ---------------

def test_a_source_absent_upstream_is_withdrawn_not_deleted(settings, zotero_item, tmp_path):
    """A registry is the system of record for source identity.

    An identity that silently vanishes cannot afterwards be told apart from one
    that never existed — which is exactly the question an audit asks about a
    citation that no longer resolves.
    """
    from airl_bridge.database import Database
    from airl_bridge.zotero import normalize_item

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    record, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(record, raw)])

    withdrawn = database.reconcile_deletions(
        [], library_type=settings.zotero_library_type,
        library_id=settings.zotero_library_id)

    assert withdrawn == [record.airl_id]
    assert database.list_sources() == []
    assert database.count_sources() == 0
    kept = database.list_sources(include_withdrawn=True)
    assert len(kept) == 1 and kept[0].withdrawn_at is not None


def test_a_withdrawn_source_that_returns_keeps_its_identity(settings, zotero_item, tmp_path):
    """Minting a new airl_id on revival would break every reference made while
    the source was withdrawn."""
    from airl_bridge.database import Database
    from airl_bridge.zotero import normalize_item

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    record, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(record, raw)])
    database.reconcile_deletions([], library_type=settings.zotero_library_type,
                                 library_id=settings.zotero_library_id)

    counts = database.upsert_sources([(record, raw)])

    assert counts["revived"] == 1
    live = database.list_sources()
    assert len(live) == 1 and live[0].airl_id == record.airl_id


def test_a_withdrawn_source_is_invisible_to_search_and_categories(settings, zotero_item, tmp_path):
    from airl_bridge.database import Database
    from airl_bridge.zotero import normalize_item

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    record, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(record, raw)])
    assert database.search_sources("reproducible")
    database.reconcile_deletions([], library_type=settings.zotero_library_type,
                                 library_id=settings.zotero_library_id)

    assert database.search_sources("reproducible") == []
    assert database.list_category_counts() == []


# --- finding L2: a truncated identifier must fail loudly --------------------

def test_an_airl_id_collision_is_refused_rather_than_merged(settings, zotero_item, tmp_path):
    """64 bits is fine at this scale. The point is not the width — it is that a
    collision must be *detected* rather than discovered later as two merged
    bibliographies."""
    from dataclasses import replace as dc_replace

    from airl_bridge.database import Database, SourceIdentityCollision
    from airl_bridge.zotero import normalize_item

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    first, raw = normalize_item(zotero_item, settings)
    database.upsert_sources([(first, raw)])

    # A different Zotero key forced onto the same identity — what a collision
    # would look like from the database's side.
    collided = first.model_copy(update={"zotero_key": "ZZZZ9999"})
    with pytest.raises(SourceIdentityCollision) as caught:
        database.upsert_sources([(collided, raw)])
    assert "ZZZZ9999" in str(caught.value)


# --- finding M8: the connection is closed, not merely committed -------------

def test_a_session_closes_its_connection(tmp_path):
    """`with sqlite3.connect(...)` reads like a resource context manager and is
    not one: it commits and rolls back, and never closes."""
    import sqlite3

    from airl_bridge.database import Database

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    with database.session() as connection:
        connection.execute("SELECT 1")
    with pytest.raises(sqlite3.ProgrammingError):
        connection.execute("SELECT 1")


def test_a_failing_session_rolls_back_and_still_closes(tmp_path):
    """The behaviour that was already correct must not change while fixing the
    part that was not."""
    import sqlite3

    from airl_bridge.database import Database

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    with pytest.raises(ValueError):
        with database.session() as connection:
            connection.execute(
                "INSERT INTO schema_meta(key, value) VALUES ('probe', 'x')")
            raise ValueError("boom")
    with database.session() as fresh:
        row = fresh.execute(
            "SELECT value FROM schema_meta WHERE key = 'probe'").fetchone()
    assert row is None
    with pytest.raises(sqlite3.ProgrammingError):
        connection.execute("SELECT 1")


def test_the_v1_to_v2_migration_is_idempotent(tmp_path):
    """`schema_meta.schema_version` was written and never read, so there was no
    migration mechanism at all."""
    from airl_bridge.database import Database

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    database.initialize()
    with database.session() as connection:
        columns = {row["name"] for row in
                   connection.execute("PRAGMA table_info(sources)")}
        version = connection.execute(
            "SELECT value FROM schema_meta WHERE key = 'schema_version'").fetchone()
    assert "withdrawn_at" in columns
    assert version["value"] == Database.SCHEMA_VERSION
