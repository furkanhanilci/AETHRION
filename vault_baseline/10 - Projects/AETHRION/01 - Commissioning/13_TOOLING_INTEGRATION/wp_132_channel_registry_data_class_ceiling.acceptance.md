---
title: "WP-132 — Channel Registry and Data-Class Ceiling — Acceptance Criteria"
aliases:
  - "WP-132 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-132_channel_registry_data_class_ceiling.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-132 — Channel Registry and Data-Class Ceiling — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-132` |
| Work package | [`WP-132` — Channel Registry and Data-Class Ceiling](wp_132_channel_registry_data_class_ceiling.md) |
| Companion | [test procedures](wp_132_channel_registry_data_class_ceiling.tests.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Platform Security Lead** — the independent verifier |
| Accountable owner | Safety & Governance Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-132` |

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

Each criterion names the test case in [`WP-132_channel_registry_data_class_ceiling.tests.md`](wp_132_channel_registry_data_class_ceiling.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every channel registers a **ceiling, an egress host and an identity**; a
      channel with no ceiling, or whose host is not on the egress allowlist, is
      refused.
- [ ] **The ceiling is enforced in code as a pre-send gate**: content above it is
      refused before send, naming the class and the ceiling. Configuring it as a
      warning is refused.
- [ ] **Free-text sending is disabled.** Only registered templates send, each
      declaring its fields and **each field's data class**; an undeclared field is
      refused.
- [ ] **DLP scanning is mandatory before send** and cannot be bypassed — it blocks
      secrets and personal data that a field's declared class did not predict.
- [ ] The self-hosted channel carries a **higher ceiling** than the third-party one,
      and raising a third-party ceiling to match requires a recorded decision with an
      owner.
- [ ] Every ceiling change records actor, reason and prior value.

## What this package cannot establish

> **The scanner is the second layer, not the boundary.** ADR-003 is explicit that a
> detector is defence in depth and never the boundary itself. Here the boundary is
> the **ceiling plus the template**: known fields with known classes, checked before
> send. If the design ever comes to rely on DLP catching what the template allowed,
> the control has inverted and the free-text ban is the thing holding it together.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Safety & Governance Owner** is assigned accountable; an implementer is named; **Platform Security Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-131` — Notification Broker Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Platform Security Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-41` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-03` failing its effectiveness test.

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
