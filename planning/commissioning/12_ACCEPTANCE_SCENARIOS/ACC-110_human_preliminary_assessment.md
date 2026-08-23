# ACC-110 — Human Preliminary Assessment Precedes the Recommendation

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-110` |
| Category | Governance/Human |
| Severity | **Critical** |
| Accountable owner | Project Decision Owner |
| Independent witness / verifier | Safety & Governance Owner / Internal Audit |
| Related packages | `WP-093`, `WP-156` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Human Preliminary Assessment Precedes the Recommendation** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A G8 decision is queued with a completed AI recommendation and a reviewer verdict already available.

**When:** The human opens the decision, through the UI and separately through the API.

**Then:** Neither interface exposes the recommendation before the `HumanPreliminaryAssessment` is sealed. After sealing, the recommendation is revealed and any change produces a `DecisionDelta`.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Queue a decision with a recommendation already computed | Execution log + trace/event references |
| 2 | Open it through the UI and inspect every field returned | Execution log + trace/event references |
| 3 | Attempt to fetch the recommendation through the API before sealing | Execution log + trace/event references |
| 4 | Record and seal the preliminary assessment | Execution log + trace/event references |
| 5 | Reveal the recommendation and change the decision | Execution log + trace/event references |
| 6 | Read the `DecisionDelta` and confirm both states are recorded | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The recommendation is unreachable through the UI before sealing
- [ ] The recommendation is unreachable through the API before sealing
- [ ] The preliminary assessment is immutable once sealed
- [ ] A post-reveal change produces a `DecisionDelta` recording both states
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `HumanPreliminaryAssessment`
- `DecisionDelta`
- `DecisionRecord`
- `AuditEntry`

## Expected events

- `human.preliminary_recorded`
- `decision.recorded`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-110-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-110-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-110-state-before.json` and `ACC-110-state-after.json`.
- `ACC-110-events.json`, `ACC-110-policy-decisions.json` and `ACC-110-audit-export.json`.
- `ACC-110-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test decision is marked `TEST_CLOSED`; the preliminary assessment and the delta are retained permanently.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
