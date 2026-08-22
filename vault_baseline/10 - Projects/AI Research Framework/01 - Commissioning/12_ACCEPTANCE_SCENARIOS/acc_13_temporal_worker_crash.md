# ACC-13 — Temporal Worker Crash

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-13` |
| Category | Reliability/Control |
| Severity | **Critical** |
| Accountable owner | Control Plane Lead |
| Independent witness / verifier | Independent SRE |
| Related packages | `WP-031`, `WP-040`, `WP-111` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Temporal Worker Crash** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An open `ProjectWorkflow` is mid-activity with an idempotent external operation in flight.

**When:** The worker process is killed together with its node and the activity times out and retries.

**Then:** Workflow history and state are not lost; the activity retries and reconciles, no duplicate effect is produced, and a new worker continues.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Start the open workflow and activity fixture | Execution log + trace/event references |
| 2 | Record the pre-commit and post-commit kill points for the external operation | Execution log + trace/event references |
| 3 | Inject the worker and node kill | Execution log + trace/event references |
| 4 | Observe the timeout, retry and the new worker's poll | Execution log + trace/event references |
| 5 | Compare the workflow, gate and artifact state | Execution log + trace/event references |
| 6 | Run the duplicate-effect and audit queries | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Workflow state holds at RPO = 0
- [ ] Exactly one external effect occurred
- [ ] The activity attempt history is visible
- [ ] A new worker resumes the work
- [ ] No unsafe `PASS` transition occurred
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TemporalHistory`
- `ActivityAttempts`
- `ToolReceipt/ArtifactRecord`
- `WorkflowState`
- `FailureInjectionRecord`

## Expected events

- `worker.lost`
- `activity.timed_out`
- `activity.retried_or_reconciled`
- `workflow.resumed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-13-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-13-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-13-state-before.json` and `ACC-13-state-after.json`.
- `ACC-13-events.json`, `ACC-13-policy-decisions.json` and `ACC-13-audit-export.json`.
- `ACC-13-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The fault is removed; worker capacity is restored and the fixture workflow is closed by controlled completion or cancellation.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
