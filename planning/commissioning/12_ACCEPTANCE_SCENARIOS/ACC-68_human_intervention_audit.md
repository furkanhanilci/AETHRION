# ACC-68 — Human Intervention Without an Audit Record

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-68` |
| Category | Governance/Audit |
| Severity | **Critical** |
| Accountable owner | Governance Lead |
| Independent witness / verifier | Internal Audit / Safety & Governance Owner |
| Related packages | `WP-038`, `WP-093`, `WP-099` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Human Intervention Without an Audit Record** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A human edits a claim, a gate condition or a publication assertion through the UI and through the API.

**When:** The audit store is made to fail during the same transaction.

**Then:** The edit fails and rolls back. There is no path by which a human action changes canonical state without an atomically written `HumanInterventionRecord` carrying before and after references.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Perform an edit through the UI and read the intervention record | Execution log + trace/event references |
| 2 | Perform the same edit through the API | Execution log + trace/event references |
| 3 | Inject an audit-store failure and repeat the edit | Execution log + trace/event references |
| 4 | Attempt an edit through the underlying store directly | Execution log + trace/event references |
| 5 | Exercise a rollback and read how the previous state was restored | Execution log + trace/event references |
| 6 | Compare canonical state before and after the failed attempt | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every successful edit has exactly one `HumanInterventionRecord` with before and after references
- [ ] The edit made during the audit failure is rolled back; canonical state is unchanged
- [ ] The direct store edit is refused
- [ ] Rollback restores through an explicit compensation record, never by deleting history
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `HumanInterventionRecord`
- `DecisionRecord`
- `AuditEntry`
- `CompensationRecord`

## Expected events

- `human.intervention_recorded`
- `transaction.rolled_back`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-68-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-68-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-68-state-before.json` and `ACC-68-state-after.json`.
- `ACC-68-events.json`, `ACC-68-policy-decisions.json` and `ACC-68-audit-export.json`.
- `ACC-68-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test interventions are marked `TEST_CLOSED`; the audit entries are retained permanently.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
