---
title: "WP-153 — Research Budget, Token Ledger and Efficiency Control — Acceptance Criteria"
aliases:
  - "WP-153 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-153_research_budget_and_token_ledger.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-153 — Research Budget, Token Ledger and Efficiency Control — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-153` |
| Work package | [`WP-153` — Research Budget, Token Ledger and Efficiency Control](wp_153_research_budget_and_token_ledger.md) |
| Companion | [test procedures](wp_153_research_budget_and_token_ledger.tests.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Research Director / SRE Lead** — the independent verifier |
| Accountable owner | FinOps Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-153` |

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

Each criterion names the test case in [`WP-153_research_budget_and_token_ledger.tests.md`](wp_153_research_budget_and_token_ledger.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A budget contract with no stop condition is refused at construction.
- [ ] Every token carries exactly one category, the categories sum to the
      provider total, and coordination overhead is **derived** rather than
      estimated.
- [ ] Budget pressure degrades communication through the declared ladder and
      **never** reduces the cohort or lowers the assurance route.
- [ ] Exhaustion yields `BLOCKED_BUDGET` or a scope-reduction request, and a stop
      record satisfies no gate.
- [ ] Reserved verification, reproduction and assurance budget is unreachable
      from the exploration path, and remains affordable after an exploration stop.
- [ ] Deterministic tool results are reused, marked as reused, and respect declared
      freshness; non-deterministic tools are never reused.
- [ ] The release report carries a quality/cost frontier, not a cost number.

## What this package cannot establish

> **What this package cannot establish.** That the budget is well spent. A ledger
> shows where tokens went; whether the science they bought was worth buying is a
> portfolio judgement WP-127 makes. Nor does it establish that the degradation
> ladder preserves quality — that is WP-150's guard, and this package only
> guarantees the ladder degrades the right thing.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **FinOps Lead** is assigned accountable; an implementer is named; **Research Director / SRE Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-100` — Cost Ledger, Budget Envelopes and FinOps — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-145` — Search Selection, Cross-Branch Fusion and Stagnation Control — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-150` — Communication Governor, Edge Utility and Context Projection — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Research Director / SRE Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-099` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-100` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-101` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-102` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-02` failing its effectiveness test.
- [ ] `CTL-EPI-03` failing its effectiveness test.

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
