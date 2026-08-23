# WP-063 — Source Representation, Licence and Status Monitoring

## Package card

| Field | Value |
|---|---|
| Work package | `WP-063` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Archivist / Safety / Citation Auditor |
| Hard dependencies | WP-014, WP-017, WP-026, WP-037, WP-050, WP-058, WP-061, WP-062 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-02, CTL-DAT-03 |
| Related acceptance scenarios | ACC-04 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-063_source_representation_status.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-063_source_representation_status.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

PDF, HTML, preprint, dataset documentation and correction/retraction representations are versioned with hash, format, licence, parser and availability; a status change triggers an `ImpactScan`.


## Analysis
### What this package actually decides

That a citation points at a **file**, not at a work. A `SourceRepresentation`
carries hash, format, licence, parser and availability — and it is what an evidence
span anchors to, because a page number without a file is not a locator (WP-018).

### The status feed is where the evidence chain closes (T04, T05)

Retraction, correction, expression of concern, preprint→published. Each is a fact
about the outside world that must reach every dependent claim, and
`00_PROGRAM/01`'s property is that the chain is **traversable in both directions**.

The running system already does the sweep. `scripts/monitor_sources.py` queries
Crossref, carries a known-retracted positive control, and **fails if the control
stays silent**. Its measurement file states the gap honestly:
`claim_impact_analysis: "not implemented — no Claim Ledger exists"`.

This package is what the sweep writes into.

### The DOI-less fraction is a real coverage limit and must be published

The current registry holds 33 sources, of which **18 have no DOI** — the
measurement file records the split. Crossref resolves by DOI, so those 18 are not
monitored at all. Any claim that G10 covers the literature base has to state that
fraction, because a monitor covering 45% reports clean for the same reason one
covering nothing would.

### Structural locator maps are format-specific and that is unavoidable (T02)

A PDF locator is page + bounding box; an HTML locator is a selector path; a dataset
locator is a row/column reference. WP-018's three-part anchor needs the middle part
to mean something per format, and a generic locator is a locator that resolves in
no format precisely.

### Unavailable representations are a retention decision, not an error (T06)

A URL rots. The question is what the system does with an evidence span anchored to
bytes it can no longer fetch — and the answer has to distinguish *we no longer have
it* from *it never said that*. The hash is what preserves the distinction.

### Baseline v1.3.0 — source status, retrieval budget and what survives a pruned context

Two additions and one guarantee.

**Material-delta detection for G10.** A citation-count change is not a material
event. A retraction, a major correction, strong contradictory evidence, a
reproduction failure or a dependency drift that invalidates a result is. The
distinction is what keeps G10 from becoming a notification nobody reads —
alert fatigue is a failure mode of a monitoring system, not a nuisance.

**Search and retrieval budget.** Literature retrieval draws on the same
`ResearchBudgetContract` as everything else, and its stopping rule stays
distinct from the communication stopping rule — the two answer different
questions and sharing a threshold would couple them wrongly.

**The guarantee:** source and literature records stay canonical **even when the
blackboard and the context projections are pruned**. A source that only exists in
an agent's context is not a source, and pruning must never be able to lose one.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md) | `Versioned connectors` · `Connector permission profiles` · `Connector contract tests` · `Compensation/reconciliation playbooks` |
| [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md) | `Content firewall` · `Parser workers` · `ContentSafetyRecord` · `Injection detector` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |

### Full prerequisite closure

**50 of 160 packages (31%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-037` · `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` |
| 28 | `WP-062` |

### What acceptance of this package releases

- **Directly unblocked:** 10 — `WP-068` · `WP-072` · `WP-076` · `WP-078` · `WP-079` · `WP-094` · `WP-103` · `WP-108` · `WP-125` · `WP-137`
- **Transitively reachable:** **63 of 160 packages (39%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **29** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Archivist / Safety / Citation Auditor |
| Gates touched | `G3` · `G10` |
| Controls | `CTL-LIT-02` · `CTL-DAT-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md)
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
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `ImpactScan workflow` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Schedule registry` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `ImpactCase service contract` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Supersession trigger` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Versioned connectors` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector permission profiles` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector contract tests` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Compensation/reconciliation playbooks` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Content firewall` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Parser workers` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `ContentSafetyRecord` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Injection detector` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Quarantine UI/API` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Capability gate for untrusted content` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Source Resolver service` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Match rules/features` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Conflict queue` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Known-item/dedup test corpus` | `WP-062` | `python3 scripts/progress.py show WP-062` |

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
- **Knowledge Lead** carries the acceptance decision; **Archivist / Safety / Citation Auditor** must verify independently of whoever implements.
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
| WP-063-T01 | Write representation ingest with hash, licence and access metadata | Implementation owner | Commit / configuration / record reference |
| WP-063-T02 | Produce the format-specific structural locator map | Implementation owner | Commit / configuration / record reference |
| WP-063-T03 | Establish the version, correction and preprint → published relationships | Implementation owner | Commit / configuration / record reference |
| WP-063-T04 | Bind the Crossref, Crossmark, retraction and status feed adapters | Implementation owner | Commit / configuration / record reference |
| WP-063-T05 | Add the periodic status Schedule and its event emission | Implementation owner | Commit / configuration / record reference |
| WP-063-T06 | Define behaviour for unavailable old representations and their retention | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Representation ingest service`
- `License/status policy`
- `Status monitor`
- `Format locator metadata`
- `Retention mapping`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-063_source_representation_status.tests.md`](WP-063_source_representation_status.tests.md).

- A new PDF never altering the previous bytes
- A retraction event raising an `ImpactCase`
- A licence denial falling back to hash-only retention
- Old-representation availability and re-anchoring
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-063_source_representation_status.acceptance.md`](WP-063_source_representation_status.acceptance.md), together with what this package still cannot establish.

- [ ] Evidence is not orphaned while the old immutable representation remains reachable.
- [ ] A status change never mutates a previously frozen manifest.
- [ ] Where the licence forbids storage, identity and hash are kept instead of bytes.
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

- Identity errors in sources propagate into every claim that cites them.
- A write into a shared library without a version precondition can silently destroy a human edit.
- A literature set that is not frozen cannot support a reproducible claim.

## Rollback / compensation

An incorrect status is superseded by a new status event; the effect of a retraction is never manually erased.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
