# WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release

## Package card

| Field | Value |
|---|---|
| Work package | `WP-107` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Engineering Lead |
| Independent verifier | Independent Technical Reviewer / Reproducer |
| Hard dependencies | WP-023, WP-024, WP-027, WP-032, WP-045, WP-047, WP-048, WP-049, WP-054, WP-059, WP-082, WP-086, WP-087, WP-089, WP-090, WP-096 |
| Related gates | Engineering,G5–G9 |
| Related controls | CTL-GOV-02, CTL-SUP-01 |
| Related acceptance scenarios | ACC-06, ACC-17, ACC-23 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

One standard and one critical code change pass through specification, reality check, isolated worktree, deterministic verification, blind review, reproduction, architecture gate and signed release.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/wp_024_ci_quality_gates.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-048 — Codex, OpenCode and Direct Worker Adapters](../05_MODEL_AGENT_TOOL/wp_048_codex_opencode_adapters.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/wp_054_gvisor_sandbox.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/wp_059_supply_chain_admission.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-107-T01 | Create the B/C risk fixtures and the technical specification | Implementation owner | Commit / configuration / record reference |
| WP-107-T02 | Open the plan reality check, protected-path check and the worktree | Implementation owner | Commit / configuration / record reference |
| WP-107-T03 | Run the agent implementation and CI verification | Implementation owner | Commit / configuration / record reference |
| WP-107-T04 | Perform blind and cross-family review of the frozen diff | Implementation owner | Commit / configuration / record reference |
| WP-107-T05 | Apply the reproducer and correction loop to HIGH/BLOCKER findings | Implementation owner | Commit / configuration / record reference |
| WP-107-T06 | Re-freeze, re-review, produce a signed build and take the human merge decision | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Engineering vertical dossier`
- `Frozen review packets`
- `Validated findings`
- `Signed OCI/release`
- `Merge DecisionRecord`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Protected-path denial
- Denial of worker self-approval
- Correction of a validated finding
- Denial of an unsigned release
- A migration rollback dry run
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The same target commit is preserved throughout all evidence.
- [ ] Only validated findings enter the correction loop.
- [ ] A critical change carries a different-family or human review and an explicit merge decision.
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

A failed release branch and worktree are quarantined; the production pointer stays on the previously signed artifact.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
