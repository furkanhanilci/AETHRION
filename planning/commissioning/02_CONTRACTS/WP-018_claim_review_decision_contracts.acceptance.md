# WP-018 — Claim, Evidence, Review and Decision Schemas — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-018` |
| Work package | [`WP-018` — Claim, Evidence, Review and Decision Schemas](WP-018_claim_review_decision_contracts.md) |
| Companion | [test procedures](WP-018_claim_review_decision_contracts.tests.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Assurance Lead / Methodologist** — the independent verifier |
| Accountable owner | Evidence Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-018` |

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

Each criterion names the test case in [`WP-018_claim_review_decision_contracts.tests.md`](WP-018_claim_review_decision_contracts.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] An `EvidenceSpan` requires **all three** of content hash, structural locator
      and text fingerprint; a span missing any one is rejected.
- [ ] Under re-extraction the hash breaks while locator and fingerprint resolve,
      and the system reports *the source changed* rather than *the evidence is
      gone*.
- [ ] Under re-typesetting the fingerprint alone re-anchors the span, and the
      re-anchoring is recorded with its provenance.
- [ ] A claim with no evidence span cannot reach a publishable state.
- [ ] A claim a decision depends on cannot be edited in place; a new version is
      required and the dependency still names the version it was taken against.
- [ ] `supports`, `contradicts` and `derived-from` all resolve in both directions.
- [ ] **A contradiction is returned by a query**, not left for a reader to notice.
- [ ] `Finding` has no state meaning "open indefinitely": every non-terminal state
      requires an owner and an expiry.
- [ ] Two conflicting verdicts open a `DisagreementCase` automatically, and it
      cannot be closed without an arbiter decision.
- [ ] A confidence value with no calibration basis is stored **and displayed** as
      `UNCALIBRATED`. It cannot be rendered as a calibrated number anywhere.
- [ ] Superseding a published claim leaves the prior version reachable and rewrites
      no downstream record.

## What this package cannot establish

> **What this package must publish about its own limits.** It defines where a
> confidence number lives and forbids it from lying about its own basis. It does
> **not** make any number calibrated — that requires the lab's measured error
> rates, which is `PR-17`/`PR-18` and an uncovered area in `00_PROGRAM/11`.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Evidence Platform Lead** is assigned accountable; an implementer is named; **Assurance Lead / Methodologist** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-012` — Canonical Ownership and Field-Level Authority Matrix — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Methodologist** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-30` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-04` failing its effectiveness test.

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
