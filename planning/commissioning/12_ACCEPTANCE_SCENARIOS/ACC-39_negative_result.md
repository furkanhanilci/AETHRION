# ACC-39 — Negative Research Result

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-39` |
| Category | Research/Portfolio |
| Severity | **Medium** |
| Accountable owner | Scientific Owner |
| Independent witness / verifier | Methodologist / Project Decision Owner |
| Related packages | `WP-035`, `WP-081`, `WP-082`, `WP-083`, `WP-104`, `WP-113` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Medium scenario may be deferred with a named owner and an expiry date |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Negative Research Result** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Under a pre-registered protocol and baseline, the intervention or approach fails to beat the baseline.

**When:** The run, analysis, review and portfolio decision complete.

**Then:** The result is neither lost nor reframed as a success; a negative run and claim artifact, the limitations and a stop/pivot/continue `DecisionRecord` are produced.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the frozen protocol, baseline and stop rule | Execution log + trace/event references |
| 2 | Run a reproducible run that does not beat the baseline | Execution log + trace/event references |
| 3 | Analyse the metrics, uncertainty and robustness | Execution log + trace/event references |
| 4 | Create the claim and the negative-result artifact | Execution log + trace/event references |
| 5 | Run the review and the decision queue | Execution log + trace/event references |
| 6 | Verify the knowledge, Obsidian and portfolio write-back | Execution log + trace/event references |
| 7 | Classify a compile failure, a data failure and a valid null result and confirm only the third can be a negative result | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The run is retained as `FAILED_TO_BEAT_BASELINE`/`NEGATIVE`
- [ ] No post-hoc metric or baseline mutation occurred
- [ ] The decision carries a rationale and a next action
- [ ] The cost is captured
- [ ] The knowledge is searchable afterwards
- [ ] A negative result is now one outcome of a **typed failure taxonomy**: only a validly executed run under the frozen plan can support a `HYPOTHESIS` class — ACC-095.
- [ ] A failed approach is retained and retrievable after the campaign closes, and does not suppress a scientifically distinct retry — ACC-063.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

The original scenario proved a negative result can be published. The reliability layer proves the other three cannot be mistaken for one — WP-152.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `RunManifest`
- `NegativeResultArtifact`
- `ClaimRecord`
- `ReviewRecord`
- `PortfolioDecision`

## Expected events

- `experiment.negative_result`
- `claim.not_supported`
- `decision.required`
- `project.stopped_pivoted_or_continued`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-39-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-39-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-39-state-before.json` and `ACC-39-state-after.json`.
- `ACC-39-events.json`, `ACC-39-policy-decisions.json` and `ACC-39-audit-export.json`.
- `ACC-39-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test project is `CLOSED`/`ARCHIVED`; the negative artifact remains searchable in the test corpus.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
