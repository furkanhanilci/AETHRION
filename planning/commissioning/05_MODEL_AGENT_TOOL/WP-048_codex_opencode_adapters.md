# WP-048 — Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker

## Package card

| Field | Value |
|---|---|
| Work package | `WP-048` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Agent Runtime Lead |
| Independent verifier | Security / Eval Office |
| Hard dependencies | WP-023, WP-027, WP-046, WP-047 |
| Related gates | G5,Engineering |
| Related controls | CTL-SEC-03, CTL-SEC-04 |
| Related acceptance scenarios | ACC-47, ACC-49, ACC-50, plus those assigned during the relevant vertical slice |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Inspect AI agent bridge** — drive real harnesses rather than writing one adapter per harness

Inspect can run Claude Code, Codex CLI and Gemini CLI as evaluation subjects inside a sandbox. ACC-47 (bootstrap missing), ACC-49 (ignored under pressure) and ACC-50 (lost to compaction) are Inspect tasks.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-048_codex_opencode_adapters.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-048_codex_opencode_adapters.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Different agent runtimes become interchangeable adapters that all satisfy the same `TaskContract`, isolation, tool, result, audit and cancellation contract.


## Analysis
### What this package actually decides

That the harness is replaceable. Five runtimes — Codex, OpenCode, a direct worker,
**Claude Code** and **Hermes Agent** — behind one adapter interface, all
satisfying the same `TaskContract`, isolation, tool, result, audit and
cancellation contract.

The reason is `PR-10` applied one layer up from models: a laboratory whose
research depends on one vendor's agent product has a dependency it did not
choose deliberately.

### The bootstrap problem is specific and easy to get wrong (T22)

*The router skill is present on the first turn without being asked for.* If the
agent has to be told to load `using-aethrion`, then the first turn — the one that
classifies the task and decides which discipline applies — happens without any
discipline. Every harness expects skills in a different place; the adapter's job
is to put them where each one looks.

This repository already does it for one harness: `.claude/skills` is a symlink to
`skills/`, which is why the 52 load here. That is one of five.

### Compaction and restart recovery (T24)

A loaded procedure lost to context compaction produces a run whose discipline
changed halfway through, and **nothing in the output shows it**. WP-043 T24 tests
survival; this package implements the recovery.

### Tool-name reconciliation is not cosmetic (T23)

Each harness names its tools differently. If the adapter does not reconcile them
against the `ToolBundle`, a policy written against `web_search` silently fails to
match a harness calling it `WebSearch` — and a control that does not match is a
control that does not apply.

### The harness acceptance suite is what makes the claim testable (T26)

The same task, the same expected skill set, every harness. Without it,
"interchangeable" is an intention. With it, a harness that quietly behaves
differently is a failing test rather than a surprise months later.

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


### The adapters implement a contract, and the contract is AETHRION's

`ADR-020`. This package predates the decision that gave it a boundary, and the
difference matters: an adapter written against a product couples the scientific
domain model to that product's API, while an adapter written against
`AgentRuntime` leaves the product replaceable.

The contract is small and deliberately semantic rather than protocol-shaped:

```text
qualify(runtime_profile)      start_session(actor, profile, workspace, context)
send_task(session, payload)   stream_events(session)   cancel(session)
collect_result(session)       close(session)
```

Where a harness speaks the Agent Client Protocol, ACP is the transport for that
contract and nothing more. **ACP protocol fields do not appear in the scientific
domain model.** It may carry sessions, working directories, messages, capabilities
and lifecycle signals; it may not redefine role, evidence, gate or challenge
semantics.

### A completion signal is an observation

A runtime reporting `completed`, a tool reporting success, an assistant
producing confident closing text — each is an operational observation about a
process, and none is a statement about the work. Acceptance still requires fresh
tests bound to a revision, a signed evidence manifest and an independent
verifier. **A runtime exit code is not `TECH_COMPLETE`.**

### Hermes is preferred, and preference is not architecture

Hermes is the default general-purpose profile where its qualification fits the
task. Codex, Claude Code, Buzz Agent and future ACP-compatible runtimes stay
selectable, and the layer is only real while more than one of them is. Runtime
diversity is also not independence: several actors on one runtime may still be
one contribution, because `CognitiveDiversityProfile` weighs cognitive function,
evidence exposure, peer visibility, model profile and prompt perspective —
`ADR-011`, unchanged.

Runtime-local memory is a convenience. It is never epistemic memory, and a cache
cannot promote itself into `Evidence` or `Principle` — the Context Projector
decides what an invocation sees.

