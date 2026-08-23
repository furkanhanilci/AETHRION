---
title: "WP-077 — Claim State, Dependency and Assessment Engine"
aliases:
  - "WP-077"
  - "WP-077 — Claim State, Dependency and Assessment Engine"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Empirical, methodological and interpretive claims move between PROVISIONAL, SUPPORTED, CONTESTED, CHALLENGED and REPLICATED under evidence, validity, conflict, reproduction and dependency blockers."
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md"
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

# WP-077 — Claim State, Dependency and Assessment Engine

## Package card

| Field | Value |
|---|---|
| Work package | `WP-077` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Methodologist / Assurance Lead |
| Hard dependencies | WP-005, WP-018, WP-075, WP-076 |
| Related gates | G5–G10 |
| Related controls | CTL-EPI-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-08, ACC-19, ACC-20 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_077_claim_state_dependency.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_077_claim_state_dependency.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Empirical, methodological and interpretive claims move between `PROVISIONAL`, `SUPPORTED`, `CONTESTED`, `CHALLENGED` and `REPLICATED` under evidence, validity, conflict, reproduction and dependency blockers.


## Analysis
### What this package actually decides

What it takes to move a claim from *we think* to *we found*. Five states, three
claim types, and an assessment vector that is deliberately **not** a score.

### The assessment vector has seven dimensions and no total (T03)

Provenance, method, directness, consistency, reproduction, scope, uncertainty.
Reporting them separately is the same decision WP-005 made for risk and WP-006 for
execution: a weighted total lets a strong dimension mask a fatal one, and the
fatal ones here are not compensable.

A claim with excellent method and no reproduction is not a `REPLICATED` claim with
a lower number. It is a different kind of claim.

### Non-compensable blockers are the package's teeth (T04)

Some failures cannot be outweighed. An orphaned evidence anchor, an unresolved
contradiction, a failed reproduction on a confirmatory claim — each stops the state
transition regardless of the other six dimensions.

### `CONTESTED` and `CHALLENGED` are different and both must exist (T01)

`CONTESTED` — the evidence base contains a genuine disagreement. `CHALLENGED` — a
specific counter-result or failed reproduction has been produced against it.
`00_PROGRAM/01` invariant 4 requires a failed clean-room reproduction to mark the
claim `CHALLENGED`, and a system with only one of these states will report an
unreplicated claim and a contradicted claim identically.

### Dependency propagation is where a single retraction becomes a cascade (T05)

A claim derived from a challenged claim is affected. Propagation must be
**computed and queued**, not applied silently — because the derived claim's author
may have good reason to say the derivation survives, and that is a judgement.

### Interpretive claims are the ones that need this most (T01)

Empirical claims fail loudly. Methodological claims fail on review. Interpretive
claims — *this result means X* — are where a fluent model is most confident and
least checkable, which is the failure `AGENTS.md` §1 names as the reason the whole
system exists.

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

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md) | `Anchor resolver` · `Format adapters` · `Re-anchor queue` · `Anchor regression corpus` |

### Full prerequisite closure

**59 of 160 packages (37%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 32 | `WP-076` |

### What acceptance of this package releases

- **Directly unblocked:** 12 — `WP-080` · `WP-085` · `WP-086` · `WP-088` · `WP-089` · `WP-090` · `WP-093` · `WP-095` · `WP-104` · `WP-106` · `WP-108` · `WP-146`
- **Transitively reachable:** **51 of 160 packages (32%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **33** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Methodologist / Assurance Lead |
| Gates touched | `G5–G10` |
| Controls | `CTL-EPI-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) | Critical | G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened. |
| [ACC-70 — EvidenceGap Lifecycle](../12_ACCEPTANCE_SCENARIOS/acc_70_evidence_gap_lifecycle.md) | High | The wrong evidence does not close the gap; the qualifying evidence satisfies it; the retraction reopens it with its full history intact. An open gap never authorises work by itself. |
| [ACC-78 — Raw Evidence Versus Interpretation](../12_ACCEPTANCE_SCENARIOS/acc_78_raw_evidence_versus_interpretation.md) | Critical | The finding gains a new version; every raw artifact's bytes and digest are unchanged. The direct raw edit is refused. Interpretation is revisable; evidence is not. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md)
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
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `StudyMode decision table` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Substantiality threshold for the multi-agent invariant` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Anchor resolver` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Format adapters` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Re-anchor queue` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Anchor regression corpus` | `WP-076` | `python3 scripts/progress.py show WP-076` |

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
- **Evidence Platform Lead** carries the acceptance decision; **Methodologist / Assurance Lead** must verify independently of whoever implements.
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
| `ASM-006` — ScienceClaw — NeedItem broadcast | `ADAPTIVE_REIMPLEMENT` | `MS-GAP-001` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-019` — DeepScientist — findings memory, failed routes, research map | `ADAPTIVE_REIMPLEMENT` | `MS-MEM-001` · `MS-MEM-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-006` | An open EvidenceGap authorises nothing. It is an input to task compilation under gate policy, never a trigger that starts work by itself. | The ArtifactReactor's autonomy — upstream, an unmet need scored by urgency automatically triggers a peer agent to run a skill. That is precisely the authority AETHRION withholds. |
| `ASM-019` | A FindingRecord is an interpretation of evidence. It never mutates the evidence it interprets, and it is not itself a ClaimVersion. | The autonomous studio runtime and its control loop, which would contend with Temporal. |

### Where a plain row would mislead

- **`ASM-006`** — The upstream mechanism is a coordination signal; the AETHRION object is a scientific need with an acceptance condition and a lifecycle.
- **`ASM-019`** — The idea worth taking is that a failed route is an asset rather than something to delete — which is what makes 'have we tried this before?' answerable from records instead of from chat history.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-006` — ScienceClaw — NeedItem broadcast** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-019` — DeepScientist — findings memory, failed routes, research map** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**Acquisition readiness — 2 obligations open across 2 of 2 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-077-T01 | Implement the claim type and lifecycle transition rules | Implementation owner | Commit / configuration / record reference |
| WP-077-T02 | Write validation for the supports / contradicts / derived-from dependency graph | Implementation owner | Commit / configuration / record reference |
| WP-077-T03 | Build the assessment vector across provenance, method, directness, consistency, reproduction, scope and uncertainty | Implementation owner | Commit / configuration / record reference |
| WP-077-T04 | Apply non-compensable blocker precedence | Implementation owner | Commit / configuration / record reference |
| WP-077-T05 | Add dependency status propagation and the impact queue | Implementation owner | Commit / configuration / record reference |
| WP-077-T06 | Write the human and assurance disposition API | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Claim state engine`
- `Dependency validator`
- `Assessment rubric`
- `Impact propagation worker`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-077_claim_state_dependency.tests.md`](wp_077_claim_state_dependency.tests.md).

- `BLOCKED` on broken provenance
- A strong source failing to compensate for a weak method
- `CONTESTED` on contradictory evidence
- State promotion on a reproduction pass
- Propagation of an upstream supersession
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-077_claim_state_dependency.acceptance.md`](wp_077_claim_state_dependency.acceptance.md), together with what this package still cannot establish.

- [ ] The seven dimensions are never averaged into a single confidence percentage.
- [ ] A critical blocker is not offset by high source quality.
- [ ] Every state change carries its rule and evidence references.
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

A wrong assessment is corrected through a new version or disposition; a publication impact scan opens automatically.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
