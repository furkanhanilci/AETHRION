# WP-064 — Zotero Library, Collection and Permission Model

## Package card

| Field | Value |
|---|---|
| Work package | `WP-064` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Security / Governance |
| Hard dependencies | WP-004, WP-012, WP-017, WP-049, WP-050, WP-061 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-03, CTL-SEC-03 |
| Related acceptance scenarios | ACC-01, ACC-02 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-064_zotero_library_access.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-064_zotero_library_access.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The personal Zotero library becomes a read-only seed surface, AIRL group libraries become collaboration surfaces bounded by trust and membership, and agent-managed collections carry an explicit namespace.


## Analysis
### What this package actually decides

That the researcher's own library is never at risk. The personal Zotero library is
a **read-only seed surface**; group libraries are where collaboration and agent
writes happen; and the boundary between them is the one invariant a researcher has
to be able to trust without reading any code.

`00_PROGRAM/01` invariant 5: *no agent can write to a personal Zotero record;
human fields are never silently overwritten.*

### The collection namespace is the visible half of the control (T04)

`00_Human_Seeds`, `10_Agent_Candidates`, `20_Screening`, `30_Included`, `40_Used`,
`50_Excluded`, `80_Updates`, `90_Frozen_View`. Eight collections, and the numbering
carries the workflow order so a human opening Zotero can see where anything is
without consulting the system.

The important property is that **agent-managed collections are named as such**. A
researcher looking at `10_Agent_Candidates` knows nothing there is their judgement.

### `90_Frozen_View` is a mirror, and must be marked as one (T04)

WP-072 writes the canonical `LiteratureSetManifest` to the object store. The Zotero
frozen view is a **reading copy** — the same relationship the Obsidian mirrors have
to the repository, and the same failure mode: someone edits the mirror and the edit
is lost or, worse, is mistaken for the source.

### Opening a group library is a governed decision, not a setup step (T02)

Membership, confidentiality, licence, retention, ownership. Each is a real question
and each has a wrong answer that is discovered later: a group library whose
organisation owner leaves, or whose retention terms conflict with a source licence,
becomes a problem no code change fixes.

### Organisation continuity is the risk nobody plans for (T06)

Zotero group libraries belong to an organisation account. A solo laboratory's
organisation has one owner, and the continuity plan is the honest acknowledgement
that this is a single point of failure — the same shape as ADR-001's declared gap.

### Baseline v1.3.0 — unchanged ownership, new cross-cutting obligations

No semantic ownership changes here. What changes is what these packages must
remain compatible with:

- the **trace and correlation** fields every plane now carries, so a divergence
  is traceable to a cause;
- **context projection**, so that a record's canonical status does not depend on
  whether it happened to be in an agent's context;
- **provenance rules** for anything adapted from an upstream source.

Generated counts, indexes and the new cross-cutting acceptance references must
stay consistent — which is a mechanical obligation, and the one most likely to be
skipped because nothing in the package's own subject matter changed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md) | `Versioned connectors` · `Connector permission profiles` · `Connector contract tests` · `Compensation/reconciliation playbooks` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |

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
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-050` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-061` |

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-065` · `WP-066` · `WP-067` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **66 of 160 packages (41%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **27** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Security / Governance |
| Gates touched | `G3` · `G10` |
| Controls | `CTL-LIT-03` · `CTL-SEC-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/ACC-02_agent_used_source_writeback.md) | Critical | The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md)
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
| `Decision policy` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `SLA/escalation table` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Delegation matrix` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Decision rationale rubric` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Human intervention vocabulary` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Timeout escalation path with no approval branch` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Versioned connectors` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector permission profiles` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector contract tests` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Compensation/reconciliation playbooks` | `WP-050` | `python3 scripts/progress.py show WP-050` |
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

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Knowledge Lead** carries the acceptance decision; **Security / Governance** must verify independently of whoever implements.
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
| WP-064-T01 | Verify the personal-library read-only credential and its access boundary | Implementation owner | Commit / configuration / record reference |
| WP-064-T02 | Define the criteria for opening a group library: membership, confidentiality, licence, retention and ownership | Implementation owner | Commit / configuration / record reference |
| WP-064-T03 | Create the project collection template | Implementation owner | Commit / configuration / record reference |
| WP-064-T04 | Establish 00_Human_Seeds / 10_Agent_Candidates / 20_Screening / 30_Included / 40_Used / 50_Excluded / 80_Updates / 90_Frozen_View | Implementation owner | Commit / configuration / record reference |
| WP-064-T05 | Apply agent versus human authority and the R3 intake/curated separation | Implementation owner | Commit / configuration / record reference |
| WP-064-T06 | Write the organisation owner/admin continuity plan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Zotero topology`
- `Collection template`
- `Credential/permission matrix`
- `Library lifecycle SOP`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-064_zotero_library_access.tests.md`](WP-064_zotero_library_access.tests.md).

- A negative write test against the personal library
- Denial of a write to the wrong group or collection
- R3 intake → curated promotion
- An owner-continuity tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-064_zotero_library_access.acceptance.md`](WP-064_zotero_library_access.acceptance.md), together with what this package still cannot establish.

- [ ] A group per project is not the default; the trust boundary decides.
- [ ] An agent cannot write to the personal library.
- [ ] A collection namespace alone is never counted as a security control.
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

A wrong group or permission release is revoked; the write connector is disabled and the `SyncReceipt` ledger is audited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
