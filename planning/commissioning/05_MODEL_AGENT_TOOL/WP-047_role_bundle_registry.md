# WP-047 — Role and **Skill** Registries, and the Task Compiler

## Package card

| Field | Value |
|---|---|
| Work package | `WP-047` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Agent Platform Lead |
| Independent verifier | Governance / Eval Office |
| Hard dependencies | WP-003, WP-007, WP-013, WP-020, WP-042, WP-045, WP-046 |
| Related gates | G1–G7 |
| Related controls | CTL-GOV-02, CTL-MOD-01 |
| Related acceptance scenarios | ACC-46, ACC-47, ACC-48, ACC-51, plus those assigned during the relevant vertical slice |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-047_role_bundle_registry.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-047_role_bundle_registry.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A role's mandate, prompt/policy, input/output schema, allowed tools, context and evaluation and acceptance conditions are compiled into a versioned `RoleBundle`.


## Analysis
### What this package actually decides

What an agent *is*, operationally. A `RoleBundle` compiles a role's mandate,
prompt, schemas, allowed tools, context budget and evaluation references into one
versioned, signed object — so "the reviewer" stops being a prompt someone wrote
and becomes an artifact with a hash.

That hash is the point. Without it, a result produced by "the reviewer" cannot be
compared to another, because nothing pins what the reviewer was.

### The skill half is the larger half (T07–T12)

Six of the twelve sub-tasks are the Skill Registry, and they exist because this
repository already has 52 skills, a validator, and a specific gap:

> `docs/STATUS.md`: skills conform to a format; **none has a behaviour baseline.**

`scripts/validate_skills.py` runs today and checks the Agent Skills format plus
the `airl.*` metadata contract. T07 promotes it from a check to an **admission
gate**: a skill that does not conform does not load.

### `skill_bundle_hash` is what makes discipline reproducible (T10)

`00_PROGRAM/09` versions the skill bundle for the same reason it versions the
policy bundle: *it changes agent behaviour, and a result produced under one
version is not comparable to one produced under another.*

Putting the hash into `TaskContract` and the evidence chain (WP-013 T06) means a
run records not only what it was given and which model ran it, but **under which
discipline**. Nothing else in the plan carries this, and without it a G7
reproduction can differ for a reason no manifest names.

### Trigger resolution must be recorded, not inferred (T08)

`skill_selection_reason` is a small field with a large consequence: it converts
"the agent used the right skill" from an assumption into a record. WP-043's T23
tests the four outcomes — right, wrong, none, competing — and this is where the
selection becomes auditable.

### The two-family policy is a control, not a taxonomy (T11)

Engineering, scientific-research, shared — **selected from `work_domain`, never
chosen freely by the agent**. An agent that picks its own discipline family will
pick the one whose rules are easiest, and it will do so for defensible-sounding
reasons. `CLAUDE.md` already states the router-first rule; this makes it
mechanical.

### Upstream provenance for the vendored eleven (T12)

Eleven skills are vendored verbatim from `obra/superpowers` at a pinned commit,
with `airl.upstream_commit` in their frontmatter and the licence reproduced in
`skills/_vendor/`. `NOTICE` records it. T12 is what detects the day upstream
moves — a derived skill silently diverging from its origin is a provenance defect
that no format check sees.

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

7, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/WP-003_role_catalog_raci.md) | `Role Catalog` · `RACI matrix` · `Role-combination policy` · `Role assignment workflow` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md) | `Capability Registry service` · `Profile state machine` · `Eligibility API` · `Expiry/revoke scheduler` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |

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

