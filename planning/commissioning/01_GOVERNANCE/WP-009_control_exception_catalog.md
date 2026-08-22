# WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers

## Package card

| Field | Value |
|---|---|
| Work package | `WP-009` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Internal Audit |
| Hard dependencies | WP-005, WP-006, WP-007, WP-008 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-03 |
| Related acceptance scenarios | ACC-24, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Every control becomes a registry object carrying an owner, an enforcement point, its evidence, its test frequency and its exception lifecycle. A control that produces no evidence is treated as a failing control.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-009-T01 | Identify the governance, epistemic, data, literature, security, operations, observability, cost and model controls | Implementation owner | Commit / configuration / record reference |
| WP-009-T02 | Establish the control → policy → test → evidence mapping | Implementation owner | Commit / configuration / record reference |
| WP-009-T03 | Write the request, approval, expiry and auto-revoke semantics for exceptions | Implementation owner | Commit / configuration / record reference |
| WP-009-T04 | Bind the non-waivable blocker list into policy | Implementation owner | Commit / configuration / record reference |
| WP-009-T05 | Assign a control-effectiveness review frequency to each control | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Control Catalog`
- `ExceptionPolicy`
- `NonWaivableBlocker registry`
- `Control-test mapping`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An auto-revoke test for expired exceptions
- A negative test attempting an exception against a non-waivable blocker
- A failure test for a control that stops producing evidence
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every control has an enforcement point and an evidence artifact.
- [ ] Every exception is time-bound and scope-bound.
- [ ] There is no exception path for a critical blocker.
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

A faulty policy bundle is rolled back and every decision that relied on an affected exception is re-evaluated.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
