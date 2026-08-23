# WP-076 — Evidence Span Anchoring and Re-anchoring

## Package card

| Field | Value |
|---|---|
| Work package | `WP-076` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Engineering Lead |
| Independent verifier | Citation Auditor / Reproducibility Engineer |
| Hard dependencies | WP-014, WP-017, WP-018, WP-026, WP-058, WP-063, WP-068, WP-075 |
| Related gates | G5,G6,G10 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-04, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-076_evidence_anchor_resolver.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-076_evidence_anchor_resolver.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Evidence is resolved against PDFs, HTML and dataset documentation through a triple anchor — representation content hash, structural position and text fingerprint — and receives an explicit state when the representation changes.


## Analysis
### What this package actually decides

Whether a citation still points at what it pointed at. WP-018 designs the
three-part anchor; this package resolves it, and its real content is the **state
machine for when resolution degrades**.

### Four states, because "broken" is four different problems (T04)

- `RELOCATED` — the span was found elsewhere in the same representation; the
  document was re-flowed, and the anchor self-healed.
- `AMBIGUOUS` — the fingerprint matches in more than one place; the system cannot
  choose, and guessing would silently re-point a citation.
- `NEEDS_REANCHOR` — the representation changed enough that only a human can say
  whether the span survived.
- `ORPHANED` — the representation is gone; the hash is all that remains.

Collapsing these into a boolean loses exactly the information a curator needs, and
`ORPHANED` in particular must stay distinct from *the evidence was wrong*.

### Confidence must be explainable, not scored (T03)

The relocation decision has the same property as WP-062's merge decision: a
curator has to act on the individual case, so the rule that produced it must be
readable. `PR-02`'s early signal is unexplainable decisions.

### The span model is richer than text (T02)

Text, table cell, figure, code block, data cell. A claim resting on a number in a
table needs the cell, not the page — and a claim resting on a figure needs the
figure, because the number is not in the text at all.

This is where extraction (WP-078) and the entailment audit (WP-080) both bind.

### The impact event closes the loop (T06)

An anchor that degrades is a claim whose support degraded. It has to reach the
claim, not sit in a resolver log.

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

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md) | `Content firewall` · `Parser workers` · `ContentSafetyRecord` · `Injection detector` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md) | `Annotation ingest service` · `AnnotationObservation records` · `EvidenceCandidate queue` · `Promotion/disposition UI contract` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |

### Full prerequisite closure

**58 of 160 packages (36%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 23 | `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` |
| 30 | `WP-067` |
| 31 | `WP-068` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-077` · `WP-078` · `WP-079` · `WP-080` · `WP-087` · `WP-095` · `WP-104`
- **Transitively reachable:** **54 of 160 packages (34%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **32** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Engineering Lead |
| Independent verifier | Citation Auditor / Reproducibility Engineer |
| Gates touched | `G5` · `G6` · `G10` |
| Controls | `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md)
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
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Content firewall` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Parser workers` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `ContentSafetyRecord` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Injection detector` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Quarantine UI/API` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Capability gate for untrusted content` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Representation ingest service` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `License/status policy` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Status monitor` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Format locator metadata` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Retention mapping` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Annotation ingest service` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `AnnotationObservation records` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `EvidenceCandidate queue` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `Promotion/disposition UI contract` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |

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
- **Evidence Engineering Lead** carries the acceptance decision; **Citation Auditor / Reproducibility Engineer** must verify independently of whoever implements.
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
| WP-076-T01 | Write the format-specific locator adapters | Implementation owner | Commit / configuration / record reference |
| WP-076-T02 | Implement the text, table, figure, code and data-cell span model | Implementation owner | Commit / configuration / record reference |
| WP-076-T03 | Establish the fingerprint, fuzzy relocation and confidence rules | Implementation owner | Commit / configuration / record reference |
| WP-076-T04 | Add the RELOCATED / AMBIGUOUS / NEEDS_REANCHOR / ORPHANED state machine | Implementation owner | Commit / configuration / record reference |
| WP-076-T05 | Write the human re-anchor queue and its audit trail | Implementation owner | Commit / configuration / record reference |
| WP-076-T06 | Emit the impact event for affected claims | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Anchor resolver`
- `Format adapters`
- `Re-anchor queue`
- `Anchor regression corpus`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-076_evidence_anchor_resolver.tests.md`](WP-076_evidence_anchor_resolver.tests.md).

- Exact resolution against a stable PDF
- `RELOCATED` on a re-laid-out PDF
- `AMBIGUOUS` on duplicated text
- No `ORPHANED` state while the old representation is available
- `ORPHANED` when the representation is genuinely unavailable
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-076_evidence_anchor_resolver.acceptance.md`](WP-076_evidence_anchor_resolver.acceptance.md), together with what this package still cannot establish.

- [ ] Anchor confidence alone is never claim support.
- [ ] A state change puts every dependent claim into impact assessment.
- [ ] Older evidence versions remain reachable.
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

A wrong relocation is not reverted; it is superseded by a new `AnchorResolution` record and a curator decision.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
