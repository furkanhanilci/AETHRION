# WP-014 — Artifact, Dataset and Immutable Manifest Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-014` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Hard dependencies | WP-011, WP-012 |
| Related gates | G3–G9 |
| Related controls | CTL-DAT-01, CTL-SUP-01 |
| Related acceptance scenarios | ACC-23 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Code, data, environment, document and publication artifacts are defined as immutable objects carrying a content hash, lineage, retention, licence and validity state.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-014-T01 | Write the `ArtifactRecord` and `ContentAddress` schema | Implementation owner | Commit / configuration / record reference |
| WP-014-T02 | Add the split, lineage and licence fields to `DatasetManifest` | Implementation owner | Commit / configuration / record reference |
| WP-014-T03 | Define the environment, OCI and SBOM references | Implementation owner | Commit / configuration / record reference |
| WP-014-T04 | Write new-version and `INVALIDATED` semantics in place of overwrite | Implementation owner | Commit / configuration / record reference |
| WP-014-T05 | Add object-lock, retention and legal-hold metadata | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ArtifactRecord schema`
- `DatasetManifest schema`
- `Environment reference schema`
- `Immutability lifecycle`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A negative test writing different bytes to the same URI
- Hash verification and lineage traversal tests
- A historical-reference test against an invalidated artifact
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No artifact is accepted without a hash over its bytes.
- [ ] Every mutation produces a new version.
- [ ] If licence or retention metadata is missing, external use is `BLOCKED`.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A corrupted object is restored to a new key and the old record is marked `INVALIDATED`; the hash history is preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
