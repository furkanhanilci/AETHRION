# WP-156 — Human Oversight Debiasing and Attention Governance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-156` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Project Decision Owner |
| Independent verifier | Safety & Governance Owner / Internal Audit |
| Hard dependencies | WP-004, WP-038, WP-093 |
| Related gates | G8 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-110, ACC-111, ACC-112 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-156_human_oversight_debiasing.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-156_human_oversight_debiasing.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The human forms and seals a judgement from the evidence before any AI recommendation is revealed, and rejecting never costs more effort than accepting.


## Analysis

### What this package actually decides

The order in which the G8 surface reveals things, and that the order is the
control.

"Humans decide" is the clause most easily satisfied on paper and lost in
practice. A human shown a confident recommendation before the evidence evaluates
the recommendation, not the evidence — `ADR-016`.

### Ordering rather than warning

An automation-bias warning asks someone to discount information they have already
read, which is not a thing people can do on request. Withholding it until they
have formed a view is a thing the **system** can do, and it costs one screen.

First screen: claim, evidence, counter-evidence, protocol deviations,
reproduction status, limitations, unresolved findings. Not the recommendation,
not the confidence score, not the reviewer's verdict.

Then `HumanPreliminaryAssessment` is sealed, the recommendation is revealed, and
any change produces a `DecisionDelta` — ACC-110.

### The delta is the measurement

Where the preliminary assessment and the final decision diverge, something moved
the human — and aggregated, that is the only direct evidence of how much the
recommendation actually drives.

A system that never records the preliminary view cannot distinguish a human who
**agreed** from a human who **deferred**, and those are different facts about the
oversight it claims to have.

### Friction symmetry, and the sixth decision value

If approving is one click and rejecting needs a written justification, a form and
a reviewer, the interface has expressed a preference — and under load people
follow interfaces. **The correction path may not be more laborious than the
approval path**, and ACC-112 tests exactly that.

Six values: `ACCEPT`, `ACCEPT_WITH_LIMITATIONS`, `REVISE`, `REJECT`, `ESCALATE`,
`INSUFFICIENT_BASIS`. The last is the one usually missing and the one that
matters: a human who cannot tell, offered only accept and reject, accepts —
ACC-111.

### What is unchanged and restated here

A timeout never approves. A learned preference never approves.
`HumanAttentionScore` orders and does not authorise. Every intervention is
atomically audited, and a failed audit write fails the edit.

Restated because this is the record a decision-surface implementer reads, and
these are the rules a decision surface is most likely to erode.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |
| [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/WP-038_human_updates_compensation.md) | `Human Update API` · `Cancellation contract` · `Compensation registry` · `Decision authentication tests` |
| [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md) | `Decision Queue UI` · `Evidence-delta component` · `Rationale forms` · `Delegation/escalation views` |

### Full prerequisite closure

**80 of 160 packages (50%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-093` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **41** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Project Decision Owner |
| Independent verifier | Safety & Governance Owner / Internal Audit |
| Gates touched | `G8` |
| Controls | `CTL-GOV-01` · `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-110 — Human Preliminary Assessment Precedes the Recommendation](../12_ACCEPTANCE_SCENARIOS/ACC-110_human_preliminary_assessment.md) | Critical | Neither interface exposes the recommendation before the `HumanPreliminaryAssessment` is sealed. After sealing, the recommendation is revealed and any change produces a `DecisionDelta`. |
| [ACC-111 — Insufficient Basis Is Reachable](../12_ACCEPTANCE_SCENARIOS/ACC-111_human_insufficient_basis.md) | High | `INSUFFICIENT_BASIS` is reachable in one action and returns the package for more evidence. It is a terminal decision value, not an error, and it does not approve anything. |
| [ACC-112 — Correction Friction Symmetry](../12_ACCEPTANCE_SCENARIOS/ACC-112_correction_friction_symmetry.md) | High | Rejecting, revising and declaring insufficient basis require no more actions than approving. Evidence deep links open in one action. An interface that makes correction more laborious than approval fails this scenario. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/WP-038_human_updates_compensation.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md)
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
| `Human Update API` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Cancellation contract` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Compensation registry` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Decision authentication tests` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Decision Queue UI` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence-delta component` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Rationale forms` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Delegation/escalation views` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Decision audit export` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `HumanAttentionScore` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence delta view` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Human preliminary flow` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Friction symmetry measurement` | `WP-093` | `python3 scripts/progress.py show WP-093` |

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
- **Project Decision Owner** carries the acceptance decision; **Safety & Governance Owner / Internal Audit** must verify independently of whoever implements.
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
| WP-156-T01 | Define `HumanPreliminaryAssessment` and its sealing | Implementation owner | Commit / configuration / record reference |
| WP-156-T02 | Implement the evidence-first reveal order in UI and API | Implementation owner | Commit / configuration / record reference |
| WP-156-T03 | Define `DecisionDelta` and record every post-reveal change | Implementation owner | Commit / configuration / record reference |
| WP-156-T04 | Implement the six decision values including `INSUFFICIENT_BASIS` | Implementation owner | Commit / configuration / record reference |
| WP-156-T05 | Measure and enforce friction symmetry between approve and reject | Implementation owner | Commit / configuration / record reference |
| WP-156-T06 | Bind attention priority to queue order only, with no authority | Implementation owner | Commit / configuration / record reference |
| WP-156-T07 | Emit preliminary-versus-final divergence to the metascience plane | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `HumanPreliminaryAssessment`
- `DecisionDelta`
- `Six-value decision vocabulary`
- `Friction symmetry measurement`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-156_human_oversight_debiasing.tests.md`](WP-156_human_oversight_debiasing.tests.md).

- The AI recommendation must not be reachable before the preliminary assessment is sealed
- The same ordering must hold through the API, not only the UI
- `INSUFFICIENT_BASIS` must be reachable in one action and must return the package
- The reject path must not require more actions than the approve path
- A timeout, a learned preference and an attention score must each fail to approve
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-156_human_oversight_debiasing.acceptance.md`](WP-156_human_oversight_debiasing.acceptance.md), together with what this package still cannot establish.

- [ ] No recommendation is reachable, by any interface, before the preliminary assessment is sealed.
- [ ] Preliminary-versus-final divergence is recorded and aggregated as an oversight measure.
- [ ] Rejecting, revising and declaring insufficient basis cost no more effort than accepting.
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

A preliminary assessment is immutable once sealed; a reopened decision creates a new assessment and a new delta, so the sequence of what the human thought and when stays reconstructable.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
