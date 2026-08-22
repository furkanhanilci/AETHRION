---
title: "WP-094 — Literature Workbench and Reconciliation UI — Acceptance Criteria"
aliases:
  - "WP-094 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-094_literature_workbench.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-094 — Literature Workbench and Reconciliation UI — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-094` |
| Work package | [`WP-094` — Literature Workbench and Reconciliation UI](wp_094_literature_workbench.md) |
| Companion | [test procedures](wp_094_literature_workbench.tests.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Knowledge Curator / Citation Auditor** — the independent verifier |
| Accountable owner | Knowledge Product Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-094` |

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

Each criterion names the test case in [`WP-094_literature_workbench.tests.md`](wp_094_literature_workbench.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The campaign dashboard shows queries, execution log, known-item recall and
      saturation.
- [ ] **The coverage panel publishes the monitored fraction and names the
      unmonitored sources.** Showing *no retractions found* without it is refused —
      a monitor covering 45% reports clean for the same reason one covering nothing
      would.
- [ ] The reconciliation screen shows **both candidates with the match features**
      that produced the conflict, so a curator can reject a merge the resolver was
      tempted by (`ACC-03`).
- [ ] Screening requires a reason code and **does not show the other screener's
      decision**; disagreements route to arbitration rather than being resolved by
      whoever looks second.
- [ ] Annotation promotion captures actor, reason and **locator state**, and
      promoting a degraded span is permitted and **visibly flagged**.
- [ ] The Zotero panel shows last sync, receipts, lag and conflicts, and **a failed
      sync is shown rather than the library being presented as current**.
- [ ] Manifest freeze and diff work from the workbench.
- [ ] **Every queue shows its depth and its oldest item**, and an item past its SLA
      escalates rather than ageing silently.

## What this package cannot establish

> **A workbench makes curation possible, not correct.** Every judgement here — this
> is the same work, this source is included, this highlight supports that claim —
> is a human decision the interface can only present well. The measurable output is
> the **false-merge rate** (WP-062) and the **screening disagreement rate**
> (WP-071); the interface's contribution to either is not separable from the
> curator's.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Product Lead** is assigned accountable; an implementer is named; **Knowledge Curator / Citation Auditor** is assigned verifier and is **independent of the producer** under WP-007's profile.
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
- [ ] `WP-091` — Lab Cockpit Information Architecture and Application Shell — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Knowledge Curator / Citation Auditor** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-01` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-02` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-03` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-04` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
