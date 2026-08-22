# WP-095 — Claim/Evidence Explorer and Provenance Graph

## Package card

| Field | Value |
|---|---|
| Work package | `WP-095` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Product Lead |
| Independent verifier | Citation Auditor / Accessibility Reviewer |
| Hard dependencies | WP-030, WP-075, WP-076, WP-077, WP-078, WP-079, WP-080, WP-082, WP-085, WP-087, WP-088, WP-089, WP-090, WP-091 |
| Related gates | G5–G10 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-04, ACC-08, ACC-21, ACC-30, ACC-31 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A user can inspect a claim's version, certainty and conditions, evidence spans, contradictions, source trust, runs, reviews, reproductions, decisions and supersession chain.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/wp_078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/wp_079_source_trust_cards.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-095-T01 | Write the claim list, detail, version and diff views | Implementation owner | Commit / configuration / record reference |
| WP-095-T02 | Add the evidence-span source preview and locator state | Implementation owner | Commit / configuration / record reference |
| WP-095-T03 | Visualise the dependency, support and contradiction graph | Implementation owner | Commit / configuration / record reference |
| WP-095-T04 | Display the assessment vector and the blocker explanation | Implementation owner | Commit / configuration / record reference |
| WP-095-T05 | Bind the run, review, reproduction and decision timeline | Implementation owner | Commit / configuration / record reference |
| WP-095-T06 | Add the impact/supersession and citation audit views | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Claim Explorer`
- `Evidence preview`
- `Provenance graph`
- `Assessment/blocker panels`
- `Audit drill-down`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A broken locator remaining visible
- Contradictory evidence not hidden
- A fallback query when the derived graph is corrupted
- Full lineage traversal for a critical claim
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No single confidence percentage is presented.
- [ ] The graph is labelled as derived and carries canonical links.
- [ ] The full chain for a material claim is reachable in a single query.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A rollback of the graph UI or the derived projection does not affect the canonical ledger; the direct ledger fallback view is preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
