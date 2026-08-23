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

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-133_outbound_notification_and_digest.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-133_outbound_notification_and_digest.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

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


## Analysis
### What this package actually decides

That a digest is a **read-only derivative**. The purpose sentence states the rule
and it is the one that keeps a summary from becoming an authority: *a digest carries
no decision and changes no state.*

This matters because a digest is the artifact a busy person reads instead of the
system. If it can carry a decision, it becomes a decision surface with none of
WP-093's controls — no frozen snapshot, no evidence delta, no rationale, no MFA.

### Urgency → channel mapping is where alert fatigue is designed in or out (T02)

Every routine notification sent at the same urgency as a page trains the recipient
to ignore both. The mapping is the design decision, and it should be conservative:
most things are a digest entry, not a message.

### The monthly metascience digest is the unusual one (T04)

`00_PROGRAM/08`'s anti-metrics and `PR-16`–`PR-18` produce numbers nobody will look
for: reviewer agreement, decision-time distribution, G10 reversal rate, the lab's
own error indicators. A recurring digest is what puts them in front of someone
without requiring them to ask.

`publishing-digests` is the skill.

### Read-only enforcement has to be structural (T05)

Not a convention. The digest generator reads projections and canonical records and
**has no write path** — which is checkable, unlike a promise.

### A digest must state its own freshness

It is assembled from projections that lag. A digest that does not say when its data
was current invites a decision against stale numbers, which is the same failure
WP-091's freshness indicator prevents on the cockpit.

### Baseline v1.3.0 — the messaging layer inherits the same two refusals

Nothing changes about what these packages own. Two rules from this baseline
apply to all of them, and both are restatements of things that erode first at the
edges of a system:

**No message and no timeout becomes authority.** An inbound message is never an
instruction; a notification is never an authorisation; an expired SLA escalates
and pages and never approves.

**Alignment with the new paths.** The capability gate governs any action an
inbound message might trigger. Evidence-delta priority drives the decision
queue. The human preliminary flow means a notification announcing a decision may
not carry the recommendation. Every intervention writes an immutable audit
record atomically with the change it describes.

## Out of scope

- The metascience measurements themselves (separate workstream)
- Decision authorisation (WP-135)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/WP-131_notification_broker.md) | — |
| [WP-132 — Channel Registry and Data-Class Ceiling](../13_TOOLING_INTEGRATION/WP-132_channel_registry_data_class_ceiling.md) | — |

### Full prerequisite closure

**40 of 160 packages (25%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **26** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | SRE Lead |
| Independent verifier | Metascience Lead |
| Gates touched | `G10` |
| Controls | `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling](../12_ACCEPTANCE_SCENARIOS/ACC-41_notification_data_class_ceiling.md) | Critical | The payload is refused or degraded to a signed reference with no D2 content; the agent never touches the channel credential; the decision and its rule are audited. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-132
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-133_outbound_notification_and_digest.tests.md`](WP-133_outbound_notification_and_digest.tests.md).

- **No side effects:** the canonical state hash is identical before and after digest generation
- **Calibration honesty:** a dimension with insufficient data renders as `UNCALIBRATED`
- **Channel mapping:** each urgency level routes to the correct channel
- With empty data, partial data or an error, generation marks the missing field instead of crashing

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-133_outbound_notification_and_digest.acceptance.md`](WP-133_outbound_notification_and_digest.acceptance.md), together with what this package still cannot establish.

- [ ] Digest generation modifies no canonical record (hash evidence)
- [ ] `UNCALIBRATED` fields are not displayed as numbers
- [ ] Bad metrics appear at the top of the summary, not in an appendix
- [ ] The daily summary shows attention-budget usage
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- Digest fatigue: a summary that is too frequent or too long stops being read; open rate is monitored
- If digest generation ever changes state, that is a Critical finding
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

Digest publication is stopped; the source data is unaffected.

## Handoff into downstream packages

WP-134 reuses the same channel mapping for escalation.
