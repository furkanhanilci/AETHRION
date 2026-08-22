# WP-118 — Operational Readiness, On-Call and Runbook Simulation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-118` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Internal Audit / Service Owners |
| Hard dependencies | WP-099, WP-101, WP-114, WP-115, WP-116, WP-117 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-03, CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The service owner, on-call, escalation, incident command, break-glass, backup/restore, reconciliation, security and business continuity runbooks have all been **executed** in staging.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-118-T01 | Complete the runbook catalogue and its freshness and link checks | Implementation owner | Commit / configuration / record reference |
| WP-118-T02 | Test the on-call rota, escalation and paging | Implementation owner | Commit / configuration / record reference |
| WP-118-T03 | Run the incident commander tabletop and a live simulation | Implementation owner | Commit / configuration / record reference |
| WP-118-T04 | Exercise the two-person break-glass and credential revocation | Implementation owner | Commit / configuration / record reference |
| WP-118-T05 | Apply the Zotero, tool, event, policy and model reconciliation runbooks | Implementation owner | Commit / configuration / record reference |
| WP-118-T06 | Complete handover, training and the readiness sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Operational Readiness Review`
- `Runbook execution records`
- `On-call simulation`
- `Training/ownership sign-offs`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An after-hours page and escalation
- Reconciliation of an uncertain tool write
- A policy rollback
- A model revocation
- Security containment
- A restore invocation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every critical service has a 24×7 owner and a runbook.
- [ ] A runbook is executed evidence, not an unread document.
- [ ] Break-glass audit and revocation both work.
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

A readiness failure blocks cutover; the date is not approved until every missing owner and runbook is resolved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
