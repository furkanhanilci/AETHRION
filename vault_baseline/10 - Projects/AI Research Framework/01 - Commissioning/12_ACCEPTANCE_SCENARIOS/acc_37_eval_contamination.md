# ACC-37 — Evaluation Set Contamination

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-37` |
| Category | Model/Eval/Security |
| Severity | **Critical** |
| Accountable owner | Eval Office |
| Independent witness / verifier | Security / Independent Auditor |
| Related packages | `WP-043`, `WP-060`, `WP-112`, `WP-124` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Evaluation Set Contamination** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A golden evaluation item's canary has been observed in a prompt log, a training/context store or a runtime access path.

**When:** The contamination detector and audit scan raise an alarm.

**Then:** The evaluation bundle is invalidated; the qualification and profile decisions that depended on it are suspended, and a clean set and re-evaluation process opens.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create the golden canary and the access policy baseline | Execution log + trace/event references |
| 2 | Inject the unauthorised exposure fixture | Execution log + trace/event references |
| 3 | Run the trace, store and access audit scan | Execution log + trace/event references |
| 4 | Query the bundle and profile lineage and the affected decisions | Execution log + trace/event references |
| 5 | Run the invalidate, revoke and impact workflow | Execution log + trace/event references |
| 6 | Produce the clean replacement set and the re-evaluation plan | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The contaminated bundle is `INVALIDATED`
- [ ] Affected profiles are suspended
- [ ] Golden store access isolation is restored
- [ ] Historical evaluations are not silently edited
- [ ] The impact assessment and re-evaluation are complete
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `EvalDatasetManifest`
- `ContaminationIncident`
- `CapabilityProfileDecision`
- `ImpactCases`
- `ReplacementPlan`

## Expected events

- `eval.contamination_detected`
- `eval.bundle.invalidated`
- `capability.suspended`
- `requalification.required`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-37-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-37-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-37-state-before.json` and `ACC-37-state-after.json`.
- `ACC-37-events.json`, `ACC-37-policy-decisions.json` and `ACC-37-audit-export.json`.
- `ACC-37-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Exposed fixture stores are sanitised; the canary is rotated and incident evidence is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
