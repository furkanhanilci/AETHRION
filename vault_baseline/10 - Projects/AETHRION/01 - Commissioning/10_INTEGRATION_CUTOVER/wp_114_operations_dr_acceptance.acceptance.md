---
title: "WP-114 — Operations, DR and Restore Acceptance Package — Acceptance Criteria"
aliases:
  - "WP-114 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-114 — Operations, DR and Restore Acceptance Package — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-114` |
| Work package | [`WP-114` — Operations, DR and Restore Acceptance Package](wp_114_operations_dr_acceptance.md) |
| Companion | [test procedures](wp_114_operations_dr_acceptance.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Independent DR Witness / Internal Audit** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-114` |

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

Each criterion names the test case in [`WP-114_operations_dr_acceptance.tests.md`](wp_114_operations_dr_acceptance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **Two distinct drills** run — a component restore and a region/management-plane
      restore — and **each is run by someone other than the runbook author**. A drill
      run by its author tests the system; one run by anyone else tests the runbook,
      which is what gets used at 3am.
- [ ] Every restore passes the **integrity queries**. Services starting is **not**
      accepted as evidence.
- [ ] The audit **hash chain verifies across the restore boundary**.
- [ ] Derived projections rebuild byte-equivalently; **human Obsidian notes survive**
      the vault rebuild.
- [ ] **The Zotero full resync produces no duplicates and overwrites no human edit**,
      and the contrast case with dedup/rebind disabled demonstrates why the
      procedure includes it. A recovery that duplicates the library is worse than
      the outage.
- [ ] **RPO for workflow state is measured as 0** and RTO is measured against its
      target — both recorded as numbers, not assertions.
- [ ] **The human timeline is measured**: detection, on-call, incident command and
      decision, with the decision authority demonstrably reachable.
- [ ] **Every runbook gap found becomes a finding with an owner.** A drill that finds
      nothing has usually rehearsed a path someone already knew.

## What this package cannot establish

> **Two rehearsals is the go-live bar, not a guarantee.** They prove the restore
> works twice, under conditions someone planned, on a system in a known state. The
> real event happens under a condition nobody planned, and `PR-13` closes only on a
> control-effectiveness test with a re-evaluation date — which is why WP-129 repeats
> this quarterly rather than treating it as done.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **SRE Lead** is assigned accountable; an implementer is named; **Independent DR Witness / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-028` — NATS JetStream and Transactional Outbox Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-030` — Neo4j, pgvector and OpenSearch Derived Read Models — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-031` — Temporal Platform, Namespaces and HA — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-052` — Kubernetes Cluster and Node Pool Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-099` — WORM Audit Ledger and Independent Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-101` — Service Catalogue, SLOs and Alert/Runbook Binding — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-109` — Acceptance Scenario Registry and Harness — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Independent DR Witness / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-21` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-27` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-28` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
- [ ] `CTL-OPS-02` failing its effectiveness test.
- [ ] `CTL-OPS-03` failing its effectiveness test.

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
