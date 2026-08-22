# WP-093 — Human Decision Queue and Evidence-Delta UI

## Package card

| Field | Value |
|---|---|
| Work package | `WP-093` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Governance Product Lead |
| Independent verifier | Project Decision Owner / Accessibility Reviewer |
| Hard dependencies | WP-004, WP-018, WP-038, WP-075, WP-077, WP-089, WP-091 |
| Related gates | G1,G8,G9 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The decision owner sees the options, what evidence changed, dissent, residual risk, policy, delegation, SLA and expiry, then issues a signed accept / reject / revise / defer decision.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/wp_038_human_updates_compensation.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-093-T01 | Write the decision inbox, filters, escalation and ownership views | Implementation owner | Commit / configuration / record reference |
| WP-093-T02 | Design the frozen evidence snapshot, delta and dissent summary | Implementation owner | Commit / configuration / record reference |
| WP-093-T03 | Apply the rationale rubric and required-field validation | Implementation owner | Commit / configuration / record reference |
| WP-093-T04 | Add delegation scope and expiry plus the non-delegable banner | Implementation owner | Commit / configuration / record reference |
| WP-093-T05 | Bind MFA re-authentication, signing and update idempotency | Implementation owner | Commit / configuration / record reference |
| WP-093-T06 | Write the decision history, revoke and supersede views | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Decision Queue UI`
- `Evidence-delta component`
- `Rationale forms`
- `Delegation/escalation views`
- `Decision audit export`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of a forged or expired approval
- Duplicate submission resolving to one decision
- SLA escalation
- An attempt at a non-delegable action
- The quality rule rejecting a generic rationale
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A timeout never becomes an automatic approval.
- [ ] Every decision carries the target, evidence and policy snapshot.
- [ ] Material dissent is never hidden from the decision maker.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A UI error is reconciled through the submission receipt; an uncertain decision is re-read rather than submitted a second time.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
