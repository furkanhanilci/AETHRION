---
title: "WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room"
aliases:
  - "WP-105"
  - "WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A frozen claim/run package passes independent, blind and where required cross-family review, then arbitration and clean-room reproduction, and either clears G6/G7 or returns under control."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g6
  - aethrion/gate/g7
  - aethrion/state/not-started
---

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

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_105_vertical_slice_review_repro.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_105_vertical_slice_review_repro.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A frozen claim/run package passes independent, blind and where required cross-family review, then arbitration and clean-room reproduction, and either clears G6/G7 or returns under control.


## Analysis
### What this package actually decides

Whether independence survives contact with a real review. Every control in
`08_EVIDENCE_ASSURANCE` is exercised here at once: frozen packages, blind dispatch,
cross-family assignment, arbitration, and a clean-room reproduction.

### The R3 case will be `BLOCKED` and that is the result

ADR-001: R3 requires an external verifier; under a solo operator it is **`BLOCKED`,
declared rather than waived**. A slice that produces an R3 pass has either found an
external verifier or has broken the control.

The honest outcome of this slice is therefore *R2 completes under a declared
partial profile, R3 blocks with a declaration* — and reporting that as a
limitation rather than a failure is the point.

### The two reviews that must actually happen (T03)

**Mechanical first.** WP-087's validators run before any reviewer is asked, and a
failing mechanical check cannot be overridden by a model verdict.

**Adversarial separately.** WP-088's adversarial reviewer attempts to falsify
rather than assess. *Failed to falsify* is a different result from *assessed as
sound*, and this slice must produce both distinctly.

### Arbitration is exercised on a real conflict (T04)

Not simulated. Two reviewers reaching different verdicts on the same frozen
package, resolved by an arbiter who records **which evidence prevailed and why** —
and refused if no independent arbiter exists.

### The reproduction must be able to fail (T05, T06)

A clean-room run that succeeds proves the manifest is sufficient. A slice that only
runs the succeeding case has not tested the root-cause machinery, and a failed
reproduction is what marks a claim `CHALLENGED` (invariant 4).

Both paths run here, and the six root-cause categories are exercised.

### The reopen behaviour is the seam (T06)

A failed reproduction reopens G4/G5. Which downstream artifacts invalidate, and
whether the claim's state follows, is where WP-008, WP-077 and WP-085 meet.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

9, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/wp_084_clean_room_environment.md) | `Clean-room platform` · `Reproducer profile` · `Environment resolver` · `Isolation attestation` |
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |
| [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md) | `Review Package Builder` · `Blind/redaction rules` · `Package manifests` · `Leak detection tests` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |
| [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md) | `Review service` · `Assignment/eligibility engine` · `Review rubrics` · `ReviewRecord storage` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |
| [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md) | `Decision Queue UI` · `Evidence-delta component` · `Rationale forms` · `Delegation/escalation views` |
| [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md) | `Claim Explorer` · `Evidence preview` · `Provenance graph` · `Assessment/blocker panels` |
| [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/wp_104_vertical_slice_run_claim.md) | `Run/claim vertical dossier` · `Run manifests/artifacts` · `Claim/Evidence records` · `Cost/trace/audit evidence` |

### Full prerequisite closure

**90 of 141 packages (64%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-100` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` · `WP-085` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` |
| 42 | `WP-104` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-106` · `WP-109` · `WP-110`
- **Transitively reachable:** **24 of 141 packages (17%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **43** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Assurance Lead |
| Independent verifier | Independent Reproducibility Lead / Decision Owner |
| Gates touched | `G6` · `G7` |
| Controls | `CTL-GOV-02` · `CTL-EPI-03` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-07 — Reviewer Order Bias](../12_ACCEPTANCE_SCENARIOS/acc_07_reviewer_order_bias.md) | High | A material order effect fails the profile's calibration; the reviewer is not admitted to a critical role, or is suspended from it. |
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) | Critical | G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened. |
| [ACC-38 — Critical Reviewer Unavailable](../12_ACCEPTANCE_SCENARIOS/acc_38_reviewer_unavailable.md) | High | Neither the producer, a self-review, nor an ineligible fallback is used; the gate is `BLOCKED` and a human scheduling/escalation item and a capacity signal are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/wp_084_clean_room_environment.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/wp_104_vertical_slice_run_claim.md)
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
| `Clean-room platform` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Reproducer profile` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Environment resolver` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Isolation attestation` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Repro runbook` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Review Package Builder` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Blind/redaction rules` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Package manifests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Leak detection tests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Review service` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Assignment/eligibility engine` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Review rubrics` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `ReviewRecord storage` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Calibration dashboard` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Decision Queue UI` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence-delta component` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Rationale forms` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Delegation/escalation views` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Decision audit export` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Claim Explorer` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Evidence preview` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Provenance graph` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Assessment/blocker panels` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Audit drill-down` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Run/claim vertical dossier` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Run manifests/artifacts` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Claim/Evidence records` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Cost/trace/audit evidence` | `WP-104` | `python3 scripts/progress.py show WP-104` |

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
- **Assurance Lead** carries the acceptance decision; **Independent Reproducibility Lead / Decision Owner** must verify independently of whoever implements.
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

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-105_vertical_slice_review_repro.tests.md`](wp_105_vertical_slice_review_repro.tests.md).

- Denial of a self-review
- Order bias detection
- A strong deterministic counter-test
- Clean-room pass and fail
- `BLOCKED` when no reviewer is available
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-105_vertical_slice_review_repro.acceptance.md`](wp_105_vertical_slice_review_repro.acceptance.md), together with what this package still cannot establish.

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
