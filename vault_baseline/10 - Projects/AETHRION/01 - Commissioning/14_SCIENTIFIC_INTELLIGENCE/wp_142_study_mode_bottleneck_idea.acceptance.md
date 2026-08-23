---
title: "WP-142 — Study Mode, Bottleneck and Idea Card Model — Acceptance Criteria"
aliases:
  - "WP-142 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-142_study_mode_bottleneck_idea.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-142 — Study Mode, Bottleneck and Idea Card Model — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-142` |
| Work package | [`WP-142` — Study Mode, Bottleneck and Idea Card Model](wp_142_study_mode_bottleneck_idea.md) |
| Companion | [test procedures](wp_142_study_mode_bottleneck_idea.tests.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Assurance Lead / Methodologist** — the independent verifier |
| Accountable owner | Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-142` |

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

Each criterion names the test case in [`WP-142_study_mode_bottleneck_idea.tests.md`](wp_142_study_mode_bottleneck_idea.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] `StudyMode` and assurance class are separate machine-readable fields, and
      a `FEASIBILITY` R3 project is expressible.
- [ ] A `StudyModeRecord` carries an **external** timestamp. A local clock does
      not establish that a plan preceded a result.
- [ ] A confirmatory `ClaimVersion` is refused where the analysis plan seal
      post-dates the first official outcome, and the refusal names the ordering.
- [ ] The claim ceiling **lowers by record and never rises on the same data** —
      both directions demonstrated in the same run.
- [ ] A bottleneck cannot hold the evidence-backed status on a model assertion
      alone, and contradictory literature is retained rather than dropped.
- [ ] An `IdeaCard` without a falsification plan cannot be promoted to hypothesis
      candidate; an exploratory idea is still permitted with the correct label.
- [ ] `PriorArtCollision` reports problem, mechanism, data, evaluation and
      contribution overlap **separately** — a single similarity scalar does not
      satisfy this.
- [ ] The planted duplicate is scored HIGH **and** the genuinely novel idea is
      not. One direction alone does not pass.
- [ ] One project completes G0→G2 producing every typed record, and one planted
      novelty or falsification defect is caught.

## What this package cannot establish

> **What this package cannot establish.** That the bottleneck is real. Evidence
> references prove somebody cited something; whether the limitation actually
> limits the field is a scientific judgement that review makes and this package
> only makes reviewable. Nor does it establish that the novelty verdict is
> correct — that verdict is V2 and inherits the error rate of whichever verifier
> produced it, which is `ADR-008`'s problem and WP-126's measurement.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Research Director** is assigned accountable; an implementer is named; **Assurance Lead / Methodologist** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-008` — G0–G10 Gate and Assurance Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-018` — Claim, Evidence, Review and Decision Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-034` — G0 Intake and G1 Charter Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-141` — Upstream Assimilation, Lineage and Characterisation Governance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Methodologist** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-56` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
