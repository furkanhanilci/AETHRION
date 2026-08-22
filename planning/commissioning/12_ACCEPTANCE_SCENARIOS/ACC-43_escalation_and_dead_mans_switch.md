# ACC-43 — Escalation Timeout and Dead-Man's Switch

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-43` |
| Category | Communication/Governance |
| Severity | **Critical** |
| Accountable owner | Platform Operations Lead |
| Independent witness / verifier | Internal Audit |
| Related packages | `WP-134`, `WP-140` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

The most dangerous failure in a human-in-the-loop system is a timeout quietly becoming an approval. This
scenario drives a decision request past its SLA with no human response and verifies that the system escalates
and fails closed rather than proceeding.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A decision request with an SLA, an escalation ladder, and no human response.

**When:** The SLA expires and the escalation ladder is exhausted.

**Then:** The request expires closed, the gate remains blocked, the dead-man's switch fires, and at no point is the absence of a response treated as consent.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Raise a decision request and let it expire without response | Expiry record |
| 2 | Assert the gate state after expiry | Gate record |
| 3 | Exhaust every rung of the escalation ladder | Escalation trail |
| 4 | Assert the dead-man's switch fired and what it did | Liveness record |
| 5 | Respond after expiry and assert the stale response is rejected | Refusal record |

## Mandatory invariants and assertions

- [ ] A timeout never becomes an approval
- [ ] The gate remains blocked after expiry
- [ ] Every escalation rung is recorded with its timestamp
- [ ] The dead-man's switch fires within its declared window
- [ ] A response arriving after expiry is rejected, not applied
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `DecisionRequest`
- `EscalationRecord`
- `GateRecord`
- `LivenessRecord`
- `AuditRecord`

## Expected events

- `decision.request.expired`
- `escalation.raised`
- `workflow.blocked`
- `liveness.deadman.fired`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-43-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-43-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-43-state-before.json` and `ACC-43-state-after.json`.
- `ACC-43-events.json`, `ACC-43-policy-decisions.json` and `ACC-43-audit-export.json`.
- `ACC-43-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test decision requests are closed as expired; escalation and audit records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
