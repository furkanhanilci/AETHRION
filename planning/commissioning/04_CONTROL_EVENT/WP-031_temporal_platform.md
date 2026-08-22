# WP-031 — Temporal Platform, Namespaces and HA

## Package card

| Field | Value |
|---|---|
| Work package | `WP-031` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Control Plane Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-021, WP-025, WP-026, WP-027, WP-028 |
| Related gates | G0–G10 |
| Related controls | CTL-OPS-02, CTL-SEC-03 |
| Related acceptance scenarios | ACC-13, ACC-14 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Temporal is deployed production-ready as the durable workflow platform, with environment, data class, retention, worker identity and failover boundaries defined.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-031-T01 | Establish the cluster or managed topology and its failure domains | Implementation owner | Commit / configuration / record reference |
| WP-031-T02 | Separate the dev, staging and production namespaces and their retention | Implementation owner | Commit / configuration / record reference |
| WP-031-T03 | Bind mTLS, workload identity and RBAC | Implementation owner | Commit / configuration / record reference |
| WP-031-T04 | Define the worker task-queue and versioning standard | Implementation owner | Commit / configuration / record reference |
| WP-031-T05 | Apply the visibility, archival and large-payload-reference rules | Implementation owner | Commit / configuration / record reference |
| WP-031-T06 | Set up backup, failover and SLO telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Temporal platform`
- `Namespace/queue catalog`
- `Worker identity policy`
- `HA/failover runbook`
- `SLO dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A worker and cluster failover test
- An unauthorised queue-poll negative test
- A large-payload object-reference test
- A visibility and archive restore test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Workflow state survives the loss of any worker.
- [ ] Large byte payloads never enter the event history.
- [ ] Every worker polls only the queues it is permitted to poll.
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

The control-cluster failover runbook is executed; because the workflow history is canonical, workers simply reattach.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
