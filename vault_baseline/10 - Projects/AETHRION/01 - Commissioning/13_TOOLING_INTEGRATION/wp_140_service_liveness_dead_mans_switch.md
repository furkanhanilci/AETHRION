---
title: "WP-140 — Service Liveness Monitoring and Dead-Man's Switch"
aliases:
  - "WP-140"
  - "WP-140 — Service Liveness Monitoring and Dead-Man's Switch"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A mechanism is built that notices when periodic work is not running."
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-140_service_liveness_dead_mans_switch.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/s
  - aethrion/gate/platform
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-140 — Service Liveness Monitoring and Dead-Man's Switch

## Package card

| Field | Value |
|---|---|
| Work package | `WP-140` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **S** — small; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Metascience Lead |
| Hard dependencies | WP-101 (Service SLO), WP-131, WP-134 |
| Related gates | Platform, G10 |
| Related controls | CTL-OBS-01 |
| Related acceptance scenarios | ACC-43 |
| Related skill | `escalating-and-paging` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_140_service_liveness_dead_mans_switch.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_140_service_liveness_dead_mans_switch.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A mechanism is built that notices when periodic work **is not running**.

Silent death is the most dangerous failure mode in this architecture: when a
feed, a timer or a sync stops, it produces no error — nothing simply happens.
The **H1/H2** findings in the audit report (silently partial sync, a deleted
source lingering as a ghost) belong to this class.

**Dead-man's switch pattern:** every periodic job emits an "I am still alive"
signal when it completes successfully. If the signal does not arrive within the
expected window, **an alarm is raised** — even though the job itself never
reported an error.

Jobs to cover: the Zotero sync timer, G10 feed scans, calibration runs, digest
generators, control injection, and backup jobs.


## Analysis
### What this package actually decides

That silence is detected. The purpose sentence names the failure that no other
control in the programme catches: *a mechanism that notices when periodic work **is
not running**.*

Every monitoring system watches for errors. `PR-20` — *periodic work fails silently*
— is the case where nothing errors because nothing ran.

### This is the failure mode the whole system is most exposed to

Count the scheduled things: the G10 impact scans, the status sweeps, the control
effectiveness tests, the calibration runs, the drift analysis, the digests, the
chain verification, the drills. Each is a control whose absence looks exactly like a
clean result.

A retraction sweep that stopped running six months ago reports no retractions, and
so does one that runs and finds none.

### The heartbeat is per job, and the alarm is on absence (T02, T03)

Not on failure — on **absence**. The job emits a success signal; the monitor alarms
when no signal arrives within the expected interval. The monitor must be
**self-hosted and independent**, because a monitor that shares infrastructure with
the jobs it watches goes silent with them.

### `SUCCEEDED` versus `PARTIAL` is the distinction the running system already needs (T04)

`src/airl_bridge/zotero.py` documents the exact failure: beyond 100 sources the sync
becomes *silently partial — the run is still recorded as `SUCCEEDED`*. That is
finding **H1**, and it is this package's rule in miniature: a job that did half its
work must not report the same status as one that did all of it.

### The escalation binding (T05)

An alarm that reaches nobody is the same as no alarm. This binds to WP-134's chain,
which promotes on non-acknowledgement.

## Out of scope

- The internal correctness of the job itself (owned by the relevant package)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md) | `Service Catalog` · `SLO catalog` · `Error-budget policy` · `Alert-runbook link checker` |
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/wp_131_notification_broker.md) | — |
| [WP-134 — Escalation and Paging](../13_TOOLING_INTEGRATION/wp_134_escalation_and_paging.md) | — |

### Full prerequisite closure

**64 of 141 packages (45%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-054` · `WP-055` · `WP-131` |
| 25 | `WP-056` · `WP-132` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-134` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |
| 30 | `WP-096` |
| 31 | `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-098` |
| 33 | `WP-101` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **34** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | SRE Lead |
| Independent verifier | Metascience Lead |
| Gates touched | `Platform` · `G10` |
| Controls | `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-43 — Escalation Timeout and Dead-Man's Switch](../12_ACCEPTANCE_SCENARIOS/acc_43_escalation_and_dead_mans_switch.md) | Critical | The request expires closed, the gate remains blocked, the dead-man's switch fires, and at no point is the absence of a response treated as consent. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-101 (Service SLO), WP-131, WP-134
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Service Catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `SLO catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Error-budget policy` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Alert-runbook link checker` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Ownership dashboard` | `WP-101` | `python3 scripts/progress.py show WP-101` |

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
- **SRE Lead** carries the acceptance decision; **Metascience Lead** must verify independently of whoever implements.
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
| WP-140-T01 | Inventory of periodic jobs and their expected intervals | Inventory file |
| WP-140-T02 | Emit a success signal (heartbeat) for every job | Signal records |
| WP-140-T03 | Alarm when no signal arrives (self-hosted monitor) | Test: stop the job → alarm arrives |
| WP-140-T04 | Distinguish partial success: `SUCCEEDED` vs `PARTIAL` | A partial sync is never counted as `SUCCEEDED` |
| WP-140-T05 | Bind alarm escalation to the WP-134 chain | An unacknowledged alarm is promoted |
| WP-140-T06 | Liveness dashboard with last-run times | The last success is visible for every job |

## Mandatory deliverables

- The periodic job inventory
- Heartbeat emission and the monitor (e.g. self-hosted Uptime Kuma / Healthchecks)
- The partial-success distinction
- The liveness dashboard

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-140_service_liveness_dead_mans_switch.tests.md`](wp_140_service_liveness_dead_mans_switch.tests.md).

- **Silent death:** stop the job → an alarm is raised within the expected window
- **Partial success:** a run that processed fewer records than expected is marked `PARTIAL`, not `SUCCEEDED`
- **The monitor itself:** if the monitor stops, that is also detected (meta-heartbeat)
- **Alarm escalation:** an unacknowledged alarm is promoted to the next step

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-140_service_liveness_dead_mans_switch.acceptance.md`](wp_140_service_liveness_dead_mans_switch.acceptance.md), together with what this package still cannot establish.

- [ ] Every periodic job has a defined, monitored expected interval
- [ ] When a job stops silently, an alarm is raised **within hours**
- [ ] Partial success cannot be reported as `SUCCEEDED`
- [ ] The monitor's own death is detected
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- The monitor must not be a single point of failure; the meta-heartbeat is mandatory
- Thresholds that are too tight produce noise, too loose produce late detection — they are tuned by measurement
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

If monitoring is disabled, the periodic jobs keep running but silent death
becomes invisible again. That is a **High** risk and requires an explicit waiver.

## Handoff into downstream packages

WP-137 binds feed liveness and WP-134 binds alarm escalation to this mechanism.
The metascience plane uses liveness data in its gate-yield measurement.
