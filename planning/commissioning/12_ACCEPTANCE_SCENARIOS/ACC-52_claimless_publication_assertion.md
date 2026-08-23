# ACC-52 — Claimless Publication Assertion

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-52` |
| Category | Publication/Evidence |
| Severity | **Critical** |
| Accountable owner | Provenance Curator |
| Independent witness / verifier | Assurance Lead / Publication Owner |
| Related packages | `WP-018`, `WP-080`, `WP-090`, `WP-106`, `WP-113` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Claimless Publication Assertion** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A publication candidate has passed review and contains one factual result sentence that the writer produced without a `ClaimVersion` reference.

**When:** The Publication Compiler is asked to finalise the package.

**Then:** The build fails; the sentence's location and the missing relation are reported; no signed `PublicationPackage` is produced. Prose whose `text_role` declares it structural or editorial is not affected.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed a claim/evidence graph in which every other assertion resolves | Execution log + trace/event references |
| 2 | Insert one factual sentence with no `claim_ref` | Execution log + trace/event references |
| 3 | Insert one heading and one transition sentence marked with a non-factual `text_role` | Execution log + trace/event references |
| 4 | Request the final package build | Execution log + trace/event references |
| 5 | Read the compiler report and locate the failing assertion | Execution log + trace/event references |
| 6 | Confirm that no signed package artifact was written | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The build exits non-zero and names the failing sentence by document location
- [ ] Zero signed `PublicationPackage` artifacts exist after the run
- [ ] The non-factual sentences did not raise a finding — the check discriminates rather than blocking all prose
- [ ] The `PublicationAssertion` records for the passing sentences remain intact and re-resolvable
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `PublicationAssertion`
- `EvidenceTag`
- `ClaimVersion`
- `VerificationResult`
- `Finding`

## Expected events

- `publication.build_requested`
- `publication.build_failed`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-52-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-52-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-52-state-before.json` and `ACC-52-state-after.json`.
- `ACC-52-events.json`, `ACC-52-policy-decisions.json` and `ACC-52-audit-export.json`.
- `ACC-52-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The candidate document and its partial build artifacts move to the test namespace; the seeded claim graph is marked `TEST_CLOSED`.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
