---
title: "WP-137 — G10 External Feed Connectors"
aliases:
  - "WP-137"
  - "WP-137 — G10 External Feed Connectors"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Post-publication monitoring feeds are connected and versioned."
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-137_g10_external_feed_connectors.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/m
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-137 — G10 External Feed Connectors

## Package card

| Field | Value |
|---|---|
| Work package | `WP-137` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Citation Auditor |
| Hard dependencies | WP-037 (G10 ImpactScan), WP-063 (Source status), WP-136 |
| Related gates | G10 |
| Related controls | CTL-EPI-04 |
| Related acceptance scenarios | ACC-04, ACC-31, ACC-36 |
| Related skill | `monitoring-external-feeds` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_137_g10_external_feed_connectors.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_137_g10_external_feed_connectors.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Post-publication monitoring feeds are connected and versioned.

| Feed | What it watches |
|---|---|
| Crossref + Retraction Watch | Has a cited source been retracted? |
| Crossmark | Correction notices |
| PubMed / domain repository | Corrections and retractions |
| Dataset registry | Dataset version changes and withdrawals |
| CVE / security advisories | Vulnerabilities in a tool we use |
| Provider changelog | A model profile changed or was removed |
| Citation tracking | Who has refuted us? |

> **Invariant:** There is no silent supersession. A material signal opens an
> `ImpactCase` and requires a human decision. Declaring something "immaterial"
> is itself a decision, and it is auditable.


## Analysis
### What this package actually decides

What the outside world is allowed to tell the system, and on what cadence. Five
feed classes — retraction, dataset registry, CVE, provider changelog — each
registered with a **version and an access date**.

### The feed registry is what makes monitoring auditable (T01)

A monitoring result is only interpretable if you know what was queried, at what
version, and when. `scripts/verify_references.py` already applies this discipline
in the running slice: its measurement file records the authorities, the threshold
and the retrieval time.

Without it, "no retractions found" is a sentence with no scope.

### The positive control is non-negotiable

`scripts/monitor_sources.py` already carries a known-retracted control and **fails
if the control stays silent**. Every feed added here inherits that rule, because a
feed that has never reported a signal is indistinguishable from a feed that is not
running.

### Retraction Watch alongside Crossref (T02)

Crossref resolves by DOI and reports what publishers register. Retraction Watch
covers cases publishers handle slowly or not at all. Two feeds because one has a
known blind spot — and the current coverage number makes that concrete: **15 of 33
registry sources carry a DOI**, so the DOI-resolved path sees less than half.

### Materiality scoring with a mandatory rationale (T05)

Not every signal matters. A CVE in a dependency the system does not execute, a
dataset revision that does not affect the slice used. Scoring is legitimate; scoring
**without a rationale** turns a judgement into a filter nobody can audit — and a
low-materiality misjudgement silently drops a real impact.

### Provider changelog monitoring feeds WP-124

A model changed behind a stable name is a requalification trigger. This is the feed
that notices.

## Out of scope

- The `ImpactCase` resolution decision itself (WP-108)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-136 — Inbound Content Quarantine and Channel Allowlist](../13_TOOLING_INTEGRATION/wp_136_inbound_content_quarantine.md) | — |

### Full prerequisite closure

**54 of 141 packages (38%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 24 | `WP-050` · `WP-054` · `WP-055` · `WP-131` |
| 25 | `WP-056` · `WP-132` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` |
| 28 | `WP-062` · `WP-136` |
| 29 | `WP-063` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Citation Auditor |
| Gates touched | `G10` |
| Controls | `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-36 — Model Snapshot Drift](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) | Critical | The profile moves to suspension or requalification, the router cache is invalidated and an `ImpactScan` opens for open tasks, runs and claims; there is no unsafe fallback. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-037 (G10 ImpactScan), WP-063 (Source status), WP-136
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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
| `Representation ingest service` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `License/status policy` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Status monitor` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Format locator metadata` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Retention mapping` | `WP-063` | `python3 scripts/progress.py show WP-063` |

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
- **Knowledge Monitoring Lead** carries the acceptance decision; **Citation Auditor** must verify independently of whoever implements.
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
| WP-137-T01 | Feed registry: source, version, access date, poll frequency | Registry file |
| WP-137-T02 | Crossref + Retraction Watch connector | A retraction is caught in test |
| WP-137-T03 | Dataset registry and CVE feeds | A version change is caught |
| WP-137-T04 | Provider model changelog monitoring | A model profile change triggers requalification |
| WP-137-T05 | Materiality scoring with a mandatory rationale | A materiality decision without a rationale is rejected |
| WP-137-T06 | Feed liveness check (dead-man's switch) | A stalled feed raises an alarm |

## Mandatory deliverables

- The feed registry (version + access date)
- The connector implementations
- Materiality scoring and its rationale record
- Feed liveness monitoring

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-137_g10_external_feed_connectors.tests.md`](wp_137_g10_external_feed_connectors.tests.md).

- **Retraction:** when a test DOI is retracted, an `ImpactCase` opens
- **Cascade:** retracted source → span → claim → publication → citing works, end to end
- **Materiality:** a `material=false` decision without a rationale is rejected
- **Silent death:** if a feed does not run for N days, an alarm is raised
- Inbound feed content is subject to the `receiving-external-messages` rules

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-137_g10_external_feed_connectors.acceptance.md`](wp_137_g10_external_feed_connectors.acceptance.md), together with what this package still cannot establish.

- [ ] A material signal cannot be logged and passed over; an `ImpactCase` is mandatory
- [ ] Every materiality decision carries a written rationale
- [ ] A feed cannot sit dead for months without being noticed
- [ ] The cascade chain is tested end to end
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- If a feed dies silently, monitoring exists only on paper; the liveness check is non-waivable
- Feed content is untrusted and is subject to the WP-136 rules
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The feed is stopped; open `ImpactCase`s are not closed and remain for human
decision. The missed monitoring window is recorded explicitly.

## Handoff into downstream packages

WP-108 (the retraction/drift vertical slice) consumes these feeds.
