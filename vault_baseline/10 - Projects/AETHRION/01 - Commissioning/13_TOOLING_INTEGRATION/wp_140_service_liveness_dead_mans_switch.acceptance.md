---
title: "WP-140 — Service Liveness Monitoring and Dead-Man's Switch — Acceptance Criteria"
aliases:
  - "WP-140 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-140_service_liveness_dead_mans_switch.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/s
  - aethrion/gate/platform
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-140 — Service Liveness Monitoring and Dead-Man's Switch — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-140` |
| Work package | [`WP-140` — Service Liveness Monitoring and Dead-Man's Switch](wp_140_service_liveness_dead_mans_switch.md) |
| Companion | [test procedures](wp_140_service_liveness_dead_mans_switch.tests.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Metascience Lead** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-140` |

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

Each criterion names the test case in [`WP-140_service_liveness_dead_mans_switch.tests.md`](wp_140_service_liveness_dead_mans_switch.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **Every periodic job is in the inventory** with a declared interval and
      tolerance, and a scheduled job with no registry entry is **detected** — an
      unwatched periodic job is an unwatched control.
- [ ] Every job emits a **heartbeat on success**, and **suppressing a job entirely
      fires an alarm within its tolerance**. Absence alarms distinguishably from
      failure.
- [ ] **The monitor is self-hosted and independent**: it still alarms when the
      watched infrastructure is down, and running it on that infrastructure is
      refused.
- [ ] **A job that processed part of its input reports `PARTIAL`, never
      `SUCCEEDED`**, and the shortfall is named. This is finding **H1**'s pattern —
      a capped read recorded as a successful run — generalised into a rule.
- [ ] Repeated `PARTIAL` results **escalate**; repeated partial success is a defect,
      not a status.
- [ ] Alarms bind to WP-134's escalation chain and **promote if unacknowledged**; an
      alarm with no owner is refused.
- [ ] **The monitor's own liveness is watched by an independent means.** A watcher
      nobody watches is the same silent failure one level up.

## What this package cannot establish

> **This package protects every other schedule in the programme.** The G10 scans, the
> control-effectiveness tests, the calibration runs, the drift analysis and the
> quarterly drills are all periodic, and every one of them fails the same way: it
> stops, nothing errors, and the absence reads as a clean result. Until this exists,
> a clean report from any scheduled control is consistent with the control not
> having run — which is why `PR-20` is on the register and why this is the last
> package in the plan rather than an afterthought.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **SRE Lead** is assigned accountable; an implementer is named; **Metascience Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-101` — Service Catalogue, SLOs and Alert/Runbook Binding — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-131` — Notification Broker Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-134` — Escalation and Paging — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Metascience Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-42` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-43` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OBS-01` failing its effectiveness test.

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