- **Directly unblocked:** 11 — `WP-048` · `WP-069` · `WP-070` · `WP-078` · `WP-088` · `WP-097` · `WP-107` · `WP-147` · `WP-148` · `WP-149` · `WP-154`
- **Transitively reachable:** **64 of 160 packages (40%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **23** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Agent Platform Lead |
| Independent verifier | Governance / Eval Office |
| Gates touched | `G1–G7` |
| Controls | `CTL-GOV-02` · `CTL-MOD-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-46 — Task Runs With No Skill Loaded](../12_ACCEPTANCE_SCENARIOS/ACC-46_skill_not_loaded.md) | Critical | The task is blocked before any production step, the divergence between `skills_required` and `skills_loaded` is recorded as a finding, and no `AgentResult` is emitted. |
| [ACC-47 — Harness Starts Without the Skill Bootstrap](../12_ACCEPTANCE_SCENARIOS/ACC-47_skill_bootstrap_missing.md) | Critical | The adapter refuses the task with an explicit bootstrap failure; it does not fall back to an unguided session, and the refusal is distinguishable in the audit trail from a task that ran and failed. |
| [ACC-48 — Wrong or Competing Skill Selected](../12_ACCEPTANCE_SCENARIOS/ACC-48_wrong_skill_selected.md) | High | The correct skill is selected, the selection reason is recorded, and an unresolvable overlap fails closed rather than picking arbitrarily. |
| [ACC-51 — Upstream Change Invalidates a Derived Skill](../12_ACCEPTANCE_SCENARIOS/ACC-51_upstream_skill_drift.md) | High | Every affected vendored and derived skill is flagged for re-examination, the pinned commit does not silently move, and a claim produced under the old bundle remains resolvable to the procedure that actually governed it. |
| [ACC-081 — Multi-Agent Cohort Required](../12_ACCEPTANCE_SCENARIOS/ACC-081_multi_agent_cohort_required.md) | Critical | Compilation refuses, or adds the independent cognitive actors the invariant requires. There is no silent single-agent downgrade, and a cohort of several instances of the same model profile on the same context does not satisfy the requirement either. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/WP-003_role_catalog_raci.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md)
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
| `Role Catalog` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `RACI matrix` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Role-combination policy` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Role assignment workflow` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
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
| `Capability Registry service` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Profile state machine` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eligibility API` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Expiry/revoke scheduler` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |
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
- **Agent Platform Lead** carries the acceptance decision; **Governance / Eval Office** must verify independently of whoever implements.
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

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-010` — Curie — intra-agent and inter-agent rigor | `ADAPTIVE_REIMPLEMENT` | `MS-RIG-001` · `MS-RIG-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-022` — K-Dense Science Superpowers — computational-science methodology skills | `DIRECT_ADAPT` | named source files — **not yet selected** | the local module and contract surface this becomes — **named at refinement** | **4** |
| `ASM-023` — K-Dense Scientific Agent Skills — domain capability catalogue | `DEFER` | nothing — recorded so it is not re-examined from scratch | the contract this is held behind | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-010` | A RigorFinding blocks a transition when policy maps it to a control. It does not by itself reject a scientific claim. | The agent hierarchy and orchestrator, which would duplicate the authority Temporal already holds. |
| `ASM-022` | A skill changes how an agent works. It never changes what an agent is permitted to do — that is the RoleContract and the policy engine. | A parallel skill family. Where an upstream skill and an AETHRION skill address the same procedure, the result is one merged local skill, not two. |
| `ASM-023` | A domain skill is a capability. It cannot bypass a data class, an evidence contract or a gate. | Wholesale copy of the catalogue. Skill count is not a success metric, and a repository-level licence is not a per-file licence. |

### Where a plain row would mislead

- **`ASM-010`** — The rule worth taking is that agent B must not infer A succeeded from A's confident prose. Every rigor check that can be deterministic must be.
- **`ASM-022`** — Sixteen skills upstream, of which twelve overlap AETHRION's scientific family: framing-research-questions, surveying-prior-work, establishing-feasibility-first, designing-the-analysis, preregistering-analysis, subagent-driven-analysis, executing-analysis, dispatching-parallel-investigations, investigating-anomalous-results, verifying-results-before-claiming, requesting-red-team-review, receiving-critical-review, setting-up-reproducible-analysis, reporting-and-archiving-findings, writing-science-skills, using-science-superpowers. Its central discipline is pre-registration in place of …
- **`ASM-023`** — 161 skills across 18+ scientific domains. Deferred until a domain is actually selected: importing a bioinformatics skill before there is a bioinformatics project adds surface without adding capability. When one is imported, the licence in that skill's own SKILL.md governs — the repository licence does not.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-010` — Curie — intra-agent and inter-agent rigor** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-022` — K-Dense Science Superpowers — computational-science methodology skills** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a pinned upstream commit — a branch name is not a pin
- the exact list of files that will move
- a characterisation suite capturing upstream behaviour **before** any code moves

**Acquisition readiness — 5 obligations open across 2 of 3 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-047-T01 | Build the `RoleBundle` schema and its Git registry | Implementation owner | Commit / configuration / record reference |
| WP-047-T02 | Write the `RoleContract` → runtime prompt/tool/context compiler | Implementation owner | Commit / configuration / record reference |
| WP-047-T03 | Create the initial bundles for planner, scout, extractor, methodologist, coder, reviewer, reproducer and curator | Implementation owner | Commit / configuration / record reference |
| WP-047-T04 | Bind the context budget and frozen-package policy | Implementation owner | Commit / configuration / record reference |
| WP-047-T05 | Add bundle signature, admission and evaluation references | Implementation owner | Commit / configuration / record reference |
| WP-047-T06 | Establish deprecation and migration management | Implementation owner | Commit / configuration / record reference |
| WP-047-T07 | Build the **Skill Registry**: discovery, the Agent Skills format contract, and `scripts/validate_skills.py` as an admission gate | Implementation owner | Registry + rejected non-conformant specimen |
| WP-047-T08 | Implement **trigger resolution** — classification fields → `skills_required` — with a recorded `skill_selection_reason` | Implementation owner | Resolver + trigger test matrix |
| WP-047-T09 | Implement **version and dependency resolution** across `airl.requires_skills`, including conflict refusal | Implementation owner | Resolver + a refused conflicting bundle |
| WP-047-T10 | Compute and record `skill_bundle_hash`; bind it into `TaskContract` and the evidence chain | Implementation owner | Hash reproduced from a stored bundle |
| WP-047-T11 | Enforce the **two-family policy**: engineering, scientific-research and shared, selected from `work_domain` — never chosen freely by the agent | Implementation owner | Policy tests both ways |
| WP-047-T12 | Track **upstream provenance**: `airl.derived_from` + `airl.upstream_commit`, and flag derived skills when upstream moves | Implementation owner | Impact report for a simulated upstream change |

## Mandatory deliverables

- `Role Bundle Registry`
- **`Skill Registry`** with format admission, version and dependency resolution
- **`Task Compiler`** producing `RoleBundle` + `SkillBundle` + `ToolBundle` + `ContextBundle`
- **`skill_bundle_hash` computation** bound into `TaskContract`
- **Upstream provenance impact report**
- `Core role bundles`
- `Bundle conformance tests`
- `Cohort, topology, projection and assurance-route compilation`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

### The compiler this package must produce

```
RoleContract  +  TaskContract  +  classification fields
        │
        ▼
   Task Compiler ── skill policy ──► skill_selection_reason
        │
        ├─► RoleBundle      who
        ├─► SkillBundle     how          → skill_bundle_hash
        ├─► ToolBundle      with what
        └─► ContextBundle   knowing what
        │
        ▼
   runtime (WP-046 / WP-048)
```

**The agent does not choose its own skills.** Selection is derived by policy
from the classification fields and recorded with its reason; an agent that
loads a different set than the one compiled produces a divergence finding.

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-047_role_bundle_registry.tests.md`](WP-047_role_bundle_registry.tests.md).

- Forbidden tools excluded at compile time
- A compile failure when acceptance criteria are missing
- A negative test for reviewer contamination by the producer's trace
- Bundle signature validation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-047_role_bundle_registry.acceptance.md`](WP-047_role_bundle_registry.acceptance.md), together with what this package still cannot establish.

- [ ] A role is not a model name.
- [ ] Every bundle carries explicit inputs, outputs and non-goals.
- [ ] The reviewer bundle enforces blind context and its independence obligations.
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

A faulty bundle is revoked; the registry pointer returns to the previous signed version and open tasks receive an impact assessment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
