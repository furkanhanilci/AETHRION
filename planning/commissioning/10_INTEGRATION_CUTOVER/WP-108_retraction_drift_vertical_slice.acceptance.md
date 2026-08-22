# WP-108 — Retraction, Drift and Supersession Vertical Slice — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-108` |
| Work package | [`WP-108` — Retraction, Drift and Supersession Vertical Slice](WP-108_retraction_drift_vertical_slice.md) |
| Companion | [test procedures](WP-108_retraction_drift_vertical_slice.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Assurance / Eval Office / Decision Owner** — the independent verifier |
| Accountable owner | Knowledge Monitoring Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-108` |

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

Each criterion names the test case in [`WP-108_retraction_drift_vertical_slice.tests.md`](WP-108_retraction_drift_vertical_slice.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All six trigger classes fire, and **each is compared against an expected set
      computed independently of the system**. An impact scan with no expected set
      reports success when it returns three claims out of nine.
- [ ] A claim **four derivation hops away is included**; an unrelated claim sharing
      a keyword is **excluded**. Both directions matter.
- [ ] A **published package** is reached, not only the claim inside it.
- [ ] A model snapshot revocation reaches **open tasks**, not only completed claims
      — `00_PROGRAM/01` invariant 7.
- [ ] **The coverage report states the monitorable fraction** and names what is
      outside it. Today the retraction path resolves by DOI and 18 of 33 registry
      sources have none.
- [ ] Every case carries priority, SLA and owner, and a Critical breach escalates.
- [ ] **The same trigger from two sources opens one case**, and a dismissed case
      **does not reopen on the next scan** — a dismissal that reappears is a snooze
      button, and a queue full of them is a queue nobody reads.
- [ ] Re-review, re-reproduction, republication and no-impact are all demonstrated
      as terminal dispositions **with reasons**.
- [ ] A suppressed scheduled scan alerts.

## What this package cannot establish

> **The expected sets are as good as the person who wrote them.** This package
> measures the impact machinery against a hand-derived answer, which is the right
> method and inherits the limits of hand derivation. A systematic blind spot shared
> by the derivation and the implementation — a dependency kind nobody modelled —
> passes both. That is `PR-16`'s shape applied to impact analysis, and the mitigation
> is that the expected sets are derived by someone other than the implementer.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Monitoring Lead** is assigned accountable; an implementer is named; **Assurance / Eval Office / Decision Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-037` — G10 Temporal Schedules and Short ImpactScan Workflows — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-042` — Capability Registry and Profile Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-044` — Model Qualification and Admission Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-063` — Source Representation, Licence and Status Monitoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-077` — Claim State, Dependency and Assessment Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-090` — PublicationPackage, RO-Crate and Provenance Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-095` — Claim/Evidence Explorer and Provenance Graph — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-106` — Vertical Slice 5 — Human Decision, Publish and Monitor — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance / Eval Office / Decision Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-04` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-31` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-36` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-02` failing its effectiveness test.
- [ ] `CTL-MOD-02` failing its effectiveness test.

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
