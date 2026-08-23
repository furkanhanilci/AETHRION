---
title: "WP-020 — Schema Registry, Compatibility and Contract SDK"
aliases:
  - "WP-020"
  - "WP-020 — Schema Registry, Compatibility and Contract SDK"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "All canonical contracts are published in a single versioned registry; producer/consumer compatibility and the shared identity and validation SDKs are enforced by CI rather than by review discipline."
source: "planning/commissioning/02_CONTRACTS/WP-020_schema_registry_sdk.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-020 — Schema Registry, Compatibility and Contract SDK

## Package card

| Field | Value |
|---|---|
| Work package | `WP-020` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Architecture Lead |
| Independent verifier | Consumer Service Owners |
| Hard dependencies | WP-011, WP-013, WP-014, WP-015, WP-016, WP-017, WP-018, WP-019 |
| Related gates | Platform |
| Related controls | CTL-OPS-01, CTL-SUP-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **LinkML** — the contract surface is generated from one model rather than hand-written

Generate JSON Schema, Pydantic, JSON-LD, SHACL and SQL DDL from a single LinkML model. This package's failure mode is contracts defined three times in three shapes, which is how the bridge and the contract core came to disagree about digest format.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_020_schema_registry_sdk.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_020_schema_registry_sdk.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

All canonical contracts are published in a single versioned registry; producer/consumer compatibility and the shared identity and validation SDKs are enforced by CI rather than by review discipline.


## Analysis
### What this package actually decides

That compatibility is a build failure rather than a review comment. The purpose
sentence names the mechanism: *enforced by CI rather than by review discipline.*

Everything in W1 produces a contract. This package is what makes those contracts
binding — and until it exists, every contract in the workstream is a document that
a producer and a consumer have separately agreed to interpret.

### The state today, stated plainly

`schemas/` in this repository contains **one file, a README**, and that README is
honest about it:

> ⚠️ **Currently empty.** The contract core in `src/airl_framework/` exists as
> in-process Python classes with no JSON Schema representation and no CI
> enforcement. It also has **no production consumer** — see finding **H4**.
> Until these schemas exist and are enforced in CI, WP-020 cannot reach
> `TECH_COMPLETE`, let alone `ACCEPTED`.

And `src/airl_framework/contracts.py`'s `SchemaRegistry` is an in-process `dict`
that refuses redefinition but *validates nothing against JSON Schema*. The rule
the module states about itself is the rule this package must satisfy: **a contract
with no consumer is dead code — bind it or delete it.**

### The dependency that makes this package structurally blocked

WP-020's acceptance requires CI. CI is **WP-024**, and its absence is finding
**H5**. `deploy/bvc-01-verify.yml` is written and has never run — a temporary
control with an owner and an expiry, and `deploy/README.md` states explicitly that
it does **not** close H5.

So this package cannot reach `ACCEPTED` before WP-024 does, and its own honest
readiness statement has to say so rather than letting the dependency surface at
verification time.

### The per-context format choice (T02) is a real decision, not a preference

JSON Schema where a human reads and writes the payload and evolution is frequent;
Protobuf where the wire cost matters and the consumer set is closed. Choosing one
globally optimises the wrong thing in half the contexts. What must be global is
the **registry**, the compatibility rule and the fixture harness — not the encoding.

### The semantic linter is the part that earns its keep (T03)

A compatibility checker catches structural breaks: removed fields, changed types.
It cannot catch the change that keeps the shape and inverts the meaning — a field
renamed from `excluded` to `included`, an enum value repurposed, a unit changed
from seconds to milliseconds. Those pass every structural check and break every
consumer. The semantic linter is a set of rules about **meaning-bearing
conventions**, and it is what makes the registry more than a type server.

### Deprecation needs a process, not a flag (T06)

A deprecated schema that nothing forces off is a schema in production with a
warning attached. The process needs a consumer inventory, a migration window and
a hard cutoff — and the registry has to be able to answer *who still consumes v1*,
which means consumer registration is part of publishing.

### Baseline v1.3.0 — new records, and the authority typing that keeps them honest

The contract surface gains the records this baseline's capabilities need, and
one field that matters more than any of them.

