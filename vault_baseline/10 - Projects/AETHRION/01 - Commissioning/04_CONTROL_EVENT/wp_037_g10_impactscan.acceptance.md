---
title: "WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows — Acceptance Criteria"
aliases:
  - "WP-037 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/04_CONTROL_EVENT/WP-037_g10_impactscan.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/04-control-event
  - aethrion/wave/w3
  - aethrion/effort/m
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-037` |
| Work package | [`WP-037` — G10 Temporal Schedules and Short ImpactScan Workflows](wp_037_g10_impactscan.md) |
| Companion | [test procedures](wp_037_g10_impactscan.tests.md) |
| Workstream | `04_CONTROL_EVENT` |
| Approval authority | **Assurance Lead / SRE** — the independent verifier |
| Accountable owner | Knowledge Monitoring Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-037` |

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

Each criterion names the test case in [`WP-037_g10_impactscan.tests.md`](wp_037_g10_impactscan.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every `MonitoringPolicy` has a schedule, an owner and a scope, and scans run
      as **short-lived closed executions** — no long-lived monitoring workflow
      exists.
- [ ] **A suppressed scheduled run raises an alert within the declared window.**
      `PR-20` — silent stoppage — is detected rather than discovered.
- [ ] All five trigger classes open an `ImpactCase`: source retraction, model
      change, data drift, policy change, incident.
- [ ] The impact query returns **direct and derived** claims. A claim three hops
      from the retracted source appears in the list.
- [ ] Every case carries a priority, an SLA and an owner, and an SLA breach
      escalates.
- [ ] Resolving by supersession leaves the prior claim reachable.
- [ ] A dismissed case reaches a **terminal state with a recorded reason** and does
      not reopen on the next scan.
- [ ] **The positive control fails the scan when removed.** A monitor that has
      never reported a signal is indistinguishable from a monitor that is not
      running — `scripts/monitor_sources.py` already holds this discipline and it
      must survive into the platform.
- [ ] `claim_impact_analysis` no longer reports *not implemented*.

## What this package cannot establish

> **Blind to sources with no DOI.** The Crossref sweep resolves by DOI, and the
> current registry holds 33 sources of which **18 have none**. Those sources are
> not monitored at all, and the measurement file records the split honestly. Any
> claim that G10 covers the literature base has to state that fraction, because a
> monitor covering 45% of sources reports clean for the same reason a monitor
> covering none would.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Monitoring Lead** is assigned accountable; an implementer is named; **Assurance Lead / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-008` — G0–G10 Gate and Assurance Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-015` — Event Envelope, Subject and Schema Taxonomy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-018` — Claim, Evidence, Review and Decision Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-031` — Temporal Platform, Namespaces and HA — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-032` — ProjectLifecycle Workflow Skeleton — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-04` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-31` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-36` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-02` failing its effectiveness test.
- [ ] `CTL-MOD-02` failing its effectiveness test.

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
