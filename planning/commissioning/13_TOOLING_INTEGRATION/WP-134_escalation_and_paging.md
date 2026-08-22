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
| Current status | `NOT_STARTED` |

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

## Out of scope

- The content of the escalated decision (the relevant gate package owns that)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-132, WP-004 (Human decision SLA)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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

- **No auto-approve:** when the SLA expires, state does not advance on its own (negative test)
- **Ack chain:** an unacknowledged escalation reaches the next step after N minutes
- **`CRITICAL` pierce:** a `CRITICAL` notification is not suppressed during quiet hours
- **Coalescing:** 10 triggers for the same event → 1 notification plus a counter

## Acceptance criteria

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
