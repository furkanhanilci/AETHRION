---
airl_id: AETHRION-SYSTEM-ROLLOUT
type: project
status: active
owner: otonom
created_at: "2026-08-21"
updated_at: "2026-08-22"
current_phase: fix-005-dry-run-preparation
canonical_status_scope: operational-tracker
tags:
  - aethrion/project
  - aethrion/architecture
  - aethrion/status
  - aethrion/roadmap
  - silbo/subproject
cssclasses:
  - aethrion-project
---

# AETHRION — Current Status and Roadmap

> [!important] A living project record
> This document is updated after every material implementation, test, review,
> acceptance, rollback or scope change. **Work is never counted complete on
> intent or on an agent's statement**; it is supported by command output, an
> artifact and, where required, independent review.

## 1. Executive summary

The AETHRION advances on two separate but related planes:

1. **The SILBO model-development sub-line:** a separate, pre-existing code base
   for training, evaluation, verifier reliability and publication-quality
   evidence. `SILBO-FIX-004` and `SILBO-FIX-005a` were accepted under exact
   sealed Fable quorum. `SILBO-FIX-005` was activated locally after a challenge;
   the fail-closed runner/report contract and 11 focused tests are ready.
   Inference will not start before mutation, full-suite and dry-run evidence pass.
2. **The AETHRION commissioning programme:** the plan describing the full research
   operating system across 140 work packages and 40 end-to-end acceptance
   scenarios. **None of this programme has been built.**

In addition, a usable first vertical slice — the **local literature V0
system** — is running:

```text
Zotero Local API (read-only)
        -> AIRL Bridge API
        -> SQLite canonical V0 registry
        -> Obsidian Literature Sets view
        -> Hermes read-only MCP tools
```

### Framework status summary

| Area | Status | Evidence / limit |
|---|---|---|
| Local literature V0 | WORKING | 33 sources, 3 categories, Obsidian projection |
| Bridge API | ACTIVE | `127.0.0.1:8765`, no Zotero write path in the code |
| Automatic sync | ACTIVE | systemd user timer, every 30 minutes |
| Hermes MCP | ACTIVE | 5 read-only tools |
| Obsidian information architecture | V0 READY | Human and generated areas separated |
| Documentation corpus | ENGLISH / COMPLETE | Steps 004–005; mirror generators with `--check`; module docstrings throughout |
| Full AETHRION commissioning | NOT STARTED / PLAN | No independent acceptance at WP level |
| Production cutover | NOT AUTHORISED | Requires 40 ACCs, restore drills and closure of critical findings |

### SILBO status summary (a separate repository, outside this evidence chain)

> These rows describe work in `/home/otonom/silbo-fix-00*`, a **separate
> repository with its own authority boundary**. They were not verified during the
> framework audit, and they say nothing about the framework's own status.

| Area | Status | Evidence |
|---|---|---|
| SILBO-FIX-004 implementation | IMPLEMENTED | Immutable `T=85625d7…`, `H=ddad3ab…` |
| SILBO-FIX-004 independent review | APPROVED | Sealed Fable review `efb87f2`; exact T/H verified |
| SILBO-FIX-004 administrative quorum | PASS / ACCEPTED | Review `933f17f` in the governed lineage; exact quorum PASS |
| SILBO-FIX-004 state reconciliation | PASS | Ledger/queue/state commit `b96b989`; preflight PASS |
| SILBO-FIX-005a | ACCEPTED | `T=ff5f959`, `H=e8e614c`, Fable `1309853`, closeout `b803846` |
| SILBO-FIX-005b follow-up | WRITTEN / NON-BLOCKING | AIR-014; constructor mismatch guard test; does not reopen 005a |
| SILBO-FIX-005 | ACTIVE / PRE-INFERENCE | Target `b14b0b3`; 11/11 focused, 8/8 mutation, evaluation 155/155, runtime 72/72 PASS; dry-run pending |
| SILBO model repository | SEPARATE / UNTOUCHED | Never used as the framework remote |

