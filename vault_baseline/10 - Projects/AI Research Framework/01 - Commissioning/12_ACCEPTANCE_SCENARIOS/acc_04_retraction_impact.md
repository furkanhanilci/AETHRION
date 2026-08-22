# ACC-04 — Retraction Impact

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-04` |
| Category | Research/Monitoring |
| Severity | **Critical** |
| Accountable owner | Knowledge Monitoring Lead |
| Independent witness / verifier | Project Decision Owner / Citation Auditor |
| Related packages | `WP-063`, `WP-037`, `WP-108`, `WP-106` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Retraction Impact** situation. The test runs on the same
release candidate, policy bundle, schema bundle and environment manifest as
every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A source at CORE trust level supports a `VERIFIED` claim, a decision and a publication package.

**When:** The status monitor receives a verified retraction or correction event and an `ImpactScan` runs.

**Then:** The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the CORE source → claim → publication fixture chain | Execution log + trace/event references |
| 2 | Inject the retraction feed event | Execution log + trace/event references |
| 3 | Run the schedule and the `ImpactScan` | Execution log + trace/event references |
| 4 | Compare the affected set against the expected fixture | Execution log + trace/event references |
| 5 | Check the Decision Queue and the publication banner | Execution log + trace/event references |
| 6 | Resend the duplicate retraction event | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Recall of affected critical claims is 100%
- [ ] One `ImpactCase`; the trigger is idempotent
- [ ] The old `LiteratureSetManifest` hash is unchanged
- [ ] Claim status changes by rule, not by hand
- [ ] A named owner, an SLA and a public supersession notice exist
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SourceStatusRecord`
- `ImpactCase`
- `ClaimAssessment`
- `MonitoringRun`
- `SupersessionPlan`

## Expected events

- `source.retracted`
- `impact.scan.started`
- `claim.challenged`
- `decision.required`
- `publication.impact_detected`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-04-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-04-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-04-state-before.json` and `ACC-04-state-after.json`.
- `ACC-04-events.json`, `ACC-04-policy-decisions.json` and `ACC-04-audit-export.json`.
- `ACC-04-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Close the synthetic retraction status with a superseding test status; mark the `ImpactCase` `TEST_RESOLVED`.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
