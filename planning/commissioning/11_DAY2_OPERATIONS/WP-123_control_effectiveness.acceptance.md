# WP-123 — Control Effectiveness and Policy Regression Rhythm — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-123` |
| Work package | [`WP-123` — Control Effectiveness and Policy Regression Rhythm](WP-123_control_effectiveness.md) |
| Companion | [test procedures](WP-123_control_effectiveness.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Internal Audit / Red Team** — the independent verifier |
| Accountable owner | Safety & Governance Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-123` |

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

Each criterion names the test case in [`WP-123_control_effectiveness.tests.md`](WP-123_control_effectiveness.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every control has a scheduled test and sampling rate; **an untested control is
      treated as failing**.
- [ ] **Five negative regression suites run on schedule** — policy, identity,
      data-class, tool scope, supply chain — and a control that silently stops
      refusing is **detected by the regression rather than in production**.
- [ ] The exception register is audited for usage; **expired exceptions are found and
      auto-revoked**, and one still working past expiry is a finding.
- [ ] **A renewal with no restated removal criterion is flagged.** A register of
      quiet renewals is a second, undocumented policy.
- [ ] Accumulated residual risk is trended and its growth raised to governance.
- [ ] Control coverage is compared against the threat-to-control map with gaps named
      and owned.
- [ ] **The false-positive rate is measured per control**, and a high rate triggers
      **tuning the control, not training the people** — a control people route
      around has already failed.
- [ ] **Two material failures of one control reopen an ADR or policy**, rather than
      producing a third remediation.
- [ ] **Closing a risk on *mitigation applied* is refused**: closure requires an
      effectiveness test, an evidence reference, a residual-risk owner and a
      re-evaluation date.

## What this package cannot establish

> **Effectiveness testing measures the controls you have.** It cannot find the
> control you never wrote, and the coverage review against the threat-to-control map
> is only as complete as that map. WP-060's attack suite and the external
> benchmarks named in `AGENTS.md` §11 — still unrun — are what would test the map
> itself.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Safety & Governance Owner** is assigned accountable; an implementer is named; **Internal Audit / Red Team** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-009` — Control Catalogue, Exceptions and Non-Waivable Blockers — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-056` — OPA Policy Platform and Bundle Distribution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-060` — Agentic Security Attack Suite and Red-Team Acceptance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-112` — Security and Privacy Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit / Red Team** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `All controls` failing its effectiveness test.

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
