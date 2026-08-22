# WP-080 — Claim–Citation Entailment, Scope and Locator Audit

## Package card

| Field | Value |
|---|---|
| Work package | `WP-080` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Citation Audit Lead |
| Independent verifier | Independent Methodologist / Human Reviewer |
| Hard dependencies | WP-007, WP-018, WP-072, WP-075, WP-076, WP-077, WP-078, WP-079 |
| Related gates | G6,G9 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-30 |
| Current status | `NOT_STARTED` |

## Adopted component

> **Reference verification is implemented** — Crossref · OpenAlex · arXiv

`scripts/verify_references.py` resolves the registry against three authorities; the measured corroboration rate is recorded in `delivery/measurements/`. What remains in this package is the **entailment** half: does the cited passage support the claim?

Rationale and adoption type: `docs/architecture/AIRL_OS_COMPONENT_REUSE.md`.

## Purpose and expected outcome

For every material sentence, a structured audit verifies whether the linked evidence span actually supports the assertion, whether the scope is appropriate, and whether a contradiction exists.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-080-T01 | Write the claim–evidence relationship rubric | Implementation owner | Commit / configuration / record reference |
| WP-080-T02 | Add mechanical locator integrity and quote/fingerprint checking | Implementation owner | Commit / configuration / record reference |
| WP-080-T03 | Build the entailment, scope, hedging and secondary-citation review graph | Implementation owner | Commit / configuration / record reference |
| WP-080-T04 | Add counter-evidence and citation-laundering checks | Implementation owner | Commit / configuration / record reference |
| WP-080-T05 | Apply risk-based human sampling and full audit | Implementation owner | Commit / configuration / record reference |
| WP-080-T06 | Integrate the `CitationAudit` verdict as a G9 blocker | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Citation audit service`
- `Audit rubric`
- `Mechanical locator checker`
- `Audit report/scorecard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Correct support passing
- A citation that is merely related but not supporting
- An overgeneralised scope failing
- Secondary-citation laundering
- A missing locator failing G9
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The presence of a citation is not evidence of support.
- [ ] Critical claims reach 100% locator and entailment coverage.
- [ ] Every reviewer verdict carries an evidence span and a rationale.
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

A failed audit sends the claim or report to revision; neither the source nor any prior evidence is overwritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
