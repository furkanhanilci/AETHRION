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

## Out of scope

- The internal correctness of the job itself (owned by the relevant package)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-101 (Service SLO), WP-131, WP-134
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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

- **Silent death:** stop the job → an alarm is raised within the expected window
- **Partial success:** a run that processed fewer records than expected is marked `PARTIAL`, not `SUCCEEDED`
- **The monitor itself:** if the monitor stops, that is also detected (meta-heartbeat)
- **Alarm escalation:** an unacknowledged alarm is promoted to the next step

## Acceptance criteria

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