### Bootstrap access is a named profile, not a phase

Before the Tool Broker exists, an isolated worker may hold direct shell and file
access inside its own worktree. That is recorded as `BOOTSTRAP_EXECUTION_PROFILE`,
scoped to a target, credential-limited, and **retired** rather than reclassified
as production-ready because it kept working. The permanent path is
`ToolIntent → Tool Broker → PolicyDecision → Execution Broker`.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md) | `Git policy` · `Worktree controller contract` · `Protected-path rules` · `Freeze procedure` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |

### Full prerequisite closure

**38 of 160 packages (24%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 23 | `WP-047` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-107`
- **Transitively reachable:** **23 of 160 packages (14%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **24** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Agent Runtime Lead |
| Independent verifier | Security / Eval Office |
| Gates touched | `G5` · `Engineering` |
| Controls | `CTL-SEC-03` · `CTL-SEC-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-46 — Task Runs With No Skill Loaded](../12_ACCEPTANCE_SCENARIOS/ACC-46_skill_not_loaded.md) | Critical | The task is blocked before any production step, the divergence between `skills_required` and `skills_loaded` is recorded as a finding, and no `AgentResult` is emitted. |
| [ACC-47 — Harness Starts Without the Skill Bootstrap](../12_ACCEPTANCE_SCENARIOS/ACC-47_skill_bootstrap_missing.md) | Critical | The adapter refuses the task with an explicit bootstrap failure; it does not fall back to an unguided session, and the refusal is distinguishable in the audit trail from a task that ran and failed. |
| [ACC-49 — Non-Waivable Skill Ignored Under Pressure](../12_ACCEPTANCE_SCENARIOS/ACC-49_skill_ignored_under_pressure.md) | Critical | The iron law holds; the attempted evasion and its verbatim justification are captured; the task cannot reach a completion claim. |
| [ACC-50 — Procedure Lost to Context Compaction or Restart](../12_ACCEPTANCE_SCENARIOS/ACC-50_skill_lost_on_compaction.md) | High | The procedure is restored or the task halts; it never continues silently without it, and the recovery is visible in the audit trail. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md)
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
| `Git policy` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Worktree controller contract` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Protected-path rules` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Freeze procedure` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `LangGraph runtime` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Temporal adapter` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Checkpoint policy` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Agent graph SDK` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Conformance tests` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `CollaborationDeploymentPlan` | `WP-047` | `python3 scripts/progress.py show WP-047` |

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
- **Agent Runtime Lead** carries the acceptance decision; **Security / Eval Office** must verify independently of whoever implements.
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
| `CMP-005` — Inspect AI | `DEPENDENCY` | The evaluation engine: dataset/solver/scorer execution, sandboxing, limits, retry/resume and transcripts. | The behaviours themselves, their pass criteria, the golden sets and the contamination controls — encoded as Inspect tasks, solvers and scorers. | **2** |
| `CMP-046` — buzz-acp — Agent Client Protocol runtime bridge | `DEPENDENCY` | Session transport, runtime process lifecycle and the protocol wire format. | The internal `AgentRuntime` contract — `qualify`, `start_session`, `send_task`, `stream_events`, `cancel`, `collect_result`, `close` — and the `AgentRuntimeProfile` that says which runtime may satisfy which requirement. | **1** |
| `CMP-047` — Hermes — general-purpose cognitive runtime | `OPTIONAL_BACKEND` | The runtime's own reasoning and tool loop, session-local state, tool-call formatting and harness behaviour. | `AgentRuntimeProfile` and its qualification: which runtime may host which cognitive function, with what capabilities, under which clean-context guarantee. | **1** |
| `CMP-048` — Buzz Agent — bundled runtime and `SKILL.md` workspace discovery | `OPTIONAL_BACKEND` | Runtime-side discovery of `SKILL.md` from `.agents/skills`, `.goose/skills` and `.claude/skills`, and git/worktree-aware workspace handling. | The Skill Compiler: which skills a given actor may see, materialised as a small task-specific bundle in that actor's worktree. | **1** |
| `CMP-049` — Codex CLI | `OPTIONAL_BACKEND` | The runtime's own agent loop, model interaction and local tool interface. | `AgentRuntimeProfile` and its qualification record — which runtime may host which cognitive function, with which capabilities, under which clean-context guarantee. | **1** |
| `CMP-050` — Claude Code | `OPTIONAL_BACKEND` | The runtime's own agent loop, harness behaviour, skill loading and local tool interface. | `AgentRuntimeProfile` and its qualification record — which runtime may host which cognitive function, with which capabilities, under which clean-context guarantee. | **1** |
| `CMP-051` — OpenCode | `OPTIONAL_BACKEND` | The runtime's own agent loop and local tool interface. | `AgentRuntimeProfile` and its qualification record — which runtime may host which cognitive function, with which capabilities, under which clean-context guarantee. | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `CMP-005` | A scorer result is a `VerificationResult`, never a `GateRecord` verdict. Inspect measures; gate policy decides. An Inspect transcript is operational evidence and is not the canonical run record. | Inspect as the canonical evidence store, and its scores as claim confidence. |
| `CMP-046` | ACP is a transport and interop boundary, never a scientific domain model. It may not redefine role, evidence, gate or challenge semantics, and an ACP event such as `completed` or `tool succeeded` is an operational observation — acceptance still depends on fresh tests, an evidence manifest and independent verification. | ACP protocol fields leaking into the scientific domain model, and runtime completion treated as package completion. |
| `CMP-047` | A runtime executes cognition; it defines nothing. Hermes may not decide what a scientific role is, whether a cohort is sufficient, whether a gate passes, whether a claim is accepted, whether a reviewer is independent, whether a protocol may change, or whether a tool effect is authorised. Runtime-local memory or cache is a convenience and can never promote itself into epistemic memory — the … | Hermes as the task compiler, the collaboration fabric or a role name. **`Hermes` is not a role**: `Statistician` is a cognitive function and may run on any qualified runtime. |
| `CMP-048` | Discovery decides what a runtime can find; it never decides what an actor may use. A skill reachable through a shared home directory but absent from the compiled bundle is a containment failure, and the canonical skill tree with its vendored provenance stays in this repository — a workspace holds a projection, never a second source of truth. | Exposing all 52 skills to every actor · Persona Packs as authoritative skill packaging · a runtime workspace as the canonical skill source · Buzz Agent's direct shell and file tools as anything but an explicitly classified bootstrap execution profile. |
| `CMP-049` | A runtime executes cognition and defines nothing. It may not decide what a scientific role is, whether a cohort is sufficient, whether a gate passes, whether a claim is accepted, whether a reviewer is independent, or whether a tool effect is authorised. Its completion signal is an operational observation: acceptance still depends on fresh tests, an evidence manifest and an independent verifier. | The harness as a role name, its session memory as epistemic memory, and its direct tool access as anything but a classified bootstrap execution profile. |
| `CMP-050` | A runtime executes cognition and defines nothing. It may not decide what a scientific role is, whether a cohort is sufficient, whether a gate passes, whether a claim is accepted, whether a reviewer is independent, or whether a tool effect is authorised. Its completion signal is an operational observation: acceptance still depends on fresh tests, an evidence manifest and an independent verifier. | The harness as a role name, its session memory as epistemic memory, and its direct tool access as anything but a classified bootstrap execution profile. |
| `CMP-051` | A runtime executes cognition and defines nothing. It may not decide what a scientific role is, whether a cohort is sufficient, whether a gate passes, whether a claim is accepted, whether a reviewer is independent, or whether a tool effect is authorised. Its completion signal is an operational observation: acceptance still depends on fresh tests, an evidence manifest and an independent verifier. | The harness as a role name, its session memory as epistemic memory, and its direct tool access as anything but a classified bootstrap execution profile. |

### Where a plain row would mislead

- **`CMP-046`** — The reason this is a dependency rather than something built here: runtime-harness interoperability is non-differentiating infrastructure, and coupling AETHRION's roles to one harness API is the coupling ADR-020 exists to prevent.
- **`CMP-047`** — WP-048 already names Hermes among its harness adapters; what changes is that it is now a profile behind a contract rather than an adapter written against one product.
- **`CMP-049`** — Named in WP-048's title and in WP-107's engineering slice, and registered by no one until now.
- **`CMP-050`** — This repository is itself operated through this runtime, which is a reason to state the boundary rather than to assume it: the harness that writes the plan holds no authority over what the plan accepts.
- **`CMP-051`** — Carried because WP-048 commits to more than one alternative harness; a runtime layer with a single alternative is not a runtime layer.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`CMP-005` — Inspect AI** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**`CMP-046` — buzz-acp — Agent Client Protocol runtime bridge** · `DEPENDENCY` · status `PROPOSED`

- what happens when it is unavailable, slow or wrong

**`CMP-047` — Hermes — general-purpose cognitive runtime** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**`CMP-048` — Buzz Agent — bundled runtime and `SKILL.md` workspace discovery** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**`CMP-049` — Codex CLI** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**`CMP-050` — Claude Code** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**`CMP-051` — OpenCode** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**Acquisition readiness — 8 obligations open across 7 of 7 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-048-T01 | Write the adapter interface and its lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-048-T02 | Implement the Codex non-interactive task adapter | Implementation owner | Commit / configuration / record reference |
| WP-048-T03 | Implement the OpenCode headless/server adapter | Implementation owner | Commit / configuration / record reference |
| WP-048-T04 | Implement the direct/local queue worker adapter | Implementation owner | Commit / configuration / record reference |
| WP-048-T05 | Bind worktree, sandbox and tool credentials | Implementation owner | Commit / configuration / record reference |
| WP-048-T06 | Add structured results, tracing, cancellation and failure normalisation | Implementation owner | Commit / configuration / record reference |
| WP-048-T20 | Add the **Claude Code** and **Hermes Agent** adapters alongside Codex, OpenCode and the direct worker | Implementation owner | One task executed end to end on each |
| WP-048-T21 | Implement **skill discovery and loading** per harness, at the location each expects | Implementation owner | Loaded-skill listing per harness |
| WP-048-T22 | Implement **automatic session bootstrap**: the router skill is present on the first turn without being asked for | Implementation owner | First-turn transcript per harness |
| WP-048-T23 | Map **tools** per harness and reconcile names with the `ToolBundle` | Implementation owner | Mapping table + negative test for an unmapped tool |
| WP-048-T24 | Implement **compaction and restart recovery** so the loaded procedure is not silently lost | Implementation owner | Recovery transcript per harness |
| WP-048-T25 | Return a **structured result** and an audit trace, including cancellation | Implementation owner | Result schema conformance per harness |
| WP-048-T26 | Run the **harness acceptance suite** — the same task, the same expected skill set, every harness | Implementation owner | Cross-harness matrix |

| WP-048-T-A1 | Define the `AgentRuntime` contract and the `AgentRuntimeProfile` qualification record | Implementation owner | Commit / configuration / record reference |
| WP-048-T-A2 | Implement the ACP transport mapping without leaking protocol fields into the domain model | Implementation owner | Commit / configuration / record reference |
| WP-048-T-A3 | Implement clean-context invocation for reviewer and verifier actors | Implementation owner | Commit / configuration / record reference |
| WP-048-T-A4 | Record the execution fingerprint: runtime profile, implementation version, transport version, model snapshot, prompt/role/skill digests, context digest, workspace digest | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Runtime adapter SDK`
- `Codex adapter`
- `OpenCode adapter`
- `Direct worker adapter`
- `Conformance report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

### Minimum adapter contract

Every harness adapter implements the same surface, or it is not an adapter:

| Capability | Why it is mandatory |
|---|---|
| skill discovery · loading · **automatic bootstrap** | A skill that does not load governs nothing |
| tool mapping · context injection | The `ToolBundle` must mean the same thing everywhere |
| session and **compaction recovery** | Governance must survive the context window |
| structured result · cancellation · audit trace | A run that cannot be audited is not evidence |

> **Format compatibility is not behavioural compatibility.** Conformance to the
> Agent Skills format makes the registry *loadable* by Claude Code, Codex,
> OpenCode, Cursor, Copilot, Gemini CLI and Hermes Agent. Whether each harness
> actually loads the right skill at the right moment is what the acceptance
> suite in this package establishes, and it is **not** established today.

- `AgentRuntime` contract
- `AgentRuntimeProfile`
- `BOOTSTRAP_EXECUTION_PROFILE` classification and its retirement condition

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-048_codex_opencode_adapters.tests.md`](WP-048_codex_opencode_adapters.tests.md).

- The same canonical task producing schema-compatible results across all three adapters
- Cancellation and timeout normalisation
- A permission and path negative test
- Recovery from runtime session loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks
- The same cognitive function must run on two qualified runtimes without changing role semantics or cohort identity
- A runtime lacking a required capability must be rejected at qualification, not discovered at run time
- A reviewer or verifier in clean context must not inherit implementer state
- A runtime completion signal must not be sufficient to move a package state

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-048_codex_opencode_adapters.acceptance.md`](WP-048_codex_opencode_adapters.acceptance.md), together with what this package still cannot establish.

- [ ] A runtime session is never AIRL workflow state.
- [ ] No adapter receives a raw provider secret.
- [ ] Results conform to the canonical `AgentResult` and artifact contract.
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

An adapter can be disabled individually; the task is dispatched to another eligible adapter under a new execution lease.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
