---
title: "WP-119 — Controlled Pilot and Cutover Rehearsal — Acceptance Criteria"
aliases:
  - "WP-119 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-119_pilot_cutover_rehearsal.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w7
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-119 — Controlled Pilot and Cutover Rehearsal — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-119` |
| Work package | [`WP-119` — Controlled Pilot and Cutover Rehearsal](wp_119_pilot_cutover_rehearsal.md) |
| Companion | [test procedures](wp_119_pilot_cutover_rehearsal.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board / Independent Observer** — the independent verifier |
| Accountable owner | Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-119` |

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

Each criterion names the test case in [`WP-119_pilot_cutover_rehearsal.tests.md`](wp_119_pilot_cutover_rehearsal.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The pilot is realistic, low risk and runs on **minimised data**; running on
      unminimised production-equivalent data is refused. A production-equivalent
      environment is a production-equivalent exposure.
- [ ] **The pilot completes G0–G10** on the real RC, configuration and data volume,
      producing eleven gate records, a publication package and a G10 scan.
- [ ] **Operations, decision and assurance SLAs are all measured as numbers**, the
      human attention quota was not exceeded, and the assurance queue did not grow
      without bound.
- [ ] **A person completed the decision path under time pressure**, with friction
      points recorded. A pilot that is technically clean and operationally unusable
      has failed.
- [ ] **The cutover runbook is rehearsed including abort and rollback**, and both
      return the system to a known state with integrity queries passing. Almost
      nobody rehearses the abort, and it is the procedure the real event will need.
- [ ] Abort thresholds and decision owners are **explicit**, and the abort holder can
      act **without the sponsor's consent**.
- [ ] Pilot feedback becomes a **correction package with owners and re-tests**, not a
      backlog list.
- [ ] The recommendation records its reasons and **`no-go` is reachable**.

## What this package cannot establish

> **A pilot is one project.** It demonstrates that the system can carry a realistic
> low-risk project once, with the operator watching. It says little about the
> second concurrent project, about an R3 project — which ADR-001 blocks — or about
> the system after three months of drift. The rehearsal's real output is the
> correction package, and a pilot that produced none should be treated as
> incomplete rather than as clean.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Program Lead** is assigned accountable; an implementer is named; **Commissioning Board / Independent Observer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-115` — Full System Regression and Commissioning Dossier — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-116` — Resilience, Chaos and Failure-Injection Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-117` — Performance, Capacity and Load Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-118` — Operational Readiness, On-Call and Runbook Simulation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Commissioning Board / Independent Observer** verified **independently of the producer** and did not see the producer's working trace.
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
