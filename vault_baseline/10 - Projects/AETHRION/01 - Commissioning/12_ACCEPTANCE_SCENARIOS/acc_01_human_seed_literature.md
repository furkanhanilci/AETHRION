---
title: "ACC-01 — Human Seed Literature"
aliases:
  - "ACC-01"
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Human Seed Literature situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-01 — Human Seed Literature

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-01` |
| Category | Research/Literature |
| Severity | **Critical** |
| Accountable owner | Knowledge Lead |
| Independent witness / verifier | Citation Auditor |
| Related packages | `WP-035`, `WP-050`, `WP-062`, `WP-064`, `WP-065`, `WP-069`, `WP-070`, `WP-072`, `WP-094`, `WP-103`, `WP-110`, `WP-115`, `WP-119`, `WP-120` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Human Seed Literature** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A seed with a DOI and a PDF attachment, explicitly selected for AIRL ingest, exists in the researcher's personal Zotero library and is absent from the Source Registry.

**When:** The read-only personal seed sync runs and the project `LiteratureCampaign` processes the source.

**Then:** The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Verify the test user and the read-only API key | Execution log + trace/event references |
| 2 | Add the seed item, PDF and annotation fixture to the selected collection | Execution log + trace/event references |
| 3 | Trigger the incremental sync | Execution log + trace/event references |
| 4 | Wait for the resolver, status/licence resolution and project binding | Execution log + trace/event references |
| 5 | Attempt a `LiteratureSetManifest` freeze | Execution log + trace/event references |
| 6 | Compare the personal item version and fields against the starting state | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Exactly one canonical `SourceRecord` exists
- [ ] The representation hash matches the fixture
- [ ] The personal item version is unchanged by AIRL
- [ ] Search/seed provenance and project binding are complete
- [ ] The manifest carries source identity, locator and status
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SourceRecord`
- `SourceRepresentation`
- `ZoteroBinding`
- `SyncReceipt(read)`
- `LiteratureSetManifest`

## Expected events

- `source.discovered`
- `source.resolved`
- `source.bound_to_project`
- `literature.set.frozen`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-01-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-01-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-01-state-before.json` and `ACC-01-state-after.json`.
- `ACC-01-events.json`, `ACC-01-policy-decisions.json` and `ACC-01-audit-export.json`.
- `ACC-01-evidence-manifest.json`: the hash, producer and environment reference of every file.
- The independent witness's `VerificationRecord`, plus any finding and disposition records.

## PASS criteria

- All scenario-specific assertions and the common integrity assertions pass.
- **An expected fail-closed, block or revise behaviour is as valid a PASS as a happy-path success** — provided it matches the expected state exactly.
- No open Critical or High findings remain.
- The evidence manifest is complete, its hashes verified and the package signed by the witness.
- Results from a different release candidate have not been merged into this one.

## FAIL and retest

The scenario FAILs if any invariant, evidence-integrity check, or expected
record/event assertion fails. A correction is opened only against a `VALIDATED`
finding. If the target revision or any related policy, schema, model or tool
bundle changes, the previous result becomes void and the scenario plus its
affected regression set are rerun.

## Cleanup and reversal

Remove the test seed selection; do not delete the `SourceRecord`, and archive the test project as `CLOSED/TEST`.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
