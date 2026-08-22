---
title: "WP-018 — Claim, Evidence, Review and Decision Schemas"
aliases:
  - "WP-018"
  - "WP-018 — Claim, Evidence, Review and Decision Schemas"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Claim versioning, evidence spans, dependencies, assessments, review verdicts, disagreement and human-decision semantics become publishable contracts."
source: "planning/commissioning/02_CONTRACTS/WP-018_claim_review_decision_contracts.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
---

# WP-018 — Claim, Evidence, Review and Decision Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-018` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Assurance Lead / Methodologist |
| Hard dependencies | WP-011, WP-012, WP-014, WP-016, WP-017 |
| Related gates | G5–G10 |
| Related controls | CTL-EPI-01, CTL-EPI-04 |
| Related acceptance scenarios | ACC-08, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_018_claim_review_decision_contracts.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_018_claim_review_decision_contracts.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Claim versioning, evidence spans, dependencies, assessments, review verdicts, disagreement and human-decision semantics become publishable contracts.


## Analysis
### What this package actually decides

What licenses a sentence. A `ClaimRecord` without an evidence anchor is an
opinion with a schema, and the anchor's design — T02's **hash + structural
locator + text fingerprint** — is the most consequential decision in the package.

Three components, because each fails differently:

- The **hash** identifies the exact representation. It is exact and brittle: a new
  PDF from the publisher breaks it.
- The **structural locator** — section, paragraph, offset — survives a
  re-extraction of the same document but not a re-typesetting.
- The **text fingerprint** survives both, and can re-find the span in a document
  whose structure has changed.

Any one alone gives up either precision or durability. Together they degrade
gracefully: when the hash stops matching, the span is still locatable and the
system can say *the source changed* rather than *the evidence is gone.*

### Why claims are versioned rather than edited

T01's state machine exists because a claim's meaning must be stable once anything
depends on it. Editing a claim in place silently changes what every downstream
review, decision and publication was about. Versioning makes supersession
explicit, and supersession is what G10 needs to close the loop.

### `ClaimDependency` is what makes contradiction expressible (T03)

`supports` / `contradicts` / `derived-from`. The middle one is the reason the
package matters: a knowledge base that can only express agreement will accumulate
mutually contradictory claims and never notice. `contradicts` makes the
inconsistency a queryable state rather than a thing a reader might spot.

This is also what `ACC-08` — the strong counter-test — needs to bind to.

### The review contracts must make disagreement terminal (T04, T05)

`ReviewRecord`, `Verdict`, `Finding`, `Disposition`, then `DisagreementCase`.
`00_PROGRAM/06` states the rule these encode: *every finding must reach a terminal
state. A finding that is neither closed nor explicitly parked with an owner and an
expiry has not been handled; it has been forgotten.*

That is a schema requirement, not a process aspiration: `Finding` needs a state
field whose domain contains no value meaning "open indefinitely".

### The gap this package inherits and cannot close

Confidence. `PR-17` — *confidence scores carry no measurement basis* — and the
`calibrating-confidence` skill both say the same thing: a number with no
measurement behind it is worse than no number, because it reads as precision.

This package should define the field and **require it to carry its calibration
basis or be marked `UNCALIBRATED`**. It cannot supply the calibration; that is the
metascience gap in `00_PROGRAM/11`. What it can do is make an uncalibrated number
impossible to display as if it were calibrated.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |

### Full prerequisite closure

**15 of 141 packages (11%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 9 | `WP-012` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-017` |

### What acceptance of this package releases

- **Directly unblocked:** 15 — `WP-019` · `WP-020` · `WP-030` · `WP-033` · `WP-037` · `WP-043` · `WP-075` · `WP-076` · `WP-077` · `WP-080` · `WP-086` · `WP-088` · `WP-089` · `WP-090` · `WP-093`
- **Transitively reachable:** **122 of 141 packages (87%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **12** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Assurance Lead / Methodologist |
| Gates touched | `G5–G10` |
| Controls | `CTL-EPI-01` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md)
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
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |

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
- **Evidence Platform Lead** carries the acceptance decision; **Assurance Lead / Methodologist** must verify independently of whoever implements.
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
| WP-018-T01 | Write the `ClaimRecord` type, status and validity conditions | Implementation owner | Commit / configuration / record reference |
| WP-018-T02 | Define the evidence anchor as hash + structural locator + text fingerprint | Implementation owner | Commit / configuration / record reference |
| WP-018-T03 | Add the `ClaimDependency` supports / contradicts / derived-from relations | Implementation owner | Commit / configuration / record reference |
| WP-018-T04 | Write the `ReviewRecord`, `Verdict`, `Finding` and `Disposition` schemas | Implementation owner | Commit / configuration / record reference |
| WP-018-T05 | Complete the `DisagreementCase`, `DecisionRecord` and supersession fields | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Evidence contract bundle`
- `Claim state machine`
- `Review/disagreement schemas`
- `Decision schema fixtures`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-018_claim_review_decision_contracts.tests.md`](wp_018_claim_review_decision_contracts.tests.md).

- An immutable claim-version test
- State tests for `RELOCATED`, `AMBIGUOUS` and `NEEDS_REANCHOR`
- A gate fixture for an unresolved critical verdict
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-018_claim_review_decision_contracts.acceptance.md`](wp_018_claim_review_decision_contracts.acceptance.md), together with what this package still cannot establish.

- [ ] Evidence is not marked `ORPHANED` while the old representation remains reachable.
- [ ] Correcting a claim produces a new version rather than an edit.
- [ ] Reviews and decisions carry a frozen snapshot of their inputs.
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

On a schema fault the record is quarantined; a migration adapter is applied without overwriting canonical history.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
