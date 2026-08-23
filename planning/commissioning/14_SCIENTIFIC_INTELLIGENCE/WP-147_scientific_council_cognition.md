# WP-147 — Scientific Council and Meta-Review Cognition

## Package card

| Field | Value |
|---|---|
| Work package | `WP-147` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Internal Audit |
| Hard dependencies | WP-003, WP-007, WP-013, WP-046, WP-047, WP-086, WP-142 |
| Related gates | G1,G2,G4,G6 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-06, ACC-72 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-147_scientific_council_cognition.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-147_scientific_council_cognition.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Task-specific specialist cognition produces recommendations at design time without acquiring any of the authority that belongs to governance roles, verifiers or reviewers.


## Analysis

### What this package actually decides

The boundary between thinking and deciding. Multi-specialist deliberation is
genuinely useful before a protocol is frozen — a methodologist, a statistician, an
experimentalist and a skeptic looking at the same design will find different
things wrong with it. What it must not become is a second authority structure.

So a `CognitiveFunction` is defined as a distinct concept from a `RoleContract`.
A council session emits a `Recommendation`. It cannot write a `GateRecord`, a
`ClaimVersion`, an `EvidenceSpan` or a `ReviewVerdict`, and that is enforced by
the authority matrix rather than stated as an expectation.

### Four things the documents must stop conflating

A governance role is accountability. A cognitive function is a way of thinking
about a problem. A runtime actor is the worker that executes. A model profile is
which model, at which snapshot, with which parameters.

These are four independent axes, and the failure mode of importing council
patterns from published systems is that their cognitive roles get written into
architecture documents as though they were governance roles. Fourteen durable
governance functions do not become twenty-one because a council has seven seats.

### Advice at design time is not review at assurance time

A council that helped shape a protocol at G2 is not a candidate reviewer for the
result at G6, and reusing the same role or model profile for both would let the
design's own assumptions grade the design's own output.

The task compiler binds council functions and reviewer roles separately, and the
independence profile records the constraint. ACC-06 already asserts that a planner
cannot approve its own plan; this package extends the same principle to
cognition.

### Parallel councils, and what synthesis must not lose

Where the design risk is high, two councils can run isolated from each other and
be synthesised after both are locked. That only means something if the isolation
is real, which is why it is tested rather than declared.

Synthesis has one hard constraint: a minority objection survives it. A meta-review
that produces a clean consensus by dropping the one specialist who disagreed has
removed exactly the signal the exercise existed to produce, so the synthesis
record retains disagreements as first-class content and a planted minority finding
must still be present afterwards.

### Baseline v1.3.0 — the council gains a protocol

The scientific council stays dynamic multi-agent cognition and stays advisory.
What it gains is the collaboration protocol:

- **independent-first** — positions sealed before any peer exposure;
- **sparse topology** — targeted exchange on material differences, not
  everyone-to-everyone;
- **sycophancy diagnostics** — agreement-before-evidence is measured;
- **unresolved-challenge convergence** — a majority cannot close a material
  objection.

And the boundary that was already here, restated because this baseline adds
cognitive functions and the temptation grows with them: **the six cognitive
archetypes do not become governance roles.** Fourteen durable governance
functions remain fourteen.

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
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md) | `Review Package Builder` · `Blind/redaction rules` · `Package manifests` · `Leak detection tests` |
| [WP-142 — Study Mode, Bottleneck and Idea Card Model](../14_SCIENTIFIC_INTELLIGENCE/WP-142_study_mode_bottleneck_idea.md) | `StudyModeRecord` · `BottleneckRecord` · `IdeaCard` · `PriorArtCollision` |

### Full prerequisite closure

**77 of 160 packages (48%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-148`
- **Transitively reachable:** **9 of 160 packages (6%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **37** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Internal Audit |
| Gates touched | `G1` · `G2` · `G4` · `G6` |
| Controls | `CTL-GOV-02` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-72 — Reviewer Isolation Before Review Lock](../12_ACCEPTANCE_SCENARIOS/ACC-72_reviewer_isolation_before_lock.md) | Critical | Both requests are denied before the lock. After the lock, the protocol's disclosure step permits the reveal. A scientific council recommendation in the packet is labelled as advice and carries no verdict. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/WP-003_role_catalog_raci.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role and **Skill** Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md), [WP-142 — Study Mode, Bottleneck and Idea Card Model](WP-142_study_mode_bottleneck_idea.md)
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
| `LangGraph runtime` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Temporal adapter` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Checkpoint policy` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Agent graph SDK` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Conformance tests` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Review Package Builder` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Blind/redaction rules` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Package manifests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Leak detection tests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `StudyModeRecord` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `BottleneckRecord` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `IdeaCard` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `PriorArtCollision` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `Gate policy bindings for G0-G2` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `Mode change deviation procedure` | `WP-142` | `python3 scripts/progress.py show WP-142` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Research Director** carries the acceptance decision; **Assurance Lead / Internal Audit** must verify independently of whoever implements.
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
| WP-147-T01 | Define `CognitiveFunction` as a profile distinct from `RoleContract` | Implementation owner | Commit / configuration / record reference |
| WP-147-T02 | Define `ScientificCouncilSession` and its recommendation output schema | Implementation owner | Commit / configuration / record reference |
| WP-147-T03 | Bind the authority matrix so council output can write no canonical verdict | Implementation owner | Commit / configuration / record reference |
| WP-147-T04 | Implement parallel independent council mode with enforced isolation | Implementation owner | Commit / configuration / record reference |
| WP-147-T05 | Implement synthesis and meta-review with minority-position retention | Implementation owner | Commit / configuration / record reference |
| WP-147-T06 | Bind council selection to the task compiler and the independence profile | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `CognitiveFunction profile`
- `ScientificCouncilSession`
- `Recommendation schema`
- `Parallel council isolation mode`
- `Synthesis and meta-review output`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-147_scientific_council_cognition.tests.md`](WP-147_scientific_council_cognition.tests.md).

- A council recommendation must not be writable as a gate or claim record
- Parallel councils must not observe one another before both are locked
- The task compiler must select only permitted functions and model profiles
- A planted minority disagreement must survive synthesis
- A council participant must not be bindable as the reviewer of the same artefact where the independence profile forbids it
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-147_scientific_council_cognition.acceptance.md`](WP-147_scientific_council_cognition.acceptance.md), together with what this package still cannot establish.

- [ ] A G1 or G2 design task produces independent specialist positions and a synthesis with no authority leakage.
- [ ] Council advice is labelled as recommendation everywhere it is stored or displayed.
- [ ] Governance role, cognitive function, runtime actor and model profile are four separate fields.
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

- A search or ranking score that becomes a claim confidence is a category error. It has to be refused by a schema, not remembered by a convention.
- A mechanism adapted without a characterisation test cannot be told apart from a mechanism that was misunderstood.
- Cognition that is permitted to recommend will be read as authority unless a field — not a paragraph — says it is not.

## Rollback / compensation

A council session is immutable once locked; re-running the exercise creates a new session that references the previous one rather than replacing it.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
