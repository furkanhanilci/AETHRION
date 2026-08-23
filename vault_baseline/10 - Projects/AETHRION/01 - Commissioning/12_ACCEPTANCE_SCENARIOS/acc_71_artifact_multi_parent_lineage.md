---
title: "ACC-71 — Multi-Parent Artifact Lineage"
aliases:
  - "ACC-71"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Multi-Parent Artifact Lineage situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-71_artifact_multi_parent_lineage.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-71 — Multi-Parent Artifact Lineage

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-71` |
| Category | Data/Integrity |
| Severity | **Critical** |
| Accountable owner | Data Platform Lead |
| Independent witness / verifier | Archivist / Reproducibility Engineer |
| Related packages | `WP-014`, `WP-026`, `WP-030` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Multi-Parent Artifact Lineage** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A synthesis artifact is created from three parent artifacts in a defined order.

**When:** The artifact is exported, the derived graph is dropped and rebuilt, and the canonical store is restored from backup.

**Then:** Parent identity, parent order and every digest are identical across all three operations. A lineage that survives export but not a rebuild is not lineage.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create three parents and a synthesis artifact referencing them in order | Execution log + trace/event references |
| 2 | Export the evidence package and read the recorded parents | Execution log + trace/event references |
| 3 | Drop and rebuild the derived graph projection | Execution log + trace/event references |
| 4 | Restore the canonical store from backup | Execution log + trace/event references |
| 5 | Compare parent lists, order and digests across all three | Execution log + trace/event references |
| 6 | Attempt to overwrite one parent's payload | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The parent list and its order are identical in the canonical store, the export and the rebuilt graph
- [ ] Every digest matches after restore
- [ ] The overwrite attempt is refused
- [ ] No parent is dropped when the synthesis artifact is re-read
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ArtifactRecord`
- `ArtifactManifest`
- `EvidenceManifest`

## Expected events

- `artifact.created`
- `graph.projection_rebuilt`
- `storage.restore_completed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-71-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-71-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-71-state-before.json` and `ACC-71-state-after.json`.
- `ACC-71-events.json`, `ACC-71-policy-decisions.json` and `ACC-71-audit-export.json`.
- `ACC-71-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test artifacts are retained under test retention; nothing is deleted, because deletion is the failure this scenario exists to catch.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
