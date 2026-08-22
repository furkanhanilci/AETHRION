# ACC-42 — Harness Starts Without the Skill Bootstrap

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-42` |
| Category | Agent/Skill Governance |
| Severity | **Critical** |
| Accountable owner | Model Platform Lead |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-047`, `WP-048` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Harness Starts Without the Skill Bootstrap** situation.

A registry that is present on disk but absent from the session governs nothing.
This scenario verifies that a harness which cannot load the router skill refuses
to accept work, rather than running unguided and looking identical to a healthy
run.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A harness adapter — Claude Code, Codex, OpenCode, Hermes or the direct worker — configured so that skill discovery fails.

**When:** A task is dispatched to that harness.

**Then:** The adapter refuses the task with an explicit bootstrap failure; it does not fall back to an unguided session, and the refusal is distinguishable in the audit trail from a task that ran and failed.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Dispatch a task to a correctly bootstrapped harness and record the loaded skill list | First-turn transcript + loaded-skill listing |
| 2 | Break skill discovery for that harness | Configuration diff |
| 3 | Dispatch the same task again | Execution log + refusal record |
| 4 | Repeat for every supported harness | Cross-harness matrix |
| 5 | Confirm the audit trail distinguishes 'never started' from 'ran and failed' | Audit export |

## Mandatory invariants and assertions

- [ ] The router skill is present on the first turn of a healthy session, unprompted
- [ ] A harness with broken discovery refuses the task
- [ ] No unguided fallback session is created
- [ ] The refusal is recorded distinctly from an execution failure
- [ ] Every supported harness behaves identically under this test
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TaskContract`
- `HarnessSession`
- `PolicyDecision`
- `Finding`
- `AuditRecord`

## Expected events

- `harness.bootstrap.failed`
- `task.rejected`
- `harness.session.started`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-42-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-42-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-42-state-before.json` and `ACC-42-state-after.json`.
- `ACC-42-events.json`, `ACC-42-policy-decisions.json` and `ACC-42-audit-export.json`.
- `ACC-42-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Harness configuration is restored; refusal and audit records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
