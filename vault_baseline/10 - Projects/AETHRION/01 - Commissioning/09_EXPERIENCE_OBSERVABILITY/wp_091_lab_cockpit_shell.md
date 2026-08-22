# WP-091 — Lab Cockpit Information Architecture and Application Shell

## Package card

| Field | Value |
|---|---|
| Work package | `WP-091` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Product/Experience Lead |
| Independent verifier | Accessibility Reviewer / Governance |
| Hard dependencies | WP-002, WP-012, WP-013, WP-020, WP-025, WP-030, WP-032, WP-033, WP-055 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A human gains a secure cockpit that shows portfolio, project, gate, task, evidence, review, decision, cost and incident state under one correlation — without becoming a second copy of canonical state.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-091-T01 | Write the persona, task and information architecture | Implementation owner | Commit / configuration / record reference |
| WP-091-T02 | Bind OIDC, MFA, RBAC and session security | Implementation owner | Commit / configuration / record reference |
| WP-091-T03 | Establish the project/gate timeline shell and the deep-link standard | Implementation owner | Commit / configuration / record reference |
| WP-091-T04 | Write the canonical API aggregation and read-model BFF | Implementation owner | Commit / configuration / record reference |
| WP-091-T05 | Add a state freshness and projection-lag indicator | Implementation owner | Commit / configuration / record reference |
| WP-091-T06 | Apply the accessibility, i18n, error, empty and loading patterns | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cockpit application shell`
- `Navigation/IA`
- `BFF/read APIs`
- `RBAC matrix`
- `Accessibility baseline`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A role-based view and access negative test
- The stale-projection banner
- Keyboard and screen-reader flows
- Deep navigation through canonical links
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The UI never owns gate state.
- [ ] Every critical decision surface shows an evidence summary and a freshness indicator.
- [ ] No unauthorised D2+ field reaches the browser.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A UI release is reverted by feature flag or canary; canonical workflows are unaffected.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
