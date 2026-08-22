# WP-109 — Forty Acceptance Scenario Registry and Harness

## Package card

| Field | Value |
|---|---|
| Work package | `WP-109` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Commissioning Board |
| Hard dependencies | WP-002, WP-009, WP-020, WP-024, WP-040, WP-060, WP-090, WP-099, WP-102, WP-103, WP-104, WP-105, WP-106, WP-107, WP-108 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-02, CTL-SEC-04 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

ACC-01 to ACC-40 become runnable — automatically or with a witnessed manual step — in a versioned test registry carrying Given/When/Then, fixtures, expected events and invariants, evidence, owner, severity and cleanup.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/wp_024_ci_quality_gates.md), [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-102 — Vertical Slice 1 — Intake through Protocol Freeze](../10_INTEGRATION_CUTOVER/wp_102_vertical_slice_intake_protocol.md), [WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze](../10_INTEGRATION_CUTOVER/wp_103_vertical_slice_literature.md), [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/wp_104_vertical_slice_run_claim.md), [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/wp_105_vertical_slice_review_repro.md), [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/wp_106_vertical_slice_decision_publish_monitor.md), [WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release](../10_INTEGRATION_CUTOVER/wp_107_engineering_vertical_slice.md), [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/wp_108_retraction_drift_vertical_slice.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-109-T01 | Transfer the 40 scenarios into a machine-readable registry | Implementation owner | Commit / configuration / record reference |
| WP-109-T02 | Write the fixture, environment and data-seeding standard | Implementation owner | Commit / configuration / record reference |
| WP-109-T03 | Add the expected canonical, event, audit and policy assertions | Implementation owner | Commit / configuration / record reference |
| WP-109-T04 | Build the test runner, evidence capture and result signing | Implementation owner | Commit / configuration / record reference |
| WP-109-T05 | Write the witness protocol for manual human and DR steps | Implementation owner | Commit / configuration / record reference |
| WP-109-T06 | Add the retry, flakiness, skip/waiver and cleanup rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Acceptance Registry`
- `Scenario runner`
- `Fixture catalog`
- `Evidence capture/signing`
- `Result dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Registry schema validation
- A known-pass and a known-fail scenario
- Enforcement of the same release-candidate digest
- A critical `SKIP` never counting as a pass
- Cleanup isolation between scenarios
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every scenario carries an owner and an immutable result.
- [ ] All results come from the same release candidate, policy and schema bundle.
- [ ] A critical scenario can never be skipped or waived.
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

Harness releases are verified with a canary fixture; results from a broken harness are `INVALIDATED` and every affected scenario is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
