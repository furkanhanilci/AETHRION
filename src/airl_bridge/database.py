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
* **Deletions are reconciled (finding H2, closed).** ``reconcile_deletions``
  withdraws sources that are no longer in the library, and the projection stops
  rendering them. A withdrawal is a **tombstone**, not a row deletion: the
  registry is the system of record for source identity, and an identity that
  silently vanishes cannot be distinguished afterwards from one that never
  existed.
* **``schema_meta.schema_version`` is read.** ``initialize`` migrates v1 → v2 by
  adding ``withdrawn_at`` when it is absent. It is the smallest migration
  mechanism that works, and it is idempotent.
"""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from contextlib import contextmanager
from typing import Any, Iterable, Iterator

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
    withdrawn_at TEXT,
    UNIQUE (zotero_library_type, zotero_library_id, zotero_key)
);

CREATE INDEX IF NOT EXISTS idx_sources_withdrawn ON sources(withdrawn_at);
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
    revived INTEGER NOT NULL DEFAULT 0,
    withdrawn INTEGER NOT NULL DEFAULT 0,
    complete INTEGER NOT NULL DEFAULT 1,
    error TEXT
);
"""


class SourceIdentityCollision(RuntimeError):
    """Two distinct Zotero bindings produced the same `airl_id` — finding L2."""


