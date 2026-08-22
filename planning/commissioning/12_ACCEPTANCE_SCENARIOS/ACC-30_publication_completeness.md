# ACC-30 — Publication Completeness

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-30` |
| Category | Publication/Evidence |
| Severity | **Critical** |
| Accountable owner | Provenance Curator |
| Independent witness / verifier | Citation Auditor / Safety |
| Related packages | `WP-080`, `WP-090`, `WP-106`, `WP-113` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Publication Completeness** situation. The test runs on the same
release candidate, policy bundle, schema bundle and environment manifest as
every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A material or critical claim in the publication draft is missing its locator or a complete lineage link.

**When:** The G9 publication builder, citation audit and Verification Engine run.

**Then:** No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the complete baseline draft and package fixture | Execution log + trace/event references |
| 2 | Remove the locator or reference from a critical claim | Execution log + trace/event references |
| 3 | Run the builder, audit, verification and Gate Service | Execution log + trace/event references |
| 4 | Check the release endpoint and the object store | Execution log + trace/event references |
| 5 | Add the missing evidence as a new version | Execution log + trace/event references |
| 6 | Verify the new package build and the retained history of the old draft | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Releases of an incomplete package = 0
- [ ] The G9 failure rule is visible
- [ ] Critical lineage coverage targets 100%
- [ ] The corrected package receives a new version and hash
- [ ] The old failed draft is retained
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `CitationAudit`
- `VerificationRecord`
- `GateRecord`
- `PublicationPackage(draft/final)`
- `CorrectionRecord`

## Expected events

- `publication.validation_failed`
- `gate.revise`
- `claim.evidence_corrected`
- `publication.package_created`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-30-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-30-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-30-state-before.json` and `ACC-30-state-after.json`.
- `ACC-30-events.json`, `ACC-30-policy-decisions.json` and `ACC-30-audit-export.json`.
- `ACC-30-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The final test package is removed from the public endpoint; the archive stays in the TEST namespace.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
