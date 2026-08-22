---
title: "WP-067 — Zotero Two-Way Sync and Reconciliation — Acceptance Criteria"
aliases:
  - "WP-067 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-067 — Zotero Two-Way Sync and Reconciliation — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-067` |
| Work package | [`WP-067` — Zotero Two-Way Sync and Reconciliation](wp_067_zotero_sync_reconciliation.md) |
| Companion | [test procedures](wp_067_zotero_sync_reconciliation.tests.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / SRE** — the independent verifier |
| Accountable owner | Knowledge Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-067` |

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

Each criterion names the test case in [`WP-067_zotero_sync_reconciliation.tests.md`](wp_067_zotero_sync_reconciliation.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A no-change sync reads and writes nothing.
- [ ] **Disjoint field edits by human and agent both survive** — the merge is
      field-level, never item-level.
- [ ] A same-field conflict opens a `ConflictCase` and **discards neither value**.
- [ ] A 412 causes re-read and merge, **never a blind retry**. The conditional
      write exists to detect this; retrying past it is the overwrite.
- [ ] Upstream deletion, permission change and duplicate appearance are three
      **distinguishable** states with three recorded responses. Conflating them is
      finding **H2**.
- [ ] Every `ConflictCase` has an SLA and **escalates on breach**; none ages
      silently.
- [ ] **Losing the checkpoint store is recoverable**: full resync plus dedup and
      rebind produces no duplicates and overwrites no human edit. A recovery that
      duplicates the library is worse than the outage.
- [ ] **The overwrite detector fires on a seeded overwrite and the prior value is
      recoverable**, and the detector suite **fails when the seed is removed**.
- [ ] Sync lag, error rate and conflict queue depth are observable.

## What this package cannot establish

> **Reconciliation cannot restore intent.** When a human and an agent edit the same
> field, the system can preserve both values and ask — it cannot know which was
> meant. Every automatic resolution class in this package is one where authority
> was decided in advance by WP-012; everything else goes to a person, and the
> queue depth is the honest measure of how often that happens.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Platform Lead** is assigned accountable; an implementer is named; **Knowledge Curator / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-061` — Canonical Source Registry Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-062` — Source Identity Resolution, Deduplication and Merge — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-064` — Zotero Library, Collection and Permission Model — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-065` — Personal Zotero Seed Ingest Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-066` — Agent Candidate and Used-Source Write-Back — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Knowledge Curator / SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-03` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-28` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-01` failing its effectiveness test.

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
