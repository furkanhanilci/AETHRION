# WP-154 — Engineering Discipline and Specification Conformance — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-154` |
| Work package | [`WP-154` — Engineering Discipline and Specification Conformance](WP-154_engineering_discipline_and_conformance.md) |
| Companion | [test procedures](WP-154_engineering_discipline_and_conformance.tests.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Engineering Productivity Lead / Assurance Lead** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-154` |

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

Each criterion names the test case in [`WP-154_engineering_discipline_and_conformance.tests.md`](WP-154_engineering_discipline_and_conformance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A coding-science task compiles both skill families, and neither substitutes
      for the other in any of the four non-synonym pairs.
- [ ] An artifact that has not closed the engineering loop cannot produce
      scientific evidence.
- [ ] **All seven planted drifts are detected**, a faithful implementation
      **passes**, and a pure refactor is `ENGINEERING_ONLY`.
- [ ] A bounded deviation is `SCIENTIFIC_MINOR` and travels with the result.
- [ ] An unapproved `SCIENTIFIC_MAJOR` cannot leave a confirmatory package
      confirmatory.
- [ ] A comparison that cannot be made confidently reports `UNKNOWN` and
      escalates — never `NONE`.
- [ ] Conformance records bind to a code digest and supersede rather than
      overwrite.

## What this package cannot establish

> **What this package cannot establish.** That the specification was right.
> Conformance proves the code implements what was frozen; if what was frozen was
> a poor method, a perfect conformance result certifies a poor method faithfully
> executed. It also cannot detect a drift that both the specification and the code
> describe identically and wrongly — that is scientific review's job, at a
> different gate.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Chief Architect** is assigned accountable; an implementer is named; **Engineering Productivity Lead / Assurance Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-023` — Git, Worktree and Protected-Path Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-047` — Role and Skill Registries, and the Task Compiler — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-081` — Protocol, Analysis, Baseline and Falsification Registry — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-107` — Engineering Vertical Slice — Spec, Worktree, Signed Release — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Engineering Productivity Lead / Assurance Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

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
- [ ] `CTL-SUP-01` failing its effectiveness test.
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
