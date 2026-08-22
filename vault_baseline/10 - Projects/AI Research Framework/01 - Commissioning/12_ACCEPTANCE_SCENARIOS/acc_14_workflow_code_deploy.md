# ACC-14 — Workflow Code Deployment and Replay

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-14` |
| Category | Reliability/Control |
| Severity | **Critical** |
| Accountable owner | Platform Assurance Lead |
| Independent witness / verifier | Control Plane Reviewer |
| Related packages | `WP-032`, `WP-040`, `WP-111` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Workflow Code Deployment and Replay** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Open workflow histories exist on the old worker build, paused or active at different gates.

**When:** New workflow code passes through replay CI and versioned deployment.

**Then:** Every golden and open history replays deterministically; an incompatible workflow stays on the appropriate worker version and no state drift occurs.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Snapshot representative histories | Execution log + trace/event references |
| 2 | Run the replay suite against the new build | Execution log + trace/event references |
| 3 | Verify the patch and version-marker paths | Execution log + trace/event references |
| 4 | Deploy a canary worker to the queue | Execution log + trace/event references |
| 5 | Test update, query and activity paths on open workflows | Execution log + trace/event references |
| 6 | Rehearse the old-worker drain and rollback | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Replay errors = 0
- [ ] History-derived state is identical before and after
- [ ] Version markers behave deterministically
- [ ] An incompatible build is not promoted
- [ ] No open workflow is orphaned
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ReplayReport`
- `WorkerBuildManifest`
- `DeploymentRecord`
- `WorkflowStateDiff`

## Expected events

- `workflow.replay.checked`
- `worker.version.deployed`
- `workflow.version_routed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-14-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-14-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-14-state-before.json` and `ACC-14-state-after.json`.
- `ACC-14-events.json`, `ACC-14-policy-decisions.json` and `ACC-14-audit-export.json`.
- `ACC-14-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The canary worker is removed or promoted; the old worker is retained only until its compatible histories complete.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
