# WP-032 — ProjectLifecycle Workflow Skeleton

## Package card

| Field | Value |
|---|---|
| Work package | `WP-032` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Workflow Engineering Lead |
| Independent verifier | Control Plane Architect / Assurance |
| Hard dependencies | WP-008, WP-013, WP-015, WP-020, WP-031 |
| Related gates | G0–G10 |
| Related controls | CTL-OPS-02 |
| Related acceptance scenarios | ACC-13, ACC-14 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The project lifecycle, gate states, pause/resume, versioned transitions and child/task invocations become a deterministic Temporal workflow skeleton.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-032-T01 | Write the `ProjectWorkflow` state machine | Implementation owner | Commit / configuration / record reference |
| WP-032-T02 | Bind the G0–G10 `GateRecord` references | Implementation owner | Commit / configuration / record reference |
| WP-032-T03 | Establish the workflow input/version and Continue-as-New strategy | Implementation owner | Commit / configuration / record reference |
| WP-032-T04 | Separate external I/O behind activity boundaries | Implementation owner | Commit / configuration / record reference |
| WP-032-T05 | Define the pause/resume/cancel query and update APIs | Implementation owner | Commit / configuration / record reference |
| WP-032-T06 | Bind state projection events to the outbox | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ProjectWorkflow implementation`
- `State transition table`
- `Workflow API`
- `Replay fixtures`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A G0 → G10 dry run
- An invalid-transition negative test
- Continue-as-New history continuity
- Worker crash and replay
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Temporal is the single authority over the lifecycle.
- [ ] Workflow code contains no network, clock or random side effect.
- [ ] Every transition carries an input snapshot and a policy reference.
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

New workflow code is deployed behind a patch or version marker; if replay fails the deployment stops and the previous worker build continues serving.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
