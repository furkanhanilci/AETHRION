---
title: "WP-095 — Claim/Evidence Explorer and Provenance Graph — Acceptance Criteria"
aliases:
  - "WP-095 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-095 — Claim/Evidence Explorer and Provenance Graph — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-095` |
| Work package | [`WP-095` — Claim/Evidence Explorer and Provenance Graph](wp_095_claim_evidence_explorer.md) |
| Companion | [test procedures](wp_095_claim_evidence_explorer.tests.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Citation Auditor / Accessibility Reviewer** — the independent verifier |
| Accountable owner | Evidence Product Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-095` |

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

Each criterion names the test case in [`WP-095_claim_evidence_explorer.tests.md`](wp_095_claim_evidence_explorer.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Claim detail shows type, state, version, certainty and conditions, and version
      diffs show changes in assertion, evidence and state.
- [ ] **All four degraded locator states render distinctly.** An `ORPHANED` span
      rendered blank is indistinguishable from a claim with no evidence, and
      substituting nearby text for an `AMBIGUOUS` span is refused.
- [ ] **Contradictions render as prominently as support**, and mutually contradicting
      claims are returnable as a query rather than left for a reader to notice.
- [ ] **The assessment renders as seven separate dimensions**; rendering it as one
      bar or score is refused, and a blocked claim names the blocking dimension and
      what would clear it.
- [ ] The claim timeline shows runs, reviews, reproductions and decisions in order,
      each deep-linked.
- [ ] A cited source's trust card renders with **facts separated from judgements**.
- [ ] **A superseded claim says so at the top** and names its successor; a
      superseding claim names what it replaced.
- [ ] A retraction surfaces on the claim as an impact case with its state change.
- [ ] The citation audit view shows each material sentence with its verdict, its
      span and its rationale.

## What this package cannot establish

> **Seeing the evidence is not evaluating it.** This explorer makes a claim's
> support inspectable in one place; whether the support is adequate is what G6's
> reviewers, WP-080's audit and WP-085's reproduction decide. The most valuable
> thing it renders is the part a summary would omit — the contradictions, the
> degraded anchors, and the dimension that is blocking.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Evidence Product Lead** is assigned accountable; an implementer is named; **Citation Auditor / Accessibility Reviewer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-030` — Neo4j, pgvector and OpenSearch Derived Read Models — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-076` — Evidence Span Anchoring and Re-anchoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-077` — Claim State, Dependency and Assessment Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-078` — Structured Evidence Extraction Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-079` — SourceTrustCard and Study Quality Assessment — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-080` — Claim–Citation Entailment, Scope and Locator Audit — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-082` — Run Registry and MLflow Lineage Integration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-087` — Mechanical Verification Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-088` — Blind, Cross-Family and Adversarial Review — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-089` — DisagreementCase and Evidence-Weighted Arbitration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-090` — PublicationPackage, RO-Crate and Provenance Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-091` — Lab Cockpit Information Architecture and Application Shell — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Citation Auditor / Accessibility Reviewer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-04` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-21` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-30` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-31` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