## 2. Status vocabulary used in this document

| Status | Meaning |
|---|---|
| `PLAN` | The design or work package is documented; there is no implementation evidence |
| `IN_PROGRESS` | Authorised, bounded work is active |
| `TECH_COMPLETE` | Code/configuration is ready; independent acceptance is not complete |
| `PARTIAL` | Only the explicitly stated subset of the target works |
| `ACCEPTED` | The package criteria were accepted on independent evidence |
| `COMMISSIONED` | The related end-to-end acceptance scenarios also passed |
| `BLOCKED` | An external decision, authority or unmet mandatory precondition blocks progress |

**`V0 READY` and `WORKING` in this document do not mean that the 140-package
programme is `ACCEPTED` or `COMMISSIONED`.** No package is currently `ACCEPTED`.

## 3. Source authorities and working directories

### 3.1 The full commissioning plan

```text
/home/otonom/Desktop/FH/AETHRION/
  planning/commissioning/
```

This area defines the target architecture, work packages WP-001–WP-140 and
acceptance scenarios ACC-01–ACC-51. It is hash-sealed:

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

### 3.2 The local literature V0 implementation

```text
/home/otonom/Desktop/FH/AETHRION/
```

The initial local Git commit:

```text
15d57af Establish local literature bridge V0
```

### 3.3 The existing SILBO product repository

The accepted FIX-004 worktree:

```text
/home/otonom/silbo-fix-004
branch: codex/fix-004
current local HEAD: b96b989
implementation target/T: 85625d7a30fd9d77c9179ccff94d08b27ac0b1fd
handoff/H: ddad3abb49e53043e668a597432b9848ad43fb6a
review import: 933f17f3fe7b6b25b60e4ec293db0e6ad4b9acf5
closeout: 5737757
state reconciliation: b96b989
```

The active, actor-owned FIX-005a worktree:

```text
/home/otonom/silbo-fix-005a
branch: codex/fix-005a
governed base: b96b9894378000451966ab2fba3132d29ac80b64
activation commit: d86f5be
implementation target/T: ff5f95904a5dd486d679056ee418b8c13dee699c
handoff/H: e8e614c39ab5dde89236df1b89838e2c745aa317
Fable final review: 13098532098a5882f75c946c9cbc9fa01fa22007
review imports: f93ce5c6bc3513ea553665b4ef903aa0c89ca330, a59e6e741d7461e72073dd9cb79eaa65c63a1fc7
closeout: b803846d6bd00d18fc2c3ee9074971616b47bef3
review state: ACCEPTED — exact quorum PASS
```

No bulk staging, cleanup or implementation is performed in the shared
`/home/otonom/silbo-ai` workspace. **SILBO model code and its remotes are kept
separate from the general AI framework publication.**

### 3.4 The general AI framework GitHub repository

```text
account: furkanhanilci
repository: AI-Research-Framework
visibility: private
default branch: main
remote: https://github.com/furkanhanilci/AETHRION.git
first published commit: 5efd305d52aca1557576e3208668ee9e474344da
```

Before the first push, the tracked files were checked: `.env`, the virtual
environment, SQLite/WAL data, the pytest cache and the projection backups are all
inside `.gitignore`. No common credential or token signature was found in the
tracked files, and the test suite passed.

## 4. The local literature V0 as built

### 4.1 The Zotero connection

- The Zotero Local API is enabled on the local machine.
- The connection runs over `http://127.0.0.1:23119/api`.
- The personal library is **read** only.
- The Bridge holds no Zotero API key and contains no create, update, merge or
  delete operation.
- No human field inside Zotero has been modified.

> ⚠️ **The strength of this claim.** The code contains no write path — that was
> verified by reading it. But **no test proves it**: the
> `zotero_write_enabled` field is a hard-coded constant, so the three artifacts
> that appear to check it are testing `False is False`. See audit finding **H3**.

### 4.2 The Bridge API

