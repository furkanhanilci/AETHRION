# WP-017 — Source Registry and Literature Contract Schemas — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-017` |
| Work package | [`WP-017` — Source Registry and Literature Contract Schemas](WP-017_source_literature_contracts.md) |
| Companion | [test procedures](WP-017_source_literature_contracts.tests.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Citation Auditor / Data Architect** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-017` |

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

Each criterion names the test case in [`WP-017_source_literature_contracts.tests.md`](WP-017_source_literature_contracts.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All ten literature contracts validate, and `SourceRecord` carries **no
      field describing a specific file** — representation data lives on
      `SourceRepresentation`.
- [ ] One work with two representations resolves correctly, each with its own
      hash, format and licence.
- [ ] An evidence anchor to a `SourceRecord` without a representation is
      **rejected**.
- [ ] A representation whose licence forbids retention falls back to hash-only
      (`PR-14`), demonstrated by a refusal.
- [ ] Every screening decision states its basis, and included/excluded counts
      reconcile against the search protocol.
- [ ] A frozen `LiteratureSetManifest` does **not** follow later registry changes.
- [ ] A retraction is visible **through** the frozen set, and every dependent claim
      is reachable — the backwards traversal works.
- [ ] `monitor_sources.py` writes into `RetractionStatus`, so the G10 measurement
      no longer reports `claim_impact_analysis: not implemented`.
- [ ] **The read-only Zotero boundary is proven behaviourally**: a transport that
      raises on any non-`GET` method, driven through the whole sync flow, passes.
      This closes finding **H3**.
- [ ] A sync with no changes still produces a `SyncReceipt` stating so.
- [ ] An `AnnotationObservation` cannot become a claim without passing through the
      claim contract.
- [ ] A `SourceRecord` merge produces lineage; every prior citation resolves.

## What this package cannot establish

> **The migration risk this package owns.** The V0 registry holds 33 real sources
> with an identity scheme this contract changes. The migration must be reversible
> and must not re-mint identity for existing records — a citation that resolved
> yesterday and not today is the failure the whole package exists to prevent.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Lead** is assigned accountable; an implementer is named; **Citation Auditor / Data Architect** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-012` — Canonical Ownership and Field-Level Authority Matrix — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Citation Auditor / Data Architect** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-LIT-01` failing its effectiveness test.
- [ ] `CTL-LIT-02` failing its effectiveness test.

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
