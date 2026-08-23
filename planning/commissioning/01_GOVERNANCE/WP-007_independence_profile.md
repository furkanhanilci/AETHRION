# WP-007 — IndependenceProfile and Separation-of-Duties Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-007` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Internal Audit / Safety Owner |
| Hard dependencies | WP-003, WP-005 |
| Related gates | G6,G7,G8 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-06, ACC-38 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-007_independence_profile.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-007_independence_profile.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The separation of producer, reviewer and reproducer becomes auditable across seven dimensions: human, model family, context, credential, environment, data path and economic interest.


## Analysis

### What this package actually decides

What the word *independent* is allowed to mean. Seven dimensions — human, model
family, context, credential, environment, data path, economic interest — replace a
claim that a reviewer was independent with a record of the axes along which they
were.

This is the package the audit's finding **C2** runs through, and ADR-001 is a
decision taken **in its absence**: R1 solo, R2 solo under a declared partial
profile, R3 `BLOCKED`. WP-007 is what turns that declaration into something a
machine can check per assignment rather than a policy stated once.

### Why seven dimensions rather than one

Because they fail separately and are separately purchasable. Two different humans
using the same model family are not independent in the way that matters for
correlated error. The same human in two contexts is not independent at all. A
reviewer with an economic interest in the outcome is not independent regardless of
the other six. Collapsing them yields a boolean that is true in the cases where it
matters least.

### The non-compensable dimensions are the real content

T03 asks which dimensions **cannot** be traded against others. This is the
package's hardest question and the one most likely to be softened. A candidate
answer: economic interest and context contamination are non-compensable — no
amount of model-family or environment separation repairs a reviewer who has seen
the producer's trace, because the contamination is in what they now believe.

Whatever the answer, it must be a **list**, and violating an entry must be a
blocker rather than a lower score.

### The gap this package cannot close by itself

Independence here is **structural**, and structural independence is a proxy for
what actually matters: uncorrelated errors. `PR-16` states it precisely —
PR-05 addresses paper independence, not correlated errors between genuinely
different models. Two frontier models from different vendors, trained on
overlapping corpora, may fail together on exactly the cases a reviewer exists to
catch.

So this package must state its own limit: it can prove seven separations were
achieved; it cannot prove the reviewers were likely to disagree. That measurement
belongs to the metascience gap recorded in `00_PROGRAM/11`, and until it exists,
every independence claim in the programme carries an unmeasured assumption.

### Re-evaluation at gate time, not only at assignment

T05 requires the profile to be re-evaluated when the gate is reached, not only
when the reviewer was assigned. Between those two moments a reviewer can acquire
context — through an incident channel, a shared dashboard, or a previous version
of the same package. Assignment-time-only checking is the common implementation
and it is the one that fails silently.

### Baseline v1.2.0 — two independence dimensions that are not about people

The seven dimensions here are about actors. Two more are about **state**, and
both admit violations that every actor-level check passes.

**Evaluator independence.** A producer that can reach the evaluator has
influenced its own score without any actor constraint being broken. The
constraint is a policy zone, not a role assignment.

**Memory-context independence.** A reviewer able to query the producer's
search-experience or procedural memory inherits the producer's dead ends and
framing. The review is anchored, and nothing in the record shows it — the actor
really is different, the profile really does say independent. Blind review
therefore excludes those stores by default, and the exclusion is a property of
the packet rather than a habit of the reviewer.

Both are recorded as pair constraints: producer/evaluator, producer/reviewer,
producer/reproducer, reviewer/reviewer. ACC-65, ACC-72; ADR-005 §6.

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

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/WP-003_role_catalog_raci.md) | `Role Catalog` · `RACI matrix` · `Role-combination policy` · `Role assignment workflow` |
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |

### Full prerequisite closure

**4 of 160 packages (2%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` |

### What acceptance of this package releases

- **Directly unblocked:** 21 — `WP-008` · `WP-009` · `WP-010` · `WP-013` · `WP-036` · `WP-042` · `WP-043` · `WP-045` · `WP-047` · `WP-056` · `WP-070` · `WP-071` · `WP-080` · `WP-084` · `WP-085` · `WP-086` · `WP-088` · `WP-089` · `WP-126` · `WP-147` · `WP-148`
- **Transitively reachable:** **152 of 160 packages (95%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **4** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **M** |
| Accountable owner | Assurance Lead |
| Independent verifier | Internal Audit / Safety Owner |
| Gates touched | `G6` · `G7` · `G8` |
| Controls | `CTL-GOV-02` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-38 — Critical Reviewer Unavailable](../12_ACCEPTANCE_SCENARIOS/ACC-38_reviewer_unavailable.md) | High | Neither the producer, a self-review, nor an ineligible fallback is used; the gate is `BLOCKED` and a human scheduling/escalation item and a capacity signal are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/WP-003_role_catalog_raci.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md)
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
| `Role Catalog` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `RACI matrix` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Role-combination policy` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Role assignment workflow` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `StudyMode decision table` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Substantiality threshold for the multi-agent invariant` | `WP-005` | `python3 scripts/progress.py show WP-005` |

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
- **Assurance Lead** carries the acceptance decision; **Internal Audit / Safety Owner** must verify independently of whoever implements.
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
| WP-007-T01 | Define the seven independence dimensions | Implementation owner | Commit / configuration / record reference |
| WP-007-T02 | Write the minimum required sets for R1, R2 and R3 | Implementation owner | Commit / configuration / record reference |
| WP-007-T03 | Identify the non-compensable dimensions and their blocker rules | Implementation owner | Commit / configuration / record reference |
| WP-007-T04 | Define the frozen-package and context-contamination controls | Implementation owner | Commit / configuration / record reference |
| WP-007-T05 | Design re-evaluation at assignment time and again at gate time | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `IndependenceProfile rubric`
- `Eligibility matrix`
- `Conflict-of-interest declaration`
- `Violation response`
- `Evaluator and memory-context independence constraints`
- `Cohort independence dimensions`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-007_independence_profile.tests.md`](WP-007_independence_profile.tests.md).

- A negative test for planner self-review
- A same-model-family and context-contamination test
- A fail-closed test for the reviewer-unavailable case
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-007_independence_profile.acceptance.md`](WP-007_independence_profile.acceptance.md), together with what this package still cannot establish.

- [ ] There is no single averaged independence score.
- [ ] If human separation cannot be achieved for R3, the workflow becomes `BLOCKED`.
- [ ] A reviewer sees only the frozen package and the context it is permitted to see.
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

Review and reproduction records produced under a violated profile are marked `INVALIDATED` and a fresh independent assignment is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
