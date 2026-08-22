# AI Research Framework — Independent Audit Report

> **Historical name; current project identity: AETHRION — Agentic Intelligence
> Research Layer.** This report is a **frozen record of what was true on
> 2026-08-21**, and it is deliberately not rebranded: it cites file paths,
> counts and command output as they existed on that date, and rewriting its
> names would make the record disagree with the evidence it reports. Read it as
> history. For the current naming rules see [`../branding.md`](../branding.md);
> for the current state see [`../STATUS.md`](../STATUS.md).

> [!warning] Frozen snapshot — do not update
> This audit describes the repository **as it stood on 2026-08-21**. Its counts
> (130 work packages, 186 files) and its findings are correct **as of that date**
> and are deliberately left unchanged: an audit that is edited to match the
> present is no longer evidence of anything.
>
> Current state, and what has since been remediated, lives in
> [`2026-08-22_remediation_verification.md`](2026-08-22_remediation_verification.md).
> This banner is the single, recorded exception to the no-edit rule.


| Field | Value |
|---|---|
| Report date | 2026-08-21 |
| Last revision | 2026-08-22 (translated to English, expanded, remediation status added) |
| Reviewer | Claude Opus 5 (independent, read-only review) |
| Review root | `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK` |
| Method | Source reading, test execution, live service queries, SQLite queries, hash verification, scripted plan-consistency analysis |
| Files modified during the audit | None (except this report) |
| Commit / push during the audit | None |

> This report treats the instruction in `docs/review/CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md`
> as **input**, not as **authority**. That prompt is itself audited in Section K
> and was found to be inconsistent with the real directory structure.

> **Reading this report a day later.** The audit was performed on 2026-08-21
> against the then-current layout (`airl_bridge_api/` as a subdirectory). On
> 2026-08-22 the repository was flattened, the plan was consolidated into one
> canonical copy, and the whole corpus was rewritten in English. Findings that
> have since been closed are marked **✅ REMEDIATED** with what changed. Findings
> without that marker are still open.

---

## A. Executive summary

### The short answer

You have **a very well written plan** and **a small but genuinely working
vertical slice**. The distance between them is far greater than the
documentation implies.

- Plan: 130 WPs + 40 ACC scenarios, 186 files, ~88,000 words.
- Implementation: **1,509 lines of Python**, 20 tests, 1 SQLite table, 33 records.
- Work packages independently accepted (`ACCEPTED`): **0**.
- And as shown below, **under current conditions it is obliged to stay 0** — this
  is not a question of working speed, it is a structural defect in the plan.

### The verdict

**NOT PRODUCTION-READY.** That is expected, and the documents state it correctly.
It is not the real finding.

**The real finding: the plan as written cannot be *started*.** No package —
including the very first one, WP-001 — can satisfy its Definition of Done in this
organisation on this infrastructure. See findings **C1** and **C2**.

### Status distribution (evidence-based)

| Status | WP (130) | ACC (40) |
|---|---:|---:|
| `IMPLEMENTED` (accepted on independent evidence) | **0** | **0** |
| `PARTIAL` (working code exists, acceptance criteria unmet) | **9** | 0 |
| `CONTRADICTED` (a claim exists with no counterpart, or contradicting one) | **2** | 0 |
| `DOCUMENTED_ONLY` (a plan exists, no working counterpart) | **119** | 40 |
| `MISSING` (plan file absent) | 0 | 0 |
| `BLOCKED` (could not be verified) | 0 | 0 |

The 9 `PARTIAL` packages: WP-011, WP-014, WP-015, WP-020, WP-061, WP-062,
WP-065, WP-073, WP-074.
The 2 `CONTRADICTED` packages: **WP-022** (its deliverable is not in the
repository — finding C3) and **WP-064** (no permission scoping; the entire
personal library is read).

### The three most critical obstacles

1. **Evidence-chain bootstrap deadlock** (C1) — every package's DoD requires a
   "signed `EvidenceManifest` written to the immutable store"; the immutable store
   is WP-026. Even WP-001 has nowhere to write its own evidence, and the plan
   defines no interim evidence exception.
2. **Organisational impossibility** (C2) — the plan assumes 73 distinct owners
   and 114 distinct verifier roles; the actual organisation is one person. The
   "verifier independent of the producer" condition cannot be met **by definition**.
3. **Evidence theatre risk** (H3, M2, M3) — all three artifacts presented as
   "read-only evidence" were in fact testing a hard-coded `False`; the "smoke
   test" exited 0 even on failure; the "acceptance" script depended on the word
   "LiDAR" appearing in the user's personal library.
   ✅ **M2 and M3 are now closed** (2026-08-22): the smoke check asserts and exits
   non-zero, and acceptance is data-independent. **H3 remains open** — the
   read-only claim is now honestly labelled as unproven rather than falsely
   asserted, which is an improvement but not a proof.

### The real vertical slice that can be run safely today

`Zotero Local API (read-only) → SQLite registry → Obsidian projection → Hermes MCP (5 read-only tools)`

This slice genuinely works, is genuinely idempotent and is genuinely local.
**33 sources, 3 categories, 20/20 tests PASS, service and timer active** —
verified. Its limit: the moment the library exceeds 100 sources it begins to sync
**silently incompletely** (finding H1).

---

## B. Repository and environment snapshot

| Field | Value | Note |
|---|---|---|
| Framework root | `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK` | **Not a Git repository at audit time.** `.git`, `.codex`, `.agents` were empty directories |
| Canonical plan tree | `planning/commissioning/` (186 files) | **Not under version control** at audit time |
| Implementation repository | `airl_bridge_api/` | Git repo, branch `main`, HEAD `6c849bd` |
| Remote | `https://github.com/furkanhanilci/AI-Research-Framework.git` | private, default `main` |
| Local vs remote | `0 ahead / 0 behind` — in sync | `origin/main = 6c849bd` |
| Working tree | Clean | `git status --short` empty |
| Tracked files | 434 | 211 of them under `vault_baseline/` |
| Python | 3.11, `.venv` present | managed by `uv` |
| Test result | **20 passed** | `.venv/bin/python -m pytest -q`, exit 0 |
| Bridge service | `active` | `/health` and `/ready` returned 200 |
| Sync timer | `active`, last run 8 minutes earlier | 30-minute period |
| Record count | 33 sources, 25 sync runs | Last 8 runs: `SUCCEEDED`, 33 fetched / 33 unchanged |
| Plan hash verification | **184/184 OK** | `sha256sum -c SHA256SUMS.txt` |
| Vault | `/home/otonom/Documents/Obsidian Vault`, 246 notes | content-identical to the baseline |
| Wikilink integrity | 103 links, **0 broken** | verified by script |
| Markdown links inside the plan | 1011 links, **0 broken** (in all three copies) | verified by script |
| CI | **None** | `.github`, `Makefile`, `ruff`, `mypy`, `pre-commit` — none present |

> ✅ **REMEDIATED (2026-08-22):** the repository was flattened so that the
> framework root **is** the Git root; `planning/commissioning/` is now tracked,
> single-copy and hash-sealed inside it (195 files re-sealed, all OK). CI is still
> absent — see H5.

---

## C. What genuinely works (credit where it is due)

Do not underestimate these; several are rarely done correctly at this scale:

1. **Idempotent upsert.** The insert/update/unchanged distinction via
   `content_hash` comparison is correct, with a UNIQUE constraint on
   `(library_type, library_id, key)`. Tested: `tests/test_database.py:5`.
2. **Stable identity.** `airl_id` is a hash of the Zotero item key binding — the
   identity does not change when the title changes. Tested: `tests/test_zotero.py:9`.
3. **Atomic file writes.** `mkstemp` + `fsync` + `os.replace` — no partially
   written Markdown file can appear (`obsidian.py:253`).
4. **Manifest-owned deletion.** The projection deletes only files registered in
   its own manifest; a human note in the same folder survives. **It has a real
   test**: `tests/test_obsidian.py:72`. This is the single most important defence
   against data loss and it is built correctly.
5. **Path traversal defence.** Escape from the vault is blocked at both the
   config level (`config.py:58`) and the projection level (`obsidian.py:42`, `:124`).
6. **Loopback enforcement.** `config.py:47` — the service refuses to start if
   `AIRL_API_HOST` is set to anything but loopback. A good fail-closed default.
7. **XSS/injection escaping.** Abstracts and titles go through `html.escape`,
   YAML strings through `json.dumps`; there is a test (`tests/test_obsidian.py:5`).
8. **systemd hardening.** `NoNewPrivileges`, `ProtectSystem=strict`,
   `ProtectHome=read-only` plus narrow `ReadWritePaths`. Hardening at this level
   was not expected.
