# ACC-60 — Failed Smoke Candidate Promotion Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-60` |
| Category | Experiment/Assurance |
| Severity | **Critical** |
| Accountable owner | Experiment Platform Lead |
| Independent witness / verifier | Assurance Lead / Internal Audit |
| Related packages | `WP-083`, `WP-087` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Failed Smoke Candidate Promotion Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A candidate has failed a minimum criterion at the SMOKE tier.

**When:** An agent, and then an ordinary human user, request promotion straight to FULL.

**Then:** Both promotions are refused. Under a CONFIRMATORY study mode the rule is non-waivable; where an exceptional path exists at all it requires an explicit authorised exception with an owner and an expiry, and it is recorded as one.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Run a candidate whose SMOKE result violates a stated minimum | Execution log + trace/event references |
| 2 | Request promotion to VERIFY | Execution log + trace/event references |
| 3 | Request promotion directly to FULL | Execution log + trace/event references |
| 4 | Have a model recommend proceeding in its output and repeat the request | Execution log + trace/event references |
| 5 | Repeat under CONFIRMATORY study mode | Execution log + trace/event references |
| 6 | Exercise the authorised exception path where policy provides one | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every promotion request is refused and produces an `ExperimentPromotionRecord` with decision STOP
- [ ] The model's recommendation does not change the outcome
- [ ] Under CONFIRMATORY the exception path is unavailable, not merely unused
- [ ] Where an exception is taken it carries an owner, a scope and an expiry
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ExperimentPromotionRecord`
- `EvaluationContract`
- `ControlException`
- `Finding`

## Expected events

- `experiment.promotion_refused`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-60-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-60-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-60-state-before.json` and `ACC-60-state-after.json`.
- `ACC-60-events.json`, `ACC-60-policy-decisions.json` and `ACC-60-audit-export.json`.
- `ACC-60-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The candidate and its tiers are marked `TEST_CLOSED`; the promotion records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
