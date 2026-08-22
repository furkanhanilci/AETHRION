---
title: "WP-092 — Project Workspace and G0–G10 Gate Timeline — Acceptance Criteria"
aliases:
  - "WP-092 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-092_project_gate_timeline.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g0-g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-092 — Project Workspace and G0–G10 Gate Timeline — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-092` |
| Work package | [`WP-092` — Project Workspace and G0–G10 Gate Timeline](wp_092_project_gate_timeline.md) |
| Companion | [test procedures](wp_092_project_gate_timeline.tests.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Research Operations / Assurance** — the independent verifier |
| Accountable owner | Experience Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-092` |

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

Each criterion names the test case in [`WP-092_project_gate_timeline.tests.md`](wp_092_project_gate_timeline.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The timeline shows every gate's state, record and actor, and a project at G5
      shows the **frozen** protocol, literature set and analysis plan **marked as
      frozen**. Showing the current version beside a frozen run is refused or
      explicitly marked as not the version used.
- [ ] A reopened gate shows a **`GateRecord` diff**, its reason, its trigger and the
      downstream invalidation. Without the diff, a reopened-and-repassed gate is
      indistinguishable from one that passed first time.
- [ ] `BLOCKED`, `REVISE` and `DISAGREEMENT` each name **every failed check and what
      would change it**; a disagreement shows both positions with neither presented
      as the answer.
- [ ] **Ten real blocks were explained correctly by a reader who did not write the
      policy**, and the score is recorded. This is `PR-02`'s test, reaching a human.
- [ ] Artifact, manifest, review, reproduction and decision panels all resolve to
      canonical records by deep link.
- [ ] Accepted residual risks are visible with their expiry, and **an expired one
      surfaces as an open finding** rather than ageing silently.
- [ ] Every command goes through the authenticated Temporal Update API, and a
      command without the decision right is refused.
- [ ] Every project surface names the **next action and its owner**.

## What this package cannot establish

> **Explaining a block is not justifying it.** This surface reports which checks
> failed and what would clear them. Whether the check *should* have blocked is
> WP-008's policy and WP-009's control registry — and a project team that
> understands a block and disagrees with it has a governance question, not an
> interface one.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Experience Lead** is assigned accountable; an implementer is named; **Research Operations / Assurance** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-008` — G0–G10 Gate and Assurance Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-032` — ProjectLifecycle Workflow Skeleton — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-033` — Gate Service and GateRecord Evaluation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-034` — G0 Intake and G1 Charter Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-035` — G2 Protocol, G3 Literature and G4 Baseline Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-036` — G5 Execute through G9 Publish Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-037` — G10 Temporal Schedules and Short ImpactScan Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-091` — Lab Cockpit Information Architecture and Application Shell — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Research Operations / Assurance** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-GOV-01` failing its effectiveness test.
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