9. **Plan integrity.** The dependency graph over 130 packages is **acyclic**, all
   in topological order (forward dependencies: 0), the CSV matches the file set
   exactly, 1011 internal links resolve, and 184 file hashes verify. That is
   serious work.
10. **Honest status semantics.** `aethrion_current_status_and_roadmap.md`
    §2 explicitly distinguishes `V0 READY ≠ ACCEPTED`. That document is not a
    marketing summary. Keep it that way.

---

## D. Findings

Format: `ID | Severity | Title` → Evidence → Impact → Recommendation.

### C1 — CRITICAL — Evidence-chain bootstrap deadlock: no package can become ACCEPTED

**Evidence:**
- `00_PROGRAM/05_DEFINITION_OF_READY_DONE.md:41` — DoD: *"The evidence manifest is
  signed and written to the immutable store."*
- `01_GOVERNANCE/WP-001_commissioning_charter.md`, mandatory deliverables:
  `- A signed EvidenceManifest` — this line appears in **130/130** WP files.
- `package_dependency_matrix.csv` — the immutable store is **WP-026**, whose
  dependencies run `WP-021;WP-014` → `WP-020` → `WP-011` → `WP-010` → … → `WP-001`.
- No bootstrap or interim evidence exception is defined in
  `00_PLANIN_KULLANIMI.md`, `06_KANIT_VE_KABUL_STRATEJISI.md` or
  `05_DEFINITION_OF_READY_DONE.md` (grep finds only `TemporaryControlRecord`,
  which is for manual controls, not for an evidence store).

**Impact:** Although the dependency graph is acyclic, the **evidence chain is
cyclic**. To accept WP-001 you must write a signed evidence manifest into the
immutable store; the immutable store is WP-026, five levels downstream. The
programme technically halts at step 1.

**Recommendation:** Define a **WP-000 Interim Evidence Policy** ahead of WP-001:
- An interim evidence store: `delivery/WP-xxx/` + `evidence-manifest.json`
  (file name, sha256, producing command, target Git SHA, timestamp).
- An interim mechanism standing in for a signature: a Git commit SHA plus
  `git tag -s`, or at minimum an append-only `EVIDENCE_LEDGER.md`.
- Write down how that interim mechanism migrates once WP-026 exists, and its
  expiry criterion (the plan's own `TemporaryControlRecord` format fits).

> **Status: OPEN.** WP-000 is referenced in the revised program documents and in
> WP-139 (evidence timestamping gives it an external time anchor without
> infrastructure), but the package itself has not been written.

---

### C2 — CRITICAL — The plan assumes 73 owners and 114 verifiers; the organisation is one person

**Evidence:**
- Analysis of `package_dependency_matrix.csv`: **73 distinct `owner` values** and
  **114 distinct `verifier` values** across 130 rows.
- `05_DEFINITION_OF_READY_DONE.md:35` — *"The verifier has performed verification
  independently of the producer."*
- `05_DEFINITION_OF_READY_DONE.md:52` (evidence that is not accepted) — *"An
  agent's or implementer's free-text claim of success"*, *"An independence claim
  from a reviewer who has seen the producer's trace"*.
- Reality: every vault note carries `owner: otonom`; `CODEOWNERS` contained a
  single comment line and defined no owner at all.
- Effort distribution: **83 packages "L"**, 42 "M", 5 "S". No calendar exists
  (`08_KAPASITE_VE_TAHMIN.md`: *"there is no fixed calendar"*).

**Impact:** Running 83 "L"-effort packages with a separate assurance pool and an
independent verifier is the job description of an institutional programme. In a
one-person organisation the independence condition cannot be met **by
definition** — the "sealed Fable review" approach used on the SILBO side is the
only realistic substitute, and the plan defines that substitute nowhere.

**Recommendation:** Choose one of two options **explicitly** and write it into
`00_PROGRAM/`:
- **(a) Reduce the scope:** cut 130 packages down to an "AIRL-OS Personal Edition"
  of ~20–25 packages that one person can actually run. Mark the rest `DEFERRED`.
- **(b) Redefine the independence model:** make the SILBO sealed-review plus
  exact-quorum protocol the framework's official verifier mechanism (that becomes
  the real implementation of WP-007). Write down the definition: different model
  family + sealed context + exact target SHA = "independence".

Until that decision is made, every line of code written will be unacceptable code.

> **Note on a self-correction.** The original phrasing of this finding overstated
> the gap: the plan's `04_ROL_VE_SORUMLULUK_MATRISI` **does** address small teams
> and role combination. The precise problem is narrower and worse: role
> combination is permitted, but **R3 remains permanently BLOCKED**, and no R3
> classification path is defined for a solo operator. The revised
> `04_role_and_responsibility_matrix.md` now states this consequence explicitly.

---

### C3 — CRITICAL — WP-022 was declared "TECH_COMPLETE"; its deliverable is not in the repository

**Evidence:**
- `implementation_log.md:164-166` — *"Initial repository skeleton areas added for
  WP-022: `schemas/`, `policy/`, `infra/`, `services/`, `workflows/`, `agents/`,
  `delivery/` and `docs/architecture/`."*
- `ls -A`: `services/`, `workflows/`, `agents/`, `infra/`, `policy/`,
  `delivery/WP-011/`, `delivery/WP-014/`, `delivery/WP-015/`, `delivery/WP-020/`
  — **all empty**.
- `git ls-files | grep -E '^(services|workflows|agents|infra|policy|delivery)/'`
  → **no output**. Git does not track empty directories.
- Therefore **none** of these directories exists in the
  `github.com/furkanhanilci/AI-Research-Framework` repository.
- The supporting deliverables were empty too:
  - `docs/architecture/FOUNDATION.md` → one line: `# Foundation repository skeleton`
  - `schemas/README.md` → one line: `# Shared contract schemas`
  - `dependency-rules.txt` → one unparseable line of prose
  - `CODEOWNERS` → one comment line, zero rules. **It enforced nothing.**

**Impact:** This is exactly the evidence type the plan itself forbids
(`05_DEFINITION_OF_READY_DONE.md:52`: *"an agent's free-text claim of success"*).
Work recorded as `TECH_COMPLETE` in the implementation log does not exist in the
remote repository at all.

**Recommendation:** Immediately downgrade WP-022's status in
`implementation_log.md` to `NOT_STARTED`. On the second attempt: a `.gitkeep` plus
a real boundary file in every directory (for example a working OPA/rego policy or
at least one JSON schema under `policy/`), real rules in `CODEOWNERS`, and an
import-linter/`tach` configuration **enforced in CI** in place of
`dependency-rules.txt`.

> ✅ **PARTIALLY REMEDIATED (2026-08-22):** `CODEOWNERS` and `dependency-rules.txt`
> now carry real, parseable content, and `docs/architecture/FOUNDATION.md` — one
> of the one-line stubs cited above — is now a real document naming what exists,
> what does not, and the three gaps that block the foundation layer. The empty
> directories were removed rather than filled, and WP-022 remains un-started.
> **CI enforcement is still missing**, so the deliverable is still not verifiable
> mechanically.

---

### H1 — HIGH — Zotero ingest is hard-capped at 100 records; no pagination, no incremental sync

**Evidence:**
- `src/airl_bridge/zotero.py:41` — `safe_limit = max(1, min(limit, 100))`
- `src/airl_bridge/main.py:126,136` — `Query(default=100, ge=1, le=100)`
- `src/airl_bridge/cli.py:68` — `choices=range(1, 101)`
- `deploy/airl-bridge-sync.service` — `POST /v1/sync?limit=100`
- `fetch_top_items` makes a single `GET /items/top` call; there is **no** `start`
  parameter, no `Total-Results` header reading and no `since=` version parameter.

**Impact:** The moment the library exceeds 100 sources, the sync begins running
**silently incomplete**. No error, no warning; `SUCCEEDED` is written to the
`sync_runs` table. Worse: because `project_obsidian()` projects the whole
database, sources that never entered because of the 100 cap never appear in
Obsidian either. With 33 sources this is invisible; on the day you grow it becomes
a data gap that is very hard to notice.

**Recommendation (priority 1):**
- A pagination loop over `start`/`limit` inside `fetch_top_items`; read the
  `Total-Results` header and verify full coverage.
- Add `library_version` (the Zotero `Last-Modified-Version`) to `sync_runs` and
  use `?since=` on the next call (this is also the core of WP-067).
- Mark the run `PARTIAL`, not `SUCCEEDED`, whenever `fetched < total`.

> **Status: OPEN.** Documented as a known limitation in `README.md`.

---

### H2 — HIGH — A record deleted in Zotero stays in the registry and in Obsidian forever

**Evidence:**
- `src/airl_bridge/database.py` — not a single query containing `DELETE` or a
  tombstone.
