---
title: "WP-127 — FinOps, Capacity and Portfolio Review Rhythm"
aliases:
  - "WP-127"
  - "WP-127 — FinOps, Capacity and Portfolio Review Rhythm"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Monthly invoice reconciliation, forecasting, quality-adjusted cost versus outcome, queue capacity, model mix and stop/pivot portfolio decisions become permanent practice."
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-127_finops_portfolio.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g0
  - aethrion/gate/g4
  - aethrion/gate/g8
  - aethrion/gate/day-2
  - aethrion/state/not-started
---

# WP-127 — FinOps, Capacity and Portfolio Review Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-127` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | FinOps Lead / Research Director |
| Independent verifier | Internal Audit / Assurance |
| Hard dependencies | WP-100, WP-117, WP-121 |
| Related gates | G0,G4,G8,Day-2 |
| Related controls | CTL-CST-01, CTL-CST-02 |
| Related acceptance scenarios | — a Day-2 rhythm is exercised in operation, not as a go-live gate |
| Recurring counterpart of | ACC-09, ACC-29 — those scenarios verify the **initial** qualification before cutover; this package owns the **recurring** one afterwards |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_127_finops_portfolio.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_127_finops_portfolio.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Monthly invoice reconciliation, forecasting, quality-adjusted cost versus outcome, queue capacity, model mix and stop/pivot portfolio decisions become permanent practice.


## Analysis
### What this package actually decides

Whether the portfolio is worth what it costs. Monthly reconciliation, forecasting,
quality-adjusted cost against outcome, and — the part with teeth — **stop/pivot
decisions for low-value, high-cost projects**.

### The stop decision is the package (T05)

Everything else is measurement. `00_PROGRAM/01`'s KPI requirement includes
stop/pivot conditions, and WP-001 makes them falsifiable. This is where they are
applied to real projects with real sunk cost — and sunk cost is one of the five
pressure conditions WP-043 tests skills against for exactly this reason.

### Expected value of verification is the unusual analysis (T03)

How much did verification cost, and what did it catch? A programme that spends more
on review than the errors review prevents has a real problem, and one that spends
too little has a different one.

Neither is visible without measuring both — and `00_PROGRAM/08` protects the
assurance pool precisely because this calculation, done naively, always favours
cutting it.

### Quality-adjusted cost is what makes model choices comparable (T03)

WP-044 admits on incremental value; WP-045 routes on quality-adjusted cost. This is
where the production numbers feed back, and where a cheaper model that produces
more rework is exposed.

### Invoice reconciliation is the ledger's honesty check (T01)

Provider bills against internal accounting. A variance with an owner (WP-100) is the
control; this is the cadence.

### Queue capacity planning connects cost to the human constraint (T04)

Queue wait, headroom and the human attention quota. A forecast that grows
throughput without growing decision capacity has forecast a `PR-04`.

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

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |
| [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md) | `Load test suite/results` · `Capacity model` · `Bottleneck/tuning report` · `Cost/headroom forecast` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |

### Full prerequisite closure

**121 of 160 packages (76%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
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
| Accountable owner | FinOps Lead / Research Director |
| Independent verifier | Internal Audit / Assurance |
| Gates touched | `G0` · `G4` · `G8` · `Day-2` |
| Controls | `CTL-CST-01` · `CTL-CST-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) | Critical | An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created. |
| [ACC-29 — Provider Invoice Variance](../12_ACCEPTANCE_SCENARIOS/acc_29_invoice_variance.md) | Medium | A `VarianceCase` opens with a provider/project/model/time-bucket breakdown, an owner, an SLA and an adjustment or dispute path; ledger history is never deleted. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
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
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Token ledger categories` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Load test suite/results` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity model` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Bottleneck/tuning report` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Cost/headroom forecast` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity sign-off` | `WP-117` | `python3 scripts/progress.py show WP-117` |
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
- **FinOps Lead / Research Director** carries the acceptance decision; **Internal Audit / Assurance** must verify independently of whoever implements.
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
| WP-127-T01 | Run the invoice, provider, compute and storage reconciliation | Implementation owner | Commit / configuration / record reference |
| WP-127-T02 | Produce the project and outcome budget variance and forecast | Implementation owner | Commit / configuration / record reference |
| WP-127-T03 | Analyse model/agent fan-out and the expected value of verification | Implementation owner | Commit / configuration / record reference |
| WP-127-T04 | Update the capacity, headroom and queue-wait plan | Implementation owner | Commit / configuration / record reference |
| WP-127-T05 | Record the stop/pivot decision for low-value, high-cost projects | Implementation owner | Commit / configuration / record reference |
| WP-127-T06 | Trigger the annual cost policy benchmark and reopen | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Monthly FinOps report`
- `Invoice cases`
- `Portfolio decision records`
- `Capacity forecast`
- `Optimization backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-127_finops_portfolio.tests.md`](wp_127_finops_portfolio.tests.md).

- An invoice variance sample
- A hard budget event audit
- Cost allocation completeness
- A quality-adjusted route comparison
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-127_finops_portfolio.acceptance.md`](wp_127_finops_portfolio.acceptance.md), together with what this package still cannot establish.

- [ ] Cost is never optimised on token price alone.
- [ ] The human cost of assurance is visible in the report.
- [ ] Every budget override carries a named decision and an expiry.
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

A wrong allocation is fixed through a reconciliation adjustment; historical invoices and ledger events are never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
