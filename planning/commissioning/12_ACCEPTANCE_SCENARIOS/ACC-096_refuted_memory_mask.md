# ACC-096 — A Refuted Memory Does Not Re-Enter Reasoning

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-096` |
| Category | Knowledge/Assurance |
| Severity | **High** |
| Accountable owner | Knowledge Lead |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-146`, `WP-151` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **A Refuted Memory Does Not Re-Enter Reasoning** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A memory item was refuted in an earlier round and is marked `REFUTED`; a second is `SUPERSEDED` and a third is a stale procedural note.

**When:** A later invocation assembles its context projection, and a failure-history query is run over the same store.

**Then:** None of the three enters ordinary reasoning context. All three remain fully visible to the failure-history query, because *what did we try* and *what is true* are different questions.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed refuted, superseded and stale items alongside current ones | Execution log + trace/event references |
| 2 | Assemble a context projection for a later invocation | Execution log + trace/event references |
| 3 | Confirm none of the three appears in it | Execution log + trace/event references |
| 4 | Confirm current items do appear | Execution log + trace/event references |
| 5 | Run a failure-history query over the same store | Execution log + trace/event references |
| 6 | Confirm all three are returned by that query | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] No refuted, superseded or stale item enters the reasoning context
- [ ] Current items do enter — the mask discriminates rather than emptying the context
- [ ] All three remain retrievable by a failure-history query
- [ ] No item was deleted or re-labelled by the mask
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `MemoryMask policy`
- `ContextProjectionRecord`
- `FailedApproach`

## Expected events

- `memory.projection_assembled`
- `memory.item_masked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-096-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-096-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-096-state-before.json` and `ACC-096-state-after.json`.
- `ACC-096-events.json`, `ACC-096-policy-decisions.json` and `ACC-096-audit-export.json`.
- `ACC-096-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test memory items are marked `TEST_CLOSED` and retained in place; the mask is a read policy and changes nothing stored.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