class Database:
    def __init__(self, path: Path):
        self.path = Path(path)

    def connect(self) -> sqlite3.Connection:
        """Open a configured connection. **The caller must close it.**

        Kept public because tests and `scripts/acceptance_v0.py` open their own
        read-only connections. Everything inside this module goes through
        `session()` instead, which is the part that was missing.
        """
        self.path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA busy_timeout=5000")
        return connection

    @contextmanager
    def session(self) -> Iterator[sqlite3.Connection]:
        """A transaction that is also closed at the end of it — finding M8.

        `with sqlite3.connect(...) as connection:` reads like a resource
        context manager and is not one. It commits on success and rolls back on
        an exception, and it never closes anything. Every call in this module
        used that form, so every request leaked a connection and a file handle
        until garbage collection happened to run — invisible on a 33-source
        library and a genuine descriptor exhaustion at any real size.

        Rollback on failure is preserved explicitly rather than inherited, so
        the behaviour that *was* correct does not quietly change while fixing
        the part that was not.
        """
        connection = self.connect()
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    SCHEMA_VERSION = "2"

    def initialize(self) -> None:
        with self.session() as connection:
            connection.executescript(SCHEMA)
            # v1 → v2 adds withdrawn_at. `schema_meta.schema_version` was
            # written and never read, so there was no migration mechanism at
            # all; this is the smallest one that works and it is idempotent.
            columns = {row["name"] for row in
                       connection.execute("PRAGMA table_info(sources)")}
            if "withdrawn_at" not in columns:
                connection.execute("ALTER TABLE sources ADD COLUMN withdrawn_at TEXT")
            run_columns = {row["name"] for row in
                           connection.execute("PRAGMA table_info(sync_runs)")}
            for name, ddl in (("revived", "INTEGER NOT NULL DEFAULT 0"),
                              ("withdrawn", "INTEGER NOT NULL DEFAULT 0"),
                              ("complete", "INTEGER NOT NULL DEFAULT 1")):
                if name not in run_columns:
                    connection.execute(
                        f"ALTER TABLE sync_runs ADD COLUMN {name} {ddl}")
            connection.execute(
                "INSERT OR REPLACE INTO schema_meta(key, value) VALUES (?, ?)",
                ("schema_version", self.SCHEMA_VERSION),
            )

    def upsert_sources(
        self, sources: Iterable[tuple[SourceRecord, dict[str, Any]]]
    ) -> dict[str, int]:
        counts = {"inserted": 0, "updated": 0, "unchanged": 0, "revived": 0}
        seen_keys: list[str] = []
        with self.session() as connection:
            for source, raw in sources:
                existing = connection.execute(
                    """
                    SELECT airl_id, content_hash, zotero_version, withdrawn_at FROM sources
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
                seen_keys.append(source.zotero_key)
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
                    # Finding L2. `airl_id` is a 64-bit truncated SHA-256 of the
                    # Zotero binding. A collision would mean two different
                    # sources sharing one identity, and because `airl_id` is the
                    # primary key the INSERT would fail with a constraint error
                    # naming neither source — or, worse, an upsert keyed on
                    # `airl_id` would silently merge them.
                    #
                    # 64 bits is fine at this scale and the point is not to
                    # widen it: it is that a collision must be *detected* rather
                    # than discovered later as two merged bibliographies. The
                    # check costs one indexed lookup per insert.
                    clash = connection.execute(
                        "SELECT zotero_key, zotero_library_id FROM sources "
                        "WHERE airl_id = ?", (source.airl_id,)
                    ).fetchone()
                    if clash is not None:
                        raise SourceIdentityCollision(
                            f"{source.airl_id} already binds "
                            f"{clash['zotero_library_id']}:{clash['zotero_key']}; "
                            f"refusing to bind "
                            f"{source.zotero_library_id}:{source.zotero_key} to "
                            f"the same identity. The identifier is a 64-bit "
                            f"truncation and this is what a collision looks like")
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
                elif existing["withdrawn_at"] is not None:
                    # It came back. A revived source keeps its airl_id — the
                    # identity was always derived from the Zotero binding, so
                    # minting a new one here would break every reference made
                    # while it was withdrawn.
                    connection.execute(
                        "UPDATE sources SET withdrawn_at = NULL, content_hash = ?, "
                        "synced_at = ?, zotero_version = ? WHERE airl_id = ?",
                        (source.content_hash, source.synced_at.isoformat(),
                         source.zotero_version, existing["airl_id"]),
                    )
                    counts["revived"] += 1
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
        counts["seen_keys"] = seen_keys
        return counts

    def reconcile_deletions(self, present_keys: Iterable[str], *,
                            library_type: str, library_id: str) -> list[str]:
        """Withdraw sources no longer present upstream — finding H2.

        A tombstone rather than a delete. This registry is the system of record
        for source identity, and an identity that silently disappears cannot
        afterwards be told apart from one that never existed — which is exactly
        the question an audit asks about a citation that no longer resolves.

        Called only from a **complete** ingest. A partial fetch would make every
        unfetched source look deleted, which is why `ingest_zotero` reconciles
        only when it has walked the whole library. That coupling is the reason
        finding H1 said to fix M9 first: pagination without it turns a masked
        truncation into active data loss.
        """
        present = set(present_keys)
        withdrawn_at = datetime.now(timezone.utc).isoformat()
        withdrawn: list[str] = []
        with self.session() as connection:
            rows = connection.execute(
                "SELECT airl_id, zotero_key FROM sources "
                "WHERE zotero_library_type = ? AND zotero_library_id = ? "
                "AND withdrawn_at IS NULL",
                (library_type, library_id),
            ).fetchall()
            for row in rows:
                if row["zotero_key"] in present:
                    continue
                connection.execute(
                    "UPDATE sources SET withdrawn_at = ? WHERE airl_id = ?",
                    (withdrawn_at, row["airl_id"]),
                )
                withdrawn.append(str(row["airl_id"]))
        return withdrawn

    def list_sources(self, limit: int | None = 100, offset: int = 0,
                     include_withdrawn: bool = False) -> list[SourceRecord]:
        """Live sources, newest first. `limit=None` means every one of them.

        The default stays at 100 for the HTTP surface. The projection passes
        `None`, because a projection that reads *most* sources deletes the rest
        as stale — finding M9, where the cap was 10,000 and silent.
        """
        clause = "" if include_withdrawn else "WHERE withdrawn_at IS NULL"
        if limit is None:
            sql = f"SELECT * FROM sources {clause} ORDER BY synced_at DESC"
            params: tuple = ()
        else:
            sql = (f"SELECT * FROM sources {clause} "
                   f"ORDER BY synced_at DESC LIMIT ? OFFSET ?")
            params = (limit, offset)
        with self.session() as connection:
            rows = connection.execute(sql, params).fetchall()
        return [self._row_to_source(row) for row in rows]

    def get_source(self, airl_id: str) -> SourceRecord | None:
        with self.session() as connection:
            row = connection.execute(
                "SELECT * FROM sources WHERE airl_id = ?", (airl_id,)
            ).fetchone()
        return self._row_to_source(row) if row is not None else None

    def search_sources(self, query: str, limit: int = 25) -> list[SourceRecord]:
        escaped = query.casefold().replace("\\", "\\\\")
        escaped = escaped.replace("%", "\\%").replace("_", "\\_")
        pattern = f"%{escaped}%"
        with self.session() as connection:
            rows = connection.execute(
                """
                SELECT * FROM sources
                WHERE withdrawn_at IS NULL AND (lower(title) LIKE ? ESCAPE '\\'
                   OR lower(doi) LIKE ? ESCAPE '\\'
                   OR lower(abstract_note) LIKE ? ESCAPE '\\'
                   OR lower(creators_json) LIKE ? ESCAPE '\\'
                   OR lower(tags_json) LIKE ? ESCAPE '\\')
                ORDER BY title COLLATE NOCASE, zotero_key
                LIMIT ?
                """,
                (pattern, pattern, pattern, pattern, pattern, limit),
            ).fetchall()
        return [self._row_to_source(row) for row in rows]

    def list_category_counts(self) -> list[tuple[str, int]]:
        with self.session() as connection:
            rows = connection.execute(
                """
                SELECT item_type, COUNT(*) AS source_count
                FROM sources
                WHERE withdrawn_at IS NULL
                GROUP BY item_type
                ORDER BY source_count DESC, item_type
                """
            ).fetchall()
        return [(str(row["item_type"]), int(row["source_count"])) for row in rows]

    def count_sources(self, include_withdrawn: bool = False) -> int:
        clause = "" if include_withdrawn else "WHERE withdrawn_at IS NULL"
        with self.session() as connection:
            row = connection.execute(
                f"SELECT COUNT(*) AS count FROM sources {clause}").fetchone()
        return int(row["count"])

    def start_sync(self) -> int:
        now = datetime.now(timezone.utc).isoformat()
        with self.session() as connection:
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
        revived: int = 0,
        withdrawn: int = 0,
        complete: bool = True,
        error: str | None = None,
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self.session() as connection:
            connection.execute(
                """
                UPDATE sync_runs SET
                    completed_at = ?, status = ?, fetched = ?, inserted = ?,
                    updated = ?, unchanged = ?, skipped = ?, revived = ?,
                    withdrawn = ?, complete = ?, error = ?
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
                    revived,
                    withdrawn,
                    int(complete),
                    error,
                    run_id,
                ),
            )

    def record_divergence(self, *, stage: str, detail: str) -> int:
        """Record that one half of a sync succeeded and the other did not.

        Finding M6. The ingest and the projection write to different stores and
        cannot be made atomic; what was missing was any record that they had
        come apart. `sync_runs` held only the ingest counters, so a registry that
        had advanced past a stale vault looked exactly like a healthy system.
        """
        now = datetime.now(timezone.utc).isoformat()
        with self.session() as connection:
            cursor = connection.execute(
                "INSERT INTO sync_runs(started_at, completed_at, status, error) "
                "VALUES (?, ?, ?, ?)",
                (now, now, "DIVERGED", f"{stage}: {detail}"),
            )
            return int(cursor.lastrowid)

    def last_divergence(self) -> sqlite3.Row | None:
        with self.session() as connection:
            return connection.execute(
                "SELECT * FROM sync_runs WHERE status = 'DIVERGED' "
                "ORDER BY id DESC LIMIT 1"
            ).fetchone()

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
            withdrawn_at=row["withdrawn_at"] if "withdrawn_at" in row.keys() else None,
        )
