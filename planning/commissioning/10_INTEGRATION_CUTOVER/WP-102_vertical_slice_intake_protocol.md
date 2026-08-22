# WP-102 — Vertical Slice 1 — Intake through Protocol Freeze

## Package card

| Field | Value |
|---|---|
| Work package | `WP-102` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Workflow Lead |
| Independent verifier | Assurance / Project Decision Owner |
| Hard dependencies | WP-034, WP-035, WP-056, WP-091, WP-092, WP-093, WP-100, WP-101 |
| Related gates | G0,G1,G2 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-06, ACC-25, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A realistic R1 project and a realistic R3 project travel from G0 to G2 with a complete risk/control plan, charter, protocol, human decision and audit chain. This is the first slice where the design meets reality.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md), [WP-092 — Project Workspace and G0–G10 Gate Timeline](../09_EXPERIENCE_OBSERVABILITY/WP-092_project_gate_timeline.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-102-T01 | Prepare the R1 and R3 synthetic project fixtures | Implementation owner | Commit / configuration / record reference |
| WP-102-T02 | Start the intake from the cockpit | Implementation owner | Commit / configuration / record reference |
| WP-102-T03 | Verify the risk, execution and independence policy decisions | Implementation owner | Commit / configuration / record reference |
| WP-102-T04 | Run the charter, SLA, delegation and protocol freeze | Implementation owner | Commit / configuration / record reference |
| WP-102-T05 | Check the budget reservation, audit and telemetry chain | Implementation owner | Commit / configuration / record reference |
| WP-102-T06 | Test the revise, block and reopen paths | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Vertical slice dossier`
- `R1/R3 project histories`
- `Trace/audit/decision evidence`
- `Integration findings`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Happy path for both R1 and R3
- `BLOCKED` on an unknown risk value
- An expired delegation
- A material protocol amendment
- Budget unavailable
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every canonical record from G0 to G2 is linked.
- [ ] R3 receives deeper assurance but uses the same gates.
- [ ] No open critical integration finding remains.
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

If the slice fails, the production-like project is closed; synthetic artifacts are retained and a correction package is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
