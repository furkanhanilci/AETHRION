# WP-039 — Event Consumer, DLQ and Safe Replay Framework

## Package card

| Field | Value |
|---|---|
| Work package | `WP-039` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Event Platform Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-015, WP-020, WP-028, WP-032 |
| Related gates | Platform,G10 |
| Related controls | CTL-OPS-01 |
| Related acceptance scenarios | ACC-12, ACC-34 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Every consumer implements idempotency, canonical-commit-before-ACK, poison-event DLQ handling, replay modes and the projection rebuild contract through one shared SDK.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-039-T01 | Write the consumer middleware and unique-key standard | Implementation owner | Commit / configuration / record reference |
| WP-039-T02 | Apply the ACK transaction boundary | Implementation owner | Commit / configuration / record reference |
| WP-039-T03 | Establish DLQ metadata, retry/backoff and the repair workflow | Implementation owner | Commit / configuration / record reference |
| WP-039-T04 | Define `replay_mode` = dry-run and read-model-rebuild behaviour | Implementation owner | Commit / configuration / record reference |
| WP-039-T05 | Add offset, lag and poison-event telemetry | Implementation owner | Commit / configuration / record reference |
| WP-039-T06 | Publish a reference consumer conformance suite | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Consumer SDK`
- `DLQ service/runbook`
- `Replay controller`
- `Conformance tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A duplicate-delivery test
- A crash before the side-effect commit
- Prevention of an infinite poison-event loop
- Denial of external mutation during a replay
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Exactly-once business effect is achieved through idempotency, not through delivery guarantees.
- [ ] Every DLQ record carries an owner and a correction path.
- [ ] A replay never automatically repeats a production mutation.
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

A consumer rollback does not lose its offset; a new version is verified as a shadow consumer before cutover.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
