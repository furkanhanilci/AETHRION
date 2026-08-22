# Findings Register

| Field | Value |
|---|---|
| Document type | Register — every audit finding and its current state |
| Scope | Findings raised against this repository, from any source |
| Sibling documents | `review/` holds the frozen reports that raised them · `STATUS.md` is generated |
| Status | `WORKING` — maintained by hand; each state below was re-checked against the working tree |
| Date | 2026-08-22 |

**In one paragraph.** The 2026-08-21 review raised twenty-four findings. Eight of
them were tracked in prose across `README.md` and `AGENTS.md`; the other sixteen
had no home at all — nine survived only as a sentence in a module docstring, and
seven existed nowhere outside a frozen report. A finding whose only record is a
docstring disappears the day that file is refactored, and several of the sixteen
had in fact been fixed with nothing saying so. This register exists so that the
state of a finding is written down once, in one place, rather than inferred.

> **This file is not generated.** A finding's state is a judgement, not a
> measurement, so no script can derive it. What *is* mechanical is the evidence
> column: every "closed" row below names a command or a file you can check.

---

## 1. Open

These are live. Nothing below is scheduled; the packages named are where the
work belongs, not a commitment to a date.

| # | Finding | Where | Why it is still open |
|---|---|---|---|
| **H1** | Zotero ingest is capped at 100 records — no pagination, no `Total-Results`, no `since=` | `src/airl_bridge/zotero.py` | Fix **M9 first.** Pagination without it turns a masked truncation into active data loss |
| **H2** | A record deleted in Zotero persists in the registry and in Obsidian forever | `src/airl_bridge/database.py` | No tombstone path and the `/deleted` endpoint is never read |
| **H3** | The read-only boundary has no behavioural test | `src/airl_bridge/zotero.py` · `tests/test_api.py` | `zotero_write_enabled` is a hard-coded constant, so the artifacts that appear to verify it test `False is False`. The fix is a `MockTransport` that raises on any non-`GET`, driven through the whole sync flow |
| **H4** | The contract core has no production consumer, and contradicts the live system | `src/airl_framework/contracts.py` | Nothing in `src/airl_bridge` imports it; `ArtifactManifest` requires a bare 64-character digest while the bridge produces `sha256:<hex>`. Its only importer is a test. Binding it is WP-020 |
| **H5** | No continuous integration | `deploy/bvc-01-verify.yml` | The workflow is written and has never run: activation needs a workflow-scoped token. BVC-01 is a temporary control and does **not** close H5, which is the absence of the WP-024 CI platform |
| **M1** | Mutating endpoints are unauthenticated; no `Host` validation | `src/airl_bridge/main.py` | Loopback narrows this without closing it. Two low-cost fixes: a trusted-host middleware, and an `X-AIRL-Token` header on the mutating endpoints — a custom header alone forces a preflight and closes CSRF |
| **M6** | No transaction boundary or compensation in `sync` | `src/airl_bridge/service.py` | The ingest commits before the projection runs; if the projection fails the registry has advanced and nothing records the divergence |
| **M7** | The projection has no dry-run and does not refuse a populated directory | `src/airl_bridge/obsidian.py` | A path projected once is irreversibly taken under management. Partially narrowed by **I4** below, which stops the run when the manifest is unreadable — but adoption of a human folder is still silent |
| **M8** | SQLite connections are never closed | `src/airl_bridge/database.py` | `with self.connect()` is a *transaction* context manager; it does not close. Every request leaks one until garbage collection |
| **M9** | Silent truncation at 10,000 rows in the projection | `src/airl_bridge/service.py` | Above that the projection would not see some sources and `_remove_stale` would delete their files as stale. The 100-record ingest cap masks this today |
| **L2** | `airl_id` is a 64-bit truncated hash with no collision handling | `src/airl_bridge/zotero.py` | Acceptable at 33 sources; it is not a property to discover at scale |
| **L4** | No test coverage of the security and error paths | `tests/test_api.py` | None of the three `POST` endpoints, the 503 and 422 handlers, the loopback refusal, the path-traversal refusal or `library_type` validation is exercised — which contradicts the plan's own Definition of Done |

## 2. Closed

