---
title: "WP-066 — Agent Candidate and Used-Source Write-Back — Acceptance Criteria"
aliases:
  - "WP-066 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-066 — Agent Candidate and Used-Source Write-Back — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-066` |
| Work package | [`WP-066` — Agent Candidate and Used-Source Write-Back](wp_066_zotero_agent_writeback.md) |
| Companion | [test procedures](wp_066_zotero_agent_writeback.tests.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / Security** — the independent verifier |
| Accountable owner | Knowledge Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-066` |

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

Each criterion names the test case in [`WP-066_zotero_agent_writeback.tests.md`](wp_066_zotero_agent_writeback.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Agents write **only** discovered candidates and used sources, only into their
      declared collections, and a write that is neither is refused.
- [ ] Every write to the personal library and to `00_Human_Seeds` is refused.
- [ ] A write to a human-authority field on an existing item is refused, naming the
      field.
- [ ] **A stale conditional write returns 412 and the human's edit survives**, and
      a blind retry that ignores the conflict is refused. This is invariant 5's
      *never silently overwritten*, implemented.
- [ ] **A collection membership update preserves human-added items**, and a
      membership write attempted without reading first is **refused by the client**
      — Zotero's full-list semantics would otherwise delete everything the agent did
      not know about.
- [ ] Every agent-written item and field carries the agent marker.
- [ ] Licence-restricted attachments are referenced, never uploaded; human notes
      are never written into.
- [ ] Exceeding the write-rate threshold throttles and reports.
- [ ] Every write produces a `SyncReceipt`, and the agent's full set of library
      changes **reconstructs from receipts alone**.

## What this package cannot establish

> **The most dangerous call in this package is the one that looks safest.**
> Collection membership uses full-list semantics: a PATCH that omits an item
> removes it. TC-11 refuses the naive form outright rather than relying on every
> caller remembering, because the failure is silent, immediate and destroys a
> researcher's curation.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Platform Lead** is assigned accountable; an implementer is named; **Knowledge Curator / Security** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-012` — Canonical Ownership and Field-Level Authority Matrix — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-050` — Initial Tool Connector Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-061` — Canonical Source Registry Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-062` — Source Identity Resolution, Deduplication and Merge — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-064` — Zotero Library, Collection and Permission Model — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Knowledge Curator / Security** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-02` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-03` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-35` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-03` failing its effectiveness test.
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
