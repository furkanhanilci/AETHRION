---
title: "WP-027 — Git, OCI Registry and Build Provenance Foundation — Acceptance Criteria"
aliases:
  - "WP-027 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/03_FOUNDATION/WP-027_git_oci_supply_chain.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/m
  - aethrion/gate/g5
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-027 — Git, OCI Registry and Build Provenance Foundation — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-027` |
| Work package | [`WP-027` — Git, OCI Registry and Build Provenance Foundation](wp_027_git_oci_supply_chain.md) |
| Companion | [test procedures](wp_027_git_oci_supply_chain.tests.md) |
| Workstream | `03_FOUNDATION` |
| Approval authority | **Security Reviewer / SRE** — the independent verifier |
| Accountable owner | Supply Chain Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-027` |

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

Each criterion names the test case in [`WP-027_git_oci_supply_chain.tests.md`](wp_027_git_oci_supply_chain.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every deployment references an image by **digest**. Deploying by tag is
      refused, and tags cannot be repointed.
- [ ] Reproducibility is either **demonstrated** — the same commit built twice on
      two machines yielding identical digests — or **declared not achieved** with a
      written list of what varies. An undemonstrated claim fails.
- [ ] Provenance names the source commit, the builder and the inputs, and
      **verification fails** on an altered image.
- [ ] A signature from an unauthorised identity is refused.
- [ ] The SBOM lists every installed component, and **vulnerability status is
      stored separately** so a query returns current status rather than build-time
      status.
- [ ] Promoting an image with an open critical advisory is refused.
- [ ] Promotion carries **the same digest** from dev to production. Rebuilding
      during promotion is refused.
- [ ] Sigstore and SWHID are used as adopted components with their
      `authority_boundary` recorded; no bespoke signing scheme exists alongside.

## What this package cannot establish

> **The limit worth stating in the deliverable itself.** A verified signature says
> the artifact came from the declared builder. It says nothing about whether the
> source was correct, and nothing about whether the builder was compromised. Supply
> chain integrity narrows the question to *do you trust this identity* — it does
> not answer it. WP-059's policy set and WP-060's red team are where that gets
> tested.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Supply Chain Security Lead** is assigned accountable; an implementer is named; **Security Reviewer / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-022` — Repository Topology and Code Ownership — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-024` — CI Foundation and Deterministic Quality Gates — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security Reviewer / SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-17` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-SEC-05` failing its effectiveness test.
- [ ] `CTL-SUP-01` failing its effectiveness test.

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
