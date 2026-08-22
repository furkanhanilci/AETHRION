# WP-049 — Tool Registry and Tool Broker Core

## Package card

| Field | Value |
|---|---|
| Work package | `WP-049` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Tool Platform Lead |
| Independent verifier | Security Architect / Internal Audit |
| Hard dependencies | WP-006, WP-011, WP-013, WP-015, WP-016, WP-020, WP-025, WP-026, WP-028, WP-046 |
| Related gates | G3,G5,G9,Engineering |
| Related controls | CTL-OPS-01, CTL-SEC-01, CTL-SEC-03 |
| Related acceptance scenarios | ACC-05, ACC-12, ACC-35 |
| Current status | `NOT_STARTED` |

## Adopted component

> **Cedar** policy engine — first candidate; **OPA** the recorded alternative

`principal · action · resource · context` already matches `TaskContract`, `forbid` overrides `permit`, and the language has a formal semantics and schema validation. **Any policy-evaluation anomaly fails closed.** A bake-off over the same 50 policies is recorded before the choice is fixed. See `docs/architecture/ADR-003`.

Rationale and adoption type: `docs/architecture/AIRL_OS_COMPONENT_REUSE.md`.

## Purpose and expected outcome

Every T0–T5 tool call passes through a chain of signed tool schema, purpose, actor, scope, data class, idempotency, policy, credential lease and audit. Agents produce intent; the broker performs the effect.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-049-T01 | Build the `ToolDefinition` registry with signatures and versioning | Implementation owner | Commit / configuration / record reference |
| WP-049-T02 | Validate the `InvocationEnvelope` | Implementation owner | Commit / configuration / record reference |
| WP-049-T03 | Bind the OPA actor × purpose × data × tool × target × risk decision | Implementation owner | Commit / configuration / record reference |
| WP-049-T04 | Write the idempotency and reconciliation store | Implementation owner | Commit / configuration / record reference |
| WP-049-T05 | Add the Vault/SPIRE credential lease and the egress proxy adapter | Implementation owner | Commit / configuration / record reference |
| WP-049-T06 | Produce result quarantine, redaction, provenance and the `ToolReceipt` | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Tool Registry`
- `Tool Broker service`
- `Invocation/Receipt persistence`
- `Connector SDK`
- `Audit events`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of an unsigned or free-form tool schema
- Duplicate invocation producing exactly one effect
- A scoped-target violation
- Secret redaction
- Reconciliation of a partial response after a timeout
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An agent can never use a connector or credential directly.
- [ ] No T3+ action executes without the required approval.
- [ ] Every call carries a policy decision and a `ToolReceipt`.
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

- A model alias is not a pinned identity; results obtained under an alias are not reproducible.
- An agent holding a credential defeats the entire broker design.
- Fallback routes are the least tested and most consequential path in this workstream.

## Rollback / compensation

On a connector or broker fault the idempotency state is preserved; an uncertain effect becomes `RECONCILIATION_REQUIRED` and is never retried automatically.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
