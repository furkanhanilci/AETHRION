---
title: "WP-139 — Evidence Timestamping and Independent Seal — Acceptance Criteria"
aliases:
  - "WP-139 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-139_evidence_timestamping.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/s
  - aethrion/gate/g2
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-139 — Evidence Timestamping and Independent Seal — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-139` |
| Work package | [`WP-139` — Evidence Timestamping and Independent Seal](wp_139_evidence_timestamping.md) |
| Companion | [test procedures](wp_139_evidence_timestamping.tests.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Research Integrity Officer** — the independent verifier |
| Accountable owner | Data Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-139` |

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

Each criterion names the test case in [`WP-139_evidence_timestamping.tests.md`](wp_139_evidence_timestamping.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **Both anchors are obtained** — OpenTimestamps and RFC 3161 — with their
      differing trust assumptions recorded. Stamping with only one requires a
      recorded reason, because their failure modes are disjoint: one needs no trusted
      party and is slow, the other is immediate and requires trusting a TSA.
- [ ] Stamps bind to the manifest digest and are stored in the object store; binding
      a stamp for a different digest is refused.
- [ ] **Verification succeeds with only the manifest and the stamps, and no access to
      this system.** An altered manifest fails, and backdating is impossible for OTS
      and refused on the TSA path.
- [ ] **Locking a G2 analysis plan stamps it automatically**, before any run — the
      single point where an external timestamp buys the most, because preregistration's
      whole claim is that the plan existed before the data.
- [ ] A confirmatory run against an unstamped locked plan is refused, or its claim is
      **marked as internally-timestamped only**.
- [ ] The verification runbook works for an outside reader.
- [ ] An unreachable calendar or TSA records the manifest as **unstamped, never as
      stamped**.
- [ ] **`airl-interim-v0.1`'s *external timestamp authority* limitation is removed
      from new manifests**, and retroactively stamped historical manifests **say that
      the stamp proves existence now, not then**.

## What this package cannot establish

> **This closes one of three interim limitations.** The profile lists three: no
> transparency log, no keyless identity, no external timestamp authority. This
> package removes the third. The first two remain — the signing key is still local
> and the signature is still not in a public log — so a manifest after this package
> proves **when it existed** to anyone, and **who signed it** only to someone who
> trusts the operator's key management.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Data Platform Lead** is assigned accountable; an implementer is named; **Research Integrity Officer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Research Integrity Officer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-23` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-40` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-03` failing its effectiveness test.
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
