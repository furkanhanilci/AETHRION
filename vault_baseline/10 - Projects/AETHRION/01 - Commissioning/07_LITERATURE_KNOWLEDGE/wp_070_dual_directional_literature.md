---
title: "WP-070 — Human + Agent Two-Way Literature Discovery"
aliases:
  - "WP-070"
  - "WP-070 — Human + Agent Two-Way Literature Discovery"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Human seeds are expanded by agents and agent candidates are filtered by human selection and counter-evidence search; coverage and provenance stay visible from both directions."
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/state/not-started
---

# WP-070 — Human + Agent Two-Way Literature Discovery

## Package card

| Field | Value |
|---|---|
| Work package | `WP-070` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Independent Literature Reviewer |
| Hard dependencies | WP-007, WP-045, WP-047, WP-062, WP-065, WP-066, WP-069 |
| Related gates | G3 |
| Related controls | CTL-EPI-02, CTL-GOV-02 |
| Related acceptance scenarios | ACC-01, ACC-02 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_070_dual_directional_literature.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_070_dual_directional_literature.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Human seeds are expanded by agents and agent candidates are filtered by human selection and counter-evidence search; coverage and provenance stay visible from both directions.


## Analysis
### What this package actually decides

That discovery runs in both directions and neither direction decides anything. A
human seeds; agents expand. Agents discover; humans filter. The two branches stay
**separate and attributable**, so a later reader can ask *who put this in the set*
and get an answer.

### Ranking is triage, never a decision (T05)

The sub-task says it outright and it is the package's most important line. A
ranked candidate list is a reading order. The moment a threshold on that ranking
determines inclusion, the model's judgement has silently replaced the screening
criteria — and the screening record will still say a human decided.

`PR-12` — *false rigor: many artifacts, weak entailment* — is exactly this shape.

### The counter-evidence branch is a deliberate asymmetry (T04)

Search naturally returns what matches the hypothesis, because the query was
written by someone holding it. A dedicated branch searching for **disconfirming**
work is the structural correction, and it is what `ACC-08`'s strong counter-test
eventually binds to.

A minority-source branch does the same for positions with few advocates: a
literature set that reflects only the mainstream is a defensible choice, but it has
to be a choice rather than an artifact of ranking.

### Merging across models is where duplicates multiply (T03)

Different scout bundles return overlapping results in different forms. Everything
merges through WP-062's resolver, with the same conservative auto-merge threshold —
because a false merge across strategies is as damaging as one within a database.

### Feeding decisions back (T06)

Human inclusion decisions are training signal for the next query iteration in the
weak sense: they inform which concepts were productive. They must not become an
automatic filter, which would close the loop and let early decisions determine
later coverage.

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

7, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |
| [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md) | `Personal seed adapter` · `Opt-in configuration` · `Sync state/receipts` · `Seed ingest dashboard` |
| [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md) | `Zotero write-back service` · `Field mapping` · `Eligibility policy` · `SyncReceipt ledger` |
| [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md) | `SearchProtocol service` · `LiteratureCampaign workflow` · `Query log` · `Known-item/coverage tests` |

### Full prerequisite closure

**57 of 160 packages (36%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 27 | `WP-058` · `WP-064` |
| 28 | `WP-062` |
| 29 | `WP-065` · `WP-066` · `WP-069` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-071` · `WP-072` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **54 of 160 packages (34%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Lead |
| Independent verifier | Independent Literature Reviewer |
| Gates touched | `G3` |
| Controls | `CTL-EPI-02` · `CTL-GOV-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) | Critical | The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md)
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
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Source Resolver service` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Match rules/features` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Conflict queue` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Known-item/dedup test corpus` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Personal seed adapter` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Opt-in configuration` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Sync state/receipts` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Seed ingest dashboard` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Zotero write-back service` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Field mapping` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Eligibility policy` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `SyncReceipt ledger` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Connector tests` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `SearchProtocol service` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `LiteratureCampaign workflow` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Query log` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Known-item/coverage tests` | `WP-069` | `python3 scripts/progress.py show WP-069` |

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
- **Evidence Lead** carries the acceptance decision; **Independent Literature Reviewer** must verify independently of whoever implements.
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
| WP-070-T01 | Separate the human seed branch from the agent discovery branch | Implementation owner | Commit / configuration / record reference |
| WP-070-T02 | Run the keyword, citation, snowball and semantic scout bundles | Implementation owner | Commit / configuration / record reference |
| WP-070-T03 | Merge results from different models and strategies through the resolver | Implementation owner | Commit / configuration / record reference |
| WP-070-T04 | Add the counter-evidence and minority-source branch | Implementation owner | Commit / configuration / record reference |
| WP-070-T05 | Treat candidate ranking as triage, never as a decision | Implementation owner | Commit / configuration / record reference |
| WP-070-T06 | Feed human inclusion decisions back into the next query iteration | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Dual-loop discovery workflow`
- `Discovery provenance`
- `Candidate/coverage matrix`
- `Counter-evidence log`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-070_dual_directional_literature.tests.md`](wp_070_dual_directional_literature.tests.md).

- Human seed → agent snowball expansion
- Agent candidate → human inclusion
- Retention of minority and counter sources
- Partial state when one branch is unavailable
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-070_dual_directional_literature.acceptance.md`](wp_070_dual_directional_literature.acceptance.md), together with what this package still cannot establish.

- [ ] An agent's popularity ordering is not an inclusion decision.
- [ ] Sources from both directions pass through the same resolver and deduplication.
- [ ] Search gaps and disagreements remain visible rather than being smoothed away.
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

A faulty scout profile or bundle is disabled; the candidates it produced are not invalidated but receive lower trust and a disposition through their source provenance.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
