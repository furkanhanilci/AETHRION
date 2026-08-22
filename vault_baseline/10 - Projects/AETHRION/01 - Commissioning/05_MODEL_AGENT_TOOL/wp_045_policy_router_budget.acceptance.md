---
title: "WP-045 — Policy Router and Minimum-Sufficient Model Package — Acceptance Criteria"
aliases:
  - "WP-045 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g1
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-045 — Policy Router and Minimum-Sufficient Model Package — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-045` |
| Work package | [`WP-045` — Policy Router and Minimum-Sufficient Model Package](wp_045_policy_router_budget.md) |
| Companion | [test procedures](wp_045_policy_router_budget.tests.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Safety / Eval / FinOps** — the independent verifier |
| Accountable owner | Model Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-045` |

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

Each criterion names the test case in [`WP-045_policy_router_budget.tests.md`](wp_045_policy_router_budget.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The same `TaskContract` routes identically every time.
- [ ] A task with no eligible profile **blocks**; it never falls back to an
      unadmitted model.
- [ ] The **minimum sufficient** package is selected, and requesting a larger one
      is refused or requires a recorded justification.
- [ ] Policy pre-filtering denies before the registry is queried.
- [ ] **A reviewer colliding with the producer's independence profile is refused at
      routing**, and refused again at gate time if context is acquired afterwards.
- [ ] Fan-out **reserves its full budget before the first call**, and a fan-out
      exceeding the remaining budget is refused before any call is made. Retries
      draw from the reservation rather than extending it.
- [ ] Every `RouteDecision` names the eligibility query, the candidate set, the
      ordering rule and the selection.
- [ ] The conformance suite has **a passing and a failing case for every declared
      routing rule**.

## What this package cannot establish

> **Deterministic routing does not make a run reproducible.** The router will
> select the same profile again; whether that profile still behaves the same is
> WP-042's expiry and WP-044's regression schedule. For hosted models the honest
> claim is *the same admitted profile was selected*, which is weaker than *the same
> model ran*.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Model Platform Lead** is assigned accountable; an implementer is named; **Safety / Eval / FinOps** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-041` — LiteLLM Model Gateway Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-042` — Capability Registry and Profile Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-044` — Model Qualification and Admission Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Safety / Eval / FinOps** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-09` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-10` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-11` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
- [ ] `CTL-DAT-02` failing its effectiveness test.
- [ ] `CTL-CST-01` failing its effectiveness test.
- [ ] `CTL-MOD-01` failing its effectiveness test.

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
