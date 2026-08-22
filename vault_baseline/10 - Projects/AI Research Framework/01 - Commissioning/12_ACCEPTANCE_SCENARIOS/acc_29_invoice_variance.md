# ACC-29 — Provider Invoice Variance

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-29` |
| Category | FinOps |
| Severity | **Medium** |
| Accountable owner | FinOps Lead |
| Independent witness / verifier | Internal Audit |
| Related packages | `WP-100`, `WP-111` |
| Acceptance phase | `PRE_GO_LIVE` — initial qualification |
| Recurring counterpart | `WP-127` · WP-127 runs the recurring FinOps review of the same measure in Day-2 |
| Production acceptance | A Medium scenario may be deferred with a named owner and an expiry date |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Provider Invoice Variance** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The provider invoice total differs from the Cost Ledger accrual by more than the policy threshold.

**When:** The monthly reconciliation job compares the invoice against the usage and cost events.

**Then:** A `VarianceCase` opens with a provider/project/model/time-bucket breakdown, an owner, an SLA and an adjustment or dispute path; ledger history is never deleted.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed the synthetic usage and cost events and a differing invoice | Execution log + trace/event references |
| 2 | Run currency, rate and time-zone normalisation | Execution log + trace/event references |
| 3 | Apply the reconciliation and its threshold | Execution log + trace/event references |
| 4 | Analyse missing and duplicate usage buckets | Execution log + trace/event references |
| 5 | Produce the `VarianceCase` owner and disposition | Execution log + trace/event references |
| 6 | Test the adjustment entry and case closure | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The variance is detected at the threshold
- [ ] No destructive ledger rewrite occurs
- [ ] The adjustment references the original entries
- [ ] Owner, SLA and audit records are complete
- [ ] The variance is visible on the dashboard
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `InvoiceRecord`
- `CostLedgerEntries`
- `VarianceCase`
- `AdjustmentEntry`
- `DecisionRecord`

## Expected events

- `invoice.ingested`
- `cost.variance_detected`
- `reconciliation.case_opened`
- `cost.adjusted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-29-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-29-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-29-state-before.json` and `ACC-29-state-after.json`.
- `ACC-29-events.json`, `ACC-29-policy-decisions.json` and `ACC-29-audit-export.json`.
- `ACC-29-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The synthetic invoice and cost centre are marked `TEST_CLOSED`; financial audit evidence is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
