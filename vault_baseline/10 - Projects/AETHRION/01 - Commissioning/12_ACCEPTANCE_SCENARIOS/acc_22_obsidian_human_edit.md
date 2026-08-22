# ACC-22 — Obsidian Human Edit Preservation

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-22` |
| Category | Knowledge |
| Severity | **High** |
| Accountable owner | Knowledge Lead |
| Independent witness / verifier | Knowledge Curator |
| Related packages | `WP-012`, `WP-073`, `WP-074`, `WP-113` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Obsidian Human Edit Preservation** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An Obsidian note contains a human-authored field and a generated block; the human edits their own field concurrently with a generated refresh.

**When:** The projection renderer refreshes the note with new source and claim state.

**Then:** The human field is preserved byte- and semantically; only the generated zone updates, and an unexpected conflict opens a curator case instead of an automatic overwrite.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Take the vault test branch and its base hash | Execution log + trace/event references |
| 2 | Apply an edit to the human zone | Execution log + trace/event references |
| 3 | Emit a canonical claim update event | Execution log + trace/event references |
| 4 | Run the renderer refresh concurrently | Execution log + trace/event references |
| 5 | Check the Git diff, zone parser and link integrity | Execution log + trace/event references |
| 6 | Try the out-of-zone conflict fixture | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Human content is unchanged
- [ ] The generated block carries new provenance and a version
- [ ] Git history is complete
- [ ] A zone conflict opens a case
- [ ] No broken links remain, or they sit in the curator queue
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VaultCommit`
- `ProjectionRecord`
- `HumanPreservationDiff`
- `ConflictCase`
- `LinkIntegrityReport`

## Expected events

- `knowledge.projection.requested`
- `obsidian.generated_updated`
- `human_edit.preserved`
- `reconciliation.required`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-22-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-22-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-22-state-before.json` and `ACC-22-state-after.json`.
- `ACC-22-events.json`, `ACC-22-policy-decisions.json` and `ACC-22-audit-export.json`.
- `ACC-22-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Archive or delete the test branch; the human fixture baseline is kept in Git history under a test tag.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
