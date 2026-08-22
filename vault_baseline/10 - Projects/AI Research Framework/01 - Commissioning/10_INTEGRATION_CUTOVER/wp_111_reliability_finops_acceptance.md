# WP-111 — Reliability, Event and FinOps Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-111` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | FinOps / Control Plane Reviewer |
| Hard dependencies | WP-040, WP-053, WP-083, WP-100, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-01, CTL-OPS-02, CTL-CST-01, CTL-CST-02 |
| Related acceptance scenarios | ACC-09..14, ACC-29, ACC-33..35 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The budget, provider, event, worker, workflow deployment, preemption, DLQ, partial tool failure and invoice variance scenarios close with state and effect integrity intact.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md), [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/wp_083_experiment_batch.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/wp_109_acceptance_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-111-T01 | Run the ACC-09–14 and ACC-29/33/34/35 fixtures | Implementation owner | Commit / configuration / record reference |
| WP-111-T02 | Inject budget, provider, worker, event and queue faults | Implementation owner | Commit / configuration / record reference |
| WP-111-T03 | Verify the state RPO, duplicate-effect, DLQ and cost ledger assertions | Implementation owner | Commit / configuration / record reference |
| WP-111-T04 | Measure the runbook and alert response | Implementation owner | Commit / configuration / record reference |
| WP-111-T05 | Produce the reliability/FinOps dossier and sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Reliability/FinOps scenario results`
- `Fault injection report`
- `SLO/cost evidence`
- `Owner sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- ACC-09, 10, 11, 12, 13, 14, 29, 33, 34 and 35
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] All critical scenarios PASS.
- [ ] Workflow state holds at RPO = 0.
- [ ] Duplicate external effects = 0.
- [ ] Hard budget enforcement and invoice reconciliation are correct.
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

A failure blocks cutover; workload, provider and consumer configuration return to the previous release and the regression is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
