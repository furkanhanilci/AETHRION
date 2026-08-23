---
title: "WP-124 — Model Requalification, Drift and Ejection Rhythm — Acceptance Criteria"
aliases:
  - "WP-124 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-124_model_requalification_drift.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g10
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-124 — Model Requalification, Drift and Ejection Rhythm — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-124` |
| Work package | [`WP-124` — Model Requalification, Drift and Ejection Rhythm](wp_124_model_requalification_drift.md) |
| Companion | [test procedures](wp_124_model_requalification_drift.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Admission Board / Safety / FinOps** — the independent verifier |
| Accountable owner | Eval Office |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-124` |

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

Each criterion names the test case in [`WP-124_model_requalification_drift.tests.md`](wp_124_model_requalification_drift.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every admitted profile has an expiry, and **passing it makes the profile
      ineligible without human action**.
- [ ] The provider change monitor runs on cadence, and **a capability fingerprint
      shift behind a stable name triggers requalification automatically**. An alias
      repoint is never accepted as a pin.
- [ ] **Regression results are compared against the profile's own prior results**,
      not only against the incumbent — requalification asks whether performance
      *changed*, which is a different question from initial admission.
- [ ] **Production drift analysis detects a small quality regression that produces no
      error.** Nothing else in the system would see it.
- [ ] Quality-adjusted cost drift is reported and a worsening ratio raised.
- [ ] Suspension and ejection record actor, reason and evidence, and **ejection
      produces an impact scan naming every open task, run and claim** using the
      profile — invariant 7.
- [ ] **The router cache is invalidated on ejection** and the profile is not
      selectable; a stale cache is detected and rebuilds from the registry.
- [ ] Every claim produced under an ejected profile reaches a disposition — re-run,
      re-review, or accepted **with a recorded reason**.

## What this package cannot establish

> **Drift is detected between checks only where it is measured.** Scheduled
> requalification catches gross change; production drift analysis catches gradual
> change in the dimensions being watched. A model that degrades on a capability
> nobody measures degrades unnoticed — which is `PR-18`'s territory, and the reason
> WP-126's calibration work is a sibling of this package rather than a duplicate.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Eval Office** is assigned accountable; an implementer is named; **Admission Board / Safety / FinOps** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-042` — Capability Registry and Profile Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-043` — Role-Based Model and Skill Evaluation, and Golden Set Management — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-044` — Model Qualification and Admission Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-045` — Policy Router and Minimum-Sufficient Model Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-108` — Retraction, Drift and Supersession Vertical Slice — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Admission Board / Safety / FinOps** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

**No acceptance scenario names this package.** It can reach `ACCEPTED` on its own evidence and cannot reach `COMMISSIONED` through a scenario, because there is none to pass. `00_PROGRAM/11`'s completeness rule calls this an incomplete entry rather than a shorter one.

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
- [ ] `CTL-MOD-02` failing its effectiveness test.

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
