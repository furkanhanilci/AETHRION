---
title: "WP-120 — Production Cutover and Go-Live Decision"
aliases:
  - "WP-120"
  - "WP-120 — Production Cutover and Go-Live Decision"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "On the strength of the signed commissioning dossier and the rehearsal, the change freeze, migration and promotion, smoke and integrity tests, traffic enablement and the formal Go-Live DecisionRecord are executed."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-120_production_cutover.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w8
  - aethrion/effort/l
  - aethrion/gate/cutover
  - aethrion/state/not-started
---

# WP-120 — Production Cutover and Go-Live Decision

## Package card

| Field | Value |
|---|---|
| Work package | `WP-120` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Executive Sponsor / Program Lead |
| Independent verifier | Commissioning Board / Internal Audit |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118, WP-119 |
| Related gates | Cutover |
| Related controls | All controls |
| Related acceptance scenarios | every scenario whose `Acceptance phase` is `PRE_GO_LIVE` (ACC-01 – ACC-51 excluding the Day-2 set) |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_120_production_cutover.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_120_production_cutover.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

On the strength of the signed commissioning dossier and the rehearsal, the change freeze, migration and promotion, smoke and integrity tests, traffic enablement and the formal Go-Live `DecisionRecord` are executed.


## Analysis
### What this package actually decides

The single moment the programme has been building toward, and the decision it
encodes is that **production opens once, integrated**.

`planning/commissioning/README.md` §1 states it: the programme is developed
incrementally *but is not opened to production with capabilities missing*. A
staged opening would let a partially commissioned system carry real research, which
is the outcome the whole plan exists to prevent.

### The go/no-go decision is the deliverable (T06)

Everything else here is procedure. The `DecisionRecord` is the artifact, and
`00_PROGRAM/10` fixes its preconditions: zero open critical findings, zero open high
findings or a time-boxed board-accepted residual, two restore rehearsals, and the
whole entry-condition list.

### Abort must remain available until the last moment (T06)

`00_PROGRAM/10` requires rollback/abort thresholds and decision owners to be
explicit, and WP-001 makes abort authority non-delegable and separate from the
sponsor. A cutover that becomes unabortable partway has removed its own safety.

### The restore point comes before anything moves (T02)

Not a backup — a **verified** restore point, with the owner check completed. An
untested restore point at cutover is `PR-13` at the worst possible moment.

### Traffic enablement is sequenced, and the sequence is reversible (T05)

Controlled sequence, each step observed, each step reversible. This is the one place
where "integrated cutover" and "staged enablement" are compatible: the *capabilities*
open together; the *traffic* arrives in a controlled order.

### The post-cutover audit snapshot closes the record (T07)

A hash-chained snapshot immediately after cutover is the baseline every later
integrity check compares against.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |
| [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md) | `Chaos test suite/results` · `Steady-state hypotheses` · `Recovery/integrity report` · `Resilience sign-off` |
| [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md) | `Load test suite/results` · `Capacity model` · `Bottleneck/tuning report` · `Cost/headroom forecast` |
| [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/wp_118_operational_readiness.md) | `Operational Readiness Review` · `Runbook execution records` · `On-call simulation` · `Training/ownership sign-offs` |
| [WP-119 — Controlled Pilot and Cutover Rehearsal](../10_INTEGRATION_CUTOVER/wp_119_pilot_cutover_rehearsal.md) | `Pilot dossier` · `Cutover rehearsal log` · `Usability/ops findings` · `Rollback proof` |

### Full prerequisite closure

**119 of 141 packages (84%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-121`
- **Transitively reachable:** **10 of 141 packages (7%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W8 — Cutover |
| Dependency depth | level **52** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Executive Sponsor / Program Lead |
| Independent verifier | Commissioning Board / Internal Audit |
| Gates touched | `Cutover` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/wp_118_operational_readiness.md), [WP-119 — Controlled Pilot and Cutover Rehearsal](../10_INTEGRATION_CUTOVER/wp_119_pilot_cutover_rehearsal.md)
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
| `Pilot dossier` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Cutover rehearsal log` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Usability/ops findings` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Rollback proof` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Go/no-go recommendation` | `WP-119` | `python3 scripts/progress.py show WP-119` |

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
- **Executive Sponsor / Program Lead** carries the acceptance decision; **Commissioning Board / Internal Audit** must verify independently of whoever implements.
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
| WP-120-T01 | Freeze the final RC, policy, schema, model, tool and infrastructure digests | Implementation owner | Commit / configuration / record reference |
| WP-120-T02 | Take the pre-cutover backup and restore point and run the owner check | Implementation owner | Commit / configuration / record reference |
| WP-120-T03 | Apply the IaC/GitOps deployment and migration steps | Implementation owner | Commit / configuration / record reference |
| WP-120-T04 | Run the service, contract, security and integrity smoke tests | Implementation owner | Commit / configuration / record reference |
| WP-120-T05 | Enable traffic, user access and monitoring in a controlled sequence | Implementation owner | Commit / configuration / record reference |
| WP-120-T06 | Record the go / no-go / abort decision with its evidence | Implementation owner | Commit / configuration / record reference |
| WP-120-T07 | Take the post-cutover audit snapshot | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cutover execution log`
- `Go-Live DecisionRecord`
- `Production release manifest`
- `Smoke/integrity results`
- `Audit snapshot`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-120_production_cutover.tests.md`](wp_120_production_cutover.tests.md).

- The preflight checklist
- Deployment and migration
- Security, identity and route smoke tests
- Workflow, source, claim and artifact integrity
- Abort and rollback readiness
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-120_production_cutover.acceptance.md`](wp_120_production_cutover.acceptance.md), together with what this package still cannot establish.

- [ ] The Commissioning Dossier is READY.
- [ ] Every `PRE_GO_LIVE` scenario PASSes, with open critical findings = 0.
- [ ] Every production digest is signed and pinned.
- [ ] The go-live decision is taken by named executives, SRE and Safety.
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

At the abort threshold traffic is closed and the last verified baseline is restored per the GitOps and database plan; newly written immutable records are never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
