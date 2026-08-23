---
title: "WP-144 — Discovery Search Graph and Candidate Lifecycle — Acceptance Criteria"
aliases:
  - "WP-144 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-144_discovery_search_graph.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-144 — Discovery Search Graph and Candidate Lifecycle — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-144` |
| Work package | [`WP-144` — Discovery Search Graph and Candidate Lifecycle](wp_144_discovery_search_graph.md) |
| Companion | [test procedures](wp_144_discovery_search_graph.tests.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Reproducibility Engineer / Chief Architect** — the independent verifier |
| Accountable owner | Experiment Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-144` |

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

Each criterion names the test case in [`WP-144_discovery_search_graph.tests.md`](wp_144_discovery_search_graph.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A `PRIMARY_PARENT` cycle is rejected, and a `REFERENCE` edge cannot alter
      an ancestry.
- [ ] A `DEBUG` transition preserves its parent's mechanism identity, and an
      exhausted debug produces a `FailedApproach` classified `IMPLEMENTATION`.
- [ ] **No transition can set a hypothesis `REFUTED` from an implementation,
      data, infrastructure or policy failure.** Only a validly executed run under
      the frozen plan can support a `HYPOTHESIS` class.
- [ ] A `FUSE` node requires at least two inputs, and its inputs and their named
      inherited mechanisms survive the canonical graph, an export **and** a
      derived-graph rebuild.
- [ ] Every executed candidate resolves to an immutable artifact, a workspace
      commit and an official run. No node is the only copy of anything.
- [ ] A persisted campaign restores identically, and a deterministic slice
      replays to the same transitions.
- [ ] A synthetic multi-branch search containing draft, debug, improve and fusion
      rebuilds with complete lineage.

## What this package cannot establish

> **What this package cannot establish.** That the search finds anything. This
> package delivers a record a reviewer can read; whether the candidates in it are
> worth generating is WP-145's allocation problem and, ultimately, an empirical
> question no schema answers. It also cannot establish that a `DEBUG`
> classification was honest — an agent that relabels a scientific dead end as an
> implementation defect is a failure mode this structure makes *visible* to
> review rather than impossible.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Experiment Platform Lead** is assigned accountable; an implementer is named; **Reproducibility Engineer / Chief Architect** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-023` — Git, Worktree and Protected-Path Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-030` — Neo4j, pgvector and OpenSearch Derived Read Models — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-082` — Run Registry and MLflow Lineage Integration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-143` — Hypothesis and Principle Evolution and Proximity Graph — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Reproducibility Engineer / Chief Architect** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-58` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-64` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-01` failing its effectiveness test.
- [ ] `CTL-EPI-03` failing its effectiveness test.

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
