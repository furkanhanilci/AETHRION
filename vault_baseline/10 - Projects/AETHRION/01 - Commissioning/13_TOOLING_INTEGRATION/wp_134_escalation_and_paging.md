---
title: "WP-134 — Escalation and Paging"
aliases:
  - "WP-134"
  - "WP-134 — Escalation and Paging"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "SLA breaches, budget hard stops, integrity suspicions and line-stop events escalate along a defined chain."
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-134_escalation_and_paging.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/m
  - aethrion/gate/g0-g10
  - aethrion/state/not-started
---

# WP-134 — Escalation and Paging

## Package card

| Field | Value |
|---|---|
| Work package | `WP-134` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Assurance Lead |
| Hard dependencies | WP-131, WP-132, WP-004 (Human decision SLA) |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-03, CTL-OBS-01 |
| Related acceptance scenarios | ACC-26, ACC-43 |
| Related skill | `escalating-and-paging` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_134_escalation_and_paging.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_134_escalation_and_paging.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

SLA breaches, budget hard stops, integrity suspicions and line-stop events
escalate along a defined chain.

> **Invariant:** A timeout **never** becomes an automatic approval. It either
> escalates to a higher role or the workflow stays paused.

**Acknowledgement is mandatory at every step.** An unacknowledged escalation
moves to the next step; it never disappears.

`CRITICAL` severity events **pierce the quiet-hours policy**: integrity
suspicion, a sandbox escape attempt, a budget hard limit and a positive finding
on a negative control do not wait until morning.


## Analysis
### What this package actually decides

That an unacknowledged escalation **promotes**. Everything else here is routing; the
promotion rule is the control, because it is what makes an escalation chain
terminate in a person rather than in a queue.

### The four triggers are chosen deliberately

SLA breach, budget hard stop, **integrity suspicion** and line-stop. The third is
unusual — most systems escalate on availability and cost. `investigating-integrity-concerns`
exists because a suspected fabrication or a corrupted evidence chain needs a human
faster than an outage does.

### Quiet hours and the `CRITICAL` pierce are a matched pair (T04)

Quiet hours without a pierce rule is a nightly outage window nobody agreed to. A
pierce rule without quiet hours is alert fatigue. Both, or neither works.

### Coalescing is what keeps the chain usable (T05)

The same event escalating fifty times is one incident and fifty interruptions.
Coalescing repeats — while still promoting on non-acknowledgement — is the
difference between a chain people answer and one they mute.

### The chain must terminate somewhere real

WP-003 and WP-118 both raise it: an escalation chain that loops back to its origin
has not escalated. In a solo laboratory this is often unsatisfiable, and the honest
outcome is ADR-001's — declare the gap with a residual-risk owner and an expiry.

### Nothing sends today

`AGENTS.md` §5: notification channels are specified, nothing connected, nothing
sends. Every escalation in this package is currently a design.

## Out of scope

- The content of the escalated decision (the relevant gate package owns that)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/wp_131_notification_broker.md) | — |
| [WP-132 — Channel Registry and Data-Class Ceiling](../13_TOOLING_INTEGRATION/wp_132_channel_registry_data_class_ceiling.md) | — |
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |

### Full prerequisite closure

**40 of 141 packages (28%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` |
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-131` |
| 25 | `WP-132` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-140`
- **Transitively reachable:** **1 of 141 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **26** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | SRE Lead |
| Independent verifier | Assurance Lead |
| Gates touched | `G0–G10` |
| Controls | `CTL-GOV-03` · `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |
| [ACC-43 — Escalation Timeout and Dead-Man's Switch](../12_ACCEPTANCE_SCENARIOS/acc_43_escalation_and_dead_mans_switch.md) | Critical | The request expires closed, the gate remains blocked, the dead-man's switch fires, and at no point is the absence of a response treated as consent. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-132, WP-004 (Human decision SLA)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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
- **SRE Lead** carries the acceptance decision; **Assurance Lead** must verify independently of whoever implements.
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

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-134-T01 | Define the escalation chain and the per-step SLAs | Chain registry |
| WP-134-T02 | Build the trigger → severity → channel matrix | Matrix + a test per row |
| WP-134-T03 | Acknowledgement mechanism and promotion of unacknowledged escalations | An unacknowledged escalation reaches the next step |
| WP-134-T04 | Quiet-hours policy and the `CRITICAL` pierce rule | A `CRITICAL` is delivered during quiet hours |
| WP-134-T05 | Noise control: repeats for the same event are coalesced | A repeated escalation is not duplicated |
| WP-134-T06 | Escalation telemetry (response time, ack rate, false positives) | Measurements flow to Metascience |

## Mandatory deliverables

- The escalation chain and SLA registry
- The trigger → severity → channel matrix
- The acknowledgement mechanism
- The quiet-hours policy
- Escalation telemetry

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-134_escalation_and_paging.tests.md`](wp_134_escalation_and_paging.tests.md).

- **No auto-approve:** when the SLA expires, state does not advance on its own (negative test)
- **Ack chain:** an unacknowledged escalation reaches the next step after N minutes
- **`CRITICAL` pierce:** a `CRITICAL` notification is not suppressed during quiet hours
- **Coalescing:** 10 triggers for the same event → 1 notification plus a counter

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-134_escalation_and_paging.acceptance.md`](wp_134_escalation_and_paging.acceptance.md), together with what this package still cannot establish.

- [ ] After an SLA breach, no gate advances by itself
- [ ] Every unacknowledged escalation is promoted; none is lost
- [ ] `CRITICAL` is never suppressed during quiet hours
- [ ] The false-positive rate is measured and thresholds are tuned from that measurement
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- Escalation fatigue is more dangerous than the escalation itself; the false-positive rate is monitored
- Turning a threshold off is forbidden; a threshold is tuned **by measurement**
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

If the escalation channel is disabled, the workflow **pauses** — it does not
proceed silently. This behaviour is non-waivable.

## Handoff into downstream packages

WP-135 binds the routing of decision-pending events to this chain.
