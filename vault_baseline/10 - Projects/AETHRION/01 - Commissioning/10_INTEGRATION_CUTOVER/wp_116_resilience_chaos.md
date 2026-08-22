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

## Purpose and expected outcome

Fail-closed behaviour, recovery, alerting and data integrity are verified under worker, provider, database, NATS, node, object store, policy, identity and network failures.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md), [WP-111 — Reliability, Event and FinOps Acceptance Package](../10_INTEGRATION_CUTOVER/wp_111_reliability_finops_acceptance.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

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

- Worker, provider, database, NATS, node, network, Vault and policy faults
- Cascading retry and cost control
- Recovery without a duplicated effect
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

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
