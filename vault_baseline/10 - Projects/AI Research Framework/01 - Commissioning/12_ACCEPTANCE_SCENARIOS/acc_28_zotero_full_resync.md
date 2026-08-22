# ACC-28 — Zotero Full Resync

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-28` |
| Category | Literature/DR |
| Severity | **High** |
| Accountable owner | Knowledge Platform Lead |
| Independent witness / verifier | Knowledge Curator / SRE |
| Related packages | `WP-067`, `WP-103`, `WP-114` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Zotero Full Resync** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The Zotero bridge checkpoint state has been lost; the personal and group libraries, the Source Registry mapping and the receipts are intact.

**When:** A full resync with the dedup and rebind procedure runs from a zero checkpoint.

**Then:** Item versions and bindings reconcile without producing duplicates or overwriting a human field; conflicts go to the curator queue.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Take the pre-resync counts, hashes and item versions | Execution log + trace/event references |
| 2 | Delete the bridge sync state in a controlled way | Execution log + trace/event references |
| 3 | Run the full library reads and resolver mapping | Execution log + trace/event references |
| 4 | Reconcile against existing receipts, bindings and idempotency records | Execution log + trace/event references |
| 5 | Process the conflicting-edits fixture | Execution log + trace/event references |
| 6 | Verify the post-resync counts, diffs and conflicts | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] New duplicates = 0
- [ ] Human-authoritative fields are unchanged
- [ ] Bindings are complete
- [ ] Uncertain conflicts are queued rather than resolved
- [ ] Writes to the personal library = 0
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SyncCheckpoints(new)`
- `ZoteroBindings`
- `SyncReceipts`
- `ConflictCases`
- `ResyncReport`

## Expected events

- `zotero.full_resync_started`
- `source.rebound`
- `reconciliation.required`
- `zotero.full_resync_completed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-28-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-28-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-28-state-before.json` and `ACC-28-state-after.json`.
- `ACC-28-events.json`, `ACC-28-policy-decisions.json` and `ACC-28-audit-export.json`.
- `ACC-28-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The new checkpoint is retained as the baseline; fixture conflicts are closed by curator disposition.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
