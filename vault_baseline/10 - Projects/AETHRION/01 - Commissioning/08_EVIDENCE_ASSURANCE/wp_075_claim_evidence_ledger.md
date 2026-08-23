---
title: "WP-075 — Canonical Claim/Evidence Ledger Service"
aliases:
  - "WP-075"
  - "WP-075 — Canonical Claim/Evidence Ledger Service"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Claim, evidence span, dependency, assessment, review link, decision and supersession records are held in an immutable, versioned canonical ledger."
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
---

# WP-075 — Canonical Claim/Evidence Ledger Service

## Package card

| Field | Value |
|---|---|
| Work package | `WP-075` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Data Architect / Assurance Lead |
| Hard dependencies | WP-018, WP-020, WP-025, WP-026, WP-028, WP-030, WP-055, WP-056, WP-061 |
| Related gates | G5–G10 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-04, ACC-08, ACC-30, ACC-31 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **AIRL-SEPIO profile** expressed in **LinkML**; **nanopub** as export only

SEPIO models assertions, evidence and provenance domain-agnostically and carries *challenges* as well as *supports*, which adversarial review needs. Nanopublication is the public export representation, not the operational ledger.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_075_claim_evidence_ledger.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_075_claim_evidence_ledger.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Claim, evidence span, dependency, assessment, review link, decision and supersession records are held in an immutable, versioned canonical ledger. This is the system's memory of what it believes and why.


## Analysis
### What this package actually decides

What the system believes, and why. The purpose sentence is the plainest in the
plan: *this is the system's memory of what it believes and why.* Every other
package produces something that eventually resolves to a record here.

### Immutable and versioned, because a claim's meaning must be stable (T02)

`00_PROGRAM/01` success invariant 1: every material claim links, **in a single
query**, to its source representation, evidence span, run, review and decision.
That query only works if the claim it names has not been edited underneath it.

So a claim is versioned, never mutated, and `challenge` and `supersede` are
first-class operations rather than status edits.

### The impact query is the reverse direction, and it is the harder one (T05)

Forward — *what supports this claim* — is a join anyone can write. Backward —
*given this retracted source, which claims are now unsupported* — has to traverse
evidence spans, then dependencies, then derived claims, transitively.

`AGENTS.md` §4.1 names both directions as the property that matters, and the
measurement file for the running G10 sweep records what is missing:
`claim_impact_analysis: "not implemented — no Claim Ledger exists"`.

This package is that ledger.

### Field-level RBAC and access logging (T04)

A claim record carries the assertion, the evidence, the reviewer verdicts and the
decision. Those have different audiences: a reviewer must not see the producer's
identity (WP-086), and an access log is what makes an unblinding detectable.

### The WORM export is what makes the ledger auditable by someone who does not
trust it (T06)

An immutable table in a database the operator controls is tamper-evident to
insiders. A WORM export is what an external auditor reads — and it is the same
gap `airl-interim-v0.1` declares about itself: tamper-evident, **not externally
witnessed**.

### Baseline v1.3.0 — the assurance layer stops using one word for two things

Three changes, and the first is a vocabulary correction with real consequences.

**"Mechanical verifier" is retired as a broad term.** It becomes V0 deterministic
· V1 computational · V2 qualified semantic · V3 human (`ADR-008`), and the class
is assigned by the verifier service from the procedure that actually ran — never
by the caller. The reason is that the gate rule *a mechanical check cannot be
overridden by a model* is correct for V0 and V1 and absurd at V2, where it says a
model's judgement cannot be overridden by a model.

**Assurance becomes routed** (`ADR-015`): by consequence and uncertainty rather
than uniformly, with a cascade to a stronger independent verifier or to a human,
and with `ABSTAIN` as a valid verdict that escalates. A route cannot be lowered
because the queue is long or the budget is tight.

**Three hard bindings** into the evidence and publication path:

- **Specification conformance** — the frozen method and the running code are
  compared, and an unapproved `SCIENTIFIC_MAJOR` deviation cannot carry a
  confirmatory package forward (`ADR-018`, ACC-104).
- **Model execution fingerprint** — every invocation contributing to a result
  records what actually executed, retry and fallback history included, and a
  hosted black-box model does not yield an `EXACT` reproduction claim
  (ACC-115, ACC-116).
- **Publication compiler** — no prose without a claim, no number without a
  `VerifiedValue`, and a complete evidence chain checked link by link
  (ACC-105, ACC-106).

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

9, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |

### Full prerequisite closure

