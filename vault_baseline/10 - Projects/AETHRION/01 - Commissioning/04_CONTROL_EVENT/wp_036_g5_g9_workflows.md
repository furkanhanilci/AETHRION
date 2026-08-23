---
title: "WP-036 — G5 Execute through G9 Publish Workflows"
aliases:
  - "WP-036"
  - "WP-036 — G5 Execute through G9 Publish Workflows"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Execution, claim freeze, blind review, reproduction, human decision and publication gates operate over a canonical artifact and decision chain."
source: "planning/commissioning/04_CONTROL_EVENT/WP-036_g5_g9_workflows.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/04-control-event
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g5-g9
  - aethrion/state/not-started
---

# WP-036 — G5 Execute through G9 Publish Workflows

## Package card

| Field | Value |
|---|---|
| Work package | `WP-036` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Workflow Engineering Lead |
| Independent verifier | Assurance Lead / Decision Owner |
| Hard dependencies | WP-004, WP-007, WP-008, WP-019, WP-032, WP-033, WP-035 |
| Related gates | G5–G9 |
| Related controls | CTL-GOV-02, CTL-EPI-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-08, ACC-19, ACC-20, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_036_g5_g9_workflows.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_036_g5_g9_workflows.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Execution, claim freeze, blind review, reproduction, human decision and publication gates operate over a canonical artifact and decision chain.


## Analysis
### What this package actually decides

The path from a run to a published claim, and the four places a claim can be
stopped along it. This is the longest workflow in the programme and the one where
the evidence chain either holds end to end or breaks at a seam.

### G5 has the invariant nobody may soften

`00_PROGRAM/01` restated it deliberately: **no agentic methodological discretion
during a frozen execution.** The original wording — *no model at G5* — was too
strong, because the subject of an experiment may itself be a model. What is
forbidden is an agent moving a threshold mid-run because the result looks wrong.

The workflow enforces it structurally: the run executes against the frozen
protocol, and any change to a parameter mid-batch is a stop, not an adjustment.

### G6's frozen package is what makes independence checkable (T02)

`00_PROGRAM/01` invariant 3: *a reviewer can work from a frozen package without
seeing the producer's trace.* That is a construction requirement on this workflow
— the package is assembled and handed over, not pointed at.

### G7 splits into two operations with different tolerances (T03)

G7a deterministic reproduction, G7b distributional replication. WP-019 separates
the four verification types; this workflow must not collapse them into one
"reproduction failed", because the three plausible causes imply three different
responses and only one of them means the claim was wrong.

### G8 is where the evidence delta matters (T04)

WP-004 built the mechanism. Here it binds: the human sees **what changed** since
the last decision on this object, not the whole package again. `PR-11` —
rubber-stamping — is the failure this addresses, and the measurable signal is
median decision time falling as volume rises.

### G9's release checklist has a security half people forget (T05)

Citation and provenance are the obvious checks. The security release check is
whether publishing this reveals something the trust boundary was protecting —
a dataset locator, an internal identifier, a prompt that exposes an unpublished
capability.

### Baseline v1.3.0 — new policies at the gates, without moving authority

G0–G10 consumes the collaboration, conformance, assurance and reproduction
policies this baseline adds. **None of that moves authority.** Temporal still
owns lifecycle transitions and LangGraph still owns bounded cognition inside one
task, and a checkpoint in the second cannot transition a gate in the first.

Three concrete additions:

- **G5 and G6** consume the cohort, the topology, the specification conformance
  result and the assurance route.
- **G7** consumes the model execution fingerprint and the reproduction level it
  supports — a hosted black-box model does not yield `EXACT`.
- **G8** runs the human preliminary flow: the recommendation is unreachable
  until the human assessment is sealed, through **every** interface rather than
  only the UI.

And the write path becomes explicit: a canonical transaction and its outbox
record commit atomically, the publisher reads the outbox afterwards, and a
consumer validates identity and version rather than trusting a payload. The
failure suite gains the injections that make split brain visible — publisher
crash, duplicate delivery, out-of-order delivery, a cancelled task's late
result, and two concurrent gate transitions.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

7, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md) | `Gate Policy v1` · `Gate artifact matrix` · `Reopen/return transition table` · `Gate owner matrix` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md) | `Gate Service` · `GateRecord persistence` · `Verdict rule tests` · `Gate explanation format` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |

### Full prerequisite closure

**33 of 160 packages (21%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 17 | `WP-024` · `WP-028` |
| 18 | `WP-027` |
| 19 | `WP-031` |
| 20 | `WP-032` |
| 21 | `WP-033` |
| 22 | `WP-034` |
| 23 | `WP-035` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-040` · `WP-092`
- **Transitively reachable:** **28 of 160 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **24** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Workflow Engineering Lead |
| Independent verifier | Assurance Lead / Decision Owner |
| Gates touched | `G5–G9` |
| Controls | `CTL-GOV-02` · `CTL-EPI-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) | Critical | G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md)
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
| `Decision policy` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `SLA/escalation table` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Delegation matrix` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Decision rationale rubric` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Human intervention vocabulary` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Timeout escalation path with no approval branch` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Gate Policy v1` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate artifact matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Reopen/return transition table` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate owner matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `CandidateWorkspace` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionPackage` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ClaimConsistencyReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Gate Service` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `GateRecord persistence` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Verdict rule tests` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Gate explanation format` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |

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
- **Workflow Engineering Lead** carries the acceptance decision; **Assurance Lead / Decision Owner** must verify independently of whoever implements.
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
| WP-036-T01 | Write the G5 `RunBatch` dispatch, checkpoint and stop flow | Implementation owner | Commit / configuration / record reference |
| WP-036-T02 | Bind the G6 frozen review package and its dispositions | Implementation owner | Commit / configuration / record reference |
| WP-036-T03 | Establish the G7 reproduction request, result and reopen flow | Implementation owner | Commit / configuration / record reference |
| WP-036-T04 | Apply the G8 evidence-delta human decision update | Implementation owner | Commit / configuration / record reference |
| WP-036-T05 | Bind the G9 citation, provenance and security release checklist | Implementation owner | Commit / configuration / record reference |
| WP-036-T06 | Add cancellation, compensation and supersession | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `G5–G9 workflows`
- `Review/repro integration contracts`
- `Decision update flow`
- `Publication transition`
- `Gate consumption of collaboration and assurance policies`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-036_g5_g9_workflows.tests.md`](wp_036_g5_g9_workflows.tests.md).

- Recovery from a partial execution failure
- `BLOCKED` on an unresolved critical review finding
- A G7 tolerance failure returning to `CHALLENGED`
- Negative tests for invalid approval and incomplete publication lineage
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-036_g5_g9_workflows.acceptance.md`](wp_036_g5_g9_workflows.acceptance.md), together with what this package still cannot establish.

- [ ] A producer cannot issue its own acceptance.
- [ ] G9 fails when claim lineage is incomplete.
- [ ] A G7 failure produces a controlled return, never a deletion of history.
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

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A pre-release fault pauses the workflow at the last safe gate; external draft side effects are compensated explicitly.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
