# WP-090 — PublicationPackage, RO-Crate and Provenance Export

## Package card

| Field | Value |
|---|---|
| Work package | `WP-090` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Provenance Curator |
| Independent verifier | Citation Auditor / Safety / Archivist |
| Hard dependencies | WP-014, WP-018, WP-026, WP-072, WP-075, WP-077, WP-080, WP-081, WP-082, WP-085, WP-087, WP-088, WP-089 |
| Related gates | G9,G10 |
| Related controls | CTL-EPI-01, CTL-DAT-03, CTL-SUP-01 |
| Related acceptance scenarios | ACC-30, ACC-31, ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Quarto/Pandoc authoring stack (provisional) · CSL · JATS · MECA · veraPDF**

The publication package is produced by an adopted authoring stack rather than a bespoke renderer: Quarto orchestrates, Pandoc's AST carries transformations, CSL supplies citation styles, JATS and MECA are interchange and submission exports, and veraPDF validates the rendered artifact when PDF/A or PDF/UA is requested. **A renderer exiting zero decides nothing** — publication remains a G9 human decision, and the authoring backend is provisional until the bake-off in `skills/authoring-research-documents/references/authoring-backend-bakeoff.md` is run.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md` §9.1.

## Purpose and expected outcome

Approved claims, limitations, source sets, protocols, runs, code/data/environment, reviews, reproductions and the `DecisionRecord` become a portable, signed and supersedable publication package.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-090-T01 | Write the `PublicationPackage` and RO-Crate profile and manifest | Implementation owner | Commit / configuration / record reference |
| WP-090-T02 | Build the claim narrative → ledger link materialiser | Implementation owner | Commit / configuration / record reference |
| WP-090-T03 | Bind the CSL citation, locator and audit results | Implementation owner | Commit / configuration / record reference |
| WP-090-T04 | Add the code, data, environment, run and reproduction artifact references | Implementation owner | Commit / configuration / record reference |
| WP-090-T05 | Apply the licence, privacy, redaction and release checks | Implementation owner | Commit / configuration / record reference |
| WP-090-T06 | Produce signature, archive, access, supersession and public landing metadata | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Publication builder`
- `RO-Crate profile`
- `Signed publication package`
- `Release checklist`
- `Supersession record`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Failure when a critical claim has no locator
- Redaction of restricted data
- Package hash and signature verification
- An old link remaining accessible after supersession
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The narrative cannot change the certainty or limitations recorded in the ledger.
- [ ] The package carries complete lineage and its `DecisionRecord`.
- [ ] An older package is never deleted; it receives a supersession link.
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

A pre-release fault marks the draft package `INVALIDATED`; a post-publication correction requires a new version, a supersession and an `ImpactCase`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
