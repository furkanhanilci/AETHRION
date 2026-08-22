# WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room

## Package card

| Field | Value |
|---|---|
| Work package | `WP-105` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Independent Reproducibility Lead / Decision Owner |
| Hard dependencies | WP-084, WP-085, WP-086, WP-087, WP-088, WP-089, WP-093, WP-095, WP-104 |
| Related gates | G6,G7 |
| Related controls | CTL-GOV-02, CTL-EPI-03, CTL-EPI-04 |
| Related acceptance scenarios | ACC-06, ACC-07, ACC-08, ACC-19, ACC-20, ACC-38 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A frozen claim/run package passes independent, blind and where required cross-family review, then arbitration and clean-room reproduction, and either clears G6/G7 or returns under control.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.md), [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_vertical_slice_run_claim.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-105-T01 | Assign independence-eligible reviewers and reproducers | Implementation owner | Commit / configuration / record reference |
| WP-105-T02 | Build and dispatch the frozen blind package | Implementation owner | Commit / configuration / record reference |
| WP-105-T03 | Run the mechanical, method and adversarial/cross-family reviews | Implementation owner | Commit / configuration / record reference |
| WP-105-T04 | Arbitrate a conflicting verdict and a strong counter-test | Implementation owner | Commit / configuration / record reference |
| WP-105-T05 | Run clean-room repeatability, reproducibility and robustness | Implementation owner | Commit / configuration / record reference |
| WP-105-T06 | Verify pass/fail root cause and the G4/G5 reopen behaviour | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Review/repro vertical dossier`
- `ReviewRecords/DisagreementCase`
- `ReproductionReport`
- `Gate histories`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of a self-review
- Order bias detection
- A strong deterministic counter-test
- Clean-room pass and fail
- `BLOCKED` when no reviewer is available
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] R3 achieves the required independence on every dimension.
- [ ] A majority vote cannot override failing evidence.
- [ ] A G7 failure moves the claim to `CHALLENGED` without erasing history.
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

A contaminated review or reproduction is invalidated and repeated with a new assignment and a fresh environment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
