# WP-120 — Production Cutover and Go-Live Decision

## Package card

| Field | Value |
|---|---|
| Work package | `WP-120` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Executive Sponsor / Program Lead |
| Independent verifier | Commissioning Board / Internal Audit |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118, WP-119 |
| Related gates | Cutover |
| Related controls | All controls |
| Related acceptance scenarios | every scenario whose `Acceptance phase` is `PRE_GO_LIVE` (ACC-01 – ACC-51 excluding the Day-2 set) |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

On the strength of the signed commissioning dossier and the rehearsal, the change freeze, migration and promotion, smoke and integrity tests, traffic enablement and the formal Go-Live `DecisionRecord` are executed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md), [WP-119 — Controlled Pilot and Cutover Rehearsal](../10_INTEGRATION_CUTOVER/WP-119_pilot_cutover_rehearsal.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-120-T01 | Freeze the final RC, policy, schema, model, tool and infrastructure digests | Implementation owner | Commit / configuration / record reference |
| WP-120-T02 | Take the pre-cutover backup and restore point and run the owner check | Implementation owner | Commit / configuration / record reference |
| WP-120-T03 | Apply the IaC/GitOps deployment and migration steps | Implementation owner | Commit / configuration / record reference |
| WP-120-T04 | Run the service, contract, security and integrity smoke tests | Implementation owner | Commit / configuration / record reference |
| WP-120-T05 | Enable traffic, user access and monitoring in a controlled sequence | Implementation owner | Commit / configuration / record reference |
| WP-120-T06 | Record the go / no-go / abort decision with its evidence | Implementation owner | Commit / configuration / record reference |
| WP-120-T07 | Take the post-cutover audit snapshot | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cutover execution log`
- `Go-Live DecisionRecord`
- `Production release manifest`
- `Smoke/integrity results`
- `Audit snapshot`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- The preflight checklist
- Deployment and migration
- Security, identity and route smoke tests
- Workflow, source, claim and artifact integrity
- Abort and rollback readiness
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The Commissioning Dossier is READY.
- [ ] Every `PRE_GO_LIVE` scenario PASSes, with open critical findings = 0.
- [ ] Every production digest is signed and pinned.
- [ ] The go-live decision is taken by named executives, SRE and Safety.
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

At the abort threshold traffic is closed and the last verified baseline is restored per the GitOps and database plan; newly written immutable records are never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
