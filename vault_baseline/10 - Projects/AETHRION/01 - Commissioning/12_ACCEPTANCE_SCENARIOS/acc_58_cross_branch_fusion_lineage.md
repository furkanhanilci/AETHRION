---
title: "ACC-58 — Cross-Branch Fusion Lineage"
aliases:
  - "ACC-58"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Cross-Branch Fusion Lineage situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-58_cross_branch_fusion_lineage.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-58 — Cross-Branch Fusion Lineage

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-58` |
| Category | Discovery/Evidence |
| Severity | **High** |
| Accountable owner | Experiment Platform Lead |
| Independent witness / verifier | Reproducibility Engineer / Chief Architect |
| Related packages | `WP-014`, `WP-144`, `WP-145` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Cross-Branch Fusion Lineage** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Search nodes A and C sit on different branches and carry distinct useful mechanisms.

**When:** A fusion candidate D is created from A and C, executed, and its result is carried through to a publication evidence export.

**Then:** D retains both input references and the named inherited mechanisms end to end — in the canonical graph, after a derived-graph rebuild, and in the export. Neither A nor C is modified.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create branches containing A and C with distinct mechanism tags | Execution log + trace/event references |
| 2 | Propose a fusion naming which mechanism is inherited from which parent | Execution log + trace/event references |
| 3 | Create node D as a `FUSE` node and execute it | Execution log + trace/event references |
| 4 | Export the evidence package for D's result | Execution log + trace/event references |
| 5 | Drop and rebuild the derived discovery graph | Execution log + trace/event references |
| 6 | Compare A's and C's artifact digests before and after | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] D carries exactly two `FUSION_INPUT` edges, to A and to C
- [ ] Each inherited mechanism names its source node
- [ ] A `FUSE` node created with fewer than two inputs is refused
- [ ] A's and C's artifact digests are unchanged
- [ ] The rebuilt graph and the export both still show the full fusion lineage
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SearchNode`
- `SearchEdge`
- `FusionProposal`
- `ArtifactRecord`
- `ExperimentRun`

## Expected events

- `search.node_created`
- `search.fusion_proposed`
- `graph.projection_rebuilt`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-58-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-58-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-58-state-before.json` and `ACC-58-state-after.json`.
- `ACC-58-events.json`, `ACC-58-policy-decisions.json` and `ACC-58-audit-export.json`.
- `ACC-58-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test campaign is closed; nodes and artifacts are retained under test retention and are not pruned.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
