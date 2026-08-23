---
title: "WP-077 — Claim State, Dependency and Assessment Engine — Acceptance Criteria"
aliases:
  - "WP-077 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-077 — Claim State, Dependency and Assessment Engine — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-077` |
| Work package | [`WP-077` — Claim State, Dependency and Assessment Engine](wp_077_claim_state_dependency.md) |
| Companion | [test procedures](wp_077_claim_state_dependency.tests.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Methodologist / Assurance Lead** — the independent verifier |
| Accountable owner | Evidence Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-077` |

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

Each criterion names the test case in [`WP-077_claim_state_dependency.tests.md`](wp_077_claim_state_dependency.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All three claim types exist with type-specific requirements, and every illegal
      lifecycle transition is refused.
- [ ] **The assessment reports seven dimensions separately with no weighted total.**
      A claim strong on six and failing reproduction is **not promoted** — a strong
      dimension cannot mask a fatal one.
- [ ] Every non-compensable blocker stops advancement: orphaned anchor, unresolved
      contradiction, failed confirmatory reproduction. Each demonstrated separately.
- [ ] **A failed clean-room reproduction marks the claim `CHALLENGED`** —
      `00_PROGRAM/01` invariant 4.
- [ ] `CONTESTED` and `CHALLENGED` are **different states**: a genuine evidence
      disagreement and a specific counter-result do not report identically.
- [ ] Dependency edges validate, and `contradicts` is queryable from both sides.
- [ ] **Challenging a claim queues its derived claims for reassessment rather than
      downgrading them.** Automatic downgrade is refused — whether a derivation
      survives is a judgement its author may legitimately defend.
- [ ] Every queued claim reaches a **terminal disposition** with an actor and a
      reason.
- [ ] An interpretive claim whose scope exceeds its evidence is blocked on the scope
      dimension.

## What this package cannot establish

> **Interpretive claims are where this package matters and where it is weakest.**
> Provenance, method and reproduction are checkable. *This result means X* is not,
> and the seven-dimension vector gives it the same structured appearance as an
> empirical claim. The mitigation is `scope-discipline` and G6's adversarial
> review; the honest statement is that the ledger records an interpretation's
> support, never its correctness.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Evidence Platform Lead** is assigned accountable; an implementer is named; **Methodologist / Assurance Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-018` — Claim, Evidence, Review and Decision Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-076` — Evidence Span Anchoring and Re-anchoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Methodologist / Assurance Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-19` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-20` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-70` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-78` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-01` failing its effectiveness test.
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
