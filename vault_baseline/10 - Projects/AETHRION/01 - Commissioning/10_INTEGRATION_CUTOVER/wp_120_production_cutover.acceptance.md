---
title: "WP-120 — Production Cutover and Go-Live Decision — Acceptance Criteria"
aliases:
  - "WP-120 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-120_production_cutover.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w8
  - aethrion/effort/l
  - aethrion/gate/cutover
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-120 — Production Cutover and Go-Live Decision — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-120` |
| Work package | [`WP-120` — Production Cutover and Go-Live Decision](wp_120_production_cutover.md) |
| Companion | [test procedures](wp_120_production_cutover.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board / Internal Audit** — the independent verifier |
| Accountable owner | Executive Sponsor / Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-120` |

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

Each criterion names the test case in [`WP-120_production_cutover.tests.md`](wp_120_production_cutover.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **Every go-live entry condition is enforced**, with a separate refusal for each
      unmet one — including an open Critical, an **expired** residual-risk acceptance,
      and fewer than two restore rehearsals.
- [ ] All six digest classes are frozen and signed; any component referenced by tag
      is refused.
- [ ] **The pre-cutover restore point is verified, not merely taken**, and proceeding
      with an unverified backup is refused.
- [ ] Deployment is idempotent, every migration has a rehearsed rollback, and
      service, contract, security and **integrity** smoke tests all pass on the
      promoted RC.
- [ ] **Traffic, access and monitoring are enabled in a declared sequence, each step
      observed and each reversible.** Capabilities open together; traffic arrives in
      order.
- [ ] **Abort remains available at every stage, including after promotion**, returns
      to the verified restore point, and is **non-delegable and refused to an
      unauthorised actor**.
- [ ] The Go-Live `DecisionRecord` names the actor, the evidence, the residual risks
      with owners and expiries, and **what was not authorised**. `no-go` and `abort`
      are both recordable outcomes.
- [ ] The post-cutover audit snapshot is hash-chained and **verifies standalone**,
      becoming the baseline for every later integrity check.

## What this package cannot establish

> **Cutover authorises operation, not correctness.** The `DecisionRecord` states that
> a named person, having seen the evidence summary and the residual risk, decided to
> open production. It does not certify that the system produces correct research —
> `AGENTS.md` §11's limit still holds, and the benchmarks that would test it from
> outside remain unrun. What changes at cutover is that the consequences of being
> wrong become real.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Executive Sponsor / Program Lead** is assigned accountable; an implementer is named; **Commissioning Board / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-115` — Full System Regression and Commissioning Dossier — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-116` — Resilience, Chaos and Failure-Injection Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-117` — Performance, Capacity and Load Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-118` — Operational Readiness, On-Call and Runbook Simulation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-119` — Controlled Pilot and Cutover Rehearsal — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Commissioning Board / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-01` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-40` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `All controls` failing its effectiveness test.

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
