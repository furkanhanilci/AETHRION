# WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows

## Package card

| Field | Value |
|---|---|
| Work package | `WP-037` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Assurance Lead / SRE |
| Hard dependencies | WP-008, WP-015, WP-017, WP-018, WP-031, WP-032 |
| Related gates | G10 |
| Related controls | CTL-LIT-02, CTL-MOD-02 |
| Related acceptance scenarios | ACC-04, ACC-31, ACC-36 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-037_g10_impactscan.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-037_g10_impactscan.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Retraction, source correction, model/data/policy drift and incident signals launch short-lived `ImpactScan` workflows on a periodic Schedule — never one long-lived monitoring workflow.


## Analysis
### What this package actually decides

That `VERIFIED` is not permanent. `AGENTS.md` §4.1 states the property the whole
evidence chain exists for: it is **traversable in both directions**, and the loop
**closes**. G10 is the closing.

### The architectural decision is short-lived scans, not a long-lived watcher

`planning/commissioning/README.md` §2 makes it binding: *G10 is not a single
workflow living for years; a Temporal Schedule launches short-lived `ImpactScan`
runs.* A workflow open for years accumulates history, survives no deployment
cleanly, and fails silently when it stops — which is `PR-20`, *periodic work fails
silently*.

Short runs on a schedule fail loudly, because a missing run is observable.

### What already exists, and the gap it names

`scripts/monitor_sources.py` runs, sweeps Crossref for retractions, corrections
and expressions of concern, and **carries a positive control that fails the check
if it stays silent**. Its measurement file states its own limit:

> `claim_impact_analysis: "not implemented — no Claim Ledger exists"`

So the trigger half of G10 is real today and the impact half is not. This package
is where the sweep gets something to write into.

### Impact is a graph query, not a search (T03)

Given a retracted source, the affected set is every claim whose evidence spans
reach it, plus every claim derived from those. That is WP-030's projection doing
exactly what it was built for — and it is the reason the graph has to traverse
backwards.

A system that answers this by searching text will miss the derived claims, which
are the ones that matter.

### False-positive disposition is what keeps the scan usable (T06)

A monitoring feed with no disposition path floods the queue, and a flooded queue
is ignored. Every `ImpactCase` reaches a terminal state — the same rule
`00_PROGRAM/06` applies to findings — and a dismissed case records why.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md) | `Gate Policy v1` · `Gate artifact matrix` · `Reopen/return transition table` · `Gate owner matrix` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md) | `Temporal platform` · `Namespace/queue catalog` · `Worker identity policy` · `HA/failover runbook` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |

### Full prerequisite closure

**30 of 141 packages (21%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 17 | `WP-024` · `WP-028` |
| 18 | `WP-027` |
| 19 | `WP-031` |
| 20 | `WP-032` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-040` · `WP-063` · `WP-092` · `WP-106` · `WP-108` · `WP-128` · `WP-137`
- **Transitively reachable:** **53 of 141 packages (38%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **21** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Assurance Lead / SRE |
| Gates touched | `G10` |
| Controls | `CTL-LIT-02` · `CTL-MOD-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/ACC-31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-36 — Model Snapshot Drift](../12_ACCEPTANCE_SCENARIOS/ACC-36_model_snapshot_drift.md) | Critical | The profile moves to suspension or requalification, the router cache is invalidated and an `ImpactScan` opens for open tasks, runs and claims; there is no unsafe fallback. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md)
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
| `Gate Policy v1` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate artifact matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Reopen/return transition table` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate owner matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Temporal platform` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Namespace/queue catalog` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Worker identity policy` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `HA/failover runbook` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `SLO dashboard` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |

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
- **Knowledge Monitoring Lead** carries the acceptance decision; **Assurance Lead / SRE** must verify independently of whoever implements.
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
| WP-037-T01 | Establish the `MonitoringPolicy` and schedule registry | Implementation owner | Commit / configuration / record reference |
| WP-037-T02 | Write the source, model, data, policy and incident trigger adapters | Implementation owner | Commit / configuration / record reference |
| WP-037-T03 | Produce the impact graph query and the affected claim/project list | Implementation owner | Commit / configuration / record reference |
| WP-037-T04 | Assign `ImpactCase` priority, SLA and owner | Implementation owner | Commit / configuration / record reference |
| WP-037-T05 | Dispatch the supersession and re-evaluation workflows | Implementation owner | Commit / configuration / record reference |
| WP-037-T06 | Add false-positive disposition and audit | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ImpactScan workflow`
- `Schedule registry`
- `ImpactCase service contract`
- `Supersession trigger`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-037_g10_impactscan.tests.md`](WP-037_g10_impactscan.tests.md).

- A retraction → affected-claim test
- A model revocation → open-task test
- Schedule retry and idempotency
- A negative test proving old claims are never silently mutated
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-037_g10_impactscan.acceptance.md`](WP-037_g10_impactscan.acceptance.md), together with what this package still cannot establish.

- [ ] No single long-lived monitoring workflow exists.
- [ ] Every scan is bounded and idempotent.
- [ ] Affected claim owners receive a queue item and a status change.
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

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A faulty impact result is closed with a new disposition; the source and claim history is never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
