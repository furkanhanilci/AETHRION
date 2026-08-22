# WP-113 — Evidence, Reproduction and Publication Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-113` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Independent Reproducer / Citation Auditor |
| Hard dependencies | WP-085, WP-087, WP-088, WP-089, WP-090, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-EPI-01, CTL-EPI-03, CTL-OPS-03 |
| Related acceptance scenarios | ACC-19..23, ACC-30, ACC-31, ACC-38, ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-113_evidence_repro_acceptance.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-113_evidence_repro_acceptance.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Clean-room pass and fail, graph rebuild, human note preservation, artifact overwrite, publication completeness, supersession, reviewer availability and negative-result scenarios close against the epistemic invariants.


## Analysis
### What this package actually decides

Whether the epistemic invariants survive. Nine scenarios, and unlike the security
set these attack the **claims** rather than the infrastructure.

### The two scenarios that test the system's honesty

**`ACC-20` clean-room fail.** A reproduction that fails must mark the claim
`CHALLENGED` and reopen the gate. A system that only demonstrates a passing
reproduction has shown the mechanism and not the control.

**`ACC-39` negative result.** A run that does not support the hypothesis must
produce a citable result and a stop-or-pivot decision. `PR-19` — publication bias
survives the gate structure — begins with a system where this is awkward.

### `ACC-22` human note preservation is the one a researcher will actually notice

The projection deletes only files in its own manifest, and a human note in the
generated folder survives. This is already true in the running slice and is proven
by a test — and it is the promise that makes an unattended 30-minute timer
acceptable.

### `ACC-21` graph rebuild is the falsification test for canonical ownership

Delete every derived index, rebuild from canonical records. Anything that does not
return was never derived, and WP-012's ownership matrix is wrong about it.

### `ACC-38` reviewer availability is where ADR-001 becomes visible

No eligible reviewer means `BLOCKED`, declared. In a solo laboratory this is the
expected outcome at R3, and a scenario that passes by finding a reviewer has either
found an external one or broken the constraint.

### `ACC-23` artifact overwrite closes the immutability claim

Different bytes at the same content address must be refused **at the storage layer**
— `PR-08`, rated critical.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |
| [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md) | `Review service` · `Assignment/eligibility engine` · `Review rubrics` · `ReviewRecord storage` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |
| [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md) | `Publication builder` · `RO-Crate profile` · `Signed publication package` · `Release checklist` |
| [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md) | `Acceptance Registry` · `Scenario runner` · `Fixture catalog` · `Evidence capture/signing` |

### Full prerequisite closure

**109 of 141 packages (77%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-115` · `WP-126`
- **Transitively reachable:** **16 of 141 packages (11%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **47** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Assurance Lead |
| Independent verifier | Independent Reproducer / Citation Auditor |
| Gates touched | `Commissioning` |
| Controls | `CTL-EPI-01` · `CTL-EPI-03` · `CTL-OPS-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/ACC-19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/ACC-31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-38 — Critical Reviewer Unavailable](../12_ACCEPTANCE_SCENARIOS/ACC-38_reviewer_unavailable.md) | High | Neither the producer, a self-review, nor an ineligible fallback is used; the gate is `BLOCKED` and a human scheduling/escalation item and a capacity signal are produced. |
| [ACC-39 — Negative Research Result](../12_ACCEPTANCE_SCENARIOS/ACC-39_negative_result.md) | Medium | The result is neither lost nor reframed as a success; a negative run and claim artifact, the limitations and a stop/pivot/continue `DecisionRecord` are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
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
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Review service` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Assignment/eligibility engine` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Review rubrics` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `ReviewRecord storage` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Calibration dashboard` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Publication builder` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `RO-Crate profile` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Signed publication package` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Release checklist` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Supersession record` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Acceptance Registry` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Scenario runner` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Fixture catalog` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Evidence capture/signing` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Result dashboard` | `WP-109` | `python3 scripts/progress.py show WP-109` |

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
- **Assurance Lead** carries the acceptance decision; **Independent Reproducer / Citation Auditor** must verify independently of whoever implements.
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
| WP-113-T01 | Run the ACC-19–23, 30, 31, 38 and 39 fixtures | Implementation owner | Commit / configuration / record reference |
| WP-113-T02 | Verify the claim, manifest, anchor and reproduction tolerance assertions | Implementation owner | Commit / configuration / record reference |
| WP-113-T03 | Perform the graph and Obsidian derived rebuild with human-content preservation | Implementation owner | Commit / configuration / record reference |
| WP-113-T04 | Audit publication and supersession | Implementation owner | Commit / configuration / record reference |
| WP-113-T05 | Verify reviewer-capacity `BLOCKED` and the negative-result stop/pivot | Implementation owner | Commit / configuration / record reference |
| WP-113-T06 | Produce the assurance dossier and sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Evidence/repro scenario results`
- `Reproduction certificates`
- `Lineage/integrity reports`
- `Assurance sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-113_evidence_repro_acceptance.tests.md`](WP-113_evidence_repro_acceptance.tests.md).

- ACC-19, 20, 21, 22, 23, 30, 31, 38 and 39
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-113_evidence_repro_acceptance.acceptance.md`](WP-113_evidence_repro_acceptance.acceptance.md), together with what this package still cannot establish.

- [ ] Critical claim lineage coverage is 100%.
- [ ] The clean-room policy is satisfied.
- [ ] No open critical or high assurance finding remains.
- [ ] Negative results are preserved.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

A failure blocks publication and cutover; claim status stays `CHALLENGED` or `PROVISIONAL` and a correction or reproduction is planned.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
