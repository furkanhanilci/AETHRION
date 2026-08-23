# WP-153 — Research Budget, Token Ledger and Efficiency Control

## Package card

| Field | Value |
|---|---|
| Work package | `WP-153` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | FinOps Lead |
| Independent verifier | Research Director / SRE Lead |
| Hard dependencies | WP-100, WP-145, WP-150 |
| Related gates | G4,G5,G6 |
| Related controls | CTL-OPS-02, CTL-EPI-03 |
| Related acceptance scenarios | ACC-099, ACC-100, ACC-101, ACC-102 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-153_research_budget_and_token_ledger.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-153_research_budget_and_token_ledger.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Research spend is contracted across nine dimensions and accounted by category, and running low degrades how much agents say — never whether the cohort exists or which assurance it owes.


## Analysis

### What this package actually decides

What happens as a research budget runs out, and the answer that this package
exists to refuse: not *shut down the team*.

`ResearchBudgetContract` extends WP-145's campaign budget across tokens, tool
calls, literature retrieval, experiment compute, **communication**, verification,
reproduction reserve, wall-clock and human attention.

### Categorised, because the aggregate hides the problem

`TokenLedgerEntry` classifies every token: `SCIENTIFIC_REASONING`,
`INTER_AGENT_COMMUNICATION`, `EVIDENCE_RETRIEVAL`, `TOOL_IO`, `VERIFICATION`,
`SYNTHESIS`, `SYSTEM_OVERHEAD`.

A single total tells you a campaign was expensive. The categories tell you
whether it was expensive because it did science or because it held a meeting, and
only the second is worth optimising. Coordination overhead ratio — the share in
`INTER_AGENT_COMMUNICATION` — is the number WP-149 and WP-150 are measured on.

### Degradation order, and what is outside it

As budget falls, communication policy degrades first:

```
structured full → compressed → pointer-only → silence unless material
```

**Outside the degradation path entirely:** the cohort (`ADR-011`), the assurance
route (`ADR-015`), and every non-waivable control. A task that cannot afford its
required assurance becomes `BLOCKED_BUDGET` or requests a scope reduction — it
does not proceed more cheaply — ACC-099, ACC-101.

### Tool-result reuse

A deterministic tool call with identical inputs inside one campaign is served
from a recorded result rather than re-executed — ACC-102. The reuse is recorded,
so a reader can tell a cached result from a fresh one, and reuse never crosses a
freshness boundary the protocol declares.

### The Pareto rule

An optimisation is judged on the quality/cost frontier, not on cost alone.
A change buying +0.2% quality for +400% cost is not accepted silently, and neither
is its mirror image. Both directions need an explicit decision, and the frontier
is what a release reports — WP-130.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |
| [WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control](../14_SCIENTIFIC_INTELLIGENCE/WP-145_search_selection_fusion_stagnation.md) | `Selection mechanism specification` · `SearchPolicyConfig` · `FusionProposal` · `StagnationDetector` |
| [WP-150 — Communication Governor, Edge Utility and Context Projection](../15_RELIABILITY_EFFICIENCY/WP-150_communication_governor_and_context_projection.md) | `CommunicationValue` · `CommunicationUtilityRecord` · `ContextProjectionRecord` · `Quality guard and rollback` |

### Full prerequisite closure

