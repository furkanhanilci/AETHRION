# WP-126 — Reviewer, Judge and Reproducer Calibration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-126` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Eval Office / Independent Human Reviewer |
| Hard dependencies | WP-007, WP-043, WP-085, WP-086, WP-087, WP-088, WP-089, WP-113, WP-121 |
| Related gates | G6,G7,Day-2 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-07, ACC-08, ACC-38 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Reviewer precision, disagreement, order/identity/verbosity bias, false positives, escaped defects and reproducer consistency are measured on a schedule against golden and counter-tests.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-113 — Evidence, Reproduction and Publication Acceptance Package](../10_INTEGRATION_CUTOVER/WP-113_evidence_repro_acceptance.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-126-T01 | Run the calibration set and hidden counter-tests periodically | Implementation owner | Commit / configuration / record reference |
| WP-126-T02 | Audit order swaps and blind/unblind leakage | Implementation owner | Commit / configuration / record reference |
| WP-126-T03 | Compute validated precision and recall, disagreement rates and triage time | Implementation owner | Commit / configuration / record reference |
| WP-126-T04 | Establish reviewer and reproducer profile expiry and suspension | Implementation owner | Commit / configuration / record reference |
| WP-126-T05 | Correct rubrics, training and bundles, then requalify | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Calibration reports`
- `Reviewer capability decisions`
- `Bias/quality dashboard`
- `Improvement actions`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Order bias
- Identity leakage
- A strong counter-test
- A false-positive reproducer
- A correlated miss across model families
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] More reviewers is never assumed to mean higher quality.
- [ ] A calibration failure suspends eligibility for the critical role.
- [ ] Human and model reviewers are measured against the same evidence rubric.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

A failed reviewer profile is suspended; open reviews receive an impact assessment and reassignment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
