# ACC-098 — Memory Poisoning Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-098` |
| Category | Security/Knowledge |
| Severity | **Critical** |
| Accountable owner | Content Security Lead |
| Independent witness / verifier | Knowledge Lead / Red Team Lead |
| Related packages | `WP-058`, `WP-146`, `WP-151` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Memory Poisoning Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Untrusted content is crafted to enter memory and be retrieved later as though it were established fact.

**When:** The content passes through quarantine, is stored, and a later invocation retrieves from memory.

**Then:** The content is stored in a typed store whose authority field forbids claim support. It cannot be retrieved as evidence, cannot support a claim, and a lesson derived from a failed approach is not an accepted fact.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Craft untrusted content designed to read as an established finding | Execution log + trace/event references |
| 2 | Pass it through quarantine and observe which store receives it | Execution log + trace/event references |
| 3 | Attempt to retrieve it as evidence | Execution log + trace/event references |
| 4 | Attempt to cite it in support of a claim | Execution log + trace/event references |
| 5 | Attempt the same through a `FailedApproach` lesson | Execution log + trace/event references |
| 6 | Confirm the evidence store was never written | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The content lands in a store whose authority forbids claim support
- [ ] It cannot be retrieved through the evidence API
- [ ] It cannot support a claim by any path, including a derived lesson
- [ ] The evidence store received nothing from this content
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `MemoryMask policy`
- `ArtifactRecord`
- `PolicyDecision`
- `Finding`

## Expected events

- `policy.denied`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-098-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-098-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-098-state-before.json` and `ACC-098-state-after.json`.
- `ACC-098-events.json`, `ACC-098-policy-decisions.json` and `ACC-098-audit-export.json`.
- `ACC-098-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The poisoned content is retained in quarantine as a fixture; nothing is promoted out of it.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