- The FastAPI service runs on loopback only.
- A SQLite WAL-based V0 registry is in place.
- Sources are bound by a stable AIRL identifier plus the Zotero item key.
- Re-running the sync does not duplicate a source.
- Health, readiness, listing, search, category and possible-duplicate endpoints
  exist.
- The OpenAPI interface is reachable locally.

> ⚠️ **Known limitation:** ingest is hard-capped at 100 records, with no
> pagination and no incremental `since=` sync. Beyond 100 sources the sync becomes
> **silently partial**. See finding **H1**.

### 4.3 The Obsidian layout

The main working surface:

- [[00 - Home/aethrion_home|AETHRION Home]]

Human-managed areas:

```text
01 - Inbox
10 - Projects
20 - Source Notes
30 - Concepts
40 - Claims
50 - Decisions
60 - Runs
70 - Literature Sets (root)
80 - Daily
90 - Archive
_Templates
```

The generated Zotero view:

```text
70 - Literature Sets/
  Zotero Sources/
    00 - Control Dashboard/
    01 - Journal Articles/           25 sources
    02 - Conference Papers/           2 sources
    03 - Reports and Preprints/       6 sources
```

File names derive from the article title. Where two Zotero items share a title, a
`— Zotero ITEMKEY` suffix prevents the collision.

Control views:

- [[70 - Literature Sets/Zotero Sources/00 - Control Dashboard/Source Catalog|Source Catalogue]]
- [[70 - Literature Sets/Zotero Sources/00 - Control Dashboard/Potential Duplicates|Potential Duplicates]]

### 4.4 Hermes MCP

Hermes sees only these tools:

1. `bridge_status`
2. `search_sources`
3. `get_source`
4. `list_categories`
5. `list_possible_duplicates`

The Hermes side carries an explicit `tools.include` list; MCP prompt and resource
capabilities are disabled. No sync, write, delete or Zotero mutation tool is
exposed.

> The Hermes configuration file lives **outside this repository**, so the
> five-tool restriction could not be verified during the audit.

### 4.5 Automation and operations

- `airl-bridge.service` is active.
- `airl-bridge-sync.timer` is active and waiting.
- The timer calls the local `/v1/sync` every 30 minutes.
- If Zotero is closed, the run records an error and the next timer retries.
- The last successful Obsidian view and the SQLite records are preserved.

### 4.6 Test and acceptance evidence

Last verified results:

```text
Python tests: 20/20 PASS
V0 acceptance: accepted
Source count: 33
Category count: 3
```

A dependency forward-reference warning appears; it is not a test failure and did
not affect acceptance. It should be rechecked on the next dependency update.

> ⚠️ **Both `V0 acceptance` and the MCP smoke check are weaker than they look.**
> The acceptance script depends on a specific paper existing in the user's
> personal library (finding **M3**), and the smoke script asserts nothing and
> exits 0 under all conditions (finding **M2**).

## 5. Steps completed during the local V0

### Step 1 — Existing installation discovery

- Hermes, Zotero, Obsidian and the file paths were examined.
- The Hermes version, model setting, MCP state and gateway state were recorded.
- The Zotero Local API access requirement was identified.

### Step 2 — Zotero Local API activation

- The Zotero setting was backed up and the Local API enabled.
- Zotero was restarted safely.
- The personal library endpoint was verified.

### Step 3 — Bridge API build

- The service project, database, normaliser, projection and CLI were written.
- The local systemd service was installed.
- The first 33 sources were ingested.

### Step 4 — Source naming and classification

- ID-based Obsidian files were moved to title-based names.
- Journal article, conference paper and report/preprint categories were created.
- Collision-free naming was added for identically titled records.
- Possible duplicates are reported, never merged automatically.

### Step 5 — Obsidian information architecture

- The boundaries between human synthesis and automatic projection were defined.
- Templates were created for project, source note, concept, claim, decision, run,
  literature set and daily note.
- The home page was first created as `SILBO AI Main Page`, then renamed to
  `AETHRION Home` on 2026-08-21 to reflect the real scope.
