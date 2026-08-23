# ACC-116 — Distributional Reproduction for a Hosted Model

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-116` |
| Category | Evidence/Reproduction |
| Severity | **High** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | Methodologist / Assurance Lead |
| Related packages | `WP-085`, `WP-157` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Distributional Reproduction for a Hosted Model** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A result depends on a hosted black-box model, and the protocol declares a run count and an interval in advance.

**When:** The reproduction is attempted at each of the five levels.

**Then:** `EXACT` is refused for hosted black-box execution. The distributional claim uses the pre-declared run count and interval, and choosing them after seeing the spread is refused.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Attempt an `EXACT` reproduction claim against a hosted black-box model | Execution log + trace/event references |
| 2 | Confirm it is refused and the reason names the substrate | Execution log + trace/event references |
| 3 | Execute the pre-declared number of runs | Execution log + trace/event references |
| 4 | Compute the distribution and compare against the declared interval | Execution log + trace/event references |
| 5 | Attempt to widen the interval after seeing the spread | Execution log + trace/event references |
| 6 | Attempt to add runs after seeing the spread | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] `EXACT` is refused for hosted black-box execution
- [ ] The distributional claim uses the pre-declared run count and interval
- [ ] Widening the interval after the fact is refused and recorded as an attempt
- [ ] Adding runs after the fact is refused
- [ ] The asserted level is the one the substrate can support
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ModelExecutionFingerprint`
- `ReproductionRun`
- `ClaimConsistencyReport`
- `ProtocolManifest`

## Expected events

- `reproduction.run_completed`
- `reproduction.level_refused`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-116-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-116-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-116-state-before.json` and `ACC-116-state-after.json`.
- `ACC-116-events.json`, `ACC-116-policy-decisions.json` and `ACC-116-audit-export.json`.
- `ACC-116-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test reproductions are marked `TEST_CLOSED`; all runs and the declared protocol are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
