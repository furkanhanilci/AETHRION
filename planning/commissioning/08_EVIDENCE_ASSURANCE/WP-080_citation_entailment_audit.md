# WP-080 — Claim–Citation Entailment, Scope and Locator Audit

## Package card

| Field | Value |
|---|---|
| Work package | `WP-080` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Citation Audit Lead |
| Independent verifier | Independent Methodologist / Human Reviewer |
| Hard dependencies | WP-007, WP-018, WP-072, WP-075, WP-076, WP-077, WP-078, WP-079 |
| Related gates | G6,G9 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Reference verification is implemented** — Crossref · OpenAlex · arXiv

`scripts/verify_references.py` resolves the registry against three authorities; the measured corroboration rate is recorded in `delivery/measurements/`. What remains in this package is the **entailment** half: does the cited passage support the claim?

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-080_citation_entailment_audit.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-080_citation_entailment_audit.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

For every material sentence, a structured audit verifies whether the linked evidence span actually supports the assertion, whether the scope is appropriate, and whether a contradiction exists.


## Analysis
### What this package actually decides

Whether the sentence is supported by the thing it cites. This is the closest the
system comes to checking its own honesty, and it is the package that most directly
addresses the failure `AGENTS.md` §1 names: *fluent, well-cited, confident model
output that is wrong.*

A citation that resolves is not a citation that supports. `scripts/README.md`
already draws the line: *a citation checker proves that a reference resolves, never
that it supports the sentence citing it.*

### Four checks, escalating in cost and in what they can catch (T02–T04)

1. **Locator integrity** — mechanical. Does the anchor resolve, does the quote
   hash match? Cheap, deterministic, and catches the citation pointing at nothing.
2. **Entailment** — does the span actually assert what the sentence claims?
3. **Scope** — is the sentence broader than the evidence? This is where
   overclaiming lives, and it is the most common real failure.
4. **Hedging** — has a hedged source finding become an unhedged assertion?

`00_PROGRAM/06`'s ordering applies: cheap layers first, so review attention is
spent on entailment rather than on broken links.

### Citation laundering is the check nobody builds (T04)

A cites B for a claim; B cites C; C says something weaker or different. Each hop
is defensible and the chain is not. Following secondary citations to their primary
source is expensive and it is the only way to catch this — and it is exactly what
a confident model does badly, because each individual hop reads correctly.

### Counter-evidence checking is an active search, not an absence (T04)

*No contradiction found* is only meaningful if a search for one was run. Otherwise
it means nobody looked, reported in the same words.

### The verdict is a **G9 blocker** (T06)

This is what makes the package real. `00_PROGRAM/01`'s G9 blocker is *missing claim
lineage or citation audit*, and a `CitationAudit` that produces a report nobody
must act on is a report.

### Risk-based sampling, full audit where it matters (T05)

Every material sentence at R3; a sample at R1. The sampling rate and the sampled
error rate are both published — a sample with no reported error rate cannot
support an inference about the unsampled remainder.

### Baseline v1.2.0 — one audit is four questions with three statuses

"Citation audit passed" hides which check actually ran. The four questions have
different epistemic statuses and must be reported separately:

| Question | Class |
|---|---|
| Does the reference exist and resolve? | V0 |
| Does the locator resolve in this representation version? | V0 |
| Does the quoted span match the source text digest? | V0/V1 |
| Does the cited passage **support** the sentence? | **V2** |
| Does the sentence claim **more** than the passage supports? | **V2** |

The first three are cheap and certain. The last two catch a hallucinated argument
and are the ones with an error rate — so they need a qualified verifier, and a
result recording them as V0 or V1 is refused (ACC-62).

**Existence is not support.** This package's reference half already runs and
reports 27 of 33 sources corroborated; that number says records exist in public
authorities, not that any claim is supported by them. The scope check is the one
that catches the hardest case: a real citation, on topic, that does not support
the sentence built on it — ACC-76.

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
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md) | `LiteratureSetManifest` · `Signed frozen package` · `Portable exports` · `Zotero frozen view` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md) | `Anchor resolver` · `Format adapters` · `Re-anchor queue` · `Anchor regression corpus` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md) | `Extraction pipeline` · `Extraction schemas` · `Evidence candidate store` · `Second-pass review queue` |
| [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md) | `SourceTrustCard engine` · `Rubric profiles` · `Calibration set` · `Trust review UI contract` |

### Full prerequisite closure

