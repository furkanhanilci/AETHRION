---
title: "WP-012 — Canonical Ownership and Field-Level Authority Matrix — Acceptance Criteria"
aliases:
  - "WP-012 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/02_CONTRACTS/WP-012_canonical_field_authority.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-012 — Canonical Ownership and Field-Level Authority Matrix — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-012` |
| Work package | [`WP-012` — Canonical Ownership and Field-Level Authority Matrix](wp_012_canonical_field_authority.md) |
| Companion | [test procedures](wp_012_canonical_field_authority.tests.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Internal Audit / Knowledge Lead** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-012` |

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

Each criterion names the test case in [`WP-012_canonical_field_authority.tests.md`](wp_012_canonical_field_authority.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every bounded context names **exactly one** canonical record.
- [ ] Authority is assigned **per field**, not per record, and at least one record
      is demonstrated to carry two different field authorities.
- [ ] Every field present on two surfaces has both a sync direction and a conflict
      rule. A direction without a rule fails.
- [ ] An agent write to a human-authority field is **rejected**, and the rejection
      names the field and its authority.
- [ ] A human note inside the generated Obsidian area survives projection —
      manifest-owned deletion holds.
- [ ] A simultaneous edit on both surfaces produces a **conflict record**; the
      losing value is preserved, never overwritten.
- [ ] Deleting a source upstream produces the assigned reconciliation outcome. The
      current behaviour — the record persists as current — is finding **H2** and
      does not pass.
- [ ] **The rebuild test passes**: every derived graph and index is deleted and
      rebuilt byte-equivalently from canonical records. Anything that cannot be
      rebuilt is reclassified as canonical and the matrix is corrected.
- [ ] The reconciliation job **reports** divergence with an owner rather than
      silently repairing it.
- [ ] An independent reviewer searched for two-surface fields missing from the
      matrix; each found is recorded with a disposition.

## What this package cannot establish

> **The test that decides whether this package is real.** Step 8. A matrix
> everyone agrees with and nobody has falsified is a diagram. The rebuild is what
> turns it into a claim about the system.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Chief Architect** is assigned accountable; an implementer is named; **Internal Audit / Knowledge Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-010` — Architecture Decision and Rejected-Alternatives Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit / Knowledge Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-03` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-21` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-22` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-01` failing its effectiveness test.
- [ ] `CTL-OPS-01` failing its effectiveness test.

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
