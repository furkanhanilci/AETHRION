# ACC-03 — Duplicate and Metadata Collision

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-03` |
| Category | Research/Literature |
| Severity | **High** |
| Accountable owner | Source Resolver Lead |
| Independent witness / verifier | Knowledge Curator |
| Related packages | `WP-012`, `WP-061`, `WP-062`, `WP-066`, `WP-067`, `WP-094`, `WP-103` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Duplicate and Metadata Collision** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The same DOI appears in two Zotero libraries with different titles and years, alongside one fuzzy title match.

**When:** A full and an incremental sync process the records concurrently with the resolver.

**Then:** The safe exact match binds to a single `SourceRecord`; conflicting fields are **not** silently overwritten and a curator `ConflictCase` is opened.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Record the conflicting fixtures and the starting item versions | Execution log + trace/event references |
| 2 | Trigger both syncs simultaneously | Execution log + trace/event references |
| 3 | Collect the resolver match features and decisions | Execution log + trace/event references |
| 4 | Inspect the `ConflictCase` in the Workbench | Execution log + trace/event references |
| 5 | Have the curator issue a disposition using the correct field authority | Execution log + trace/event references |
| 6 | Run a full resync again | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The canonical duplicate count is one, or an explained split
- [ ] Human-authoritative fields are preserved
- [ ] The `ConflictCase` carries a rationale and an actor
- [ ] The full resync creates no new duplicates
- [ ] Existing external bindings are not lost
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ResolverRecord`
- `ConflictCase`
- `Merge/SplitRecord`
- `ZoteroBinding`
- `SyncReceipt`

## Expected events

- `source.collision_detected`
- `reconciliation.required`
- `source.merge_dispositioned`
- `zotero.sync.completed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-03-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-03-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-03-state-before.json` and `ACC-03-state-after.json`.
- `ACC-03-events.json`, `ACC-03-policy-decisions.json` and `ACC-03-audit-export.json`.
- `ACC-03-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Remove the fixture items from the test library; resolver decisions are retained under `TEST` retention.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
