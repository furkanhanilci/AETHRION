# WP-010 — Architecture Decision and Rejected-Alternatives Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-010` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Architecture Board |
| Hard dependencies | WP-002, WP-005, WP-006, WP-007, WP-008, WP-009 |
| Related gates | Program,Platform |
| Related controls | CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The Temporal/LangGraph/NATS, Source Registry/Zotero/Obsidian, canonical-record, trust-zone and cutover decisions are captured in an ADR baseline together with the triggers that would reopen them.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/WP-009_control_exception_catalog.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-010-T01 | Separate the binding decisions into individual ADRs | Implementation owner | Commit / configuration / record reference |
| WP-010-T02 | Write the alternatives, the trade-offs and the reason each was rejected | Implementation owner | Commit / configuration / record reference |
| WP-010-T03 | Define the reopen trigger for every decision | Implementation owner | Commit / configuration / record reference |
| WP-010-T04 | Link the canonical-owner and trust-boundary consequences of each decision | Implementation owner | Commit / configuration / record reference |
| WP-010-T05 | Establish the ADR → WP → control mapping | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Signed ADR bundle`
- `Rejected alternatives register`
- `Reopen trigger register`
- `Architecture baseline digest`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A sweep for mutually contradictory ADRs
- An ADR-link check for every material package
- A reopen-trigger tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No contradiction remains on canonical ownership or engine boundaries.
- [ ] Every binding decision carries an accountable approver.
- [ ] The baseline digest can be embedded in a release manifest.
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

- A policy that is written but not machine-checkable is an intention, not a control.
- Role and authority documents drift silently; every change here needs a baseline bump.
- The hardest failure in this workstream is a rule that everyone agrees with and nobody can enforce.

## Rollback / compensation

If a new baseline is not accepted, the last signed ADR bundle remains in force and dependent implementation packages do not become `READY`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