- Zotero sources were moved under `70 - Literature Sets/Zotero Sources` by the
  user's decision.

### Step 6 — Hermes MCP connection

- A read-only MCP adapter was built.
- Hermes discovered the five tools.
- A live status call and a source search were invoked successfully over MCP.

### Step 7 — Periodic sync

- A 30-minute systemd timer was installed.
- The first oneshot run completed with `Result=success` and exit code `0`.

### Step 8 — Versioning and operations documents

- The V0 architecture document and the operations guide were written.
- An end-to-end acceptance script was added.
- A local Git repository and an initial commit were created.
- The old generated tree and the old home page were moved to a recoverable
  backup rather than deleted.

### Steps 9–17 — The SILBO closure queue

Steps 9 through 17 concern the **SILBO product repository**, not the framework:
the FIX-004 review and quorum, the state and queue reconciliation, the general
framework GitHub setup, and the FIX-005a activation, immutable target, sealed
Fable review and acceptance.

Their detail is retained in the SILBO repository's own records. Two things matter
here:

1. **The general framework repository was created and published** (Step 14) as
   `furkanhanilci/AETHRION`, private, with the commissioning plan
   imported.
2. **Nothing in the SILBO chain was verified by the framework audit**, and no
   SILBO acceptance implies any framework acceptance.

## 6. The current managed state of the SILBO product repository

### Accepted history

| Work | Status |
|---|---|
| SILBO-SYS-003 | Accepted under exact Fable quorum |
| SILBO-FIX-002 | Accepted |
| SILBO-FIX-003 | Accepted with exact target/handoff, sealed Fable review and quorum |

### Accepted cycle: SILBO-FIX-004

```text
BASE = 410ef3f83b230ef14564b3a1e5375031af906113
T    = 85625d7a30fd9d77c9179ccff94d08b27ac0b1fd
H    = ddad3abb49e53043e668a597432b9848ad43fb6a
```

Per the implementation and independent review evidence:

- Evaluation: 144/144 PASS
- Runtime: 52/52 PASS
- Do-nothing: 10/10 rejected
- Reference: 10/10 accepted
- Mutation: 15/15 caught
- Archived rescore: 104/104 consistent
- E-F16/E-F20: executable-CLOSED

Fable reproduced these results independently and issued a sealed `APPROVED` for
the exact `T/H/manifest` triple. The review-only commit was taken into the
governed lineage without a byte changing, and the exact quorum verification
returned `PASS`.

One non-blocking `MINOR` finding was recorded: the `executes()` predicate does
not recognise wrapper invocation forms such as `sh -c …`. Since no archive record
uses that form and the standard path is `run_python`, it did not block acceptance;
it is handled as a `CANDIDATE` consistent with the ADR-008 reopen condition.

### Accepted cycle: SILBO-FIX-005a

```text
BASE = b96b9894378000451966ab2fba3132d29ac80b64
T    = ff5f95904a5dd486d679056ee418b8c13dee699c
H    = e8e614c39ab5dde89236df1b89838e2c745aa317
```

FIX-005a protects the repair path, the outcome classification and the
context-isolation boundary that prevents the runtime's internal verification
output leaking into the model context — with mutation-proven tests. Fable
independently produced the same 147/177 result and the 30-entry survivor list,
verified zero semantic Groups 1–3 survivors, and returned a PASS on the exact
T/H/manifest quorum.

Fable's non-blocking F1 finding is that two mutants of the byte-identical
constructor `display_command` guard are untested. It is queued as
AIR-014/SILBO-FIX-005b; it does not reopen 005a and does not block FIX-005/B3.

### Active cycle: SILBO-FIX-005

- The run identity `RUN-FIX005-B3-001` keeps the new and old runs from mixing;
  eight tasks and a twenty-entry seed matrix are pre-registered.
- Only `max_tokens_per_task` is doubled; all other budgets are preserved and the
  aggregate inference limit is 10,800 seconds.
