# ACC-46 — Task Runs With No Skill Loaded

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-46` |
| Category | Agent/Skill Governance |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Internal Audit |
| Related packages | `WP-013`, `WP-046`, `WP-047`, `WP-048` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Task Runs With No Skill Loaded** situation.

A procedure that can be skipped is not governance. The compiler resolves a
non-waivable skill into `skills_required`; this scenario removes it from the
runtime and verifies that the task refuses to proceed rather than proceeding
without it.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A `TaskContract` whose classification resolves at least one non-waivable skill into `skills_required`.

**When:** The runtime starts the task with that skill absent from `skills_loaded`.

**Then:** The task is blocked before any production step, the divergence between `skills_required` and `skills_loaded` is recorded as a finding, and no `AgentResult` is emitted.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Compile the task and record `skills_required`, `skills_selected` and `skill_bundle_hash` | Compiler output + task record |
| 2 | Start the runtime with the non-waivable skill removed | Execution log + trace/event references |
| 3 | Attempt to produce a result anyway | Execution log + refusal record |
| 4 | Repeat with a waivable skill and confirm the difference in behaviour | Policy decision records |
| 5 | Restore the skill and confirm the task proceeds normally | Execution log + task record |
| 6 | Compile a substantial task and confirm every output element is present, not only the skill bundle | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The task is blocked before the first production step
- [ ] `skills_required` ⊄ `skills_loaded` is recorded as a divergence finding
- [ ] No `AgentResult` and no claim is produced by the blocked task
- [ ] A waivable skill produces a warning, not a block, and the difference is policy-driven
- [ ] The audit record names the rule, the policy version and the missing skill
- [ ] The Task Compiler now emits more than a skill bundle: a cohort, a diversity profile, a communication topology, a context projection, a budget contract and an assurance route.
- [ ] A task compiled with skills but no cohort is as incomplete as one compiled with no skills — ACC-081.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

This scenario tested that a skill loads. Baseline v1.3.0 makes the compiler's output substantially larger, and each missing element is a silent capability loss — WP-047, WP-148.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `TaskContract`
- `SkillBundle`
- `PolicyDecision`
- `Finding`
- `AuditRecord`

## Expected events

- `task.blocked`
- `skill.binding.diverged`
- `policy.denied`
- `task.resumed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-46-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-46-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-46-state-before.json` and `ACC-46-state-after.json`.
- `ACC-46-events.json`, `ACC-46-policy-decisions.json` and `ACC-46-audit-export.json`.
- `ACC-46-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test task is cancelled; the divergence finding and audit records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
