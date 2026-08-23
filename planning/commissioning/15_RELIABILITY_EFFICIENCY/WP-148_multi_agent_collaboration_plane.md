# WP-148 — Multi-Agent Collaboration Plane and Cohort Integrity

## Package card

| Field | Value |
|---|---|
| Work package | `WP-148` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Chief Architect |
| Hard dependencies | WP-007, WP-013, WP-046, WP-047, WP-147 |
| Related gates | G1,G2,G4,G6 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-081, ACC-082, ACC-089, ACC-090 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-148_multi_agent_collaboration_plane.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-148_multi_agent_collaboration_plane.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A substantial scientific task compiles to a cohort of epistemically independent cognitive contributions whose first positions are sealed before any of them sees another's.


## Analysis

### What this package actually decides

That a substantial scientific task cannot be carried by one cognitive actor, and
that the system refuses it at compile time rather than warning about it.

`ADR-011` gives the reason: this system is built against **plausibility**, not
against low capability, and a second independent look is the only mechanism that
sees what the first could not. Cutting the cohort to save tokens trades the thing
the system exists for against the thing it costs.

### Independence is a profile, not a count

Two instances of the same model on the same context are one contribution. They
will agree, and the agreement carries no information.

`CognitiveDiversityProfile` records five dimensions instead: cognitive function,
evidence exposure, peer visibility, model profile, prompt perspective. Model
diversity is necessary and **not sufficient** — ACC-081 refuses a cohort of five
identical profiles and passes one of three differentiated ones.

### Why order is the mechanism

Peer output is hidden for round zero. Each actor produces an
`InitialPositionArtifact`; the artifacts are **sealed**; only then are material
differences exposed for targeted exchange.

Anchoring is an effect rather than a preference. An actor shown a confident prior
answer converges on it, and the record afterwards shows two agreeing actors —
indistinguishable from two that independently agreed. Sealing the first position
is the only thing that makes the difference legible later, and it has to happen
before the exposure rather than be reconstructed after it.

### Convergence is not a vote

A cohort converges when no material methodological challenge is unresolved, no
critical evidence contradiction is open, and every protocol blocker is closed or
explicitly escalated.

Four actors agreeing does not close a skeptic's unanswered objection. That is the
whole content of ACC-090, and it is the rule that separates this from a majority
mechanism: **the minority position is what the cohort was convened to
produce**, and a convergence rule that can outvote it has spent the cost of the
cohort and discarded the return.


### The plane is AETHRION's; the substrate underneath it is not

`ADR-020`. Most of what this plane needs operationally — identities, teams,
rooms, message transport, presence, runtime attachment, a workspace a human can
watch — is not scientific, is genuinely solved elsewhere, and would consume most
of this package's budget while differentiating nothing. So it is adopted behind a
`CollaborationBackend` contract, with Buzz as the first candidate.

Everything above the contract stays exactly as this package already specifies it:
`AgentCohortRecord`, `CognitiveDiversityProfile`, the sealed
`InitialPositionArtifact`, `MaterialChallenge`, and convergence that is not a
vote. The backend is told what must happen and reports what it did.

### The architectural test, and it is not rhetorical

**If the backend disappears, which truths disappear?** Rooms, presence, message
history and operational coordination are acceptable losses. Gate state, claims,
evidence spans, verified values, protocol freeze, human decisions, experiment
lineage, reproduction records and accepted artifacts are not. If any of those
depends on backend state, the integration is wrong rather than fragile — and
`T12` below exists to demonstrate the answer rather than assert it.

### A backend identity is not a cohort, and five of them are not five contributions

The temptation the substrate creates is arithmetic: five identities in a room
look like a cohort. They are one contribution if they share a model profile and a
context, and `ADR-011`'s five-dimension profile is what says so. Backend identity
count is not an input to `CognitiveDiversityProfile` and must not become one.

Nor is an operational identity a `RoleBinding`. Cryptographic identity supports
attribution; it does not establish that an actor holds a governance role.
Attribution and authorisation are different questions, and the mapping is
`backend identity + runtime session + cohort actor id + RoleContract` — four
things joined, never four things equated.

### Qualification is characterisation, not a successful message

A backend is qualified by fifteen behaviours, of which the load-bearing one is
isolation: identity persistence, roster deployment, targeted versus broadcast
delivery, thread ordering, reconnect and restart, runtime attachment, worktree-
aware workspace behaviour, skill discovery precedence and duplicate handling,
audit export completeness, unavailability behaviour, **round-zero peer isolation**,
**sparse graph materialisation without accidental all-to-all visibility**,
retention and deletion, credential exposure, and upgrade drift across pins.

