---
title: "WP-028 — NATS JetStream and Transactional Outbox Foundation"
aliases:
  - "WP-028"
  - "WP-028 — NATS JetStream and Transactional Outbox Foundation"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "The at-least-once event backbone is established with an outbox that places the publish intent in the same transaction as the canonical database commit, plus an idempotent relay."
source: "planning/commissioning/03_FOUNDATION/WP-028_nats_jetstream_outbox.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-028 — NATS JetStream and Transactional Outbox Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-028` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Event Platform Lead |
| Independent verifier | SRE / Data Platform Lead |
| Hard dependencies | WP-015, WP-021, WP-025 |
| Related gates | Platform |
| Related controls | CTL-OPS-01, CTL-OBS-01 |
| Related acceptance scenarios | ACC-12, ACC-34 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_028_nats_jetstream_outbox.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_028_nats_jetstream_outbox.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The at-least-once event backbone is established with an outbox that places the publish intent in the same transaction as the canonical database commit, plus an idempotent relay.


## Analysis
### What this package actually decides

That a published event and a committed fact cannot disagree. The outbox is the
whole package: the publish intent is written **in the same transaction** as the
canonical commit, and a relay drains it. Everything else is configuration.

Without it there are exactly two failure modes and both happen: commit-then-crash
loses the event, and publish-then-fail-to-commit announces something that never
happened. The second is worse, because downstream consumers act on it.

### This is where `PR-07` is enforced in infrastructure

*Dual authority over event/state* — a NATS consumer changes gate state — is rated
critical, and WP-015 forbids it at the contract layer. This package is where the
subject ACLs make it impossible rather than forbidden: the consumer's workload
identity simply cannot write to the streams that Temporal owns.

A rule enforced only in a contract is enforced by whoever reads the contract.

### Idempotent relay, not exactly-once delivery (T03)

There is no exactly-once delivery over a network, and a package that claims it has
mis-stated its own guarantee. What exists is at-least-once delivery plus an
idempotency key, and the relay must be safe to run twice — including after a crash
midway through a batch.

`ACC-12` is the test that matters: a duplicate arrives, **exactly one** business
effect occurs.

### Replay and read-model rebuild are one mechanism with two uses (T05)

`00_PROGRAM/01` invariant 6 requires derived state to be rebuildable from
canonical records. WP-030 does the rebuilding; this package supplies the ordered,
retained stream that makes it possible — and `replay_mode` from WP-015 is what
keeps a rebuild from re-firing external side effects.

### DLQ is a queue with an owner, or it is a bin (T04)

`ACC-34` tests the repair path. A DLQ nobody is paged about accumulates poisoned
events, and the first anyone hears of it is a missing downstream record months
later.

### Baseline v1.3.0 — modular monolith first, and a projection that can be destroyed

The collaboration plane, the conformance checker and the release assurance work
land as **modules**, not as services. A logical plane is an ownership boundary;
turning each into a deployment unit before there is a consumer buys operational
cost and no assurance.

Two guarantees the foundation now owes:

**Every derived projection is destroyable.** The graph, the vector index and the
search index are rebuilt from canonical stores as a routine, tested operation —
ACC-119. A rebuild path that is an emergency procedure will not work on the day
it is needed.

**Release artifacts carry provenance.** SLSA provenance, Sigstore signatures, an
SBOM and its scan result, and the upstream register accounting for every adapted
file. `ADR-019`, delivered by WP-159 and admitted against by WP-024's CI.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |

### Full prerequisite closure

**22 of 160 packages (14%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 15 | `WP-021` |
| 16 | `WP-025` |

### What acceptance of this package releases

- **Directly unblocked:** 12 — `WP-030` · `WP-031` · `WP-039` · `WP-049` · `WP-061` · `WP-074` · `WP-075` · `WP-096` · `WP-099` · `WP-100` · `WP-101` · `WP-114`
- **Transitively reachable:** **121 of 160 packages (76%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **17** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Event Platform Lead |
| Independent verifier | SRE / Data Platform Lead |
| Gates touched | `Platform` |
| Controls | `CTL-OPS-01` · `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-12 — Duplicate Event Delivery](../12_ACCEPTANCE_SCENARIOS/acc_12_duplicate_event.md) | Critical | Exactly one business effect occurs, the duplicate is acknowledged and audited, and the side effect is not performed a second time. |
| [ACC-34 — DLQ Repair and Corrected Replay](../12_ACCEPTANCE_SCENARIOS/acc_34_dlq_repair.md) | High | No consumer loop forms; owner, diagnostics and audit are complete, the corrected event is processed exactly once and the original causation is preserved. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md)
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
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |

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
- **Event Platform Lead** carries the acceptance decision; **SRE / Data Platform Lead** must verify independently of whoever implements.
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
| WP-028-T01 | Set up the JetStream cluster, streams and retention | Implementation owner | Commit / configuration / record reference |
| WP-028-T02 | Bind subject ACLs and workload identity | Implementation owner | Commit / configuration / record reference |
| WP-028-T03 | Write the PostgreSQL outbox schema and the relay | Implementation owner | Commit / configuration / record reference |
| WP-028-T04 | Apply the durable-consumer, ACK and DLQ standard | Implementation owner | Commit / configuration / record reference |
| WP-028-T05 | Establish replay and read-model rebuild modes | Implementation owner | Commit / configuration / record reference |
| WP-028-T06 | Add schema-registry validation and telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `NATS cluster`
- `Outbox relay`
- `Consumer SDK`
- `DLQ/replay runbook`
- `Event dashboards`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-028_nats_jetstream_outbox.tests.md`](wp_028_nats_jetstream_outbox.tests.md).

- Duplicate delivery producing exactly one business effect
- Relay crash recovery after the commit
- Poison-event routing to DLQ and a corrected replay
- Canonical state preserved through a total NATS loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-028_nats_jetstream_outbox.acceptance.md`](wp_028_nats_jetstream_outbox.acceptance.md), together with what this package still cannot establish.

- [ ] An ACK is issued only after the business commit.
- [ ] Gate state is never changed directly by a NATS consumer.
- [ ] Outbox lag has an SLO and an alert.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

A relay or consumer rollback preserves offsets and the outbox; no side effect is enabled until a replay dry-run has verified the behaviour.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
