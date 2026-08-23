# ACC-78 — Raw Evidence Versus Interpretation

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-78` |
| Category | Data/Integrity |
| Severity | **Critical** |
| Accountable owner | Evidence Lead |
| Independent witness / verifier | Archivist / Assurance Lead |
| Related packages | `WP-026`, `WP-075`, `WP-077` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Raw Evidence Versus Interpretation** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A `FindingRecord` interprets a set of raw artifacts, and review concludes the interpretation was wrong.

**When:** The finding is revised, and separately a direct edit of the underlying raw artifact is requested.

**Then:** The finding gains a new version; every raw artifact's bytes and digest are unchanged. The direct raw edit is refused. Interpretation is revisable; evidence is not.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Record raw artifacts and a finding that interprets them | Execution log + trace/event references |
| 2 | Capture every raw digest | Execution log + trace/event references |
| 3 | Revise the finding after review | Execution log + trace/event references |
| 4 | Compare the raw digests with the captured values | Execution log + trace/event references |
| 5 | Request a direct edit of a raw artifact | Execution log + trace/event references |
| 6 | Rebuild the finding history from canonical records | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every raw digest is unchanged after the revision
- [ ] The finding has two versions, both retrievable, with the first unmodified
- [ ] The direct raw edit is refused
- [ ] The finding's status change did not alter any `EvidenceSpan`
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `FindingRecord`
- `ArtifactRecord`
- `EvidenceSpan`
- `ClaimVersion`

## Expected events

- `knowledge.finding_versioned`
- `contract.write_refused`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-78-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-78-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-78-state-before.json` and `ACC-78-state-after.json`.
- `ACC-78-events.json`, `ACC-78-policy-decisions.json` and `ACC-78-audit-export.json`.
- `ACC-78-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test findings and artifacts are marked `TEST_CLOSED`; raw artifacts are retained under WORM retention.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
