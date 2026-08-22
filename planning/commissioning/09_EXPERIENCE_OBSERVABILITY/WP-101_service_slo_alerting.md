# WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding

## Package card

| Field | Value |
|---|---|
| Work package | `WP-101` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Service Owners / Internal Audit |
| Hard dependencies | WP-002, WP-022, WP-025, WP-026, WP-028, WP-031, WP-041, WP-049, WP-052, WP-055, WP-056, WP-061, WP-075, WP-096, WP-098, WP-099, WP-100 |
| Related gates | Platform |
| Related controls | CTL-OBS-01, CTL-OPS-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Every service's owner, tier, dependencies, data class, SLIs/SLOs, error budget, dashboard, alerts, runbook and DR class are held in one catalogue.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/WP-022_repository_topology.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-098 — Grafana and the Six Operational Graphs](../09_EXPERIENCE_OBSERVABILITY/WP-098_grafana_six_graphs.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-101-T01 | Establish the Service Catalogue schema and registry | Implementation owner | Commit / configuration / record reference |
| WP-101-T02 | Map service tiers onto the critical user journeys | Implementation owner | Commit / configuration / record reference |
| WP-101-T03 | Define the availability, latency, correctness, freshness and durability SLIs | Implementation owner | Commit / configuration / record reference |
| WP-101-T04 | Write the error-budget and release-freeze rules | Implementation owner | Commit / configuration / record reference |
| WP-101-T05 | Add the alert owner, escalation and runbook link checker | Implementation owner | Commit / configuration / record reference |
| WP-101-T06 | Establish dependency/SLO roll-up and a quarterly review | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Service Catalog`
- `SLO catalog`
- `Error-budget policy`
- `Alert-runbook link checker`
- `Ownership dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Detection of orphaned services and alerts
- A synthetic SLO breach
- An error-budget-driven release freeze
- Owner-departure continuity
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No production service opens without an owner, a runbook and an SLO.
- [ ] Correctness and freshness SLOs are measured alongside uptime.
- [ ] Every critical alert carries a 24×7 escalation path.
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

A wrong SLO change is rolled back under service owner plus SRE review; silencing an alert counts as disabling a control and requires a time-bound exception.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
