---
title: "WP-081 — Protocol, Analysis, Baseline and Falsification Registry — Acceptance Criteria"
aliases:
  - "WP-081 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g2
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-081 — Protocol, Analysis, Baseline and Falsification Registry — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-081` |
| Work package | [`WP-081` — Protocol, Analysis, Baseline and Falsification Registry](wp_081_protocol_baseline_registry.md) |
| Companion | [test procedures](wp_081_protocol_baseline_registry.tests.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Statistician / Falsification Lead** — the independent verifier |
| Accountable owner | Method Office Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-081` |

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

Each criterion names the test case in [`WP-081_protocol_baseline_registry.tests.md`](wp_081_protocol_baseline_registry.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All four artifacts carry owner, hash, gate reference and lifecycle, and an
      in-place edit of a frozen one is refused.
- [ ] **Counter-test, leakage assessment, null and baseline are mandatory schema
      fields.** A submission missing any is refused — `00_PROGRAM/01`'s G4 blocker
      is enforced by the schema, not by a reviewer who can be persuaded.
- [ ] **A stop rule with no observable and threshold is refused.** "Stop when the
      results are clear" is not a stop rule.
- [ ] An amendment **before** any run is accepted and versioned. An amendment
      **after** a run exists is **refused as a correction** and permitted only as a
      new, declared exploratory study.
- [ ] **The post-hoc change detector flags a backdated amendment** by comparing
      amendment time to first run time, and **the detector suite fails when the
      seeded case is removed**.
- [ ] The analysis plan freezes **separately** from the protocol, with its own
      digest and gate record, and G4 refuses without it.
- [ ] A run names the **frozen digest**, not the artifact identifier alone, and a
      confirmatory claim resolves to its analysis plan in one query.
- [ ] Superseding a protocol leaves prior versions resolvable and runs against them
      correctly referenced.

## What this package cannot establish

> **A frozen protocol prevents one failure mode, not all of them.** It stops method
> being adjusted after seeing results. It does not stop a weak design being frozen
> early, and freezing makes a weak design harder to fix rather than easier —
> which is why G6's adversarial review and `ACC-08`'s strong counter-test sit
> downstream, and why the reviewer at G2 matters more than the registry.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Method Office Lead** is assigned accountable; an implementer is named; **Statistician / Falsification Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-008` — G0–G10 Gate and Assurance Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-035` — G2 Protocol, G3 Literature and G4 Baseline Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Statistician / Falsification Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-39` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-56` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-103` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-104` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-02` failing its effectiveness test.
- [ ] `CTL-DAT-01` failing its effectiveness test.

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
