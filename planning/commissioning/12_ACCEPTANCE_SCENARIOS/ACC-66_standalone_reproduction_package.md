# ACC-66 — Standalone Reproduction Package

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-66` |
| Category | Evidence/Reproduction |
| Severity | **Critical** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | Reproducibility Engineer / Independent Grader |
| Related packages | `WP-085`, `WP-105` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Standalone Reproduction Package** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A producing agent has emitted a `ReproductionPackage` naming its entrypoint, environment specification, dependency lock, inputs, expected outputs and comparison specification.

**When:** The producing and reproducing agents are removed entirely and a fresh environment is given only the declared package and its permitted inputs.

**Then:** The package executes without any agent present and yields output and comparison artifacts. A package that depends on an undeclared local file fails here rather than silently at grading time.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze the reproduction package and its declared inputs | Execution log + trace/event references |
| 2 | Remove the agents and all agent context from the execution path | Execution log + trace/event references |
| 3 | Execute the package in a fresh environment | Execution log + trace/event references |
| 4 | Repeat with one declared dependency deliberately removed from the manifest | Execution log + trace/event references |
| 5 | Confirm the reproducer cannot reach the producer cache | Execution log + trace/event references |
| 6 | Hand the outputs to the independent grader | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The package runs to completion with no agent in the loop
- [ ] The variant with an undeclared dependency fails, and the failure names the missing declaration
- [ ] The reproducer's attempts to reach the producer cache are denied
- [ ] Grading happens in a third environment, separate from both
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ReproductionPackage`
- `ReproductionRun`
- `AlgorithmUnderstandingRecord`
- `ClaimConsistencyReport`

## Expected events

- `reproduction.package_frozen`
- `reproduction.run_completed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-66-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-66-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-66-state-before.json` and `ACC-66-state-after.json`.
- `ACC-66-events.json`, `ACC-66-policy-decisions.json` and `ACC-66-audit-export.json`.
- `ACC-66-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The reproduction environment is destroyed; the package, its digests and the run outputs are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
