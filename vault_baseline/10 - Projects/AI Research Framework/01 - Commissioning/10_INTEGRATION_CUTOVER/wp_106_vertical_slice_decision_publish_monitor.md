# WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor

## Package card

| Field | Value |
|---|---|
| Work package | `WP-106` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Project Decision Owner |
| Independent verifier | Citation Auditor / Safety / Archivist |
| Hard dependencies | WP-037, WP-074, WP-077, WP-080, WP-085, WP-089, WP-090, WP-093, WP-095, WP-099, WP-105 |
| Related gates | G8,G9,G10 |
| Related controls | CTL-GOV-01, CTL-EPI-01, CTL-LIT-02 |
| Related acceptance scenarios | ACC-04, ACC-25, ACC-30, ACC-31, ACC-36, ACC-40 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A human G8 decision is taken with residual risk and dissent visible, a signed G9 package is published, and the G10 retraction/supersession impact flow runs.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/wp_074_obsidian_projection_sync.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/wp_105_vertical_slice_review_repro.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-106-T01 | Run the evidence-delta, decision rationale and MFA update | Implementation owner | Commit / configuration / record reference |
| WP-106-T02 | Perform the publication completeness, licence and privacy checks | Implementation owner | Commit / configuration / record reference |
| WP-106-T03 | Produce the RO-Crate, signature, archive and release event | Implementation owner | Commit / configuration / record reference |
| WP-106-T04 | Trigger a retraction, a correction and a model drift signal | Implementation owner | Commit / configuration / record reference |
| WP-106-T05 | Create the `ImpactCase`, claim challenge, owner queue item and superseding package | Implementation owner | Commit / configuration / record reference |
| WP-106-T06 | Verify the full chain in the audit export | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Decision/publish/monitor dossier`
- `DecisionRecord`
- `PublicationPackage`
- `ImpactCase/Supersession`
- `Audit export`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- G9 failing on a missing locator
- Denial of a forged decision
- Retraction impact propagation
- An old link surviving a superseded publication
- Full-chain audit verification
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A release happens only through a named human decision.
- [ ] An older publication stays reachable and is visibly superseded.
- [ ] G10 never silently mutates a claim.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

A pre-release rollback invalidates the draft; after release, only a superseding publication and an impact workflow are permitted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
