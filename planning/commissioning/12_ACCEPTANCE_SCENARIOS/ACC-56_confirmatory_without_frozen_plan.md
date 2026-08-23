# ACC-56 — Confirmatory Result Without a Frozen Analysis Plan

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-56` |
| Category | Research/Assurance |
| Severity | **Critical** |
| Accountable owner | Research Director |
| Independent witness / verifier | Assurance Lead / Methodologist |
| Related packages | `WP-008`, `WP-081`, `WP-142` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Confirmatory Result Without a Frozen Analysis Plan** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A project declares `StudyMode` CONFIRMATORY, and the `AnalysisPlanManifest` seal carries a timestamp later than the first official outcome.

**When:** The project asks the gate to accept a confirmatory `ClaimVersion`.

**Then:** The gate refuses. The work may be relabelled exploratory only through an explicit, recorded policy decision that lowers the claim ceiling; it can never be relabelled confirmatory afterwards on the same data.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Declare `StudyMode` CONFIRMATORY and record the claim ceiling | Execution log + trace/event references |
| 2 | Produce an official outcome before sealing the analysis plan | Execution log + trace/event references |
| 3 | Seal the analysis plan and compare the two external timestamps | Execution log + trace/event references |
| 4 | Attempt to register a confirmatory `ClaimVersion` | Execution log + trace/event references |
| 5 | Exercise the recorded relabel-to-exploratory path | Execution log + trace/event references |
| 6 | Attempt to relabel the same result confirmatory again | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The confirmatory registration is refused with the timestamp ordering as the stated reason
- [ ] The relabel to exploratory produces a `StudyModeRecord` successor and a deviation record; it does not edit the original
- [ ] The second relabel attempt, back to confirmatory, is refused
- [ ] The external time anchor, not a local clock, decides the ordering
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `StudyModeRecord`
- `AnalysisPlanManifest`
- `ClaimVersion`
- `GateRecord`
- `DeviationRecord`

## Expected events

- `gate.blocked`
- `study_mode.superseded`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-56-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-56-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-56-state-before.json` and `ACC-56-state-after.json`.
- `ACC-56-events.json`, `ACC-56-policy-decisions.json` and `ACC-56-audit-export.json`.
- `ACC-56-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test project is closed; the sealed plan, both timestamps and the deviation record are retained as evidence.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
