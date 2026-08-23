# ACC-088 — Strategic Silence Never Silences a Blocker

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-088` |
| Category | Collaboration/Safety |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Safety & Governance Owner |
| Related packages | `WP-150` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Strategic Silence Never Silences a Blocker** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The communication governor is active and one edge has accumulated a low utility history.

**When:** That edge carries a `BLOCKER`, and separately a non-waivable safety message. A low-calibration sender then emits a material finding on the same edge.

**Then:** Neither the blocker nor the safety message can be silenced at any utility threshold. The low-calibration sender's message is not deleted either — its priority and corroboration requirement change.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Drive an edge's utility history to the bottom of the range | Execution log + trace/event references |
| 2 | Emit a `BLOCKER` on that edge | Execution log + trace/event references |
| 3 | Emit a non-waivable safety message on the same edge | Execution log + trace/event references |
| 4 | Emit a material finding from a low-calibration sender | Execution log + trace/event references |
| 5 | Read the governor decision for each | Execution log + trace/event references |
| 6 | Attempt to configure a threshold that would suppress the blocker | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The blocker is delivered regardless of edge utility
- [ ] The non-waivable safety message is delivered regardless of edge utility
- [ ] The low-calibration message is delivered with changed priority and corroboration, not deleted
- [ ] No threshold configuration can suppress a blocker; the attempt is refused
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `CommunicationValue`
- `CommunicationUtilityRecord`
- `TypedAgentMessage`
- `Finding`

## Expected events

- `message.routed`
- `policy.denied`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-088-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-088-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-088-state-before.json` and `ACC-088-state-after.json`.
- `ACC-088-events.json`, `ACC-088-policy-decisions.json` and `ACC-088-audit-export.json`.
- `ACC-088-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test messages are marked `TEST_CLOSED`; the utility history is restored to its baseline.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
