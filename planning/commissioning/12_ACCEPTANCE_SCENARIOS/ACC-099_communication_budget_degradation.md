# ACC-099 — Budget Degrades Communication, Not the Cohort

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-099` |
| Category | FinOps/Collaboration |
| Severity | **Critical** |
| Accountable owner | FinOps Lead |
| Independent witness / verifier | Research Director / Assurance Lead |
| Related packages | `WP-150`, `WP-153` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Budget Degrades Communication, Not the Cohort** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A campaign approaches its communication budget ceiling with its cohort and assurance route fixed.

**When:** The budget continues to fall through each degradation threshold.

**Then:** Communication policy degrades — structured, compressed, pointer-only, silence unless material. The cohort is not reduced, the assurance route is not lowered, and no non-waivable control is skipped.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Configure a campaign with a communication budget and an assurance route | Execution log + trace/event references |
| 2 | Drive spend through each degradation threshold in turn | Execution log + trace/event references |
| 3 | Read the communication policy in force at each | Execution log + trace/event references |
| 4 | Confirm the cohort size is unchanged throughout | Execution log + trace/event references |
| 5 | Confirm the assurance route is unchanged throughout | Execution log + trace/event references |
| 6 | Drive spend to exhaustion and read the terminal state | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Communication degrades through the declared ladder in order
- [ ] The cohort is never reduced by budget pressure
- [ ] The assurance route is never lowered by budget pressure
- [ ] Exhaustion yields `BLOCKED_BUDGET` or a scope-reduction request, never a cheaper completion
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ResearchBudgetContract`
- `TokenLedgerEntry`
- `AgentCohortRecord`
- `CampaignStopRecord`

## Expected events

- `budget.threshold`
- `budget.exhausted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-099-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-099-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-099-state-before.json` and `ACC-099-state-after.json`.
- `ACC-099-events.json`, `ACC-099-policy-decisions.json` and `ACC-099-audit-export.json`.
- `ACC-099-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; the ledger and the stop record are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
