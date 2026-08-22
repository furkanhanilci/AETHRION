# WP-110 — Research and Literature Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-110` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Citation Auditor / Assurance |
| Hard dependencies | WP-103, WP-104, WP-105, WP-106, WP-108, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-EPI-01, CTL-LIT-01, CTL-GOV-02 |
| Related acceptance scenarios | ACC-01..ACC-08 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The human seed, agent write-back, duplicate, retraction, injection, self-approval, order bias and counter-test scenarios close with complete evidence.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze](../10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.md), [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_vertical_slice_run_claim.md), [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.md), [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.md), [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-110-T01 | Reset the ACC-01 to ACC-08 fixtures | Implementation owner | Commit / configuration / record reference |
| WP-110-T02 | Execute a controlled, non-parallel run on the same release candidate | Implementation owner | Commit / configuration / record reference |
| WP-110-T03 | Verify the expected Registry, Zotero, Ledger, Gate and Audit outcomes | Implementation owner | Commit / configuration / record reference |
| WP-110-T04 | Run critical-finding triage, reproduction and correction | Implementation owner | Commit / configuration / record reference |
| WP-110-T05 | Produce the research acceptance dossier and obtain owner sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ACC-01–08 results`
- `Research acceptance dossier`
- `Finding/disposition records`
- `Owner sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- ACC-01 through ACC-08
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] All eight scenarios PASS.
- [ ] No open critical or high research finding remains.
- [ ] The manifest, claim, reviewer and source integrity queries all complete.
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

A failure blocks cutover; fixture state is cleaned and, after correction, the regression set — not only the affected scenario — is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
