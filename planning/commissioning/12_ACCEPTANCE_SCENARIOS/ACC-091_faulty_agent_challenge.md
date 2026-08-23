# ACC-091 — Faulty Agent Output Does Not Propagate

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-091` |
| Category | Collaboration/Resilience |
| Severity | **Critical** |
| Accountable owner | Incident Commander / SRE Lead |
| Independent witness / verifier | Red Team Lead / Assurance Lead |
| Related packages | `WP-148`, `WP-152` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Faulty Agent Output Does Not Propagate** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** One cohort member is made faulty — it emits confident output that contradicts the evidence it cites.

**When:** The cohort proceeds and a Challenger examines peer output.

**Then:** The faulty output is challenged rather than absorbed, does not reach any canonical record, and the failure is classified and routed. The Challenger's finding does not itself close a gate.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Introduce a faulty member emitting evidence-contradicting output | Execution log + trace/event references |
| 2 | Run the cohort and let the Challenger examine peer output | Execution log + trace/event references |
| 3 | Confirm the faulty output is challenged and does not enter a canonical record | Execution log + trace/event references |
| 4 | Read the `FailureAssessment` class and its routing | Execution log + trace/event references |
| 5 | Attempt to close the gate on the Challenger's finding alone | Execution log + trace/event references |
| 6 | Run a control round with no faulty member | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The faulty output reaches no canonical record
- [ ] The failure is classified and routed to its owning discipline
- [ ] The Challenger's finding does not close a gate
- [ ] The control round does not raise the same finding
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `FailureAssessment`
- `MaterialChallenge`
- `Finding`
- `AgentCohortRecord`

## Expected events

- `failure.assessed`
- `material.challenge.opened`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-091-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-091-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-091-state-before.json` and `ACC-091-state-after.json`.
- `ACC-091-events.json`, `ACC-091-policy-decisions.json` and `ACC-091-audit-export.json`.
- `ACC-091-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The faulty member is removed; the failure record and the challenge history are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
