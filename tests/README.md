# Tests

| Field | Value |
|---|---|
| Document type | Index — what is tested, and what is deliberately not |
| Scope | The 25 tests that run today |
| Sibling documents | `../scripts/README.md` · `../docs/OPERATIONS.md` |
| Status | `WORKING` — 25 passing; coverage is narrow and honestly so |
| Date | 2026-08-22 |

**In one paragraph.** Twenty-five tests cover the components that exist: the
bridge's database, projection, API and MCP boundary, the shared contract core,
and the evidence attestation tooling. They do not cover the target architecture,
because it is not built, and they do not cover agent behaviour, because no
behaviour-testing runtime exists. A green suite here means the implemented slice
behaves; it does not mean the framework works.

| File | Covers | Notable property |
|---|---|---|
| `test_database.py` | canonical registry, idempotent upsert, stable identity | re-running a sync must not duplicate a source |
| `test_obsidian.py` | projection writing, manifest-owned deletion, path containment | the projector deletes only files it recorded creating |
| `test_api.py` | the FastAPI surface | loopback-only binding |
| `test_mcp_server.py` | the MCP tool set | asserts **exactly five** read-only tools |
| `test_contracts.py` | identity, manifest, event envelope, schema registry | rejects malformed digests and duplicate schema registration |
| `test_evidence_manifest.py` | issuing and verifying attestations | **the tamper cases are the point**: an altered payload, an altered covered file and a forged signature each fail |

## What is not tested

- **The read-only Zotero boundary behaviourally.** It is visible in the code and
  asserted nowhere — finding **H3**. A mock transport that raises on any
  non-`GET` would close it cheaply.
- **Agent behaviour.** No skill has a baseline test; the runtime for one does not
  exist. This is the largest untested claim in the repository.
- **Everything designed and unbuilt** — Temporal, the ledgers, the brokers, the
  gates.

```bash
uv run pytest          # all 25
uv run pytest -k mcp   # one area
```
