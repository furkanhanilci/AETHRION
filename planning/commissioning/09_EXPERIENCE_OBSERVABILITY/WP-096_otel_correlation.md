# WP-096 — OpenTelemetry End-to-End Correlation Spine

## Package card

| Field | Value |
|---|---|
| Work package | `WP-096` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Observability Lead |
| Independent verifier | Security / SRE |
| Hard dependencies | WP-011, WP-015, WP-020, WP-021, WP-025, WP-028, WP-031, WP-041, WP-046, WP-049, WP-052, WP-055, WP-057, WP-082 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The same project/workflow/run/trace correlation travels from a console command through the Temporal workflow, agent/model/tool calls, the sandbox, the database and event bus, and into artifact, claim and cost records.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-096-T01 | Deploy the OTel collector/gateway in HA with tenant and data-class routing | Implementation owner | Commit / configuration / record reference |
| WP-096-T02 | Write the trace, span, log and metric semantic conventions | Implementation owner | Commit / configuration / record reference |
| WP-096-T03 | Bind the context-propagation SDKs into every service | Implementation owner | Commit / configuration / record reference |
| WP-096-T04 | Add Temporal activity, LangGraph, model, tool, database, NATS and Kubernetes instrumentation | Implementation owner | Commit / configuration / record reference |
| WP-096-T05 | Apply the sampling, error-escalation and clock policy | Implementation owner | Commit / configuration / record reference |
| WP-096-T06 | Establish trace-completeness SLOs and queries | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `OTel platform`
- `Semantic conventions`
- `Instrumentation libraries`
- `Trace completeness dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An end-to-end request trace
- Asynchronous NATS causation linking
- Retry and duplicate span semantics
- An alert on missing correlation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Correlation identifiers match the canonical records exactly.
- [ ] A missing trace is not business state loss, but it is an SLO violation.
- [ ] No D3/D4 raw payload becomes a span attribute.
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

A collector outage never makes the workflow unsafe — telemetry buffers or drops per policy; configuration is rolled back and the gap opens an `IncidentRecord`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
