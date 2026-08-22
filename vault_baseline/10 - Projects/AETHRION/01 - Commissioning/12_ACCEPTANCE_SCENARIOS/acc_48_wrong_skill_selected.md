---
title: "ACC-48 — Wrong or Competing Skill Selected"
aliases:
  - "ACC-48"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Wrong or Competing Skill Selected situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-48_wrong_skill_selected.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-48 — Wrong or Competing Skill Selected

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-48` |
| Category | Agent/Skill Governance |
| Severity | **High** |
| Accountable owner | Eval Office |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-013`, `WP-043`, `WP-047` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Wrong or Competing Skill Selected** situation.

Trigger resolution is where the skill layer most plausibly fails quietly: the
agent loads *a* procedure, just not the right one. This scenario measures
resolution rather than assuming it.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A task whose situation matches one skill's trigger, with a second skill whose description overlaps it.

**When:** The compiler resolves `skills_required` and the runtime loads them.

**Then:** The correct skill is selected, the selection reason is recorded, and an unresolvable overlap fails closed rather than picking arbitrarily.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Run the base case and confirm the expected skill is selected | Compiler output + `skill_selection_reason` |
| 2 | Introduce a competing skill with an overlapping trigger | Registry diff |
| 3 | Re-run and record which skill is selected and why | Selection record |
| 4 | Run the confusion matrix across the trigger test set | Trigger confusion matrix |
| 5 | Verify the engineering / scientific / shared family boundary is respected | Policy decision records |

## Mandatory invariants and assertions

- [ ] The selected skill matches the expected skill on the trigger test set
- [ ] Every selection carries a machine-readable `skill_selection_reason`
- [ ] An unresolvable overlap fails closed instead of selecting arbitrarily
- [ ] Family selection follows `work_domain` and is never chosen by the agent
- [ ] The confusion matrix is stored as evidence, not summarised in prose
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SkillBundle`
- `TriggerResolution`
- `PolicyDecision`
- `AuditRecord`

## Expected events

- `skill.selected`
- `skill.selection.ambiguous`
- `policy.denied`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-48-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-48-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-48-state-before.json` and `ACC-48-state-after.json`.
- `ACC-48-events.json`, `ACC-48-policy-decisions.json` and `ACC-48-audit-export.json`.
- `ACC-48-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The competing test skill is removed from the registry; resolution records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
