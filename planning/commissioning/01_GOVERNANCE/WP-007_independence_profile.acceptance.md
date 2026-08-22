# WP-007 — IndependenceProfile and Separation-of-Duties Policy — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-007` |
| Work package | [`WP-007` — IndependenceProfile and Separation-of-Duties Policy](WP-007_independence_profile.md) |
| Companion | [test procedures](WP-007_independence_profile.tests.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Internal Audit / Safety Owner** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-007` |

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

Each criterion names the test case in [`WP-007_independence_profile.tests.md`](WP-007_independence_profile.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All seven dimensions — human, model family, context, credential,
      environment, data path, economic interest — have a defined value domain and
      a stated evidence source.
- [ ] Minimum required sets for R1, R2 and R3 are stated **per dimension**, with no
      entry reading "as much as practical".
- [ ] The non-compensable list is non-empty, and each entry produces a **hard
      refusal** rather than a lowered score.
- [ ] Every dimension is demonstrated to reject independently — seven rejection
      transcripts, each naming the dimension that fired.
- [ ] Economic interest rejects even when the other six dimensions are satisfied.
- [ ] **The profile is re-evaluated at gate time.** A reviewer who was valid at
      assignment and acquired context afterwards is refused at the gate.
- [ ] The frozen review packet contains **zero** producer-trace artifacts,
      demonstrated by a diff against the producer's workspace.
- [ ] An R3 assignment under a solo operator produces `BLOCKED` with the ADR-001
      declaration attached, naming the missing external verifier.
- [ ] An R2 assignment records which dimensions are **unmet**, not only which are
      met. A partial profile that lists only its strengths is not a declaration.
- [ ] An independent reviewer proposed at least one additional non-compensable
      dimension, resolved with a recorded reason.

## What this package cannot establish

> **The limit this package must publish about itself.** It proves structural
> separation, not uncorrelated error. Two independent reviewers may still fail
> together. Until error correlation is measured — **PR-16**, and an uncovered area
> in `00_PROGRAM/11` — every independence claim downstream inherits that
> assumption, and this package's own documentation must say so.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Assurance Lead** is assigned accountable; an implementer is named; **Internal Audit / Safety Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-003` — Role Catalogue and RACI Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit / Safety Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-38` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
