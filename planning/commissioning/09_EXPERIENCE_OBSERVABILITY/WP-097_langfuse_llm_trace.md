# WP-097 — Langfuse Model/Agent Tracing and Prompt Governance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-097` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | AI Observability Lead |
| Independent verifier | Privacy/Security / Eval Office |
| Hard dependencies | WP-006, WP-013, WP-020, WP-025, WP-026, WP-041, WP-046, WP-047, WP-055, WP-056, WP-057, WP-096 |
| Related gates | G2–G7 |
| Related controls | CTL-OBS-02, CTL-DAT-03 |
| Related acceptance scenarios | ACC-32 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Prompt, template, model, tool, token, latency, cost and evaluation signals from agent and model calls are traced under data-class retention and redaction — and private chain-of-thought is never requested or stored.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-097-T01 | Deploy Langfuse with project structure, RBAC and data routing | Implementation owner | Commit / configuration / record reference |
| WP-097-T02 | Apply the trace hierarchy and the AIRL correlation mapping | Implementation owner | Commit / configuration / record reference |
| WP-097-T03 | Bind the prompt and template version registry | Implementation owner | Commit / configuration / record reference |
| WP-097-T04 | Add input, output and tool-schema redaction and minimisation | Implementation owner | Commit / configuration / record reference |
| WP-097-T05 | Apply the no-chain-of-thought and rationale-summary policy | Implementation owner | Commit / configuration / record reference |
| WP-097-T06 | Establish evaluation feedback, cost, export, retention and backup | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Langfuse platform`
- `Prompt registry`
- `Trace/redaction policy`
- `Retention/export runbook`
- `Trace quality dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A secret inside a prompt being redacted or quarantined
- D3 traces limited to minimum fields
- Prompt-version correlation
- Confirmation that private reasoning is not stored
- Backup and restore
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A trace is never canonical workflow or claim state.
- [ ] Sensitive data obeys its TTL and its declared purpose.
- [ ] A model outcome carries a short rationale, evidence and gaps — not a dump of hidden reasoning.
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

The trace pipeline can be disabled or switched to redact-first mode; canonical runs and evidence continue, and the telemetry gap is recorded.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
