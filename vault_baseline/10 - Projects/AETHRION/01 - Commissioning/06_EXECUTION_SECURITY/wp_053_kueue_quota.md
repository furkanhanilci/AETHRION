---
title: "WP-053 — Kueue Queue, Quota and Priority Policy"
aliases:
  - "WP-053"
  - "WP-053 — Kueue Queue, Quota and Priority Policy"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Research scouting, experiments, review, reproduction, incident and critical assurance work are scheduled under budget, quota, admission and safe preemption."
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-053_kueue_quota.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w3
  - aethrion/effort/m
  - aethrion/gate/g5-g7
  - aethrion/state/not-started
---

# WP-053 — Kueue Queue, Quota and Priority Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-053` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Compute Platform Lead |
| Independent verifier | FinOps / Assurance / SRE |
| Hard dependencies | WP-006, WP-052 |
| Related gates | G5–G7 |
| Related controls | CTL-CST-01, CTL-SEC-04 |
| Related acceptance scenarios | ACC-09, ACC-33 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_053_kueue_quota.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_053_kueue_quota.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Research scouting, experiments, review, reproduction, incident and critical assurance work are scheduled under budget, quota, admission and safe preemption.


## Analysis
### What this package actually decides

Who waits when there is not enough compute. Every queueing system encodes a
priority order, and the decision here is that **assurance is not preemptible by
delivery**.

`00_PROGRAM/08` protects two pools for the same stated reason: both produce
information that delivery pressure would otherwise trade away, and both produce it
slowly. Assurance is one; metascience is the other.

### Budget reservation binds compute to the workflow (T04)

A Temporal task that dispatches compute without reserving budget discovers the
limit halfway through a batch. `00_PROGRAM/01` invariant 9 is explicit: at a hard
budget limit **no new expensive work opens** and the workflow **pauses without
losing state**.

Reservation before dispatch is what makes that a control rather than an
after-the-fact accounting entry — the same discipline WP-045 applies to model
fan-out.

### Preemption must checkpoint or it is data loss (T05)

Preempting a long experiment run and losing its progress converts a scheduling
decision into a research cost. Preemption is legitimate; preemption without a
checkpoint contract is not.

### Queue wait is a leading indicator (T06)

`PR-04` — *verification backlog grows*, early signal *G6/G7 waiting and bypass
requests* — shows up here first, as queue wait on the assurance queue. By the time
it shows up as a bypass request, the pressure has already been applied to a human.

### Baseline v1.3.0 — four zones, a capability gate, and a benchmark firewall

The isolation story gains a fourth zone and two new attack surfaces.

**Four zones, not three.** Producer, evaluator, reproducer and independent
grader, separated in secrets, cache and workspace. The leakage paths that matter
are the quiet ones — a shared cache, an inherited credential, a warm container
layer — and none of them looks like a boundary violation in a log. Each is tested
explicitly rather than inferred from the zone configuration (ACC-113).

**Security is a capability, not a prompt.** *Prompt says safe* is not security;
*the capability is unavailable unless policy grants it* is. External content —
PDF, web page, tool result, reviewer comment — is quarantined into a data object,
and the agent's tool intent passes a policy gate before any credential is
injected (ACC-117).

**A benchmark firewall.** An evaluation run freezes its dataset manifest, network
mode, allowed domains, known identifiers and evaluator isolation before it
starts, and audits every retrieval. Gold answers, private rubrics, hidden tests
and grader prompts are unreachable from the agent environment (ACC-118).

The attack suite gains ASB and WASP as external regressions, alongside internal
fixtures for source-PDF injection, malicious citation text, tool-result
injection, memory poisoning and credential exfiltration.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |

### Full prerequisite closure

**28 of 160 packages (18%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-026` · `WP-051` |
| 17 | `WP-024` |
| 18 | `WP-027` |
| 19 | `WP-052` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-054` · `WP-060` · `WP-083` · `WP-084` · `WP-100` · `WP-111` · `WP-117`
- **Transitively reachable:** **88 of 160 packages (55%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **20** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Compute Platform Lead |
| Independent verifier | FinOps / Assurance / SRE |
| Gates touched | `G5–G7` |
| Controls | `CTL-CST-01` · `CTL-SEC-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) | Critical | An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created. |
| [ACC-33 — Kueue Preemption](../12_ACCEPTANCE_SCENARIOS/acc_33_kueue_preemption.md) | High | The scout is checkpointed, paused or evicted and the critical reproduction is admitted; canonical task state and artifacts are not lost and the scout resumes later. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md)
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
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Producer and evaluator zone profiles` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `MutationPolicy` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Kubernetes clusters` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Node pool catalog` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Namespace/security baseline` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Upgrade/restore runbook` | `WP-052` | `python3 scripts/progress.py show WP-052` |

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
- **Compute Platform Lead** carries the acceptance decision; **FinOps / Assurance / SRE** must verify independently of whoever implements.
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
| WP-053-T01 | Establish the ClusterQueue/LocalQueue and cohort model | Implementation owner | Commit / configuration / record reference |
| WP-053-T02 | Define the project and portfolio quotas and the resource flavours | Implementation owner | Commit / configuration / record reference |
| WP-053-T03 | Apply PriorityClasses and the assurance capacity reserve | Implementation owner | Commit / configuration / record reference |
| WP-053-T04 | Bind budget reservation to the Temporal task | Implementation owner | Commit / configuration / record reference |
| WP-053-T05 | Write the preemption, checkpoint and retry behaviour | Implementation owner | Commit / configuration / record reference |
| WP-053-T06 | Add queue wait, utilisation and cost telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Kueue configuration`
- `Quota/priority policy`
- `Budget admission adapter`
- `Queue dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-053_kueue_quota.tests.md`](wp_053_kueue_quota.tests.md).

- Preemption of a low-priority scout job
- Capacity reservation for a critical reproduction
- Quota and budget denial
- Resume after checkpoint
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-053_kueue_quota.acceptance.md`](wp_053_kueue_quota.acceptance.md), together with what this package still cannot establish.

- [ ] Preemption never loses canonical state or artifacts.
- [ ] Assurance work is never starved by feature fan-out.
- [ ] No service account can bypass quota.
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

- A control not exercised by a negative test is an assumption.
- Default-allow egress anywhere in the chain nullifies every other isolation control.
- Sandbox escape is tested by attempting it, not by reading the configuration.

## Rollback / compensation

A wrong priority or quota bundle returns to its previous version; queued workloads are re-evaluated and running workloads are not forcibly lost.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
