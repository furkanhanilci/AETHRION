# WP-002 — Scope, NFRs and Requirement Traceability

## Package card

| Field | Value |
|---|---|
| Work package | `WP-002` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Assurance Lead |
| Hard dependencies | WP-001 |
| Related gates | Program |
| Related controls | CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-002_scope_nfr_traceability.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-002_scope_nfr_traceability.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Functional scope and the durability, traceability, isolation, idempotency, audit, privacy, cost and accessibility NFRs are converted into testable requirements. A requirement that cannot be tested is a preference, and is recorded as one.


## Analysis

### What this package actually decides

The boundary between a requirement and a preference. Its own purpose statement
draws it: *a requirement that cannot be tested is a preference, and is recorded
as one.* That single rule is the package's entire contribution, and applying it
honestly is what makes it hard — because most NFRs arrive as adjectives.

"The system must be auditable" is a preference. "Any claim resolves to its source
span, run, review and decision in one query returning in under N seconds" is a
requirement, because it can fail.

### Why this sits directly under the charter

The traceability spine `REQ → WP → TST/ACC → Evidence → Decision` is established
here, and every later package hangs off it. `00_PROGRAM/06` states the go-live
dossier must answer that query **for any requirement** — which is only possible
if `REQ` identifiers exist before the packages that satisfy them are refined.
Establishing the spine after the fact means retrofitting identifiers onto work
already done, and retrofitted traceability is traceability nobody trusts.

### The failure mode

NFR targets chosen for achievability rather than need. A latency target set to
whatever the prototype happens to do is not a requirement; it is a measurement
wearing a requirement's clothes, and it will never fail, which means it will
never inform a decision.

The counter-control is sub-task T02's insistence that every NFR carry a
**measurement method** and a **test owner** alongside the target. A target with
no measurement method cannot be gamed because it cannot be evaluated at all —
which is worse.

### The specific gap this package inherits

`00_PROGRAM/05` records that the current package template's acceptance criteria
are *not measurable in the sense meant here*. WP-002 is where that is fixed at
the requirement level; the per-package fix happens at refinement. If WP-002 ships
with generic NFRs, every one of the 140 packages downstream inherits generic
acceptance criteria, and the programme loses the ability to close anything
objectively. This is the highest-leverage document package in the programme for
that reason.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md) | `CommissioningCharter` · `Program authority matrix` · `Initial budget envelope` · `Executive DecisionRecord` |

### Full prerequisite closure

**1 of 141 packages (1%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-003` · `WP-005` · `WP-006` · `WP-010` · `WP-091` · `WP-101` · `WP-109`
- **Transitively reachable:** **138 of 141 packages (98%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **2** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | Chief Architect |
| Independent verifier | Assurance Lead |
| Gates touched | `Program` |
| Controls | `CTL-GOV-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md)
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
| `CommissioningCharter` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Program authority matrix` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Initial budget envelope` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Executive DecisionRecord` | `WP-001` | `python3 scripts/progress.py show WP-001` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `S`** — small — one owner, one review cycle.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Chief Architect** carries the acceptance decision; **Assurance Lead** must verify independently of whoever implements.
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
| WP-002-T01 | Extract the functional capability list with `REQ` identifiers | Implementation owner | Commit / configuration / record reference |
| WP-002-T02 | Assign a target, a measurement method and a test owner to every NFR | Implementation owner | Commit / configuration / record reference |
| WP-002-T03 | Separate out the areas that need a domain-specific profile from the generic core | Implementation owner | Commit / configuration / record reference |
| WP-002-T04 | Define the REQ → WP → TST/ACC traceability schema | Implementation owner | Commit / configuration / record reference |
| WP-002-T05 | Record the out-of-scope items and the rules for handling future requests | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Requirement Registry`
- `NFR scorecard`
- `Traceability matrix seed`
- `Scope boundary record`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-002_scope_nfr_traceability.tests.md`](WP-002_scope_nfr_traceability.tests.md).

- An existence test proving every `REQ` carries measurable acceptance
- Owner review of every out-of-scope item
- An NFR contradiction and feasibility walkthrough
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-002_scope_nfr_traceability.acceptance.md`](WP-002_scope_nfr_traceability.acceptance.md), together with what this package still cannot establish.

- [ ] 100% of material requirements carry an owner and a test.
- [ ] No unquantified 'fast / secure / scalable' phrasing remains.
- [ ] Domain profiles are separated from the generic core.
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

- A policy that is written but not machine-checkable is an intention, not a control.
- Role and authority documents drift silently; every change here needs a baseline bump.
- The hardest failure in this workstream is a rule that everyone agrees with and nobody can enforce.

## Rollback / compensation

Requirements that cannot be traced return to draft status; no downstream package may be marked `READY` against them.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
