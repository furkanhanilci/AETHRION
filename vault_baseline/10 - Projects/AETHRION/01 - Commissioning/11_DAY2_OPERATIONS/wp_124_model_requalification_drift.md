---
title: "WP-124 — Model Requalification, Drift and Ejection Rhythm"
aliases:
  - "WP-124"
  - "WP-124 — Model Requalification, Drift and Ejection Rhythm"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A change in model snapshot, provider behaviour, evaluation quality, latency, cost, safety or data contract produces periodic requalification and, where warranted, ejection."
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-124_model_requalification_drift.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g10
  - aethrion/gate/day-2
  - aethrion/state/not-started
---

# WP-124 — Model Requalification, Drift and Ejection Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-124` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Admission Board / Safety / FinOps |
| Hard dependencies | WP-042, WP-043, WP-044, WP-045, WP-108, WP-121 |
| Related gates | G10,Day-2 |
| Related controls | CTL-MOD-01, CTL-MOD-02 |
| Related acceptance scenarios | — a Day-2 rhythm is exercised in operation, not as a go-live gate |
| Recurring counterpart of | ACC-10, ACC-11, ACC-36 — those scenarios verify the **initial** qualification before cutover; this package owns the **recurring** one afterwards |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_124_model_requalification_drift.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_124_model_requalification_drift.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A change in model snapshot, provider behaviour, evaluation quality, latency, cost, safety or data contract produces periodic requalification and, where warranted, ejection.


## Analysis
### What this package actually decides

That a model's admission expires. `00_PROGRAM/09` states the rule this operates: *a
model alias change is not accepted as a pinned snapshot; requalification is
required.* And `00_PROGRAM/01` invariant 7: a snapshot change produces
requalification **and an explicit task impact assessment**.

### Drift is the failure this catches, and it is silent (T03)

A provider changes a model behind a stable name. Nothing errors. Outputs shift
slightly, validated precision drops, and the first visible symptom is a reviewer
disagreeing more often — months later.

Production drift analysis is the only thing that sees it between scheduled
requalifications.

### Requalification is not the initial admission repeated (T02)

The initial admission (WP-044) established fitness against a baseline. Requalification
asks a different question: **has this profile's performance changed**, measured
against its own prior results as well as the incumbent's.

That makes the regression sets more important than the golden sets here.

### Ejection has to reach open work (T05)

Suspending a profile changes nothing for the tasks already running under it. The
impact scan over open tasks, runs and claims is what makes ejection real, and the
router cache must be invalidated or the profile keeps being selected.

### The provider change monitor is the cheap half (T01)

Provider changelogs, deprecation notices and fingerprint shifts. `monitoring-external-feeds`
is the skill; this is the cadence.

### Baseline v1.3.0 — Day-2 measures what this baseline added

The recurring rhythms gain six subjects, each of which is a number that only
means something when tracked over time:

- **Multi-agent efficiency** — coordination overhead against the naive
  fully-connected baseline, and whether the optimisation still holds.
- **Verifier calibration** — precision, recall, **abstention rate** and error
  correlation between verifier families, requalified on a schedule.
- **Source and upstream drift** — pinned mechanisms whose upstream moved, and
  sources whose status changed.
- **Supply-chain posture** — OSV and Scorecard findings, and residual risks that
  reached their expiry.
- **Failure taxonomy distribution** — including how often attribution returned
  `UNKNOWN`, which is a system-health signal rather than a defect count.
- **The Pareto frontier** — quality against cost, so an optimisation that stopped
  paying is visible.

Incident learning consumes the typed `FailureAssessment` and retains negative
results. A failed approach that is deleted is a lesson the next campaign pays for
again.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md) | `Capability Registry service` · `Profile state machine` · `Eligibility API` · `Expiry/revoke scheduler` |
| [WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md) | `Eval dataset manifests` · `Role eval harness` · `Grader/rubric bundle` · `Contamination controls` |
| [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md) | `Qualification pipeline` · `Admission dossier` · `CapabilityProfile update` · `Regression schedule` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |
| [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/wp_108_retraction_drift_vertical_slice.md) | `Impact vertical dossier` · `ImpactCase set` · `Affected-object accuracy report` · `Supersession/re-evaluation records` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |

### Full prerequisite closure

**122 of 160 packages (76%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 47 | `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` |
| 48 | `WP-115` |
| 49 | `WP-116` · `WP-117` |
| 50 | `WP-118` |
| 51 | `WP-119` |
| 52 | `WP-120` |
| 53 | `WP-121` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-130`
- **Transitively reachable:** **1 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W9 — Day-2 |
| Dependency depth | level **54** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Eval Office |
| Independent verifier | Admission Board / Safety / FinOps |
| Gates touched | `G10` · `Day-2` |
| Controls | `CTL-MOD-01` · `CTL-MOD-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/wp_108_retraction_drift_vertical_slice.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Capability Registry service` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Profile state machine` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eligibility API` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Expiry/revoke scheduler` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eval dataset manifests` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Role eval harness` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Grader/rubric bundle` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Contamination controls` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Eval scorecard` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Cross-model × cross-harness compliance matrix` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Qualification pipeline` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Admission dossier` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `CapabilityProfile update` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Regression schedule` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Ejection procedure` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Fingerprint and abstention scope on qualification records` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Impact vertical dossier` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `ImpactCase set` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Affected-object accuracy report` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Supersession/re-evaluation records` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Hypercare log` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Incident/finding summary` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Production KPI baseline` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Day-2 handoff` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Program closure report` | `WP-121` | `python3 scripts/progress.py show WP-121` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Eval Office** carries the acceptance decision; **Admission Board / Safety / FinOps** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-124-T01 | Operate the profile expiry calendar and the provider change monitor | Implementation owner | Commit / configuration / record reference |
| WP-124-T02 | Run the role regression and adversarial evaluations | Implementation owner | Commit / configuration / record reference |
| WP-124-T03 | Analyse production validated precision, quality and cost drift | Implementation owner | Commit / configuration / record reference |
| WP-124-T04 | Manage the SHADOW → admission and admitted → suspend/eject decisions | Implementation owner | Commit / configuration / record reference |
| WP-124-T05 | Run the open task/run/claim impact scan and invalidate the router cache | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Requalification reports`
- `CapabilityProfile decisions`
- `Drift/ejection events`
- `ImpactCase results`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-124_model_requalification_drift.tests.md`](wp_124_model_requalification_drift.tests.md).

- A silent snapshot change
- Quality, latency and cost drift
- A safety or data-contract change
- No eligible route remaining after an ejection
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-124_model_requalification_drift.acceptance.md`](wp_124_model_requalification_drift.acceptance.md), together with what this package still cannot establish.

- [ ] An expired profile leaves the routing pool automatically.
- [ ] An ejection does not alter past runs but does produce an impact assessment.
- [ ] A newly popular model does not enter a role without evaluation.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

A wrong ejection can be superseded by a `DecisionRecord`; re-admission still requires fresh evidence.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
