# ACC-086 — Sparse Topology Preserves Quality

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-086` |
| Category | Collaboration/Efficiency |
| Severity | **High** |
| Accountable owner | Chief Architect |
| Independent witness / verifier | Research Director / Eval Office |
| Related packages | `WP-149`, `WP-150`, `WP-158` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Sparse Topology Preserves Quality** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The same task set is available to a naive fully connected cohort and to an optimised sparse topology, under the same budget, the same benchmark firewall and the same dataset manifest.

**When:** Both arms run to completion.

**Then:** The optimised arm reports a meaningful reduction in coordination cost with quality within the declared tolerance. The comparison is against the fully connected cohort — not against a single agent — and both numbers are reported as a frontier.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze the task set, the budget and the benchmark policy for both arms | Execution log + trace/event references |
| 2 | Run the naive fully connected arm and record its token and quality profile | Execution log + trace/event references |
| 3 | Run the optimised sparse arm under identical conditions | Execution log + trace/event references |
| 4 | Compute coordination overhead ratio for both | Execution log + trace/event references |
| 5 | Compute the quality delta and compare it with the declared tolerance | Execution log + trace/event references |
| 6 | Publish the frontier rather than a single headline number | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Both arms report the same metric schema; no metric exists for only one arm
- [ ] The baseline is the fully connected cohort, and a single-agent arm is not substituted for it
- [ ] The tolerance was frozen in a sealed `EfficiencyQualificationProfile` **before** the holdout was exposed, and the run records that profile's digest
- [ ] Calibration and holdout data do not overlap, and the profile carries the attestation saying so
- [ ] An attempt to edit a threshold after `frozen_at` is refused; a changed threshold requires a new profile version
- [ ] Cost improving while quality exceeds the ceiling FAILS, and cost improving by less than the declared minimum is **not accepted as an efficiency improvement** — two distinct outcomes, neither recordable as a qualified success
- [ ] Coordination cost falls measurably and the quality delta stays within tolerance
- [ ] A quality regression beyond tolerance is reported rather than suppressed
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `CommunicationGraph`
- `TokenLedgerEntry`
- `MetascienceReport`
- `BenchmarkRunPolicy`

## Expected events

- `benchmark.run_completed`
- `metascience.report_published`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-086-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-086-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-086-state-before.json` and `ACC-086-state-after.json`.
- `ACC-086-events.json`, `ACC-086-policy-decisions.json` and `ACC-086-audit-export.json`.
- `ACC-086-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Both arms are marked `TEST_CLOSED`; all metrics and both evidence packages are retained for comparison.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