| # | Finding | Closed by | Check it |
|---|---|---|---|
| **C1** | Evidence-chain bootstrap deadlock: no package could become `ACCEPTED` | WP-000 — the interim evidence policy, implemented and issued | `uv run python scripts/evidence_manifest.py verify --manifest delivery/WP-000/evidence.dsse.json --tamper-demo` |
| **C2** | The plan assumed 73 owners and 114 verifiers; the organisation is one person | ADR-001 — R1 solo · R2 under a declared partial profile · **R3 `BLOCKED`**, declared rather than waived | `docs/architecture/ADR-001_solo_operator_independence.md` |
| **C3** | WP-022 was declared `TECH_COMPLETE` with its deliverable absent | The claim was withdrawn; only WP-000 is `TECH_COMPLETE` | `python3 scripts/progress.py show WP-022` |
| **M2** | `mcp_smoke.py` asserted nothing and exited 0 under all conditions | Rewritten: asserts the exact five-tool set, exits 1 with the Bridge down | `uv run python scripts/mcp_smoke.py` |
| **M3** | `acceptance_v0.py` depended on the operator's personal library | Rewritten as 11 data-independent structural checks | `uv run python scripts/acceptance_v0.py` |
| **M4** | The plan lived in four physical copies with contradictory authority | One canonical tree under `planning/commissioning/`, hash-sealed; the vault copy is a generated mirror | `(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt)` |
| **M5** | WP↔ACC traceability was inconsistent in 39 of 40 cases | References now resolve in both directions and are checked | `python3 scripts/validate_commissioning_plan.py` |
| **M10** | Documentation drift after renames — prior-project names leaked into the unit descriptions | Units reinstalled | `grep -i silbo deploy/` returns nothing |
| **M11** | The canonical plan tree was not under version control | It is: 222 tracked files | `git ls-files planning/commissioning \| wc -l` |
| **L1** | `.env` and `.env.example` were byte-identical; the example carried real paths | The example carries `<VAULT_ABSOLUTE_PATH>`; `.env` is git-ignored | `grep VAULT_ABSOLUTE_PATH .env.example` |
| **L3** | Category folder names mixed English and Turkish | All twelve are English | `src/airl_bridge/catalog.py` |
| **L5** | A fake `.git`, an empty `.codex` and an empty `.agents` at the root | Removed | `ls -d .codex .agents` fails |

---

## 3. Findings raised by the 2026-08-22 repository inspection

A separate namespace, because the 2026-08-21 audit is frozen evidence and its
`C`/`H`/`M`/`L` identifiers belong to it. All seven were fixed in the same pass
that raised them; each names the test or check that would catch a regression.

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **I1** | `docs/STATUS.md` is a signed subject of the WP-000 attestation and carried a timestamp refreshed on every run, so the session-start command invalidated the session-end verification **deterministically** — teaching the operator to re-sign without reading | `write_status.py` rewrites the page only when a check result changes | Run `write_status.py` twice; the second prints `unchanged` |
| **I2** | An `unchanged` ingest still wrote `synced_at`, which the projection renders as each note's `generated_at` — so a run reporting `unchanged: 33` rewrote 36 vault files every 30 minutes | `database.upsert_sources` no longer writes an unchanged record; only a moved upstream version is reconciled | `tests/test_database.py::test_unchanged_source_is_not_rewritten` |
| **I3** | The two dashboards were generated *outside* the projection manifest — files the projector creates and can never clean up | Dashboards are written before the manifest is sealed and are recorded in it | `tests/test_obsidian.py::test_dashboards_are_recorded_in_the_manifest` |
| **I4** | An unreadable manifest was swallowed (`return 0`) and then overwritten, permanently orphaning every file it listed | `_remove_stale` raises `ProjectionError` instead | `tests/test_obsidian.py::test_unreadable_manifest_refuses_rather_than_orphaning_files` |
| **I5** | `pydantic` was imported directly by `airl_bridge.models` and declared nowhere — it arrived only transitively through FastAPI | Declared in `pyproject.toml` | — |
| **I6** | Six counts were stale across four documents while `check_doc_consistency.py` reported that documents agree: the test count in nine places, the bundle size in three, the attestation's subject count, and the figure count in the runbook. Every one was a number nobody had written a rule for | Fifteen rules added; `tests`, `bundle_checks` and `attestation_subjects` are now derived | `python3 scripts/check_doc_consistency.py` |
| **I7** | `docs/figures/aethrion_verification.svg` drew ten rows for a twelve-check bundle and named `seal_commissioning_plan.py`, a script that does not exist | `fig_verification.py` derives its rows from `write_status.CHECKS` and **raises** if the bundle grows a check it has no prose for | `python3 scripts/make_figures.py --check` |

---

## 4. What this register does not do

It does not rank, schedule or assign. It records what is known to be wrong and
whether it still is. Two limits are worth stating plainly:

- **A closed finding is closed against the check named beside it**, not in
  general. `M2` is closed because `mcp_smoke.py` now asserts and can fail — not
  because the MCP boundary is proven correct.
- **The list is only as complete as the reviews that produced it.** An external
  reader once found two stale claims in a corpus whose status page reported
  none, and this inspection found seven more. Assume the same is possible now.
