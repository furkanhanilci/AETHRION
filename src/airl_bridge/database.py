"""The canonical V0 source registry, backed by SQLite in WAL mode.

This is the system-of-record for source identity in V0. It will be replaced by
the PostgreSQL Source Registry (WP-061) once that exists; until then, every
claim about "canonical" state in this repository means *this file*.

Design properties worth preserving:

* **Idempotent upsert.** Insert/update/unchanged is decided by comparing
  ``content_hash``, with a UNIQUE constraint on
  ``(zotero_library_type, zotero_library_id, zotero_key)``.
* **An unchanged record is not written.** ``synced_at`` records when the content
  last *changed*, not when it was last looked at. The projection renders it as
  each note's ``generated_at``, so refreshing it on every run rewrote the whole
  vault every 30 minutes while the run reported ``unchanged``. A counter that
  says nothing happened must be backed by nothing happening.
* **Run history.** ``sync_runs`` records every ingest attempt with its counters,
  so a failed run is visible rather than silent.

Known limitations:

* **No deletion or tombstone path (finding H2).** Nothing in this module deletes
  a source or marks it withdrawn, and the Zotero ``/deleted`` endpoint is never
  read. A source removed in Zotero therefore lives on here — and in Obsidian —
  indefinitely.
* **Connections are never closed (finding M8).** ``with self.connect()`` is a
  *transaction* context manager in ``sqlite3``; it does not close the
  connection. Every request leaks one until garbage collection.
* **``schema_meta.schema_version`` is written and never read.** There is no
  migration mechanism.
"""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .models import SourceRecord


SCHEMA = """
CREATE TABLE IF NOT EXISTS schema_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sources (
    airl_id TEXT PRIMARY KEY,
    zotero_library_type TEXT NOT NULL,
    zotero_library_id TEXT NOT NULL,
    zotero_key TEXT NOT NULL,
    zotero_version INTEGER NOT NULL,
    item_type TEXT NOT NULL,
    title TEXT NOT NULL,
    creators_json TEXT NOT NULL,
    publication_date TEXT NOT NULL,
    doi TEXT NOT NULL,
    url TEXT NOT NULL,
    abstract_note TEXT NOT NULL,
    tags_json TEXT NOT NULL,
    raw_json TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    synced_at TEXT NOT NULL,
    UNIQUE (zotero_library_type, zotero_library_id, zotero_key)
);

CREATE INDEX IF NOT EXISTS idx_sources_doi ON sources(doi);
CREATE INDEX IF NOT EXISTS idx_sources_title ON sources(title);

CREATE TABLE IF NOT EXISTS sync_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL,
    fetched INTEGER NOT NULL DEFAULT 0,
    inserted INTEGER NOT NULL DEFAULT 0,
    updated INTEGER NOT NULL DEFAULT 0,
    unchanged INTEGER NOT NULL DEFAULT 0,
    skipped INTEGER NOT NULL DEFAULT 0,
    error TEXT
);
"""


