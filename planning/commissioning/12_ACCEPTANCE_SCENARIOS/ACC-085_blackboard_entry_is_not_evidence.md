# ACC-085 — A Blackboard Entry Is Not Evidence

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-085` |
| Category | Collaboration/Evidence |
| Severity | **Critical** |
| Accountable owner | Evidence Lead |
| Independent witness / verifier | Assurance Lead / Internal Audit |
| Related packages | `WP-075`, `WP-149` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **A Blackboard Entry Is Not Evidence** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The blackboard holds entries including a `CONSENSUS_CANDIDATE` that reads like a finding.

**When:** A client attempts to cite that entry as evidence for a claim, and separately to promote it directly to a `ClaimVersion`. The whole blackboard is then deleted.

**Then:** Both attempts are refused. After deletion, no canonical scientific record is lost — everything that mattered was an artifact, a span, a claim or a finding, and the entry only pointed at it.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed a blackboard with entries including a persuasive consensus candidate | Execution log + trace/event references |
| 2 | Attempt to cite an entry as evidence for a claim | Execution log + trace/event references |
| 3 | Attempt to promote the entry directly to a `ClaimVersion` | Execution log + trace/event references |
| 4 | Capture the canonical scientific state | Execution log + trace/event references |
| 5 | Delete the entire blackboard | Execution log + trace/event references |
| 6 | Re-read canonical state and compare | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Citing a blackboard entry as evidence is refused
- [ ] There is no path from an entry to a `ClaimVersion`
- [ ] Deleting the blackboard loses no canonical scientific record
- [ ] Artifact pointers held by deleted entries still resolve from the artifact store
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `BlackboardEntry`
- `ClaimVersion`
- `EvidenceSpan`
- `ArtifactRecord`

## Expected events

- `contract.write_refused`
- `blackboard.purged`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-085-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-085-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-085-state-before.json` and `ACC-085-state-after.json`.
- `ACC-085-events.json`, `ACC-085-policy-decisions.json` and `ACC-085-audit-export.json`.
- `ACC-085-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test blackboard is destroyed deliberately as part of the scenario; canonical records are retained and re-verified afterwards.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
