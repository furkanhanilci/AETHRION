---
title: "WP-006 — ExecutionProfile and Route Policy — Acceptance Criteria"
aliases:
  - "WP-006 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/01_GOVERNANCE/WP-006_execution_profile.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/g1
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-006 — ExecutionProfile and Route Policy — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-006` |
| Work package | [`WP-006` — ExecutionProfile and Route Policy](wp_006_execution_profile.md) |
| Companion | [test procedures](wp_006_execution_profile.tests.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Safety Owner / SRE** — the independent verifier |
| Accountable owner | Platform Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-006` |

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

Each criterion names the test case in [`WP-006_execution_profile.tests.md`](wp_006_execution_profile.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All four rubrics — `DataClass` D0–D4, `CodeTrust` C0–C3, `ToolEffect` T0–T5,
      network/credential scope — have a written anchor for every level.
- [ ] Every combination in the tested matrix produces exactly one
      `ExecutionProfile`; no combination is undefined.
- [ ] **Axis independence is demonstrated**: holding data class constant and
      raising `CodeTrust` tightens the profile.
- [ ] The dominance rule is demonstrated once per axis — maximum on one axis with
      all others minimum still produces the strict profile.
- [ ] An unclassified task receives the **most restrictive** tier and is flagged.
- [ ] Untrusted content instructing a higher `ToolEffect` does **not** change the
      profile, and the attempt is audited. This is the ADR-003 boundary in
      executable form.
- [ ] Enforcement is demonstrated at **all four** points — model router, tool
      broker, Kueue placement, sandbox attestation — each refusing independently.
- [ ] Egress outside the declared scope is **denied by default** and raises an
      alert rather than a warning.
- [ ] Relaxing a profile without approval, and with an expired approval, are
      rejected as distinguishable failures.
- [ ] No two axes were found to move together in every tested case; any that were
      are recorded as a design finding with a disposition.

## What this package cannot establish

> **Non-waivable.** `00_PROGRAM/07` places identity, data-routing and sandbox
> failures outside the waiver mechanism. A profile that computes correctly but
> enforces at three of four points does not pass at 75%; it does not pass.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Platform Security Lead** is assigned accountable; an implementer is named; **Safety Owner / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-002` — Scope, NFRs and Requirement Traceability — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Safety Owner / SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-15` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-02` failing its effectiveness test.
- [ ] `CTL-SEC-04` failing its effectiveness test.

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
