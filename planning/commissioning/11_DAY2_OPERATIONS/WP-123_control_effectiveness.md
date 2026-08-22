# WP-123 — Control Effectiveness and Policy Regression Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-123` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Internal Audit / Red Team |
| Hard dependencies | WP-009, WP-056, WP-060, WP-112, WP-121 |
| Related gates | Day-2 |
| Related controls | All controls |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Policies and controls are measured for **effectiveness** — through scheduled negative tests, attacks, exception audits, coverage and false-positive review — not merely for existence.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/WP-009_control_exception_catalog.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-112 — Security and Privacy Acceptance Package](../10_INTEGRATION_CUTOVER/WP-112_security_privacy_acceptance.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-123-T01 | Apply the control test calendar and its sampling rates | Implementation owner | Commit / configuration / record reference |
| WP-123-T02 | Run the OPA, identity, data, tool and supply-chain negative regressions | Implementation owner | Commit / configuration / record reference |
| WP-123-T03 | Audit exception expiry, usage and residual risk | Implementation owner | Commit / configuration / record reference |
| WP-123-T04 | Review control coverage, gaps and false positives | Implementation owner | Commit / configuration / record reference |
| WP-123-T05 | Trigger an ADR or policy reopen after two material failures | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Control effectiveness reports`
- `Policy regression results`
- `Exception audit`
- `Control improvement backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Non-waivable denial tests
- An expired exception scan
- An attack regression sample
- Decision log coverage
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A critical control-effectiveness failure produces a same-day incident and containment.
- [ ] Exceptions never extend automatically.
- [ ] Control success is not measured by denial count alone.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

A faulty policy bundle is rolled back; the affected decisions and tasks receive an impact scan.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
