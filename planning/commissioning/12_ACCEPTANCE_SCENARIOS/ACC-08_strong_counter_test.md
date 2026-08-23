# ACC-08 — Strong Counter-Test

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-08` |
| Category | Research/Assurance |
| Severity | **Critical** |
| Accountable owner | Falsification Lead |
| Independent witness / verifier | Assurance Lead / Arbiter |
| Related packages | `WP-018`, `WP-036`, `WP-075`, `WP-077`, `WP-087`, `WP-088`, `WP-089`, `WP-095`, `WP-104`, `WP-105`, `WP-110` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Strong Counter-Test** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Three reviewers have returned `PASS`, but a pre-registered deterministic counter-test holds a fixture that refutes the claim.

**When:** The **V1 computational verifier** runs the counter-test against the frozen target — deterministic re-execution under pinned software and configuration, not a model reading the result.

**Then:** The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Produce the fixture of PASS `ReviewRecord`s | Execution log + trace/event references |
| 2 | Pin the frozen target and the counter-test hash | Execution log + trace/event references |
| 3 | Run the test through the Verification Engine | Execution log + trace/event references |
| 4 | Put the finding through structural and reproducer validation | Execution log + trace/event references |
| 5 | Run disagreement handling and arbitration | Execution log + trace/event references |
| 6 | Verify the gate and claim disposition | Execution log + trace/event references |
| 7 | Run the counter-test inside a cohort and leave one member's objection unanswered | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The counter-test failure becomes a `VALIDATED` finding
- [ ] The G6 verdict is not `PASS`
- [ ] The claim state is `CHALLENGED` or `REJECTED`
- [ ] The arbiter records an evidence rationale
- [ ] Review count remains an anti-metric, never a justification
- [ ] A **material challenge cannot be closed by majority agreement**, and a counter-test left unanswered blocks convergence — ACC-090.
- [ ] The sycophancy diagnostic reports agreement-before-evidence, so a cohort that converged without engaging is visible rather than merely fast.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

The strong counter-test was a single-actor discipline. Inside a cohort it acquires a second failure mode — everyone agreeing the counter-test is unnecessary — which CONSENSAGENT frames as sycophancy and WP-148 makes structurally hard.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `VerificationRecord`
- `ValidatedFinding`
- `DisagreementCase`
- `ClaimAssessment`
- `GateRecord`

## Expected events

- `counter_test.failed`
- `finding.validated`
- `disagreement.opened`
- `claim.challenged`
- `gate.blocked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-08-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-08-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-08-state-before.json` and `ACC-08-state-after.json`.
- `ACC-08-events.json`, `ACC-08-policy-decisions.json` and `ACC-08-audit-export.json`.
- `ACC-08-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The fixture claim is archived as `TEST_CHALLENGED`; an anonymised finding is added to the reviewer calibration dataset.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
