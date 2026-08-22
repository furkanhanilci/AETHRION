# ACC-12 — Duplicate Event Delivery

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-12` |
| Category | Reliability/Event |
| Severity | **Critical** |
| Accountable owner | Event Platform Lead |
| Independent witness / verifier | Independent SRE |
| Related packages | `WP-028`, `WP-039`, `WP-111` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Duplicate Event Delivery** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A business mutation event has been published from the canonical record and the consumer idempotency store is intact.

**When:** The same `event_id`/idempotency key is delivered two or more times, and the consumer also crashes after its first commit.

**Then:** Exactly one business effect occurs, the duplicate is acknowledged and audited, and the side effect is not performed a second time.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Produce the canonical record and its outbox event | Execution log + trace/event references |
| 2 | Inject duplicate delivery to the consumer | Execution log + trace/event references |
| 3 | Kill the process after the first business commit but before the ACK | Execution log + trace/event references |
| 4 | Restart the consumer and allow re-delivery | Execution log + trace/event references |
| 5 | Compare the database, external effect, audit trail and offset | Execution log + trace/event references |
| 6 | Repeat under `replay_mode` | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Business effect count = 1
- [ ] Unique idempotency records = 1
- [ ] The ACK follows the canonical commit
- [ ] A replay performs no external mutation
- [ ] The audit trail carries the duplicate disposition
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `OutboxRecord`
- `ConsumerIdempotencyRecord`
- `BusinessRecord`
- `AuditRecord`
- `ConsumerOffset`

## Expected events

- `event.published`
- `consumer.effect_committed`
- `event.duplicate_ignored`
- `event.acked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-12-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-12-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-12-state-before.json` and `ACC-12-state-after.json`.
- `ACC-12-events.json`, `ACC-12-policy-decisions.json` and `ACC-12-audit-export.json`.
- `ACC-12-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test consumer and stream fixtures are removed by scoped cleanup rather than purge; audit and evidence are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
