# WP-089 — DisagreementCase and Evidence-Weighted Arbitration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-089` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead / Arbiter |
| Independent verifier | Project Decision Owner / Internal Audit |
| Hard dependencies | WP-004, WP-007, WP-018, WP-075, WP-077, WP-087, WP-088 |
| Related gates | G6,G8 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-08 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Conflicting reviewer verdicts, producer objections to a correction and evidence mismatches become explicit cases; the arbiter records **which evidence prevailed and why**.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-089-T01 | Write conflict detection and the `DisagreementCase` lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-089-T02 | Bind the verdict/claim/evidence graph into the case snapshot | Implementation owner | Commit / configuration / record reference |
| WP-089-T03 | Apply arbiter eligibility and independence checks | Implementation owner | Commit / configuration / record reference |
| WP-089-T04 | Add the evidence-weighted disposition rubric and counter-test requests | Implementation owner | Commit / configuration / record reference |
| WP-089-T05 | Establish escalation of unresolved material risk to G8 | Implementation owner | Commit / configuration / record reference |
| WP-089-T06 | Write the appeal, supersession and audit flow | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Disagreement service`
- `Arbitration rubric`
- `Disposition workflow`
- `Appeal/decision integration`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A PASS/REJECT conflict raising an automatic case
- Three votes against one deterministic failing test
- Denial of an arbiter with a conflict of interest
- Unresolved risk remaining visible at G8
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A conflict is never silently overwritten.
- [ ] Resolution carries an evidence rationale, not a vote count.
- [ ] A non-waivable blocker cannot be waived by an arbiter.
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

A faulty disposition is corrected through an appeal or a superseding record; the original verdicts and case remain intact.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
