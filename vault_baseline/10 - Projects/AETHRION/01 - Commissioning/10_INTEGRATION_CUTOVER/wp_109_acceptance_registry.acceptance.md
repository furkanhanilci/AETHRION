---
title: "WP-109 — Forty Acceptance Scenario Registry and Harness — Acceptance Criteria"
aliases:
  - "WP-109 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.acceptance.md"
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

# WP-109 — Forty Acceptance Scenario Registry and Harness — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-109` |
| Work package | [`WP-109` — Forty Acceptance Scenario Registry and Harness](wp_109_acceptance_registry.md) |
| Companion | [test procedures](wp_109_acceptance_registry.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board** — the independent verifier |
| Accountable owner | Platform Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-109` |

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

Each criterion names the test case in [`WP-109_acceptance_registry.tests.md`](wp_109_acceptance_registry.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **All 51 scenarios are in the registry**, not the 40 the purpose sentence
      names. ACC-41–46 and ACC-47–51 are included, and the discrepancy is recorded
      as a correction.
- [ ] Every entry is machine-readable with fixtures, expected events, invariants,
      evidence, owner, severity and cleanup; a missing owner or severity is refused.
- [ ] **The phase audit reports that all 51 are `PRE_GO_LIVE` and that no
      `DAY2_CONTINUOUS` scenario exists** — so the go-live condition requiring them
      to be armed is currently vacuous. This is raised as a finding, not resolved
      silently.
- [ ] Fixtures are deterministic and isolated; a second scenario sees nothing from
      the first.
- [ ] Canonical, event, audit and policy assertions all evaluate, including
      **asserted absence** of an event.
- [ ] Results are signed with **every assertion's observed value captured**, not
      summarised.
- [ ] **A manual step with no witness record is not counted as a pass**, and the
      witness record names identity, observation and timestamp.
- [ ] **SKIP is refused on a Critical scenario**; a permitted skip is recorded and
      **reported separately from passes**.
- [ ] **A scenario that passes only on retry produces a finding**, so retries cannot
      become a way to pass.
- [ ] A failed cleanup **blocks the next scenario** rather than letting it run dirty.

## What this package cannot establish

> **A runnable scenario is not a passing one.** This package makes 51 scenarios
> executable and produces signed evidence for each. It does not run them — that is
> WP-110 through WP-114 — and `docs/STATUS.md` records the current state plainly:
> **none of the 51 has ever been run.** Making them runnable is the precondition for
> discovering how many actually pass.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Platform Assurance Lead** is assigned accountable; an implementer is named; **Commissioning Board** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-002` — Scope, NFRs and Requirement Traceability — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-009` — Control Catalogue, Exceptions and Non-Waivable Blockers — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-024` — CI Foundation and Deterministic Quality Gates — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-040` — Workflow Replay, Versioning and Failure Test Suite — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-060` — Agentic Security Attack Suite and Red-Team Acceptance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-090` — PublicationPackage, RO-Crate and Provenance Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-099` — WORM Audit Ledger and Independent Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-102` — Vertical Slice 1 — Intake through Protocol Freeze — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-103` — Vertical Slice 2 — Two-Way Literature and Set Freeze — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-104` — Vertical Slice 3 — Baseline through Run to Claim/Evidence — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-105` — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-106` — Vertical Slice 5 — Human Decision, Publish and Monitor — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-107` — Engineering Vertical Slice — Spec, Worktree, Signed Release — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-108` — Retraction, Drift and Supersession Vertical Slice — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Commissioning Board** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-OPS-02` failing its effectiveness test.
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
