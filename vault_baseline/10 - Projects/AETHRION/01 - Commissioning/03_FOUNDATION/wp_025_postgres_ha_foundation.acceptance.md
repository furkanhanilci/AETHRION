---
title: "WP-025 — PostgreSQL HA and Registry Data Foundation — Acceptance Criteria"
aliases:
  - "WP-025 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/03_FOUNDATION/WP-025_postgres_ha_foundation.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-025 — PostgreSQL HA and Registry Data Foundation — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-025` |
| Work package | [`WP-025` — PostgreSQL HA and Registry Data Foundation](wp_025_postgres_ha_foundation.md) |
| Companion | [test procedures](wp_025_postgres_ha_foundation.tests.md) |
| Workstream | `03_FOUNDATION` |
| Approval authority | **SRE / Security** — the independent verifier |
| Accountable owner | Database Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-025` |

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

Each criterion names the test case in [`WP-025_postgres_ha_foundation.tests.md`](wp_025_postgres_ha_foundation.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Replicas occupy distinct failure domains; a plaintext connection is refused;
      storage is encrypted with a key that resolves to the declared model.
- [ ] Every database role is **denied** at least one action outside its grant.
- [ ] Static-password connections are refused in favour of workload identity.
- [ ] A migration applies **and rolls back**, with the schema returning to its
      prior state. A rollback that has never been exercised is not a rollback.
- [ ] A destructive migration in one stage is refused; two stages are required.
- [ ] A migration against another service's owned table is refused.
- [ ] **A point-in-time restore into a clean environment passes every defined
      integrity query** — row counts per canonical table, referential closure
      across the correlation chain, and the digest of a known artifact record.
      The service starting is not the test.
- [ ] Measured data loss under primary failure is within the **declared RPO**, and
      restore wall-clock is within the **declared RTO**, both recorded as numbers.
- [ ] Failover promotes without split brain.
- [ ] Pool exhaustion queues or refuses cleanly; the database is never driven to
      its own connection limit. The V0 leak (finding **M8**) is not carried across.
- [ ] A slow query appears in telemetry carrying its correlation identifier.

## What this package cannot establish

> **One rehearsal is not two.** `00_PROGRAM/10`'s go-live entry condition requires
> **two independent restore rehearsals**. This package proves the mechanism works
> once, under conditions its own author arranged. The second rehearsal, run by
> someone else against an unannounced point in time, is WP-118's, and it is the
> one that tests the runbook rather than the database.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Database Platform Lead** is assigned accountable; an implementer is named; **SRE / Security** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **SRE / Security** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-27` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-03` failing its effectiveness test.
- [ ] `CTL-SEC-03` failing its effectiveness test.

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
