# ACC-11 — No Eligible Fallback

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-11` |
| Category | Reliability/Model |
| Severity | **Critical** |
| Accountable owner | Model Platform Lead |
| Independent witness / verifier | Safety Owner |
| Related packages | `WP-041`, `WP-045`, `WP-111` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **No Eligible Fallback** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The primary provider is down and no alternative satisfies the task's D3, data-region, tool, risk and independence requirements.

**When:** The router searches for a fallback.

**Then:** No unsafe route is selected; the task and workflow become `BLOCKED` and a human planning/escalation queue item opens.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create a D3 critical `TaskContract` | Execution log + trace/event references |
| 2 | Inject the primary outage | Execution log + trace/event references |
| 3 | Make each alternative profile ineligible for a different policy reason | Execution log + trace/event references |
| 4 | Collect the router decision and the candidate filtering trace | Execution log + trace/event references |
| 5 | Check the workflow and the decision queue | Execution log + trace/event references |
| 6 | Attempt a policy bypass | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Model call count is 0
- [ ] The `RouteDecision` is `NO_ELIGIBLE_ROUTE`
- [ ] The workflow is `BLOCKED`
- [ ] Every candidate denial rule is visible
- [ ] No bypass or unknown-allow path exists
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `RouteDecision`
- `PolicyDecisions`
- `WorkflowState`
- `DecisionRequest`

## Expected events

- `route.no_eligible_profile`
- `workflow.blocked`
- `decision.required`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-11-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-11-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-11-state-before.json` and `ACC-11-state-after.json`.
- `ACC-11-events.json`, `ACC-11-policy-decisions.json` and `ACC-11-audit-export.json`.
- `ACC-11-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Fault and policy fixtures are cleared; the task is closed as `TEST_CANCELLED`, or as a new attempt once an eligible profile exists.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
