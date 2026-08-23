# ACC-113 — Producer to Evaluator Leakage

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-113` |
| Category | Security/Evidence |
| Severity | **Critical** |
| Accountable owner | Execution Security Lead |
| Independent witness / verifier | Reproducibility Lead / Red Team Lead |
| Related packages | `WP-084`, `WP-157` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Producer to Evaluator Leakage** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Producer and evaluator zones are configured, and the quiet leakage paths are available: a shared cache, an inherited credential, a warm container layer.

**When:** The producer attempts to reach evaluator state through each.

**Then:** Every path is closed. None of them looks like a boundary violation in a log, which is why each is tested explicitly rather than inferred from the zone configuration.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed the evaluator zone with a canary reachable only from inside it | Execution log + trace/event references |
| 2 | Attempt access through a shared cache | Execution log + trace/event references |
| 3 | Attempt access through an inherited credential | Execution log + trace/event references |
| 4 | Attempt access through a warm container layer | Execution log + trace/event references |
| 5 | Attempt access through a shared temporary directory | Execution log + trace/event references |
| 6 | Scan every producer artifact, log and trace for the canary | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every leakage path is closed and audited
- [ ] The canary appears in zero producer artifacts, logs or traces
- [ ] A boundary breach invalidates the run rather than lowering its score
- [ ] The zone configuration alone is not accepted as evidence — each path is tested
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `CandidateWorkspace`
- `ExecutionProfile`
- `PolicyDecision`
- `Finding`

## Expected events

- `policy.denied`
- `execution.boundary_violation_attempted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-113-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-113-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-113-state-before.json` and `ACC-113-state-after.json`.
- `ACC-113-events.json`, `ACC-113-policy-decisions.json` and `ACC-113-audit-export.json`.
- `ACC-113-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The canary is rotated; zones are rebuilt from baseline; attempt records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
