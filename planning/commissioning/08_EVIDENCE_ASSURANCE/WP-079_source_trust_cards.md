# WP-079 — SourceTrustCard and Study Quality Assessment

## Package card

| Field | Value |
|---|---|
| Work package | `WP-079` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Methodologist |
| Independent verifier | Independent Domain/Statistician Reviewer |
| Hard dependencies | WP-005, WP-017, WP-063, WP-075, WP-076, WP-078 |
| Related gates | G3,G6,G10 |
| Related controls | CTL-EPI-02, CTL-LIT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-079_source_trust_cards.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-079_source_trust_cards.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A source's status, study design, sample, measurement, bias, analysis, external validity and reporting limits are held in a reasoned trust card rather than collapsed into a single score.


## Analysis
### What this package actually decides

How much weight a source can bear — reported as a **reasoned card, not a score**.
The purpose sentence rules out the alternative explicitly, and the reason is the
same one that shapes WP-005, WP-006 and WP-077: a single number lets a strong
dimension mask a disqualifying one, and it cannot be argued with.

### Separate dimensions, because they fail separately (T03)

Method, bias, precision, applicability. A large, well-run trial in a population
unlike yours scores well on three and is inapplicable. A small, precise, directly
applicable study is weak on precision alone. Collapsing them produces two sources
with the same number and nothing in common.

### The automatic half and the assessed half must stay visibly separate (T02, T03)

Status, licence and provenance are **facts** — retracted or not, licensed or not,
where it came from. Method, bias, precision and applicability are **judgements**.
Presenting them in one card without marking which is which invites a reader to
treat an assessment with the confidence of a lookup.

### Expiry is what stops a card from ageing into a claim (T05)

A trust card is an assessment made at a time, against a version of the source. A
new version, a retraction, or simple age all invalidate it — and an expired card
must read as *unassessed*, not as its last value.

This is the same discipline WP-042 applies to model admission.

### The calibration sample is what makes the rubric more than vocabulary (T06)

Two assessors applying the same rubric to the same source should reach similar
cards. If they do not, the rubric is a set of words rather than a scale — and the
agreement number is the only way to know.

`measuring-agreement` is the skill; this is where it produces a number.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md) | `Anchor resolver` · `Format adapters` · `Re-anchor queue` · `Anchor regression corpus` |
| [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md) | `Extraction pipeline` · `Extraction schemas` · `Evidence candidate store` · `Second-pass review queue` |

### Full prerequisite closure

**61 of 141 packages (43%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-037` · `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` |
| 30 | `WP-067` |
| 31 | `WP-068` |
| 32 | `WP-076` |
| 33 | `WP-078` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-080` · `WP-095` · `WP-104`
- **Transitively reachable:** **38 of 141 packages (27%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **34** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Methodologist |
| Independent verifier | Independent Domain/Statistician Reviewer |
| Gates touched | `G3` · `G6` · `G10` |
| Controls | `CTL-EPI-02` · `CTL-LIT-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md)
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
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
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
| `Anchor resolver` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Format adapters` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Re-anchor queue` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Anchor regression corpus` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Extraction pipeline` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Extraction schemas` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Evidence candidate store` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Second-pass review queue` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Quality dashboard` | `WP-078` | `python3 scripts/progress.py show WP-078` |

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
- **Methodologist** carries the acceptance decision; **Independent Domain/Statistician Reviewer** must verify independently of whoever implements.
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
| WP-079-T01 | Define rubrics and profiles per source type | Implementation owner | Commit / configuration / record reference |
| WP-079-T02 | Bind the automatic status, licence and provenance fields | Implementation owner | Commit / configuration / record reference |
| WP-079-T03 | Assess method, bias, precision and applicability as separate dimensions | Implementation owner | Commit / configuration / record reference |
| WP-079-T04 | Write the human/agent assessment and disagreement semantics | Implementation owner | Commit / configuration / record reference |
| WP-079-T05 | Add expiry, new-version and retraction impact rules | Implementation owner | Commit / configuration / record reference |
| WP-079-T06 | Prepare the calibration sample and the reviewer guide | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SourceTrustCard engine`
- `Rubric profiles`
- `Calibration set`
- `Trust review UI contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-079_source_trust_cards.tests.md`](WP-079_source_trust_cards.tests.md).

- A prestigious venue with a weak method not yielding high trust
- Retraction overriding every other dimension
- Reviewer calibration
- Missing data recorded as `UNKNOWN` rather than zero
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-079_source_trust_cards.acceptance.md`](WP-079_source_trust_cards.acceptance.md), together with what this package still cannot establish.

- [ ] Trust is not a single authority score.
- [ ] Every card carries its rules, evidence and rationale.
- [ ] Source quality never substitutes for claim entailment or reproduction.
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

A rubric change never mutates an existing card; it produces a re-assessment queue and a new card version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
