---
title: "WP-004 — Human Decision, SLA, Delegation and Escalation Policy"
aliases:
  - "WP-004"
  - "WP-004 — Human Decision, SLA, Delegation and Escalation Policy"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every decision type in the Human Decision Queue receives an SLA, an evidence summary, a delegation boundary, an expiry and an explicit fail-closed behaviour."
source: "planning/commissioning/01_GOVERNANCE/WP-004_human_decision_sla_delegation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/g1
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/state/not-started
---

# WP-004 — Human Decision, SLA, Delegation and Escalation Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-004` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Project Decision Owner |
| Independent verifier | Safety & Governance Owner |
| Hard dependencies | WP-003 |
| Related gates | G1,G8,G9 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_004_human_decision_sla_delegation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_004_human_decision_sla_delegation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every decision type in the Human Decision Queue receives an SLA, an evidence summary, a delegation boundary, an expiry and an explicit fail-closed behaviour. Human decision capacity is the scarcest resource in the system, and this package is where it is budgeted.


## Analysis

### What this package actually decides

How much human attention the system is allowed to spend, and what happens when it
runs out. `00_PROGRAM/08` states the constraint this package implements: model
capacity is elastic, human decision capacity is not, and a model can generate
more decision requests per day than any person can consider properly.

The decision encoded here is that the queue **waits**. There is no express mode,
because an express review is not a review — and a system that degrades review
depth under load has inverted its own safety property exactly when it needs it.

### Why this is a governance package rather than a UI package

Because the binding artifact is the `DelegationRecord` and the non-delegable
list, not the queue widget. WP-092 builds the surface; WP-004 decides what the
surface is allowed to offer. If the two are done in the wrong order, the
delegation model is inferred from what the UI happened to make easy.

### The failure mode: rubber-stamping

`PR-11` names it and this package owns the counter-controls. Three mechanisms,
all deliverables here rather than later:

1. **Evidence-delta presentation** — the approver is shown what changed since the
   last decision on the same object, not the full package again. Re-reading an
   unchanged package is the behaviour that trains skimming.
2. **Approval expiry** — an approval that has aged past its window is not a
   standing approval. Without this, a decision taken under one evidence state
   silently authorises a different one.
3. **Rationale capture** — a decision with no recorded reason is indistinguishable
   from a click, and the G10 reversal rate cannot be attributed without it.

### The measurement that makes this package honest

`00_PROGRAM/08` names it: decision-time distribution, which evidence sections
were actually opened, the G10 reversal rate, and the rate of acceptance despite an
adversarial rejection. A rising reversal rate is the earliest observable signal of
rubber-stamping. This package must **emit** those signals; WP-091/WP-098 display
them. A decision queue that cannot report how long its decisions took has removed
its own ability to detect the failure it exists to prevent.

### Fail-closed is the default and must be stated per decision type

Sub-task T05 requires explicit fail-closed behaviour. "The SLA expired" must
resolve to a defined state for every decision type — and for material decisions
that state is *not approved*. An SLA that expires into approval is a timer that
grants authority, which is the opposite of a control.

### Baseline v1.2.0 — the intervention vocabulary, and the two things that are never approvals

A human decision is currently modelled as approve or reject. Real intervention is
wider, and the wider set has to be recorded or the audit trail records only the
outcomes that happened to fit two words: `APPROVE`, `REJECT`, `EDIT`,
`GUIDANCE`, `REQUEST_REVISION`, `ROLLBACK`, `ABORT`. Each produces a
`HumanInterventionRecord` with before and after references.

Two things are then structurally excluded rather than defaulted off:

- **A timeout is not an approval.** An expired SLA escalates and pages. There is
  no configuration under which it produces a `DecisionRecord`, because a setting
  that can be turned on is a control that will be turned on — ACC-69.
- **A learned preference is not an authorisation.** That this operator usually
  approves this class may order the queue and suggest an edit format. It may not
  sign anything.

`HumanAttentionScore` follows from the same rule: it orders the queue and carries
no authority, so a mandatory gate at the bottom of the queue still blocks.

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

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md) | `Role Catalog` · `RACI matrix` · `Role-combination policy` · `Role assignment workflow` |

### Full prerequisite closure

**3 of 160 packages (2%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` |

### What acceptance of this package releases

- **Directly unblocked:** 11 — `WP-008` · `WP-013` · `WP-034` · `WP-036` · `WP-038` · `WP-055` · `WP-064` · `WP-089` · `WP-093` · `WP-134` · `WP-156`
- **Transitively reachable:** **152 of 160 packages (95%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **4** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Project Decision Owner |
| Independent verifier | Safety & Governance Owner |
| Gates touched | `G1` · `G8` · `G9` |
| Controls | `CTL-GOV-01` · `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) | Critical | The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |
| [ACC-69 — Human Decision Timeout Must Not Auto-Approve](../12_ACCEPTANCE_SCENARIOS/acc_69_decision_timeout_no_autoapproval.md) | Critical | The state escalates and pages; it never becomes approved. No timeout, no learned preference, no inbound message and no low attention score creates a `DecisionRecord`. |
| [ACC-111 — Insufficient Basis Is Reachable](../12_ACCEPTANCE_SCENARIOS/acc_111_human_insufficient_basis.md) | High | `INSUFFICIENT_BASIS` is reachable in one action and returns the package for more evidence. It is a terminal decision value, not an error, and it does not approve anything. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md)
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
- **Project Decision Owner** carries the acceptance decision; **Safety & Governance Owner** must verify independently of whoever implements.
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
| WP-004-T01 | Classify decision types as material or non-material | Implementation owner | Commit / configuration / record reference |
| WP-004-T02 | Assign an SLA and an escalation chain to each decision | Implementation owner | Commit / configuration / record reference |
| WP-004-T03 | Write the scope, duration and role rules for a `DelegationRecord` | Implementation owner | Commit / configuration / record reference |
| WP-004-T04 | Lock the non-delegable G8, publication, retraction and cutover decisions | Implementation owner | Commit / configuration / record reference |
| WP-004-T05 | Define approval expiry, revocation and evidence-delta behaviour | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Decision policy`
- `SLA/escalation table`
- `Delegation matrix`
- `Decision rationale rubric`
- `Human intervention vocabulary`
- `Timeout escalation path with no approval branch`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-004_human_decision_sla_delegation.tests.md`](wp_004_human_decision_sla_delegation.tests.md).

- A test proving an SLA timeout never produces an automatic approval
- A negative test with forged and expired delegations
- An attempt to delegate a non-delegable decision
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-004_human_decision_sla_delegation.acceptance.md`](wp_004_human_decision_sla_delegation.acceptance.md), together with what this package still cannot establish.

- [ ] A timeout produces only `BLOCKED` or an escalation — never an approval.
- [ ] Every material decision carries a named owner and a written rationale.
- [ ] Out-of-scope use of a delegation is rejected by policy, not by convention.
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

A faulty delegation is revoked and every open decision it touched is returned to the re-evaluation queue.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
