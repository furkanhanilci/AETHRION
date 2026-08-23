---
title: "WP-015 — Event Envelope, Subject and Schema Taxonomy"
aliases:
  - "WP-015"
  - "WP-015 — Event Envelope, Subject and Schema Taxonomy"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "For events published after the canonical commit, the identity, causation, actor, data class, payload reference, version and retention contract are completed."
source: "planning/commissioning/02_CONTRACTS/WP-015_event_envelope_taxonomy.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-015 — Event Envelope, Subject and Schema Taxonomy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-015` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Event Platform Lead |
| Independent verifier | Control Plane Lead / Security |
| Hard dependencies | WP-011, WP-012, WP-014 |
| Related gates | Platform |
| Related controls | CTL-OPS-01, CTL-OBS-01 |
| Related acceptance scenarios | ACC-12, ACC-34 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_015_event_envelope_taxonomy.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_015_event_envelope_taxonomy.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

For events published **after** the canonical commit, the identity, causation, actor, data class, payload reference, version and retention contract are completed. Events describe what already happened; they never decide what happens next.


## Analysis

### What this package actually decides

That events describe the past. The purpose sentence is the invariant: *events
describe what already happened; they never decide what happens next.*

That single line is the whole architectural boundary between the Event plane and
the Control plane, and `PR-07` is what happens when it is not enforced: *a NATS
consumer changes gate state.* Rated critical. Once one consumer does it, the
authoritative history of the workflow is split between Temporal and whichever
consumer acted, and replay stops being sound.

### Why the envelope carries a payload *reference* rather than the payload

T03 separates an inline payload from an encrypted reference, and the rule that
follows is the one the acceptance criteria enforce: **no PII, D3 or D4 payload in
an event body.** An event stream is replayed, retained, mirrored to a DLQ and read
by consumers with different authorisations. Anything in the body inherits the
weakest of those, permanently — you cannot unpublish an event.

### At-least-once is a contract on the consumer, not a promise from the broker

T04's phrasing matters: *the at-least-once delivery and idempotent-consumer
expectation.* NATS will deliver twice. The envelope's job is to make that
survivable by carrying an idempotency key, and the consumer's job is to use it.
`ACC-12` tests exactly this: a duplicate arrives and **exactly one** business
effect occurs.

That is `00_PROGRAM/01` success invariant 2 — the same external side effect
happens exactly once across retry and replay — reduced to one field and one
consumer rule.

### `replay_mode` is the field most likely to be forgotten (T05)

A replayed event and a live event look identical to a consumer unless the envelope
says otherwise. A consumer that cannot tell them apart will re-send the
notification, re-charge the budget, re-open the ticket. `replay_mode` is what lets
a consumer be idempotent about *effects* rather than only about state.

### The subject taxonomy is a retention decision in disguise (T02)

Subjects group events, and retention is set per subject. Choosing the taxonomy
therefore chooses what is kept and for how long — which means a subject chosen for
readability can silently set a security or cost property. The retention table is a
deliverable for that reason: subject and retention are decided together or not at
all.

### `ACC-34` is the case nobody designs for

DLQ repair. A poisoned event is corrected and replayed, and the two hazards are a
consumer loop and a lost causation chain. The envelope has to carry enough for the
corrected event to state what it replaces, or the audit trail forks.

### Baseline v1.3.0 — new records, and the authority typing that keeps them honest

The contract surface gains the records this baseline's capabilities need, and
one field that matters more than any of them.

**New canonical records:** `AgentCohortRecord`, `CognitiveDiversityProfile`,
`CommunicationEdgePolicy`, `BlackboardEntry`, `TypedAgentMessage`,
`CommunicationUtilityRecord`, `ContextProjectionRecord`,
`MemoryInterventionRecord`, `ResearchBudgetContract`, `TokenLedgerEntry`,
`SpecificationConformanceRecord`, `HumanPreliminaryAssessment`, `DecisionDelta`,
`ModelExecutionFingerprint`, `BenchmarkRunPolicy`, `ContaminationFinding`,
`UpstreamAssimilationRecord`.

**Explicit authority typing.** Every record carries what it may never become. The
three conversions this baseline forbids are all of the same kind, and each has
already been attempted somewhere in the field:

| Forbidden conversion | Why it is tempting |
|---|---|
| A blackboard entry into evidence | It is where the interesting sentences appear |
| A communication or search utility score into a claim confidence | It is a number, and it correlates with something |
| An event payload into gate authority | It is the fastest path and it usually works |

The rule that makes them checkable rather than remembered: **events, blackboard
entries and derived read models cannot masquerade as canonical scientific
state**, and the schema is where that is enforced.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |

### Full prerequisite closure

**13 of 160 packages (8%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 9 | `WP-012` |
| 10 | `WP-014` |

### What acceptance of this package releases

- **Directly unblocked:** 10 — `WP-020` · `WP-028` · `WP-032` · `WP-037` · `WP-039` · `WP-049` · `WP-096` · `WP-099` · `WP-100` · `WP-149`
- **Transitively reachable:** **140 of 160 packages (88%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **11** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Event Platform Lead |
| Independent verifier | Control Plane Lead / Security |
| Gates touched | `Platform` |
| Controls | `CTL-OPS-01` · `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-12 — Duplicate Event Delivery](../12_ACCEPTANCE_SCENARIOS/acc_12_duplicate_event.md) | Critical | Exactly one business effect occurs, the duplicate is acknowledged and audited, and the side effect is not performed a second time. |
| [ACC-34 — DLQ Repair and Corrected Replay](../12_ACCEPTANCE_SCENARIOS/acc_34_dlq_repair.md) | High | No consumer loop forms; owner, diagnostics and audit are complete, the corrected event is processed exactly once and the original causation is preserved. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md)
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
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |

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
- **Event Platform Lead** carries the acceptance decision; **Control Plane Lead / Security** must verify independently of whoever implements.
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
| WP-015-T01 | Fix the `EventEnvelope` fields | Implementation owner | Commit / configuration / record reference |
| WP-015-T02 | Establish the workflow, artifact, evidence, security, cost and telemetry subject taxonomy | Implementation owner | Commit / configuration / record reference |
| WP-015-T03 | Write the rule separating an inline payload from an encrypted reference | Implementation owner | Commit / configuration / record reference |
| WP-015-T04 | Add the at-least-once delivery and idempotent-consumer expectation | Implementation owner | Commit / configuration / record reference |
| WP-015-T05 | Define schema evolution and `replay_mode` semantics | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `EventEnvelope schema`
- `Event Catalog seed`
- `Subject/retention table`
- `Consumer contract`
- `Post-commit event taxonomy for the collaboration plane`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-015_event_envelope_taxonomy.tests.md`](wp_015_event_envelope_taxonomy.tests.md).

- A duplicate-event fixture
- A negative test writing a D3 payload into the event body
- A major-schema replay-compatibility test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-015_event_envelope_taxonomy.acceptance.md`](wp_015_event_envelope_taxonomy.acceptance.md), together with what this package still cannot establish.

- [ ] Every event carries event, causation, correlation and idempotency identifiers.
- [ ] No NATS event can change gate state on its own.
- [ ] No PII, D3 or D4 payload enters an event body.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

An incompatible event is routed to the DLQ; producer and consumer stay on the old subject and migrate through an adapter.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
