---
title: "WP-147 — Scientific Council and Meta-Review Cognition — Acceptance Criteria"
aliases:
  - "WP-147 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-147_scientific_council_cognition.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/m
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/gate/g4
  - aethrion/gate/g6
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-147 — Scientific Council and Meta-Review Cognition — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-147` |
| Work package | [`WP-147` — Scientific Council and Meta-Review Cognition](wp_147_scientific_council_cognition.md) |
| Companion | [test procedures](wp_147_scientific_council_cognition.tests.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Assurance Lead / Internal Audit** — the independent verifier |
| Accountable owner | Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-147` |

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

Each criterion names the test case in [`WP-147_scientific_council_cognition.tests.md`](wp_147_scientific_council_cognition.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] `CognitiveFunction` is a distinct type from `RoleContract`, and governance
      role, cognitive function, runtime actor and model profile are **four
      separate fields**.
- [ ] A council session cannot write a `GateRecord`, a `ClaimVersion`, an
      `EvidenceSpan` or a `ReviewVerdict`. All four refused, separately.
- [ ] Council output is labelled a recommendation on every surface that stores,
      displays or exports it.
- [ ] Parallel councils cannot observe one another before both are locked, and
      post-lock disclosure works through the protocol path.
- [ ] A planted minority position **survives synthesis**, and a genuinely
      unanimous council is **not** reported as disputed.
- [ ] The task compiler selects cognitive functions and model profiles; a
      producer cannot summon its own.
- [ ] A council participant cannot be bound as reviewer of the same artefact
      where the independence profile forbids it.
- [ ] A locked session is immutable, and the governance catalogue is still
      fourteen functions after this package lands.

## What this package cannot establish

> **What this package cannot establish.** That the advice is any good. Structural
> separation guarantees a recommendation cannot become a verdict; it says nothing
> about whether the recommendation was worth having, and a council of five model
> profiles that share a training corpus may agree confidently and be wrong
> together. Measuring that is WP-126's error-correlation work, and until it runs,
> a unanimous council is evidence of agreement and not of correctness.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Research Director** is assigned accountable; an implementer is named; **Assurance Lead / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-003` — Role Catalogue and RACI Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-046` — LangGraph Bounded Cognition Runtime — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-047` — Role and Skill Registries, and the Task Compiler — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-086` — Frozen and Blind Review Package Builder — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-142` — Study Mode, Bottleneck and Idea Card Model — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-72` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
