# WP-069 — SearchProtocol and LiteratureCampaign Orchestration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-069` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Methodologist / Citation Auditor |
| Hard dependencies | WP-013, WP-017, WP-032, WP-035, WP-046, WP-047, WP-049, WP-050, WP-061, WP-062 |
| Related gates | G2,G3 |
| Related controls | CTL-EPI-02, CTL-LIT-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-069_search_protocol_campaign.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-069_search_protocol_campaign.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A research question becomes a re-runnable literature campaign defined by databases, queries, date and language limits, inclusion/exclusion criteria, stop rules and known-item tests.


## Analysis
### What this package actually decides

That a literature search is **re-runnable**. Databases, queries, limits, criteria,
stop rules — frozen as a `SearchProtocol` so the same search can be executed again
and produce a comparable result.

The alternative is the common one: someone searched, found things, and nobody can
say what would have been found differently.

### The stop rule is the part that makes a search finish honestly (T05)

Without one, searching stops when the searcher is tired, and the write-up says
"we searched extensively". Known-item recall and saturation are the two defensible
stop conditions: **did the search find the papers we already knew about**, and
**has the marginal new-source rate fallen below a threshold**.

Known-item recall is the stronger one, and it is a test the search can fail.

### Query execution logs and response snapshots (T04)

A search re-run six months later returns different results, because the databases
changed. That is expected and it is why the response snapshot matters: the protocol
says what was asked, the snapshot says what came back, and the difference between a
re-run and the original is then attributable rather than mysterious.

### Freezing and amendment mirror the protocol discipline (T03)

Same rule as WP-035: amend before you look, version the amendment, and an
amendment after seeing results is a new search rather than a correction. A search
protocol edited to match what was found is the literature-review form of
p-hacking.

### Bounded scout tasks (T06)

The `LiteratureCampaign` dispatches scouts as **bounded** tasks — a budget, a
scope, a stop condition. An unbounded scout is `PR-09`'s cost runaway with a
research justification attached.

### Baseline v1.3.0 — source status, retrieval budget and what survives a pruned context

Two additions and one guarantee.

**Material-delta detection for G10.** A citation-count change is not a material
event. A retraction, a major correction, strong contradictory evidence, a
reproduction failure or a dependency drift that invalidates a result is. The
distinction is what keeps G10 from becoming a notification nobody reads —
alert fatigue is a failure mode of a monitoring system, not a nuisance.

**Search and retrieval budget.** Literature retrieval draws on the same
`ResearchBudgetContract` as everything else, and its stopping rule stays
distinct from the communication stopping rule — the two answer different
questions and sharing a threshold would couple them wrongly.

**The guarantee:** source and literature records stay canonical **even when the
blackboard and the context projections are pruned**. A source that only exists in
an agent's context is not a source, and pruning must never be able to lose one.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md) | `Versioned connectors` · `Connector permission profiles` · `Connector contract tests` · `Compensation/reconciliation playbooks` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |

### Full prerequisite closure

**53 of 160 packages (33%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` |
| 28 | `WP-062` |

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-070` · `WP-071` · `WP-072` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **55 of 160 packages (34%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **29** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Lead |
| Independent verifier | Methodologist / Citation Auditor |
| Gates touched | `G2` · `G3` |
| Controls | `CTL-EPI-02` · `CTL-LIT-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-75 — Literature Retrieval Budget and Stopping Rule](../12_ACCEPTANCE_SCENARIOS/ACC-75_retrieval_budget_and_stopping_rule.md) | High | The loop halts at the frozen budget, and the attempt to change the stopping rule is refused. The sufficiency assessment is advisory; the protocol is authority. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md)
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
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `LangGraph runtime` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Temporal adapter` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Checkpoint policy` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Agent graph SDK` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Conformance tests` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Versioned connectors` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector permission profiles` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector contract tests` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Compensation/reconciliation playbooks` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Source Resolver service` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Match rules/features` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Conflict queue` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Known-item/dedup test corpus` | `WP-062` | `python3 scripts/progress.py show WP-062` |

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
- **Evidence Lead** carries the acceptance decision; **Methodologist / Citation Auditor** must verify independently of whoever implements.
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
| WP-069-T01 | Write the question → concept → query authoring flow | Implementation owner | Commit / configuration / record reference |
| WP-069-T02 | Define the database and source connector catalogue and its coverage | Implementation owner | Commit / configuration / record reference |
| WP-069-T03 | Establish `SearchProtocol` freeze, versioning and amendment | Implementation owner | Commit / configuration / record reference |
| WP-069-T04 | Record the query execution log, response snapshot and references | Implementation owner | Commit / configuration / record reference |
| WP-069-T05 | Compute known-item recall, saturation and the stop rule | Implementation owner | Commit / configuration / record reference |
| WP-069-T06 | Bind the Temporal `LiteratureCampaign` and its bounded scout tasks | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SearchProtocol service`
- `LiteratureCampaign workflow`
- `Query log`
- `Known-item/coverage tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-069_search_protocol_campaign.tests.md`](WP-069_search_protocol_campaign.tests.md).

- Re-running a frozen query
- Failure when a known item is missing
- Resume after a provider partial failure
- A protocol amendment producing a new version
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-069_search_protocol_campaign.acceptance.md`](WP-069_search_protocol_campaign.acceptance.md), together with what this package still cannot establish.

- [ ] Every result is bound to its query, provider and timestamp.
- [ ] The number of search results is never treated as evidence of coverage.
- [ ] A query for critical counter-evidence is mandatory.
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

- Identity errors in sources propagate into every claim that cites them.
- A write into a shared library without a version precondition can silently destroy a human edit.
- A literature set that is not frozen cannot support a reproducible claim.

## Rollback / compensation

A provider failure marks the query `PARTIAL`; the set cannot be frozen until a coverage decision is taken explicitly.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