- `src/airl_bridge/service.py:41` — `project_obsidian()` projects the entire DB.
- `obsidian.py:112` `_remove_stale()` deletes only files that "no longer enter the
  projection from the DB"; since the DB never shrinks, this path is never
  triggered in practice.
- The Zotero `/deleted` endpoint is never called.

**Impact:** When the user deletes a source from Zotero or removes it from the
library, the source remains in the canonical registry and in Obsidian. Over time
the vault accumulates ghost sources. This directly violates the plan's invariant 6
("the derived graph can be rebuilt from scratch from canonical records"): the
canonical record is already wrong.

**Recommendation:** Along with `since=` sync, add a read of Zotero
`/deleted?since=N`; do **not** delete the records — tombstone them with
`status = WITHDRAWN` + `withdrawn_at` (WP-011-T05 already asks for this) and drop
them from the projection.

> **Status: OPEN.**

---

### H3 — HIGH — `zotero_write_enabled` is a constant, not a measured control; three "evidence" artifacts test it

**Evidence:**
- `src/airl_bridge/models.py:65` — `zotero_write_enabled: bool = False` (default)
- `src/airl_bridge/main.py:62-68` — `HealthResponse(...)` **never sets** the field,
  so it is always the default `False`.
- `src/airl_bridge/mcp_server.py:78` — `health.get("zotero_write_enabled", False)`
  — `False` even when the field is absent.
- `src/airl_bridge/cli.py:34` — `"zotero_write_enabled": False` — a flat constant.
- And the three artifacts that "verify" it:
  - `tests/test_api.py:26` — `assert payload["zotero_write_enabled"] is False`
  - `scripts/acceptance_v0.py:41` — `require(health["zotero_write_enabled"] is False, ...)`
  - `scripts/acceptance_v0.py:77` — prints the same constant `False` to its output.

**Impact:** This is a tautology. `False is False` is being tested. If the code
gained an `httpx.post` call tomorrow, all three checks would stay green. The
framework's strongest security claim — "nothing is written to Zotero", stated in
`README.md:31`, `ARCHITECTURE_V0.md` and the status document — has **zero test
coverage**.

**Recommendation:**
- Remove `HealthResponse.zotero_write_enabled`, or bind it to a genuinely computed
  value.
- Write a **behavioural test** instead: give `ZoteroClient` a `MockTransport` whose
  handler raises `AssertionError` on any method other than `GET`, and run the whole
  `sync` flow through it. That actually proves the claim.
- Add a static check in CI: fail the build if the regex `post|put|patch|delete`
  matches inside `src/airl_bridge/zotero.py`.

> **Status: OPEN.** This is the single highest-value fix in the list: it converts
> the project's central security claim from an assertion into evidence.

---

### H4 — HIGH — The `airl_framework` contract core has zero production consumers and contradicts the live system

**Evidence:**
- `grep -rn airl_framework` → only `pyproject.toml:28`, `tests/test_contracts.py:3`
  and two vault notes. **Not a single import inside `src/airl_bridge/`.**
- The bridge produces no `EventEnvelope`; there is no event bus in the system.
- A direct contradiction: `contracts.py:11` → `_HASH_RE = ^[0-9a-f]{64}$` (bare
  digest), while `zotero.py:104` → `content_hash = "sha256:" + hexdigest`
  (prefixed). The existing canonical record therefore **violates the newly written
  `ArtifactManifest` contract on the day it was born**.
- `SourceRecord.airl_id` is never validated through `Identity`.
- `SchemaRegistry` is a `dict` — not persistent, does not accept JSON Schema
  (it stores `Mapping[str, Any]` and never validates), and is not enforced by CI.
  WP-020's expected outcome was *"enforced by CI"*.

**Impact:** `implementation_log.md` Step 001 declares WP-011/014/015/020
`TECH_COMPLETE`. In reality: a 170-line library bound to nothing, incompatible
with the existing data model. Its tests pass, but this is precisely what
`05_DEFINITION_OF_READY_DONE.md:56` forbids: *"the tests pass but there is no
requirement"*.

**Recommendation:** **Bind what exists** before writing new contracts:
1. Reduce `content_hash` to a single definition (suggestion: bare 64-hex plus a
   separate `hash_algo` field). Write the migration script and its reversal.
2. Route `SourceRecord.airl_id` generation through `Identity`, giving the contract
   at least one real consumer.
3. Turn `SchemaRegistry` into something that loads `schemas/*.json` and genuinely
   validates with `jsonschema`; otherwise WP-020 is `MISSING`.

> **Status: OPEN.**

---

### H5 — HIGH — There is no CI; the acceptance criteria of WP-024 and WP-020 are structurally impossible

**Evidence:** `.github/`, `.gitlab-ci.yml`, `Makefile`, `ruff.toml`, `mypy.ini`,
`.pre-commit-config.yaml` — **none present**. `pyproject.toml` contains only
`[tool.hatch...]` and `[tool.pytest...]`; no lint, type or format configuration.

