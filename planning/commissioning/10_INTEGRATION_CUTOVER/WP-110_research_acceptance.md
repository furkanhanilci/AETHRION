# WP-110 — Research and Literature Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-110` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Citation Auditor / Assurance |
| Hard dependencies | WP-103, WP-104, WP-105, WP-106, WP-108, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-EPI-01, CTL-LIT-01, CTL-GOV-02 |
| Related acceptance scenarios | ACC-01..ACC-08 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-110_research_acceptance.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-110_research_acceptance.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The human seed, agent write-back, duplicate, retraction, injection, self-approval, order bias and counter-test scenarios close with complete evidence.


## Analysis
### What this package actually decides

Whether the research invariants hold under adversarial conditions. Eight scenarios
— ACC-01 through ACC-08 — and they are chosen to attack the epistemic layer rather
than the infrastructure.

### The four that matter most

**`ACC-05` prompt injection through a PDF.** The Bridge's MCP server documents this
gap against itself today, and its mitigation is *not implemented yet*. This is where
it is closed and demonstrated.

**`ACC-06` plan self-approval.** Can a producer approve their own work through any
path? This is ADR-001's control tested rather than declared, and in a solo
laboratory it is the scenario most likely to reveal that independence is procedural.

**`ACC-07` reviewer order bias.** WP-088 randomises finding order. This is where the
randomisation is shown to matter.

**`ACC-08` strong counter-test.** Does the system produce and act on disconfirming
evidence, or does it accumulate support? `PR-12`'s *false rigor* lives here.

### One release candidate, no parallelism (T02)

`00_PROGRAM/05`: all criteria pass **on the same target revision**. Running
scenarios in parallel introduces shared-state interference that produces failures
nobody can attribute — and a controlled serial run is slower and interpretable.

### Critical findings must be reproduced, not triaged away (T04)

`00_PROGRAM/06`: a critical finding cannot be closed as *probably a false positive*
— a reproducer result is required. Six of these eight scenarios are Critical.

### Baseline v1.3.0 — the slices exercise the cohort, and the regression injects faults

The vertical slices and the cutover path grow to cover what this baseline adds,
and one package changes character.

**WP-107 becomes the engineering completion slice.** Requirement and
specification → worktree → TDD → code review → CI → supply-chain attestation →
signed artifact → **eligibility to produce scientific evidence**. That last arrow
is the junction between the two disciplines, and before this baseline nothing
proved it end to end.

**The other slices exercise the collaboration plane**: a compiled cohort, sealed
initial positions, typed delta exchange over a sparse topology, an adaptive
assurance route, a fingerprinted reproduction and a firewalled benchmark run.

**The regression suite gains injections rather than cases.** Faulty agent,
malicious agent, split brain, duplicate and out-of-order events, communication
degradation under budget pressure, and benchmark contamination. These are
failures that are invisible in a healthy run and obvious only in a post-mortem,
which is why they are caused deliberately rather than waited for.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze](../10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.md) | `Literature vertical dossier` · `Frozen LiteratureSetManifest` · `Zotero SyncReceipts` · `Coverage/screening report` |
| [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_vertical_slice_run_claim.md) | `Run/claim vertical dossier` · `Run manifests/artifacts` · `Claim/Evidence records` · `Cost/trace/audit evidence` |
| [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.md) | `Review/repro vertical dossier` · `ReviewRecords/DisagreementCase` · `ReproductionReport` · `Gate histories` |
| [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.md) | `Decision/publish/monitor dossier` · `DecisionRecord` · `PublicationPackage` · `ImpactCase/Supersession` |
| [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md) | `Impact vertical dossier` · `ImpactCase set` · `Affected-object accuracy report` · `Supersession/re-evaluation records` |
| [WP-109 — Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md) | `Acceptance Registry` · `Scenario runner` · `Fixture catalog` · `Evidence capture/signing` |

### Full prerequisite closure

**110 of 160 packages (69%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` · `WP-154` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-115`
- **Transitively reachable:** **16 of 160 packages (10%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **47** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Research Director |
| Independent verifier | Citation Auditor / Assurance |
| Gates touched | `Commissioning` |
| Controls | `CTL-EPI-01` · `CTL-LIT-01` · `CTL-GOV-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-80 — Governed Versus Ungoverned Research Harness](../12_ACCEPTANCE_SCENARIOS/ACC-80_governed_versus_ungoverned_harness.md) | Medium | The harness emits the task and integrity metrics for both, reproducibly, with the cost of each recorded. A worse governed task score is a valid published result and is not suppressed. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze](../10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.md), [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_vertical_slice_run_claim.md), [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.md), [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.md), [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md), [WP-109 — Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Literature vertical dossier` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Frozen LiteratureSetManifest` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Zotero SyncReceipts` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Coverage/screening report` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Run/claim vertical dossier` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Run manifests/artifacts` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Claim/Evidence records` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Cost/trace/audit evidence` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Review/repro vertical dossier` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `ReviewRecords/DisagreementCase` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `ReproductionReport` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `Gate histories` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `Decision/publish/monitor dossier` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `DecisionRecord` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `PublicationPackage` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `ImpactCase/Supersession` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `Audit export` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `Impact vertical dossier` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `ImpactCase set` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Affected-object accuracy report` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Supersession/re-evaluation records` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Acceptance Registry` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Scenario runner` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Fixture catalog` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Evidence capture/signing` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Result dashboard` | `WP-109` | `python3 scripts/progress.py show WP-109` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Research Director** carries the acceptance decision; **Citation Auditor / Assurance** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-030` — ResearchClawBench — end-to-end autonomous research benchmark | `BENCHMARK` | a measurement of this system — nothing enters it | the contract this is held behind | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-030` | Measures the governed-versus-ungoverned experiment. Never a gate. | Any runtime dependency. |

### Where a plain row would mislead

- **`ASM-030`** — Already registered in AETHRION_COMPONENT_REUSE.md §4; the pinned facts are recorded here. 40 tasks across 10 domains, each grounded in a real published paper with the target paper hidden and expert-curated weighted rubrics. Published headline results — strongest autonomous agent 21.5, strongest harness LLM 20.7, frontier mean 26.5 — set the scale against which any AETHRION result must be read.

### Unresolved before implementation

**None.** Every obligation the modes above create has been met.

**Acquisition readiness — resolved.** All 1 registered sources have met the obligations their modes create.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-110-T01 | Reset the ACC-01 to ACC-08 fixtures | Implementation owner | Commit / configuration / record reference |
| WP-110-T02 | Execute a controlled, non-parallel run on the same release candidate | Implementation owner | Commit / configuration / record reference |
| WP-110-T03 | Verify the expected Registry, Zotero, Ledger, Gate and Audit outcomes | Implementation owner | Commit / configuration / record reference |
| WP-110-T04 | Run critical-finding triage, reproduction and correction | Implementation owner | Commit / configuration / record reference |
| WP-110-T05 | Produce the research acceptance dossier and obtain owner sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ACC-01–08 results`
- `Research acceptance dossier`
- `Finding/disposition records`
- `Owner sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-110_research_acceptance.tests.md`](WP-110_research_acceptance.tests.md).

- ACC-01 through ACC-08
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-110_research_acceptance.acceptance.md`](WP-110_research_acceptance.acceptance.md), together with what this package still cannot establish.

- [ ] All eight scenarios PASS.
- [ ] No open critical or high research finding remains.
- [ ] The manifest, claim, reviewer and source integrity queries all complete.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

A failure blocks cutover; fixture state is cleaned and, after correction, the regression set — not only the affected scenario — is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
