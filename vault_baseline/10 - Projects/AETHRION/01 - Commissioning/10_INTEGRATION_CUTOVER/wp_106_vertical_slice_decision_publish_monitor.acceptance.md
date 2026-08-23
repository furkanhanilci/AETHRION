---
title: "WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor — Acceptance Criteria"
aliases:
  - "WP-106 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-106` |
| Work package | [`WP-106` — Vertical Slice 5 — Human Decision, Publish and Monitor](wp_106_vertical_slice_decision_publish_monitor.md) |
| Companion | [test procedures](wp_106_vertical_slice_decision_publish_monitor.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Citation Auditor / Safety / Archivist** — the independent verifier |
| Accountable owner | Project Decision Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-106` |

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

Each criterion names the test case in [`WP-106_vertical_slice_decision_publish_monitor.tests.md`](wp_106_vertical_slice_decision_publish_monitor.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **The G8 decision is a real decision**: evidence delta shown, dissent and
      residual risk visible, rationale required, MFA at signing, non-delegable
      enforced, and the update idempotent.
- [ ] Publication refuses on a missing reproduction certificate and on an open
      citation-audit finding.
- [ ] **All three release checks refuse independently** — licence, privacy, and
      **security release** naming the boundary. The third is the one a research
      laboratory is least practised at.
- [ ] The RO-Crate package is readable by a tool that knows nothing of this system,
      and its signature, archive and release event all verify.
- [ ] **All three G10 triggers reach the published claim** — retraction, correction
      and model drift — and a claim **three derivation hops away appears in the
      impact list**.
- [ ] The impacted claim moves to `CHALLENGED` with an owner and an SLA.
- [ ] **A superseding package leaves the prior version reachable**, and withdrawing
      an original without supersession is refused.
- [ ] A spurious impact case reaches a terminal disposition and does not reopen.
- [ ] **The whole slice verifies from the standalone verifier with no access to the
      running system.**
- [ ] **One project has produced eleven `GateRecord`s across G0–G10.**

## What this package cannot establish

> **One traverse is not a system.** Completing this slice removes the qualifier
> `docs/STATUS.md` has printed since the beginning — that no research question has
> travelled the lifecycle — and replaces it with a narrower true statement: **one
> synthetic project has.** The scenarios in `12_ACCEPTANCE_SCENARIOS` exist because
> a single successful traverse says nothing about the fifty-one situations the
> system is supposed to survive, and `PR-21` still stands: the programme assumes an
> organisation this laboratory does not have.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Project Decision Owner** is assigned accountable; an implementer is named; **Citation Auditor / Safety / Archivist** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-037` — G10 Temporal Schedules and Short ImpactScan Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-074` — Obsidian Projection, Link Integrity and Knowledge Write-Back — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-077` — Claim State, Dependency and Assessment Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-080` — Claim–Citation Entailment, Scope and Locator Audit — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-089` — DisagreementCase and Evidence-Weighted Arbitration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-090` — PublicationPackage, RO-Crate and Provenance Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-093` — Human Decision Queue and Evidence-Delta UI — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-095` — Claim/Evidence Explorer and Provenance Graph — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-099` — WORM Audit Ledger and Independent Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-105` — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Citation Auditor / Safety / Archivist** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-04` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-25` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-30` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-31` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-36` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-40` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-52` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-53` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-01` failing its effectiveness test.
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
