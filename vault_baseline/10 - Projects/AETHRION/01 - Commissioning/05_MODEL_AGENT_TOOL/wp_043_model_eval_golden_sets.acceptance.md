---
title: "WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management — Acceptance Criteria"
aliases:
  - "WP-043 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/gate/g6
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-043` |
| Work package | [`WP-043` — Role-Based Model and Skill Evaluation, and Golden Set Management](wp_043_model_eval_golden_sets.md) |
| Companion | [test procedures](wp_043_model_eval_golden_sets.tests.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Independent Domain/Assurance Reviewer** — the independent verifier |
| Accountable owner | Eval Office |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-043` |

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

Each criterion names the test case in [`WP-043_model_eval_golden_sets.tests.md`](wp_043_model_eval_golden_sets.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every eval set is composed of labelled golden, adversarial and regression
      items, with splits isolated from training and trace identities.
- [ ] **A planted canary is detected** by the contamination check.
- [ ] Grader-versus-human agreement is **reported as a measured number** with
      disagreements itemised. An uncalibrated grader does not pass.
- [ ] **Every non-waivable skill has a RED transcript** — the scenario run without
      the skill, with the failure captured verbatim — and a GREEN transcript where
      it does not occur. This closes the repository's largest untested claim.
- [ ] A skill whose RED and GREEN transcripts are identical is **flagged**: it
      changed nothing, and a baseline that cannot distinguish presence from absence
      is not evidence.
- [ ] Every anticipated rationalization table is **replaced by observed text**.
- [ ] All five pressure scenarios are run per non-waivable skill — time, authority,
      sunk cost, partial success, "just this once" — and each outcome is recorded
      whether it held or not.
- [ ] Trigger resolution is tested in all four outcomes: right skill, wrong skill,
      no skill, two competing skills. Competing skills resolve deterministically or
      refuse.
- [ ] Skill survival is tested across **context compaction, session restart and
      long-run drift**; loss is detected rather than assumed absent.
- [ ] A **cross-model × cross-harness compliance matrix** exists with a populated
      cell for every non-waivable skill.

## What this package cannot establish

> **The measurement this package still cannot supply.** Whether a skill's presence
> improves *research outcomes* rather than procedural compliance. RED/GREEN shows
> a skill changes behaviour; the compliance matrix shows where. Neither shows that
> the changed behaviour produces better claims — that requires the lab's own
> false-positive and false-negative rates, which is **PR-18** and an uncovered
> area in `00_PROGRAM/11`. A perfectly compliant laboratory can still be
> systematically wrong.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Eval Office** is assigned accountable; an implementer is named; **Independent Domain/Assurance Reviewer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-018` — Claim, Evidence, Review and Decision Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-029` — MLflow Experiment and Evaluation Tracking Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-042` — Capability Registry and Profile Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Independent Domain/Assurance Reviewer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-07` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-37` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-MOD-01` failing its effectiveness test.
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
