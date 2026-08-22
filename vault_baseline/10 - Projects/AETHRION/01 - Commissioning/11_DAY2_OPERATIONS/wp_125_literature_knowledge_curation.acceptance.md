---
title: "WP-125 — Literature, Zotero and Obsidian Curation Rhythm — Acceptance Criteria"
aliases:
  - "WP-125 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-125_literature_knowledge_curation.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-125 — Literature, Zotero and Obsidian Curation Rhythm — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-125` |
| Work package | [`WP-125` — Literature, Zotero and Obsidian Curation Rhythm](wp_125_literature_knowledge_curation.md) |
| Companion | [test procedures](wp_125_literature_knowledge_curation.tests.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Citation Auditor / Knowledge Curator** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-125` |

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

Each criterion names the test case in [`WP-125_literature_knowledge_curation.tests.md`](wp_125_literature_knowledge_curation.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The daily sync check runs, and **a failed sync is surfaced the same day** with
      the library never presented as current.
- [ ] Every curator queue has a recorded depth and oldest item, and an item past its
      SLA escalates. A queue growing without bound is a **finding**.
- [ ] **Unscreened candidates expire at their TTL with the expiry recorded**, so the
      coverage claim stays honest rather than resting on an unworked queue.
- [ ] Duplicate and **false-merge rates** are reported as numbers.
- [ ] The monthly status scan routes detections to `ImpactScan`, **fails when its
      positive control is removed**, and **states the monitored fraction** — today
      the DOI-resolved path covers 15 of 33 registry sources.
- [ ] The vault lint passes: links resolve, frontmatter is present, tags are in the
      controlled vocabulary, and no page is orphaned.
- [ ] **A human edit inside a generated zone is reported as drift with the text
      recoverable**, and projecting unchanged input rewrites nothing.
- [ ] The quarterly review confirms or changes group membership, permissions and
      licences **with a reason**; a licence that no longer permits retention triggers
      byte removal with a hash-only reference retained.

## What this package cannot establish

> **Curation cadence keeps the base current; it does not make it complete.** The
> coverage limits from WP-069 and WP-070 do not improve with time, and the monthly
> scan can only monitor what carries a resolvable identifier. A knowledge base that
> is perfectly maintained over an incomplete literature is exactly as incomplete as
> it was on the day it was frozen.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Lead** is assigned accountable; an implementer is named; **Citation Auditor / Knowledge Curator** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-061` — Canonical Source Registry Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-062` — Source Identity Resolution, Deduplication and Merge — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-063` — Source Representation, Licence and Status Monitoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-064` — Zotero Library, Collection and Permission Model — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-065` — Personal Zotero Seed Ingest Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-066` — Agent Candidate and Used-Source Write-Back — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-067` — Zotero Two-Way Sync and Reconciliation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-068` — Zotero Annotation → EvidenceCandidate Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-069` — SearchProtocol and LiteratureCampaign Orchestration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-070` — Human + Agent Two-Way Literature Discovery — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-071` — Screening, Inclusion/Exclusion and Coverage — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-072` — LiteratureSetManifest Freeze and Human-Readable Archive — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-073` — Obsidian Vault, Human/Generated Zones and Templates — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-074` — Obsidian Projection, Link Integrity and Knowledge Write-Back — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-121` — Hypercare, Stabilisation and Programme Closure — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Citation Auditor / Knowledge Curator** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-LIT-03` failing its effectiveness test.

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
