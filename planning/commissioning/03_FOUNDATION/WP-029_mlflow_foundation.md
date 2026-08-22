# WP-029 — MLflow Experiment and Evaluation Tracking Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-029` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer / Security |
| Hard dependencies | WP-021, WP-025, WP-026 |
| Related gates | G4–G7 |
| Related controls | CTL-DAT-01, CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Experiment, evaluation, metric and artifact references are tracked under data-class-compliant, access-controlled, immutable run identities.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-029-T01 | Deploy the tracking server, backend store and artifact store | Implementation owner | Commit / configuration / record reference |
| WP-029-T02 | Apply project/run RBAC and data-class separation | Implementation owner | Commit / configuration / record reference |
| WP-029-T03 | Add the run tag standard and the correlation identifier | Implementation owner | Commit / configuration / record reference |
| WP-029-T04 | Reference canonical artifacts instead of copying them | Implementation owner | Commit / configuration / record reference |
| WP-029-T05 | Define the metric schema and its lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-029-T06 | Establish backup, restore and an export test | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `MLflow deployment`
- `Run naming/tag policy`
- `Access controls`
- `Tracking SDK wrapper`
- `Restore procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An unauthorised project-read negative test
- A run → artifact/source correlation query
- A backup restore with metric-integrity verification
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] MLflow never owns canonical artifact bytes.
- [ ] Every run is bound to a project, workflow and run identifier.
- [ ] D3/D4 prompt and data telemetry never leaves the policy boundary.
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

Losing the tracking service does not lose the run execution artifacts; queued metadata is ingested idempotently on recovery.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
