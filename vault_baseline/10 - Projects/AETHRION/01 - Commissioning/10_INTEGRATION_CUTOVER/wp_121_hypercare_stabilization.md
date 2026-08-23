---
title: "WP-121 — Hypercare, Stabilisation and Programme Closure"
aliases:
  - "WP-121"
  - "WP-121 — Hypercare, Stabilisation and Programme Closure"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "After go-live, intensive observation, fast incident and reconciliation handling, SLO/cost/quality measurement and explicit exit criteria hand the system over to normal Day-2 operations."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w8
  - aethrion/effort/m
  - aethrion/gate/cutover
  - aethrion/gate/day-2
  - aethrion/state/not-started
---

# WP-121 — Hypercare, Stabilisation and Programme Closure

## Package card

| Field | Value |
|---|---|
| Work package | `WP-121` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead / Program Lead |
| Independent verifier | Executive Sponsor / Assurance |
| Hard dependencies | WP-120 |
| Related gates | Cutover,Day-2 |
| Related controls | All controls |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_121_hypercare_stabilization.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_121_hypercare_stabilization.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

After go-live, intensive observation, fast incident and reconciliation handling, SLO/cost/quality measurement and explicit exit criteria hand the system over to normal Day-2 operations.


## Analysis
### What this package actually decides

When intensive supervision ends. Hypercare exists because the first weeks after
cutover have a different failure profile: the system is new, the operators are
learning it, and the drift that Day-2 processes catch monthly can accumulate
daily.

### Exit criteria must be defined before hypercare starts (T06)

Otherwise hypercare ends when everyone is tired. The criteria are observables —
SLO stability over a window, error budget consumption, incident rate, and the
quality KPIs from WP-001's charter — and they are the same numbers Day-2 will keep
watching.

### The quality KPI baseline is the part that outlasts hypercare (T05)

`00_PROGRAM/08` names the anti-metrics: G10 reversal rate,
acceptance-despite-adversarial-rejection, and the decision-time distribution. A
baseline established during hypercare is what every later measurement is compared
against, and establishing it badly makes drift undetectable for a year.

### Rollback authority stays with hypercare, not with the change process (T03)

During hypercare a rollback is a normal response, not an incident. Making that
explicit is what prevents a team from working around a problem rather than
reverting it.

### Knowledge capture is the deliverable nobody schedules (T04)

The operators learn things during hypercare that exist nowhere else. Capturing them
into runbooks and the vault before the rota disperses is the difference between an
organisation that learned and one where a person did.

### The handoff must be to a named owner (T06)

`00_PROGRAM/09` and WP-101 both require it: a service with no owner cannot be
released, and the same applies to the system as a whole entering Day-2.

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

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-120 — Production Cutover and Go-Live Decision](../10_INTEGRATION_CUTOVER/wp_120_production_cutover.md) | `Cutover execution log` · `Go-Live DecisionRecord` · `Production release manifest` · `Smoke/integrity results` |

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

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-122` · `WP-123` · `WP-124` · `WP-125` · `WP-126` · `WP-127` · `WP-128` · `WP-129` · `WP-130`
- **Transitively reachable:** **9 of 160 packages (6%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W8 — Cutover |
| Dependency depth | level **53** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | SRE Lead / Program Lead |
| Independent verifier | Executive Sponsor / Assurance |
| Gates touched | `Cutover` · `Day-2` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-120 — Production Cutover and Go-Live Decision](../10_INTEGRATION_CUTOVER/wp_120_production_cutover.md)
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
| `Cutover execution log` | `WP-120` | `python3 scripts/progress.py show WP-120` |
| `Go-Live DecisionRecord` | `WP-120` | `python3 scripts/progress.py show WP-120` |
| `Production release manifest` | `WP-120` | `python3 scripts/progress.py show WP-120` |
| `Smoke/integrity results` | `WP-120` | `python3 scripts/progress.py show WP-120` |
| `Audit snapshot` | `WP-120` | `python3 scripts/progress.py show WP-120` |

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
- **SRE Lead / Program Lead** carries the acceptance decision; **Executive Sponsor / Assurance** must verify independently of whoever implements.
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
| WP-121-T01 | Establish the hypercare command centre, rota and decision cadence | Implementation owner | Commit / configuration / record reference |
| WP-121-T02 | Monitor the critical journeys, synthetic tests, queues, cost, security and evidence dashboards | Implementation owner | Commit / configuration / record reference |
| WP-121-T03 | Operate incident, finding, change-freeze and rollback authority | Implementation owner | Commit / configuration / record reference |
| WP-121-T04 | Run user support, feedback and knowledge capture | Implementation owner | Commit / configuration / record reference |
| WP-121-T05 | Verify the SLO, error budget and quality KPI baseline | Implementation owner | Commit / configuration / record reference |
| WP-121-T06 | Sign the exit review and the Day-2 owner handoff | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Hypercare log`
- `Incident/finding summary`
- `Production KPI baseline`
- `Day-2 handoff`
- `Program closure report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-121_hypercare_stabilization.tests.md`](wp_121_hypercare_stabilization.tests.md).

- A synthetic G0 → decision journey
- Zotero sync, impact and queue health
- A budget and invoice sample
- An audit export sample
- On-call response
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-121_hypercare_stabilization.acceptance.md`](wp_121_hypercare_stabilization.acceptance.md), together with what this package still cannot establish.

- [ ] Open critical incidents at hypercare exit = 0.
- [ ] The SLO and evidence integrity targets are met.
- [ ] Day-2 owners, runbooks and operating rhythms are active.
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

On critical instability the cutover rollback authority is used; operation does not continue by bypassing part of the feature set.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
