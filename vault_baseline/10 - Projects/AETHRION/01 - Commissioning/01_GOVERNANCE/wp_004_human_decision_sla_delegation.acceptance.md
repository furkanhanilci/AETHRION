---
title: "WP-004 — Human Decision, SLA, Delegation and Escalation Policy — Acceptance Criteria"
aliases:
  - "WP-004 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/01_GOVERNANCE/WP-004_human_decision_sla_delegation.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/g1
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-004 — Human Decision, SLA, Delegation and Escalation Policy — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-004` |
| Work package | [`WP-004` — Human Decision, SLA, Delegation and Escalation Policy](wp_004_human_decision_sla_delegation.md) |
| Companion | [test procedures](wp_004_human_decision_sla_delegation.tests.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Safety & Governance Owner** — the independent verifier |
| Accountable owner | Project Decision Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-004` |

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

Each criterion names the test case in [`WP-004_human_decision_sla_delegation.tests.md`](wp_004_human_decision_sla_delegation.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every decision type carries a materiality classification, an SLA, an
      escalation chain, an expiry, a delegation rule and an explicit fail-closed
      state — zero unclassified types.
- [ ] Every **material** decision type fails closed to *not approved*. No decision
      type expires into approval.
- [ ] G8, publication, retraction and cutover decisions are **non-delegable**, and
      an attempt to delegate each is rejected by a machine check, demonstrated once
      per type.
- [ ] A delegation used outside its scope and a delegation used after its duration
      are rejected **separately**, and the audit distinguishes the two failures.
- [ ] Changing the evidence behind an approved object invalidates or flags the
      standing approval; it never silently carries over.
- [ ] An expired or revoked approval is refused **at the point of use**, not merely
      displayed as stale.
- [ ] The queue emits all four rubber-stamp signals — decision-time distribution,
      evidence sections opened, G10 reversal rate, acceptance-despite-adversarial-
      rejection rate — each carrying a correlation identifier.
- [ ] At the human attention quota, requests **queue**. Nothing is auto-approved,
      nothing is dropped, and no express path exists.
- [ ] An independent reviewer proposed at least one addition to the non-delegable
      list, resolved with a recorded reason.

## What this package cannot establish

> **The signal to watch after go-live.** Median decision time falling while
> decision volume rises. That combination has one common cause and it is not
> improved efficiency.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Project Decision Owner** is assigned accountable; an implementer is named; **Safety & Governance Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-003` — Role Catalogue and RACI Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Safety & Governance Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-25` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-26` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-GOV-01` failing its effectiveness test.
- [ ] `CTL-GOV-03` failing its effectiveness test.

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
