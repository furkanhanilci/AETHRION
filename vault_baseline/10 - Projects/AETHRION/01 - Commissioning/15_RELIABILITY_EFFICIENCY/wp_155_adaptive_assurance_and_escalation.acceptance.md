---
title: "WP-155 — Adaptive Assurance, Verifier Qualification and Escalation — Acceptance Criteria"
aliases:
  - "WP-155 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-155_adaptive_assurance_and_escalation.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g6
  - aethrion/gate/g7
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-155 — Adaptive Assurance, Verifier Qualification and Escalation — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-155` |
| Work package | [`WP-155` — Adaptive Assurance, Verifier Qualification and Escalation](wp_155_adaptive_assurance_and_escalation.md) |
| Companion | [test procedures](wp_155_adaptive_assurance_and_escalation.tests.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Eval Office / Internal Audit** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-155` |

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

Each criterion names the test case in [`WP-155_adaptive_assurance_and_escalation.tests.md`](wp_155_adaptive_assurance_and_escalation.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] V0 always runs first, and a V0 or V1 failure remains non-waivable
      regardless of any later class.
- [ ] A missing, expired or threshold-mismatched qualification yields
      `INCONCLUSIVE` and blocks; only a current, matching one satisfies.
- [ ] Advisory verdicts from unqualified verifiers are retained and labelled.
- [ ] `ABSTAIN` escalates, satisfies no requirement, is **not** recorded as a
      failure, and its rate is a tracked qualification metric.
- [ ] A verifier that never abstains on the ambiguous calibration set **fails
      qualification**.
- [ ] A route cannot be lowered by queue length or by budget pressure, and
      low-consequence claims still route cheaply.

## What this package cannot establish

> **What this package cannot establish.** That the qualified verifiers are
> accurate on anything outside their calibration set. Qualification is a
> measurement on labelled data at a threshold, and generalisation beyond it is an
> assumption — which is why the key carries the task class and the domain profile,
> and why an expiry exists at all. A verifier qualified on citation entailment
> says nothing about its method–code alignment.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Assurance Lead** is assigned accountable; an implementer is named; **Eval Office / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-044` — Model Qualification and Admission Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-087` — Mechanical Verification Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-126` — Reviewer, Judge and Reproducer Calibration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Eval Office / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-107` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-108` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-109` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-01` failing its effectiveness test.
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
