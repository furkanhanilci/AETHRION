# AI Research Framework

An evidence-centred, auditable operating system for research (AIRL-OS).

Its central thesis: **agents produce, machines verify, humans decide** — and
those three roles are kept structurally separate.

This repository holds the target architecture, the execution discipline, and the
components that actually work today. **A plan is not evidence of
implementation**; the table below separates the two.

| Area | Status | Location |
|---|---|---|
| Literature bridge V0 | ✅ **Working**, locally accepted | `src/airl_bridge/` |
| Zotero → Obsidian projection | ✅ Working, read-only at the Zotero boundary | `src/airl_bridge/obsidian.py` |
| Hermes MCP access | ✅ Working, five read-only tools | `src/airl_bridge/mcp_server.py` |
| Shared contract core | ⚠️ `TECH_COMPLETE` — no production consumer | `src/airl_framework/` |
| Skill registry (49 skills, two families) | ✅ Format-conformant and loadable · 📐 behaviour **not yet tested** | `skills/` |
| Obsidian information architecture | ✅ V0 ready | `vault_baseline/` |
| Target architecture and skill layer | 📐 Designed, awaiting decision | `docs/architecture/` |
| Full commissioning programme | ⬜ Planned, not started | `planning/commissioning/` |
| Interim evidence policy (WP-000) | 📐 Written — unblocks the storage half of C1 | `planning/commissioning/01_GOVERNANCE/` |

## Layout

```
src/          Bridge component and the shared contract core
tests/        Test suite
skills/       49 skills — HOW agents work; engineering + scientific + shared
planning/     WP-000, WP-001..140, ACC-01..40 (hash-sealed canonical plan)
docs/         Architecture, review and operations documents
schemas/      Shared contract schemas
delivery/     Per-package evidence packages
deploy/       systemd unit files
scripts/      Acceptance, smoke, skill-validation and mirror-generation scripts
vault_baseline/  Versioned copy of the Obsidian vault
```

## Where to start

| Question | Document |
|---|---|
| **What is this system?** — explained and diagrammed | [`docs/architecture/AIRL_OS_ARCHITECTURE.md`](docs/architecture/AIRL_OS_ARCHITECTURE.md) |
| What actually exists today? | [`docs/review/`](docs/review/) — evidence-based independent audit |
| **What** should be added to the target architecture? | [`docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md`](docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md) |
| **How** should agents work? | [`docs/architecture/AIRL_OS_SKILL_LAYER.md`](docs/architecture/AIRL_OS_SKILL_LAYER.md) · [`skills/README.md`](skills/README.md) |
| **Who** performs each role — human, model or code? | [`docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md`](docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md) |
| What is **adopted** rather than invented? | [`docs/architecture/AIRL_OS_EXTERNAL_STANDARDS.md`](docs/architecture/AIRL_OS_EXTERNAL_STANDARDS.md) |
| Architecture of the working vertical slice | [`docs/ARCHITECTURE_V0.md`](docs/ARCHITECTURE_V0.md) |
| Day-to-day operation | [`docs/OPERATIONS.md`](docs/OPERATIONS.md) |
| The full programme plan | [`planning/commissioning/README.md`](planning/commissioning/README.md) |

## The working vertical slice: Literature Bridge V0

```text
Zotero Local API (read-only)
        → SQLite canonical source registry
        → Obsidian "70 - Literature Sets/Zotero Sources" projection
        → Hermes MCP (five read-only tools)
```

The service listens on `127.0.0.1` only. It holds no Zotero API key, and the
codebase contains no Zotero write operation.

### Install

```bash
cd /home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK
uv sync --extra dev
cp .env.example .env      # then fill in your own paths
```

### Enable the Zotero Local API

1. Start Zotero
2. **Settings → Advanced → General**
3. Enable **Allow other applications on this computer to communicate with Zotero**
4. Keep port `23119` local — do not forward or expose it

```bash
uv run airl-bridge doctor
```

### Run

```bash
uv run airl-bridge serve

systemctl --user status airl-bridge.service
systemctl --user status airl-bridge-sync.timer
journalctl --user -u airl-bridge.service -n 50
```

A user timer runs the same local synchronisation every 30 minutes.

Local endpoints: [`/health`](http://127.0.0.1:8765/health) ·
[`/ready`](http://127.0.0.1:8765/ready) · [`/docs`](http://127.0.0.1:8765/docs)

### First synchronisation

```bash
curl -X POST 'http://127.0.0.1:8765/v1/sync?limit=100'
curl 'http://127.0.0.1:8765/v1/sources?limit=10'

# or without starting the server
uv run airl-bridge sync --limit 100
```

Repeated synchronisation is idempotent for the same Zotero library and item key.
Zotero-derived files live under the automatically managed `Zotero Sources`
branch and are regenerated from the canonical registry. Human synthesis stays in
`20 - Source Notes`; curated sets stay at the root of `70 - Literature Sets`.

> ⚠️ **Known limitation:** ingest is hard-capped at 100 records; there is no
> pagination and no `since=` incremental sync. Once the library exceeds 100
> sources, synchronisation silently becomes partial. See finding **H1** in the
> audit report.

### Verify

```bash
uv run pytest                          # 20 tests
uv run python scripts/mcp_smoke.py     # asserts the five-tool boundary; exits 1 on failure
uv run python scripts/acceptance_v0.py # data-independent structural acceptance
python3 scripts/validate_skills.py     # Agent Skills format + AIRL metadata contract
(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt)
```

All five run by hand. **There is no CI** — see finding **H5**, and
[`docs/OPERATIONS.md`](docs/OPERATIONS.md) for the full verification bundle.

## Hermes MCP access

Hermes starts the `airl-bridge-mcp` server over stdio and sees exactly five
read-only tools: status, source search, source detail, category counts, and
possible-duplicate reporting. No synchronisation, write, delete or Zotero
mutation tool is exposed. The Hermes configuration pins an explicit five-tool
include list; MCP prompt and resource capabilities are disabled.

## Status semantics

`WORKING` means a component has been verified locally.
`ACCEPTED` means an independent verifier accepted its evidence package.

**No work package is currently `ACCEPTED`.** That is not an oversight — the
mechanisms required to reach that state (signed evidence manifests, an immutable
store, an independent verifier) do not yet exist. See finding **C1** in the audit
report.

[**WP-000**](planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md)
now removes the *storage* half of that blocker by expressing the
`EvidenceManifest` as a signed in-toto attestation in a public transparency log,
rather than waiting for WP-026. The *independence* half — finding **C2**, who may
verify in a one-person operation — remains open, and no standard resolves it.

## Verification

```
20/20 tests pass · plan seal 196/196 OK · service and timer active
MCP smoke: 5 read-only tools, exits 1 when the Bridge is down
Acceptance: 11 structural checks pass, data-independent
Skills: 49/49 conform to the Agent Skills format and the AIRL metadata contract
Mirror drift: 0 (197 plan files, 58 skill/doc files)
Obsidian baseline and vault identical
```

Every check above is reproducible from a clean checkout with the Bridge running.
None of them runs automatically.
