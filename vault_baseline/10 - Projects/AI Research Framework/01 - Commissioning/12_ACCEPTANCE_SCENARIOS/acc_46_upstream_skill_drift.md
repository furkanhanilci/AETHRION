# ACC-46 — Upstream Change Invalidates a Derived Skill

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-46` |
| Category | Agent/Skill Governance |
| Severity | **High** |
| Accountable owner | Knowledge Steward |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-013`, `WP-047` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Upstream Change Invalidates a Derived Skill** situation.

Part of the registry is vendored from an upstream project and part is derived
from it. When upstream moves, the question 'which of our procedures must be
re-examined?' must have a mechanical answer rather than an archaeological one.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A registry containing vendored skills pinned to an upstream commit and AIRL skills declaring `airl.derived_from`.

**When:** The upstream project advances to a commit that changes one of those skills.

**Then:** Every affected vendored and derived skill is flagged for re-examination, the pinned commit does not silently move, and a claim produced under the old bundle remains resolvable to the procedure that actually governed it.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Record the current pinned commit and the derived-skill map | Provenance snapshot |
| 2 | Advance the simulated upstream commit | Upstream diff |
| 3 | Run the provenance impact report | Impact report |
| 4 | Confirm the pin does not move without an explicit, recorded change | Registry diff + audit record |
| 5 | Resolve an old claim's `skill_bundle_hash` back to its exact procedure | Resolution proof |

## Mandatory invariants and assertions

- [ ] Every vendored skill affected by the upstream change is flagged
- [ ] Every derived skill declaring `airl.derived_from` for a changed upstream skill is flagged
- [ ] The pinned commit never moves implicitly
- [ ] A historical `skill_bundle_hash` still resolves to the exact procedure text
- [ ] The impact report is machine-readable evidence, not a narrative
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SkillBundle`
- `ProvenanceRecord`
- `ImpactReport`
- `AuditRecord`

## Expected events

- `skill.upstream.changed`
- `skill.reexamination.required`
- `provenance.pin.updated`

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

The simulated upstream is reverted; provenance and impact records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
