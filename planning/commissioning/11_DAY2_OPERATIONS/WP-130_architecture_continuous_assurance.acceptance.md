# WP-130 — Architecture and Platform Continuous Assurance — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-130` |
| Work package | [`WP-130` — Architecture and Platform Continuous Assurance](WP-130_architecture_continuous_assurance.md) |
| Companion | [test procedures](WP-130_architecture_continuous_assurance.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Architecture Board / Internal Audit** — the independent verifier |
| Accountable owner | Chief Architect / Platform Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-130` |

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

Each criterion names the test case in [`WP-130_architecture_continuous_assurance.tests.md`](WP-130_architecture_continuous_assurance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **The monthly drift scan checks every stated invariant** and lists deviations:
      a derivative holding unrecoverable state is **reclassified as canonical**, a
      consumer writing gate state is flagged as `PR-07`, and a dependency-direction
      violation **fails rather than warns**.
- [ ] **A published contract with no consumer is flagged** — *bind it or delete it*,
      which is finding **H4**'s own rule applied on a schedule.
- [ ] Schema, adapter and policy compatibility all pass, and **a provider response
      shape changing behind an adapter is detected** before the canonical contract
      silently diverges from what is stored.
- [ ] **Both golden paths run end to end on schedule** — a synthetic research project
      through G0–G10 and a synthetic engineering change through review to signed
      release — and a broken step **fails and alerts**. This is the closest thing the
      system has to continuous integration of itself.
- [ ] **A sampled derived rebuild is byte-equivalent from canonical records**, and
      anything that no longer rebuilds is reclassified with the matrix corrected.
- [ ] **Every number a document states about the repository is derived or flagged as
      unverifiable**, and a stated number with no derivation rule is flagged — the
      known failure class is that checks cover only the numbers someone registered.
- [ ] **No test mutates production state**, and the monitoring coverage fraction is
      reported with the unmonitored set named.
- [ ] **A platform invariant cannot be accepted on assertion.** The platform meets
      the evidentiary standard it imposes on the research it hosts.

## What this package cannot establish

> **This package institutionalises looking, and looking is still not proving.**
> `AGENTS.md` §11 states the limit that survives every check in this programme: all
> of them are internal consistency, and every one would hold for a corpus describing
> a system that does not work. External truth enters through two doors — reference
> verification, and the adopted benchmarks — and the second remains **unrun**. A
> platform that passes its own continuous assurance has demonstrated that it is
> self-consistent, which is exactly what it always was.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Chief Architect / Platform Assurance Lead** is assigned accountable; an implementer is named; **Architecture Board / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-010` — Architecture Decision and Rejected-Alternatives Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-030` — Neo4j, pgvector and OpenSearch Derived Read Models — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-040` — Workflow Replay, Versioning and Failure Test Suite — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-060` — Agentic Security Attack Suite and Red-Team Acceptance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-109` — Forty Acceptance Scenario Registry and Harness — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-115` — Full System Regression and Commissioning Dossier — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-123` — Control Effectiveness and Policy Regression Rhythm — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-124` — Model Requalification, Drift and Ejection Rhythm — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-125` — Literature, Zotero and Obsidian Curation Rhythm — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-126` — Reviewer, Judge and Reproducer Calibration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-127` — FinOps, Capacity and Portfolio Review Rhythm — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-128` — Incident, Postmortem and Learning Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-129` — Quarterly DR, Supply-Chain and Audit Drill — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Architecture Board / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
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
