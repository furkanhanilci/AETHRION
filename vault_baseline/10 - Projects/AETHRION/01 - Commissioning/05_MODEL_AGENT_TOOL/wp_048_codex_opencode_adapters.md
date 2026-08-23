---
title: "WP-048 — Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker"
aliases:
  - "WP-048"
  - "WP-048 — Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Different agent runtimes become interchangeable adapters that all satisfy the same TaskContract, isolation, tool, result, audit and cancellation contract."
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-048_codex_opencode_adapters.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/engineering
  - aethrion/state/not-started
---

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
| [Test procedures](wp_048_codex_opencode_adapters.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_048_codex_opencode_adapters.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

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

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md) | `Git policy` · `Worktree controller contract` · `Protected-path rules` · `Freeze procedure` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |

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
- **Transitively reachable:** **27 of 160 packages (17%)** cannot be accepted until this one is.

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

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md)
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

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-048_codex_opencode_adapters.tests.md`](wp_048_codex_opencode_adapters.tests.md).

- The same canonical task producing schema-compatible results across all three adapters
- Cancellation and timeout normalisation
- A permission and path negative test
- Recovery from runtime session loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-048_codex_opencode_adapters.acceptance.md`](wp_048_codex_opencode_adapters.acceptance.md), together with what this package still cannot establish.

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
