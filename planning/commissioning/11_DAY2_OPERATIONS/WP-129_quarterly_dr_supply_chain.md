# WP-129 — Quarterly DR, Supply-Chain and Audit Drill

## Package card

| Field | Value |
|---|---|
| Work package | `WP-129` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead / Supply Chain Security |
| Independent verifier | Independent Audit Witness |
| Hard dependencies | WP-027, WP-059, WP-099, WP-114, WP-121 |
| Related gates | Day-2 |
| Related controls | CTL-OPS-02, CTL-OPS-03, CTL-SEC-05 |
| Related acceptance scenarios | ACC-17, ACC-27, ACC-40 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Quarterly restore, workflow replay, signature and revocation, audit export and dependency/patch drills prove that the production baseline remains sustainable over time.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-129-T01 | Select the rotating component or regional restore drill | Implementation owner | Commit / configuration / record reference |
| WP-129-T02 | Test open workflow replay and worker versioning | Implementation owner | Commit / configuration / record reference |
| WP-129-T03 | Exercise image, tool and policy signature and revocation | Implementation owner | Commit / configuration / record reference |
| WP-129-T04 | Run a full project audit export with hash verification | Implementation owner | Commit / configuration / record reference |
| WP-129-T05 | Review patch, CVE, backup, retention and ownership gaps | Implementation owner | Commit / configuration / record reference |
| WP-129-T06 | Close the drill findings and plan the next quarter | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Quarterly drill dossier`
- `Restore/replay evidence`
- `Supply-chain/audit results`
- `Improvement backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Rotating PITR, object, Temporal and NATS restores
- Denial of a revoked artifact
- Audit chain verification
- Owner and runbook execution
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] RPO, RTO and integrity targets are met.
- [ ] An open critical drill finding escalates as a production risk, not merely as a cutover blocker.
- [ ] Every piece of evidence carries an independent witness.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

A drill is stopped on unexpected risk; the production blast-radius guard and the incident process take over.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
