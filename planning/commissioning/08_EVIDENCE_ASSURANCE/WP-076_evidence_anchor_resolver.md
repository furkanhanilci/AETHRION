# WP-076 — Evidence Span Anchoring and Re-anchoring

## Package card

| Field | Value |
|---|---|
| Work package | `WP-076` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Engineering Lead |
| Independent verifier | Citation Auditor / Reproducibility Engineer |
| Hard dependencies | WP-014, WP-017, WP-018, WP-026, WP-058, WP-063, WP-068, WP-075 |
| Related gates | G5,G6,G10 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-04, ACC-30 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Evidence is resolved against PDFs, HTML and dataset documentation through a triple anchor — representation content hash, structural position and text fingerprint — and receives an explicit state when the representation changes.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-076-T01 | Write the format-specific locator adapters | Implementation owner | Commit / configuration / record reference |
| WP-076-T02 | Implement the text, table, figure, code and data-cell span model | Implementation owner | Commit / configuration / record reference |
| WP-076-T03 | Establish the fingerprint, fuzzy relocation and confidence rules | Implementation owner | Commit / configuration / record reference |
| WP-076-T04 | Add the RELOCATED / AMBIGUOUS / NEEDS_REANCHOR / ORPHANED state machine | Implementation owner | Commit / configuration / record reference |
| WP-076-T05 | Write the human re-anchor queue and its audit trail | Implementation owner | Commit / configuration / record reference |
| WP-076-T06 | Emit the impact event for affected claims | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Anchor resolver`
- `Format adapters`
- `Re-anchor queue`
- `Anchor regression corpus`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Exact resolution against a stable PDF
- `RELOCATED` on a re-laid-out PDF
- `AMBIGUOUS` on duplicated text
- No `ORPHANED` state while the old representation is available
- `ORPHANED` when the representation is genuinely unavailable
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Anchor confidence alone is never claim support.
- [ ] A state change puts every dependent claim into impact assessment.
- [ ] Older evidence versions remain reachable.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

A wrong relocation is not reverted; it is superseded by a new `AnchorResolution` record and a curator decision.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
