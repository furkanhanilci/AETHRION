# WP-146 — Epistemic Memory Taxonomy and Retention — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-146` |
| Work package | [`WP-146` — Epistemic Memory Taxonomy and Retention](WP-146_epistemic_memory_taxonomy.md) |
| Companion | [test procedures](WP-146_epistemic_memory_taxonomy.tests.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Archivist / Internal Audit** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-146` |

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

Each criterion names the test case in [`WP-146_epistemic_memory_taxonomy.tests.md`](WP-146_epistemic_memory_taxonomy.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Six memory contracts exist with a complete authority-matrix row each, and
      **exactly one** carries the may-support-a-claim property.
- [ ] The decay job excludes the evidence store and the human-intervention audit,
      and **reports the exclusions**.
- [ ] The planted evidence control survives with an unchanged digest **and** the
      planted stale procedure expires. Both halves, in the same run.
- [ ] A procedural or search-experience record cannot be cited in support of a
      claim.
- [ ] A blind reviewer cannot reach the producer's search or procedural memory,
      and can still reach everything the frozen packet includes.
- [ ] A `FailedApproach` remains retrievable after its campaign closes, and does
      not suppress a scientifically distinct retry.
- [ ] A source retraction cascades to findings, claims and principles **without
      deleting any raw artifact**.
- [ ] A `HumanInterventionRecord` cannot be edited.
- [ ] A `MemoryQuery` that names no store is refused rather than silently
      widened, and derived indexes rebuild losslessly from canonical stores.

## What this package cannot establish

> **What this package cannot establish.** That the right things are remembered. A
> typed store with correct authority can still be full of lessons nobody needed
> and missing the one that mattered, and only the metascience measures in WP-130
> — failed-approach reuse, repeated-experiment rate, memory-assisted uplift
> against a control — say whether the memory is earning its cost. Nor does it
> establish that a procedural entry marked current is still true; revalidation
> reduces that risk and does not remove it.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Lead** is assigned accountable; an implementer is named; **Archivist / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-012` — Canonical Ownership and Field-Level Authority Matrix — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-030` — Neo4j, pgvector and OpenSearch Derived Read Models — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-075` — Canonical Claim/Evidence Ledger Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-077` — Claim State, Dependency and Assessment Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-144` — Discovery Search Graph and Candidate Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Archivist / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-63` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-70` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-79` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-096` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-098` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-03` failing its effectiveness test.
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
