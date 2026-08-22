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

## Purpose and expected outcome

Empirical, methodological and interpretive claims move between `PROVISIONAL`, `SUPPORTED`, `CONTESTED`, `CHALLENGED` and `REPLICATED` under evidence, validity, conflict, reproduction and dependency blockers.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

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

- `BLOCKED` on broken provenance
- A strong source failing to compensate for a weak method
- `CONTESTED` on contradictory evidence
- State promotion on a reproduction pass
- Propagation of an upstream supersession
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

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
