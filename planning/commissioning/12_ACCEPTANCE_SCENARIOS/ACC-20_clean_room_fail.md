# ACC-20 — Clean-Room Reproduction Failure

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-20` |
| Category | Evidence/Reproduction |
| Severity | **Critical** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | Assurance Lead / Methodologist |
| Related packages | `WP-019`, `WP-036`, `WP-077`, `WP-084`, `WP-085`, `WP-105`, `WP-113` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Clean-Room Reproduction Failure** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A frozen claim/run package and a pre-declared tolerance exist; the fixture produces an environment or data mismatch, or a genuine deviation in the result.

**When:** The independent reproduction runs and lands outside tolerance.

**Then:** G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the manifest and the deliberate mismatch fixture | Execution log + trace/event references |
| 2 | Run the clean-room job | Execution log + trace/event references |
| 3 | Record the metric and tolerance failure | Execution log + trace/event references |
| 4 | Perform hash, environment and data diffing and root-cause triage | Execution log + trace/event references |
| 5 | Follow the claim, gate and workflow transition | Execution log + trace/event references |
| 6 | Produce the corrected manifest and the new reproduction plan | Execution log + trace/event references |
| 7 | Attempt the reproduction in five environments of decreasing producer lineage and compare the status awarded | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] G7 is not `PASS`
- [ ] The claim is `CHALLENGED`
- [ ] The original producer and reproduction artifacts are retained
- [ ] The `RootCauseCase` carries an owner and an SLA
- [ ] The G4/G5 return produces a new version
- [ ] Reproduced status is refused by **environment digest lineage**, not by declaration — and the subtle lineages count: cached layers, shared credentials, a shared cache — ACC-114.
- [ ] A run that executes despite failing the independence check is classified as **repeatability**, with its reason recorded, rather than discarded.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

The original failure case was a shared workspace. The reliability layer adds the four cases that do not look like sharing a workspace and are — WP-157.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `ReproductionReport(fail)`
- `ClaimAssessment`
- `GateRecord`
- `RootCauseCase`
- `WorkflowHistory`

## Expected events

- `reproduction.failed`
- `claim.challenged`
- `gate.revise`
- `workflow.returned_to_g4_or_g5`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-20-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-20-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-20-state-before.json` and `ACC-20-state-after.json`.
- `ACC-20-events.json`, `ACC-20-policy-decisions.json` and `ACC-20-audit-export.json`.
- `ACC-20-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The mismatch fixture is closed; the failed report is kept unchanged and the correction proceeds as a new run.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
