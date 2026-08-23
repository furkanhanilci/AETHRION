---
title: "WP-150 — Communication Governor, Edge Utility and Context Projection"
aliases:
  - "WP-150"
  - "WP-150 — Communication Governor, Edge Utility and Context Projection"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "What is sent, how much of it, and what each actor is allowed to see are decided by recorded policy against measured edge utility — with a quality guard that rolls the whole thing back."
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-150_communication_governor_and_context_projection.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/state/not-started
---

# WP-150 — Communication Governor, Edge Utility and Context Projection

## Package card

| Field | Value |
|---|---|
| Work package | `WP-150` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | FinOps Lead / Assurance Lead |
| Hard dependencies | WP-096, WP-100, WP-149 |
| Related gates | G5,G6 |
| Related controls | CTL-EPI-04, CTL-OPS-02 |
| Related acceptance scenarios | ACC-086, ACC-087, ACC-088 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_150_communication_governor_and_context_projection.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_150_communication_governor_and_context_projection.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

What is sent, how much of it, and what each actor is allowed to see are decided by recorded policy against measured edge utility — with a quality guard that rolls the whole thing back.


## Analysis

### What this package actually decides

Which messages are worth their tokens, and what an actor's context window should
actually contain.

`CommunicationValue` combines novelty, decision impact, contradiction value,
evidence value and sender calibration against redundancy, token cost and latency.
The first implementation is deterministic and heuristic; a learned policy is a
post-V1 question.

### The score is routing priority and nothing else

`CommunicationValue` is not scientific truth and cannot become a claim
confidence. It is the same forbidden conversion `ADR-006` fixes for search
scores, arriving in the collaboration plane instead of the discovery graph, and
it is refused the same way — by schema and by policy rather than by convention.

Decisions available to the governor: `SEND_FULL_STRUCTURED`, `SEND_COMPRESSED`,
`SEND_POINTER_ONLY`, `DEFER`, `SILENCE`.

### Two things a governor may never silence

A `BLOCKER`, and any non-waivable safety message. A low-utility edge carrying a
blocker is still carrying a blocker — ACC-088.

And a low-calibration sender is not silenced either. Its message changes
**priority and corroboration requirement**, not existence: silencing an actor
because it has been wrong before is how a cohort stops being able to surprise
itself.

### Context projection is a separate lever

No model invocation receives the whole project history. A `ContextProjection` is
assembled per invocation: role contract, task contract, relevant skills, current
canonical state, admissible evidence, targeted peer deltas and any memory
reminder that earned its place.

This is where most of the token cost actually is, and it is also an assurance
control — a reviewer's projection is what `ADR-005` §6 bounds, and it is why
independence is a property of the projection rather than of the reviewer.

### Anchored optimisation, or it is not an optimisation

An optimisation is accepted only when the quality delta stays within tolerance
**and** coordination cost falls meaningfully, measured against WP-149's naive
fully-connected baseline. A regression rolls the topology back — ACC-086,
ACC-087.

The failure this guards against is the ordinary one: a change that improves the
number being watched and degrades the one that is not.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |
| [WP-149 — Sparse Communication Topology and the Scientific Blackboard](../15_RELIABILITY_EFFICIENCY/wp_149_sparse_topology_and_blackboard.md) | `BlackboardEntry` · `TypedAgentMessage` · `CommunicationGraph` · `CommunicationEdgePolicy` |

### Full prerequisite closure