Sending a message between two agents proves none of it.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-147 — Scientific Council and Meta-Review Cognition](../14_SCIENTIFIC_INTELLIGENCE/WP-147_scientific_council_cognition.md) | `CognitiveFunction profile` · `ScientificCouncilSession` · `Recommendation schema` · `Parallel council isolation mode` |

### Full prerequisite closure

**78 of 160 packages (49%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` · `WP-141` |
| 28 | `WP-062` · `WP-081` · `WP-142` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-147` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-149` · `WP-152`
- **Transitively reachable:** **8 of 160 packages (5%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **38** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Chief Architect |
| Gates touched | `G1` · `G2` · `G4` · `G6` |
| Controls | `CTL-GOV-02` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-081 — Multi-Agent Cohort Required](../12_ACCEPTANCE_SCENARIOS/ACC-081_multi_agent_cohort_required.md) | Critical | Compilation refuses, or adds the independent cognitive actors the invariant requires. There is no silent single-agent downgrade, and a cohort of several instances of the same model profile on the same context does not satisfy the requirement either. |
| [ACC-082 — Independent-First Embargo](../12_ACCEPTANCE_SCENARIOS/ACC-082_independent_first_embargo.md) | Critical | The pre-seal request is denied and audited. The post-seal request succeeds through the protocol path, and only the material differences are exposed rather than the full prior output. |
| [ACC-089 — Sycophancy Anchor Attack](../12_ACCEPTANCE_SCENARIOS/ACC-089_sycophancy_anchor_attack.md) | Critical | The independent-first embargo means no member saw the wrong anchor before forming a position. The wrong position does not become consensus, and the sycophancy diagnostic reports the agreement pattern. |
| [ACC-090 — False Consensus Cannot Close a Challenge](../12_ACCEPTANCE_SCENARIOS/ACC-090_false_consensus.md) | Critical | Convergence is refused while the challenge is unresolved. A majority cannot close it. It closes by being answered, by being explicitly accepted as a stated limitation, or by escalating. |
| [ACC-091 — Faulty Agent Output Does Not Propagate](../12_ACCEPTANCE_SCENARIOS/ACC-091_faulty_agent_challenge.md) | Critical | The faulty output is challenged rather than absorbed, does not reach any canonical record, and the failure is classified and routed. The Challenger's finding does not itself close a gate. |
| [ACC-093 — A Malicious Agent Cannot Bind Authority](../12_ACCEPTANCE_SCENARIOS/ACC-093_malicious_agent_cannot_bind_authority.md) | Critical | Every attempt is denied and audited. No agent can bind authority under any circumstance — authority is held by Temporal, by the signed decision path and by policy, none of which an agent can reach. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role and **Skill** Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-147 — Scientific Council and Meta-Review Cognition](../14_SCIENTIFIC_INTELLIGENCE/WP-147_scientific_council_cognition.md)
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
| `CognitiveFunction profile` | `WP-147` | `python3 scripts/progress.py show WP-147` |
| `ScientificCouncilSession` | `WP-147` | `python3 scripts/progress.py show WP-147` |
| `Recommendation schema` | `WP-147` | `python3 scripts/progress.py show WP-147` |
| `Parallel council isolation mode` | `WP-147` | `python3 scripts/progress.py show WP-147` |
| `Synthesis and meta-review output` | `WP-147` | `python3 scripts/progress.py show WP-147` |

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
- **Research Director** carries the acceptance decision; **Assurance Lead / Chief Architect** must verify independently of whoever implements.
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
| `ASM-041` — CONSENSAGENT — sycophancy as a reliability and cost problem | `ADAPTIVE_REIMPLEMENT` | `MS-COHORT-001` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-042` — MAS-Resilience — faulty-agent resilience, Challenger and Inspector | `ADAPTIVE_REIMPLEMENT` | `MS-RESIL-001` · `MS-RESIL-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-060` — Buzz Harbor Orchestra — frozen roster manifest for a cohort run | `DIRECT_ADAPT` | `benchmarks/harbor-buzz-orchestra/src/harbor_buzz_orchestra/manifest.py` · `benchmarks/harbor-buzz-orchestra/tests/test_manifest.py` | the local module and contract surface this becomes — **named at refinement** | **2** |
| `ASM-063` — Buzz — signed collaboration event and audit export | `PATTERN` | the idea only — no code and nothing called at runtime | everything — the implementation here is this repository's own | none |
| `CMP-045` — Buzz — collaboration relay, teams, rooms and agent identities | `OPTIONAL_BACKEND` | Operational collaboration: identity material, team and roster deployment, room and thread creation, message transport and targeted delivery, agent presence, runtime process attachment, and the collaboration activity feed. | The `CollaborationBackend` contract and everything above it: `AgentCohortRecord`, `CognitiveDiversityProfile`, `CommunicationGraph`, `CommunicationEdgePolicy`, `TypedAgentMessage`, `InitialPositionArtifact` and the round-zero embargo. AETHRION compiles *what collaboration must happen*; the backend is told, and reports … | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-041` | A sycophancy diagnostic is a measurement of how a cohort behaved. It is not a verdict on whether the cohort was right, and agreement is never evidence. | The prompt-refinement optimiser. Its purpose is to reach consensus faster; here consensus is not the goal, and a mechanism that accelerates agreement is the wrong lever on a system whose failure mode is agreement. |
| `ASM-042` | A Challenger targets assumptions and a Inspector checks consistency. Neither holds gate authority, and a clean Inspector result satisfies no required verification — ACC-092. | **The source code, because of the licence.** GPL-3.0 is incompatible with this repository's proprietary licence, so no file may be copied under any circumstance. The mechanism is specified from the paper and written natively — which ADR-004 permits and ADR-019 requires to be recorded. |
| `ASM-060` | A manifest records what a cohort run was configured with. It is never evidence that the run was scientifically adequate, and a frozen roster does not establish epistemic independence — five identities on one model and one context are one contribution, whatever the manifest says. | The shared-filesystem execution model, the orchestrator's own scheduling semantics, and any notion that completing the manifest completes the work. AETHRION worktree isolation, cohort versioning and acceptance rules are unchanged. |
| `ASM-063` | A signed collaboration event attributes an operational act to an operational identity. It does not prove that identity held an AETHRION governance role at the time, and it is not admissible as evidence for a claim. Attribution and authority are different questions. | The event store as the audit ledger — that is WP-099's WORM ledger — and cryptographic identity as `RoleBinding`. |
| `CMP-045` | A collaboration backend carries messages and holds no scientific authority whatever. A Buzz message is not a `ClaimVersion`, a Buzz room is not the blackboard, a Buzz workflow is not a gate transition, and a Buzz approval is not a `DecisionRecord`. Removing the backend entirely must lose no claim, evidence span, verified value, gate state, protocol freeze, human decision, experiment lineage, … | Relay state as canonical scientific truth · channel history as the Claim/Evidence store · workflow state as G0–G10 lifecycle authority · approvals as G8/G9 authority · free-for-all shared-channel visibility as the scientific default · operational agent identity as a `RoleBinding` · direct shell … |

### Where a plain row would mislead

- **`ASM-041`** — Frames sycophancy as agents reinforcing one another instead of engaging critically, which inflates cost through extra debate rounds. Evaluated on six reasoning datasets across three models. The mechanism taken is the diagnostic and the framing; the convergence rule here is unresolved-material-challenge closure rather than agreement — ACC-089, ACC-090.
- **`ASM-042`** — Reports that a hierarchical A→(B↔C) topology degrades least under faulty agents — 5.5% against 10.5% and 23.7% — and that Challenger and Inspector recover up to 96.4% of injected errors. Its AutoTransform and AutoInject fault-injection methods are the model for this baseline's faulty-agent fixtures. **This entry is the register's worked example of a licence changing the method rather than the decision.**
- **`ASM-060`** — The mechanism worth taking is narrow and real: an execution manifest that freezes roster, model revision, prompt digest, budget envelope and concurrency before a run starts, so what ran can be reconstructed afterwards. That maps almost exactly onto `AgentCohortRecord` plus the budget envelope, and it is the shape WP-153's ledger needs upstream of it. **Read at the source on 2026-08-24.** The LICENSE file at the pinned tree is the unmodified Apache License 2.0 — nine numbered sections, the standard appendix, no non-commercial clause, no field-of-use restriction and no added term — under …
- **`ASM-063`** — The provenance surface is genuinely good, which is why the boundary has to be stated: a well-signed record of the wrong kind of fact is more persuasive than an unsigned one, not less.
- **`CMP-045`** — Buzz appears in both registers and the two entries are different subjects: this row is the runtime collaboration substrate, while `ASM-060`–`ASM-063` record specific mechanisms taken from the same project. Prototype-grade and moving at review, so a floating `main` is not an acceptable dependency — see WP-159.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-041` — CONSENSAGENT — sycophancy as a reliability and cost problem** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-042` — MAS-Resilience — faulty-agent resilience, Challenger and Inspector** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-060` — Buzz Harbor Orchestra — frozen roster manifest for a cohort run** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a characterisation suite capturing upstream behaviour **before** any code moves

**`CMP-045` — Buzz — collaboration relay, teams, rooms and agent identities** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**Acquisition readiness — 5 obligations open across 4 of 5 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-148-T01 | Define `AgentCohortRecord` with its digest and its binding to `TaskContract` | Implementation owner | Commit / configuration / record reference |
| WP-148-T02 | Define `CognitiveDiversityProfile` across the five independence dimensions | Implementation owner | Commit / configuration / record reference |
| WP-148-T03 | Implement the independent-first scheduler and `InitialPositionArtifact` sealing | Implementation owner | Commit / configuration / record reference |
| WP-148-T04 | Implement material-difference extraction and targeted exposure | Implementation owner | Commit / configuration / record reference |
| WP-148-T05 | Implement `MaterialChallenge` tracking and the convergence rule | Implementation owner | Commit / configuration / record reference |
| WP-148-T06 | Bind cohort compilation into the Task Compiler under the independence profile | Implementation owner | Commit / configuration / record reference |
| WP-148-T07 | Emit cohort integrity and diversity metrics to the metascience plane | Implementation owner | Commit / configuration / record reference |

| WP-148-T08 | Define `CollaborationBackendProfile` — capabilities, identity model, transport semantics, room model, runtime attachment, audit export, isolation, failure semantics, qualification record | Implementation owner | Commit / configuration / record reference |
| WP-148-T09 | Define the `CollaborationBackend` contract and the actor-identity mapping | Implementation owner | Commit / configuration / record reference |
| WP-148-T10 | Implement the Buzz adapter skeleton against the contract, with no Buzz term in the domain model | Implementation owner | Commit / configuration / record reference |
| WP-148-T11 | Run the fifteen-behaviour characterisation suite against a pinned backend | Implementation owner | Commit / configuration / record reference |
| WP-148-T12 | Demonstrate backend loss: destroy all collaboration state and show every canonical record survives | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `AgentCohortRecord`
- `CognitiveDiversityProfile`
- `InitialPositionArtifact`
- `MaterialChallenge`
- `ConvergenceAssessment`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

- `CollaborationBackendProfile`
- `CollaborationBackend` contract
- Backend capability matrix and qualification record
- Round-zero isolation proof on the qualified backend
- Backend-loss reconstruction proof

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-148_multi_agent_collaboration_plane.tests.md`](WP-148_multi_agent_collaboration_plane.tests.md).

- A single-actor compile of a substantial task must be refused, not warned about
- A cohort of identical model profiles must not satisfy the independence requirement
- A peer output requested before the position lock must be denied and audited
- An unresolved material challenge must block convergence against a majority
- The cohort digest must be deterministic for the same compiled inputs
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

- Five backend identities on one model profile and one context must not satisfy cognitive diversity
- Actors under embargo must not read peer initial positions although they share one backend service
- A backend actor must not be able to bind AETHRION authority or move a gate
- Destroying and recreating all backend state must lose no claim, evidence span, finding, artifact or decision
- A backend that cannot enforce required isolation must fail qualification rather than run with the topology relaxed

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-148_multi_agent_collaboration_plane.acceptance.md`](WP-148_multi_agent_collaboration_plane.acceptance.md), together with what this package still cannot establish.

- [ ] A substantial task cannot compile to one cognitive actor, and the refusal names the invariant.
- [ ] Independence is evaluated from the diversity profile, never from actor count.
- [ ] Initial positions are sealed before any peer exposure, and the seal is checkable afterwards.
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

- An efficiency measure that improves a cost number and quietly lowers assurance has moved the failure, not removed it. Every optimisation here is anchored to a quality guard and rolls back when it trips.
- A coordination defect is invisible in a healthy run and obvious only in a post-mortem. These packages are specified as injection suites for that reason, not as properties.
- Multi-agent cost pressure always argues for fewer agents. The cohort is fixed by ADR-011 and is not a lever any package here may pull.

- - A collaboration substrate that is convenient acquires authority faster than one that is not; the boundary is enforced by contract and test, never by the intention of whoever wired it.

## Rollback / compensation

A cohort is superseded rather than edited: re-running a collaboration creates a new cohort record referencing the previous one, and the sealed initial positions of both are retained.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
