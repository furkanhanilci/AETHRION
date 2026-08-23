---
title: "WP-149 — Sparse Communication Topology and the Scientific Blackboard"
aliases:
  - "WP-149"
  - "WP-149 — Sparse Communication Topology and the Scientific Blackboard"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Agents exchange typed deltas over a compiled sparse graph, on a blackboard that is a projection and never a source of scientific truth."
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-149_sparse_topology_and_blackboard.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/state/not-started
---

# WP-149 — Sparse Communication Topology and the Scientific Blackboard

## Package card

| Field | Value |
|---|---|
| Work package | `WP-149` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Research Director / Platform Assurance Lead |
| Hard dependencies | WP-013, WP-015, WP-046, WP-047, WP-148 |
| Related gates | G4,G5,G6 |
| Related controls | CTL-EPI-04, CTL-OPS-01 |
| Related acceptance scenarios | ACC-083, ACC-084, ACC-085, ACC-086 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_149_sparse_topology_and_blackboard.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_149_sparse_topology_and_blackboard.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Agents exchange typed deltas over a compiled sparse graph, on a blackboard that is a projection and never a source of scientific truth.


## Analysis

### What this package actually decides

That keeping a cohort does not mean paying for a quadratic conversation, and that
the conversation is never where the science lives.

A naive cohort talks to itself every-to-every, every round, in full transcripts.
Published work on communication pruning reports large token reductions at small
quality cost, and the useful reading is not *use fewer agents* but **most of what
they say to each other is redundant** — `ADR-013`.

### The blackboard is deletable

The structural rule, stated so it can be tested: **delete the blackboard and no
canonical science is lost.** Everything that mattered is an `ArtifactRecord`, an
`EvidenceSpan`, a `ClaimVersion` or a `FindingRecord`; the entry pointed at it.

Three consequences, and the second is the one that gets violated first:

- A `BlackboardEntry` is not evidence — ACC-085.
- There is **no path** from an entry to a `ClaimVersion`. A promising sentence on
  the blackboard is still a sentence on the blackboard.
- A `REFUTED` or `SUPERSEDED` entry leaves ordinary reasoning context and stays
  visible to a failure-history query — two different questions, and WP-151 owns
  the mask that separates them.

### Typed, because a tone cannot be tracked

Ten message types: `PROPOSAL`, `CHALLENGE`, `EVIDENCE`, `REQUEST`, `CORRECTION`,
`DISAGREEMENT`, `CONSENSUS_CANDIDATE`, `ABSTAIN`, `STATUS`, `BLOCKER`.

The type is what makes the exchange checkable. A `CHALLENGE` can be followed to
resolution; an objection inside a paragraph of prose cannot, and it disappears
the moment somebody summarises the thread. WP-148's convergence rule is only
enforceable because a challenge is a type.

### Delta-only, for two reasons

A message carries what changed, the evidence it points at and the action it asks
for. Large content goes to the artifact store and the message carries a digest —
ACC-084, ACC-085.

The token saving is the obvious reason. The other one matters more: a full
transcript passed between agents is a channel through which one agent's error
becomes another's premise, which is `ADR-005`'s memory-contamination concern
arriving through a different door.

### Sparse by default, and honest about the baseline

The Task Compiler derives the initial topology from task class, scientific phase,
roles, evidence dependencies, independence requirements and budget. Edges carry a
policy: allowed types, token ceiling, evidence scope, visibility, security class.

**A fully connected graph is available only in an explicit benchmark or control
mode**, because that is the baseline the optimisation is measured against.
Comparing against a single agent would measure the cost of having a cohort — a
decision already taken on other grounds — rather than the pruning.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-148 — Multi-Agent Collaboration Plane and Cohort Integrity](../15_RELIABILITY_EFFICIENCY/wp_148_multi_agent_collaboration_plane.md) | `AgentCohortRecord` · `CognitiveDiversityProfile` · `InitialPositionArtifact` · `MaterialChallenge` |

### Full prerequisite closure