**87 of 160 packages (54%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` · `WP-143` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-096` · `WP-144` |
| 31 | `WP-068` · `WP-071` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-145` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-147` |
| 38 | `WP-148` |
| 39 | `WP-149` |
| 40 | `WP-150` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **41** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | FinOps Lead |
| Independent verifier | Research Director / SRE Lead |
| Gates touched | `G4` · `G5` · `G6` |
| Controls | `CTL-OPS-02` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-099 — Budget Degrades Communication, Not the Cohort](../12_ACCEPTANCE_SCENARIOS/ACC-099_communication_budget_degradation.md) | Critical | Communication policy degrades — structured, compressed, pointer-only, silence unless material. The cohort is not reduced, the assurance route is not lowered, and no non-waivable control is skipped. |
| [ACC-100 — Token Ledger Classification](../12_ACCEPTANCE_SCENARIOS/ACC-100_token_ledger_classification.md) | High | Every token carries one of the seven categories, the categories sum to the total, and the coordination overhead ratio is derivable from the ledger rather than estimated. |
| [ACC-101 — Reserved Assurance Budget Is Unreachable](../12_ACCEPTANCE_SCENARIOS/ACC-101_budget_hard_stop_reserved_assurance.md) | Critical | The reserve is unreachable from the exploration path. The campaign stops on its exploration ceiling with the reserve intact, and the assurance work it was reserved for can still run. |
| [ACC-102 — Deterministic Tool-Result Reuse](../12_ACCEPTANCE_SCENARIOS/ACC-102_tool_result_reuse.md) | Medium | The second is served from the recorded result and marked as reused. The third re-executes because the freshness boundary forbids reuse. A reused result is distinguishable from a fresh one in the record. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md), [WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control](../14_SCIENTIFIC_INTELLIGENCE/WP-145_search_selection_fusion_stagnation.md), [WP-150 — Communication Governor, Edge Utility and Context Projection](WP-150_communication_governor_and_context_projection.md)
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
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Token ledger categories` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Selection mechanism specification` | `WP-145` | `python3 scripts/progress.py show WP-145` |
| `SearchPolicyConfig` | `WP-145` | `python3 scripts/progress.py show WP-145` |
| `FusionProposal` | `WP-145` | `python3 scripts/progress.py show WP-145` |
| `StagnationDetector` | `WP-145` | `python3 scripts/progress.py show WP-145` |
| `ResearchCampaignGovernor` | `WP-145` | `python3 scripts/progress.py show WP-145` |
| `CampaignStopRecord` | `WP-145` | `python3 scripts/progress.py show WP-145` |
| `CommunicationValue` | `WP-150` | `python3 scripts/progress.py show WP-150` |
| `CommunicationUtilityRecord` | `WP-150` | `python3 scripts/progress.py show WP-150` |
| `ContextProjectionRecord` | `WP-150` | `python3 scripts/progress.py show WP-150` |
| `Quality guard and rollback` | `WP-150` | `python3 scripts/progress.py show WP-150` |

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
- **FinOps Lead** carries the acceptance decision; **Research Director / SRE Lead** must verify independently of whoever implements.
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
| `ASM-039` — AgentSlimming — baseline-anchored workflow optimisation | `ADAPTIVE_REIMPLEMENT` | `MS-COMM-004` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-045` — BATS — budget-aware tool use and test-time scaling | `DIRECT_ADAPT` | `src/agent_budget_tracker.py` · `src/agent_bats.py` | the local module and contract surface this becomes — **named at refinement** | **3** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-039` | An importance score allocates optimisation effort. It cannot remove a cognitive contribution the multi-agent invariant requires — ADR-011. | **Node pruning and cheap-model substitution.** Upstream these are the point; here they are the one optimisation refused by name. The framework removes workflow nodes and replaces them with cheaper models, which applied to a scientific cohort is exactly the cost lever ADR-011 exists to refuse. |
| `ASM-045` | A remaining-budget signal changes what a campaign does next. It can never lower an assurance route, reduce a cohort or skip a non-waivable control — a task that cannot afford its assurance is BLOCKED. | Hard-coded provider pricing — cost data comes from the Model Gateway and the Cost Ledger. And the two-dimensional budget model: this architecture needs nine dimensions including communication, verification, reproduction reserve and human attention. |

### Where a plain row would mislead

- **`ASM-039`** — MIT-licensed and therefore legally adaptable, and still reimplemented — the taken mechanisms are multi-metric importance estimation, **baseline-anchored acceptance**, quality-regression rollback and Pareto reporting. The reported cost reduction was not confirmed on the repository page and is recorded here as a paper claim rather than an observed figure. This is the clearest entry in the register where a permissive licence does not make copying correct.
- **`ASM-045`** — Makes remaining tool budget part of the agent's continuous context, and uses it to decide between deepening a promising lead and pivoting. Apache-2.0 with two compact, isolable modules, which makes this the strongest direct-adaptation candidate added by this delta. Also carries intermediate summarisation and old-tool-response compression, which belong to the context projection rather than to the budget controller.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-039` — AgentSlimming — baseline-anchored workflow optimisation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-045` — BATS — budget-aware tool use and test-time scaling** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a pinned upstream commit — a branch name is not a pin
- a characterisation suite capturing upstream behaviour **before** any code moves

**Acquisition readiness — 4 obligations open across 2 of 2 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-153-T01 | Define `ResearchBudgetContract` across the nine dimensions | Implementation owner | Commit / configuration / record reference |
| WP-153-T02 | Define `TokenLedgerEntry` and its seven categories | Implementation owner | Commit / configuration / record reference |
| WP-153-T03 | Implement the communication degradation ladder | Implementation owner | Commit / configuration / record reference |
| WP-153-T04 | Place cohort, assurance route and non-waivable controls outside degradation | Implementation owner | Commit / configuration / record reference |
| WP-153-T05 | Implement `BLOCKED_BUDGET` and the scope-reduction request path | Implementation owner | Commit / configuration / record reference |
| WP-153-T06 | Implement deterministic tool-result reuse with recorded provenance | Implementation owner | Commit / configuration / record reference |
| WP-153-T07 | Emit the quality/cost frontier for the release dossier | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ResearchBudgetContract`
- `TokenLedgerEntry`
- `Communication degradation ladder`
- `Tool-result reuse`
- `Pareto frontier report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-153_research_budget_and_token_ledger.tests.md`](WP-153_research_budget_and_token_ledger.tests.md).

- Budget pressure must degrade communication verbosity and must not reduce the cohort
- A required assurance step must not be skipped for budget; the task blocks instead
- Every token must carry a category, and the coordination ratio must be derivable
- A reused tool result must be marked as reused and must respect declared freshness
- Each budget dimension must stop at its own boundary and name which fired
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-153_research_budget_and_token_ledger.acceptance.md`](WP-153_research_budget_and_token_ledger.acceptance.md), together with what this package still cannot establish.

- [ ] Budget exhaustion degrades verbosity, never cohort size and never assurance depth.
- [ ] Token spend is attributable by category, so coordination overhead is a measured ratio.
- [ ] A campaign that cannot afford its assurance blocks rather than proceeding cheaply.
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

## Rollback / compensation

A budget contract is frozen per campaign: raising a ceiling mid-campaign creates a superseding contract with a recorded decision, and the original ceilings stay readable beside the results they produced.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
