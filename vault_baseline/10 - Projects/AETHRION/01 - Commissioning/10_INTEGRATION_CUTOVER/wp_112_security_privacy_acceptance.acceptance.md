---
title: "WP-112 — Security and Privacy Acceptance Package — Acceptance Criteria"
aliases:
  - "WP-112 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-112_security_privacy_acceptance.acceptance.md"
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

# WP-112 — Security and Privacy Acceptance Package — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-112` |
| Work package | [`WP-112` — Security and Privacy Acceptance Package](wp_112_security_privacy_acceptance.md) |
| Companion | [test procedures](wp_112_security_privacy_acceptance.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Independent Red Team / Privacy Reviewer** — the independent verifier |
| Accountable owner | Safety & Governance Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-112` |

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

Each criterion names the test case in [`WP-112_security_privacy_acceptance.tests.md`](wp_112_security_privacy_acceptance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **Every scenario declares its expected outcome — deny / contain / detect /
      respond — before it runs**, and an outcome weaker than expected is a finding.
      An attack that failed because the attacker erred is not evidence.
- [ ] Sandbox escape is **contained and detected** with a forensic snapshot taken
      **before** teardown.
- [ ] Exfiltration is **denied** to unlisted hosts and via DNS, and **detected** to
      an allowed destination — the path the categorical controls cannot refuse.
- [ ] Unsigned images, unapproved builders and D3 routing below ceiling are each
      denied.
- [ ] Policy rollback **preserves the decision log**; an expired exception is refused
      **at the point of use** with auto-revoke firing without human action.
- [ ] **A forged approval and a replayed approval are both refused and audited**, and
      signing without MFA is refused. A forged approval that succeeded would leave
      every downstream claim resting on an authorisation that never happened.
- [ ] **No secret lands in any trace store** — redaction at ingestion, verified by
      auditing the store.
- [ ] **The contamination canary fires** and the affected profile is ejected, and the
      check **fails when the canary is removed**. Contamination does not error; the
      metric simply improves.
- [ ] **Audit alteration, deletion and reordering all break the chain**, naming the
      position, and a tampered export fails standalone verification.
- [ ] Every expected incident opened, routed to an owner, with a **measured response
      time**, and its forensic artifacts are sufficient to investigate.
- [ ] **Every critical finding was corrected and retested**, and sign-off with an
      open critical is refused.

## What this package cannot establish

> **This suite tests the attacks in the threat-to-control map.** Its coverage is
> bounded by that map, and `AGENTS.md` §11 names the external benchmark that would
> test it adversarially from outside — **AgentDojo** — and records that it has not
> been run. A clean pass here means the controls hold against the attacks this
> laboratory imagined, which is a weaker claim than it will feel like at sign-off.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Safety & Governance Owner** is assigned accountable; an implementer is named; **Independent Red Team / Privacy Reviewer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-060` — Agentic Security Attack Suite and Red-Team Acceptance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-109` — Acceptance Scenario Registry and Harness — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Independent Red Team / Privacy Reviewer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-15` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-24` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-32` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-37` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
- [ ] `CTL-SEC-01..05` failing its effectiveness test.
- [ ] `CTL-OBS-02` failing its effectiveness test.

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
