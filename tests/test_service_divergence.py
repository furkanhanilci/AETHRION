"""When one half of a sync succeeds and the other does not, someone must be told.

`sync()` commits the ingest before the projection runs, because they are
different stores and there is no distributed transaction to be had. That
ordering was never the defect. The defect (finding **M6**) was that a failing
projection left the registry advanced, the vault stale, and *nothing anywhere
saying so* — `sync_runs` held only the ingest counters, so a system that had come
apart looked exactly like a healthy one.
"""
import asyncio

import httpx
import pytest

from airl_bridge.database import Database
from airl_bridge.obsidian import ObsidianProjector, ProjectionError
from airl_bridge.service import BridgeService
from airl_bridge.zotero import ZoteroClient


def item(key: str) -> dict:
    return {"key": key, "version": 1,
            "data": {"key": key, "itemType": "journalArticle", "title": key}}


def build(settings, tmp_path, projector=None):
    def handler(request: httpx.Request) -> httpx.Response:
        start = int(request.url.params.get("start", 0))
        return httpx.Response(200, json=[item("K1")] if start == 0 else [])

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    service = BridgeService(
        database,
        ZoteroClient(settings, transport=httpx.MockTransport(handler)),
        projector or ObsidianProjector(settings),
    )
    return database, service


class FailingProjector(ObsidianProjector):
    def project_sources(self, sources, dry_run: bool = False):
        raise ProjectionError("the vault went away mid-run")


def test_a_failing_projection_is_reported_not_swallowed(settings, tmp_path):
    database, service = build(settings, tmp_path, FailingProjector(settings))
    result = asyncio.run(service.sync())

    assert result.diverged is True
    assert result.projection is None
    assert "went away" in result.projection_error
    assert result.ingest.inserted == 1, "the ingest half really did succeed"


def test_the_divergence_reaches_the_run_ledger(settings, tmp_path):
    """A caller can ignore a return value. The ledger is what an operator reads
    afterwards, and it is where the evidence has to be."""
    database, service = build(settings, tmp_path, FailingProjector(settings))
    asyncio.run(service.sync())

    row = database.last_divergence()
    assert row is not None
    assert row["status"] == "DIVERGED"
    assert "projection" in row["error"]


def test_a_healthy_sync_records_no_divergence(settings, tmp_path):
    """The negative control. Without it this suite would pass just as happily
    against a service that recorded a divergence on every run."""
    database, service = build(settings, tmp_path)
    result = asyncio.run(service.sync())

    assert result.diverged is False
    assert result.projection is not None
    assert database.last_divergence() is None


def test_an_ingest_failure_does_not_masquerade_as_a_divergence(settings, tmp_path):
    """A sync that never got past the ingest has not diverged — nothing moved.

    Reporting it as a divergence would send an operator looking for a
    reconciliation that is not needed.
    """
    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    service = BridgeService(
        database,
        ZoteroClient(settings, transport=httpx.MockTransport(
            lambda _: (_ for _ in ()).throw(httpx.ConnectError("refused")))),
        ObsidianProjector(settings),
    )
    with pytest.raises(Exception):
        asyncio.run(service.sync())
    assert database.last_divergence() is None


# --- findings H1 + M9 are one property, not two ----------------------------

def test_a_partial_walk_does_not_reconcile_deletions(settings, tmp_path):
    """The coupling the findings register named when it said to fix M9 before H1.

    Reconciling a library against a partial fetch withdraws every source the
    fetch did not reach. Here the ingest is capped at one item while the library
    holds two, and the second must survive.
    """
    pages = {0: [item("K1"), item("K2")]}

    def handler(request: httpx.Request) -> httpx.Response:
        start = int(request.url.params.get("start", 0))
        return httpx.Response(200, json=pages.get(start, []))

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    service = BridgeService(
        database,
        ZoteroClient(settings, transport=httpx.MockTransport(handler)),
        ObsidianProjector(settings),
    )
    asyncio.run(service.ingest_zotero())          # complete: both stored
    assert database.count_sources() == 2

    partial = asyncio.run(service.ingest_zotero(limit=1))
    assert partial.complete is False
    assert partial.withdrawn == 0
    assert database.count_sources() == 2, "a partial walk must withdraw nothing"


def test_a_complete_walk_withdraws_what_is_gone(settings, tmp_path):
    library = {"items": [item("K1"), item("K2")]}

    def handler(request: httpx.Request) -> httpx.Response:
        start = int(request.url.params.get("start", 0))
        return httpx.Response(200, json=library["items"] if start == 0 else [])

    database = Database(tmp_path / "db.sqlite3")
    database.initialize()
    service = BridgeService(
        database,
        ZoteroClient(settings, transport=httpx.MockTransport(handler)),
        ObsidianProjector(settings),
    )
    asyncio.run(service.ingest_zotero())
    assert database.count_sources() == 2

    library["items"] = [item("K1")]
    result = asyncio.run(service.ingest_zotero())

    assert result.complete is True and result.withdrawn == 1
    assert database.count_sources() == 1
    assert len(database.list_sources(include_withdrawn=True)) == 2
