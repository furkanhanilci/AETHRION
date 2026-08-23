# WP-151 — Memory Masking and Proactive Intervention

## Package card

| Field | Value |
|---|---|
| Work package | `WP-151` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Assurance Lead / Archivist |
| Hard dependencies | WP-146, WP-150 |
| Related gates | G5,G6,G10 |
| Related controls | CTL-EPI-04, CTL-DAT-03 |
| Related acceptance scenarios | ACC-096, ACC-097, ACC-098 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-151_memory_masking_and_intervention.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-151_memory_masking_and_intervention.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

What an actor is reminded of is selected by epistemic status and relevance, and a refuted or superseded item cannot re-enter reasoning as though it were current.


## Analysis

### What this package actually decides

Which of the six memories reaches a given invocation, and in what state.

WP-146 established the stores and their authority. This package is the read path:
a `MemoryMask` evaluating relevance, epistemic status, freshness, contradiction
status, source authority, task dependence and redundancy per item.

### A refuted memory is the specific hazard

Published work on multi-agent debate memory shows that erroneous prior turns
degrade later reasoning — an agent that read a wrong intermediate conclusion
carries it forward even after it was refuted.

So `REFUTED`, `SUPERSEDED`, unverified interpretation and stale procedural advice
**cannot enter ordinary reasoning context** — ACC-096. They remain fully visible
to a failure-history query, because *what did we already try and why did it fail*
is a different question from *what is currently true*, and answering the first
one is why WP-146 keeps failed approaches at all.

### Proactive, but not chatty

A reminder is emitted when the mask judges it material — a frozen constraint the
current step is about to violate, a prior refutation of the direction being
taken. Not every turn.

Two rules keep it from becoming noise or authority: a reminder carries canonical
artifact references, and **a reminder never creates a claim**. It points at
something that already exists — ACC-097.

### Anti-poisoning

Search experience, procedural memory and principle memory are never substituted
for the evidence store, and a lesson extracted from a `FailedApproach` is not an
accepted fact.

ACC-098 attacks exactly this: content crafted to enter memory and be retrieved
later as though it were established. The defence is the typed store and its
authority field, not a filter on the content.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-146 — Epistemic Memory Taxonomy and Retention](../14_SCIENTIFIC_INTELLIGENCE/WP-146_epistemic_memory_taxonomy.md) | `Six memory type contracts` · `FindingRecord` · `FailedApproach` · `NegativeResult` |
| [WP-150 — Communication Governor, Edge Utility and Context Projection](../15_RELIABILITY_EFFICIENCY/WP-150_communication_governor_and_context_projection.md) | `CommunicationValue` · `CommunicationUtilityRecord` · `ContextProjectionRecord` · `Quality guard and rollback` |

### Full prerequisite closure

**86 of 160 packages (54%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 30 | `WP-067` · `WP-070` · `WP-096` · `WP-144` |
| 31 | `WP-068` · `WP-071` · `WP-100` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` · `WP-146` |
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
| Effort class | **M** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Assurance Lead / Archivist |
| Gates touched | `G5` · `G6` · `G10` |
| Controls | `CTL-EPI-04` · `CTL-DAT-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-096 — A Refuted Memory Does Not Re-Enter Reasoning](../12_ACCEPTANCE_SCENARIOS/ACC-096_refuted_memory_mask.md) | High | None of the three enters ordinary reasoning context. All three remain fully visible to the failure-history query, because *what did we try* and *what is true* are different questions. |
| [ACC-097 — Proactive Reminder of a Frozen Constraint](../12_ACCEPTANCE_SCENARIOS/ACC-097_proactive_frozen_constraint_reminder.md) | High | A reminder is emitted carrying canonical artifact references. It creates no claim and asserts nothing new. On an ordinary step with no material constraint at stake, no reminder is emitted. |
| [ACC-098 — Memory Poisoning Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-098_memory_poisoning_attempt.md) | Critical | The content is stored in a typed store whose authority field forbids claim support. It cannot be retrieved as evidence, cannot support a claim, and a lesson derived from a failed approach is not an accepted fact. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-146 — Epistemic Memory Taxonomy and Retention](../14_SCIENTIFIC_INTELLIGENCE/WP-146_epistemic_memory_taxonomy.md), [WP-150 — Communication Governor, Edge Utility and Context Projection](WP-150_communication_governor_and_context_projection.md)
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
| `Six memory type contracts` | `WP-146` | `python3 scripts/progress.py show WP-146` |
| `FindingRecord` | `WP-146` | `python3 scripts/progress.py show WP-146` |
| `FailedApproach` | `WP-146` | `python3 scripts/progress.py show WP-146` |
| `NegativeResult` | `WP-146` | `python3 scripts/progress.py show WP-146` |
| `MethodExperience` | `WP-146` | `python3 scripts/progress.py show WP-146` |
| `MemoryQuery policy` | `WP-146` | `python3 scripts/progress.py show WP-146` |
| `Retention and revalidation jobs` | `WP-146` | `python3 scripts/progress.py show WP-146` |
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

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Knowledge Lead** carries the acceptance decision; **Assurance Lead / Archivist** must verify independently of whoever implements.
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
| WP-151-T01 | Define `MemoryMask` policy and its seven evaluation dimensions | Implementation owner | Commit / configuration / record reference |
| WP-151-T02 | Implement exclusion of refuted, superseded and stale items from reasoning context | Implementation owner | Commit / configuration / record reference |
| WP-151-T03 | Preserve full visibility of excluded items to failure-history queries | Implementation owner | Commit / configuration / record reference |
| WP-151-T04 | Define `MemoryInterventionRecord` and the reminder emission rule | Implementation owner | Commit / configuration / record reference |
| WP-151-T05 | Bind the mask to the context projection of WP-150 | Implementation owner | Commit / configuration / record reference |
| WP-151-T06 | Build the memory-poisoning fixture suite | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `MemoryMask policy`
- `MemoryInterventionRecord`
- `Memory poisoning fixture suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-151_memory_masking_and_intervention.tests.md`](WP-151_memory_masking_and_intervention.tests.md).

- A refuted memory item must not appear in ordinary reasoning context
- The same item must remain retrievable by a failure-history query
- A reminder must carry canonical artifact references and must create no claim
- A planted poisoning attempt must not become retrievable as established fact
- Procedural or search memory must not substitute for the evidence store
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-151_memory_masking_and_intervention.acceptance.md`](WP-151_memory_masking_and_intervention.acceptance.md), together with what this package still cannot establish.

- [ ] Epistemic status governs context entry, and the same item stays queryable as history.
- [ ] A reminder points at canonical artifacts and never introduces a new assertion.
- [ ] The planted poisoning fixture does not survive into a reasoning context.
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

A mask is a read policy: changing it changes what future invocations see and never alters, deletes or re-labels a stored memory item.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
