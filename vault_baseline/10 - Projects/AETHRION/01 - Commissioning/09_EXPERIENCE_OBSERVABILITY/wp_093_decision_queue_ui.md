---
title: "WP-093 — Human Decision Queue and Evidence-Delta UI"
aliases:
  - "WP-093"
  - "WP-093 — Human Decision Queue and Evidence-Delta UI"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "The decision owner sees the options, what evidence changed, dissent, residual risk, policy, delegation, SLA and expiry, then issues a signed accept / reject / revise / defer decision."
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g1
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/state/not-started
---

# WP-093 — Human Decision Queue and Evidence-Delta UI

## Package card

| Field | Value |
|---|---|
| Work package | `WP-093` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Governance Product Lead |
| Independent verifier | Project Decision Owner / Accessibility Reviewer |
| Hard dependencies | WP-004, WP-018, WP-038, WP-075, WP-077, WP-089, WP-091 |
| Related gates | G1,G8,G9 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_093_decision_queue_ui.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_093_decision_queue_ui.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The decision owner sees the options, what evidence changed, dissent, residual risk, policy, delegation, SLA and expiry, then issues a signed accept / reject / revise / defer decision.


## Analysis
### What this package actually decides

Where the human decision actually happens, and what the human must see before
making it. This is the surface `00_PROGRAM/08` calls the binding constraint of the
whole system: model capacity is elastic, human decision capacity is not.

### The evidence delta is the anti-rubber-stamp control (T02)

`PR-11` — rubber-stamping, early signal *very fast or generic approvals*. WP-004
built the mechanism; this is where it is presented.

Showing **what changed** since the last decision on this object, rather than the
full package again, is what makes a second decision a decision rather than a
re-scroll. Re-presenting an unchanged package is the behaviour that trains
skimming.

### Dissent must be visible, not summarised away (T02)

A minority reviewer position, an unresolved disagreement, an adversarial reviewer's
counterexample — these are the parts of the package most likely to change a
decision and most likely to be compressed out of a summary. They get their own
place on the surface.

`ACC-38` and `PR-11` both bear on this.

### The rationale rubric turns a click into a decision (T03)

A recorded reason is what makes the G10 reversal rate attributable. Without it, a
reversal tells you the decision was wrong and nothing about why.

### Non-delegable decisions need a banner, not a validation error (T04)

G8, publication, retraction and cutover cannot be delegated (WP-004). Telling
someone *after* they tried is worse than telling them before.

### MFA re-authentication at the point of signing (T05)

A decision is a durable authorisation. Re-authenticating at signature binds the
human identity to the decision at the moment it is taken (WP-055), which is what
the independence claim afterwards rests on.

### Defer is a first-class outcome

Accept, reject, revise, **defer**. A queue that offers only the first three forces
a decision from someone who has correctly concluded they cannot yet make one — and
`00_PROGRAM/08`'s quota model requires waiting to be a legitimate state.

### Baseline v1.2.0 — priority without authority, and the delta a human actually needs

Two additions, and the second is the one that changes what the queue is for.

**`HumanAttentionScore`** orders the queue from gate criticality, verifier
confidence and calibration, novelty, unresolved findings, risk class and
correction history. It carries **no authority**: a mandatory gate at the bottom
of the queue still blocks, and no score, timeout or learned preference produces a
`DecisionRecord` — ACC-69.

**The evidence delta.** A decision surface that shows the full state on every
visit trains its reader to skim. What a returning human needs is what changed
since the last decision: new and removed evidence, changed claim scope, new
failures, reviewer disagreement, reproduction status, and which publication
assertions are affected.

Every edit made here produces a `HumanInterventionRecord` atomically with the
change. If the audit write fails, the edit fails — ACC-68.

### Baseline v1.3.0 — showing the cost of collaboration, and the shape of a decision

The experience and observability layer gains three things it could not
previously display, because they did not exist to be displayed.

**Collaboration cost.** Coordination overhead ratio, redundant message rate,
useful challenge rate, rounds, and the token ledger's seven categories. A single
cost total says a campaign was expensive; the categories say whether it was
expensive because it did science or because it held a meeting.

**The human decision surface, reordered.** Evidence first, recommendation second,
and a `DecisionDelta` when the second changes the first (`ADR-016`). The queue
uses evidence-delta priority — what changed since the last decision, not the full
state every time. **Attention priority orders and never authorises**, and no
timeout or learned preference produces an approval.

**Verifier abstention, surfaced.** An `ABSTAIN` is an escalation signal and has to
look like one in the interface. A surface that renders it as a soft pass has
undone `ADR-015`.

New SLOs: coordination overhead, challenge rate, contamination and security
findings, and the quality/cost Pareto frontier.

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
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/wp_038_human_updates_compensation.md) | `Human Update API` · `Cancellation contract` · `Compensation registry` · `Decision authentication tests` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |
| [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md) | `Cockpit application shell` · `Navigation/IA` · `BFF/read APIs` · `RBAC matrix` |

### Full prerequisite closure

