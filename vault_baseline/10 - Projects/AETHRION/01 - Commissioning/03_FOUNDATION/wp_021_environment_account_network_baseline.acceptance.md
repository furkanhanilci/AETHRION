---
title: "WP-021 — Development, Staging and Production Environment Baseline — Acceptance Criteria"
aliases:
  - "WP-021 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/03_FOUNDATION/WP-021_environment_account_network_baseline.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-021 — Development, Staging and Production Environment Baseline — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-021` |
| Work package | [`WP-021` — Development, Staging and Production Environment Baseline](wp_021_environment_account_network_baseline.md) |
| Companion | [test procedures](wp_021_environment_account_network_baseline.tests.md) |
| Workstream | `03_FOUNDATION` |
| Approval authority | **Security Architect / SRE** — the independent verifier |
| Accountable owner | Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-021` |

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

Each criterion names the test case in [`WP-021_environment_account_network_baseline.tests.md`](wp_021_environment_account_network_baseline.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Three environments exist as **separate accounts** with no standing trust
      from a lower environment to a higher one.
- [ ] A dev-scoped role attempting a production action is **denied**, and the
      denial is logged in the production account rather than only in dev.
- [ ] Every administrative action requires MFA; an attempt without it is denied.
- [ ] Break-glass grants access that is **time-limited**, opens an incident
      automatically, and expires **without human revocation** — all three
      demonstrated.
- [ ] Promotion runs in one direction only. Promoting from production to a lower
      environment is refused.
- [ ] Copying production data into a lower environment is refused, and the refusal
      names the data class.
- [ ] Every store is encrypted at rest with a key that resolves to the declared
      key model.
- [ ] A D3 artifact lands in the declared residency region, verified by reading
      back its placement.
- [ ] Applying the baseline IaC twice is a **no-op** on the second run.
- [ ] An independent reviewer searched the plan for standing credentials; each one
      found is a finding with a named owner.

## What this package cannot establish

> **Not established here.** That the separation survives operational pressure. An
> account boundary is enforced by the cloud provider and a promotion rule is
> enforced by a pipeline; both can be bypassed by an operator with break-glass.
> What this package can prove is that the bypass is **designed, time-limited and
> loud**. Whether it stays that way is `PR-13`'s territory and is measured by how
> often break-glass is actually used, which belongs in WP-101's SLO set.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Platform Lead** is assigned accountable; an implementer is named; **Security Architect / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-001` — Commissioning Charter and Programme Authority — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-010` — Architecture Decision and Rejected-Alternatives Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security Architect / SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-27` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-SEC-02` failing its effectiveness test.

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