**70 of 160 packages (44%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-086` · `WP-087` · `WP-090` · `WP-095` · `WP-104` · `WP-106`
- **Transitively reachable:** **47 of 160 packages (29%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **35** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Citation Audit Lead |
| Independent verifier | Independent Methodologist / Human Reviewer |
| Gates touched | `G6` · `G9` |
| Controls | `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-52 — Claimless Publication Assertion](../12_ACCEPTANCE_SCENARIOS/ACC-52_claimless_publication_assertion.md) | Critical | The build fails; the sentence's location and the missing relation are reported; no signed `PublicationPackage` is produced. Prose whose `text_role` declares it structural or editorial is not affected. |
| [ACC-76 — Unsupported Publication Sentence](../12_ACCEPTANCE_SCENARIOS/ACC-76_unsupported_publication_sentence.md) | Critical | The reference-existence check passes at V0, and the entailment and scope checks fail at V2. Publication is blocked. A control sentence whose citation genuinely supports it passes both. |
| [ACC-105 — A Claim Without a Complete Evidence Chain](../12_ACCEPTANCE_SCENARIOS/ACC-105_claim_without_evidence_chain.md) | Critical | The break is found and named at the failing link, and publication is blocked. A complete chain passes, so the audit discriminates rather than blocking every claim. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md)
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
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `LiteratureSetManifest` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Signed frozen package` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Portable exports` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Zotero frozen view` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Freeze/diff report` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Anchor resolver` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Format adapters` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Re-anchor queue` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Anchor regression corpus` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Extraction pipeline` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Extraction schemas` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Evidence candidate store` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Second-pass review queue` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Quality dashboard` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `SourceTrustCard engine` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Rubric profiles` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Calibration set` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Trust review UI contract` | `WP-079` | `python3 scripts/progress.py show WP-079` |

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
- **Citation Audit Lead** carries the acceptance decision; **Independent Methodologist / Human Reviewer** must verify independently of whoever implements.
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
| `ASM-033` — CiTO — Citation Typing Ontology | `STANDARD` | the running implementation | the contract this is held behind | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-001` | A CoE Audit result is a VerificationResult, never a GateRecord verdict. The audit reports; the gate policy decides. | The producer architecture, the provider assumptions, and any notion that the audit score is itself a decision. |
| `ASM-033` | A citation type describes the intent of a link. It does not establish that the link is correct — that is the V2 entailment verifier's job. | The full ontology surface; only the relations EvidenceTag actually needs. |

### Where a plain row would mislead

- **`ASM-001`** — Two public versions of this work report different evaluation corpus sizes. Any number quoted from it must carry the version it came from — the same rule this architecture applies to SourceRepresentation.
- **`ASM-033`** — Not in the source brief; added here. EvidenceTag.support_relation was about to be an invented three-value enum (SUPPORTS / CHALLENGES / CONTEXTUALIZES). CiTO already provides the published vocabulary for exactly this — cito:supports, cito:disagreesWith, cito:usesMethodIn and the rest — and AETHRION's own rule is not to invent an identifier scheme where one is maintained by people closer to the problem. Binding the enum to CiTO IRIs costs nothing now and makes an EvidenceTag exportable to anyone who reads SPAR.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-001` — ScientistOne / Science One Framework — Chain-of-Evidence** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-033` — CiTO — Citation Typing Ontology** · `STANDARD` · status `PROPOSED`

- a conformance suite against the published specification

**Acquisition readiness — 2 obligations open across 2 of 2 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-080-T01 | Write the claim–evidence relationship rubric | Implementation owner | Commit / configuration / record reference |
| WP-080-T02 | Add mechanical locator integrity and quote/fingerprint checking | Implementation owner | Commit / configuration / record reference |
| WP-080-T03 | Build the entailment, scope, hedging and secondary-citation review graph | Implementation owner | Commit / configuration / record reference |
| WP-080-T04 | Add counter-evidence and citation-laundering checks | Implementation owner | Commit / configuration / record reference |
| WP-080-T05 | Apply risk-based human sampling and full audit | Implementation owner | Commit / configuration / record reference |
| WP-080-T06 | Integrate the `CitationAudit` verdict as a G9 blocker | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Citation audit service`
- `Audit rubric`
- `Mechanical locator checker`
- `Audit report/scorecard`
- `Decomposed citation audit with per-question verification class`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-080_citation_entailment_audit.tests.md`](WP-080_citation_entailment_audit.tests.md).

- Correct support passing
- A citation that is merely related but not supporting
- An overgeneralised scope failing
- Secondary-citation laundering
- A missing locator failing G9
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-080_citation_entailment_audit.acceptance.md`](WP-080_citation_entailment_audit.acceptance.md), together with what this package still cannot establish.

- [ ] The presence of a citation is not evidence of support.
- [ ] Critical claims reach 100% locator and entailment coverage.
- [ ] Every reviewer verdict carries an evidence span and a rationale.
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

A failed audit sends the claim or report to revision; neither the source nor any prior evidence is overwritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
