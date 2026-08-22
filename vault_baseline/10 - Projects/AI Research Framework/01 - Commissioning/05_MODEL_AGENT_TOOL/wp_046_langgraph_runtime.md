# WP-046 — LangGraph Bounded Cognition Runtime

## Package card

| Field | Value |
|---|---|
| Work package | `WP-046` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Agent Platform Lead |
| Independent verifier | Control Plane Architect / Security |
| Hard dependencies | WP-013, WP-020, WP-031, WP-032, WP-041, WP-045 |
| Related gates | G2–G7 |
| Related controls | CTL-OPS-02, CTL-DAT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

LangGraph manages only the node/state, checkpoint, interrupt and `AgentResult` production within the scope of a `TaskContract`. It owns neither lifecycle state nor side effects.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-046-T01 | Build the canonical task graph wrapper and its state schema | Implementation owner | Commit / configuration / record reference |
| WP-046-T02 | Write the Temporal activity and child-task adapter | Implementation owner | Commit / configuration / record reference |
| WP-046-T03 | Bind the checkpoint store with its TTL and data-class policy | Implementation owner | Commit / configuration / record reference |
| WP-046-T04 | Apply node timeout, retry and cancellation semantics | Implementation owner | Commit / configuration / record reference |
| WP-046-T05 | Block every side effect that does not go through the Tool or Execution Broker | Implementation owner | Commit / configuration / record reference |
| WP-046-T06 | Add `AgentResult`/artifact upload and trace correlation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `LangGraph runtime`
- `Temporal adapter`
- `Checkpoint policy`
- `Agent graph SDK`
- `Conformance tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Task cancellation propagation
- Resume from checkpoint
- A direct side-effect negative test
- Rebuild from the `TaskContract` after total runtime loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] LangGraph never mirrors gate or workflow state.
- [ ] Every external effect is a broker call.
- [ ] Checkpoints containing sensitive data obey the retention policy.
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

- A model alias is not a pinned identity; results obtained under an alias are not reproducible.
- An agent holding a credential defeats the entire broker design.
- Fallback routes are the least tested and most consequential path in this workstream.

## Rollback / compensation

Runtime releases are canaried per task; a failed task is re-dispatched onto the new runtime or resumed from its last checkpoint.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