class Database:
    def __init__(self, path: Path):
        self.path = Path(path)

    def connect(self) -> sqlite3.Connection:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA busy_timeout=5000")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(SCHEMA)
            connection.execute(
                "INSERT OR REPLACE INTO schema_meta(key, value) VALUES (?, ?)",
                ("schema_version", "1"),
            )

    def upsert_sources(
        self, sources: Iterable[tuple[SourceRecord, dict[str, Any]]]
    ) -> dict[str, int]:
        counts = {"inserted": 0, "updated": 0, "unchanged": 0}
        with self.connect() as connection:
            for source, raw in sources:
                existing = connection.execute(
                    """
                    SELECT airl_id, content_hash, zotero_version FROM sources
                    WHERE zotero_library_type = ?
                      AND zotero_library_id = ?
                      AND zotero_key = ?
                    """,
                    (
                        source.zotero_library_type,
                        source.zotero_library_id,
                        source.zotero_key,
                    ),
                ).fetchone()
                values = (
                    source.airl_id,
                    source.zotero_library_type,
                    source.zotero_library_id,
                    source.zotero_key,
                    source.zotero_version,
                    source.item_type,
                    source.title,
                    json.dumps(source.creators, ensure_ascii=False, sort_keys=True),
                    source.publication_date,
                    source.doi,
                    source.url,
                    source.abstract_note,
                    json.dumps(source.tags, ensure_ascii=False, sort_keys=True),
                    json.dumps(raw, ensure_ascii=False, sort_keys=True),
                    source.content_hash,
                    source.synced_at.isoformat(),
                )
                if existing is None:
                    connection.execute(
                        """
                        INSERT INTO sources(
                            airl_id, zotero_library_type, zotero_library_id,
                            zotero_key, zotero_version, item_type, title,
                            creators_json, publication_date, doi, url,
                            abstract_note, tags_json, raw_json, content_hash, synced_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        values,
                    )
                    counts["inserted"] += 1
                elif existing["content_hash"] == source.content_hash:
                    # An unchanged record is not written. ``synced_at`` is the
                    # time the content last *changed*, not the time it was last
                    # looked at, because the Obsidian projection renders it as
                    # the note's ``generated_at``: refreshing it on every sync
                    # rewrote all 33 notes every 30 minutes while this branch
                    # reported that nothing had changed. Only the upstream
                    # version is reconciled, and only when it actually moved.
                    if existing["zotero_version"] != source.zotero_version:
                        connection.execute(
                            "UPDATE sources SET zotero_version = ? WHERE airl_id = ?",
                            (source.zotero_version, existing["airl_id"]),
                        )
                    counts["unchanged"] += 1
                else:
                    connection.execute(
                        """
                        UPDATE sources SET
                            zotero_version = ?, item_type = ?, title = ?, creators_json = ?,
                            publication_date = ?, doi = ?, url = ?, abstract_note = ?,
                            tags_json = ?, raw_json = ?, content_hash = ?, synced_at = ?
                        WHERE airl_id = ?
                        """,
                        (
                            source.zotero_version,
                            source.item_type,
                            source.title,
                            json.dumps(source.creators, ensure_ascii=False, sort_keys=True),
                            source.publication_date,
                            source.doi,
                            source.url,
                            source.abstract_note,
                            json.dumps(source.tags, ensure_ascii=False, sort_keys=True),
                            json.dumps(raw, ensure_ascii=False, sort_keys=True),
                            source.content_hash,
                            source.synced_at.isoformat(),
                            existing["airl_id"],
                        ),
                    )
                    counts["updated"] += 1
        return counts

    def list_sources(self, limit: int = 100, offset: int = 0) -> list[SourceRecord]:
        with self.connect() as connection:
            rows = connection.execute(
                "SELECT * FROM sources ORDER BY synced_at DESC LIMIT ? OFFSET ?",
                (limit, offset),
            ).fetchall()
        return [self._row_to_source(row) for row in rows]

    def get_source(self, airl_id: str) -> SourceRecord | None:
        with self.connect() as connection:
            row = connection.execute(
                "SELECT * FROM sources WHERE airl_id = ?", (airl_id,)
            ).fetchone()
        return self._row_to_source(row) if row is not None else None

    def search_sources(self, query: str, limit: int = 25) -> list[SourceRecord]:
        escaped = query.casefold().replace("\\", "\\\\")
        escaped = escaped.replace("%", "\\%").replace("_", "\\_")
        pattern = f"%{escaped}%"
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT * FROM sources
                WHERE lower(title) LIKE ? ESCAPE '\\'
                   OR lower(doi) LIKE ? ESCAPE '\\'
                   OR lower(abstract_note) LIKE ? ESCAPE '\\'
                   OR lower(creators_json) LIKE ? ESCAPE '\\'
                   OR lower(tags_json) LIKE ? ESCAPE '\\'
                ORDER BY title COLLATE NOCASE, zotero_key
                LIMIT ?
                """,
                (pattern, pattern, pattern, pattern, pattern, limit),
            ).fetchall()
        return [self._row_to_source(row) for row in rows]

    def list_category_counts(self) -> list[tuple[str, int]]:
        with self.connect() as connection:
            rows = connection.execute(
                """
                SELECT item_type, COUNT(*) AS source_count
                FROM sources
                GROUP BY item_type
                ORDER BY source_count DESC, item_type
                """
            ).fetchall()
        return [(str(row["item_type"]), int(row["source_count"])) for row in rows]

    def count_sources(self) -> int:
        with self.connect() as connection:
            row = connection.execute("SELECT COUNT(*) AS count FROM sources").fetchone()
        return int(row["count"])

    def start_sync(self) -> int:
        now = datetime.now(timezone.utc).isoformat()
        with self.connect() as connection:
            cursor = connection.execute(
                "INSERT INTO sync_runs(started_at, status) VALUES (?, ?)",
                (now, "RUNNING"),
            )
            return int(cursor.lastrowid)

    def finish_sync(
        self,
        run_id: int,
        *,
        status: str,
        fetched: int = 0,
        inserted: int = 0,
        updated: int = 0,
        unchanged: int = 0,
        skipped: int = 0,
        error: str | None = None,
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self.connect() as connection:
            connection.execute(
                """
                UPDATE sync_runs SET
                    completed_at = ?, status = ?, fetched = ?, inserted = ?,
                    updated = ?, unchanged = ?, skipped = ?, error = ?
                WHERE id = ?
                """,
                (
                    now,
                    status,
                    fetched,
                    inserted,
                    updated,
                    unchanged,
                    skipped,
                    error,
                    run_id,
                ),
            )

    @staticmethod
    def _row_to_source(row: sqlite3.Row) -> SourceRecord:
        return SourceRecord(
            airl_id=row["airl_id"],
            zotero_library_type=row["zotero_library_type"],
            zotero_library_id=row["zotero_library_id"],
            zotero_key=row["zotero_key"],
            zotero_version=row["zotero_version"],
            item_type=row["item_type"],
            title=row["title"],
            creators=json.loads(row["creators_json"]),
            publication_date=row["publication_date"],
            doi=row["doi"],
            url=row["url"],
            abstract_note=row["abstract_note"],
            tags=json.loads(row["tags_json"]),
            content_hash=row["content_hash"],
            synced_at=row["synced_at"],
        )
