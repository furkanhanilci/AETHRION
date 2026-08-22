# WP-028 — NATS JetStream and Transactional Outbox Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-028` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Event Platform Lead |
| Independent verifier | SRE / Data Platform Lead |
| Hard dependencies | WP-015, WP-021, WP-025 |
| Related gates | Platform |
| Related controls | CTL-OPS-01, CTL-OBS-01 |
| Related acceptance scenarios | ACC-12, ACC-34 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The at-least-once event backbone is established with an outbox that places the publish intent in the same transaction as the canonical database commit, plus an idempotent relay.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-028-T01 | Set up the JetStream cluster, streams and retention | Implementation owner | Commit / configuration / record reference |
| WP-028-T02 | Bind subject ACLs and workload identity | Implementation owner | Commit / configuration / record reference |
| WP-028-T03 | Write the PostgreSQL outbox schema and the relay | Implementation owner | Commit / configuration / record reference |
| WP-028-T04 | Apply the durable-consumer, ACK and DLQ standard | Implementation owner | Commit / configuration / record reference |
| WP-028-T05 | Establish replay and read-model rebuild modes | Implementation owner | Commit / configuration / record reference |
| WP-028-T06 | Add schema-registry validation and telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `NATS cluster`
- `Outbox relay`
- `Consumer SDK`
- `DLQ/replay runbook`
- `Event dashboards`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Duplicate delivery producing exactly one business effect
- Relay crash recovery after the commit
- Poison-event routing to DLQ and a corrected replay
- Canonical state preserved through a total NATS loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An ACK is issued only after the business commit.
- [ ] Gate state is never changed directly by a NATS consumer.
- [ ] Outbox lag has an SLO and an alert.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

A relay or consumer rollback preserves offsets and the outbox; no side effect is enabled until a replay dry-run has verified the behaviour.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