- On resume, the runner fail-closed verifies the task/endpoint/envelope/budget
  identity and the capsule bytes; it never overwrites the older output.
- The report produces the post-repair `write_file`, the completed second internal
  `run_shell` verification, the exit reason, and the pre/post/total token and wall
  time fields.
- A missing verification receipt or an unrelated internal tool call does not count
  as a measurement; without the second verification the decision is necessarily
  `REPAIR_NOT_MEASURED`.
- In addition to the local GGUF SHA-256 and the endpoint model identity, the
  `system_fingerprint` of the first model response is frozen; any drift during the
  run or the report halts the process fail-closed.
- As of 2026-08-21: `py_compile` and 11/11 focused unit tests PASS; the five-file
  local target was frozen as `b14b0b34a115e7cc088008d0a29cf1769f912169`.
- The exact target was mutation-proven in a clean detached worktree: baseline and
  final 11/11 PASS, 8/8 named mutants caught, sources restored byte-exact every
  round. Raw JSON SHA-256 `e142bf74e6df455eef0e11a535c2063f0a17c9a690c607e38903a2f7763b3f54`.
- On the same detached target, the full evaluation 155/155 and runtime 72/72 PASS.

### Known open guard

`G6` is red because of 9/21 unresolved provenance facts in the SILBO-FIX-006
scope. The last preflight showed this as an explicit waiver and found no other
unwaived guard failure.

### The publication subsystem

The isolated publication subsystem is implemented and mutation-tested, but it has
neither an independent Fable review nor integration into the main line. **None of
the six candidate papers is READY.**

## 7. Comparison matrix against the full AETHRION programme

| Programme area | Actual current state | Main remaining scope |
|---|---|---|
| `00_PROGRAM` | Plan files exist | Charter acceptance, owners, budget, gate and evidence registry operation |
| `01_GOVERNANCE` | Some role/review controls exist inside the SILBO repository | WP-001–010 formal acceptance |
| `02_CONTRACTS` | V0 models and some repository contracts exist | WP-011–020 schema registry and authority contracts |
| `03_FOUNDATION` | A local Git/SQLite/systemd prototype exists | PostgreSQL HA, object store, NATS, OCI/CI, derived models |
| `04_CONTROL_EVENT` | Not built | Temporal, G0–G10, GateRecord, replay/DLQ |
| `05_MODEL_AGENT_TOOL` | Hermes MCP V0 exists | LiteLLM, capability/model admission, LangGraph, Tool Broker |
| `06_EXECUTION_SECURITY` | Bubblewrap evidence exists in SILBO | Kubernetes, Kueue, gVisor, SPIFFE/Vault, OPA, egress/DLP |
| `07_LITERATURE_KNOWLEDGE` | A working local V0 exists | PostgreSQL registry, resolver, annotations, manifest freeze, write-back |
| `08_EVIDENCE_ASSURANCE` | The SILBO evidence protocol is partly strong | Claim Ledger, MLflow, clean-room reproduction, review/publish packages |
| `09_EXPERIENCE_OBSERVABILITY` | Obsidian and local dashboards exist | Cockpit, telemetry, Langfuse, Grafana, cost ledger, SLOs |
| `10_INTEGRATION_CUTOVER` | Local V0 acceptance exists | WP-102–121 and ACC-01–ACC-51 commissioning |
| `11_DAY2_OPERATIONS` | A timer/runbook V0 exists | DR, incident handling, requalification, continuous assurance |
| `13_TOOLING_INTEGRATION` | Designed (WP-131–140) | Notification Broker, channel ceilings, external records, evidence sealing, liveness |

## 8. The forward execution plan

### Phase A — Close the existing SILBO queue safely

Steps 1–16 are complete (FIX-004 review, quorum, reconciliation; FIX-005a
activation through acceptance; the FIX-005 challenge and activation).

17. **Implement the runner/report contract with the new run identity and the
    fail-closed capsule; after test and mutation evidence, freeze the dry-run
    pre-registration commit.** `IN_PROGRESS — target b14b0b3; 11/11, 8/8 mutation,
    evaluation 155/155, runtime 72/72 PASS; dry-run NEXT`
