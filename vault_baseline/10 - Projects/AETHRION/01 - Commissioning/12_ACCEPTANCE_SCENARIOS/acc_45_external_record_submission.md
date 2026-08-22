---
title: "ACC-45 — Irreversible External Record Submission"
aliases:
  - "ACC-45"
type: acceptance-scenario
category: commissioning
summary: "Minting a persistent identifier or submitting an external record cannot be undone."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-45_external_record_submission.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-45 — Irreversible External Record Submission

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-45` |
| Category | External/Governance |
| Severity | **Critical** |
| Accountable owner | Data Steward |
| Independent witness / verifier | Project Decision Owner |
| Related packages | `WP-138`, `WP-139` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

Minting a persistent identifier or submitting an external record cannot be undone. This scenario verifies
that no such submission occurs without explicit human approval, that a duplicate submission does not mint a
second identifier, and that what was submitted is exactly what was approved.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A prepared external record submission with a resolved persistent identifier request.

**When:** Submission is attempted without human approval, then with it, then repeated.

**Then:** The unapproved attempt is refused; the approved submission produces exactly one identifier; the repeat is idempotent; and the submitted payload hash matches the approved one.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Attempt submission with no approval record | Refusal record |
| 2 | Obtain explicit approval and submit | Submission receipt |
| 3 | Compare the submitted payload hash with the approved payload hash | Hash comparison |
| 4 | Repeat the submission and assert idempotency | Identifier registry |
| 5 | Assert the timestamp anchor covers the submission record | Anchor receipt |

## Mandatory invariants and assertions

- [ ] No external submission occurs without an explicit approval record
- [ ] Exactly one identifier is minted for one approved record
- [ ] The submitted payload hash equals the approved payload hash
- [ ] A repeated submission mints nothing further
- [ ] The submission record is time-anchored
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ExternalRecordSubmission`
- `PersistentIdentifier`
- `ApprovalRecord`
- `AuditRecord`

## Expected events

- `external.submission.refused`
- `external.submission.accepted`
- `identifier.minted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-45-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-45-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-45-state-before.json` and `ACC-45-state-after.json`.
- `ACC-45-events.json`, `ACC-45-policy-decisions.json` and `ACC-45-audit-export.json`.
- `ACC-45-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test submissions use a sandbox registry; identifiers minted there are recorded and never reused in production.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
