---
title: "WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control — Acceptance Criteria"
aliases:
  - "WP-145 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-145_search_selection_fusion_stagnation.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-145` |
| Work package | [`WP-145` — Search Selection, Cross-Branch Fusion and Stagnation Control](wp_145_search_selection_fusion_stagnation.md) |
| Companion | [test procedures](wp_145_search_selection_fusion_stagnation.tests.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **FinOps Lead / Assurance Lead** — the independent verifier |
| Accountable owner | Experiment Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-145` |

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

Each criterion names the test case in [`WP-145_search_selection_fusion_stagnation.tests.md`](wp_145_search_selection_fusion_stagnation.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A `ResearchBudgetContract` with **no stop condition** is refused at
      construction.
- [ ] The selector returns the expected node on a fixed fixture under both metric
      directions, resolves ties deterministically, and does not treat a missing
      metric as zero.
- [ ] A previously expanded interior node remains eligible for re-expansion.
- [ ] The same graph snapshot and configuration produce the **same decision** on
      repeat runs.
- [ ] A selection score, a normalised rank or a tournament position cannot be
      written into a `VerifiedValue`, a claim assessment or a gate record.
- [ ] A `FusionProposal` names the inherited mechanism per parent, the expected
      interaction and the falsification condition; an incompatible combination
      raises a check rather than producing a candidate.
- [ ] The stagnation detector is **silent one iteration before** the configured
      window and **fires at it**, and takes the action the recorded policy names.
- [ ] Each of cost, rounds, experiment count, compute and convergence patience
      stops the campaign at its own boundary, and the stop record names which.
- [ ] **`STOPPED_BY_BUDGET` satisfies no gate**, and budget reserved for VERIFY,
      FULL and G7 reproduction cannot be consumed by exploration.

## What this package cannot establish

> **What this package cannot establish.** That the allocation is *good*. A
> selector that is deterministic, bounded and auditable can still spend a
> campaign's budget on the wrong branch, and only measurement against a benchmark
> — MLE-Bench, EXP-Bench, the ablations in WP-130 — says whether the policy
> earns its complexity. The thresholds shipped here are an initial experimental
> profile, not calibrated settings, and this package does not pretend otherwise.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Experiment Platform Lead** is assigned accountable; an implementer is named; **FinOps Lead / Assurance Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-083` — ExperimentBatch and Staged Execution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-100` — Cost Ledger, Budget Envelopes and FinOps — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-144` — Discovery Search Graph and Candidate Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **FinOps Lead / Assurance Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-09` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-58` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-59` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-101` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-02` failing its effectiveness test.

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
