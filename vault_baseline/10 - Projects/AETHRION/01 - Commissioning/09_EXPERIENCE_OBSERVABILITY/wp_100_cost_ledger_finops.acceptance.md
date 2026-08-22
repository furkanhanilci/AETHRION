---
title: "WP-100 — Cost Ledger, Budget Envelopes and FinOps — Acceptance Criteria"
aliases:
  - "WP-100 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/gate/g8
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-100 — Cost Ledger, Budget Envelopes and FinOps — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-100` |
| Work package | [`WP-100` — Cost Ledger, Budget Envelopes and FinOps](wp_100_cost_ledger_finops.md) |
| Companion | [test procedures](wp_100_cost_ledger_finops.tests.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Project Decision Owner / Internal Audit** — the independent verifier |
| Accountable owner | FinOps Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-100` |

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

Each criterion names the test case in [`WP-100_cost_ledger_finops.tests.md`](wp_100_cost_ledger_finops.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Spending is **reserved before the first billable call**, and an unreserved
      billable call is **refused**. Accounting after the fact reports a runaway; it
      does not prevent one.
- [ ] Costs are ingested from all five sources — model gateway, compute, tool,
      storage and **human triage**. A model that counts tokens and ignores the hours
      a person spent has mispriced the scarcest resource in the system.
- [ ] **Fan-out and retries draw from the original reservation and never extend
      it.** A retry storm exhausts the budget rather than growing it — this is
      `PR-09`'s early signal.
- [ ] The 80% threshold warns without stopping; **at 100% no new expensive work
      opens and the workflow pauses without losing state**, and a bypass attempt is
      refused.
- [ ] Reaching the hard limit raises a `DecisionRequest` to the owner.
- [ ] **Cost is attributed to outcome** — per claim, per reproduction, and per
      negative result — and the cost of work producing a negative result is
      **visible and not labelled waste**.
- [ ] Provider invoices reconcile against the ledger, a variance above threshold
      opens a case, and **every case carries an owner**.
- [ ] The forecast states its assumptions.

## What this package cannot establish

> **A budget bounds spend, not value.** This ledger can say what a claim cost and
> can stop a runaway. It cannot say whether the claim was worth producing — that is
> the portfolio judgement `00_PROGRAM/08` places with the Research Director, and
> `PR-12`'s *false rigor* describes the failure where a well-budgeted, fully
> attributed programme produces artifacts nobody needed.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **FinOps Lead** is assigned accountable; an implementer is named; **Project Decision Owner / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-015` — Event Envelope, Subject and Schema Taxonomy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-028` — NATS JetStream and Transactional Outbox Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-041` — LiteLLM Model Gateway Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-045` — Policy Router and Minimum-Sufficient Model Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-052` — Kubernetes Cluster and Node Pool Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-053` — Kueue Queue, Quota and Priority Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-082` — Run Registry and MLflow Lineage Integration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-096` — OpenTelemetry End-to-End Correlation Spine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Project Decision Owner / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-09` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-29` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
