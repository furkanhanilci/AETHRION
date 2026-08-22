# WP-006 — ExecutionProfile and Route Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-006` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Security Lead |
| Independent verifier | Safety Owner / SRE |
| Hard dependencies | WP-002 |
| Related gates | G1,G5 |
| Related controls | CTL-DAT-02, CTL-SEC-04 |
| Related acceptance scenarios | ACC-15, ACC-18 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

`DataClass`, `CodeTrust`, `ToolEffect` and network/credential scope act as **separate axes** that jointly produce the sandbox, route, approval and isolation controls. Collapsing them into one score is the failure this package exists to prevent.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-006-T01 | Define the D0–D4 `DataClass` rubric | Implementation owner | Commit / configuration / record reference |
| WP-006-T02 | Write the C0–C3 `CodeTrust` and T0–T5 `ToolEffect` rubrics | Implementation owner | Commit / configuration / record reference |
| WP-006-T03 | Define the network and credential scope levels | Implementation owner | Commit / configuration / record reference |
| WP-006-T04 | Write the dominance rule and the minimum execution tier rule | Implementation owner | Commit / configuration / record reference |
| WP-006-T05 | Map the enforcement points across the model router, the broker, Kueue and the sandbox | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ExecutionProfile semantics`
- `Route/control decision tables`
- `Enforcement map`
- `Negative examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A D0 + untrusted-code hardened-sandbox test
- A D4 + signed-code isolated-route test
- A negative test proving T4/T5 remain human-only
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Data class is never equated with sandbox tier.
- [ ] The highest required control cannot be lowered by a permissive value on another axis.
- [ ] Every routing decision carries an explainable policy rule ID.
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

Policy changes are validated in shadow mode; on a wrong route, profiles are revoked and affected workloads are paused rather than allowed to continue.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
