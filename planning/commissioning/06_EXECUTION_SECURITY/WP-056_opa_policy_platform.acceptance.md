# WP-056 — Policy Decision Point and Bundle Distribution — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-056` |
| Work package | [`WP-056` — Policy Decision Point and Bundle Distribution](WP-056_opa_policy_platform.md) |
| Companion | [test procedures](WP-056_opa_policy_platform.tests.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Safety / Security / Internal Audit** — the independent verifier |
| Accountable owner | Policy Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-056` |

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

Each criterion names the test case in [`WP-056_opa_policy_platform.tests.md`](WP-056_opa_policy_platform.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Eight policy domains exist as **separate modules with explicit precedence**;
      no rule set evaluates every domain at once. This is the structural answer to
      `PR-02`.
- [ ] **Every rule has a negative case that must be denied** — zero rules with only
      positive tests — and property tests find no input producing an allow the
      precedence rules forbid.
- [ ] An unsigned bundle is refused **at every enforcement point**, and promotion
      carries the same digest from dev to production.
- [ ] Rollback restores the previous signed bundle and **preserves the decision
      log**.
- [ ] **Shadow evaluation reports a flipped decision before promotion**, enforcing
      nothing. A policy change discovered in an incident was not shadowed.
- [ ] Rules that have never fired are **listed and dispositioned** — a rule that
      never fires is dead or is guarding something never attempted, and both are
      worth knowing.
- [ ] Decision logs redact D3 content while recording the decision, and an exported
      log cannot be altered.
- [ ] Every denial names the module, the rule and the inputs that produced it.

## What this package cannot establish

> **Tested policy is not correct policy.** The suite proves the rules do what they
> say. Whether they say the right thing is a governance question answered by
> WP-009's control registry and by `PR-02`'s real test — whether a person other
> than the author can explain a denial (WP-016's legibility check). A policy that
> passes every test and nobody understands will be routed around.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Policy Platform Lead** is assigned accountable; an implementer is named; **Safety / Security / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-009` — Control Catalogue, Exceptions and Non-Waivable Blockers — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-055` — SPIFFE/SPIRE Workload Identity and Vault — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Safety / Security / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-24` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-26` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
