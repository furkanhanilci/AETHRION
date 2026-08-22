# WP-016 — PolicyDecision, Control and Exception Schemas — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-016` |
| Work package | [`WP-016` — PolicyDecision, Control and Exception Schemas](WP-016_policy_control_exception_contracts.md) |
| Companion | [test procedures](WP-016_policy_control_exception_contracts.tests.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Internal Audit** — the independent verifier |
| Accountable owner | Policy Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-016` |

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

Each criterion names the test case in [`WP-016_policy_control_exception_contracts.tests.md`](WP-016_policy_control_exception_contracts.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] `PolicyDecision` carries inputs, input hash, bundle version, rule ID and a
      **non-empty explanation** — all mandatory.
- [ ] A stored decision **replays**: the same input hash against the same bundle
      version produces the identical decision.
- [ ] The input hash is sensitive — changing any input changes the hash.
- [ ] A request matching no rule is **denied by default**.
- [ ] Every anomaly kind — missing input, evaluation timeout, unparseable bundle —
      produces a **denial, not a warning**, with one transcript each.
- [ ] An expired exception is refused **at the point of use**; an out-of-scope use
      is refused distinguishably from an expiry.
- [ ] Every declared re-evaluation trigger causes re-evaluation, demonstrated once
      per trigger. No decision is inherited across a trigger.
- [ ] Every explanation names the rule that fired.
- [ ] `ControlRecord` agrees with WP-009's registry; neither holds a second copy of
      the control list.
- [ ] **Ten real denials were explained correctly by a reader who did not author
      the policy**, and the score is recorded. This is the `PR-02` control.

## What this package cannot establish

> **The behaviour to watch in production.** The rate of policy overrides. A rising
> override rate does not mean the policy is too strict; it usually means the
> denials stopped being explainable, and people route around what they cannot
> understand.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Policy Platform Lead** is assigned accountable; an implementer is named; **Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-009` — Control Catalogue, Exceptions and Non-Waivable Blockers — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

**No acceptance scenario names this package.** It can reach `ACCEPTED` on its own evidence and cannot reach `COMMISSIONED` through a scenario, because there is none to pass. `00_PROGRAM/11`'s completeness rule calls this an incomplete entry rather than a shorter one.

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
- [ ] `CTL-GOV-03` failing its effectiveness test.

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
