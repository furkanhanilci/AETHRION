# ACC-35 — Tool Partial Failure

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-35` |
| Category | Tool/Reliability |
| Severity | **Critical** |
| Accountable owner | Tool Platform Lead |
| Independent witness / verifier | SRE / Connector Owner |
| Related packages | `WP-049`, `WP-050`, `WP-111` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Tool Partial Failure** situation. The test runs on the same
release candidate, policy bundle, schema bundle and environment manifest as
every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A reversible external write succeeds, but a timeout or connection loss prevents the response from reaching the broker.

**When:** The broker receives a retry request.

**Then:** A blind retry does not produce a second side effect; a read and reconcile finds the remote effect, and exactly one `ToolReceipt` is finalized — or the call becomes `RECONCILIATION_REQUIRED`.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the external fixture endpoint and the idempotency key | Execution log + trace/event references |
| 2 | Inject a response drop after the write succeeds | Execution log + trace/event references |
| 3 | Collect the broker's timeout state | Execution log + trace/event references |
| 4 | Retry the same invocation | Execution log + trace/event references |
| 5 | Run the remote read and reconciliation | Execution log + trace/event references |
| 6 | Verify effect count, receipt, outbox and audit records | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] External effect count = 1
- [ ] The uncertain state is explicit rather than assumed
- [ ] Reconciliation locates the effect
- [ ] Exactly one finalized receipt and event exist
- [ ] No silent success is recorded before the evidence arrives
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ToolInvocation`
- `IdempotencyRecord`
- `ToolReceipt`
- `ReconciliationCase`
- `OutboxRecord`

## Expected events

- `tool.invocation_started`
- `tool.response_unknown`
- `reconciliation.started`
- `tool.effect_confirmed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-35-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-35-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-35-state-before.json` and `ACC-35-state-after.json`.
- `ACC-35-events.json`, `ACC-35-policy-decisions.json` and `ACC-35-audit-export.json`.
- `ACC-35-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The external test effect is compensated or deleted; the reconciliation case is `TEST_CLOSED`.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
