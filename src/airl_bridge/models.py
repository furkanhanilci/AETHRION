from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class SourceRecord(BaseModel):
    airl_id: str
    zotero_library_type: str
    zotero_library_id: str
    zotero_key: str
    zotero_version: int
    item_type: str
    title: str
    creators: list[dict[str, Any]] = Field(default_factory=list)
    publication_date: str = ""
    doi: str = ""
    url: str = ""
    abstract_note: str = ""
    tags: list[dict[str, Any]] = Field(default_factory=list)
    content_hash: str
    synced_at: datetime


class IngestResult(BaseModel):
    fetched: int
    inserted: int
    updated: int
    unchanged: int
    skipped: int


class ProjectionResult(BaseModel):
    projected: int
    directory: str
    removed_stale: int = 0
    dashboard_directory: str | None = None


class CategorySummary(BaseModel):
    item_type: str
    display_name: str
    source_count: int


class DuplicateGroup(BaseModel):
    normalized_title: str
    source_count: int
    sources: list[SourceRecord]


class SyncResult(BaseModel):
    ingest: IngestResult
    projection: ProjectionResult


class HealthResponse(BaseModel):
    status: str
    version: str
    database: str
    zotero_base_url: str
    obsidian_vault: str
    zotero_write_enabled: bool = False
