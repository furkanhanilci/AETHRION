# WP-089 — DisagreementCase and Evidence-Weighted Arbitration — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-089` |
| Work package | [`WP-089` — DisagreementCase and Evidence-Weighted Arbitration](WP-089_disagreement_arbitration.md) |
| Companion | [test procedures](WP-089_disagreement_arbitration.tests.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Project Decision Owner / Internal Audit** — the independent verifier |
| Accountable owner | Assurance Lead / Arbiter |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-089` |

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

Each criterion names the test case in [`WP-089_disagreement_arbitration.tests.md`](WP-089_disagreement_arbitration.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Conflicting verdicts, producer objections and evidence mismatches **all open
      a case automatically** and share one lifecycle.
- [ ] **Resolution by majority is refused.** A third verdict does not settle a
      disagreement — in a model-operated laboratory a majority is cheap, and
      counting discards the information that made the disagreement informative.
- [ ] **The case snapshot fixes what the arbiter saw**, so a resolution can be
      re-read later against the evidence it was actually taken against.
- [ ] An arbiter who reviewed or produced is refused. Where **no independent
      arbiter exists**, the case is `BLOCKED` with a declaration naming the missing
      party, the residual-risk owner and an expiry — ADR-001's form, not an arbiter
      independent in name only.
- [ ] **The disposition records which evidence prevailed and why**, never which
      reviewer. Resolving by seniority or identity is refused.
- [ ] An arbiter can **commission a counter-test**, and a case resolved on one cites
      it. This is the only resolution that adds information rather than choosing
      between existing positions.
- [ ] **An unresolved material-risk case escalates to G8** with both positions
      intact, and **closing a case by ageing it out is refused**.
- [ ] An appeal opens a new case referencing the original, which stays intact.
- [ ] Every closed case has a terminal state with an owner and a reason.

## What this package cannot establish

> **Arbitration cannot manufacture the independence it requires.** ADR-001 already
> decided that R3 is `BLOCKED` for a solo operator, and an arbitration needing
> independence from a producer and two reviewers is the sharpest case of that
> constraint. The correct output when it cannot be satisfied is a **declaration and
> a block**, and any implementation that quietly appoints a nominally independent
> arbiter has converted a known limitation into a hidden one.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Assurance Lead / Arbiter** is assigned accountable; an implementer is named; **Project Decision Owner / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-004` — Human Decision, SLA, Delegation and Escalation Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-018` — Claim, Evidence, Review and Decision Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-077` — Claim State, Dependency and Assessment Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-087` — Mechanical Verification Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-088` — Blind, Cross-Family and Adversarial Review — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Project Decision Owner / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-090` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
