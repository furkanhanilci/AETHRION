# ACC-75 — Literature Retrieval Budget and Stopping Rule

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-75` |
| Category | Research/Literature |
| Severity | **High** |
| Accountable owner | Knowledge Lead |
| Independent witness / verifier | Citation Auditor / Assurance Lead |
| Related packages | `WP-069`, `WP-071`, `WP-072` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Literature Retrieval Budget and Stopping Rule** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A confirmatory literature campaign runs under a `SearchProtocol` whose stopping rule and query budget were frozen before any result was seen.

**When:** The self-feedback loop repeatedly reports insufficient evidence and requests further expansion, and the campaign then attempts to relax the stopping rule after favourable results appear.

**Then:** The loop halts at the frozen budget, and the attempt to change the stopping rule is refused. The sufficiency assessment is advisory; the protocol is authority.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze a search protocol with an explicit query budget and stopping rule | Execution log + trace/event references |
| 2 | Run the campaign with a fixture that always reports insufficiency | Execution log + trace/event references |
| 3 | Observe the loop at the budget boundary | Execution log + trace/event references |
| 4 | Attempt to raise the budget mid-campaign | Execution log + trace/event references |
| 5 | Attempt to change the stopping rule after seeing results | Execution log + trace/event references |
| 6 | Confirm a planted counter-example is retrieved by the challenge queries | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The loop stops at the frozen budget, not when the model is satisfied
- [ ] The mid-campaign budget increase is refused
- [ ] The post-hoc stopping-rule change is refused and recorded as an attempt
- [ ] The planted counter-evidence is retrieved — the challenge path is a live control, not a declaration
- [ ] Every excluded record carries a reason
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SearchProtocol`
- `LiteratureCampaign`
- `EvidenceSufficiencyAssessment`
- `LiteratureSetManifest`

## Expected events

- `literature.budget_exhausted`
- `literature.protocol_change_refused`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-75-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-75-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-75-state-before.json` and `ACC-75-state-after.json`.
- `ACC-75-events.json`, `ACC-75-policy-decisions.json` and `ACC-75-audit-export.json`.
- `ACC-75-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; the search log, inclusion decisions and frozen manifest are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
