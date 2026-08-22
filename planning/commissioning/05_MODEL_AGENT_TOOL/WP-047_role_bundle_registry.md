# WP-047 — Role and **Skill** Registries, and the Task Compiler

## Package card

| Field | Value |
|---|---|
| Work package | `WP-047` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Agent Platform Lead |
| Independent verifier | Governance / Eval Office |
| Hard dependencies | WP-003, WP-007, WP-013, WP-020, WP-042, WP-045, WP-046 |
| Related gates | G1–G7 |
| Related controls | CTL-GOV-02, CTL-MOD-01 |
| Related acceptance scenarios | ACC-46, ACC-47, ACC-48, ACC-51, plus those assigned during the relevant vertical slice |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A role's mandate, prompt/policy, input/output schema, allowed tools, context and evaluation and acceptance conditions are compiled into a versioned `RoleBundle`.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/WP-003_role_catalog_raci.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-047-T01 | Build the `RoleBundle` schema and its Git registry | Implementation owner | Commit / configuration / record reference |
| WP-047-T02 | Write the `RoleContract` → runtime prompt/tool/context compiler | Implementation owner | Commit / configuration / record reference |
| WP-047-T03 | Create the initial bundles for planner, scout, extractor, methodologist, coder, reviewer, reproducer and curator | Implementation owner | Commit / configuration / record reference |
| WP-047-T04 | Bind the context budget and frozen-package policy | Implementation owner | Commit / configuration / record reference |
| WP-047-T05 | Add bundle signature, admission and evaluation references | Implementation owner | Commit / configuration / record reference |
| WP-047-T06 | Establish deprecation and migration management | Implementation owner | Commit / configuration / record reference |
| WP-047-T07 | Build the **Skill Registry**: discovery, the Agent Skills format contract, and `scripts/validate_skills.py` as an admission gate | Implementation owner | Registry + rejected non-conformant specimen |
| WP-047-T08 | Implement **trigger resolution** — classification fields → `skills_required` — with a recorded `skill_selection_reason` | Implementation owner | Resolver + trigger test matrix |
| WP-047-T09 | Implement **version and dependency resolution** across `airl.requires_skills`, including conflict refusal | Implementation owner | Resolver + a refused conflicting bundle |
| WP-047-T10 | Compute and record `skill_bundle_hash`; bind it into `TaskContract` and the evidence chain | Implementation owner | Hash reproduced from a stored bundle |
| WP-047-T11 | Enforce the **two-family policy**: engineering, scientific-research and shared, selected from `work_domain` — never chosen freely by the agent | Implementation owner | Policy tests both ways |
| WP-047-T12 | Track **upstream provenance**: `airl.derived_from` + `airl.upstream_commit`, and flag derived skills when upstream moves | Implementation owner | Impact report for a simulated upstream change |

## Mandatory deliverables

- `Role Bundle Registry`
- **`Skill Registry`** with format admission, version and dependency resolution
- **`Task Compiler`** producing `RoleBundle` + `SkillBundle` + `ToolBundle` + `ContextBundle`
- **`skill_bundle_hash` computation** bound into `TaskContract`
- **Upstream provenance impact report**
- `Core role bundles`
- `Bundle conformance tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

### The compiler this package must produce

```
RoleContract  +  TaskContract  +  classification fields
        │
        ▼
   Task Compiler ── skill policy ──► skill_selection_reason
        │
        ├─► RoleBundle      who
        ├─► SkillBundle     how          → skill_bundle_hash
        ├─► ToolBundle      with what
        └─► ContextBundle   knowing what
        │
        ▼
   runtime (WP-046 / WP-048)
```

**The agent does not choose its own skills.** Selection is derived by policy
from the classification fields and recorded with its reason; an agent that
loads a different set than the one compiled produces a divergence finding.

## Test and verification plan

- Forbidden tools excluded at compile time
- A compile failure when acceptance criteria are missing
- A negative test for reviewer contamination by the producer's trace
- Bundle signature validation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A role is not a model name.
- [ ] Every bundle carries explicit inputs, outputs and non-goals.
- [ ] The reviewer bundle enforces blind context and its independence obligations.
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

A faulty bundle is revoked; the registry pointer returns to the previous signed version and open tasks receive an impact assessment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
