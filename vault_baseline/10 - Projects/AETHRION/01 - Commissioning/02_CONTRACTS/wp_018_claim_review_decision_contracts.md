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

## Purpose and expected outcome

Claim versioning, evidence spans, dependencies, assessments, review verdicts, disagreement and human-decision semantics become publishable contracts.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

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

- An immutable claim-version test
- State tests for `RELOCATED`, `AMBIGUOUS` and `NEEDS_REANCHOR`
- A gate fixture for an unresolved critical verdict
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

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
