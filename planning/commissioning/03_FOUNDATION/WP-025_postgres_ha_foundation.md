# WP-025 — PostgreSQL HA and Registry Data Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-025` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Database Platform Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-021, WP-020 |
| Related gates | Platform |
| Related controls | CTL-OPS-03, CTL-SEC-03 |
| Related acceptance scenarios | ACC-27 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

An encrypted, replicated, point-in-time-restorable PostgreSQL foundation is established for the project, source, claim, policy, cost and ledger services.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-025-T01 | Choose the HA topology and the failure domains | Implementation owner | Commit / configuration / record reference |
| WP-025-T02 | Bind encryption, TLS, RBAC and workload identity | Implementation owner | Commit / configuration / record reference |
| WP-025-T03 | Establish the migration framework and schema ownership | Implementation owner | Commit / configuration / record reference |
| WP-025-T04 | Prepare PITR backups, retention and a restore environment | Implementation owner | Commit / configuration / record reference |
| WP-025-T05 | Add connection pooling, quotas and slow-query telemetry | Implementation owner | Commit / configuration / record reference |
| WP-025-T06 | Define the RPO/RTO targets and the integrity queries | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `PostgreSQL clusters`
- `DB role matrix`
- `Migration pipeline`
- `Backup/restore configuration`
- `DB SLO dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A primary failover test
- A PITR restore followed by integrity queries
- A cross-service role-permission negative test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Failover preserves data consistency.
- [ ] A restore meets the target RPO and RTO.
- [ ] No service uses a shared superuser.
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

On a migration failure, apply a forward fix or a verified down migration; irreversible operations are performed through dual-write / expand-contract in two stages.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
