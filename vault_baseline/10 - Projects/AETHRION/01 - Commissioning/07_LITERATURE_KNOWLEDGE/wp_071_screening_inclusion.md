---
title: "WP-071 — Screening, Inclusion/Exclusion and Coverage"
aliases:
  - "WP-071"
  - "WP-071 — Screening, Inclusion/Exclusion and Coverage"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Title/abstract and full-text screening reaches a freezable set through reason-coded inclusion and exclusion, recorded disagreement, sampling and risk-based independent review."
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md"
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

# WP-071 — Screening, Inclusion/Exclusion and Coverage

## Package card

| Field | Value |
|---|---|
| Work package | `WP-071` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Methodologist / Blind Literature Reviewer |
| Hard dependencies | WP-007, WP-017, WP-061, WP-062, WP-069, WP-070 |
| Related gates | G3 |
| Related controls | CTL-GOV-02, CTL-EPI-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_071_screening_inclusion.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_071_screening_inclusion.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Title/abstract and full-text screening reaches a freezable set through reason-coded inclusion and exclusion, recorded disagreement, sampling and risk-based independent review.


## Analysis
### What this package actually decides

Why a source is in or out, in a form someone else can check. Reason-coded
decisions, recorded disagreement, and a PRISMA-style flow that accounts for every
source from retrieval to inclusion.

### Reason codes are what make exclusion reviewable (T01)

"Excluded" is not a decision anyone can audit. "Excluded — population does not
match the inclusion criterion" is. Codes also make the exclusion *distribution*
visible, and a distribution dominated by one code is usually a criterion problem
rather than a literature problem.

### Blind assignment and conflict-of-interest checks (T03)

A screener who knows the other screener's decision is not a second opinion. This
is WP-007's independence applied at the cheapest possible gate — screening is where
independence costs least and is therefore where it is most affordable.

### Dual review depth follows risk, not preference (T04)

R1, R2, R3 map to sampling depth. `00_PROGRAM/01`'s rule holds: risk changes
depth, never identity — so even an R1 screening produces a record, it is simply a
shallower one.

### `DisagreementCase` must not resolve by majority (T05)

Two screeners disagree; a third does not break the tie by vote. The arbiter reads
both rationales and decides, and the decision records **why** — because a
disagreement that resolved by counting has discarded the reasoning that made it a
disagreement.

`ACC-06`, `ACC-07` and `ACC-38` are where the reviewer-bias scenarios bind.

### The unknown-status count is the honest number (T06)

Every PRISMA flow has sources that could not be retrieved, could not be assessed,
or whose status is unresolved. Reporting them as excluded is the common
simplification and it overstates the completeness of the screen. They get their own
box.

### Baseline v1.3.0 — unchanged ownership, new cross-cutting obligations

No semantic ownership changes here. What changes is what these packages must
remain compatible with:

- the **trace and correlation** fields every plane now carries, so a divergence
  is traceable to a cause;
- **context projection**, so that a record's canonical status does not depend on
  whether it happened to be in an agent's context;
- **provenance rules** for anything adapted from an upstream source.

Generated counts, indexes and the new cross-cutting acceptance references must
stay consistent — which is a mechanical obligation, and the one most likely to be
skipped because nothing in the package's own subject matter changed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |
| [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md) | `SearchProtocol service` · `LiteratureCampaign workflow` · `Query log` · `Known-item/coverage tests` |
| [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/wp_070_dual_directional_literature.md) | `Dual-loop discovery workflow` · `Discovery provenance` · `Candidate/coverage matrix` · `Counter-evidence log` |

### Full prerequisite closure

