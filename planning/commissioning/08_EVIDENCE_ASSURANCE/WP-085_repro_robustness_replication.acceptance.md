# WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-085` |
| Work package | [`WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline](WP-085_repro_robustness_replication.md) |
| Companion | [test procedures](WP-085_repro_robustness_replication.tests.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Assurance Lead / Statistician** — the independent verifier |
| Accountable owner | Reproducibility Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-085` |

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

Each criterion names the test case in [`WP-085_repro_robustness_replication.tests.md`](WP-085_repro_robustness_replication.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The type selector produces a **different minimum combination per risk class**,
      and **one type cannot substitute for another**.
- [ ] All four types run under **separate protocols, tolerances and certificates**:
      repeatability, reproducibility, robustness, replication.
- [ ] Robustness assesses **the conclusion**, not the point estimate.
- [ ] **Deterministic reproduction of a hosted-model run is refused on structural
      grounds** — not reported as a tolerance failure. The constraint is that a
      hosted model carries no pinnable snapshot, and the certificate must say so.
- [ ] A local open-weight run reproduces deterministically by weight-file hash.
- [ ] A reproducer who produced the original is refused, and one who acquires
      context after assignment is refused **at the gate**.
- [ ] **Tolerances are pre-registered**; widening one after seeing the result is
      refused, and running with no declared tolerance is refused.
- [ ] **All six root-cause categories are exercised**, and only *defect in the
      original* implies the claim was wrong. A report with no root cause is refused.
- [ ] A failed confirmatory reproduction marks the claim **`CHALLENGED`**.
- [ ] Every completed verification issues a certificate naming type, tolerance,
      environment, independence profile and outcome.

## What this package cannot establish

> **R3 is `BLOCKED` under a solo operator and this package cannot change that.**
> ADR-001 decided it: R3 requires an external verifier, and independence is
> declared rather than waived. This package can run every verification type
> correctly and still not produce an R3-eligible result, because the constraint is
> organisational rather than technical — and `00_PROGRAM/07`'s `PR-21` names it.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Reproducibility Lead** is assigned accountable; an implementer is named; **Assurance Lead / Statistician** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-077` — Claim State, Dependency and Assessment Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-081` — Protocol, Analysis, Baseline and Falsification Registry — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-082` — Run Registry and MLflow Lineage Integration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-083` — ExperimentBatch and Staged Execution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-084` — Clean-Room Reproduction Environment — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Statistician** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-19` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-20` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-65` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-66` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-67` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-114` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
