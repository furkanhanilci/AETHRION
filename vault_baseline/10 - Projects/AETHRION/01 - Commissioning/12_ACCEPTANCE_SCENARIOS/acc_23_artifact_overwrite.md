---
title: "ACC-23 — Artifact Overwrite Attempt"
aliases:
  - "ACC-23"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Artifact Overwrite Attempt situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-23_artifact_overwrite.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-23 — Artifact Overwrite Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-23` |
| Category | Data/Integrity |
| Severity | **Critical** |
| Accountable owner | Data Platform Lead |
| Independent witness / verifier | Archivist / Security |
| Related packages | `WP-014`, `WP-026`, `WP-087`, `WP-104`, `WP-107`, `WP-113`, `WP-139` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Artifact Overwrite Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A canonical content-addressed URI holds the bytes of hash A; a client attempts to write the bytes of hash B to the same URI/key.

**When:** The object write/finalize or manifest update call is made.

**Then:** The overwrite is rejected; the new bytes can only be written as a new content address and version, and existing references are unchanged.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Upload and finalize artifact A | Execution log + trace/event references |
| 2 | Attempt to upload/overwrite B at the same key | Execution log + trace/event references |
| 3 | Collect the hash mismatch response and audit record | Execution log + trace/event references |
| 4 | Write B under a new content address | Execution log + trace/event references |
| 5 | Query the old run, claim and publication references | Execution log + trace/event references |
| 6 | Run the tamper and integrity scan | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] A's bytes and hash are unchanged
- [ ] The overwrite operation is denied
- [ ] B receives a unique address and version
- [ ] Old references continue to resolve to A
- [ ] The audit trail records the tamper attempt
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ArtifactRecords A/B`
- `ObjectStoreAudit`
- `PolicyDecision`
- `IntegrityScanRecord`

## Expected events

- `artifact.created`
- `artifact.overwrite_denied`
- `artifact.version_created`
- `integrity.checked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-23-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-23-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-23-state-before.json` and `ACC-23-state-after.json`.
- `ACC-23-events.json`, `ACC-23-policy-decisions.json` and `ACC-23-audit-export.json`.
- `ACC-23-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The B test version may be removed under retention policy; A remains as the baseline test artifact.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
