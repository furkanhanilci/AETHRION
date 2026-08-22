---
title: "WP-047 — Role and Skill Registries, and the Task Compiler — Acceptance Criteria"
aliases:
  - "WP-047 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g1-g7
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-047 — Role and Skill Registries, and the Task Compiler — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-047` |
| Work package | [`WP-047` — Role and Skill Registries, and the Task Compiler](wp_047_role_bundle_registry.md) |
| Companion | [test procedures](wp_047_role_bundle_registry.tests.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Governance / Eval Office** — the independent verifier |
| Accountable owner | Agent Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-047` |

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

Each criterion names the test case in [`WP-047_role_bundle_registry.tests.md`](wp_047_role_bundle_registry.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A `RoleBundle` compiles deterministically to an **identical hash** from the
      same `RoleContract`, and an unsigned bundle is refused.
- [ ] A tool outside the bundle's allowed set is refused **at the broker**, naming
      the bundle.
- [ ] The context budget is never silently exceeded, and a reviewer bundle's
      context contains **no producer trace**.
- [ ] **`validate_skills.py` is an admission gate**: a non-conforming skill does
      not load. Conformance stops being a report.
- [ ] Trigger resolution records `skill_selection_reason`; competing skills resolve
      deterministically **or refuse**; an uncovered task is detected rather than run
      bare.
- [ ] `airl.requires_skills` resolves with the closure recorded, and an
      irreconcilable version conflict is **refused** rather than resolved by an
      arbitrary winner.
- [ ] **`skill_bundle_hash` reaches the evidence chain**, two bundles produce two
      hashes, and comparing results across differing hashes is refused or flagged
      non-comparable. A run records the discipline it was produced under.
- [ ] An agent cannot choose its own skill family; the family follows `work_domain`.
- [ ] Moving the pinned upstream commit **flags every derived skill**, and the
      eleven vendored skills are byte-identical to their pinned commit or the
      difference is a finding.
- [ ] Deprecating a bundle identifies live consumers before the cutoff, and the
      cutoff refuses rather than warns.

## What this package cannot establish

> **Conformance is not behaviour.** This package makes skills loadable, versioned,
> resolvable and hashable into the evidence chain. It does **not** show that any
> of them changes what an agent does — that is WP-043's RED/GREEN baseline, and
> until it runs, `docs/STATUS.md` will keep printing *none has a behaviour
> baseline* about all 52. A registry of skills that do nothing is a registry.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Agent Platform Lead** is assigned accountable; an implementer is named; **Governance / Eval Office** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-003` — Role Catalogue and RACI Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-042` — Capability Registry and Profile Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-045` — Policy Router and Minimum-Sufficient Model Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-046` — LangGraph Bounded Cognition Runtime — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Governance / Eval Office** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-GOV-02` failing its effectiveness test.
- [ ] `CTL-MOD-01` failing its effectiveness test.

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
