# WP-048 — Codex, OpenCode and Direct Worker Adapters

## Package card

| Field | Value |
|---|---|
| Work package | `WP-048` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Agent Runtime Lead |
| Independent verifier | Security / Eval Office |
| Hard dependencies | WP-023, WP-027, WP-046, WP-047 |
| Related gates | G5,Engineering |
| Related controls | CTL-SEC-03, CTL-SEC-04 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Different agent runtimes become interchangeable adapters that all satisfy the same `TaskContract`, isolation, tool, result, audit and cancellation contract.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-048-T01 | Write the adapter interface and its lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-048-T02 | Implement the Codex non-interactive task adapter | Implementation owner | Commit / configuration / record reference |
| WP-048-T03 | Implement the OpenCode headless/server adapter | Implementation owner | Commit / configuration / record reference |
| WP-048-T04 | Implement the direct/local queue worker adapter | Implementation owner | Commit / configuration / record reference |
| WP-048-T05 | Bind worktree, sandbox and tool credentials | Implementation owner | Commit / configuration / record reference |
| WP-048-T06 | Add structured results, tracing, cancellation and failure normalisation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Runtime adapter SDK`
- `Codex adapter`
- `OpenCode adapter`
- `Direct worker adapter`
- `Conformance report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- The same canonical task producing schema-compatible results across all three adapters
- Cancellation and timeout normalisation
- A permission and path negative test
- Recovery from runtime session loss
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A runtime session is never AIRL workflow state.
- [ ] No adapter receives a raw provider secret.
- [ ] Results conform to the canonical `AgentResult` and artifact contract.
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

- A model alias is not a pinned identity; results obtained under an alias are not reproducible.
- An agent holding a credential defeats the entire broker design.
- Fallback routes are the least tested and most consequential path in this workstream.

## Rollback / compensation

An adapter can be disabled individually; the task is dispatched to another eligible adapter under a new execution lease.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
