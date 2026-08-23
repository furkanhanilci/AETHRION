# ACC-72 — Reviewer Isolation Before Review Lock

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-72` |
| Category | Governance/Assurance |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Internal Audit / Eval Office |
| Related packages | `WP-007`, `WP-086`, `WP-088`, `WP-147` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Reviewer Isolation Before Review Lock** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Reviewers A and B hold the same frozen review packet and neither has submitted.

**When:** B requests A's draft review, then queries the producer's search-experience memory, then the review phase advances past the lock.

**Then:** Both requests are denied before the lock. After the lock, the protocol's disclosure step permits the reveal. A scientific council recommendation in the packet is labelled as advice and carries no verdict.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Issue the same frozen packet to A and B | Execution log + trace/event references |
| 2 | Have B request A's unsubmitted review | Execution log + trace/event references |
| 3 | Have B query the producer's search-experience and procedural memory | Execution log + trace/event references |
| 4 | Have a council recommendation appear in the packet and attempt to treat it as a verdict | Execution log + trace/event references |
| 5 | Lock both reviews and advance the phase | Execution log + trace/event references |
| 6 | Repeat B's request for A's review after the lock | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Both pre-lock requests are denied and audited
- [ ] The producer's search memory is not reachable from the reviewer context
- [ ] The council recommendation cannot be recorded as a `ReviewVerdict` or a `GateRecord`
- [ ] The post-lock reveal succeeds through the protocol path
- [ ] The packet contents are identical for A and B
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `FrozenReviewPacket`
- `ReviewFinding`
- `IndependenceProfile`
- `ScientificCouncilSession`

## Expected events

- `review.access_denied`
- `review.locked`
- `review.disclosure_permitted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-72-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-72-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-72-state-before.json` and `ACC-72-state-after.json`.
- `ACC-72-events.json`, `ACC-72-policy-decisions.json` and `ACC-72-audit-export.json`.
- `ACC-72-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test review round is marked `TEST_CLOSED`; the packet, both reviews and the access denials are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
