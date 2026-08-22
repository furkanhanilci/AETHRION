# WP-069 — SearchProtocol and LiteratureCampaign Orchestration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-069` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Methodologist / Citation Auditor |
| Hard dependencies | WP-013, WP-017, WP-032, WP-035, WP-046, WP-047, WP-049, WP-050, WP-061, WP-062 |
| Related gates | G2,G3 |
| Related controls | CTL-EPI-02, CTL-LIT-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A research question becomes a re-runnable literature campaign defined by databases, queries, date and language limits, inclusion/exclusion criteria, stop rules and known-item tests.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/wp_050_tool_connectors.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-069-T01 | Write the question → concept → query authoring flow | Implementation owner | Commit / configuration / record reference |
| WP-069-T02 | Define the database and source connector catalogue and its coverage | Implementation owner | Commit / configuration / record reference |
| WP-069-T03 | Establish `SearchProtocol` freeze, versioning and amendment | Implementation owner | Commit / configuration / record reference |
| WP-069-T04 | Record the query execution log, response snapshot and references | Implementation owner | Commit / configuration / record reference |
| WP-069-T05 | Compute known-item recall, saturation and the stop rule | Implementation owner | Commit / configuration / record reference |
| WP-069-T06 | Bind the Temporal `LiteratureCampaign` and its bounded scout tasks | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SearchProtocol service`
- `LiteratureCampaign workflow`
- `Query log`
- `Known-item/coverage tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Re-running a frozen query
- Failure when a known item is missing
- Resume after a provider partial failure
- A protocol amendment producing a new version
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every result is bound to its query, provider and timestamp.
- [ ] The number of search results is never treated as evidence of coverage.
- [ ] A query for critical counter-evidence is mandatory.
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

- Identity errors in sources propagate into every claim that cites them.
- A write into a shared library without a version precondition can silently destroy a human edit.
- A literature set that is not frozen cannot support a reproducible claim.

## Rollback / compensation

A provider failure marks the query `PARTIAL`; the set cannot be frozen until a coverage decision is taken explicitly.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
