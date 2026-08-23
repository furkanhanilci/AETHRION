---
title: "WP-127 — FinOps, Capacity and Portfolio Review Rhythm — Acceptance Criteria"
aliases:
  - "WP-127 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-127_finops_portfolio.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g0
  - aethrion/gate/g4
  - aethrion/gate/g8
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-127 — FinOps, Capacity and Portfolio Review Rhythm — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-127` |
| Work package | [`WP-127` — FinOps, Capacity and Portfolio Review Rhythm](wp_127_finops_portfolio.md) |
| Companion | [test procedures](wp_127_finops_portfolio.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Internal Audit / Assurance** — the independent verifier |
| Accountable owner | FinOps Lead / Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-127` |

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

Each criterion names the test case in [`WP-127_finops_portfolio.tests.md`](wp_127_finops_portfolio.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Provider, compute and storage invoices reconcile against the ledger, and a
      variance above threshold **opens a case with an owner**.
- [ ] The forecast **states its assumptions** and compares against the envelope; one
      with unstated assumptions is refused.
- [ ] Fan-out cost is analysed separately from base work.
- [ ] **The expected value of verification reports both cost and defects caught**, and
      **reducing assurance capacity on that number alone is refused** — the
      calculation done naively always favours cutting the pool `00_PROGRAM/08`
      protects.
- [ ] Quality-adjusted cost **exposes a cheaper model that produces more rework**, and
      the production numbers feed back into routing.
- [ ] The capacity plan projects assurance wait and headroom, and **a growth forecast
      exceeding the human decision quota is refused or reduced** — throughput growth
      without decision capacity forecasts a `PR-04`.
- [ ] **A stop decision is taken and recorded on a low-value, high-cost project**, and
      **sunk cost is not accepted as a counter-argument**.
- [ ] A period with **no** stop or pivot decision across the portfolio is **reviewed**
      — a portfolio where nothing is ever stopped is not being managed.

## What this package cannot establish

> **Cost-per-outcome measures what was spent, not what was learned.** A negative
> result that closed a line of enquiry may be the most valuable thing a quarter
> produced and will appear in this ledger as expenditure with no claim. `PR-19` and
> `PR-12` both bear on it: a portfolio optimised on cost-per-claim will produce
> claims, and a laboratory that stops funding disconfirmation has stopped doing
> research.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **FinOps Lead / Research Director** is assigned accountable; an implementer is named; **Internal Audit / Assurance** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-100` — Cost Ledger, Budget Envelopes and FinOps — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-117` — Performance, Capacity and Load Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit / Assurance** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-CST-01` failing its effectiveness test.
- [ ] `CTL-CST-02` failing its effectiveness test.

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
