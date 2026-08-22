---
title: "WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows — Acceptance Criteria"
aliases:
  - "WP-035 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/04_CONTROL_EVENT/WP-035_g2_g4_workflows.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/04-control-event
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g2
  - aethrion/gate/g3
  - aethrion/gate/g4
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-035` |
| Work package | [`WP-035` — G2 Protocol, G3 Literature and G4 Baseline Workflows](wp_035_g2_g4_workflows.md) |
| Companion | [test procedures](wp_035_g2_g4_workflows.tests.md) |
| Workstream | `04_CONTROL_EVENT` |
| Approval authority | **Methodologist / Evidence Lead / Falsification Lead** — the independent verifier |
| Accountable owner | Scientific Workflow Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-035` |

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

Each criterion names the test case in [`WP-035_g2_g4_workflows.tests.md`](wp_035_g2_g4_workflows.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A frozen `ProtocolManifest` **cannot be edited in place**; an amendment
      requires a new version.
- [ ] An amendment made **before** any data is accepted; an amendment made
      **after** results exist is **refused for confirmatory use** and may proceed
      only as a declared exploratory study. The timestamp relative to the run is
      the control.
- [ ] G2b refuses to close with no analysis plan.
- [ ] A frozen `LiteratureSetManifest` resolves to exactly what it recorded and
      does **not** follow later registry changes.
- [ ] A retraction is visible **through** the frozen set without mutating it, and
      every dependent claim is reachable.
- [ ] G4 refuses without a `FalsificationPlan` — *no counter-test* is a blocker,
      not a warning.
- [ ] Golden-set content in the protocol inputs is **detected and refused before
      compute opens** (`PR-15`).
- [ ] G4 refuses with no budget envelope.
- [ ] Changing the protocol after G4 reopens G2 and invalidates downstream gates.

## What this package cannot establish

> **A frozen protocol is not a good protocol.** These gates enforce that the method
> was fixed in advance and that a counter-test exists. Whether the method answers
> the question, and whether the counter-test is a real one rather than a
> formality, is `adversarial-reviewing`'s job at G6 and `ACC-08`'s at
> commissioning. Freezing a weak design early only makes it harder to fix.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Scientific Workflow Lead** is assigned accountable; an implementer is named; **Methodologist / Evidence Lead / Falsification Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-008` — G0–G10 Gate and Assurance Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-032` — ProjectLifecycle Workflow Skeleton — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-033` — Gate Service and GateRecord Evaluation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-034` — G0 Intake and G1 Charter Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Methodologist / Evidence Lead / Falsification Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-01` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-39` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-02` failing its effectiveness test.
- [ ] `CTL-LIT-01` failing its effectiveness test.
- [ ] `CTL-CST-01` failing its effectiveness test.

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
