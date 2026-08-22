# WP-128 — Incident, Postmortem and Learning Closure

## Package card

| Field | Value |
|---|---|
| Work package | `WP-128` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Incident Commander / SRE Lead |
| Independent verifier | Safety / Assurance / Service Owner |
| Hard dependencies | WP-037, WP-060, WP-099, WP-101, WP-116, WP-118, WP-121 |
| Related gates | G10,Day-2 |
| Related controls | CTL-OPS-03, CTL-MOD-02, CTL-LIT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Security, data, reliability, cost and epistemic incidents are run through a contain → recover → learn → close lifecycle that ends in a control, evaluation or runbook change.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-128-T01 | Operate severity classification and the `IncidentWorkflow` | Implementation owner | Commit / configuration / record reference |
| WP-128-T02 | Perform containment, credential revocation, pausing and communication | Implementation owner | Commit / configuration / record reference |
| WP-128-T03 | Run forensic, audit and canonical integrity analysis and root-cause analysis | Implementation owner | Commit / configuration / record reference |
| WP-128-T04 | Write the blameless postmortem and the decision timeline | Implementation owner | Commit / configuration / record reference |
| WP-128-T05 | Bind each action to a WP, control, evaluation, runbook or `ImpactCase` | Implementation owner | Commit / configuration / record reference |
| WP-128-T06 | Verify effectiveness and take the closure decision | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `IncidentRecords`
- `Forensic packages`
- `Postmortems`
- `Learning/action register`
- `Closure evidence`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Security containment
- Duplicate effect and data integrity
- An escaped epistemic claim
- Re-testing action effectiveness
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A material incident is never closed by a document alone.
- [ ] Every action carries an owner, a date and evidence.
- [ ] Affected claims, projects, models and controls receive an impact scan.
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

If the recovery proves wrong the incident is reopened; evidence and postmortems remain versioned rather than edited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
