# ACC-27 — Regional / Management Plane DR

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-27` |
| Category | Operations/DR |
| Severity | **Critical** |
| Accountable owner | SRE Lead |
| Independent witness / verifier | Independent DR Witness |
| Related packages | `WP-114`, `WP-129` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Regional / Management Plane DR** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A production-equivalent management region and its control services are unreachable; current backups, replicas and open workflows exist.

**When:** DR declaration, restore/failover and the traffic/DNS/control-plane switch runbook are executed.

**Then:** Temporal workflow state holds at RPO = 0, canonical registries, artifacts and audit records are intact, service returns within the RTO target, and derived views are rebuilt.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Take the pre-drill manifests, open workflow list and integrity baselines | Execution log + trace/event references |
| 2 | Isolate the region and control dependencies | Execution log + trace/event references |
| 3 | Start the incident, DR decision and communication flow | Execution log + trace/event references |
| 4 | Restore or fail over Temporal, PostgreSQL, objects, NATS and identity | Execution log + trace/event references |
| 5 | Rebuild projections and caches | Execution log + trace/event references |
| 6 | Verify integrity, ACC smoke tests, RPO/RTO and the failback path | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Workflow RPO = 0
- [ ] The restore meets the RTO target
- [ ] Registry, artifact and audit hashes match
- [ ] No duplicate effect occurred
- [ ] Derived views rebuild successfully
- [ ] The decision and audit records are complete
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `DRDecision`
- `RestoreManifests`
- `IntegrityQueryResults`
- `RPO/RTOReport`
- `IncidentRecord`

## Expected events

- `dr.declared`
- `service.failed_over`
- `restore.completed`
- `integrity.verified`
- `dr.closed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-27-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-27-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-27-state-before.json` and `ACC-27-state-after.json`.
- `ACC-27-events.json`, `ACC-27-policy-decisions.json` and `ACC-27-audit-export.json`.
- `ACC-27-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The DR environment and failover state are failed back or retained per runbook; the fault isolation is removed.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
