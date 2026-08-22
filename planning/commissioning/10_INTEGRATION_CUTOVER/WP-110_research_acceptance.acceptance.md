# WP-110 — Research and Literature Acceptance Package — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-110` |
| Work package | [`WP-110` — Research and Literature Acceptance Package](WP-110_research_acceptance.md) |
| Companion | [test procedures](WP-110_research_acceptance.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Citation Auditor / Assurance** — the independent verifier |
| Accountable owner | Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-110` |

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

Each criterion names the test case in [`WP-110_research_acceptance.tests.md`](WP-110_research_acceptance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All eight scenarios run **serially against one release candidate**, each
      result independently attributable.
- [ ] **`ACC-05` closes the gap the Bridge documents against itself**: an injected
      instruction in a PDF abstract arrives at the MCP surface inside a boundary
      marker with the agent's scope unchanged.
- [ ] **`ACC-06` refuses producer self-approval through every available path** — the
      cockpit, the API and delegation — and under solo operation either refuses by
      separation constraint or **`BLOCKED`s with the ADR-001 declaration**.
- [ ] `ACC-07` randomises finding order with the seed recorded, and verdicts are
      compared across orders.
- [ ] **`ACC-08` shows the counter-test was executed and its result acted on**, and a
      disconfirming outcome **moves the claim's state** rather than being quietly
      retained.
- [ ] `ACC-01`–`ACC-04` each close: no personal Zotero field modified; the agent
      cannot apply its own proposal; two distinct works are not merged; a retraction
      reaches derived claims.
- [ ] **A Critical finding cannot be closed as a probable false positive** — a
      reproducer result is required, and one is produced.
- [ ] The dossier carries every result, its evidence and its disposition, and the
      sign-off names an owner, requires MFA and lists residual risks with owners and
      expiries.

## What this package cannot establish

> **`ACC-06` is the scenario this laboratory is most likely to fail.** Self-approval
> is prevented by separation constraints on a `RoleBinding`, and a solo operator
> holds many roles. ADR-001 already decided the honest answer: R1 solo, R2 under a
> declared partial profile, **R3 `BLOCKED`**. If this scenario passes cleanly at R3,
> the most likely explanation is that the control was not exercised — not that the
> constraint was satisfied.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Research Director** is assigned accountable; an implementer is named; **Citation Auditor / Assurance** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-103` — Vertical Slice 2 — Two-Way Literature and Set Freeze — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-104` — Vertical Slice 3 — Baseline through Run to Claim/Evidence — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-105` — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-106` — Vertical Slice 5 — Human Decision, Publish and Monitor — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-108` — Retraction, Drift and Supersession Vertical Slice — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-109` — Forty Acceptance Scenario Registry and Harness — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Citation Auditor / Assurance** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-01` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-01` failing its effectiveness test.
- [ ] `CTL-GOV-02` failing its effectiveness test.

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
