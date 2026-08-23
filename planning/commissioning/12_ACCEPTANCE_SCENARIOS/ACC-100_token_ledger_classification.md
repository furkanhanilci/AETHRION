# ACC-100 — Token Ledger Classification

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-100` |
| Category | FinOps/Observability |
| Severity | **High** |
| Accountable owner | FinOps Lead |
| Independent witness / verifier | AI Observability Lead |
| Related packages | `WP-100`, `WP-153` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Token Ledger Classification** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A campaign runs with agents reasoning, communicating, retrieving evidence, calling tools, verifying and synthesising.

**When:** The token ledger is read at the end of the campaign.

**Then:** Every token carries one of the seven categories, the categories sum to the total, and the coordination overhead ratio is derivable from the ledger rather than estimated.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Run a campaign exercising all seven categories | Execution log + trace/event references |
| 2 | Read the ledger and confirm every entry is categorised | Execution log + trace/event references |
| 3 | Sum the categories and compare with the provider-reported total | Execution log + trace/event references |
| 4 | Derive the coordination overhead ratio | Execution log + trace/event references |
| 5 | Confirm the ratio matches an independent count of inter-agent messages | Execution log + trace/event references |
| 6 | Confirm no entry is uncategorised or double-counted | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every ledger entry carries exactly one category
- [ ] The categories sum to the total with no uncategorised remainder
- [ ] The coordination overhead ratio is derivable, not estimated
- [ ] The derived ratio agrees with an independent message count
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TokenLedgerEntry`
- `CostLedgerEntries`
- `MetascienceReport`

## Expected events

- `budget.threshold`
- `metascience.report_published`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-100-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-100-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-100-state-before.json` and `ACC-100-state-after.json`.
- `ACC-100-events.json`, `ACC-100-policy-decisions.json` and `ACC-100-audit-export.json`.
- `ACC-100-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; ledger entries move to the test cost centre and are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
