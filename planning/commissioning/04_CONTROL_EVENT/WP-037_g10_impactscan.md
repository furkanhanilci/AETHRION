# WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows

## Package card

| Field | Value |
|---|---|
| Work package | `WP-037` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Assurance Lead / SRE |
| Hard dependencies | WP-008, WP-015, WP-017, WP-018, WP-031, WP-032 |
| Related gates | G10 |
| Related controls | CTL-LIT-02, CTL-MOD-02 |
| Related acceptance scenarios | ACC-04, ACC-31, ACC-36 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Retraction, source correction, model/data/policy drift and incident signals launch short-lived `ImpactScan` workflows on a periodic Schedule — never one long-lived monitoring workflow.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-037-T01 | Establish the `MonitoringPolicy` and schedule registry | Implementation owner | Commit / configuration / record reference |
| WP-037-T02 | Write the source, model, data, policy and incident trigger adapters | Implementation owner | Commit / configuration / record reference |
| WP-037-T03 | Produce the impact graph query and the affected claim/project list | Implementation owner | Commit / configuration / record reference |
| WP-037-T04 | Assign `ImpactCase` priority, SLA and owner | Implementation owner | Commit / configuration / record reference |
| WP-037-T05 | Dispatch the supersession and re-evaluation workflows | Implementation owner | Commit / configuration / record reference |
| WP-037-T06 | Add false-positive disposition and audit | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ImpactScan workflow`
- `Schedule registry`
- `ImpactCase service contract`
- `Supersession trigger`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A retraction → affected-claim test
- A model revocation → open-task test
- Schedule retry and idempotency
- A negative test proving old claims are never silently mutated
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No single long-lived monitoring workflow exists.
- [ ] Every scan is bounded and idempotent.
- [ ] Affected claim owners receive a queue item and a status change.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A faulty impact result is closed with a new disposition; the source and claim history is never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