**New canonical records:** `AgentCohortRecord`, `CognitiveDiversityProfile`,
`CommunicationEdgePolicy`, `BlackboardEntry`, `TypedAgentMessage`,
`CommunicationUtilityRecord`, `ContextProjectionRecord`,
`MemoryInterventionRecord`, `ResearchBudgetContract`, `TokenLedgerEntry`,
`SpecificationConformanceRecord`, `HumanPreliminaryAssessment`, `DecisionDelta`,
`ModelExecutionFingerprint`, `BenchmarkRunPolicy`, `ContaminationFinding`,
`UpstreamAssimilationRecord`.

**Explicit authority typing.** Every record carries what it may never become. The
three conversions this baseline forbids are all of the same kind, and each has
already been attempted somewhere in the field:

| Forbidden conversion | Why it is tempting |
|---|---|
| A blackboard entry into evidence | It is where the interesting sentences appear |
| A communication or search utility score into a claim confidence | It is a number, and it correlates with something |
| An event payload into gate authority | It is the fastest path and it usually works |

The rule that makes them checkable rather than remembered: **events, blackboard
entries and derived read models cannot masquerade as canonical scientific
state**, and the schema is where that is enforced.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |

### Full prerequisite closure

**19 of 160 packages (12%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 21 — `WP-021` · `WP-022` · `WP-024` · `WP-025` · `WP-032` · `WP-039` · `WP-041` · `WP-042` · `WP-043` · `WP-046` · `WP-047` · `WP-049` · `WP-056` · `WP-061` · `WP-075` · `WP-087` · `WP-091` · `WP-096` · `WP-097` · `WP-109` · `WP-143`
- **Transitively reachable:** **139 of 160 packages (87%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **14** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Platform Architecture Lead |
| Independent verifier | Consumer Service Owners |
| Gates touched | `Platform` |
| Controls | `CTL-OPS-01` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `CandidateWorkspace` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionPackage` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ClaimConsistencyReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |

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
- **Platform Architecture Lead** carries the acceptance decision; **Consumer Service Owners** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `CMP-026` — LinkML | `DEPENDENCY` | Code and schema generation. | The single contract model from which JSON Schema, Pydantic, JSON-LD, SHACL and SQL DDL are generated. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `CMP-026` | A generator produces representations of a model; it never decides the model. A generated artifact that disagrees with the model is a defect in the model or the generator, never a third opinion. | Hand-written parallel definitions of a contract that the model already generates. |

### Where a plain row would mislead

- **`CMP-026`** — This attacks a real debt: contracts currently risk being defined three times in three shapes, which is how the bridge and the contract core came to disagree about digests — finding H4.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`CMP-026` — LinkML** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 2 obligations open across 1 of 1 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-020-T01 | Set up the schema repository and its CODEOWNERS ownership | Implementation owner | Commit / configuration / record reference |
| WP-020-T02 | Apply the JSON Schema versus Protobuf choice per bounded context | Implementation owner | Commit / configuration / record reference |
| WP-020-T03 | Write the compatibility checker and the semantic linter | Implementation owner | Commit / configuration / record reference |
| WP-020-T04 | Generate the ID, correlation, policy and artifact helper SDKs | Implementation owner | Commit / configuration / record reference |
| WP-020-T05 | Publish the fixture set and the contract-test harness | Implementation owner | Commit / configuration / record reference |
| WP-020-T06 | Define the deprecation and migration process | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Schema Registry v1`
- `Generated SDKs`
- `Compatibility CI`
- `Contract fixture catalog`
- `Deprecation policy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-020_schema_registry_sdk.tests.md`](wp_020_schema_registry_sdk.tests.md).

- Validate every schema against its fixtures
- A negative CI run on a deliberate breaking change
- Old-consumer/new-producer and new-consumer/old-producer contract tests
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-020_schema_registry_sdk.acceptance.md`](wp_020_schema_registry_sdk.acceptance.md), together with what this package still cannot establish.

- [ ] No canonical schema exists outside the registry.
- [ ] A breaking change cannot merge without a major version and an adapter.
- [ ] The generated SDKs produce identical semantics across target languages.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A faulty schema release is not yanked; a new patch version is published and the registry pointer returns to the last verified bundle.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
