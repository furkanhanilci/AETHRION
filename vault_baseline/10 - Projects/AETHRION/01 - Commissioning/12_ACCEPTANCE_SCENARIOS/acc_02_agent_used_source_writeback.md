---
title: "ACC-02 — Agent-Used Source Write-Back"
aliases:
  - "ACC-02"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Agent-Used Source Write-Back situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-02_agent_used_source_writeback.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-02 — Agent-Used Source Write-Back

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-02` |
| Category | Research/Literature |
| Severity | **Critical** |
| Accountable owner | Evidence Lead |
| Independent witness / verifier | Knowledge Curator |
| Related packages | `WP-050`, `WP-064`, `WP-066`, `WP-070`, `WP-072`, `WP-094`, `WP-103` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Agent-Used Source Write-Back** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A source found by agent discovery has been used by a material claim, its Source Registry record is complete, and it is not yet in the group library.

**When:** The used-source eligibility policy passes and the Zotero write-back connector is invoked.

**Then:** The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Ingest the source as an agent candidate | Execution log + trace/event references |
| 2 | Create the `EvidenceSpan` and the material claim link | Execution log + trace/event references |
| 3 | Verify the eligibility policy decision | Execution log + trace/event references |
| 4 | Send the write-back call twice with the same idempotency key | Execution log + trace/event references |
| 5 | Read the Zotero item, collections and version, and the registry binding | Execution log + trace/event references |
| 6 | Verify the source inside the manifest and its exports | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Exactly one item exists in Zotero
- [ ] The item is inside the correct managed collections
- [ ] The second call produces no new item and no side effect
- [ ] The `SyncReceipt` carries the previous and new version plus the policy ID
- [ ] There is no write to the personal library
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SourceRecord`
- `ClaimRecord`
- `EvidenceSpan`
- `ZoteroBinding`
- `SyncReceipt(write)`

## Expected events

- `source.used`
- `zotero.write.requested`
- `zotero.write.completed`
- `literature.source.promoted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-02-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-02-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-02-state-before.json` and `ACC-02-state-after.json`.
- `ACC-02-events.json`, `ACC-02-policy-decisions.json` and `ACC-02-audit-export.json`.
- `ACC-02-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Move the test group item to trash under the managed cleanup policy; retain the canonical source and claim test records with a `TEST` disposition.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
