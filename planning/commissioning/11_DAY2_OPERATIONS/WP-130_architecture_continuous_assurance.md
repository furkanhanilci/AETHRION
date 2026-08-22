# WP-130 — Architecture and Platform Continuous Assurance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-130` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect / Platform Assurance Lead |
| Independent verifier | Architecture Board / Internal Audit |
| Hard dependencies | WP-010, WP-030, WP-040, WP-060, WP-109, WP-115, WP-121, WP-123, WP-124, WP-125, WP-126, WP-127, WP-128, WP-129 |
| Related gates | G0–G10, Platform, Day-2 |
| Related controls | All controls |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Architectural invariants, canonical ownership, contract compatibility, workflow replay, derived rebuild, the golden research path and control effectiveness are re-verified on a schedule. The platform is held to the same evidentiary standard it imposes on the research it hosts.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/WP-040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md), [WP-123 — Control Effectiveness and Policy Regression Rhythm](../11_DAY2_OPERATIONS/WP-123_control_effectiveness.md), [WP-124 — Model Requalification, Drift and Ejection Rhythm](../11_DAY2_OPERATIONS/WP-124_model_requalification_drift.md), [WP-125 — Literature, Zotero and Obsidian Curation Rhythm](../11_DAY2_OPERATIONS/WP-125_literature_knowledge_curation.md), [WP-126 — Reviewer, Judge and Reproducer Calibration](../11_DAY2_OPERATIONS/WP-126_assurance_calibration.md), [WP-127 — FinOps, Capacity and Portfolio Review Rhythm](../11_DAY2_OPERATIONS/WP-127_finops_portfolio.md), [WP-128 — Incident, Postmortem and Learning Closure](../11_DAY2_OPERATIONS/WP-128_incident_learning.md), [WP-129 — Quarterly DR, Supply-Chain and Audit Drill](../11_DAY2_OPERATIONS/WP-129_quarterly_dr_supply_chain.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-130-T01 | Run the monthly architecture drift and canonical-owner scan | Implementation owner | Commit / configuration / record reference |
| WP-130-T02 | Run the schema, adapter and policy compatibility suite | Implementation owner | Commit / configuration / record reference |
| WP-130-T03 | Execute the golden-path synthetic research and engineering runs | Implementation owner | Commit / configuration / record reference |
| WP-130-T04 | Run a derived graph, index and Obsidian rebuild sample | Implementation owner | Commit / configuration / record reference |
| WP-130-T05 | Review the platform chaos, replay and backup evidence | Implementation owner | Commit / configuration / record reference |
| WP-130-T06 | Produce the ADR reopen triggers, service retirement and technical-debt decisions | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Continuous Assurance report`
- `Architecture drift findings`
- `Golden-path results`
- `ADR/retirement decisions`
- `Assurance backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Canonical dual-write drift detection
- Workflow replay regression
- Graph rebuild
- A golden G0–G10 run
- The two-failure policy/control reopen trigger
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The platform is verified by its own research assurance system.
- [ ] A material control failure occurring twice reopens the corresponding ADR.
- [ ] The target architecture does not drift silently into a product dependency.
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

If the drift is critical the affected release, route or control is paused; the last validated baseline is restored and an impact scan is performed.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
