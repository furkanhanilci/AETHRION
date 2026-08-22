"""Pydantic models for the Bridge API surface.

These are **transport models**, not canonical contracts. The canonical contract
core lives in :mod:`airl_framework.contracts`; today the two are not bound to
each other (audit finding **H4**), and their ``content_hash`` formats disagree:
this module produces ``"sha256:<hex>"`` while the contract core expects a bare
64-character digest.

Do not add business rules here. A model that starts validating semantics is a
contract in disguise, and it belongs in the contract core where it can be
versioned and enforced.
"""
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
