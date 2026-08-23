"""The orchestration layer: ingest, project, and the sync that combines them.

Two properties this layer is responsible for, both of them former audit
findings and both of them about *honesty under partial failure* rather than
about happy-path behaviour:

* **The divergence is recorded (finding M6, closed).** ``sync()`` commits the
  ingest before the projection runs, because they are different stores and there
  is no distributed transaction to be had. What was wrong was not the ordering —
  it was that a failing projection left the registry advanced, the vault stale,
  and *nothing anywhere saying so*. ``sync`` now records the divergence on the
  run and returns a ``SyncResult`` whose ``diverged`` flag makes it
  unmisreadable.

* **Nothing is silently partial (findings H1 and M9, closed).** The ingest walks
  the whole library and knows whether it reached the end; the projection reads
  every live source rather than the first ten thousand. Those two are one
  property, not two: a projection that sees most sources deletes the rest as
  stale, and a reconciliation run against most of a library withdraws the rest.
"""
from __future__ import annotations

from .database import Database
from .models import IngestResult, ProjectionResult, SyncResult
from .obsidian import ObsidianProjector, ProjectionError
from .zotero import InvalidZoteroItem, ZoteroClient, normalize_item


class BridgeService:
    def __init__(
        self,
        database: Database,
        zotero: ZoteroClient,
        projector: ObsidianProjector,
    ):
        self.database = database
        self.zotero = zotero
        self.projector = projector

    async def ingest_zotero(self, limit: int | None = None) -> IngestResult:
        """Walk the library, upsert, and reconcile deletions if the walk finished.

        `limit` defaults to None — the whole library. It used to default to 100,
        which meant the ordinary call path was a partial sync that reported
        `SUCCEEDED`.
        """
        run_id = self.database.start_sync()
        try:
            raw_items, complete = await self.zotero.fetch_top_items(limit=limit)
            normalized = []
            skipped = 0
            for raw in raw_items:
                try:
                    normalized.append(normalize_item(raw, self.zotero.settings))
                except InvalidZoteroItem:
                    skipped += 1
            counts = self.database.upsert_sources(normalized)
            seen_keys = counts.pop("seen_keys", [])

            # Deletions are reconciled ONLY against a complete walk. This is the
            # coupling the findings register flagged when it said to fix M9
            # before H1: reconciling a library against a partial fetch withdraws
            # every source the fetch did not reach.
            withdrawn: list[str] = []
            if complete:
                withdrawn = self.database.reconcile_deletions(
                    seen_keys,
                    library_type=self.zotero.settings.zotero_library_type,
                    library_id=self.zotero.settings.zotero_library_id,
                )

            result = IngestResult(
                fetched=len(raw_items), skipped=skipped, complete=complete,
                withdrawn=len(withdrawn), **counts
            )
            self.database.finish_sync(
                run_id,
                status="SUCCEEDED" if complete else "PARTIAL",
                **result.model_dump(),
            )
            return result
        except Exception as exc:
            self.database.finish_sync(run_id, status="FAILED", error=str(exc))
            raise

    def project_obsidian(self) -> ProjectionResult:
        """Project every live source.

        `limit=None`, not `limit=10_000`. The cap was finding M9 and it was not
        merely a ceiling: `_remove_stale` deletes any projected file whose source
        is absent from the list it was handed, so a truncated read turned into
        deletion of the notes beyond the cut.
        """
        sources = self.database.list_sources(limit=None)
        return self.projector.project_sources(sources)

    async def sync(self, limit: int | None = None) -> SyncResult:
        """Ingest, then project — and say so plainly when only the first worked.

        There is no transaction spanning SQLite and a directory of Markdown
        files, so the two cannot be made atomic. What can be made true is that a
        caller is never handed a result that looks like both halves succeeded.
        """
        ingest = await self.ingest_zotero(limit=limit)
        try:
            projection = self.project_obsidian()
        except (ProjectionError, OSError) as exc:
            self.database.record_divergence(
                stage="projection",
                detail=f"{type(exc).__name__}: {exc}",
            )
            return SyncResult(
                ingest=ingest,
                projection=None,
                projection_error=f"{type(exc).__name__}: {exc}",
                diverged=True,
            )
        return SyncResult(ingest=ingest, projection=projection)
