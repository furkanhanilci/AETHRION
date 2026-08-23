# ACC-76 — Unsupported Publication Sentence

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-76` |
| Category | Publication/Evidence |
| Severity | **Critical** |
| Accountable owner | Citation Auditor |
| Independent witness / verifier | Assurance Lead / Provenance Curator |
| Related packages | `WP-080`, `WP-087`, `WP-090` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Unsupported Publication Sentence** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A generated sentence cites a real, resolvable source on the right topic, and the cited passage does not actually support what the sentence asserts.

**When:** The citation audit and the publication build run.

**Then:** The reference-existence check passes at V0, and the entailment and scope checks fail at V2. Publication is blocked. A control sentence whose citation genuinely supports it passes both.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed a corpus with a supporting passage and a superficially relevant one | Execution log + trace/event references |
| 2 | Generate one sentence supported by its citation and one that is not | Execution log + trace/event references |
| 3 | Run the V0 reference existence and locator checks | Execution log + trace/event references |
| 4 | Run the V2 entailment and scope checks | Execution log + trace/event references |
| 5 | Add a third sentence whose support exists only in a table or figure | Execution log + trace/event references |
| 6 | Request the publication build | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The V0 checks pass for all three — existence is not support
- [ ] The unsupported sentence fails the V2 entailment check
- [ ] The genuinely supported sentence passes, so the detector discriminates
- [ ] The table-only case is reported as a measured multimodal limitation, not a silent pass
- [ ] The build is blocked while an unsupported factual assertion remains
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `EvidenceTag`
- `PublicationAssertion`
- `VerificationResult`
- `VerifierQualificationRecord`

## Expected events

- `verification.entailment_failed`
- `publication.build_failed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-76-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-76-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-76-state-before.json` and `ACC-76-state-after.json`.
- `ACC-76-events.json`, `ACC-76-policy-decisions.json` and `ACC-76-audit-export.json`.
- `ACC-76-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test corpus and candidate document are marked `TEST_CLOSED`; the verification results are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
