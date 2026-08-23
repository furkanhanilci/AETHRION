# ACC-109 — Verifier Abstention Is a Valid Result

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-109` |
| Category | Assurance/Model |
| Severity | **High** |
| Accountable owner | Eval Office |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-044`, `WP-155` |
| Acceptance phase | `PRE_GO_LIVE` |
| Recurring counterpart | `WP-126` · WP-126 runs the recurring abstention-rate recalibration in Day-2 |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Verifier Abstention Is a Valid Result** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A qualified V2 verifier is presented with a genuinely ambiguous case from the calibration set, and separately with unambiguous positive and negative cases.

**When:** Each is verified.

**Then:** The ambiguous case yields `ABSTAIN`, which escalates rather than passing or failing. The unambiguous cases yield verdicts. A verifier that never abstains on the ambiguous set fails qualification.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Present the ambiguous calibration case | Execution log + trace/event references |
| 2 | Confirm the result is `ABSTAIN` and that it escalates | Execution log + trace/event references |
| 3 | Confirm abstention does not satisfy the required verification | Execution log + trace/event references |
| 4 | Present unambiguous positive and negative cases | Execution log + trace/event references |
| 5 | Confirm both yield verdicts | Execution log + trace/event references |
| 6 | Qualify a verifier that never abstains and read its qualification outcome | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The ambiguous case yields `ABSTAIN` and escalates
- [ ] Abstention satisfies no required verification and is not recorded as a failure
- [ ] The unambiguous cases yield verdicts — the verifier is not merely abstaining everywhere
- [ ] A verifier that never abstains on the ambiguous set fails qualification
- [ ] Abstention rate is recorded as a qualification metric
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerificationResult`
- `VerifierQualificationRecord`
- `GateRecord`

## Expected events

- `verifier.abstained`
- `verification.inconclusive`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-109-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-109-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-109-state-before.json` and `ACC-109-state-after.json`.
- `ACC-109-events.json`, `ACC-109-policy-decisions.json` and `ACC-109-audit-export.json`.
- `ACC-109-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test verifications are marked `TEST_CLOSED`; the calibration set is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
