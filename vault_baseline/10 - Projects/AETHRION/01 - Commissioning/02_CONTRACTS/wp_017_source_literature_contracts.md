# WP-017 — Source Registry and Literature Contract Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-017` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Citation Auditor / Data Architect |
| Hard dependencies | WP-011, WP-012, WP-014 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-LIT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Source identity, representation, trust, search, screening, set manifest, Zotero binding and status-event schemas are defined canonically, so that a citation means the same thing everywhere in the system.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-017-T01 | Write the `SourceRecord` identifier and merge-lineage fields | Implementation owner | Commit / configuration / record reference |
| WP-017-T02 | Add the `SourceRepresentation` hash, format, licence and locator fields | Implementation owner | Commit / configuration / record reference |
| WP-017-T03 | Define `SourceTrustCard` and `RetractionStatus` | Implementation owner | Commit / configuration / record reference |
| WP-017-T04 | Write the `SearchProtocol`, `ScreeningDecision` and `LiteratureSetManifest` schemas | Implementation owner | Commit / configuration / record reference |
| WP-017-T05 | Add the `ZoteroBinding`, `SyncReceipt` and `AnnotationObservation` schemas | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Literature schema bundle`
- `Status lifecycle`
- `Sample manifests`
- `Zotero binding contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- DOI and title-collision fixtures
- A manifest-immutability test
- A test requiring an attachment hash on every annotation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A Zotero item key is never treated as the canonical source ID.
- [ ] A manifest is a frozen snapshot of the Source Registry.
- [ ] New status or representation versions do not alter a previously frozen set.
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

A wrong merge is corrected through a split event; older set manifests and bindings are preserved unchanged.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
