# WP-121 — Hypercare, Stabilisation and Programme Closure — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-121` |
| Work package | [`WP-121` — Hypercare, Stabilisation and Programme Closure](WP-121_hypercare_stabilization.md) |
| Companion | [test procedures](WP-121_hypercare_stabilization.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Executive Sponsor / Assurance** — the independent verifier |
| Accountable owner | SRE Lead / Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-121` |

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

Each criterion names the test case in [`WP-121_hypercare_stabilization.tests.md`](WP-121_hypercare_stabilization.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **Exit criteria are declared before hypercare begins**, and beginning without
      them is refused. Otherwise hypercare ends when everyone is tired.
- [ ] The rota covers every hour, the decision cadence is scheduled, and the critical
      journeys are continuously observed with synthetic checks that **alert on
      failure within a declared window**.
- [ ] At least one incident runs to closure through contain → recover → learn →
      close.
- [ ] **Rollback is exercised as a normal hypercare response**, not as an incident
      escalation — which is what stops a team working around a problem instead of
      reverting it.
- [ ] Every reconciliation runbook runs at least once and records what diverged.
- [ ] **Operator learning is captured into runbooks and the vault before the rota
      disperses**, and exiting with open knowledge items is refused.
- [ ] **The SLO and quality baselines are measured over a declared window**, and the
      quality baseline includes all three anti-metrics: G10 reversal rate,
      acceptance-despite-adversarial-rejection, and decision-time distribution. A
      baseline drawn from too few observations is **flagged**.
- [ ] The exit review is held against the criteria, **extending hypercare is a
      reachable outcome**, and the handoff is accepted by a **named Day-2 owner**
      with open items transferred with owners and expiries.

## What this package cannot establish

> **Hypercare ends supervision, not risk.** The system after handoff is the same
> system, watched less closely. Everything that made hypercare useful — the
> synthetic runs, the anti-metric baselines, the reconciliation cadence — becomes
> Day-2's job (WP-122–130), and the baselines established here are the only
> reference later drift can be measured against.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **SRE Lead / Program Lead** is assigned accountable; an implementer is named; **Executive Sponsor / Assurance** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-120` — Production Cutover and Go-Live Decision — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Executive Sponsor / Assurance** verified **independently of the producer** and did not see the producer's working trace.
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
