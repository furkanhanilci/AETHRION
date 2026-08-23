# WP-001 — Commissioning Charter and Programme Authority

## Package card

| Field | Value |
|---|---|
| Work package | `WP-001` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Executive Sponsor |
| Independent verifier | Internal Audit / Commissioning Board |
| Hard dependencies | — |
| Related gates | Program |
| Related controls | CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-001_commissioning_charter.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-001_commissioning_charter.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The programme's purpose, its production boundary, its funding authority, its decision bodies and the single-cutover rule are brought into force through a signed charter. Until this charter exists, no other package has the standing to bind anyone.


## Analysis

### What this package actually decides

Who is allowed to stop the programme. Everything else in the charter — outcome,
scope, budget envelope, KPIs — is subordinate to that, because a programme that
can only be continued is not being governed.

The charter is the sole source of *standing*. Until it is signed, no other
package binds anyone: WP-003 can catalogue roles, but a role catalogue with no
charter behind it is a description of who does what, not an assignment of
authority to anyone.

### Why it is one of only two packages with no dependencies

Because authority cannot be derived from work already done. Every other package
in the programme inherits its right to exist from this one; if WP-001 depended on
anything, that thing would be the real charter.

### The failure mode

A charter that lists decision **bodies** without naming decision **holders**.
"The Commissioning Board approves cutover" is not an authority assignment; it is
a deferral, and it fails at exactly the moment it is needed, because the board's
composition becomes the argument instead of the decision. Sub-task T03 is
therefore the load-bearing one: cutover authority and abort authority are named
individually, and they are the two that cannot be delegated.

### The tension a single-operator programme creates here

`ADR-001` permits R1 acceptance by a solo operator under a declared profile, and
this package's own verifier is *Internal Audit / Commissioning Board* — a body
that does not exist. The charter must therefore either name a real external
signatory or **declare the gap** with the same explicitness ADR-001 used for R3.
Declaring it is legitimate; leaving it implied is the failure this whole
repository is built against.

### Anti-metrics are not optional here

Sub-task T05 requires anti-metrics alongside KPIs. In a model-operated programme
the obvious KPIs — packages accepted per week, scenarios passing, claims produced
— are all trivially satisfiable by lowering the bar. The anti-metrics are what
make the KPIs safe to optimise: G10 reversal rate, acceptance-despite-adversarial
-rejection rate, and median human decision time are the three that detect a
programme gaming itself.

### Baseline v1.3.0 — the invariants a cost optimiser must not be able to reach

Three additions, and they share a shape: each names something that an
efficiency argument would otherwise be free to trade away.

**The cohort is not a lever.** `ADR-011` fixes that substantial scientific
execution requires at least two epistemically independent cognitive
contributions. Independence is a five-dimension profile, not a count — several
instances of one model on one context are one contribution. Governance language
here must make that an invariant rather than a default, because the pressure to
relax it will arrive as a budget conversation.

**Two disciplines, composable, neither collapsed.** `ADR-012`. A passing test is
not a confirmed hypothesis and a preregistered analysis is not correct code. The
four pairs that get conflated — TDD against preregistration, code review against
scientific review, debugging against anomaly investigation, parallel agents
against parallel analysts — stay distinct in the role, risk and control language.

**What budget may and may not degrade.** Communication verbosity degrades; the
cohort and the assurance route do not. A task that cannot afford its required
assurance is `BLOCKED`, never quietly completed more cheaply. The new
non-waivable controls follow from that: cohort integrity, assurance-route
integrity, human preliminary judgment before recommendation, and specification
conformance for confirmatory work.

## Out of scope

- Technology selection
- The detailed delivery calendar
- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

**None.** This package depends on nothing and can start at `t0`. Only two packages in the programme have this property.

### Full prerequisite closure

**Empty.** Nothing has to happen before this package.

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-002` · `WP-003` · `WP-005` · `WP-021`
- **Transitively reachable:** **158 of 160 packages (99%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **1** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **S** |
| Accountable owner | Executive Sponsor |
| Independent verifier | Internal Audit / Commissioning Board |
| Gates touched | `Program` |
| Controls | `CTL-GOV-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- No hard dependency — this package can start as soon as the programme is authorised.
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

**No upstream inputs.** Everything this package needs, it produces.

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
- **Executive Sponsor** carries the acceptance decision; **Internal Audit / Commissioning Board** must verify independently of whoever implements.
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
| WP-001-T01 | Write the business outcome, the scope and the explicit out-of-scope boundary | Implementation owner | Commit / configuration / record reference |
| WP-001-T02 | Assign the authorities of the Executive Sponsor, Programme Lead, Chief Architect, Assurance and Safety | Implementation owner | Commit / configuration / record reference |
| WP-001-T03 | Define who holds production cutover authority and who holds abort authority | Implementation owner | Commit / configuration / record reference |
| WP-001-T04 | Record the initial budget envelope together with procurement limits | Implementation owner | Commit / configuration / record reference |
| WP-001-T05 | Obtain approval of the success KPIs, the anti-metrics and the stop/pivot conditions | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `CommissioningCharter`
- `Program authority matrix`
- `Initial budget envelope`
- `Executive DecisionRecord`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-001_commissioning_charter.tests.md`](WP-001_commissioning_charter.tests.md).

- Charter schema and mandatory-field validation
- An authority-collision tabletop exercise
- A cutover/abort decision walkthrough
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-001_commissioning_charter.acceptance.md`](WP-001_commissioning_charter.acceptance.md), together with what this package still cannot establish.

- [ ] Every accountable role is filled by a **named person**, not a job title.
- [ ] The single-cutover rule and the zero-critical-finding condition are stated explicitly.
- [ ] Budget, scope and stop/pivot authorities are signed.
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

If the charter is not accepted, no platform procurement and no production commitment is opened; the draft is archived with the reason for rejection recorded.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
