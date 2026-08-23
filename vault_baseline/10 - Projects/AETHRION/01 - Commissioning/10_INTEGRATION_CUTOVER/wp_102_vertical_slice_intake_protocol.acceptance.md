---
title: "WP-102 — Vertical Slice 1 — Intake through Protocol Freeze — Acceptance Criteria"
aliases:
  - "WP-102 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-102_vertical_slice_intake_protocol.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-102 — Vertical Slice 1 — Intake through Protocol Freeze — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-102` |
| Work package | [`WP-102` — Vertical Slice 1 — Intake through Protocol Freeze](wp_102_vertical_slice_intake_protocol.md) |
| Companion | [test procedures](wp_102_vertical_slice_intake_protocol.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Assurance / Project Decision Owner** — the independent verifier |
| Accountable owner | Research Workflow Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-102` |

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

Each criterion names the test case in [`WP-102_vertical_slice_intake_protocol.tests.md`](wp_102_vertical_slice_intake_protocol.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Both an R1 and an R3 fixture are run, and they are **realistic rather than
      minimal** — a slice that only exercises the happy path has tested the path
      that works.
- [ ] Risk, execution and independence profiles all bind at G1 and **compose into
      one `ControlPlan`**; where two imply conflicting controls the **stricter
      applies** and the conflict is recorded.
- [ ] A charter with no falsifying observation **fails G1**.
- [ ] **The R3 project reaches `BLOCKED` with the ADR-001 declaration** naming the
      missing external verifier, and forcing past it is refused. For a solo
      laboratory that block is the **correct** outcome, not a failure of the slice.
- [ ] An expired G1 decision fails closed and escalates; a non-delegable decision
      cannot be delegated.
- [ ] **Budget is reserved before any compute opens**, and the hard limit pauses the
      workflow without losing state.
- [ ] Closing G0, G1 and G2 in one session emits **three separate `GateRecord`s**.
- [ ] The revise path records both attempts; a post-G2 protocol change **reopens G2**
      and invalidates downstream.
- [ ] The audit export verifies from the **standalone verifier**, and one correlation
      identifier runs from the cockpit command to the gate record.
- [ ] **Every defect this slice exposes is filed against the upstream package it is
      in.** Finding defects is this package's function; a slice reporting only
      success has probably not been run against anything realistic.

## What this package cannot establish

> **Two projects and three gates is not the system.** This slice proves G0–G2
> compose. G3 through G10 involve literature freezing, execution, review,
> reproduction, decision, publication and monitoring — six more packages of seam,
> and each subsequent slice (WP-103–106) exists because the previous one cannot
> speak for it. `docs/STATUS.md` will keep printing *no research question has
> travelled G0 → G10* until WP-106 completes.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Research Workflow Lead** is assigned accountable; an implementer is named; **Assurance / Project Decision Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-034` — G0 Intake and G1 Charter Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-035` — G2 Protocol, G3 Literature and G4 Baseline Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-056` — Policy Decision Point and Bundle Distribution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-091` — Lab Cockpit Information Architecture and Application Shell — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-092` — Project Workspace and G0–G10 Gate Timeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-093` — Human Decision Queue and Evidence-Delta UI — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-100` — Cost Ledger, Budget Envelopes and FinOps — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-101` — Service Catalogue, SLOs and Alert/Runbook Binding — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance / Project Decision Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-25` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-26` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-GOV-03` failing its effectiveness test.

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