**82 of 160 packages (51%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 30 | `WP-067` · `WP-070` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-100` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-147` |
| 38 | `WP-148` |
| 39 | `WP-149` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-151` · `WP-153`
- **Transitively reachable:** **2 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **40** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Chief Architect |
| Independent verifier | FinOps Lead / Assurance Lead |
| Gates touched | `G5` · `G6` |
| Controls | `CTL-EPI-04` · `CTL-OPS-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-084 — Delta-Only Communication](../12_ACCEPTANCE_SCENARIOS/acc_084_delta_only_communication.md) | High | The message is rejected in favour of a delta plus an artifact pointer. The full content is written to the artifact store and the message carries its digest. |
| [ACC-086 — Sparse Topology Preserves Quality](../12_ACCEPTANCE_SCENARIOS/acc_086_sparse_topology_quality_preservation.md) | High | The optimised arm reports a meaningful reduction in coordination cost with quality within the declared tolerance. The comparison is against the fully connected cohort — not against a single agent — and both numbers are reported as a frontier. |
| [ACC-087 — Communication Optimisation Rollback](../12_ACCEPTANCE_SCENARIOS/acc_087_communication_optimization_rollback.md) | High | The topology rolls back automatically, without human intervention, and the regression and the rollback are both recorded. The campaign continues under the previous topology rather than stopping. |
| [ACC-088 — Strategic Silence Never Silences a Blocker](../12_ACCEPTANCE_SCENARIOS/acc_088_strategic_silence_never_silences_a_blocker.md) | Critical | Neither the blocker nor the safety message can be silenced at any utility threshold. The low-calibration sender's message is not deleted either — its priority and corroboration requirement change. |
| [ACC-099 — Budget Degrades Communication, Not the Cohort](../12_ACCEPTANCE_SCENARIOS/acc_099_communication_budget_degradation.md) | Critical | Communication policy degrades — structured, compressed, pointer-only, silence unless material. The cohort is not reduced, the assurance route is not lowered, and no non-waivable control is skipped. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-149 — Sparse Communication Topology and the Scientific Blackboard](wp_149_sparse_topology_and_blackboard.md)
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
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Token ledger categories` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `BlackboardEntry` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `TypedAgentMessage` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `CommunicationGraph` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `CommunicationEdgePolicy` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `Naive fully-connected baseline harness` | `WP-149` | `python3 scripts/progress.py show WP-149` |

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
- **Chief Architect** carries the acceptance decision; **FinOps Lead / Assurance Lead** must verify independently of whoever implements.
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
| WP-150-T01 | Define `CommunicationValue` and its deterministic first implementation | Implementation owner | Commit / configuration / record reference |
| WP-150-T02 | Define `CommunicationUtilityRecord` and its per-edge history | Implementation owner | Commit / configuration / record reference |
| WP-150-T03 | Implement the five governor decisions and the blocker exemption | Implementation owner | Commit / configuration / record reference |
| WP-150-T04 | Define `ContextProjectionRecord` and the per-invocation assembly | Implementation owner | Commit / configuration / record reference |
| WP-150-T05 | Implement the quality guard and the topology rollback path | Implementation owner | Commit / configuration / record reference |
| WP-150-T06 | Emit coordination overhead, redundancy and useful-challenge metrics | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `CommunicationValue`
- `CommunicationUtilityRecord`
- `ContextProjectionRecord`
- `Quality guard and rollback`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-150_communication_governor_and_context_projection.tests.md`](wp_150_communication_governor_and_context_projection.tests.md).

- A blocker or non-waivable safety message must not be silenced at any utility threshold
- A low-calibration sender's message must change priority, not be deleted
- A communication utility score written to a claim assessment must be refused
- A quality regression beyond tolerance must roll back the topology automatically
- A context projection must exclude what the independence profile forbids
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-150_communication_governor_and_context_projection.acceptance.md`](wp_150_communication_governor_and_context_projection.acceptance.md), together with what this package still cannot establish.

- [ ] Coordination overhead is a measured ratio against a runnable baseline, not an estimate.
- [ ] No utility threshold can suppress a blocker or a non-waivable safety message.
- [ ] An optimisation that costs quality beyond tolerance reverts without human intervention.
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

The governor is a policy applied per campaign; disabling it returns the campaign to the fully-connected baseline rather than to an undefined state, and the reversion is recorded.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
