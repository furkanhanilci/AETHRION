---
title: "WP-128 — Incident, Postmortem and Learning Closure — Acceptance Criteria"
aliases:
  - "WP-128 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-128_incident_learning.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g10
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-128 — Incident, Postmortem and Learning Closure — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-128` |
| Work package | [`WP-128` — Incident, Postmortem and Learning Closure](wp_128_incident_learning.md) |
| Companion | [test procedures](wp_128_incident_learning.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Safety / Assurance / Service Owner** — the independent verifier |
| Accountable owner | Incident Commander / SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-128` |

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

Each criterion names the test case in [`WP-128_incident_learning.tests.md`](wp_128_incident_learning.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The severity classification includes an **epistemic** class, and a wrong
      published claim is accepted as one rather than forced into another category.
      Most incident processes have no category for the failure this system most
      needs to handle.
- [ ] **Containment precedes analysis in every incident**, and attempting to analyse
      first is refused by the workflow. Credential revocation, workflow pause and
      publication stop all work during containment, and the pause loses no state.
- [ ] Forensic artifacts are sufficient to determine what happened.
- [ ] **The integrity queries run after containment**, and a corrupted projection is
      **distinguished from a corrupted ledger** — one rebuilds, the other does not,
      and they look similar at first.
- [ ] Root-cause analysis reaches a cause rather than a proximate trigger, and the
      postmortem is **blameless**, naming systems and decisions rather than people.
- [ ] **The decision timeline is reconstructed from audit and telemetry, not from
      memory.**
- [ ] **Every action binds to a work package, control, evaluation, runbook or
      `ImpactCase`.** Closing with an unbound action is refused, and so is closing
      with an open Critical action.
- [ ] A recurrence of a closed incident's cause **reopens governance review** — the
      action did not work.

## What this package cannot establish

> **A good postmortem does not prevent the next incident.** It produces a bound
> action, and the action prevents that specific recurrence. `00_PROGRAM/07`'s rule
> applies here as everywhere: the risk closes on a **control effectiveness test**
> with a re-evaluation date, which is WP-123's job — not on the postmortem being
> written.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Incident Commander / SRE Lead** is assigned accountable; an implementer is named; **Safety / Assurance / Service Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-037` — G10 Temporal Schedules and Short ImpactScan Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-060` — Agentic Security Attack Suite and Red-Team Acceptance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-099` — WORM Audit Ledger and Independent Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-101` — Service Catalogue, SLOs and Alert/Runbook Binding — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-116` — Resilience, Chaos and Failure-Injection Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-118` — Operational Readiness, On-Call and Runbook Simulation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-152` — Failure Taxonomy, Attribution and Resilience Controls — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Safety / Assurance / Service Owner** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-OPS-03` failing its effectiveness test.
- [ ] `CTL-MOD-02` failing its effectiveness test.
- [ ] `CTL-LIT-02` failing its effectiveness test.

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
