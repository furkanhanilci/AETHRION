---
title: "WP-119 — Controlled Pilot and Cutover Rehearsal"
aliases:
  - "WP-119"
  - "WP-119 — Controlled Pilot and Cutover Rehearsal"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A low-risk but realistic pilot and a full end-to-end cutover/abort/rollback rehearsal are completed in a production-equivalent, non-production environment using the same procedure as the real event."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-119_pilot_cutover_rehearsal.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w7
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
---

# WP-119 — Controlled Pilot and Cutover Rehearsal

## Package card

| Field | Value |
|---|---|
| Work package | `WP-119` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Program Lead |
| Independent verifier | Commissioning Board / Independent Observer |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118 |
| Related gates | Commissioning |
| Related controls | All controls |
| Related acceptance scenarios | ACC-01..ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_119_pilot_cutover_rehearsal.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_119_pilot_cutover_rehearsal.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A low-risk but realistic pilot and a full end-to-end cutover/abort/rollback rehearsal are completed in a production-equivalent, non-production environment using the same procedure as the real event.


## Analysis
### What this package actually decides

Whether the whole thing works for a real user, once, before it matters. A pilot
project travels G0–G10 on production-equivalent configuration — and the cutover
runbook is rehearsed including **abort and rollback**.

### The abort rehearsal is the half that gets skipped (T04)

Everyone rehearses the cutover. Almost nobody rehearses aborting it halfway, and
that is the procedure that will actually be needed if the real event goes wrong.
`00_PROGRAM/10` requires rollback/abort thresholds and decision owners to be
explicit; this is where they are exercised.

### Human usability is a measured outcome, not an impression (T03)

Operations SLAs, decision SLAs, assurance SLAs — and whether a person could
actually work the cockpit under time pressure. `00_PROGRAM/08` makes human capacity
the binding constraint, so a pilot that is technically clean and operationally
unusable has failed.

### Data minimisation, because a pilot is a real exposure (T01)

A production-equivalent environment with production-equivalent data is a
production-equivalent breach surface. The pilot uses minimised data, and the
selection criteria say so.

### Feedback becomes a correction package, not a backlog (T05)

Pilot findings that go into a list are findings that go nowhere. A correction
package with owners and a re-test is what makes the pilot worth running.

### The recommendation must be able to be *no* (T06)

Same property as WP-115's board verdict. A rehearsal whose only possible output is
*go* has not rehearsed anything.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |
| [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md) | `Chaos test suite/results` · `Steady-state hypotheses` · `Recovery/integrity report` · `Resilience sign-off` |
| [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md) | `Load test suite/results` · `Capacity model` · `Bottleneck/tuning report` · `Cost/headroom forecast` |
| [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/wp_118_operational_readiness.md) | `Operational Readiness Review` · `Runbook execution records` · `On-call simulation` · `Training/ownership sign-offs` |

### Full prerequisite closure

**118 of 141 packages (84%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-120`
- **Transitively reachable:** **11 of 141 packages (8%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W7 — Commissioning |
| Dependency depth | level **51** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Program Lead |
| Independent verifier | Commissioning Board / Independent Observer |
| Gates touched | `Commissioning` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/wp_118_operational_readiness.md)
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
| `Commissioning Dossier` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `RC evidence manifest` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Finding/risk register snapshot` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Readiness scorecard` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Board verdict` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Chaos test suite/results` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Steady-state hypotheses` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Recovery/integrity report` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Resilience sign-off` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Load test suite/results` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity model` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Bottleneck/tuning report` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Cost/headroom forecast` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity sign-off` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Operational Readiness Review` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Runbook execution records` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `On-call simulation` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Training/ownership sign-offs` | `WP-118` | `python3 scripts/progress.py show WP-118` |

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
- **Program Lead** carries the acceptance decision; **Commissioning Board / Independent Observer** must verify independently of whoever implements.
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
| WP-119-T01 | Define the pilot selection criteria and apply data minimisation | Implementation owner | Commit / configuration / record reference |
| WP-119-T02 | Run a G0–G10 pilot on production-equivalent RC, configuration and data volume | Implementation owner | Commit / configuration / record reference |
| WP-119-T03 | Measure the operations, decision and assurance SLAs and human usability | Implementation owner | Commit / configuration / record reference |
| WP-119-T04 | Rehearse the cutover runbook: freeze, migration, smoke, abort and rollback | Implementation owner | Commit / configuration / record reference |
| WP-119-T05 | Convert pilot feedback into a correction package | Implementation owner | Commit / configuration / record reference |
| WP-119-T06 | Produce the final rehearsal report and the go/no-go recommendation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Pilot dossier`
- `Cutover rehearsal log`
- `Usability/ops findings`
- `Rollback proof`
- `Go/no-go recommendation`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-119_pilot_cutover_rehearsal.tests.md`](wp_119_pilot_cutover_rehearsal.tests.md).

- A full G0–G10 pilot
- An abort threshold trigger
- Rollback to the prior baseline
- On-call and human decision timing
- An audit export
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-119_pilot_cutover_rehearsal.acceptance.md`](wp_119_pilot_cutover_rehearsal.acceptance.md), together with what this package still cannot establish.

- [ ] The pilot satisfies every invariant.
- [ ] Rollback is proven by evidence from the rehearsal.
- [ ] No open critical or high pilot finding remains.
- [ ] The real cutover procedure is timeboxed and owned.
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

The pilot produces no production side effects; rehearsal state is closed out through environment teardown and archival.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
