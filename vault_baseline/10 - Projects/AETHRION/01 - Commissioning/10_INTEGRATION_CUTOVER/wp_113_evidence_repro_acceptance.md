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

## Purpose and expected outcome

Clean-room pass and fail, graph rebuild, human note preservation, artifact overwrite, publication completeness, supersession, reviewer availability and negative-result scenarios close against the epistemic invariants.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/wp_109_acceptance_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

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

- ACC-19, 20, 21, 22, 23, 30, 31, 38 and 39
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

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
