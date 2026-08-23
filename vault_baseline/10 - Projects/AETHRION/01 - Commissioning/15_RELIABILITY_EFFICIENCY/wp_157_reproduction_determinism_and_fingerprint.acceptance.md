---
title: "WP-157 — Reproduction Determinism and Model Execution Fingerprint — Acceptance Criteria"
aliases:
  - "WP-157 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-157_reproduction_determinism_and_fingerprint.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/g7
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-157 — Reproduction Determinism and Model Execution Fingerprint — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-157` |
| Work package | [`WP-157` — Reproduction Determinism and Model Execution Fingerprint](wp_157_reproduction_determinism_and_fingerprint.md) |
| Companion | [test procedures](wp_157_reproduction_determinism_and_fingerprint.tests.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Assurance Lead / Independent Grader** — the independent verifier |
| Accountable owner | Reproducibility Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-157` |

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

Each criterion names the test case in [`WP-157_reproduction_determinism_and_fingerprint.tests.md`](wp_157_reproduction_determinism_and_fingerprint.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A contributing model invocation without a complete fingerprint **fails the
      run**, and retry and fallback history is part of that completeness.
- [ ] A silent failover is visible in the fingerprint and invalidates any `EXACT`
      claim.
- [ ] `EXACT` is refused for hosted black-box execution; the asserted level is one
      the substrate can support.
- [ ] A distributional claim uses a **pre-declared** run count and interval;
      widening either afterwards is refused and recorded.
- [ ] Shared cache, inherited credential and warm-layer paths between zones are
      each closed, and the evaluator canary appears in zero producer artifacts.
- [ ] Only a genuinely independent environment yields reproduced status, decided
      by environment digest lineage rather than by declaration.
- [ ] The reproduction package executes with no agent context present.

## What this package cannot establish

> **What this package cannot establish.** That a distributional reproduction means
> the result is right. It means repeated execution lands within a declared
> interval, which is a statement about stability under a specific substrate on a
> specific date. A hosted model changed by its provider next month will not
> reproduce, and the fingerprint is what makes that diagnosable rather than
> mysterious — it does not make it preventable.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Reproducibility Lead** is assigned accountable; an implementer is named; **Assurance Lead / Independent Grader** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-084` — Clean-Room Reproduction Environment — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Independent Grader** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-113` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-114` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-115` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-116` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-01` failing its effectiveness test.
- [ ] `CTL-EPI-03` failing its effectiveness test.

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
