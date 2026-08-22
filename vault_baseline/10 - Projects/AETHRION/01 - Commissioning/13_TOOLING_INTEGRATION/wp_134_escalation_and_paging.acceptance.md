---
title: "WP-134 — Escalation and Paging — Acceptance Criteria"
aliases:
  - "WP-134 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-134_escalation_and_paging.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/m
  - aethrion/gate/g0-g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-134 — Escalation and Paging — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-134` |
| Work package | [`WP-134` — Escalation and Paging](wp_134_escalation_and_paging.md) |
| Companion | [test procedures](wp_134_escalation_and_paging.tests.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Assurance Lead** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-134` |

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

Each criterion names the test case in [`WP-134_escalation_and_paging.tests.md`](wp_134_escalation_and_paging.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every chain step names an actor and an SLA, and the chain **terminates in an
      actor distinct from its origin** — or the gap is **declared** with a
      residual-risk owner and an expiry. A chain that loops back to its origin has
      not escalated.
- [ ] All four triggers escalate: SLA breach, budget hard stop, **integrity
      suspicion** and line-stop — with integrity suspicion escalating **faster than
      an availability alert**, because a suspected fabrication needs a human sooner
      than an outage.
- [ ] **An unacknowledged escalation promotes to the next step without human
      action**, and continues to the terminus.
- [ ] Quiet hours defer non-critical escalations, a **`CRITICAL` pierces
      immediately**, and **configuring quiet hours with no pierce rule is refused**.
- [ ] **Repeats of one event coalesce into a single escalation with a repeat count**,
      while still **promoting** on non-acknowledgement. Distinct events do not
      coalesce.
- [ ] Every escalation records its trigger, severity, path, acknowledgements and
      outcome.

## What this package cannot establish

> **A chain that cannot terminate outside the laboratory does not escalate.** For a
> solo operator every path leads back to the same person, and the correct output is
> a declaration rather than a chain that appears to have depth. ADR-001 supplies the
> form; `PR-21` names the condition — the programme assumes an organisation this
> laboratory does not have.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **SRE Lead** is assigned accountable; an implementer is named; **Assurance Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-131` — Notification Broker Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-132` — Channel Registry and Data-Class Ceiling — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-004` — Human Decision, SLA, Delegation and Escalation Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-26` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
- [ ] `CTL-GOV-03` failing its effectiveness test.
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