18. If readiness passes, run the B3 measurement on the same eight tasks and twenty
    seeds within a three-hour aggregate limit.
19. Handle FIX-006, FIX-006b, FIX-007, FIX-008 and the remaining FIX-009 family in
    order.
20. Do not start new GPU training until the instrument/security queue is closed.

### Phase B — Begin formal commissioning

The AIRL plan states explicitly that the first formal package is
`WP-001 Commissioning Charter`. **The existing V0 will not be declared ACCEPTED
retrospectively.** First:

0. **WP-000 Interim Evidence Policy** — without it no package can ever reach
   `ACCEPTED` (audit finding **C1**).
1. Named accountable owner and independent verifier assignment — and a written
   decision on what "independent" means in a one-person organisation (finding
   **C2**).
2. Freeze the system boundary, NFRs, risks and human decision rights.
3. Decide environment, budget, data class and execution profile.
4. The evidence manifest and the package status registry.
5. Independent acceptance of WP-001.

### Phase C — The contract and foundation wave

1. WP-011–020: identity, canonical authority and schema contracts — **and at
   least one production consumer for the contract core** (finding **H4**).
2. WP-021–024: environment, repository and CI quality gates — **CI first**, since
   it closes four findings at once (finding **H5**).
3. WP-025–030: PostgreSQL, object store, NATS/outbox, MLflow and derived read
   models.

A controlled migration and rollback plan will be prepared for the SQLite V0 data;
no direct production data migration will be performed.

### Phase D — Control, agent and security planes

1. The Temporal-based G0–G10 control flow.
2. Event, replay and DLQ behaviour.
3. LiteLLM and the Capability Registry.
4. LangGraph, only for bounded cognitive tasks.
5. The Tool Broker and the Execution Broker.
6. Trust zones, sandboxing, workload identity, OPA and egress policy.

### Phase E — Raise literature V0 to a formal platform

1. Move the SQLite records into the canonical PostgreSQL Source Registry.
2. Add DOI/identity resolution and dedup/merge decision records.
3. Add selected-collection/tag opt-in and the incremental `since` reader
   (finding **H1**).
4. Add deletion reconciliation and tombstones (finding **H2**).
5. Normalise attachment, note and annotation bindings.
6. Add `LiteratureSetManifest` freezing and the immutable object store.
7. Produce Obsidian link integrity, human-preservation diff and full rebuild
   evidence.
8. Consider Zotero write-back only under a separate authority, a group library
   and an audit policy.

### Phase F — Evidence, experience and observability

1. The Claim/Evidence Ledger.
2. Evidence locators and the citation entailment audit.
3. The Run Registry and MLflow.
4. Frozen review and clean-room reproduction packages.
5. The cockpit, the decision queue and the literature workbench.
6. OpenTelemetry, Langfuse, Grafana, the cost ledger and SLOs.

### Phase G — Integration, commissioning and production

1. WP-102–108 vertical slices.
2. WP-109–118 acceptance registry, security, DR, performance and operational
   readiness.
3. Running ACC-01–ACC-51 on the same target.
4. At least two restore drills.
5. Zero open critical findings.
6. A pilot cutover rehearsal.
7. A human-approved production cutover and hypercare.

## 9. Authority boundaries requiring a human decision

The following are never done autonomously:

- Pushing or merging to any repository other than the authorised
  `furkanhanilci/AETHRION`.
- Production deployment, or exposing an API to an external network.
- Writing to, deleting from, or automatically merging Zotero records.
- Large dependency downloads or opening cloud resources.
- Long GPU training, model conversion or quantisation.
- Data migration, irreversible migration or artifact deletion.
- Any policy choice that affects human decision rights.

Each is carried out separately, after its exact target, rollback, cost and
acceptance evidence have been defined.

