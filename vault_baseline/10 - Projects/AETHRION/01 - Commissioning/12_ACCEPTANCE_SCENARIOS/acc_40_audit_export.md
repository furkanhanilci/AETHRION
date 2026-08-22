---
title: "ACC-40 — Complete Project Audit Export"
aliases:
  - "ACC-40"
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Complete Project Audit Export situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-40_audit_export.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-40 — Complete Project Audit Export

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-40` |
| Category | Audit/Operations |
| Severity | **Critical** |
| Accountable owner | Internal Audit Lead |
| Independent witness / verifier | Independent Auditor |
| Related packages | `WP-090`, `WP-099`, `WP-106`, `WP-109`, `WP-112`, `WP-114`, `WP-119`, `WP-139` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Complete Project Audit Export** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A project that has passed G0–G10 holds policy, identity, model, tool, source, claim, run, artifact, cost, review, reproduction and decision records.

**When:** An auditor runs the export for a project and time scope, then the offline verifier.

**Then:** The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Take the completed synthetic project and its expected object and event counts | Execution log + trace/event references |
| 2 | Make a least-privilege audit export request | Execution log + trace/event references |
| 3 | Produce the export manifest, objects, hash chain and signature | Execution log + trace/event references |
| 4 | Verify the chain, links and counts with the offline verifier | Execution log + trace/event references |
| 5 | Tamper with or drop a record in one copy and verify again | Execution log + trace/event references |
| 6 | Check access, audit-of-audit and retention | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The complete export verifies
- [ ] The REQ → WP → test/evidence → decision chain is queryable
- [ ] Tampered or missing records are detected
- [ ] The auditor's access is read-only
- [ ] Sensitive fields remain policy-compliant
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `AuditExportManifest`
- `WORMRecords`
- `VerificationReport`
- `AuditAccessRecord`
- `SecurityIncident(tamper fixture)`

## Expected events

- `audit.export_requested`
- `audit.export_created`
- `audit.export_verified`
- `audit.integrity_failed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-40-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-40-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-40-state-before.json` and `ACC-40-state-after.json`.
- `ACC-40-events.json`, `ACC-40-policy-decisions.json` and `ACC-40-audit-export.json`.
- `ACC-40-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The export test copy is securely destroyed; the canonical signed export and audit access are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
