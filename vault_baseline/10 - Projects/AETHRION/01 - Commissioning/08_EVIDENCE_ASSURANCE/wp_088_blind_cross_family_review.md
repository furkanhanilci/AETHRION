---
title: "WP-088 — Blind, Cross-Family and Adversarial Review"
aliases:
  - "WP-088"
  - "WP-088 — Blind, Cross-Family and Adversarial Review"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Independent method, claim, code, security and adversarial reviewers examine the frozen package according to risk and rubric; verdicts arrive with findings and claim references."
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g6
  - aethrion/state/not-started
---

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
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_088_blind_cross_family_review.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_088_blind_cross_family_review.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Independent method, claim, code, security and adversarial reviewers examine the frozen package according to risk and rubric; verdicts arrive with findings and claim references.


## Analysis
### What this package actually decides

Who reviews, on what basis, and how their verdicts are kept from contaminating
each other. Five reviewer roles — method, claim, code, security, adversarial — with
independence checked at assignment and again at the gate.

### Cross-family is the structural answer to correlated error (T04)

`PR-16` states the gap: PR-05 addresses paper independence, not correlated errors
between genuinely different models. Two reviewers from the same model family share
training data and share failure modes, and they will agree on exactly the cases
where agreement is least informative.

Requiring different families is a proxy for uncorrelated error. It is a **proxy**,
and the package should say so — the measurement that would settle it is
`measuring-agreement`'s pairwise error correlation, which is WP-126 and the
metascience gap.

### Order randomisation removes an anchoring effect (T04)

Reviewers who see findings in the same order anchor on the first. Randomising the
order is nearly free and removes a systematic bias that no amount of rubric
discipline addresses.

### Sealed responses are what make parallel review parallel (T03)

If reviewer B can see reviewer A's verdict before submitting, there is one review
with an extra step. Sealing until all are in is what preserves the independence the
assignment established.

### The adversarial reviewer has a different job (T05)

Method, claim, code and security reviewers assess. The adversarial reviewer's task
is to **falsify** — to construct the counterexample. `adversarial-reviewing` is the
skill, `ACC-08` is the scenario, and the distinction matters because an assessor
who finds nothing has done their job while a falsifier who finds nothing has only
failed to.

### Calibration telemetry is what makes the reviewer pool improvable (T06)

Verdict distribution per reviewer, agreement rate, and the rate at which a
reviewer's findings survive arbitration. A reviewer who never finds anything and a
reviewer whose findings never survive are two different problems, and both are
invisible without the numbers.

### Baseline v1.3.0 — the assurance layer stops using one word for two things

Three changes, and the first is a vocabulary correction with real consequences.

**"Mechanical verifier" is retired as a broad term.** It becomes V0 deterministic
· V1 computational · V2 qualified semantic · V3 human (`ADR-008`), and the class
is assigned by the verifier service from the procedure that actually ran — never
by the caller. The reason is that the gate rule *a mechanical check cannot be
overridden by a model* is correct for V0 and V1 and absurd at V2, where it says a
model's judgement cannot be overridden by a model.

**Assurance becomes routed** (`ADR-015`): by consequence and uncertainty rather
than uniformly, with a cascade to a stronger independent verifier or to a human,
and with `ABSTAIN` as a valid verdict that escalates. A route cannot be lowered
because the queue is long or the budget is tight.

**Three hard bindings** into the evidence and publication path:

- **Specification conformance** — the frozen method and the running code are
  compared, and an unapproved `SCIENTIFIC_MAJOR` deviation cannot carry a
  confirmatory package forward (`ADR-018`, ACC-104).
- **Model execution fingerprint** — every invocation contributing to a result
  records what actually executed, retry and fallback history included, and a
  hosted black-box model does not yield an `EXACT` reproduction claim
  (ACC-115, ACC-116).
- **Publication compiler** — no prose without a claim, no number without a
  `VerifiedValue`, and a complete evidence chain checked link by link
  (ACC-105, ACC-106).

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md) | `Capability Registry service` · `Profile state machine` · `Eligibility API` · `Expiry/revoke scheduler` |
| [WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md) | `Eval dataset manifests` · `Role eval harness` · `Grader/rubric bundle` · `Contamination controls` |
| [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md) | `Qualification pipeline` · `Admission dossier` · `CapabilityProfile update` · `Regression schedule` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md) | `Review Package Builder` · `Blind/redaction rules` · `Package manifests` · `Leak detection tests` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |

### Full prerequisite closure

**75 of 160 packages (47%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-089` · `WP-090` · `WP-095` · `WP-105` · `WP-113` · `WP-126`
- **Transitively reachable:** **39 of 160 packages (24%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **38** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Assurance Lead |
| Independent verifier | Independent Human Reviewer / Eval Office |
| Gates touched | `G6` |
| Controls | `CTL-GOV-02` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-07 — Reviewer Order Bias](../12_ACCEPTANCE_SCENARIOS/acc_07_reviewer_order_bias.md) | High | A material order effect fails the profile's calibration; the reviewer is not admitted to a critical role, or is suspended from it. |
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-38 — Critical Reviewer Unavailable](../12_ACCEPTANCE_SCENARIOS/acc_38_reviewer_unavailable.md) | High | Neither the producer, a self-review, nor an ineligible fallback is used; the gate is `BLOCKED` and a human scheduling/escalation item and a capacity signal are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Capability Registry service` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Profile state machine` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eligibility API` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Expiry/revoke scheduler` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eval dataset manifests` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Role eval harness` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Grader/rubric bundle` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Contamination controls` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Eval scorecard` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Cross-model × cross-harness compliance matrix` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Qualification pipeline` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Admission dossier` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `CapabilityProfile update` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Regression schedule` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Ejection procedure` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Fingerprint and abstention scope on qualification records` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Review Package Builder` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Blind/redaction rules` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Package manifests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Leak detection tests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `V0-V3 verification routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerifierQualificationRecord` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Positive and negative control suite` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Adaptive assurance routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Abstention verdicts` | `WP-087` | `python3 scripts/progress.py show WP-087` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Assurance Lead** carries the acceptance decision; **Independent Human Reviewer / Eval Office** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

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

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-088_blind_cross_family_review.tests.md`](wp_088_blind_cross_family_review.tests.md).

- Denial of a self-review assignment
- R3 cross-family and human separation
- Order-swap bias detection
- A critical counter-test overriding a `PASS` majority
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-088_blind_cross_family_review.acceptance.md`](wp_088_blind_cross_family_review.acceptance.md), together with what this package still cannot establish.

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
