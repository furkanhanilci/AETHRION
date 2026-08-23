---
title: "WP-039 — Event Consumer, DLQ and Safe Replay Framework"
aliases:
  - "WP-039"
  - "WP-039 — Event Consumer, DLQ and Safe Replay Framework"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every consumer implements idempotency, canonical-commit-before-ACK, poison-event DLQ handling, replay modes and the projection rebuild contract through one shared SDK."
source: "planning/commissioning/04_CONTROL_EVENT/WP-039_event_consumer_dlq_replay.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/04-control-event
  - aethrion/wave/w3
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-039 — Event Consumer, DLQ and Safe Replay Framework

## Package card

| Field | Value |
|---|---|
| Work package | `WP-039` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Event Platform Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-015, WP-020, WP-028, WP-032 |
| Related gates | Platform,G10 |
| Related controls | CTL-OPS-01 |
| Related acceptance scenarios | ACC-12, ACC-34 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_039_event_consumer_dlq_replay.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_039_event_consumer_dlq_replay.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every consumer implements idempotency, canonical-commit-before-ACK, poison-event DLQ handling, replay modes and the projection rebuild contract through one shared SDK.


## Analysis
### What this package actually decides

That every consumer is correct by default, because there is one SDK and it does
the hard parts. Idempotency, ACK ordering, DLQ handling and replay semantics are
each easy to get subtly wrong, and a system with fifteen consumers each
implementing them independently has fifteen chances.

### Canonical-commit-before-ACK is the ordering that matters (T02)

ACK first and the consumer can crash having acknowledged work it never did — the
event is gone. Commit first and a crash before ACK causes redelivery, which the
idempotency key absorbs. The order is not a preference; one of the two loses data
and the other does not.

### `replay_mode` needs two distinct behaviours, not one flag (T04)

Dry-run means *evaluate and report, change nothing*. Read-model-rebuild means
*update projections, perform no external effect*. Collapsing them gives a rebuild
that either does nothing useful or re-sends every notification in the stream's
retention window.

### The conformance suite is the deliverable that makes the SDK a contract (T06)

An SDK anyone may bypass is a library. A conformance suite that every consumer
must pass — including one written by hand — is what makes the guarantees hold
system-wide. This is the same move as WP-020's contract-test harness, one layer
down.

### Poison-event telemetry is a correctness signal (T05)

A rising DLQ depth means events are not being processed, and the downstream
records simply do not appear. Nothing errors. `PR-20`'s shape again: the failure
mode is silence.

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

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |

### Full prerequisite closure

**30 of 160 packages (19%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-040`
- **Transitively reachable:** **23 of 160 packages (14%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **21** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Event Platform Lead |
| Independent verifier | SRE / Security |
| Gates touched | `Platform` · `G10` |
| Controls | `CTL-OPS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-12 — Duplicate Event Delivery](../12_ACCEPTANCE_SCENARIOS/acc_12_duplicate_event.md) | Critical | Exactly one business effect occurs, the duplicate is acknowledged and audited, and the side effect is not performed a second time. |
| [ACC-34 — DLQ Repair and Corrected Replay](../12_ACCEPTANCE_SCENARIOS/acc_34_dlq_repair.md) | High | No consumer loop forms; owner, diagnostics and audit are complete, the corrected event is processed exactly once and the original causation is preserved. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md)
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
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |

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
- **Event Platform Lead** carries the acceptance decision; **SRE / Security** must verify independently of whoever implements.
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

### No registered source names this package

Neither register binds an upstream mechanism or a runtime component to `WP-039`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-039-T01 | Write the consumer middleware and unique-key standard | Implementation owner | Commit / configuration / record reference |
| WP-039-T02 | Apply the ACK transaction boundary | Implementation owner | Commit / configuration / record reference |
| WP-039-T03 | Establish DLQ metadata, retry/backoff and the repair workflow | Implementation owner | Commit / configuration / record reference |
| WP-039-T04 | Define `replay_mode` = dry-run and read-model-rebuild behaviour | Implementation owner | Commit / configuration / record reference |
| WP-039-T05 | Add offset, lag and poison-event telemetry | Implementation owner | Commit / configuration / record reference |
| WP-039-T06 | Publish a reference consumer conformance suite | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Consumer SDK`
- `DLQ service/runbook`
- `Replay controller`
- `Conformance tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-039_event_consumer_dlq_replay.tests.md`](wp_039_event_consumer_dlq_replay.tests.md).

- A duplicate-delivery test
- A crash before the side-effect commit
- Prevention of an infinite poison-event loop
- Denial of external mutation during a replay
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-039_event_consumer_dlq_replay.acceptance.md`](wp_039_event_consumer_dlq_replay.acceptance.md), together with what this package still cannot establish.

- [ ] Exactly-once business effect is achieved through idempotency, not through delivery guarantees.
- [ ] Every DLQ record carries an owner and a correction path.
- [ ] A replay never automatically repeats a production mutation.
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

A consumer rollback does not lose its offset; a new version is verified as a shadow consumer before cutover.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
