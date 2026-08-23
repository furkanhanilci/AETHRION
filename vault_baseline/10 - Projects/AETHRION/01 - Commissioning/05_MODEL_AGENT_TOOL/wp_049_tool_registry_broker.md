---
title: "WP-049 — Tool Registry and Tool Broker Core"
aliases:
  - "WP-049"
  - "WP-049 — Tool Registry and Tool Broker Core"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every T0–T5 tool call passes through a chain of signed tool schema, purpose, actor, scope, data class, idempotency, policy, credential lease and audit."
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/gate/engineering
  - aethrion/state/not-started
---

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
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **`PolicyDecision` interface** — the commissioned contract; **Cedar** and **OPA/Rego** are optional backends behind it

The interface, not the engine, is what this package binds to. A policy engine with formal semantics and schema validation, whose `principal · action · resource · context` shape already matches `TaskContract` and in which a prohibition cannot be out-voted by a permission. **Any policy-evaluation anomaly fails closed.** The engine is chosen by the bake-off recorded in `docs/architecture/ADR-010`, which cannot run until a policy set exists — and none is authored. See also `docs/architecture/ADR-003`.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_049_tool_registry_broker.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_049_tool_registry_broker.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every T0–T5 tool call passes through a chain of signed tool schema, purpose, actor, scope, data class, idempotency, policy, credential lease and audit. Agents produce intent; the broker performs the effect.


## Analysis
### What this package actually decides

That agents produce **intent** and the broker performs the **effect**. The purpose
sentence is the architecture: an agent never holds a credential, never reaches an
external system, and never performs a side effect. It emits an
`InvocationEnvelope`; the broker decides, leases, acts, and returns a receipt.

`PR-06` — *agent tool authority expands too far*, early signal *direct credential
or connector use* — is rated critical, and this package is the only thing standing
between the design and that signal.

### The chain is the deliverable, and every link is a refusal point (T01–T06)

Signed tool schema → purpose → actor → scope → data class → idempotency → policy →
credential lease → audit. Nine links, and the package's value is that **each one
can say no**. A broker that validates the envelope and then acts has implemented
one link.

### Idempotency is what makes retry safe across a trust boundary (T04)

An agent retries. A broker without an idempotency store performs the effect twice,
and the second one is in an external system where compensation may be impossible.
The reconciliation store is what turns *at-least-once invocation* into
*at-most-once effect* — the same property WP-039 gives consumers, applied to
outbound calls.

### Credential leases, not credentials (T05)

A lease is scoped, time-limited and revocable. A credential is none of those. The
difference matters most at cancellation: WP-038 revokes the lease and the effect
stops being possible, which is not true of a key that was handed over.

### Result quarantine is where ADR-003 lands (T06)

Tool output is **untrusted content**. It arrives from outside the trust boundary
and it may contain instructions — that is `ACC-05`, prompt injection through a
PDF, and the same risk exists in a web page, a repository README or an API
response.

The rule is ADR-003's: content crosses, authority does not. Quarantine, redact,
attach provenance, and hand it back **as data**. The Bridge's own MCP server
already names this exact gap in its docstring: `get_source` returns a Zotero
abstract as raw text, and the cheap mitigation — wrapping external content in an
explicit boundary marker — *is not implemented yet*.

### The `ToolReceipt` is what makes a claim's side effects auditable

Every external effect in the system's history should be reconstructable from
receipts. Without them, "what did this agent actually do" is answered by reading
logs, which is not an answer.

### Baseline v1.3.0 — the Task Compiler stops emitting a skill list

This is the largest change in the model and agent layer, and it is a change of
kind rather than of size. The compiler's output was a skill bundle and a model
choice. It becomes the full execution shape of a task:

`AgentCohortRecord` · `CognitiveDiversityProfile` · skill bundles **by family** ·
`CommunicationTopology` · `ContextProjectionPolicy` · `ResearchBudgetContract` ·
`AssuranceRoute` · `ExecutionProfile` · `IndependenceProfile`.

A coding-science task compiles **both** skill families — preregistration
discipline beside test-driven development, scientific review beside code review
— without either aliasing the other (`ADR-012`).

Two other bindings:

- **Qualification records gain scope.** A verifier's qualification is keyed by
  verifier, version, task class, domain profile *and* threshold, and now also
  carries a model execution fingerprint and an abstention rate.
- **The Tool Broker gains a capability gate.** An action is unavailable unless
  policy grants it — not available-but-discouraged. Untrusted content can supply
  values and can never create an action, which is `ADR-003` enforced at the tool
  boundary rather than asserted at the prompt. Deterministic tool results are
  reusable within a declared freshness window and are marked as reused.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |

### Full prerequisite closure

**37 of 160 packages (23%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` |
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |

### What acceptance of this package releases

- **Directly unblocked:** 16 — `WP-050` · `WP-054` · `WP-055` · `WP-057` · `WP-058` · `WP-060` · `WP-064` · `WP-065` · `WP-066` · `WP-069` · `WP-096` · `WP-099` · `WP-100` · `WP-101` · `WP-107` · `WP-131`
- **Transitively reachable:** **106 of 160 packages (66%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **23** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Tool Platform Lead |
| Independent verifier | Security Architect / Internal Audit |
| Gates touched | `G3` · `G5` · `G9` · `Engineering` |
| Controls | `CTL-OPS-01` · `CTL-SEC-01` · `CTL-SEC-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) | Critical | The content stays untrusted quoted data; extraction continues read-only, no tool, secret or write call occurs, and security event and scan evidence is produced. |
| [ACC-12 — Duplicate Event Delivery](../12_ACCEPTANCE_SCENARIOS/acc_12_duplicate_event.md) | Critical | Exactly one business effect occurs, the duplicate is acknowledged and audited, and the side effect is not performed a second time. |
| [ACC-35 — Tool Partial Failure](../12_ACCEPTANCE_SCENARIOS/acc_35_tool_partial_failure.md) | Critical | A blind retry does not produce a second side effect; a read and reconcile finds the remote effect, and exactly one `ToolReceipt` is finalized — or the call becomes `RECONCILIATION_REQUIRED`. |
| [ACC-102 — Deterministic Tool-Result Reuse](../12_ACCEPTANCE_SCENARIOS/acc_102_tool_result_reuse.md) | Medium | The second is served from the recorded result and marked as reused. The third re-executes because the freshness boundary forbids reuse. A reused result is distinguishable from a fresh one in the record. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Producer and evaluator zone profiles` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `MutationPolicy` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `LangGraph runtime` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Temporal adapter` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Checkpoint policy` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Agent graph SDK` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Conformance tests` | `WP-046` | `python3 scripts/progress.py show WP-046` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Tool Platform Lead** carries the acceptance decision; **Security Architect / Internal Audit** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### No registered source names this package

Neither register binds an upstream mechanism or a runtime component to `WP-049`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

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
- `Capability gate`
- `Tool-result reuse with recorded provenance`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-049_tool_registry_broker.tests.md`](wp_049_tool_registry_broker.tests.md).

- Denial of an unsigned or free-form tool schema
- Duplicate invocation producing exactly one effect
- A scoped-target violation
- Secret redaction
- Reconciliation of a partial response after a timeout
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-049_tool_registry_broker.acceptance.md`](wp_049_tool_registry_broker.acceptance.md), together with what this package still cannot establish.

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