**79 of 160 packages (49%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-102` · `WP-105` · `WP-106` · `WP-135` · `WP-156`
- **Transitively reachable:** **28 of 160 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **40** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Governance Product Lead |
| Independent verifier | Project Decision Owner / Accessibility Reviewer |
| Gates touched | `G1` · `G8` · `G9` |
| Controls | `CTL-GOV-01` · `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) | Critical | The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |
| [ACC-68 — Human Intervention Without an Audit Record](../12_ACCEPTANCE_SCENARIOS/acc_68_human_intervention_audit.md) | Critical | The edit fails and rolls back. There is no path by which a human action changes canonical state without an atomically written `HumanInterventionRecord` carrying before and after references. |
| [ACC-69 — Human Decision Timeout Must Not Auto-Approve](../12_ACCEPTANCE_SCENARIOS/acc_69_decision_timeout_no_autoapproval.md) | Critical | The state escalates and pages; it never becomes approved. No timeout, no learned preference, no inbound message and no low attention score creates a `DecisionRecord`. |
| [ACC-110 — Human Preliminary Assessment Precedes the Recommendation](../12_ACCEPTANCE_SCENARIOS/acc_110_human_preliminary_assessment.md) | Critical | Neither interface exposes the recommendation before the `HumanPreliminaryAssessment` is sealed. After sealing, the recommendation is revealed and any change produces a `DecisionDelta`. |
| [ACC-112 — Correction Friction Symmetry](../12_ACCEPTANCE_SCENARIOS/acc_112_correction_friction_symmetry.md) | High | Rejecting, revising and declaring insufficient basis require no more actions than approving. Evidence deep links open in one action. An interface that makes correction more laborious than approval fails this scenario. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/wp_038_human_updates_compensation.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md)
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
| `Decision policy` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `SLA/escalation table` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Delegation matrix` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Decision rationale rubric` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Human intervention vocabulary` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Timeout escalation path with no approval branch` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Human Update API` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Cancellation contract` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Compensation registry` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Decision authentication tests` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Cockpit application shell` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Navigation/IA` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `BFF/read APIs` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `RBAC matrix` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Accessibility baseline` | `WP-091` | `python3 scripts/progress.py show WP-091` |

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
- **Governance Product Lead** carries the acceptance decision; **Project Decision Owner / Accessibility Reviewer** must verify independently of whoever implements.
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

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-021` — AutoResearchClaw — human-in-the-loop action vocabulary and attention prioritisation | `ADAPTIVE_REIMPLEMENT` | `MS-HITL-001` · `MS-HITL-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-051` — Automation bias and correction effort in human oversight | `PATTERN` | the running implementation | the contract this is held behind | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-021` | A HumanAttentionScore orders a queue. It carries no authority: a mandatory human gate with the lowest score in the queue still blocks. | auto_proceed_on_timeout. Upstream it is a configurable boolean defaulting to false. In AETHRION the capability itself is absent at G8 and at every mandatory human gate, because a setting that can be turned on is a control that will be turned on. |
| `ASM-051` | A debiasing measure changes the order and cost of an interaction. It confers no authority and removes none — the human decision remains the human's. | Any claim that ordering eliminates automation bias. It reduces anchoring; it cannot manufacture attention. |

### Where a plain row would mislead

- **`ASM-021`** — This is the clearest case in the register of an upstream option being deliberately narrowed rather than copied. The action vocabulary is taken; the escape hatch is not.
- **`ASM-051`** — Two findings drive ADR-016. When correction takes more effort, people correct fewer AI errors — which is why friction symmetry between approve and reject is a tested property (ACC-112). And access to AI advice sharply reduces willingness to say 'I don't know', with wrong advice able to raise confidence while lowering accuracy — which is why `INSUFFICIENT_BASIS` exists as a one-action terminal decision (ACC-111).

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-021` — AutoResearchClaw — human-in-the-loop action vocabulary and attention prioritisation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**Acquisition readiness — 1 obligation open across 1 of 2 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-093-T01 | Write the decision inbox, filters, escalation and ownership views | Implementation owner | Commit / configuration / record reference |
| WP-093-T02 | Design the frozen evidence snapshot, delta and dissent summary | Implementation owner | Commit / configuration / record reference |
| WP-093-T03 | Apply the rationale rubric and required-field validation | Implementation owner | Commit / configuration / record reference |
| WP-093-T04 | Add delegation scope and expiry plus the non-delegable banner | Implementation owner | Commit / configuration / record reference |
| WP-093-T05 | Bind MFA re-authentication, signing and update idempotency | Implementation owner | Commit / configuration / record reference |
| WP-093-T06 | Write the decision history, revoke and supersede views | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Decision Queue UI`
- `Evidence-delta component`
- `Rationale forms`
- `Delegation/escalation views`
- `Decision audit export`
- `HumanAttentionScore`
- `Evidence delta view`
- `Human preliminary flow`
- `Friction symmetry measurement`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-093_decision_queue_ui.tests.md`](wp_093_decision_queue_ui.tests.md).

- Denial of a forged or expired approval
- Duplicate submission resolving to one decision
- SLA escalation
- An attempt at a non-delegable action
- The quality rule rejecting a generic rationale
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-093_decision_queue_ui.acceptance.md`](wp_093_decision_queue_ui.acceptance.md), together with what this package still cannot establish.

- [ ] A timeout never becomes an automatic approval.
- [ ] Every decision carries the target, evidence and policy snapshot.
- [ ] Material dissent is never hidden from the decision maker.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A UI error is reconciled through the submission receipt; an uncertain decision is re-read rather than submitted a second time.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
