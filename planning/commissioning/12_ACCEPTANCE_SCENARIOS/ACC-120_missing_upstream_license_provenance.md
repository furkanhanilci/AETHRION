# ACC-120 — Missing Upstream Licence or Provenance

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-120` |
| Category | Supply Chain |
| Severity | **High** |
| Accountable owner | Supply Chain Security Lead |
| Independent witness / verifier | Engineering Productivity Lead / Internal Audit |
| Related packages | `WP-059`, `WP-141`, `WP-159` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Missing Upstream Licence or Provenance** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An adapted upstream file is introduced without an SPDX header, without a register entry and without a pinned commit; a second, correctly registered file is introduced alongside it.

**When:** Both are submitted for merge and the release checks run.

**Then:** The unregistered file fails admission before merge. The correctly registered one passes. OSV, Scorecard, SLSA provenance and signature verification run over the release, and a dependency with no available fix becomes an owned, expiring residual risk rather than silence.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Introduce an adapted file with no lineage, licence or pin | Execution log + trace/event references |
| 2 | Submit it and read the CI admission result | Execution log + trace/event references |
| 3 | Introduce a correctly registered adapted file and submit it | Execution log + trace/event references |
| 4 | Run OSV-Scanner and OpenSSF Scorecard over the release | Execution log + trace/event references |
| 5 | Verify SLSA provenance and Sigstore signatures on the release artifacts | Execution log + trace/event references |
| 6 | Confirm an unfixable finding becomes an owned residual risk with an expiry | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The unregistered file fails admission before merge
- [ ] The correctly registered file passes — the check discriminates
- [ ] `NOTICE` and the upstream register agree on every adapted file
- [ ] Release artifacts carry verifiable provenance and a checkable signature
- [ ] An unfixable vulnerability is recorded with an owner and an expiry, not suppressed
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `UpstreamLineage`
- `AssimilationCandidate`
- `Finding`
- `ReleaseAttestation`

## Expected events

- `ci.admission_failed`
- `upstream.drift_detected`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-120-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-120-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-120-state-before.json` and `ACC-120-state-after.json`.
- `ACC-120-events.json`, `ACC-120-policy-decisions.json` and `ACC-120-audit-export.json`.
- `ACC-120-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test files are removed from the branch; CI records, scan results and residual-risk entries are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
