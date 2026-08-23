# ACC-59 — Discovery Search Stagnation

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-59` |
| Category | Discovery/FinOps |
| Severity | **High** |
| Accountable owner | Experiment Platform Lead |
| Independent witness / verifier | FinOps Lead / Assurance Lead |
| Related packages | `WP-100`, `WP-145` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Discovery Search Stagnation** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A discovery campaign runs against a synthetic objective whose frontier stops improving and whose candidate diversity collapses.

**When:** The campaign continues past the configured stagnation window.

**Then:** The detector fires at the configured boundary, the configured action is taken, and the campaign terminates. An unbounded search is impossible even if every model in it recommends continuing.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Configure the stagnation window, the diversity floor and the budget ceiling | Execution log + trace/event references |
| 2 | Run the campaign against a plateau fixture | Execution log + trace/event references |
| 3 | Observe the detector at one iteration before the configured boundary | Execution log + trace/event references |
| 4 | Observe the detector at the boundary itself | Execution log + trace/event references |
| 5 | Let the configured action run to termination | Execution log + trace/event references |
| 6 | Read the stop record and the budget snapshot | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The detector does not fire before the boundary and does fire at it
- [ ] The configured action is the one recorded in `SearchPolicyConfig`, not a model's preference
- [ ] The campaign terminates with reason `STOPPED_BY_STAGNATION` or `STOPPED_BY_BUDGET`
- [ ] The stop record is not an acceptance and satisfies no gate
- [ ] The same snapshot and configuration produce the same decision on replay
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SearchPolicyConfig`
- `CampaignStopRecord`
- `ResearchBudgetContract`
- `SearchExperience`

## Expected events

- `search.stagnation_detected`
- `search.campaign_stopped`
- `budget.snapshot_recorded`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-59-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-59-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-59-state-before.json` and `ACC-59-state-after.json`.
- `ACC-59-events.json`, `ACC-59-policy-decisions.json` and `ACC-59-audit-export.json`.
- `ACC-59-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; its search experience records are retained for the memory tests.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
