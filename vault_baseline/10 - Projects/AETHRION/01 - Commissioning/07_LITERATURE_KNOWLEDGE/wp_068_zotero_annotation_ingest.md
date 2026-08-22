# WP-068 — Zotero Annotation → EvidenceCandidate Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-068` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Intake Lead |
| Independent verifier | Citation Auditor / Knowledge Curator |
| Hard dependencies | WP-017, WP-058, WP-061, WP-063, WP-065, WP-067 |
| Related gates | G3,G5 |
| Related controls | CTL-EPI-01, CTL-LIT-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Zotero highlights and comments become `AnnotationObservation` and `EvidenceCandidate` records carrying the parent attachment, representation hash, locator and actor — never evidence on their own.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/wp_058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/wp_067_zotero_sync_reconciliation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-068-T01 | Write the incremental reader for annotation items | Implementation owner | Commit / configuration / record reference |
| WP-068-T02 | Map the parent attachment to its `SourceRepresentation` | Implementation owner | Commit / configuration / record reference |
| WP-068-T03 | Normalise the text, comment, colour, page, position, author and version fields | Implementation owner | Commit / configuration / record reference |
| WP-068-T04 | Apply attachment hash and locator resolution, including the mismatch state | Implementation owner | Commit / configuration / record reference |
| WP-068-T05 | Add the `EvidenceCandidate` promotion queue and duplicate logic | Implementation owner | Commit / configuration / record reference |
| WP-068-T06 | Establish the impact behaviour for deleted and edited annotations | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Annotation ingest service`
- `AnnotationObservation records`
- `EvidenceCandidate queue`
- `Promotion/disposition UI contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Promotion of a highlight on the correct attachment
- `NEEDS_REANCHOR` on a mismatched PDF
- Versioning of an edited or deleted annotation
- Duplicate note and annotation handling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An annotation never becomes an `EvidenceSpan` or a `VERIFIED` claim automatically.
- [ ] No promotion occurs without an attachment representation hash.
- [ ] Human commentary is kept in a separate field with its own provenance.
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

- Identity errors in sources propagate into every claim that cites them.
- A write into a shared library without a version precondition can silently destroy a human edit.
- A literature set that is not frozen cannot support a reproducible claim.

## Rollback / compensation

A wrong mapping marks the candidate `INVALIDATED`; nothing is ever written back onto the canonical Zotero annotation.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
