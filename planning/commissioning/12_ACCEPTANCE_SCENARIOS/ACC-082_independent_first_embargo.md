# ACC-082 — Independent-First Embargo

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-082` |
| Category | Collaboration/Assurance |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Internal Audit / Research Director |
| Related packages | `WP-148`, `WP-149` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Independent-First Embargo** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A cohort is compiled and round zero is in progress; no member has submitted an `InitialPositionArtifact`.

**When:** One member requests another's output, then the same member requests it again after all positions are sealed.

**Then:** The pre-seal request is denied and audited. The post-seal request succeeds through the protocol path, and only the material differences are exposed rather than the full prior output.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Compile a cohort and open round zero | Execution log + trace/event references |
| 2 | Request a peer's output before any position is sealed | Execution log + trace/event references |
| 3 | Seal all initial positions and capture their digests | Execution log + trace/event references |
| 4 | Repeat the request through the protocol path | Execution log + trace/event references |
| 5 | Confirm the exposure carries material deltas, not the full prior output | Execution log + trace/event references |
| 6 | Re-read each sealed artifact and compare digests | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The pre-seal request is denied and appears in the audit trail
- [ ] Every initial position is sealed before any exposure occurs
- [ ] Sealed artifact digests are unchanged after the exposure
- [ ] The exposure is a material delta, not a transcript
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `InitialPositionArtifact`
- `AgentCohortRecord`
- `MaterialChallenge`
- `AuditEntry`

## Expected events

- `cohort.round_zero_sealed`
- `collaboration.access_denied`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-082-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-082-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-082-state-before.json` and `ACC-082-state-after.json`.
- `ACC-082-events.json`, `ACC-082-policy-decisions.json` and `ACC-082-audit-export.json`.
- `ACC-082-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The round is marked `TEST_CLOSED`; sealed positions and the denial records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