**The only authorised remote for the general framework is
`furkanhanilci/AETHRION`.** The SILBO model repository is a separate
workflow with a separate authority boundary; framework commits are never sent
there.

## 10. Principal risks and controls

| Risk | Control |
|---|---|
| Mistaking V0 for the full system | The programme matrix and explicit status semantics |
| Overwriting human Obsidian notes | The generated-branch boundary and manifest-owned deletion |
| Modifying Zotero data | A read-only adapter and the absence of any write tool |
| Wrongly merging duplicate sources | Reporting only; no automatic merge |
| Agent self-approval | Exact Fable review and quorum |
| A stale status document | Git SHAs, executable guards and artifact precedence |
| A test measuring the wrong thing | Two-directional tests and a mutation requirement |
| Damage to a shared worktree | Actor-owned worktrees and narrow Git operations |
| Premature expensive infrastructure or training | Dependency and resource gates |
| Moving to production too early | The 40 ACCs, restore drills and the critical-findings condition |
| **Evidence theatre** | **Behavioural tests instead of constants; asserting smoke checks; CI** (findings H3, M2, M3, H5) |

## 11. Rollback and backup state

The previous Obsidian layout is kept in a local backup:

```text
/home/otonom/Desktop/FH/AETHRION/
  data/projection-backups/
```

Bridge database and WAL files are kept out of Git. The source copies of the unit
files live under `deploy/`. The V0 code is recoverable from local Git commits.

> ⚠️ The projection backups are in `.gitignore` — **they are neither version
> controlled nor backed up**, while `OPERATIONS.md` presents them as the official
> rollback point. See the audit, Section H.

## 12. The update protocol after every step

When a material step completes, apply this order:

1. Verify the relevant command, test or artifact output.
2. Change this document's `updated_at` field.
3. Revise the executive summary and the status table.
4. Update the relevant phase or step status.
5. Add the new evidence, commit, target, handoff or review SHA.
6. Record any new risk, limitation or rollback information.
7. Update the "Next exact step" section as a **single executable action**.
8. Add a row to the change log below.
9. Verify that the Obsidian copy and the Git baseline copy are identical.

Every step is labelled explicitly `PASS`, `PARTIAL`, `BLOCKED` or `FAIL`. **A
partial success never hides its failing sub-items.**

## 13. Change log

