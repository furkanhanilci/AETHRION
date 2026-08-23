---
title: "WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room — Acceptance Criteria"
aliases:
  - "WP-105 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.acceptance.md"
generated: false
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
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-105` |
| Work package | [`WP-105` — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](wp_105_vertical_slice_review_repro.md) |
| Companion | [test procedures](wp_105_vertical_slice_review_repro.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Independent Reproducibility Lead / Decision Owner** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-105` |

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

Each criterion names the test case in [`WP-105_vertical_slice_review_repro.tests.md`](wp_105_vertical_slice_review_repro.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Independence is enforced at assignment **and at the gate**; cross-family is
      required at R3.
- [ ] **The frozen package shows zero producer-trace artifacts** against a diff, and
      a seeded identifier is caught by the leak detector.
- [ ] **Mechanical verification runs before any reviewer**, and a model verdict
      cannot override a failing validator.
- [ ] **The adversarial reviewer produces a falsification attempt**, and *failed to
      falsify* is recorded distinctly from *assessed as sound*.
- [ ] Reviewer responses are sealed until all are in.
- [ ] **A real conflict is arbitrated**, and the disposition names **which evidence
      prevailed and why** — never which reviewer. Majority resolution is refused,
      and with no independent arbiter the case is **`BLOCKED` with a declaration**.
- [ ] **Both reproduction paths run**: a clean-room pass within tolerance, and a
      forced failure marking the claim **`CHALLENGED`**. A slice that only runs the
      succeeding case has not tested the root-cause machinery.
- [ ] **All six root-cause categories are exercised**, and only *defect in the
      original* implies the claim was wrong.
- [ ] A failed reproduction **reopens G4/G5**, invalidates downstream and moves the
      claim state.
- [ ] **The R3 claim reaches `BLOCKED` with the ADR-001 declaration.** An R3 pass in
      a solo laboratory means the control was broken, not that the claim was good.

## What this package cannot establish

> **Structural independence is what this slice can demonstrate.** Blind packages,
> distinct model families, sealed responses and a clean room all hold. What none of
> them measures is whether two independent reviewers were actually likely to
> disagree — `PR-16`, unmeasured, and the reason `measuring-agreement` and WP-126
> exist. A slice where every reviewer agreed is consistent with a well-run review
> and with a correlated one, and this slice cannot tell them apart.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Assurance Lead** is assigned accountable; an implementer is named; **Independent Reproducibility Lead / Decision Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-084` — Clean-Room Reproduction Environment — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-086` — Frozen and Blind Review Package Builder — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-087` — Mechanical Verification Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-088` — Blind, Cross-Family and Adversarial Review — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-089` — DisagreementCase and Evidence-Weighted Arbitration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-093` — Human Decision Queue and Evidence-Delta UI — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-095` — Claim/Evidence Explorer and Provenance Graph — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-104` — Vertical Slice 3 — Baseline through Run to Claim/Evidence — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Independent Reproducibility Lead / Decision Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-07` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-19` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-20` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-38` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-66` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-03` failing its effectiveness test.
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
