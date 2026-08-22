# WP-026 — Content-Addressed Object Store and WORM — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-026` |
| Work package | [`WP-026` — Content-Addressed Object Store and WORM](WP-026_object_store_worm.md) |
| Companion | [test procedures](WP-026_object_store_worm.tests.md) |
| Workstream | `03_FOUNDATION` |
| Approval authority | **Archivist / Security** — the independent verifier |
| Accountable owner | Data Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-026` |

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

Each criterion names the test case in [`WP-026_object_store_worm.tests.md`](WP-026_object_store_worm.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Quarantine, canonical and publication areas are separate, with data-class
      separation enforced between them.
- [ ] Object keys are content addresses in the **single format WP-014 fixed**, and
      a multipart upload's verified hash equals the whole-object hash.
- [ ] Overwriting an existing key is **refused at the storage layer**, and so is
      deletion under lock — including with the highest available credential.
      Object lock is not a permission.
- [ ] Legal hold **overrides** retention: deletion after retention expiry is
      refused while a hold is in force.
- [ ] A canonical-plane identity cannot read a quarantined object.
- [ ] Promotion out of quarantine records a decision and mints a new canonical key.
- [ ] Every access is logged with an identity; objects are encrypted at rest.
- [ ] A replica read is byte-identical, and **the bit-rot scan detects an
      out-of-band corruption** rather than reporting clean.
- [ ] A restore reproduces a known digest set exactly.
- [ ] **The WP-000 interim migration is exercised**: an existing interim manifest
      is migrated into this store and verifies. Finding **C1**'s storage half moves
      from a temporary profile to the permanent one.

## What this package cannot establish

> **What acceptance of this package does not do.** It does not make any manifest
> *externally witnessed*. `airl-interim-v0.1`'s limitation list names three gaps —
> no transparency log, no keyless identity, no external timestamp authority — and
> this package closes only the store. The other two are WP-139 and the Sigstore
> policy in WP-027/WP-059. A manifest in an immutable store held by the same
> operator is tamper-evident, which is still not witnessed.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Data Platform Lead** is assigned accountable; an implementer is named; **Archivist / Security** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Archivist / Security** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-23` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
