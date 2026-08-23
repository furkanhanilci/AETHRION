# ACC-70 — EvidenceGap Lifecycle

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-70` |
| Category | Evidence/Knowledge |
| Severity | **High** |
| Accountable owner | Evidence Lead |
| Independent witness / verifier | Knowledge Lead / Assurance Lead |
| Related packages | `WP-075`, `WP-077`, `WP-146` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **EvidenceGap Lifecycle** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An `EvidenceGap` is open with an explicit required evidence type and acceptance condition.

**When:** Evidence of the right type but failing the acceptance condition is offered, then qualifying evidence is offered, and later the source behind that evidence is retracted.

**Then:** The wrong evidence does not close the gap; the qualifying evidence satisfies it; the retraction reopens it with its full history intact. An open gap never authorises work by itself.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Open a gap with a typed acceptance condition | Execution log + trace/event references |
| 2 | Offer evidence of the right type that fails the condition | Execution log + trace/event references |
| 3 | Offer qualifying evidence and observe the transition to SATISFIED | Execution log + trace/event references |
| 4 | Retract the underlying source | Execution log + trace/event references |
| 5 | Observe the reopening and read the gap's history | Execution log + trace/event references |
| 6 | Confirm the open gap started no task on its own | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The non-qualifying evidence leaves the gap OPEN
- [ ] The qualifying evidence moves it to SATISFIED and records what satisfied it
- [ ] The retraction reopens it without erasing the prior satisfaction
- [ ] No task was created by the gap outside gate policy and task compilation
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `EvidenceGap`
- `EvidenceSpan`
- `SourceRecord`
- `ImpactScan`

## Expected events

- `evidence.gap_opened`
- `evidence.gap_satisfied`
- `evidence.gap_reopened`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-70-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-70-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-70-state-before.json` and `ACC-70-state-after.json`.
- `ACC-70-events.json`, `ACC-70-policy-decisions.json` and `ACC-70-audit-export.json`.
- `ACC-70-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test gap is marked `TEST_CLOSED`; its full lifecycle history is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
