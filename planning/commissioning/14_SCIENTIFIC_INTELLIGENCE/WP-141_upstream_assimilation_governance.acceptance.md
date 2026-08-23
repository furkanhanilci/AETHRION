# WP-141 — Upstream Assimilation, Lineage and Characterisation Governance — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-141` |
| Work package | [`WP-141` — Upstream Assimilation, Lineage and Characterisation Governance](WP-141_upstream_assimilation_governance.md) |
| Companion | [test procedures](WP-141_upstream_assimilation_governance.tests.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Supply Chain Security Lead / Internal Audit** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-141` |

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

Each criterion names the test case in [`WP-141_upstream_assimilation_governance.tests.md`](WP-141_upstream_assimilation_governance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every entry carries an id, a name, an assimilation type, a status, a
      licence, the date that licence was read **at the source**, what was
      deliberately not taken, and an **authority boundary**. An entry missing any
      of these fails the checker.
- [ ] `--self-test` injects a defect per rule and reports **zero silent
      controls**. A rule that cannot be made to fire is not a control.
- [ ] A `DIRECT_ADAPT` entry cannot reach `ADAPTING` or `ACCEPTED` without a
      40-character pinned commit, a named source-file list, a characterisation
      suite and a licence inside the permissive set — each refusal demonstrated
      separately, not as one combined case.
- [ ] An `ADAPTIVE_REIMPLEMENT` entry naming source files is **refused**, and the
      refusal names the reason: if files moved, the decision was direct
      adaptation.
- [ ] A planted unregistered adapted file fails admission **before merge**, and a
      correctly registered one **passes**. Both directions, on the same run.
- [ ] Upstream drift against a pin opens a review item and **no automatic update
      occurs**; the characterisation suite reruns before the pin moves.
- [ ] `provenance/README.md` is generated from the register and hand-editing it
      is caught by the drift check.
- [ ] Every adapted file in the repository is represented in the register, or
      carries a recorded exception with an owner and an expiry.
- [ ] `NOTICE` and the register agree on every file that carries a third-party
      licence.

## What this package cannot establish

> **What this package cannot establish.** That any adapted mechanism is *correct*.
> A characterisation suite proves the local implementation behaves like the
> upstream one; whether the upstream one was right is a different question that
> only the mechanism's own acceptance can answer. It also cannot establish that
> the licence reading was correct — that is a human judgement made on a date, and
> the register records the date so it can be re-made rather than assumed.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Chief Architect** is assigned accountable; an implementer is named; **Supply Chain Security Lead / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-010` — Architecture Decision and Rejected-Alternatives Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-022` — Repository Topology and Code Ownership — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-024` — CI Foundation and Deterministic Quality Gates — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-059` — Supply-Chain Admission, Sigstore and SLSA Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Supply Chain Security Lead / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-73` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-74` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-GOV-01` failing its effectiveness test.

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