| Time | Step | Status | Evidence / note |
|---|---|---|---|
| 2026-08-21 | Local literature V0 build | PASS | 33 sources, Bridge, Obsidian, Hermes MCP |
| 2026-08-21 | Obsidian folder and naming revision | PASS | Zotero sources under Literature Sets |
| 2026-08-21 | Timer and operations baseline | PASS | First oneshot success, Git `15d57af` |
| 2026-08-21 | SILBO continuity and snapshot check | PASS | H `ddad3ab`, protocol and attestation PASS |
| 2026-08-21 | FIX-004 Fable review completed | APPROVED | Review `efb87f2`, sealed exact T/H, review file only |
| 2026-08-21 | FIX-004 exact review quorum | ACCEPTED | `status: PASS`, `errors: []`, reviewer `fable` |
| 2026-08-21 | Ledger/queue/state reconciliation | PASS | Local commit `b96b989`; preflight PASS |
| 2026-08-21 | General private repository created | PASS | `furkanhanilci/AETHRION` |
| 2026-08-21 | First framework push | PASS | `main=5efd305`; tests and secret/ignore checks |
| 2026-08-21 | Commissioning plan published | PASS | Private remote; the full plan tree |
| 2026-08-21 | FIX-005a local activation | PASS | Worktree/branch, task/state, preflight; commit `d86f5be` |
| 2026-08-21 | FIX-005a immutable target | PASS | `T=ff5f959`; 147/177 caught, 30 attributed, Group 0, named 41/41 |
| 2026-08-21 | FIX-005a sealed Fable review | APPROVED WITH FOLLOW-UP | `1309853`; follow-up non-blocking, 0 subject edits |
| 2026-08-21 | FIX-005a exact coordinator quorum | PASS / ACCEPTED | `errors: []`; exact T/H/manifest, reviewer `fable` |
| 2026-08-21 | Fable F1 follow-up recorded | WRITTEN / NON-BLOCKING | AIR-014 / SILBO-FIX-005b; does not reopen 005a |
| 2026-08-21 | FIX-005 local activation | PASS | `codex/fix-005`, commit `f598869`; G6 waived only for FIX-006 |
| 2026-08-21 | FIX-005 local measurement target | PASS / MUTATION PENDING | `b14b0b3`; 5 files, clean diff-check, clean worktree |
| 2026-08-21 | FIX-005 detached mutation evidence | PASS | Exact `b14b0b3`; 11/11 baseline and final, 8/8 mutants caught |
| 2026-08-21 | FIX-005 full test suites | PASS | Exact `b14b0b3`; evaluation 155/155, runtime 72/72 |
| 2026-08-21 | FIX-005 pre-inference capsule and readiness | PASS / INFERENCE GATED | Capsule CREATED→BYTE_IDENTICAL, drift rejection; `inference_started=false` |
| 2026-08-21 | Full commissioning plan imported into Obsidian | PASS | The full plan tree plus the section index |
| 2026-08-21 | Plan navigation and step memory | PASS | The Navigation and Execution Cockpit |
| 2026-08-22 | Step 001 foundation/contract core | TECH_COMPLETE / REVIEW PENDING | WP-011/014/015/020; 20 tests PASS |
| 2026-08-22 | **Step 001 correction — WP-022 claim retracted** | **CORRECTED** | The deliverable was not in the repository; status returned to `NOT_STARTED` (finding **C3**) |
| 2026-08-22 | Step 003 independent audit | DESIGN_PROPOSED | Audit report, ideal structure, skill layer, role→model assignment |
| 2026-08-22 | Step 003 — 38 skills written | DESIGN_PROPOSED | `skills/`; not yet baseline-tested |
| 2026-08-22 | Step 006 — 49 skills, two families, Agent Skills format, WP-000 written | DESIGN_PROPOSED | Format conformance is mechanically checked; **behaviour still untested** |
| 2026-08-22 | Step 007 — commissioning **baseline v1.0**: skill layer bound into the plan, ACC-41–46, eight architectural corrections | DESIGN_PROPOSED | First baseline to commission against; **nothing executed yet** |
| 2026-08-22 | Step 003 — WP-131–140 added | PASS | `13_TOOLING_INTEGRATION`; measurable acceptance criteria |
| 2026-08-22 | **Step 004 — full English revision** | **PASS** | 140 WPs, 40 ACCs, 12 programme documents, 5 architecture/review documents, the vault; mirror generators added; 20 tests PASS; plan re-sealed |
| 2026-08-22 | **Step 005 — file-by-file repository review** | **PASS** | Module docstrings across `src/` and `tests/`; findings **M2** and **M3** closed (smoke check now exits 1 when the Bridge is down; acceptance is data-independent); `FOUNDATION.md` stub replaced; SILBO naming removed from the units; four broken programme references fixed; ACC severity rules made severity-aware |

## 14. Next exact step

**Settle the role → model assignment** (`AETHRION_ROLE_MODEL_ASSIGNMENT.md`,
Section 3): for every role, human / model / deterministic code / deferred.
Without that decision the Independence Matrix cannot be measured, the R classes
cannot be applied, and the skills cannot enter baseline testing.

Immediately after it, in order:

1. Rename `model_snapshot` → `capability_fingerprint` (Invariant 4 cannot hold
   with a hosted model).
2. Write **WP-000 Interim Evidence Policy** (finding **C1** — without it no
   package can be accepted).
3. Stand up the **CI foundation** (finding **H5** — it closes four findings and
   automates evidence production).

On the SILBO line, separately: prepare the independent Fable review and handoff
against exact `b14b0b34a115e7cc088008d0a29cf1769f912169`; **do not start inference
before that review completes.** No push is made to the SILBO model repository.
