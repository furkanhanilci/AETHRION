"""The orchestration layer: ingest, project, and the sync that combines them.

Known limitations, both recorded in the audit:

* **No transaction boundary (finding M6).** ``sync()`` commits the ingest before
  the projection runs. If the projection then fails, the registry has advanced
  while the vault has not, and nothing records that divergence — ``finish_sync``
  stores only the ingest counters.
* **Silent truncation (finding M9).** ``project_obsidian`` reads at most 10,000
  sources. Above that the projection would not see some sources and
  ``_remove_stale`` would then delete their files as stale. The 100-record ingest
  cap (finding **H1**) masks this today; **fix M9 before fixing H1**, or the H1
  fix opens an active data-loss path.
"""
from __future__ import annotations

from .database import Database
from .models import IngestResult, ProjectionResult, SyncResult
from .obsidian import ObsidianProjector
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

    async def ingest_zotero(self, limit: int = 100) -> IngestResult:
        run_id = self.database.start_sync()
        try:
            raw_items = await self.zotero.fetch_top_items(limit=limit)
            normalized = []
            skipped = 0
            for raw in raw_items:
                try:
                    normalized.append(normalize_item(raw, self.zotero.settings))
                except InvalidZoteroItem:
                    skipped += 1
            counts = self.database.upsert_sources(normalized)
            result = IngestResult(
                fetched=len(raw_items), skipped=skipped, **counts
            )
            self.database.finish_sync(run_id, status="SUCCEEDED", **result.model_dump())
            return result
        except Exception as exc:
            self.database.finish_sync(run_id, status="FAILED", error=str(exc))
            raise

    def project_obsidian(self) -> ProjectionResult:
        sources = self.database.list_sources(limit=10_000)
        return self.projector.project_sources(sources)

    async def sync(self, limit: int = 100) -> SyncResult:
        ingest = await self.ingest_zotero(limit=limit)
        projection = self.project_obsidian()
        return SyncResult(ingest=ingest, projection=projection)
