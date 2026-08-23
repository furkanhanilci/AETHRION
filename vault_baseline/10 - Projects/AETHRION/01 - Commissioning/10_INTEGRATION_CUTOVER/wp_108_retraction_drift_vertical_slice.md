---
title: "WP-108 — Retraction, Drift and Supersession Vertical Slice"
aliases:
  - "WP-108"
  - "WP-108 — Retraction, Drift and Supersession Vertical Slice"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Source retractions and corrections, model snapshot revocations, dataset and policy changes and incidents route the affected claims, runs, publications and tasks to the right owner and re-evaluation path."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-108 — Retraction, Drift and Supersession Vertical Slice

## Package card

| Field | Value |
|---|---|
| Work package | `WP-108` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Assurance / Eval Office / Decision Owner |
| Hard dependencies | WP-037, WP-042, WP-044, WP-063, WP-075, WP-077, WP-090, WP-095, WP-106 |
| Related gates | G10 |
| Related controls | CTL-LIT-02, CTL-MOD-02 |
| Related acceptance scenarios | ACC-04, ACC-31, ACC-36 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_108_retraction_drift_vertical_slice.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_108_retraction_drift_vertical_slice.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Source retractions and corrections, model snapshot revocations, dataset and policy changes and incidents route the affected claims, runs, publications and tasks to the right owner and re-evaluation path.


## Analysis
### What this package actually decides

Whether the impact machinery finds everything it should — measured against an
**expected set**, not against whether it found something.

T03 is the sub-task that makes this a test rather than a demonstration: compare the
computed affected set against the expected set. Without an expected set, an impact
scan that returns three claims when nine are affected reports success.

### Six trigger classes, because they arrive by six paths (T01)

Retraction, correction, model snapshot revocation, dataset change, policy change,
incident. Each enters through a different adapter, and a system tested only on
retraction has tested the one everybody designs for.

Model revocation is the least obvious: `00_PROGRAM/01` invariant 7 requires a model
snapshot change to produce requalification **and an explicit task impact
assessment**, which means open tasks — not only completed claims.

### Idempotency on duplicate triggers (T06)

The same retraction arriving twice — from a scheduled sweep and from a webhook —
must not open two cases. This is WP-039's consumer discipline reaching G10, and
without it the queue fills with duplicates and gets ignored.

### False positives are the failure that kills the feed (T06)

A monitoring feed with a high false-positive rate is a feed nobody reads. Every
dismissal reaches a terminal state with a reason, and a dismissed case **does not
reopen on the next scan** — otherwise the dismissal is a snooze button.

### The DOI-less fraction bounds what this package can claim

15 of 33 registry sources carry a DOI. The retraction path resolves by DOI, so 18
sources are outside it entirely. The expected set must be computed over what is
**monitorable**, and the report must state the fraction — otherwise a complete-
looking impact scan is silently partial.

### Baseline v1.3.0 — the slices exercise the cohort, and the regression injects faults

The vertical slices and the cutover path grow to cover what this baseline adds,
and one package changes character.

**WP-107 becomes the engineering completion slice.** Requirement and
specification → worktree → TDD → code review → CI → supply-chain attestation →
signed artifact → **eligibility to produce scientific evidence**. That last arrow
is the junction between the two disciplines, and before this baseline nothing
proved it end to end.

**The other slices exercise the collaboration plane**: a compiled cohort, sealed
initial positions, typed delta exchange over a sparse topology, an adaptive
assurance route, a fingerprinted reproduction and a firewalled benchmark run.

**The regression suite gains injections rather than cases.** Faulty agent,
malicious agent, split brain, duplicate and out-of-order events, communication
degradation under budget pressure, and benchmark contamination. These are
failures that are invisible in a healthy run and obvious only in a post-mortem,
which is why they are caused deliberately rather than waited for.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

9, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md) | `Capability Registry service` · `Profile state machine` · `Eligibility API` · `Expiry/revoke scheduler` |
| [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md) | `Qualification pipeline` · `Admission dossier` · `CapabilityProfile update` · `Regression schedule` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md) | `Publication builder` · `RO-Crate profile` · `Signed publication package` · `Release checklist` |
| [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md) | `Claim Explorer` · `Evidence preview` · `Provenance graph` · `Assessment/blocker panels` |
| [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/wp_106_vertical_slice_decision_publish_monitor.md) | `Decision/publish/monitor dossier` · `DecisionRecord` · `PublicationPackage` · `ImpactCase/Supersession` |

### Full prerequisite closure

**95 of 160 packages (59%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-073` · `WP-077` · `WP-078` |
| 34 | `WP-074` · `WP-079` · `WP-085` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-109` · `WP-110` · `WP-124`
- **Transitively reachable:** **25 of 160 packages (16%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **45** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Assurance / Eval Office / Decision Owner |
| Gates touched | `G10` |
| Controls | `CTL-LIT-02` · `CTL-MOD-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-36 — Model Snapshot Drift](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) | Critical | The profile moves to suspension or requalification, the router cache is invalidated and an `ImpactScan` opens for open tasks, runs and claims; there is no unsafe fallback. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/wp_106_vertical_slice_decision_publish_monitor.md)
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
| `ImpactScan workflow` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Schedule registry` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `ImpactCase service contract` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Supersession trigger` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Capability Registry service` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Profile state machine` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eligibility API` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Expiry/revoke scheduler` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Qualification pipeline` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Admission dossier` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `CapabilityProfile update` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Regression schedule` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Ejection procedure` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Fingerprint and abstention scope on qualification records` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Representation ingest service` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `License/status policy` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Status monitor` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Format locator metadata` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Retention mapping` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Publication builder` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `RO-Crate profile` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Signed publication package` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Release checklist` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Supersession record` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Publication compiler` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Assertion and value binding checks` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Claim Explorer` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Evidence preview` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Provenance graph` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Assessment/blocker panels` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Audit drill-down` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Decision/publish/monitor dossier` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `DecisionRecord` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `PublicationPackage` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `ImpactCase/Supersession` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `Audit export` | `WP-106` | `python3 scripts/progress.py show WP-106` |

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
- **Knowledge Monitoring Lead** carries the acceptance decision; **Assurance / Eval Office / Decision Owner** must verify independently of whoever implements.
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
| WP-108-T01 | Produce the retraction, correction, model, data, policy and incident fixtures | Implementation owner | Commit / configuration / record reference |
| WP-108-T02 | Run the schedule/event → `ImpactScan` and the graph query | Implementation owner | Commit / configuration / record reference |
| WP-108-T03 | Compare the computed affected claim/task/project/publication set against the expected set | Implementation owner | Commit / configuration / record reference |
| WP-108-T04 | Apply priority, SLA, owner and the provisional/challenged state | Implementation owner | Commit / configuration / record reference |
| WP-108-T05 | Perform re-review, reproduction, republication or a no-impact disposition | Implementation owner | Commit / configuration / record reference |
| WP-108-T06 | Test false-positive handling and duplicate-trigger idempotency | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Impact vertical dossier`
- `ImpactCase set`
- `Affected-object accuracy report`
- `Supersession/re-evaluation records`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-108_retraction_drift_vertical_slice.tests.md`](wp_108_retraction_drift_vertical_slice.tests.md).

- ACC-04, 31 and 36
- A duplicate trigger producing one case
- A false-positive disposition
- A model revocation against an open task
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-108_retraction_drift_vertical_slice.acceptance.md`](wp_108_retraction_drift_vertical_slice.acceptance.md), together with what this package still cannot establish.

- [ ] Affected-set recall is 100% for the critical fixtures.
- [ ] No existing object is silently mutated.
- [ ] Every material impact carries a named owner and a deadline.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

A faulty case disposition is superseded; the trigger and the previous status remain in the audit history.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
