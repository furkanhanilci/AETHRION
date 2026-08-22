---
title: "WP-126 — Reviewer, Judge and Reproducer Calibration — Acceptance Criteria"
aliases:
  - "WP-126 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-126_assurance_calibration.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g6
  - aethrion/gate/g7
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-126 — Reviewer, Judge and Reproducer Calibration — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-126` |
| Work package | [`WP-126` — Reviewer, Judge and Reproducer Calibration](wp_126_assurance_calibration.md) |
| Companion | [test procedures](wp_126_assurance_calibration.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Eval Office / Independent Human Reviewer** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-126` |

<!-- /generated:identity -->

## How to read a criterion

<!-- generated:howto — produced by scripts/make_package_companions.py; do not edit inside this block -->

A criterion belongs here only if it can **fail**. `00_PROGRAM/05` lists what is not evidence, and the first entry is an implementer's free-text declaration of success.

| A criterion states | Not |
|---|---|
| a number, a threshold or a command | "works correctly" |
| the observation that would falsify it | "has been reviewed" |
| the test case that decides it | "all tests pass" |
| what it does **not** establish | silence about its own limits |

Each criterion names the test case in [`WP-126_assurance_calibration.tests.md`](wp_126_assurance_calibration.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The calibration set has known outcomes, is held out and refreshed, and
      **hidden counter-tests measure recall** — precision alone says nothing about
      what was missed.
- [ ] **Validated precision counts findings that survived arbitration and
      reproduction**, not raw finding count. A reviewer whose findings rarely survive
      is **flagged**, and so is one who never finds anything.
- [ ] **All three biases are measured as numbers**: order, identity, and **verbosity**
      — the last being the one most specific to model reviewers and least often
      tested.
- [ ] **The blind leakage audit finds no correlation between verdicts and producer
      identity**, or traces the leak.
- [ ] **Pairwise error correlation is reported as a number for every reviewer pair**,
      and two reviewers correlated above threshold **cannot both satisfy an
      independence requirement**. This is `PR-16` and `00_PROGRAM/10`'s go-live
      condition.
- [ ] A near-zero disagreement rate is **investigated rather than celebrated** —
      reviewers who never disagree are the signature of correlated error.
- [ ] Reproducer agreement is measured with disagreements itemised.
- [ ] **Reviewer profiles expire and require requalification**, a measured
      degradation suspends with evidence, and a corrected rubric requires
      requalification against it.
- [ ] Defects that escaped review are attributed back to the reviewing profile.

## What this package cannot establish

> **This package measures the assumption; it cannot repair it.** If pairwise error
> correlation turns out to be high across every available model family, the honest
> consequence is that R3 independence is unattainable with the reviewer pool
> available — which is ADR-001's conclusion reached by measurement instead of by
> headcount. That would be a valuable result and an uncomfortable one, and the
> programme has to be willing to act on it rather than adjusting the threshold.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Assurance Lead** is assigned accountable; an implementer is named; **Eval Office / Independent Human Reviewer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-043` — Role-Based Model and Skill Evaluation, and Golden Set Management — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-086` — Frozen and Blind Review Package Builder — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-087` — Mechanical Verification Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-088` — Blind, Cross-Family and Adversarial Review — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-089` — DisagreementCase and Evidence-Weighted Arbitration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-113` — Evidence, Reproduction and Publication Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Eval Office / Independent Human Reviewer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-07` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-38` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

<!-- /generated:dod -->

## Non-waivable items

<!-- generated:nonwaivable — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/07_programme_risk_register.md`: *critical security, identity, evidence, reproduction and data blockers cannot be lowered by a numeric total.* The score exists for prioritisation; it is not a waiver mechanism.

The following cannot be waived on this package under any residual-risk acceptance:

- [ ] Identity and correlation failures.
- [ ] Data routing across a trust-zone boundary without policy.
- [ ] Artifact integrity or lineage loss.
- [ ] A reviewer independence violation.
- [ ] A missing or unverifiable `EvidenceManifest`.
- [ ] `CTL-GOV-02` failing its effectiveness test.
- [ ] `CTL-EPI-04` failing its effectiveness test.

> A package with an open item above is `BLOCKED`, not `ACCEPTED with conditions`. The distinction is the reason the list exists.

<!-- /generated:nonwaivable -->

## Verifier's decision

Completed by the independent verifier, not by the producer. **Issuance is not acceptance** — a package that has produced evidence and has not been verified is `TECH_COMPLETE`.

| Field | Value |
|---|---|
| Verifier | |
| Independence profile applied | R1 / R2 declared-partial / R3 — see ADR-001 |
| Dimensions **not** met | *(an R2 profile that lists only its strengths is not a declaration)* |
| Target revision verified | |
| Decision | `PENDING` / `ACCEPTED` / `REJECTED` |
| Date | |
| Conditions and their expiry | |
