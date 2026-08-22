# WP-026 — Content-Addressed Object Store and WORM

## Package card

| Field | Value |
|---|---|
| Work package | `WP-026` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Archivist / Security |
| Hard dependencies | WP-021, WP-014 |
| Related gates | G3–G10 |
| Related controls | CTL-DAT-03, CTL-SUP-01 |
| Related acceptance scenarios | ACC-23, ACC-27 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Object-lock / WORM backend** — integrate and verify, do not build

The requirement is compliance-mode retention that no account, including root, can delete. AETHRION owns the `ImmutableObjectStore` contract and the verification that the backend actually refuses deletion; it does not own the storage engine. `lakeFS`-style versioning covers *working* data, which is a different problem.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Purpose and expected outcome

PDF, dataset, artifact, evidence and publication bytes are stored immutably under a content hash, with object lock, encryption, retention and legal-hold.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-026-T01 | Establish the bucket/namespace layout and the data-class separation | Implementation owner | Commit / configuration / record reference |
| WP-026-T02 | Apply content-addressed keys and multipart hash verification | Implementation owner | Commit / configuration / record reference |
| WP-026-T03 | Enable object lock/WORM and the retention policy | Implementation owner | Commit / configuration / record reference |
| WP-026-T04 | Bind the encryption keys and access logging | Implementation owner | Commit / configuration / record reference |
| WP-026-T05 | Separate the quarantine, canonical and publication areas | Implementation owner | Commit / configuration / record reference |
| WP-026-T06 | Set up replication, restore and a bit-rot scan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Object storage IaC`
- `Object address service`
- `Retention matrix`
- `Integrity scan job`
- `Restore procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A denial test for overwriting the same key
- Hash detection of a corrupted byte range
- A cross-region restore and legal-hold test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A canonical object cannot be overwritten.
- [ ] Every object is bound to an `ArtifactRecord` and its hash.
- [ ] A retention deletion policy does not execute without an owner approval.
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

A corrupt replica is repaired from a good hash; the restore produces a new physical object and the canonical reference is re-verified.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
