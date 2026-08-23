# ACC-53 — Unverified Numeric Result

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-53` |
| Category | Publication/Evidence |
| Severity | **Critical** |
| Accountable owner | Provenance Curator |
| Independent witness / verifier | Assurance Lead / Reproducibility Engineer |
| Related packages | `WP-082`, `WP-087`, `WP-090`, `WP-106` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Unverified Numeric Result** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A claim is properly evidenced and its result is registered as a `VerifiedValue` of 87.3%.

**When:** The writer stage emits the same sentence with the figure changed to 89.1%, a number no `VerifiedValue` carries.

**Then:** The build fails regardless of the quality of the surrounding prose; the report lists the value refs that were permitted and the one that was not. A declared rounding or display transform of a registered value passes.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Register a `VerifiedValue` of 87.3% bound to a raw evaluator artifact | Execution log + trace/event references |
| 2 | Render the publication with the substituted figure 89.1% | Execution log + trace/event references |
| 3 | Render a second sentence quoting the same value rounded to 87% | Execution log + trace/event references |
| 4 | Request the final package build | Execution log + trace/event references |
| 5 | Read the number-grounding report | Execution log + trace/event references |
| 6 | Confirm the canonical `VerifiedValue` is unchanged by the attempt | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The build fails and names 89.1% as ungrounded
- [ ] The declared rounding of 87.3% to 87% passes and records its display transform
- [ ] The canonical value and its digest are byte-identical before and after
- [ ] No `VerifiedValue` was created by the writer stage
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerifiedValue`
- `RawEvaluatorArtifact`
- `PublicationAssertion`
- `VerificationResult`

## Expected events

- `publication.build_failed`
- `value.grounding_failed`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-53-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-53-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-53-state-before.json` and `ACC-53-state-after.json`.
- `ACC-53-events.json`, `ACC-53-policy-decisions.json` and `ACC-53-audit-export.json`.
- `ACC-53-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test values are marked `TEST_CLOSED`; the raw evaluator artifact is retained under test retention.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
