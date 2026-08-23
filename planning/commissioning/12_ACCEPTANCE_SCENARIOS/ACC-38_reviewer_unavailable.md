# ACC-38 — Critical Reviewer Unavailable

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-38` |
| Category | Assurance/Operations |
| Severity | **High** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Project Decision Owner |
| Related packages | `WP-003`, `WP-007`, `WP-045`, `WP-088`, `WP-105`, `WP-113` |
| Acceptance phase | `PRE_GO_LIVE` — initial qualification |
| Recurring counterpart | `WP-126` · WP-126 runs the recurring reviewer calibration in Day-2 |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Critical Reviewer Unavailable** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** For an R3 artifact, no eligible and available actor exists in the independent, cross-family, human reviewer pool.

**When:** The assignment service requests a reviewer and the SLA expires.

**Then:** Neither the producer, a self-review, nor an ineligible fallback is used; the gate is `BLOCKED` and a human scheduling/escalation item and a capacity signal are produced.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create the R3 review request and the frozen package | Execution log + trace/event references |
| 2 | Mark every eligible reviewer unavailable | Execution log + trace/event references |
| 3 | Run the assignment and routing attempts | Execution log + trace/event references |
| 4 | Observe the SLA timeout and escalation | Execution log + trace/event references |
| 5 | Attempt to bypass by assigning the producer or an ineligible model | Execution log + trace/event references |
| 6 | Make a reviewer available and complete the new assignment | Execution log + trace/event references |
| 7 | Repeat with a verifier that abstains rather than one that is unavailable, and confirm both escalate | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] No self-assignment or ineligible assignment occurs
- [ ] The gate is `BLOCKED`, never `PASS`
- [ ] SLA escalation and a capacity metric are produced
- [ ] The frozen package is unchanged throughout
- [ ] The later eligible review is valid
- [ ] An unavailable reviewer is one case of a general rule: **abstention and unavailability escalate and never approve** — ACC-109.
- [ ] A route is not lowered because the queue is long or a reviewer is missing — ACC-108.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

Baseline v1.3.0 adds a verdict that looks like unavailability and is not — `ABSTAIN` is a calibrated verifier saying it cannot tell, and it must escalate rather than pass — `ADR-015`.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `ReviewRequest`
- `AssignmentDecisions`
- `Workflow/GateState`
- `EscalationRecord`
- `CapacitySignal`

## Expected events

- `review.no_eligible_reviewer`
- `workflow.blocked`
- `assurance.capacity_alert`
- `review.assignment_created`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-38-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-38-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-38-state-before.json` and `ACC-38-state-after.json`.
- `ACC-38-events.json`, `ACC-38-policy-decisions.json` and `ACC-38-audit-export.json`.
- `ACC-38-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The availability fixture returns to baseline; the blocked test request closes through a valid review or a controlled cancellation.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