**58 of 160 packages (36%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 30 | `WP-070` |

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-072` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **53 of 160 packages (33%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **31** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Lead |
| Independent verifier | Methodologist / Blind Literature Reviewer |
| Gates touched | `G3` |
| Controls | `CTL-GOV-02` · `CTL-EPI-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-75 — Literature Retrieval Budget and Stopping Rule](../12_ACCEPTANCE_SCENARIOS/acc_75_retrieval_budget_and_stopping_rule.md) | High | The loop halts at the frozen budget, and the attempt to change the stopping rule is refused. The sufficiency assessment is advisory; the protocol is authority. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/wp_070_dual_directional_literature.md)
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
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Source Resolver service` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Match rules/features` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Conflict queue` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Known-item/dedup test corpus` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `SearchProtocol service` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `LiteratureCampaign workflow` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Query log` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Known-item/coverage tests` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Dual-loop discovery workflow` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Discovery provenance` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Candidate/coverage matrix` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Counter-evidence log` | `WP-070` | `python3 scripts/progress.py show WP-070` |

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
- **Evidence Lead** carries the acceptance decision; **Methodologist / Blind Literature Reviewer** must verify independently of whoever implements.
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
| `ASM-018` — OpenScholar — self-feedback retrieval sufficiency loop | `ADAPTIVE_REIMPLEMENT` | `MS-LIT-003` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `CMP-009` — OpenScholar | `ADAPTER` | Retrieval and self-feedback sufficiency at runtime. | The same adapter contract as PaperQA2, deliberately — so the two remain comparable. | **2** |
| `CMP-010` — ASReview | `ADAPTER` | Active-learning ranking of candidate records. | The screening decision record, the stopping rule and the coverage claim that follows from it. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-018` | An EvidenceSufficiencyAssessment is advisory and model-mediated. The stopping rule of a confirmatory or systematic campaign is frozen in the SearchProtocol before results are seen and cannot be changed by the loop that reads them. | The peS2o datastore and retriever stack — AETHRION's canonical representation path is GROBID/Pub2TEI into TEI, not a second corpus. |
| `CMP-009` | Retrieval supplies candidates and never a claim, exactly as for PaperQA2. | Any hard-coded preference between the two retrievers before the bake-off runs. |
| `CMP-010` | Screening ranks; it never excludes. An exclusion is a recorded human or policy decision with a reason, and a stopping rule reports coverage rather than declaring completeness. | Model-suggested exclusion as an exclusion. |

### Where a plain row would mislead

- **`ASM-018`** — Taken as the second opinion to PaperQA2 behind one adapter contract, so the choice between them is settled by measurement rather than by preference.
- **`CMP-009`** — Also carries reimplemented mechanisms — `ASM-018`.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-018` — OpenScholar — self-feedback retrieval sufficiency loop** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`CMP-009` — OpenScholar** · `ADAPTER` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**`CMP-010` — ASReview** · `ADAPTER` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 5 obligations open across 3 of 3 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-071-T01 | Define the screening criteria, rubric and reason codes | Implementation owner | Commit / configuration / record reference |
| WP-071-T02 | Establish the title/abstract and full-text queues | Implementation owner | Commit / configuration / record reference |
| WP-071-T03 | Add blind human/agent assignment and conflict-of-interest checks | Implementation owner | Commit / configuration / record reference |
| WP-071-T04 | Apply R1/R2/R3 dual-review and sampling depth | Implementation owner | Commit / configuration / record reference |
| WP-071-T05 | Bind `DisagreementCase` and arbiter escalation | Implementation owner | Commit / configuration / record reference |
| WP-071-T06 | Produce the PRISMA-style flow, coverage and unknown-status report | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Screening service`
- `Decision queue`
- `Reason taxonomy`
- `Coverage/flow report`
- `Screening calibration set`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-071_screening_inclusion.tests.md`](wp_071_screening_inclusion.tests.md).

- Include/exclude boundary calibration
- A case with conflicting reviewers
- The missing-full-text state
- The R3 independence requirement
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-071_screening_inclusion.acceptance.md`](wp_071_screening_inclusion.acceptance.md), together with what this package still cannot establish.

- [ ] Every exclusion carries a reason code and an actor.
- [ ] Material disagreement is never hidden by aggregation.
- [ ] An unavailable source is never counted as `INCLUDED` by default.
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

A criteria change opens an amendment and a rescreen queue for the affected decisions; previous decisions are preserved as history.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
