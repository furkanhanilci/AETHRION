---
title: "WP-084 — Clean-Room Reproduction Environment — Acceptance Criteria"
aliases:
  - "WP-084 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g7
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-084 — Clean-Room Reproduction Environment — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-084` |
| Work package | [`WP-084` — Clean-Room Reproduction Environment](wp_084_clean_room_environment.md) |
| Companion | [test procedures](wp_084_clean_room_environment.tests.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Security / Independent SRE** — the independent verifier |
| Accountable owner | Reproducibility Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-084` |

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

Each criterion names the test case in [`WP-084_clean_room_environment.tests.md`](wp_084_clean_room_environment.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The clean room has its own queue, nodes, namespace and workload identity.
- [ ] **The producer's workspace, credentials, package cache, model cache and
      container layers are each separately denied** — five denial records. A cache
      is not one thing, and any one of them can make an unreproducible run appear
      reproducible.
- [ ] **A deliberately missing input causes a named failure**, never a silent
      success by finding it elsewhere. This is the test that proves the isolation.
- [ ] Every fetched artifact is hash-verified before use; a mismatch is refused.
- [ ] **Network access is denied by default**; a manifest-declared fetch goes
      through a pinned path and is recorded.
- [ ] The environment manifest is **captured from the running environment**, not
      written from intention.
- [ ] The declared hardware tolerance applies on different architecture, and the
      report states which tolerance was used.
- [ ] Outputs are hashed and land in quarantine before teardown.
- [ ] **A failed reproduction is snapshotted before destruction**, and the
      environment is destroyed on success, failure and timeout alike.

## What this package cannot establish

> **A clean room proves the artifacts are sufficient, not that the result is
> right.** A reproduction that succeeds shows the frozen manifest contains
> everything needed to produce the same output. If the method was wrong, it
> reproduces the wrong answer exactly — which is why G7 sits after G6 rather than
> instead of it.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Reproducibility Lead** is assigned accountable; an implementer is named; **Security / Independent SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-027` — Git, OCI Registry and Build Provenance Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-052` — Kubernetes Cluster and Node Pool Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-053` — Kueue Queue, Quota and Priority Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-054` — gVisor Sandbox and Execution Cell Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-055` — SPIFFE/SPIRE Workload Identity and Vault — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-059` — Supply-Chain Admission, Sigstore and SLSA Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-082` — Run Registry and MLflow Lineage Integration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security / Independent SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-19` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-20` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-03` failing its effectiveness test.
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
