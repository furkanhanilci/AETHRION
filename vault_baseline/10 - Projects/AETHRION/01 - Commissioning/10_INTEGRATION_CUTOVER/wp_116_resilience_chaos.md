---
title: "WP-116 — Resilience, Chaos and Failure-Injection Commissioning"
aliases:
  - "WP-116"
  - "WP-116 — Resilience, Chaos and Failure-Injection Commissioning"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Fail-closed behaviour, recovery, alerting and data integrity are verified under worker, provider, database, NATS, node, object store, policy, identity and network failures."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md"
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

# WP-116 — Resilience, Chaos and Failure-Injection Commissioning

## Package card

| Field | Value |
|---|---|
| Work package | `WP-116` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Platform Assurance / Service Owners |
| Hard dependencies | WP-040, WP-060, WP-101, WP-111, WP-114, WP-115 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-01, CTL-OPS-02, CTL-OPS-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_116_resilience_chaos.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_116_resilience_chaos.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Fail-closed behaviour, recovery, alerting and data integrity are verified under worker, provider, database, NATS, node, object store, policy, identity and network failures.


## Analysis
### What this package actually decides

What happens under failures nobody scripted. WP-111 injects the faults the risk
register anticipated; this package's value is in the combinations and in the
**blast-radius guard** that makes running them survivable.

### The failure model comes first, and the guard comes with it (T01)

Chaos without a blast-radius guard is an outage you caused. The guard names what
the experiment may touch, what it must not, and the abort condition — and it is the
reason this can run against something production-equivalent.

### Fail-closed is the property, not recovery time (purpose sentence)

A system that recovers quickly from a failure it handled unsafely has failed. The
observation order is: did it **fail closed**, then did it recover, then did it
alert, then is the data intact.

### Queue drain after recovery is the check that catches silent loss (T05)

Services come back, dashboards go green, and the DLQ still holds forty events
nobody will process. Verifying the drain — and the canonical integrity afterwards —
is what distinguishes recovery from apparent recovery.

### Credential and identity faults are the underused half (T02)

Most chaos suites kill processes. Revoking a credential mid-operation, expiring an
SVID during a workflow, or failing the policy engine tests the paths where
`fail-closed` is a real decision rather than a retry.

### The steady-state scorecard defines what "recovered" means (T06)

Without a declared steady state, recovery is judged by whether things look normal.
The scorecard names the observables and their thresholds **before** the experiment.

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
| [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md) | `Replay test suite` · `Golden histories` · `Fault-injection harness` · `Workflow compatibility report` |
| [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md) | `Agentic attack suite` · `Malicious fixture corpus` · `Red-team report template` · `Security regression schedule` |
| [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md) | `Service Catalog` · `SLO catalog` · `Error-budget policy` · `Alert-runbook link checker` |
| [WP-111 — Reliability, Event and FinOps Acceptance Package](../10_INTEGRATION_CUTOVER/wp_111_reliability_finops_acceptance.md) | `Reliability/FinOps scenario results` · `Fault injection report` · `SLO/cost evidence` · `Owner sign-off` |
| [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md) | `Two DR drill reports` · `Restore manifests` · `Integrity query results` · `RPO/RTO scorecard` |
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |

### Full prerequisite closure

**115 of 160 packages (72%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-118` · `WP-119` · `WP-120` · `WP-128`
- **Transitively reachable:** **15 of 160 packages (9%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W7 — Commissioning |
| Dependency depth | level **49** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | SRE Lead |
| Independent verifier | Platform Assurance / Service Owners |
| Gates touched | `Commissioning` |
| Controls | `CTL-OPS-01` · `CTL-OPS-02` · `CTL-OPS-03` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md), [WP-111 — Reliability, Event and FinOps Acceptance Package](../10_INTEGRATION_CUTOVER/wp_111_reliability_finops_acceptance.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md)
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
| `Replay test suite` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Golden histories` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Fault-injection harness` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Workflow compatibility report` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Split-brain injection suite` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Agentic attack suite` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Malicious fixture corpus` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Red-team report template` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security regression schedule` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `ASB and WASP external regression` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Memory poisoning and evaluator exfiltration fixtures` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Service Catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `SLO catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Error-budget policy` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Alert-runbook link checker` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Ownership dashboard` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Coordination overhead and Pareto SLOs` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Reliability/FinOps scenario results` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `Fault injection report` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `SLO/cost evidence` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `Owner sign-off` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `Two DR drill reports` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Restore manifests` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Integrity query results` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `RPO/RTO scorecard` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `DR sign-off` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Commissioning Dossier` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `RC evidence manifest` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Finding/risk register snapshot` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Readiness scorecard` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Board verdict` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Faulty-agent, split-brain and contamination regression` | `WP-115` | `python3 scripts/progress.py show WP-115` |

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
- **SRE Lead** carries the acceptance decision; **Platform Assurance / Service Owners** must verify independently of whoever implements.
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
| WP-116-T01 | Write the failure model and the blast-radius guard | Implementation owner | Commit / configuration / record reference |
| WP-116-T02 | Inject service, node, provider, network and credential faults | Implementation owner | Commit / configuration / record reference |
| WP-116-T03 | Observe retry, circuit breaker, idempotency and compensation behaviour | Implementation owner | Commit / configuration / record reference |
| WP-116-T04 | Measure the SLO alert, on-call and runbook response | Implementation owner | Commit / configuration / record reference |
| WP-116-T05 | Verify canonical integrity and queue drain after recovery | Implementation owner | Commit / configuration / record reference |
| WP-116-T06 | Produce the chaos findings and the steady-state scorecard | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Chaos test suite/results`
- `Steady-state hypotheses`
- `Recovery/integrity report`
- `Resilience sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-116_resilience_chaos.tests.md`](wp_116_resilience_chaos.tests.md).

- Worker, provider, database, NATS, node, network, Vault and policy faults
- Cascading retry and cost control
- Recovery without a duplicated effect
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-116_resilience_chaos.acceptance.md`](wp_116_resilience_chaos.acceptance.md), together with what this package still cannot establish.

- [ ] Every critical steady-state invariant holds.
- [ ] Fault blast radius stays within its declared bound.
- [ ] The alert, runbook and owner SLA chain actually works.
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

On an unexpected blast radius the experiment kill switch fires; work does not continue without an environment restore and an incident review.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
