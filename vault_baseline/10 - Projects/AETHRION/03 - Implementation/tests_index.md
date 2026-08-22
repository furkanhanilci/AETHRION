---
title: "Tests"
type: index
category: implementation
status: WORKING
summary: "Forty-six tests cover the components that exist: the bridge's database, projection, API and MCP boundary, the shared contract core, and the evidence attestation tooling."
source: "tests/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/execution
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `tests/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Tests

| Field | Value |
|---|---|
| Document type | Index — what is tested, and what is deliberately not |
| Scope | The 46 tests that run today |
| Sibling documents | `../scripts/README.md` · `../docs/OPERATIONS.md` |
| Status | `WORKING` — 46 passing; coverage is narrow and honestly so |
| Date | 2026-08-22 |

**In one paragraph.** Forty-six tests cover the components that exist: the
bridge's database, projection, API and MCP boundary, the shared contract core,
and the evidence attestation tooling. They do not cover the target architecture,
because it is not built, and they do not cover agent behaviour, because no
behaviour-testing runtime exists. A green suite here means the implemented slice
behaves; it does not mean the framework works.

| File | Covers | Notable property |
|---|---|---|
| `test_database.py` | canonical registry, idempotent upsert, stable identity | re-running a sync must not duplicate a source, and an `unchanged` record is not written — the counter and the disk must agree |
| `test_obsidian.py` | projection writing, manifest-owned deletion, path containment | the projector deletes only files it recorded creating, records everything it writes, and refuses to run on a manifest it cannot read |
| `test_api.py` | the `GET` half of the FastAPI surface | **no defensive path is covered here** — see below |
| `test_mcp_server.py` | the MCP tool set | asserts **exactly five** read-only tools |
| `test_contracts.py` | identity, manifest, event envelope, schema registry | rejects malformed digests and duplicate schema registration |
| `test_mirrors.py` | the Obsidian mirrors | a mirror writes what changed and **preserves the inode** of everything else — a running editor watches inodes, and a tree that is deleted and recreated breaks every watch it holds | It also refuses to write over a page whose frontmatter says `generated: false`, because a projection may replace its own pages and nobody else's.
| `test_evidence_manifest.py` | issuing and verifying attestations | **the tamper cases are the point**: an altered payload, an altered covered file and a forged signature each fail |

## What is not tested

- **The read-only Zotero boundary behaviourally.** It is visible in the code and
  asserted nowhere — finding **H3**. A mock transport that raises on any
  non-`GET` would close it cheaply. `test_api.py` asserts
  `zotero_write_enabled is False` against a hard-coded constant, which proves
  nothing.
- **Every defensive path in the service** — finding **L4**. None of the three
  `POST` endpoints is exercised, and neither is the `ZoteroUnavailable` → 503
  handler, the `ProjectionError` → 422 handler, the loopback refusal in
  `Settings.from_env`, the path-traversal refusal, or `library_type` validation.
  This row used to read "loopback-only binding" as though it were covered; it is
  not, and `test_api.py`'s own docstring said so.
- **Agent behaviour.** No skill has a baseline test; the runtime for one does not
  exist. This is the largest untested claim in the repository.
- **Everything designed and unbuilt** — Temporal, the ledgers, the brokers, the
  gates.

```bash
uv run pytest          # all 46
uv run pytest -k mcp   # one area
```
