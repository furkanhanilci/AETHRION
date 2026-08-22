# WP-133 — Outbound Notification and Periodic Digest

## Package card

| Field | Value |
|---|---|
| Work package | `WP-133` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **S** — small; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Metascience Lead |
| Hard dependencies | WP-131, WP-132 |
| Related gates | G10 |
| Related controls | CTL-OBS-01 |
| Related acceptance scenarios | ACC-41 |
| Related skill | `notifying-humans`, `publishing-digests` |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Operational notifications and periodic summaries are published. A digest is a
**read-only derivative**: it carries no decision and changes no state.

Cadence:

| Frequency | Content | Audience |
|---|---|---|
| Daily | Open decisions, SLA risk, yesterday's runs, budget, attention-budget usage | Decision Owner |
| Weekly | Portfolio, gate flow, blocked work, open findings | All roles |
| **Monthly** | **Metascience scorecard**: calibration, agreement, gate yield, control FP/FN, claim survival | Assurance + Metascience |
| Quarterly | Cost, model requalification, incident analysis | FinOps + Platform |

> The monthly metascience summary is the laboratory's own report card. If it
> looks bad, it is not hidden — it appears at the **top** of the digest, not in
> an appendix.

## Out of scope

- The metascience measurements themselves (separate workstream)
- Decision authorisation (WP-135)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-132
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-133-T01 | Define the notification types and their templates | Template registry |
| WP-133-T02 | Establish the urgency → channel mapping | Mapping table + test |
| WP-133-T03 | Build the daily and weekly digest generators | Evidence that generation changes no state |
| WP-133-T04 | Build the monthly metascience digest | `UNCALIBRATED` fields are never rendered as numbers |
| WP-133-T05 | Enforce that every digest source is read-only | A write attempt is rejected in test |

## Mandatory deliverables

- The notification template registry
- The urgency → channel mapping
- Daily, weekly, monthly and quarterly digest generators
- The read-only source guarantee

## Test and verification plan

- **No side effects:** the canonical state hash is identical before and after digest generation
- **Calibration honesty:** a dimension with insufficient data renders as `UNCALIBRATED`
- **Channel mapping:** each urgency level routes to the correct channel
- With empty data, partial data or an error, generation marks the missing field instead of crashing

## Acceptance criteria

- [ ] Digest generation modifies no canonical record (hash evidence)
- [ ] `UNCALIBRATED` fields are not displayed as numbers
- [ ] Bad metrics appear at the top of the summary, not in an appendix
- [ ] The daily summary shows attention-budget usage
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- Digest fatigue: a summary that is too frequent or too long stops being read; open rate is monitored
- If digest generation ever changes state, that is a Critical finding
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

Digest publication is stopped; the source data is unaffected.

## Handoff into downstream packages

WP-134 reuses the same channel mapping for escalation.
