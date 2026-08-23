---
title: "WP-046 — LangGraph Bounded Cognition Runtime"
aliases:
  - "WP-046"
  - "WP-046 — LangGraph Bounded Cognition Runtime"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "LangGraph manages only the node/state, checkpoint, interrupt and AgentResult production within the scope of a TaskContract."
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g2-g7
  - aethrion/state/not-started
---

# WP-046 — LangGraph Bounded Cognition Runtime

## Package card

| Field | Value |
|---|---|
| Work package | `WP-046` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Agent Platform Lead |
| Independent verifier | Control Plane Architect / Security |
| Hard dependencies | WP-013, WP-020, WP-031, WP-032, WP-041, WP-045 |
| Related gates | G2–G7 |
| Related controls | CTL-OPS-02, CTL-DAT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_046_langgraph_runtime.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_046_langgraph_runtime.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

LangGraph manages only the node/state, checkpoint, interrupt and `AgentResult` production within the scope of a `TaskContract`. It owns neither lifecycle state nor side effects.


## Analysis
### What this package actually decides

Where cognition is allowed to happen, and how far it reaches. The plan's binding
decision is narrow and deliberate: *LangGraph manages cognitive state **inside** a
bounded agent task only.* It owns neither lifecycle state nor side effects.

### The boundary is the package (T05)

Every side effect goes through the Tool Broker or the Execution Broker. An agent
graph that can write a file, call an API or spend money directly has escaped the
control plane, and every guarantee above it — policy, budget, audit, independence
— becomes advisory.

This is ADR-003's trust boundary at the runtime layer: **content crosses,
authority does not.** A node may read anything it is given; it may act only
through a broker.

### Checkpoints carry data class and therefore need a TTL (T03)

A checkpoint store accumulates intermediate reasoning, and intermediate reasoning
contains whatever the task was given. A D3 task checkpointing into an unclassified
store is a leak with a long tail, because checkpoints outlive the task that made
them.

### Cancellation has to reach into a running graph (T04)

WP-038 cancels the workflow; that only helps if the graph stops. A node that
continues after cancellation keeps spending budget and may still produce an
effect, and the workflow that requested cancellation has already moved on.

### `AgentResult` is where the hypothesis is stated (T06)

WP-013 requires `gaps` and `assumptions`. This runtime is what populates them, and
the same warning applies: an empty list is cheap to return and reads as *no
assumptions* rather than *not implemented*. The conformance suite measures the
non-empty rate on real tasks, not the field's presence.

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

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md) | `Temporal platform` · `Namespace/queue catalog` · `Worker identity policy` · `HA/failover runbook` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md) | `LiteLLM deployment` · `Provider configuration` · `Gateway policy adapter` · `Model-call audit/cost events` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |

### Full prerequisite closure

**36 of 160 packages (22%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-047` · `WP-048` · `WP-049` · `WP-069` · `WP-096` · `WP-097` · `WP-147` · `WP-148` · `WP-149`
- **Transitively reachable:** **109 of 160 packages (68%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **22** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Agent Platform Lead |
| Independent verifier | Control Plane Architect / Security |
| Gates touched | `G2–G7` |
| Controls | `CTL-OPS-02` · `CTL-DAT-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-46 — Task Runs With No Skill Loaded](../12_ACCEPTANCE_SCENARIOS/acc_46_skill_not_loaded.md) | Critical | The task is blocked before any production step, the divergence between `skills_required` and `skills_loaded` is recorded as a finding, and no `AgentResult` is emitted. |
| [ACC-49 — Non-Waivable Skill Ignored Under Pressure](../12_ACCEPTANCE_SCENARIOS/acc_49_skill_ignored_under_pressure.md) | Critical | The iron law holds; the attempted evasion and its verbatim justification are captured; the task cannot reach a completion claim. |
| [ACC-50 — Procedure Lost to Context Compaction or Restart](../12_ACCEPTANCE_SCENARIOS/acc_50_skill_lost_on_compaction.md) | High | The procedure is restored or the task halts; it never continues silently without it, and the recovery is visible in the audit trail. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Temporal platform` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Namespace/queue catalog` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Worker identity policy` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `HA/failover runbook` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `SLO dashboard` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `LiteLLM deployment` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Provider configuration` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway policy adapter` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Model-call audit/cost events` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway runbook` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |

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
- **Agent Platform Lead** carries the acceptance decision; **Control Plane Architect / Security** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-046-T01 | Build the canonical task graph wrapper and its state schema | Implementation owner | Commit / configuration / record reference |
| WP-046-T02 | Write the Temporal activity and child-task adapter | Implementation owner | Commit / configuration / record reference |
| WP-046-T03 | Bind the checkpoint store with its TTL and data-class policy | Implementation owner | Commit / configuration / record reference |
| WP-046-T04 | Apply node timeout, retry and cancellation semantics | Implementation owner | Commit / configuration / record reference |
| WP-046-T05 | Block every side effect that does not go through the Tool or Execution Broker | Implementation owner | Commit / configuration / record reference |
| WP-046-T06 | Add `AgentResult`/artifact upload and trace correlation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `LangGraph runtime`
- `Temporal adapter`
- `Checkpoint policy`
- `Agent graph SDK`
- `Conformance tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-046_langgraph_runtime.tests.md`](wp_046_langgraph_runtime.tests.md).

- Task cancellation propagation
- Resume from checkpoint
- A direct side-effect negative test
- Rebuild from the `TaskContract` after total runtime loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-046_langgraph_runtime.acceptance.md`](wp_046_langgraph_runtime.acceptance.md), together with what this package still cannot establish.

- [ ] LangGraph never mirrors gate or workflow state.
- [ ] Every external effect is a broker call.
- [ ] Checkpoints containing sensitive data obey the retention policy.
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

Runtime releases are canaried per task; a failed task is re-dispatched onto the new runtime or resumed from its last checkpoint.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
