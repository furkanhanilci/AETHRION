# ACC-119 — Destructive Projection Rebuild

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-119` |
| Category | Data/Integrity |
| Severity | **Critical** |
| Accountable owner | Data Platform Lead |
| Independent witness / verifier | SRE Lead / Archivist |
| Related packages | `WP-030`, `WP-159` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Destructive Projection Rebuild** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Derived projections hold the graph, the vector index and the search index over canonical scientific state.

**When:** Every projection is destroyed and rebuilt from canonical stores, and the split-brain injections are run.

**Then:** The rebuild is lossless. No injection produces a silent divergence: each ends with canonical state correct and the projection agreeing, or with an explicit recorded failure.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Capture canonical state and every projection | Execution log + trace/event references |
| 2 | Destroy all derived projections | Execution log + trace/event references |
| 3 | Rebuild from canonical stores and compare | Execution log + trace/event references |
| 4 | Kill the publisher after a database commit and observe recovery | Execution log + trace/event references |
| 5 | Deliver an event twice and out of order | Execution log + trace/event references |
| 6 | Attempt two concurrent gate transitions on one project | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The rebuild is lossless against the captured comparison
- [ ] No injection produces a silent divergence
- [ ] A duplicate or out-of-order event changes no canonical state
- [ ] Only one of two concurrent gate transitions succeeds, and the other is refused explicitly
- [ ] The correlation chain remains intact across every injection
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ArtifactRecord`
- `ClaimVersion`
- `GateRecord`
- `OutboxRecord`

## Expected events

- `graph.projection_rebuilt`
- `event.duplicate_detected`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-119-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-119-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-119-state-before.json` and `ACC-119-state-after.json`.
- `ACC-119-events.json`, `ACC-119-policy-decisions.json` and `ACC-119-audit-export.json`.
- `ACC-119-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Projections are left rebuilt and verified; canonical state is untouched throughout — that is the property under test.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