**44 of 160 packages (28%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-061` |

### What acceptance of this package releases

- **Directly unblocked:** 17 — `WP-076` · `WP-077` · `WP-078` · `WP-079` · `WP-080` · `WP-081` · `WP-086` · `WP-087` · `WP-089` · `WP-090` · `WP-093` · `WP-095` · `WP-099` · `WP-101` · `WP-104` · `WP-108` · `WP-146`
- **Transitively reachable:** **70 of 160 packages (44%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **27** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Data Architect / Assurance Lead |
| Gates touched | `G5–G10` |
| Controls | `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-70 — EvidenceGap Lifecycle](../12_ACCEPTANCE_SCENARIOS/acc_70_evidence_gap_lifecycle.md) | High | The wrong evidence does not close the gap; the qualifying evidence satisfies it; the retraction reopens it with its full history intact. An open gap never authorises work by itself. |
| [ACC-78 — Raw Evidence Versus Interpretation](../12_ACCEPTANCE_SCENARIOS/acc_78_raw_evidence_versus_interpretation.md) | Critical | The finding gains a new version; every raw artifact's bytes and digest are unchanged. The direct raw edit is refused. Interpretation is revisable; evidence is not. |
| [ACC-085 — A Blackboard Entry Is Not Evidence](../12_ACCEPTANCE_SCENARIOS/acc_085_blackboard_entry_is_not_evidence.md) | Critical | Both attempts are refused. After deletion, no canonical scientific record is lost — everything that mattered was an artifact, a span, a claim or a finding, and the entry only pointed at it. |
| [ACC-105 — A Claim Without a Complete Evidence Chain](../12_ACCEPTANCE_SCENARIOS/acc_105_claim_without_evidence_chain.md) | Critical | The break is found and named at the failing link, and publication is blocked. A complete chain passes, so the audit discriminates rather than blocking every claim. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md)
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
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Destructive projection rebuild proof` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |

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
- **Evidence Platform Lead** carries the acceptance decision; **Data Architect / Assurance Lead** must verify independently of whoever implements.
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
| `ASM-001` — ScientistOne / Science One Framework — Chain-of-Evidence | `ADAPTIVE_REIMPLEMENT` | `MS-COE-001` · `MS-COE-002` · `MS-COE-003` · `MS-COE-004` · `MS-COE-005` · `MS-COE-006` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-005` — ScienceClaw — immutable artifact DAG | `DIRECT_ADAPT` | `artifacts/artifact.py` · `artifacts/graph_snapshot.py` | the local module and contract surface this becomes — **named at refinement** | **3** |
| `ASM-006` — ScienceClaw — NeedItem broadcast | `ADAPTIVE_REIMPLEMENT` | `MS-GAP-001` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `CMP-025` — SEPIO | `STANDARD` | The assertion/evidence/provenance core model. | The AIRL profile over SEPIO's core — which relation types are used and what each licenses. | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-001` | A CoE Audit result is a VerificationResult, never a GateRecord verdict. The audit reports; the gate policy decides. | The producer architecture, the provider assumptions, and any notion that the audit score is itself a decision. |
| `ASM-005` | An ArtifactRecord is evidence lineage. It confers no authority to act and no claim status. | Per-agent store.jsonl and the shared global_index.jsonl as canonical storage. AETHRION holds payloads in a content-addressed object store and metadata in PostgreSQL; a JSONL index is at most a derived projection. |
| `ASM-006` | An open EvidenceGap authorises nothing. It is an input to task compilation under gate policy, never a trigger that starts work by itself. | The ArtifactReactor's autonomy — upstream, an unmet need scored by urgency automatically triggers a peer agent to run a skill. That is precisely the authority AETHRION withholds. |
| `CMP-025` | A model of assertions is not an assertion about truth. SEPIO gives the shape; the gate decides what may be believed. | SEPIO's full ontology where the profile does not use it. |

### Where a plain row would mislead

- **`ASM-001`** — Two public versions of this work report different evaluation corpus sizes. Any number quoted from it must carry the version it came from — the same rule this architecture applies to SourceRepresentation.
- **`ASM-005`** — The value semantics — ordered parents, content hash, producer provenance — are what is taken. The storage decision is not.
- **`ASM-006`** — The upstream mechanism is a coordination signal; the AETHRION object is a scientific need with an acceptance condition and a lifecycle.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-001` — ScientistOne / Science One Framework — Chain-of-Evidence** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-005` — ScienceClaw — immutable artifact DAG** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a pinned upstream commit — a branch name is not a pin
- a characterisation suite capturing upstream behaviour **before** any code moves

**`ASM-006` — ScienceClaw — NeedItem broadcast** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**Acquisition readiness — 5 obligations open across 3 of 4 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-075-T01 | Migrate the claim, evidence, dependency and assessment tables | Implementation owner | Commit / configuration / record reference |
| WP-075-T02 | Write the version, create, challenge and supersede APIs | Implementation owner | Commit / configuration / record reference |
| WP-075-T03 | Bind optimistic locking, actor, policy and outbox events | Implementation owner | Commit / configuration / record reference |
| WP-075-T04 | Apply field-level and data-class RBAC plus access logging | Implementation owner | Commit / configuration / record reference |
| WP-075-T05 | Add the lineage and impact query APIs | Implementation owner | Commit / configuration / record reference |
| WP-075-T06 | Establish backup, integrity checks and the WORM audit export | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Claim Ledger service`
- `Migrations/API`
- `State transition engine`
- `Lineage queries`
- `Service runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-075_claim_evidence_ledger.tests.md`](wp_075_claim_evidence_ledger.tests.md).

- Immutable versioning and supersession
- Denial of an unauthorised claim verification
- A claim → source/run/review/decision query
- Concurrent challenges to the same claim
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-075_claim_evidence_ledger.acceptance.md`](wp_075_claim_evidence_ledger.acceptance.md), together with what this package still cannot establish.

- [ ] Correcting the text of a claim produces a new version.
- [ ] `VERIFIED` is not a permanent or irreversible state.
- [ ] A material claim with a missing link cannot appear in a publication.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

A faulty transition is corrected by a superseding event; historical decisions and references remain unchanged.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
