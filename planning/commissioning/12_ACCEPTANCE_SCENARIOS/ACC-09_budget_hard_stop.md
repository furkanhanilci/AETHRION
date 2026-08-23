# ACC-09 — Budget Hard Stop

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-09` |
| Category | FinOps/Reliability |
| Severity | **Critical** |
| Accountable owner | FinOps Lead |
| Independent witness / verifier | Project Decision Owner / SRE |
| Related packages | `WP-041`, `WP-045`, `WP-053`, `WP-060`, `WP-083`, `WP-100`, `WP-104`, `WP-111`, `WP-145` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Budget Hard Stop** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A C3 fan-out or experiment batch has approached 80% of its budget and the next job would exceed the 100% hard limit.

**When:** A new expensive model or compute reservation is requested and a concurrent retry is attempted.

**Then:** An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed the `BudgetEnvelope` and the cost fixture | Execution log + trace/event references |
| 2 | Run the call that crosses 80% | Execution log + trace/event references |
| 3 | Send parallel requests that exceed the hard limit | Execution log + trace/event references |
| 4 | Observe the Temporal, Kueue and gateway states | Execution log + trace/event references |
| 5 | Check the owner budget decision queue | Execution log + trace/event references |
| 6 | Release and reconcile the reservation | Execution log + trace/event references |
| 7 | Drive the budget through each communication degradation threshold and confirm the cohort and assurance route are unchanged | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The 80% event fires exactly once
- [ ] New expensive calls or jobs after the hard limit number 0
- [ ] The workflow is `PAUSED`/`BUDGET_BLOCKED`
- [ ] Existing artifacts and checkpoints are intact
- [ ] Cost events are idempotent
- [ ] Budget pressure degrades **communication verbosity** through its declared ladder and never reduces the cohort or lowers the assurance route — ACC-099.
- [ ] Reserved verification, reproduction and assurance budget is unreachable from the exploration path — ACC-101.
- [ ] A `BLOCKER` or non-waivable safety message is delivered at any utility threshold — ACC-088.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

The original scenario stopped expensive work at a hard limit. The reliability layer adds what happens *before* the limit, and the rule that matters is what degradation may not touch — WP-153.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `BudgetEnvelope`
- `ReservationRecords`
- `Route/Queue PolicyDecisions`
- `WorkflowState`
- `CostLedgerEntries`

## Expected events

- `budget.threshold_80`
- `budget.exhausted`
- `workflow.paused`
- `decision.required`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-09-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-09-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-09-state-before.json` and `ACC-09-state-after.json`.
- `ACC-09-events.json`, `ACC-09-policy-decisions.json` and `ACC-09-audit-export.json`.
- `ACC-09-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test reservations are released; the `BudgetEnvelope` is marked `TEST_CLOSED` and ledger entries move to the test cost centre.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