**79 of 160 packages (49%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 38 | `WP-148` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-150` · `WP-158`
- **Transitively reachable:** **4 of 160 packages (2%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **39** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Chief Architect |
| Independent verifier | Research Director / Platform Assurance Lead |
| Gates touched | `G4` · `G5` · `G6` |
| Controls | `CTL-EPI-04` · `CTL-OPS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-082 — Independent-First Embargo](../12_ACCEPTANCE_SCENARIOS/acc_082_independent_first_embargo.md) | Critical | The pre-seal request is denied and audited. The post-seal request succeeds through the protocol path, and only the material differences are exposed rather than the full prior output. |
| [ACC-083 — Typed Inter-Agent Message](../12_ACCEPTANCE_SCENARIOS/acc_083_typed_inter_agent_message.md) | High | Both are rejected at the contract boundary. A correctly typed message passes, and its type is what makes a `CHALLENGE` trackable to resolution. |
| [ACC-084 — Delta-Only Communication](../12_ACCEPTANCE_SCENARIOS/acc_084_delta_only_communication.md) | High | The message is rejected in favour of a delta plus an artifact pointer. The full content is written to the artifact store and the message carries its digest. |
| [ACC-085 — A Blackboard Entry Is Not Evidence](../12_ACCEPTANCE_SCENARIOS/acc_085_blackboard_entry_is_not_evidence.md) | Critical | Both attempts are refused. After deletion, no canonical scientific record is lost — everything that mattered was an artifact, a span, a claim or a finding, and the entry only pointed at it. |
| [ACC-086 — Sparse Topology Preserves Quality](../12_ACCEPTANCE_SCENARIOS/acc_086_sparse_topology_quality_preservation.md) | High | The optimised arm reports a meaningful reduction in coordination cost with quality within the declared tolerance. The comparison is against the fully connected cohort — not against a single agent — and both numbers are reported as a frontier. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md), [WP-047 — Role and **Skill** Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-148 — Multi-Agent Collaboration Plane and Cohort Integrity](wp_148_multi_agent_collaboration_plane.md)
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
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `LangGraph runtime` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Temporal adapter` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Checkpoint policy` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Agent graph SDK` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Conformance tests` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `AgentCohortRecord` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `CognitiveDiversityProfile` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `InitialPositionArtifact` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `MaterialChallenge` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `ConvergenceAssessment` | `WP-148` | `python3 scripts/progress.py show WP-148` |

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
- **Chief Architect** carries the acceptance decision; **Research Director / Platform Assurance Lead** must verify independently of whoever implements.
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
| WP-149-T01 | Define `BlackboardEntry` with artifact pointers, epistemic status and retention | Implementation owner | Commit / configuration / record reference |
| WP-149-T02 | Define the ten typed messages and their required fields | Implementation owner | Commit / configuration / record reference |
| WP-149-T03 | Enforce the delta-only rule and the artifact-pointer substitution | Implementation owner | Commit / configuration / record reference |
| WP-149-T04 | Define `CommunicationGraph` and `CommunicationEdgePolicy` | Implementation owner | Commit / configuration / record reference |
| WP-149-T05 | Implement topology compilation from the task and the independence profile | Implementation owner | Commit / configuration / record reference |
| WP-149-T06 | Implement the fully-connected control mode and the baseline harness | Implementation owner | Commit / configuration / record reference |
| WP-149-T07 | Prove the blackboard is deletable without canonical loss | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `BlackboardEntry`
- `TypedAgentMessage`
- `CommunicationGraph`
- `CommunicationEdgePolicy`
- `Naive fully-connected baseline harness`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## The threshold freeze — `EfficiencyQualificationProfile`

"Quality stays inside a **pre-declared** tolerance" is the sentence this package
turns on, and as written it is unenforceable. Nothing in the plan says *where*
the tolerance is declared, *when* it stops being editable, or *who* would notice
if it moved. A threshold that can be adjusted after the release-candidate result
is visible is not a threshold; it is a description of whatever happened.

So the declaration becomes an artifact with an identity and a freeze point.

| Field group | Contents | What it prevents |
|---|---|---|
| Identity | `profile_id` · `version` · `study_or_release_id` · `created_at` · `frozen_at` · `approved_by` | A profile nobody owns, and a version that quietly replaces itself |
| Arms under comparison | `baseline_cohort_manifest_digest` · `baseline_topology_digest` · `optimized_topology_policy_digest` | Comparing against a baseline that was itself tuned |
| Data | `calibration_dataset_digest` · `holdout_dataset_digest` · `no_overlap_attestation` | Calibrating a threshold on the data it is later evaluated against |
| Thresholds | `quality_metric` · `quality_direction` · `quality_loss_ceiling` · `coordination_metric` · `minimum_coordination_reduction` | The number chosen after the outcome |
| Statistics | `confidence_interval_method` · `alpha` · `minimum_sample_size` | A reduction inside the noise, reported as a win |
| Consequences | `rollback_trigger` · `non_waivable_floor` · `limitations` · `profile_digest` | An accepted optimisation with no automatic way back |

### The freeze protocol

1. Choose the metric family and the calibration data.
2. Estimate variance and the plausible frontier.
3. **Freeze** thresholds and statistical method; set `frozen_at`.
4. Sign and seal the profile; record `profile_digest`.
5. **Only then** expose the holdout and the release candidate.
6. Run the baseline and optimised arms.
7. Compare the quality delta and the cost reduction against the frozen profile.
8. Roll the topology back automatically on a regression.
9. **Retain the failed optimisation as metascience evidence** — an optimisation
   that did not work is a measurement, and discarding it biases every summary
   built from the ones that did.

### The two failure modes this must distinguish

A change can improve cost and damage quality, or improve quality and save
nothing. Both are failures of an *efficiency* claim and they are not the same
event:

- cost improves, quality delta exceeds `quality_loss_ceiling` → **rejected**, and
  the topology rolls back;
- quality holds, reduction falls below `minimum_coordination_reduction` → **not
  accepted as an efficiency improvement**, though nothing rolls back.

Neither may be recorded as a success with a caveat attached.

> **The numbers are targets, not constants.** `00_PROGRAM/06` states the release
> targets — a communication reduction against the fully-connected baseline, and
> a quality-loss ceiling — and states that they are to be frozen **after**
> calibration, with intervals. This profile is the object that freezing produces.
> Until a calibration run exists, every field above is `SPECIFIED` and no value
> in it has been measured.

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-149_sparse_topology_and_blackboard.tests.md`](wp_149_sparse_topology_and_blackboard.tests.md).

- An untyped or free-text inter-agent message must be rejected
- A message carrying a payload above the delta threshold must be rejected in favour of a pointer
- A blackboard entry must not be promotable to a claim or citable as evidence
- Deleting the whole blackboard must lose no canonical scientific record
- A quality regression against the fully-connected baseline must roll the topology back
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-149_sparse_topology_and_blackboard.acceptance.md`](wp_149_sparse_topology_and_blackboard.acceptance.md), together with what this package still cannot establish.

- [ ] Every inter-agent message is typed, and an untyped one cannot be sent.
- [ ] The blackboard can be dropped entirely with no loss of canonical scientific state.
- [ ] The optimisation baseline is the naive fully-connected cohort, and it is runnable.
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

A compiled topology belongs to its campaign: a policy change applies to subsequent campaigns, and a running campaign keeps and records the topology it started under.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
