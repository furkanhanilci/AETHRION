---
title: "WP-050 — Initial Tool Connector Package"
aliases:
  - "WP-050"
  - "WP-050 — Initial Tool Connector Package"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Web, Crossref, Zotero, Git, object store, MLflow and the controlled notification tools run as least-privilege connectors that conform to the broker contract."
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/state/not-started
---

# WP-050 — Initial Tool Connector Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-050` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Tool Platform Lead |
| Independent verifier | Security / Connector Owners |
| Hard dependencies | WP-049 |
| Related gates | G3,G5,G9 |
| Related controls | CTL-LIT-03, CTL-OPS-01, CTL-SEC-01 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-05, ACC-35 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_050_tool_connectors.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_050_tool_connectors.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Web, Crossref, Zotero, Git, object store, MLflow and the controlled notification tools run as least-privilege connectors that conform to the broker contract.


## Analysis
### What this package actually decides

What the laboratory can reach, and on what terms. Seven connector families —
web, Crossref, Zotero, Git, object store, MLflow, notification — each with its own
least-privilege profile, its own compensation path, and its own target resolver.

### Least privilege per connector, not per broker (T01–T06)

The broker enforces the chain; the connector defines what is even possible. A web
connector with an allowlist cannot reach an arbitrary host **even if the policy
were wrong** — which is defence in depth rather than duplication.

### The Zotero split is the most consequential design decision here (T03)

Read, candidate, and update-proposal are **three separate connectors** with three
separate permission profiles. The plan's binding decision is that the personal
library is a read-only seed; group libraries are a controlled collaboration view.

`00_PROGRAM/01` invariant 5: *no agent can write to a personal Zotero record;
human fields are never silently overwritten.*

The running system's compliance is currently a property of its implementation
rather than of its contract: `src/airl_bridge/zotero.py` has no write path, and
`tests/README.md` records that the boundary is **asserted nowhere** — finding
**H3**. Splitting the connectors is what makes the read-only half structurally
incapable of writing rather than merely uninclined.

### `ACC-02` is the scenario this package must satisfy

Agent-used source write-back. The proposal path exists so an agent can *suggest* a
Zotero change; the human applies it. A connector that can both propose and apply
has collapsed the control.

### Compensation per connector, not in general (T07)

"Undo the tool call" is not implementable in the abstract. A Git branch can be
deleted; an object-store upload becomes `INVALIDATED`; a posted notification can
only be followed by a correction. Each connector states which of the three it is,
and the honest third option must be representable — WP-038's uncompensated
outcome.

### Web is the highest-risk connector and needs the tightest profile (T01)

It is the one that reaches arbitrary untrusted content, and its output flows into
agent context. Allowlist, egress proxy, quarantine, provenance — and `ACC-05`
applies here as much as to PDFs.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |

### Full prerequisite closure

**38 of 141 packages (27%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 8 — `WP-058` · `WP-060` · `WP-062` · `WP-063` · `WP-064` · `WP-065` · `WP-066` · `WP-069`
- **Transitively reachable:** **62 of 141 packages (44%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **24** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Tool Platform Lead |
| Independent verifier | Security / Connector Owners |
| Gates touched | `G3` · `G5` · `G9` |
| Controls | `CTL-LIT-03` · `CTL-OPS-01` · `CTL-SEC-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) | Critical | The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created. |
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) | Critical | The content stays untrusted quoted data; extraction continues read-only, no tool, secret or write call occurs, and security event and scan evidence is produced. |
| [ACC-35 — Tool Partial Failure](../12_ACCEPTANCE_SCENARIOS/acc_35_tool_partial_failure.md) | Critical | A blind retry does not produce a second side effect; a read and reconcile finds the remote effect, and exactly one `ToolReceipt` is finalized — or the call becomes `RECONCILIATION_REQUIRED`. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md)
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
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |

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
- **Tool Platform Lead** carries the acceptance decision; **Security / Connector Owners** must verify independently of whoever implements.
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
| WP-050-T01 | Implement the web read/search connector with its allowlist | Implementation owner | Commit / configuration / record reference |
| WP-050-T02 | Write the Crossref and status-lookup connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T03 | Separate the Zotero read, candidate and update-proposal connectors | Implementation owner | Commit / configuration / record reference |
| WP-050-T04 | Add the Git branch/worktree connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T05 | Build the object store signed-upload and reference connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T06 | Bind the MLflow run and metric connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T07 | Write a target resolver and compensation path for every connector | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Versioned connectors`
- `Connector permission profiles`
- `Connector contract tests`
- `Compensation/reconciliation playbooks`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-050_tool_connectors.tests.md`](wp_050_tool_connectors.tests.md).

- Quarantine of a web injection attempt
- Denial of any write to the personal Zotero library
- Denial of a write to a protected Git branch
- Object hash mismatch detection
- A connector timeout after the external call actually succeeded
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-050_tool_connectors.acceptance.md`](wp_050_tool_connectors.acceptance.md), together with what this package still cannot establish.

- [ ] Each connector operates only within its declared T class and target scope.
- [ ] Connector output is labelled as untrusted data.
- [ ] Every external write is either idempotent or reconcilable.
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

- A model alias is not a pinned identity; results obtained under an alias are not reproducible.
- An agent holding a credential defeats the entire broker design.
- Fallback routes are the least tested and most consequential path in this workstream.

## Rollback / compensation

A connector is disabled by feature flag; uncertain writes go to the reconciliation queue and reads fall back to retry with backoff.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
