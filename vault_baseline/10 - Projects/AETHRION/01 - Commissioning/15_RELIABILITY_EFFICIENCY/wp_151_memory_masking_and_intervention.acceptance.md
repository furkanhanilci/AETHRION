---
title: "WP-151 — Memory Masking and Proactive Intervention — Acceptance Criteria"
aliases:
  - "WP-151 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-151_memory_masking_and_intervention.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/m
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-151 — Memory Masking and Proactive Intervention — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-151` |
| Work package | [`WP-151` — Memory Masking and Proactive Intervention](wp_151_memory_masking_and_intervention.md) |
| Companion | [test procedures](wp_151_memory_masking_and_intervention.tests.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Assurance Lead / Archivist** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-151` |

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

Each criterion names the test case in [`WP-151_memory_masking_and_intervention.tests.md`](wp_151_memory_masking_and_intervention.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Refuted, superseded and stale items do not enter reasoning context, and
      current items do.
- [ ] Every excluded item remains retrievable by a failure-history query.
- [ ] Masking deletes nothing and re-labels nothing — it is a read policy.
- [ ] Procedural, search-experience and principle memory cannot support a claim,
      including through a lesson derived from a failed approach.
- [ ] A reminder fires on a material step, carries canonical artifact references,
      and **creates no new assertion**.
- [ ] No reminder fires on an ordinary step — the mechanism is selective rather
      than per-turn.
- [ ] Planted poisoned content does not become retrievable as established fact.

## What this package cannot establish

> **What this package cannot establish.** That the mask keeps the right things.
> Relevance is a judgement, and an item wrongly excluded is invisible by
> construction — nothing in the record shows what an agent did not see. The
> failure-history query is the partial mitigation and it is only useful to someone
> who thinks to ask. Measuring the cost of exclusion is a metascience question
> that WP-130 owns and that no test here answers.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Lead** is assigned accountable; an implementer is named; **Assurance Lead / Archivist** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-146` — Epistemic Memory Taxonomy and Retention — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-150` — Communication Governor, Edge Utility and Context Projection — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Archivist** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-096` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-097` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-098` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-04` failing its effectiveness test.
- [ ] `CTL-DAT-03` failing its effectiveness test.

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
