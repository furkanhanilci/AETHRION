# `airl_bridge` — the working vertical slice

| Field | Value |
|---|---|
| Document type | Component reference |
| Scope | The one part of AIRL-OS that exists as running software |
| Sibling documents | `../../docs/ARCHITECTURE_V0.md` · `../../docs/OPERATIONS.md` |
| Status | `WORKING` — verified locally, never independently accepted |
| Date | 2026-08-22 |

**In one paragraph.** Zotero is read, never written; sources are given a stable
AIRL identity in a canonical SQLite registry; that registry is projected into
Obsidian under a manifest that owns its own deletions; and an MCP server exposes
exactly five read-only tools. Every design decision here is about **bounding what
can go wrong**, which is why the module list reads as boundaries rather than
features.

| Module | Responsibility | The boundary it holds |
|---|---|---|
| `zotero.py` | Read-only Zotero local API client | No API key is stored and **no write path exists** |
| `database.py` · `models.py` | Canonical registry, schema, idempotent upsert | A Zotero item is not an AIRL source; identity is minted here |
| `service.py` | Sync orchestration, staleness, projection lifecycle | Ingest is capped at 100 records — finding **H1** |
| `obsidian.py` | Atomic projection writer | **Manifest-owned deletion**: a human's file in a generated folder is not "stale" |
| `catalog.py` | Category taxonomy, duplicate heuristics | Surfaces duplicates; never merges them |
| `mcp_server.py` | Five read-only MCP tools | `sync`, write, delete and merge are **deliberately absent** |
| `main.py` · `cli.py` · `config.py` | FastAPI app, operator CLI, settings | Binds to loopback only |

## Known limitations, in the order they should be fixed

1. **M9 before H1.** Projection enumeration is capped at 10 000 rows. Fixing
   Zotero pagination first would turn a masked truncation into an **active data
   loss path**, because `_remove_stale` would treat unseen sources as removed.
2. **H2** — no deletion reconciliation: a source deleted in Zotero lives on.
3. **H3** — the read-only boundary has no behavioural test.
4. **ACC-44** — `get_source` returns abstract text to a model. Bounded today only
   by the absence of any write-capable tool.
5. **H4** — this package imports nothing from `airl_framework`, and their digest
   formats disagree.
