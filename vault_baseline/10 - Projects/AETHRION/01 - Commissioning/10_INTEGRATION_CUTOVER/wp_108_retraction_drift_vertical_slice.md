# WP-108 — Retraction, Drift and Supersession Vertical Slice

## Package card

| Field | Value |
|---|---|
| Work package | `WP-108` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Assurance / Eval Office / Decision Owner |
| Hard dependencies | WP-037, WP-042, WP-044, WP-063, WP-075, WP-077, WP-090, WP-095, WP-106 |
| Related gates | G10 |
| Related controls | CTL-LIT-02, CTL-MOD-02 |
| Related acceptance scenarios | ACC-04, ACC-31, ACC-36 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Source retractions and corrections, model snapshot revocations, dataset and policy changes and incidents route the affected claims, runs, publications and tasks to the right owner and re-evaluation path.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/wp_106_vertical_slice_decision_publish_monitor.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-108-T01 | Produce the retraction, correction, model, data, policy and incident fixtures | Implementation owner | Commit / configuration / record reference |
| WP-108-T02 | Run the schedule/event → `ImpactScan` and the graph query | Implementation owner | Commit / configuration / record reference |
| WP-108-T03 | Compare the computed affected claim/task/project/publication set against the expected set | Implementation owner | Commit / configuration / record reference |
| WP-108-T04 | Apply priority, SLA, owner and the provisional/challenged state | Implementation owner | Commit / configuration / record reference |
| WP-108-T05 | Perform re-review, reproduction, republication or a no-impact disposition | Implementation owner | Commit / configuration / record reference |
| WP-108-T06 | Test false-positive handling and duplicate-trigger idempotency | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Impact vertical dossier`
- `ImpactCase set`
- `Affected-object accuracy report`
- `Supersession/re-evaluation records`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- ACC-04, 31 and 36
- A duplicate trigger producing one case
- A false-positive disposition
- A model revocation against an open task
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Affected-set recall is 100% for the critical fixtures.
- [ ] No existing object is silently mutated.
- [ ] Every material impact carries a named owner and a deadline.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

A faulty case disposition is superseded; the trigger and the previous status remain in the audit history.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
