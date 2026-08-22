# WP-088 — Blind, Cross-Family and Adversarial Review

## Package card

| Field | Value |
|---|---|
| Work package | `WP-088` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Independent Human Reviewer / Eval Office |
| Hard dependencies | WP-007, WP-018, WP-042, WP-043, WP-044, WP-045, WP-047, WP-077, WP-086, WP-087 |
| Related gates | G6 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-06, ACC-07, ACC-08, ACC-38 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Independent method, claim, code, security and adversarial reviewers examine the frozen package according to risk and rubric; verdicts arrive with findings and claim references.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-088-T01 | Establish the review role, rubric and assignment service | Implementation owner | Commit / configuration / record reference |
| WP-088-T02 | Bind the `IndependenceProfile` eligibility check | Implementation owner | Commit / configuration / record reference |
| WP-088-T03 | Apply blind package dispatch and sealed responses | Implementation owner | Commit / configuration / record reference |
| WP-088-T04 | Write cross-family, order-randomised parallel review | Implementation owner | Commit / configuration / record reference |
| WP-088-T05 | Bind the adversarial counterexample and falsification task | Implementation owner | Commit / configuration / record reference |
| WP-088-T06 | Add verdict/finding aggregation and calibration telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Review service`
- `Assignment/eligibility engine`
- `Review rubrics`
- `ReviewRecord storage`
- `Calibration dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of a self-review assignment
- R3 cross-family and human separation
- Order-swap bias detection
- A critical counter-test overriding a `PASS` majority
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A majority vote is not acceptance.
- [ ] Every finding carries a target locator and a severity.
- [ ] If independence cannot be achieved the review is `BLOCKED`.
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

A contaminated or biased review is invalidated; a new assignment opens with a corrected frozen package.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
