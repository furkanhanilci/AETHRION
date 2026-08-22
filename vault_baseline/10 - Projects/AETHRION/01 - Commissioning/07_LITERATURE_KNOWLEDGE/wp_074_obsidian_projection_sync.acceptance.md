---
title: "WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back — Acceptance Criteria"
aliases:
  - "WP-074 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-074_obsidian_projection_sync.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-074` |
| Work package | [`WP-074` — Obsidian Projection, Link Integrity and Knowledge Write-Back](wp_074_obsidian_projection_sync.md) |
| Companion | [test procedures](wp_074_obsidian_projection_sync.tests.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / Data Platform Lead** — the independent verifier |
| Accountable owner | Knowledge Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-074` |

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

Each criterion names the test case in [`WP-074_obsidian_projection_sync.tests.md`](wp_074_obsidian_projection_sync.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Changing one source rewrites **only** that source's note, and **projecting
      twice with no change rewrites nothing** — no content, no mtime. No generated
      file carries a wall-clock timestamp.
- [ ] **Manifest-owned deletion holds**: a human note in the generated area
      survives, a removed source's note is removed, and **an unreadable manifest
      refuses the run** rather than being overwritten.
- [ ] **The plan mirror refuses a root-directory target**, naming the stray files —
      the hazard `AGENTS.md` §10 records as having destroyed a vault — and **no
      automated path passes `--force`**.
- [ ] A three-way merge preserves both a human edit in the human zone and a
      generator update in the generated zone; an edit inside a generated zone is
      **reported as drift**.
- [ ] **The 10,000-source projection cap is removed**, and a partial read of the
      registry causes the projection to **refuse to remove anything** rather than
      deleting the unseen. This is finding **M9**.
- [ ] **Ingest pagination (H1) is unblocked only after this package is accepted**,
      enforced rather than documented. The ordering is not a preference: paging
      first turns a masked truncation into deletion of a researcher's files.
- [ ] Broken links and orphans reach the curator queue.
- [ ] **A full rebuild returns every generated file byte-identically**, and anything
      that does not return is reclassified as human work with the zone map
      corrected.

## What this package cannot establish

> **This package can destroy a researcher's work and has come close.** Every
> control here — the manifest, the stray-file refusal, the unreadable-manifest
> stop, the refusal to remove on a partial read — exists because the alternative
> is silent, immediate and unrecoverable. None of them should be relaxed for
> convenience, and the `--force` flag exists for a human at a keyboard who has
> read the file list, never for an automated caller.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Knowledge Platform Lead** is assigned accountable; an implementer is named; **Knowledge Curator / Data Platform Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-028` — NATS JetStream and Transactional Outbox Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-030` — Neo4j, pgvector and OpenSearch Derived Read Models — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-061` — Canonical Source Registry Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-072` — LiteratureSetManifest Freeze and Human-Readable Archive — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-073` — Obsidian Vault, Human/Generated Zones and Templates — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Knowledge Curator / Data Platform Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-21` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-22` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-31` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-03` failing its effectiveness test.
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