**Impact:** Tests run by hand only. `05_DEFINITION_OF_READY_DONE.md:24` ("unit and
package-level integration tests have run") will rest on a manual declaration for
every package — meaning the C2/C3 problem repeats in every package. WP-020's goal
of "producer/consumer compatibility enforced by CI" cannot be met by definition
when there is no CI to enforce it.

**Recommendation (priority 2, immediately after C1):** a single GitHub Actions
workflow: `uv sync` → `ruff check` → `pytest -q` → the H3 read-only static check →
`sha256sum -c` plan integrity check. That one file closes three separate findings
and automates evidence production.

> **Status: OPEN.** This remains the highest-leverage implementable step.

---

### M1 — MEDIUM — Unauthenticated mutating endpoints and no Host header validation

**Evidence:** `src/airl_bridge/main.py:124-138` — `POST /v1/ingest/zotero`,
`POST /v1/project/obsidian`, `POST /v1/sync`. No auth, no token, no CSRF
protection. `create_app` installs **no middleware at all** — neither
`CORSMiddleware` nor `TrustedHostMiddleware`.

**Impact (real despite loopback binding):**
- **CSRF:** any page in the browser can send a preflight-free "simple request"
  with `fetch('http://127.0.0.1:8765/v1/sync?limit=100', {method:'POST', mode:'no-cors'})`.
  It cannot read the response, but **the side effect happens**: the sync runs and
  the vault's `Zotero Sources` branch is rewritten.
- **DNS rebinding:** because the `Host` header is not validated, an attacker who
  rebinds their domain to 127.0.0.1 is treated as same-origin and can read **the
  entire literature registry** through `GET /v1/sources`.
- Every local process on the machine has the same privileges.

**Recommendation:** Low cost, high impact:
- `TrustedHostMiddleware(allowed_hosts=["127.0.0.1", "localhost", "127.0.0.1:8765"])`
- An `AIRL_API_TOKEN` read from `.env` and checked as an `X-AIRL-Token` header on
  mutating endpoints (the systemd sync unit sends the header too). A custom header
  alone closes CSRF, because it forces a preflight.

> **Status: OPEN.**

---

### M2 — MEDIUM — `mcp_smoke.py` asserts nothing and exits 0 under all conditions

**Evidence:** `scripts/mcp_smoke.py:25-31` — `status.isError` and `search.isError`
are **reported**, never checked. The function contains no `assert`, `raise` or
`sys.exit`. Nor does it verify that the tool list is "exactly 5 read-only tools",
which `README.md:127` and `OPERATIONS.md` both claim.

**Impact:** `README.md:117` and `OPERATIONS.md` present this script as a
verification step. Even with the bridge entirely down, the script prints JSON and
**exits 0**. If a human does not read the output, it looks green.

**Recommendation:** Add `assert not status.isError`, `assert not search.isError`
and `assert sorted(t.name for t in tools.tools) == [the five names]`. Five lines.

> ✅ **REMEDIATED (2026-08-22).** The script now asserts the **exact** five-tool
> set, both call results and a non-empty response, and exits non-zero on any
> failure. Verified behaviourally: with the Bridge stopped it exits `1`; with the
> Bridge running it exits `0`. Adding a sixth tool now fails the check until
> `EXPECTED_TOOLS` is deliberately updated.

---

### M3 — MEDIUM — `acceptance_v0.py` depends on the user's personal data and is not reproducible

**Evidence:** `scripts/acceptance_v0.py:39,49` —
`lidar_results = get("/v1/sources/search", q="LiDAR", limit=2)` and
`require(bool(lidar_results), "Source search returned no LiDAR result")`.

**Impact:** This "acceptance" passes only on *this* machine with *this* Zotero
library. If the user deletes their LiDAR papers, acceptance turns red. The plan's
own rule (`06_KANIT_VE_KABUL_STRATEJISI` / `05_DoD`: evidence reproducible on the
same target revision) is not met. Because it also needs a live service, it cannot
run in CI.

**Recommendation:** Split it in two: (a) a data-independent structural acceptance
(manifest/registry count consistency, dashboard presence, category totals) that
runs in CI against a fixed fixture; (b) a live-environment smoke check that reads
its search query from `.env` and treats an empty result as `SKIPPED`, not `FAIL`.

> ✅ **REMEDIATED (2026-08-22).** Exactly that split. Eleven data-independent
> structural checks (registry ↔ manifest ↔ category counts must agree, every
> projected file must exist, vault landmarks present) plus an optional live search
> reading `AIRL_ACCEPTANCE_QUERY`, where an empty result is `SKIPPED` rather than
> `FAIL`. The tautological `zotero_write_enabled` assertion was **removed**, and
> the script now reports what it does *not* prove under `not_proven_here`.
>
> Removing that assertion was itself part of the fix: an assertion that cannot
> fail is worse than none, because it manufactures the appearance of evidence.

---

### M4 — MEDIUM — The plan lived in 4 physical copies with contradictory canonical authority

**Evidence:**

| # | Location | Version control | Integrity |
|---|---|---|---|
| 1 | `AIRL_OS_DEVREYE_ALMA_PLANI/` (framework root) | **None** (root was not a Git repo) | `SHA256SUMS.txt` 184/184 OK |
| 2 | `airl_bridge_api/planning/commissioning/` | Yes (git) | No manifest |
| 3 | `vault_baseline/.../01 - Commissioning/` | Yes (git) | No manifest, different file names |
| 4 | `~/Documents/Obsidian Vault/.../01 - Commissioning/` | None | No manifest |

- Copies 1 and 2 had **already diverged**: `diff -rq` found differences in 12 files.
- Copies 3 and 4 **did not contain** `SHA256SUMS.txt` or the dependency matrix CSV
  — so the Obsidian mirror could not be verified for integrity at all.
- Contradictory statements of canonical authority appeared in the cockpit note,
  the status/roadmap note and the review prompt.

**Impact:** This is exactly the problem WP-012 ("Canonical Ownership and
Field-Level Authority Matrix") is meant to solve — and the plan was suffering from
it itself. Despite the existence of `09_DEGISIKLIK_VE_KONFIGURASYON_KONTROLU.md`,
drift had already begun.

> ✅ **REMEDIATED (2026-08-22):** consolidated to a single canonical copy at
> `planning/commissioning/` inside the Git repository, re-sealed
> (195 files, all OK). The Obsidian tree is now explicitly a generated reading
> mirror. **Still missing:** the automated mirror generator and the CI drift
> check, so the mirror can still be edited directly without detection.

---

### M5 — MEDIUM — WP↔ACC traceability is inconsistent in 39 of 40 cases

**Evidence (scripted analysis):**
- The WP↔ACC mapping derived from the CSV `scenarios` column disagrees with the
  *"Related packages"* field of the ACC files in **39 of 40 scenarios**.
  Example ACC-01: CSV → 12 packages; the ACC file → 5 packages. The two lists are
  not even subsets of each other.
- **62 of 130 WPs** are referenced by no ACC file at all.
- **39 of 130 WP** cards still carry the placeholder *"Assigned during the relevant
  vertical slice and commissioning"*.

**Impact:** The `COMMISSIONED` definition in `11_KAPSAM_KARSILIK_MATRISI` and the
DoD ("all ACC scenarios that use this package must pass") cannot be evaluated
mechanically. Which ACC closes which package differs depending on which source you
read.

**Recommendation:** Generate traceability in one direction only: make the CSV the
single source of truth, **generate** the "Related packages" field of the ACC files
from it, and run a CI check for "every WP is bound to at least one ACC" plus
"both directions agree". Fill the 39 placeholders, or mark those packages
explicitly `NO_ACC_REQUIRED`.

> **Note on a self-correction.** The original phrasing implied the ACC README and
> the ACC documents disagreed. They agree; the CSV is the outlier, carrying
> different and undocumented semantics. **Status: OPEN** — the CSV is now
> regenerated from the WP data, but the ACC → WP direction is still authored by
> hand.

---

### M6 — MEDIUM — No transaction boundary or compensation in the `sync` operation

**Evidence:** `src/airl_bridge/service.py:45-48` —
```python
ingest = await self.ingest_zotero(limit=limit)   # DB already committed
projection = self.project_obsidian()              # what if this raises?
```
- `finish_sync()` records only `IngestResult` fields (`service.py:35`); the
  projection result is **written nowhere**.
- `ProjectionError` → HTTP 422 (`main.py:56`), but the registry has already moved on.

**Impact:** When the vault is locked, full or unreachable, a silent divergence
opens between the registry and Obsidian and is recorded nowhere. The next timer
run does rewrite the projection in full, but in the interval the vault sits in a
wrong state that is not auditable.

**Recommendation:** Add `projection_status`, `projected`, `removed_stale` and
`projection_error` columns to `sync_runs`; wrap `sync()` so that a projection
failure marks the run `PARTIAL`. This is the V0 counterpart of WP-038 (human
updates and compensation).

> **Status: OPEN.**

---

### M7 — MEDIUM — The projection performs destructive file operations without dry-run or target validation

**Evidence:** `obsidian.py:112-132` — every `.md` file registered in the manifest
is `unlink()`ed unconditionally, and `_remove_empty_parents` removes directories
too. Config validation blocks only absolute paths and `..` (`config.py:58`).
`AIRL_OBSIDIAN_GENERATED_DIR` comes from `.env`, and `.env` was mode **0644**.

**Impact:** If `AIRL_OBSIDIAN_GENERATED_DIR` were one day pointed at a human folder
such as `20 - Source Notes`, the first run would generate there and write a
manifest, and the second run would delete the files listed in that manifest. The
existing test (`test_obsidian.py:72`) protects a human file — but only one that
never entered the manifest. A path that has been projected once is irreversibly
taken under management.

**Recommendation:**
- A `--dry-run` flag and `POST /v1/project/obsidian?dry_run=true`.
- If the target directory is non-empty and has no manifest → **refuse**; never
  adopt automatically.
- Require an additional confirmation when `projected == 0 && removed_stale > 0`
  (i.e. "delete everything"); today that case silently wipes the whole branch.

> **Status: OPEN.** `.env` permissions were fixed (see L1), which narrows but does
> not close the risk.

---

### M8 — MEDIUM — SQLite connections are never closed

**Evidence:** `database.py:60-67` `connect()` opens a new connection on every call.
`with self.connect() as connection:` is, in Python's `sqlite3`, a **transaction**
context manager — it does **not** close the connection. There is no `close()` call
anywhere in the file. `list_sources`, `get_source`, `search_sources`,
`count_sources`, `list_category_counts`, `start_sync`, `finish_sync`,
`upsert_sources` and `initialize` all follow the same pattern.

**Impact:** Every HTTP request leaks a connection until garbage collection. With 33
records and a 30-minute timer this is invisible; under real load the WAL file and
the file-descriptor count become a problem.

**Recommendation:** Wrap with `contextlib.closing(...)`, or turn `Database` into a
connection-per-request dependency. A five-line fix.

> **Status: OPEN.**

---

### M9 — MEDIUM — Silent truncation at 10,000 rows

**Evidence:** `service.py:42` `list_sources(limit=10_000)`,
`main.py:114` `duplicate_source_groups(database.list_sources(limit=10_000))`.

**Impact:** In a library exceeding 10,000 sources, the projection does not see
some sources — and then `_remove_stale` **treats the files of the sources it did
not see as stale and deletes them**. H1 (the 100 cap) masks this today; if H1 is
fixed first, M9 becomes an active data-loss path. **Do not fix H1 before M9.**

**Recommendation:** Add a paginating iterator (`iter_sources()`) to `list_sources`
and run the projection through it; remove the default limit.

> **Status: OPEN.** The ordering constraint (M9 before H1) still stands.

---

### M10 — MEDIUM — Documentation drift (not updated after renames)

**Evidence:** Six locations still referenced pre-rename vault paths and one stated
"16/16 tests PASS" where the correct figure was 20. `implementation_log.md`
Step 000-F records that rename as `PASS`, yet the old names survived in at least
six places.

**Note:** The only difference between the repository copy and the installed copy
of the systemd units is a trailing newline — **not real drift**; this was checked.

**Recommendation:** `scripts/check_docs.py` — a check that verifies the vault paths
mentioned in the documentation actually exist; run it in CI. Stop writing test
counts into documents by hand.

> ✅ **REMEDIATED (2026-08-22):** all documents were rewritten from the current
> structure, and the two systemd unit descriptions that still read "SILBO" were
> corrected and re-installed so the running units match the repository.
> **The `check_docs.py` guard is still missing**, so the drift can recur.

---

### M11 — MEDIUM — The canonical plan tree is not under version control

**Evidence:** The `.git` at the framework root was **an empty directory**, not a Git
repository (`git status` → `fatal: not a git repository`). The canonical plan tree
(186 files, hash-sealed) was tracked in no repository.

**Impact:** The "canonical" tree sealed with SHA256SUMS had no history, could not
be reverted and was not backed up. If deleted by accident, it could only be
recovered from a copy that had already diverged.

> ✅ **REMEDIATED (2026-08-22):** solved together with M4 — one copy, inside Git,
> with the hash manifest beside it.

---

### L1 — LOW — `.env` and `.env.example` were byte-identical; the example contained real paths

`.env` and `.env.example` were identical (315 bytes) with mode `0644`.
`.env.example` was tracked in Git and published the user's real home-directory
paths into a private repository. No secret was present yet — but `.env` is the file
designed for secrets, and the `chmod 600` would have been forgotten on the day the
first token was added.

> ✅ **REMEDIATED (2026-08-22):** `.env.example` now uses placeholders
> (`<VAULT_ABSOLUTE_PATH>`) and `.env` is mode `600`.

---

### L2 — LOW — `airl_id` is a 64-bit truncated hash with no collision handling

`zotero.py:83` — `sha256(binding)[:16]` (64 bits). `database.py:19` makes `airl_id`
the PRIMARY KEY. A collision would raise `sqlite3.IntegrityError` mid-sync and
leave a partial commit. The birthday bound is around 4 billion records so the
practical risk is low, but the plan (WP-011) asks for collision-free identity and a
merge/tombstone rule, and neither exists.

> **Status: OPEN.**

---

### L3 — LOW — Category folder names mixed English and Turkish

`catalog.py:10-23` mixed English names such as `01 - Journal Articles` with
Turkish-language names for books, theses and the catch-all categories, inside the
same dictionary. Only the first three types were in use (33 sources), so the mix
was invisible; it would have appeared in the vault the moment the first book was
added.

> ✅ **REMEDIATED (2026-08-22):** all eleven category names are now English
> (`04 - Books`, `05 - Book Sections`, `06 - Theses`, `07 - Web Sources`,
> `08 - Datasets`, `09 - Patents`, `90 - Other Documents`, `99 - Other Sources`).
> Existing projected folders are regenerated from the canonical registry.

---

### L4 — LOW — Zero test coverage of the security and error paths

`tests/test_api.py` only calls `GET` (the `_get` helper, line 10). Untested paths:
- None of the three `POST` endpoints
- `ZoteroUnavailable` → 503 handler (`main.py:52`)
- `ProjectionError` → 422 handler (`main.py:56`)
- `Settings.from_env` loopback refusal (`config.py:47`)
- `AIRL_OBSIDIAN_GENERATED_DIR` traversal refusal (`config.py:58`)
- `library_type` validation (`config.py:63`)

In other words, **every defensive mechanism is untested**. This directly
contradicts the plan's `05_DoD` requirement that "security/data/policy negative
tests have passed".

> **Status: OPEN.**

---

### L5 — LOW — A fake `.git`, an empty `.codex` and an empty `.agents` at the root

These misled tooling (this session began with "git repository: true" while no repo
existed at the root). Clean them up or make them a real repository.

> ✅ **REMEDIATED (2026-08-22):** the root is now a real Git repository; the empty
> marker directories were removed.

---

## E. Plan quality audit (quantitative)

The plan is good. But the phrase "130 detailed work packages" implies more than is
there. Measured:

| Metric | Value |
|---|---|
| WP files | 130, 87,971 words, 9,653 non-blank lines |
| **Lines repeated verbatim in ≥120 of the 130 files** | **5,718 / 9,653 = 59.2%** |
| Lines unique to exactly one WP | 3,318 = 34.4% → **~25 unique lines per WP** |
| ACC files | 40, 2,870 lines |
| Lines repeated in ≥36 of the 40 files | 1,400 = **48.8%** |
| Unique lines per ACC | ~32 |

**Interpretation:** The `Test and verification plan`, `Acceptance criteria`,
`Acceptance evidence package`, `Risks`, `Rollback` and `Handoff` sections of every
WP are **the same template verbatim**. In the "Implementation tasks" table of all
130 packages, the `Completion evidence` column reads
`Commit / configuration / record reference` — which is **not a measurable
acceptance criterion**.

The template has value (consistency, no forgotten dimension). But:
- `05_DoD` says "acceptance criteria are **measurable**"; the template criteria are
  not measurable ("all mandatory tests have passed").
- The genuine specification content is **~25 lines per package** — insufficient for
  implementation. WP-011's entire technical content, for instance, is a five-line
  table.

**Recommendation:** Keep the template, but make a `refinement` step mandatory for
every package entering implementation: a package is not `READY` until
package-specific, measurable acceptance criteria (numbers, thresholds, commands)
are written. Let the template criteria be the *minimum* and the refinement criteria
be the *real gate*.

**The plan's quantitative strengths:** 130/130 files present, matching the CSV
exactly; the dependency graph **acyclic and topologically ordered** (forward
dependencies: 0); 1011 internal links with **0 broken**; 184 file hashes verifying
**OK**. Integrity at this level is rare.

> **Status: PARTIALLY ADDRESSED (2026-08-22).** The rewritten WP files carry
> substantially more package-specific content (purpose paragraphs, workstream
> hazards, explicit rollback semantics), which raises the unique-content ratio.
> The **measurable-criteria requirement is still unmet** — the refinement step
> remains the correct fix.

---

## F. Contract and data-flow audit

| Contract | Planned (WP) | Present | Status |
|---|---|---|---|
| Identity / correlation | WP-011 | `Identity` class (170 lines), unused in production | PARTIAL — H4 |
| Canonical field authority | WP-012 | None; the plan itself lived in 4 copies — M4 | DOCUMENTED_ONLY |
| Project/task/role | WP-013 | None | DOCUMENTED_ONLY |
| Artifact manifest | WP-014 | `ArtifactManifest` class; `content_hash` format contradicts | PARTIAL — H4 |
| Event envelope | WP-015 | `EventEnvelope` class; **no event is ever produced**, no bus | PARTIAL — H4 |
| Policy/control/exception | WP-016 | None (`policy/` empty) | MISSING |
| Source/literature | WP-017 | `SourceRecord` (pydantic); no representation/status/trust | PARTIAL |
| Claim/evidence/review/decision | WP-018 | None | DOCUMENTED_ONLY |
| Run/environment/reproduction | WP-019 | `sync_runs` table (ingest counters); no manifest | PARTIAL (very weak) |
| Schema registry + SDK | WP-020 | In-process `dict`; no JSON Schema, no validation, no CI | PARTIAL → effectively MISSING |

**Producer/consumer incompatibilities:**
1. `content_hash` format: `"sha256:<hex>"` (production) vs `^[0-9a-f]{64}$`
   (contract) — an **active contradiction**.
2. `airl_id` generation does not pass through contract validation.
3. The Obsidian frontmatter (`obsidian.py:292-308`) is a separate *de facto*
   schema — `airl_id`, `type`, `status`, `source_category`, `content_hash`,
   `provenance` — registered in no registry and unversioned. Vault files carry no
   `schema_version` today and therefore cannot be migrated later.
4. `.airl-projection-manifest.json` carries `schema_version: 1` but is not in any
   registry.
5. SQLite writes `schema_meta.schema_version = "1"` (`database.py:73`) but **never
   reads it** — there is no migration mechanism. The
   `data/projection-backups/Sources-before-title-migration-20260821/` directory
   shows a migration was performed by hand.

---

## G. Security and trust-boundary audit

| Dimension | Target (plan) | Present | Assessment |
|---|---|---|---|
| Trust zones (Zone 0–3) | WP-051 | None; one process, one user | DOCUMENTED_ONLY |
| Network egress | WP-057 | Bridge is loopback-only (`config.py:47`) — **good** | Sufficient for V0 |
| API authn/authz | WP-055/056 | **None** — M1 | Open |
| CSRF / Host validation | — | **None** — M1 | Open |
| Secret management | WP-055 | `.env` was 0644, no secrets yet but weak preparation — L1 | Weak (now fixed) |
| Sandbox | WP-054 | systemd hardening (real and good) | Sufficient for V0 |
| Content quarantine / prompt injection | WP-058 | `html.escape` present (tested); PDF/abstract text reaches Hermes raw | Partial |
| Policy enforcement | WP-056 | None (`policy/` empty) | None |
| Supply-chain admission | WP-059 | None; `uv.lock` present (good), no signature or SBOM | None |
| Least privilege | — | Zotero read-only is **claimed**, not tested — H3 | Unverified |
| Auditability | WP-099 | `sync_runs` table (ingest counters); no event or audit log | Very weak |
| Rollback | — | `data/projection-backups/` with 3 backups plus Git | Reasonable for V0 |

**Prompt injection note:** Hermes MCP `get_source` passes the Zotero abstract to
the model as raw text (`mcp_server.py:98`). An abstract originating from a
malicious PDF can inject instructions. ACC-05 is exactly this scenario and is
`DOCUMENTED_ONLY`. In V0 the tools are read-only so the blast radius is small — but
it grows if Hermes has *other* tools (file writes and so on).
**Action:** mark external content in the MCP output with an explicit boundary (such
as `<untrusted-source-content>`) — cheap and effective.

---

## H. Literature / Zotero / Obsidian audit

**Flow verified:** `Zotero(23119) → Bridge(8765) → SQLite → Obsidian → Hermes MCP`.
Live: `/ready` → `{"status":"ready","zotero":"reachable","source_count":33}`.
DB: 33 sources (25 journalArticle, 6 report, 2 conferencePaper), 25 sync runs, the
last 8 `SUCCEEDED` / 33 unchanged.

| Check | Result |
|---|---|
| Is source identity stable? | ✅ Yes, tested |
| Is it idempotent? | ✅ Yes, tested |
| Title-based naming with a collision suffix | ✅ Yes, tested (`test_obsidian.py:41`) |
| Are human notes preserved? | ✅ Yes, manifest-owned deletion, tested |
| Is there any write to Zotero? | ✅ None in the code (verified by hand) — ❌ but not proven by a test (H3) |
| Is the baseline in sync with the real vault? | ✅ `diff -rq` → only `.obsidian/` config and one empty daily note |
| Wikilink integrity | ✅ 103 links, 0 broken |
| Plan mirror link integrity | ✅ 1011 links, 0 broken |
| Duplicate reporting without automatic merge | ✅ Correct (`catalog.py:36`, report only) |
| Full-coverage sync | ❌ 100 cap — H1 |
| Deletion / reconciliation | ❌ None — H2 |
| Annotation / attachment ingest | ❌ None (`zotero.py:14` skips them) — WP-068 MISSING |
| Collection/tag opt-in permission boundary | ❌ None; all of `users/0` is read — WP-064 CONTRADICTED |
| Literature set manifest freeze | ❌ None — WP-072 MISSING |
| `schema_version` in vault notes | ❌ None — cannot be migrated |
| Duplicate note names | ⚠️ `README.md` ×2, `readme.md` ×2 (ambiguous Obsidian shortlinks) — ✅ since renamed to distinct index names |

**Note:** `data/projection-backups/` holds 3 rollback backups. They are in
`.gitignore` — meaning **the rollback backups are neither version-controlled nor
backed up**, while `OPERATIONS.md` presents them as the official rollback point.
That is risky.

---

## I. Evidence and reproducibility audit

Every "success" claim, separated by whether it is reproducible:

| Claim | Evidence type | Reproducible? |
|---|---|---|
| "20/20 tests PASS" | `pytest -q` | ✅ Yes — reproduced in this session |
| "33 sources, 3 categories" | live `/ready` + SQLite | ⚠️ Only on this machine with this library |
| "Bridge + timer active" | `systemctl --user is-active` | ✅ Yes — verified |
| "Plan integrity" | `sha256sum -c` 184/184 | ✅ Yes — reproduced |
| "Baseline = vault" | `diff -rq` | ✅ Yes — reproduced |
| "Zotero write disabled" | a constant `False` | ❌ **No — H3, not evidence** |
| "V0 acceptance: accepted" | `acceptance_v0.py` | ❌ **No — M3, depends on personal data, needs a live service** |
| "MCP: 5 read-only tools" | `mcp_smoke.py` | ❌ **No — M2, asserts nothing** |
| "Step 001 TECH_COMPLETE (WP-011/014/015/020/022)" | implementation log | ❌ **Wrong for WP-022 — C3** |
| SILBO FIX-004/005a `ACCEPTED` | separate repo, sealed review + quorum | 🔍 **Out of scope for this review** — separate repository, separate authority |

**Conclusion:** All three artifacts currently presented as "evidence" prove
nothing. They were not written in bad faith — but they are a textbook instance of
the plan's own `05_DoD:52` clause ("a happy-path demo only").

**Note — the SILBO separation:** the SILBO FIX-004 / FIX-005a / FIX-005 records in
the status document and the implementation log belong to a separate repository
(`/home/otonom/silbo-fix-00*`) and were **not verified** within this review. It is
good that the documents make this separation explicitly. But note: 8 of the 20 rows
in the framework status table (`§1 Current status summary`) are SILBO rows, all
marked `ACCEPTED`/`PASS`. Someone glancing at the framework would conclude the
framework itself had been accepted.
**Recommendation:** move the SILBO rows into a separate table.

---

## J. Risk register

| # | Risk | Impact | Likelihood | Detection evidence | Mitigation | Closure criterion |
|---|---|---|---|---|---|---|
| R1 | The programme can never start (evidence deadlock) | Critical | **Certain** | C1 | WP-000 Interim Evidence Policy | WP-001 can reach `ACCEPTED` on interim evidence |
| R2 | The scope does not fit the organisation | Critical | **Certain** | C2 | Cut scope, or adopt the sealed-review verifier model | A written decision in `00_PROGRAM` |
| R3 | Divergence between claim and reality (WP-022) | High | Occurred | C3 | Downgrade the status; verify claims in CI | `git ls-files` shows the deliverables |
| R4 | Silent data gap beyond 100 sources | High | High (a matter of time) | H1 | Pagination + `since=` | Test: a 250-record mock library syncs fully |
| R5 | Deleted sources persist as ghosts | High | High | H2 | `/deleted` + tombstone | Test: a deleted source becomes `WITHDRAWN` and leaves the projection |
| R6 | The read-only claim silently breaks one day | High | Medium | H3 | Behavioural test + static check | The MockTransport test runs in CI |
| R7 | The contract core rots as dead code | High | High | H4 | At least one production consumer | `airl_bridge` uses `Identity` |
| R8 | Manual evidence production is not repeatable | High | Certain | H5 | GitHub Actions | A green pipeline on every push |
| R9 | Local API abuse (CSRF / rebinding) | Medium | Low | M1 | TrustedHost + token | Test: POST without a token returns 401 |
| R10 | Plan copies diverge | Medium | Occurred | M4 | One canonical copy + generated mirror + CI drift check | `check_plan_drift.py` green |
| R11 | The projection adopts the wrong folder | Medium | Low | M7 | dry-run + non-empty-directory refusal | Test: a populated human folder is refused |
| R12 | Active data loss above 10k sources | Medium | Low (rises after H1) | M9 | Paginating iterator | Closes together with H1 |
| R13 | Rollback backups are not version-controlled | Medium | Medium | Section H | Hash the backups and bind them to a manifest | A backup manifest + a verification command |
| R14 | Documentation drift erodes trust | Medium | Occurred | M10 | `check_docs.py` | Path verification in CI |
| R15 | Prompt injection (Zotero abstract → MCP) | Medium | Low (in V0) | Section G | Untrusted-content tagging | A boundary tag in the MCP output |

---

## K. Audit of `CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md`

The user said they did not trust this prompt. They were right. Findings:

**K1 — It includes directories that do not exist (lines 69, 71, 73):**
- `planning/commissioning/09_OPERATIONS/` → actually `09_EXPERIENCE_OBSERVABILITY/`
- `planning/commissioning/11_DECOMMISSION/` → actually `11_DAY2_OPERATIONS/`
- `planning/commissioning/13_CHANGE_CONTROL/` → **does not exist at all**

The prompt was written without reading the plan's real structure. A reviewer who
followed the list literally would report three sections as "MISSING" and never
examine two real ones.

**K2 — It lists empty directories as review targets (lines 119-125):**
`services/`, `workflows/`, `agents/`, `infra/`, `policy/` — all empty and untracked
(C3). The prompt describes the structure that was *wanted*, not the one that exists.

**K3 — The report format buries the findings (lines 262-272):**
It asks for a 130-row WP matrix plus a 40-row ACC matrix. About 160 of those rows
would say the same thing (`DOCUMENTED_ONLY`, evidence: "the file exists, the code
does not"). The real 10–15 findings would vanish inside that table. **The report
format performs rigour without producing action.**

**K4 — The command it asks you to run is wrong (line 205):**
`python -m unittest discover -s airl_bridge_api/tests -q` does not run from the repo
root; `pythonpath=["src"]` is defined only in the pytest configuration
(`pyproject.toml:32`). `unittest` raises `ModuleNotFoundError`.

**K5 — The question it never asks:**
The prompt asks "how much has been built?" six times, but never asks:
**"Can this plan be executed by this organisation?"** — C1 and C2, the two most
expensive findings, sit in the prompt's blind spot.

**K6 — What it gets right (keep this):** the evidence classification
(`IMPLEMENTED`/`PARTIAL`/`DOCUMENTED_ONLY`/`CONTRADICTED`/`BLOCKED`), the rule that
"file existence is not evidence", the rule not to conflate SILBO with the
framework, and the read-only constraint. Those are correct and were applied in this
report.

**Recommendation:** Fix the prompt (K1, K2, K4) and change the report format:
instead of a 130-row matrix, produce a table of **"packages whose status is not
`DOCUMENTED_ONLY`"** plus a summary distribution. The rest is the default anyway.

---

## L. A realistic implementation order

Each step is marked `implementable` (code/config changes) or `document-only`
(a decision or text). The order follows the dependencies and **cannot be skipped**.

---

### Step 0 — The scope decision `document-only` 🔴 BLOCKING

**Goal:** Resolve C2. The 130-package / 73-owner / 114-verifier model is invalid for
this organisation; writing code before the model is written down is wasted effort.
**Precondition:** None. **This is the first job.**
**Changes:** a new `00_PROGRAM/12_organisation_and_independence_model.md`; a revision
of `04_role_and_responsibility_matrix.md`.
**Content:** (a) scope — which WPs are `IN_SCOPE` and which `DEFERRED`;
(b) independence — formalising the SILBO sealed-review plus exact-quorum protocol as
the framework's verifier (different model family, sealed context, exact target SHA).
**Evidence:** the document plus a change-log line in the status/roadmap note.
**Rollback:** revert the document. **Done when:** every package in the catalogue
carries an `IN_SCOPE`/`DEFERRED` label and the verifier definition is written.

---

### Step 1 — Interim Evidence Policy (WP-000) `document-only` 🔴 BLOCKING

**Goal:** Resolve C1. Define a valid evidence store until WP-026 exists.
**Precondition:** Step 0.
**Changes:** `00_PROGRAM/WP-000_interim_evidence_policy.md`; an "interim evidence"
clause in `05_definition_of_ready_and_done.md`; an append-only
`delivery/EVIDENCE_LEDGER.md`.
**Format:** `delivery/WP-xxx/evidence-manifest.json` →
`{target_git_sha, command, exit_code, artifacts:[{path, sha256}], produced_at, producer, verifier}`.
**Evidence:** the policy document plus the first manifest example.
**Rollback:** revert the document. **Done when:** a package can reach `ACCEPTED`
under this policy (tested in Step 3).

> Note: **WP-139** (evidence timestamping) supplies the external time anchor for
> this interim store without requiring any of WP-026's infrastructure.

---

### Step 2 — CI foundation `implementable` (H5, and closes four findings at once)

**Goal:** Automate evidence production.
**Precondition:** Step 1 (the evidence format must be settled).
**Changes:** `.github/workflows/ci.yml`, `pyproject.toml` (`[tool.ruff]`),
`scripts/check_readonly_boundary.py`, `scripts/check_plan_integrity.py`.
**Content:** `uv sync --extra dev` → `ruff check` → `pytest -q` → the Zotero write
static check (H3) → `sha256sum -c SHA256SUMS` (M4/M11).
**Evidence:** a green workflow run URL plus `evidence-manifest.json`.
**Rollback:** delete the workflow file. **Done when:** five checks are green on
every push.

---

### Step 3 — A real test of the read-only boundary `implementable` (H3)

**Goal:** Actually prove the framework's strongest security claim. **This is also
the pilot for Step 1**: the first `evidence-manifest.json` is produced here.
**Precondition:** Step 2.
**Changes:** `tests/test_readonly_boundary.py` (new); `src/airl_bridge/models.py:65`
and `main.py:62` (remove the fake field); `scripts/acceptance_v0.py:41,77` (remove
the tautological check).
**Test:** a `MockTransport` handler that raises `AssertionError` when
`request.method != "GET"`; run the whole `sync()` flow through it.
**Evidence:** the test output plus a manifest. **Rollback:** revert the commit.
**Done when:** breaking the test requires adding a `POST` to `zotero.py` — and when
you do, CI turns red (try it once and revert; that is evidence too).

---

### Step 4 — A paginating iterator (M9) `implementable` — **BEFORE H1**

**Goal:** Remove the silent 10,000-row truncation. It must come before H1, or the
H1 fix opens an active data-loss path.
**Precondition:** Step 2.
**Changes:** `database.py` (`iter_sources()`), `service.py:42`, `main.py:114`.
**Evidence:** a projection test with a 15,000-row fixture (everything projected,
`removed_stale == 0`). **Rollback:** revert the commit.
**Done when:** no `limit=10_000` remains in the code.

---

### Step 5 — Zotero pagination + incremental sync (H1) `implementable`

**Precondition:** Step 4.
**Changes:** `zotero.py` (`start` loop, `Total-Results` reading, `since=` support),
`database.py` (`sync_runs.library_version`), `service.py`, `cli.py:68` (drop the
limit choices), `main.py:126,136`, `deploy/airl-bridge-sync.service`.
**Evidence:** a 250-record mock library → 250 fetched; the run marked `PARTIAL`
whenever `fetched < total`. **Rollback:** revert the commit plus the
`library_version` migration reversal.
**Done when:** on the real library, `source_count == Zotero Total-Results`.

---

### Step 6 — Deletion reconciliation + tombstones (H2) `implementable`

**Precondition:** Step 5 (the `since=` infrastructure).
**Changes:** `zotero.py` (`/deleted?since=`), `database.py` (`sources.status`,
`withdrawn_at`, a migration and an actual **read** of `schema_version`),
`service.py`, `obsidian.py` (do not project `WITHDRAWN`).
**Evidence:** test — a deleted source becomes `status=WITHDRAWN`, its Obsidian file
disappears and its DB row survives. **Rollback:** a migration reversal script,
written in advance. **Done when:** the V0 counterpart of WP-067 works.

---

### Step 7 — API hardening (M1) `implementable`

**Precondition:** Step 2.
**Changes:** `main.py` (`TrustedHostMiddleware`, a token dependency), `config.py`
(`AIRL_API_TOKEN`), `.env` (chmod 600), `.env.example` (placeholders),
`deploy/airl-bridge-sync.service` (the header), `docs/OPERATIONS.md`.
**Evidence:** test — POST without a token → 401; a wrong Host → 400.
**Rollback:** remove the middleware. **Done when:** L1 and M1 are closed.

---

### Step 8 — Sync transaction/compensation + audit (M6) `implementable`

**Precondition:** Step 6.
**Changes:** `database.py` (projection columns on `sync_runs`), `service.py:45`,
`models.py`.
**Evidence:** test — a projection failure marks the run `PARTIAL`, the error is
recorded and the registry stays consistent. **Done when:** the V0 counterpart of
WP-038 works.

---

### Step 9 — Reduce the plan to a single canonical copy (M4, M11) `implementable`

**Precondition:** Step 2 (for the CI drift check).
**Changes:** remove (or symlink) the duplicate plan tree; `scripts/mirror_plan.py`
(canonical → vault generation); `scripts/check_plan_drift.py`; `SHA256SUMS` beside
the canonical copy; update the cockpit, status and review prompt.
**Evidence:** the drift check green in CI; `sha256sum -c` OK.
**Rollback:** move to `90 - Archive` rather than deleting, then move back.
**Done when:** the plan lives in one place with a generated mirror, verified by CI.

> ✅ Consolidation and re-sealing are **done (2026-08-22)**; the generator and the
> CI drift check remain.

---

### Step 10 — Bind the contract core (H4) `implementable`

**Precondition:** Step 3, Step 9.
**Changes:** `zotero.py:104` (`content_hash` format → bare hex plus `hash_algo`), a
migration script, `zotero.py:83` (`airl_id` through `Identity`), `schemas/*.json`
(real JSON Schema), `contracts.py` (validate with `jsonschema`), a schema
compatibility check in CI.
**Evidence:** `grep airl_framework src/airl_bridge/` returns at least 2 results; a
schema test; a migration dry run plus a reversal attempt.
**Done when:** WP-011/014/020 are genuinely `TECH_COMPLETE` — and can become
`ACCEPTED` under the verifier model from Step 0.

---

### Step 11 — Pull the claims back to reality `document-only`

**Precondition:** Step 10.
**Changes:** `implementation_log.md` (WP-022 → `NOT_STARTED`, with the C3
explanation), the status/roadmap note (test count 20; SILBO rows moved to a
separate table), `docs/ARCHITECTURE_V0.md` (the M10 path corrections),
`deploy/*.service|timer` (SILBO naming), `README.md` (L3),
`docs/review/CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md` (K1, K2, K4).
**Evidence:** `scripts/check_docs.py` green. **Done when:** not one unverifiable
path or number remains in the documentation.

> ✅ Mostly **done (2026-08-22)** through the full English rewrite; the
> `check_docs.py` guard is still missing, so this can regress.

---

### Step 12 — The first real ACC scenario `implementable`

**Goal:** Actually automate one of the 40 ACC scenarios. Candidate: **ACC-22
(Obsidian human edit preservation)** — the existing `test_obsidian.py:72` already
does half of it, and it closes your most critical data-loss risk.
**Precondition:** Step 1 (the evidence format), Step 2 (CI).
**Changes:** `tests/acceptance/test_acc_22.py`,
`delivery/ACC-22/evidence-manifest.json`, and a "current automation" line in the
ACC-22 document.
**Evidence:** the ACC test passing in CI plus a signed manifest.
**Done when:** 1 of the 40 ACCs is `IMPLEMENTED`. That becomes the first proof that
the programme can actually start.

---

**After Step 12:** Phase C (the WP-013/016/017 contracts), then the WP-061–074
literature platform. But Step 0 and Step 1 come first — without them, everything
else keeps producing unacceptable code.

---

## M. Final verdict — direct answers to the six questions

**1. How much of the framework has actually been built?**
Roughly **2–3%**. Measure: 0 of 130 WPs are `ACCEPTED`, 9 are `PARTIAL`. Working
code totals 1,509 lines. What exists is a single vertical slice: a read-only
literature bridge. What does not exist: the control plane, event backbone,
execution fabric, evidence ledger, observability and security platform — that is
five of the architecture's six planes.

**2. Which parts are only planned?**
119/130 WPs and 40/40 ACCs. Concretely: Temporal, NATS, PostgreSQL, MLflow,
Kubernetes, gVisor, SPIFFE/Vault, OPA, LiteLLM, LangGraph, Neo4j/pgvector,
Langfuse, Grafana, the cost ledger, clean-room reproduction, the claim/evidence
ledger, blind review and the publication package. **Not one line of code exists for
any of them.**

**3. The three most critical obstacles?**
(a) **C1** — the evidence-chain bootstrap deadlock: even WP-001 cannot be accepted.
(b) **C2** — a 73-owner / 114-verifier assumption against a one-person organisation.
(c) **H3 + M2 + M3** — the evidence production mechanism is itself broken; the three
artifacts you see as "green" verify nothing. Until these three are fixed, every
advance is a fake advance.

**4. The real vertical slice that can be run safely today?**
Literature Bridge V0: `Zotero (read-only) → SQLite → Obsidian → Hermes MCP`. At the
33-source scale it is safe, idempotent, preserves human notes and stays local.
**Limit: the moment the library exceeds 100 sources it syncs silently incompletely
(H1).** Note that today; once you grow it becomes very hard to notice.

**5. What is the next implementation step, exactly?**
Not code. **Step 0**: write
`00_PROGRAM/12_organisation_and_independence_model.md` — which WPs are `IN_SCOPE`,
and what "independent verifier" means in a one-person organisation. Immediately
after: **Step 1**, `WP-000_interim_evidence_policy.md`. Without these two, any code
you write is unacceptable by the plan's own rules.

**6. Which missing evidence prevents anything being called "complete"?**
- A **behavioural** test of the Zotero read-only boundary (H3)
- An MCP verification that actually asserts (M2)
- Data-independent, reproducible acceptance (M3)
- Repeatable, automated test-execution evidence — CI (H5)
- A producer-independent verifier decision (C2) — absent for every package
- A signed `EvidenceManifest` and an immutable store (C1) — no mechanism exists
- A rollback/compensation trial (mandatory in the DoD) — performed for no package
- Negative security tests (L4) — none of the defensive paths are tested
- The WP-022 deliverable (C3) — not in the repository

---

## N. Evidence appendix

### Commands executed and their results

> **Note:** these commands were run against the directory structure as it stood at
> audit time (with an `airl_bridge_api/` subdirectory). The repository was
> subsequently flattened to the `AI_RESEARCH_FRAMEWORK/` level; read the paths
> accordingly.

| Command | Exit | Result |
|---|---:|---|
| `.venv/bin/python -m pytest -q` | 0 | **20 passed**, 1 warning (pydantic_settings forward-ref) |
| `curl -s http://127.0.0.1:8765/health` | 0 | `{"status":"ok","version":"0.1.0",...,"zotero_write_enabled":false}` |
| `curl -s http://127.0.0.1:8765/ready` | 0 | `{"status":"ready","zotero":"reachable","obsidian_vault":true,"source_count":33}` |
| `systemctl --user is-active airl-bridge.service airl-bridge-sync.timer` | 0 | `active` / `active`; last sync 8 minutes earlier |
| `sha256sum -c .../SHA256SUMS.txt` | 0 | **184/184 OK**, 0 FAILED |
| `sqlite3 data/airl_bridge.sqlite3` (via Python) | 0 | 33 sources, 25 sync_runs, last 8 `SUCCEEDED` |
| `git -C airl_bridge_api log --oneline` | 0 | 21 commits, HEAD `6c849bd`, 0/0 against `origin/main` |
| `git ls-files \| grep -E '^(services\|workflows\|agents\|infra\|policy\|delivery)/'` | 1 | **No output** → C3 |
| `diff -rq vault_baseline "$VAULT"` | 1 | Only `.obsidian/` config + an empty daily note + `Zotero Sources/` |
| `diff -rq <plan copy 1> <plan copy 2>` | 1 | **12 files differ** → M4 |
| `diff .env .env.example` | 0 | **Byte-identical** → L1 |
| `diff deploy/*.service ~/.config/systemd/user/*.service` | 1 | Trailing newline only — **not real drift** |
| Wikilink scanner (Python) | 0 | 246 notes, 103 wikilinks, **0 broken**, 2 duplicate basenames |
| Markdown link scanner (Python) | 0 | 1011 links in each of the three plan copies, **0 broken** |
| Plan consistency analysis (Python) | 0 | 130/130 WP file↔CSV match, **no cycles**, forward dependencies **0** |
| Boilerplate analysis (Python) | 0 | **59.2%** repetition in WPs; **48.8%** in ACCs |
| WP↔ACC cross-check (Python) | 0 | **39/40 inconsistent**; 62/130 WPs receive no ACC reference |
| Role analysis (CSV) | 0 | **73 owners**, **114 verifiers**; effort: 83 L / 42 M / 5 S |
| `ls .github Makefile ruff.toml mypy.ini .pre-commit-config.yaml` | 2 | **None present** → H5 |
| `gh api repos/furkanhanilci/AI-Research-Framework` | 0 | `private=true`, `default_branch=main` |

### Volume scanned

| Area | Count |
|---|---:|
| Plan files (canonical tree) | 186 (184 md + 1 csv + 1 txt) |
| Plan word count (WPs only) | 87,971 |
| Python source lines (`src/`) | 1,509 |
| Test lines (`tests/`) | 381 |
| Tests | 20 |
| API endpoints | 10 (7 GET, 3 POST) |
| MCP tools | 5 (all read-only) |
| Obsidian notes (real vault) | 246 |
| Vault baseline files | 211 |
| Git-tracked files | 434 |
| Zotero sources | 33 |

### Areas that could not be verified (BLOCKED)

| Area | Reason |
|---|---|
| The SILBO FIX-004 / FIX-005a / FIX-005 acceptance chain | A separate repository, outside this review's scope; the claims were not verified |
| The Hermes `tools.include` five-tool restriction | The Hermes configuration file lives outside the repository; the claim in `README.md` and `OPERATIONS.md` was not verified |
| GitHub branch protection / required checks | Repository metadata was read via `gh api`; protection rules were not queried (read-only boundary) |
| Running `acceptance_v0.py` | It POSTs and GETs against the live service and depends on personal data; it was read and assessed, not executed |
| The real total record count in the Zotero Local API | Zotero was not queried directly; `source_count=33` came through the bridge |

---

## Closing note

I was asked to be harsh, and I was. But the thing that needs stating is this:
**the real problem here is not insufficient work.** Code quality, atomic writes,
manifest-owned deletion, systemd hardening, plan integrity — that is good
engineering.

The problem is **the gulf between the scale of the plan and the scale of the
organisation**, and the fact that this gulf has begun to falsify the evidence
production mechanism. The `zotero_write_enabled is False` test, `mcp_smoke.py`'s
exit 0 and WP-022's empty directories are all the same phenomenon: the appearance
of evidence without the substance of it.

That is fixable, and the fix is not more work — it is a smaller scope and a real
verifier. Steps 0 and 1 cost a day each and unblock everything else.
