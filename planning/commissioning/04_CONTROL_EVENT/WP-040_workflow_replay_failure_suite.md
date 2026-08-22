# WP-040 — Workflow Replay, Versioning and Failure Test Suite

## Package card

| Field | Value |
|---|---|
| Work package | `WP-040` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Independent SRE / Control Plane Reviewer |
| Hard dependencies | WP-024, WP-031, WP-032, WP-033, WP-034, WP-035, WP-036, WP-037, WP-038, WP-039 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-OPS-01, CTL-OPS-02 |
| Related acceptance scenarios | ACC-10, ACC-11, ACC-13, ACC-14, ACC-35 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Open workflow histories continue without state loss across code deployments, worker/provider/database loss, retries, timeouts and compensation.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-036 — G5 Execute through G9 Publish Workflows](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md), [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/WP-038_human_updates_compensation.md), [WP-039 — Event Consumer, DLQ and Safe Replay Framework](../04_CONTROL_EVENT/WP-039_event_consumer_dlq_replay.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-040-T01 | Create the golden event histories | Implementation owner | Commit / configuration / record reference |
| WP-040-T02 | Add deterministic replay CI to every workflow build | Implementation owner | Commit / configuration / record reference |
| WP-040-T03 | Write worker-kill and activity-timeout fault injection | Implementation owner | Commit / configuration / record reference |
| WP-040-T04 | Build the database, NATS and provider outage scenarios | Implementation owner | Commit / configuration / record reference |
| WP-040-T05 | Add patch/version-marker and Continue-as-New tests | Implementation owner | Commit / configuration / record reference |
| WP-040-T06 | Produce the state, artifact and integrity comparison report | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Replay test suite`
- `Golden histories`
- `Fault-injection harness`
- `Workflow compatibility report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Replaying an open history against new code
- A worker crash mid-activity
- `BLOCKED` when a provider times out and no fallback exists
- Recovery from a NATS or database outage
- A partial compensation failure
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] 100% of the critical replay tests pass.
- [ ] Workflow state is preserved at RPO = 0.
- [ ] No failure path produces an unsafe route or a duplicated effect.
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

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A worker build that fails replay is not promoted; the previous compatible worker version keeps processing open workflows.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
