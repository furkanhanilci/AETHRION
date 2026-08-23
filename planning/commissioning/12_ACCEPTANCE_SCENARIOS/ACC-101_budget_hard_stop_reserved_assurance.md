# ACC-101 — Reserved Assurance Budget Is Unreachable

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-101` |
| Category | FinOps/Assurance |
| Severity | **Critical** |
| Accountable owner | FinOps Lead |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-145`, `WP-153` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Reserved Assurance Budget Is Unreachable** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A campaign holds reserved budget for verification, reproduction and the assurance route, and its exploration budget is nearly exhausted.

**When:** Exploration attempts to consume the reserve.

**Then:** The reserve is unreachable from the exploration path. The campaign stops on its exploration ceiling with the reserve intact, and the assurance work it was reserved for can still run.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Configure reserves for verification, reproduction and assurance | Execution log + trace/event references |
| 2 | Drive exploration spend to its ceiling | Execution log + trace/event references |
| 3 | Attempt to consume each reserve from the exploration path | Execution log + trace/event references |
| 4 | Confirm the campaign stops with the reserves intact | Execution log + trace/event references |
| 5 | Run the reserved assurance work and confirm it is affordable | Execution log + trace/event references |
| 6 | Read the stop record and confirm it satisfies no gate | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Each reserve is unreachable from the exploration path
- [ ] The campaign stops on its exploration ceiling with reserves intact
- [ ] The reserved assurance and reproduction work remains affordable afterwards
- [ ] `STOPPED_BY_BUDGET` satisfies no gate
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ResearchBudgetContract`
- `CampaignStopRecord`
- `TokenLedgerEntry`

## Expected events

- `budget.exhausted`
- `search.campaign_stopped`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-101-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-101-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-101-state-before.json` and `ACC-101-state-after.json`.
- `ACC-101-events.json`, `ACC-101-policy-decisions.json` and `ACC-101-audit-export.json`.
- `ACC-101-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; reserves are released to the test cost centre.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
