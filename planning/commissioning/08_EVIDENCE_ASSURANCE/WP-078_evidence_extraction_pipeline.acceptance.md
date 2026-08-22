# WP-078 — Structured Evidence Extraction Pipeline — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-078` |
| Work package | [`WP-078` — Structured Evidence Extraction Pipeline](WP-078_evidence_extraction_pipeline.md) |
| Companion | [test procedures](WP-078_evidence_extraction_pipeline.tests.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Independent Evidence Auditor** — the independent verifier |
| Accountable owner | Evidence Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-078` |

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

Each criterion names the test case in [`WP-078_evidence_extraction_pipeline.tests.md`](WP-078_evidence_extraction_pipeline.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Extraction runs **only on sources that cleared quarantine**, under a T0/T1
      read-only profile.
- [ ] **Every extracted field carries a locator and a quote hash.** A field with no
      locator is refused — a value without provenance is a summary, and a summary
      cannot support a claim.
- [ ] Altering the source text after extraction breaks the quote hash and flags the
      candidate.
- [ ] Method fields come from the method section; an estimate reported only in a
      table anchors to the **table cell**.
- [ ] **`not reported`, `null` and *field absent* stay three distinguishable
      states.** Conflating them turns a study's limitation into an extraction gap,
      or hides it entirely.
- [ ] The deterministic parsing stage reproduces identically.
- [ ] **The second pass is independent** — a different model family or strategy,
      checked against the independence profile — and **the disagreement rate is
      reported as a number per field type**. A second pass by the same model
      reproducing the same mistakes is not verification.
- [ ] Disagreements are resolved by a human or arbiter with **both original values
      retained**.
- [ ] Counter-evidence and null results are captured rather than dropped.
- [ ] Disagreement rate, missing-field rate and locator-failure rate are observable.

## What this package cannot establish

> **The disagreement rate is a lower bound, not the error rate.** Two independent
> passes agreeing means neither caught an error; it does not mean there was none.
> `PR-16` states the reason directly — independence is asserted throughout and
> measured nowhere, and two genuinely different models can fail together on exactly
> the cases a reader would most want checked. The honest reading of a low
> disagreement rate is *these two passes agree*, and nothing more.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Evidence Lead** is assigned accountable; an implementer is named; **Independent Evidence Auditor** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-045` — Policy Router and Minimum-Sufficient Model Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-047` — Role and Skill Registries, and the Task Compiler — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-058` — Untrusted Content Quarantine and Prompt-Injection Firewall — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-063` — Source Representation, Licence and Status Monitoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-068` — Zotero Annotation → EvidenceCandidate Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-076` — Evidence Span Anchoring and Re-anchoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Independent Evidence Auditor** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-SEC-01` failing its effectiveness test.
- [ ] `CTL-EPI-01` failing its effectiveness test.

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
