# WP-056 — OPA Policy Platform and Bundle Distribution

## Package card

| Field | Value |
|---|---|
| Work package | `WP-056` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Policy Platform Lead |
| Independent verifier | Safety / Security / Internal Audit |
| Hard dependencies | WP-005, WP-006, WP-007, WP-009, WP-016, WP-020, WP-021, WP-055 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-02, CTL-DAT-02, CTL-SEC-02 |
| Related acceptance scenarios | ACC-06, ACC-18, ACC-24, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-056_opa_policy_platform.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-056_opa_policy_platform.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Role, data, tool, model, environment, gate, exception and budget decisions are distributed to every enforcement point as tested, signed, explainable OPA bundles.


## Analysis
### What this package actually decides

That policy is code with tests, a build and a rollback — not configuration someone
edits. Every enforcement point in the system consumes a **signed bundle**, and the
bundle is versioned so that a decision can be replayed against the exact rules
that produced it (WP-016).

### Module boundaries are what keep `PR-02` at bay (T01)

*Policy becomes combinatorial*, rated critical, early signal *large cross-tables,
unexplainable decisions*. The counter is structural: separate modules per domain —
role, data, tool, model, environment, gate, exception, budget — with explicit
precedence between them rather than one rule set that considers everything at once.

`00_PROGRAM/01` already states the shape: *separate profiles, precedence and
hard-promotion rules*, never a combinatorial cross-product.

### Negative and property tests are the deliverable (T03)

A policy suite of positive tests proves the allowed paths work. It says nothing
about whether anything is denied. Every rule needs a case that **must be denied**,
and property tests are what catch the combination nobody enumerated.

`AGENTS.md`'s own rule applies with full force: a check that cannot fail proves
nothing.

### Shadow evaluation is how a policy change is made safely (T06)

New bundle evaluated alongside the live one, decisions compared, differences
reported — **without enforcing**. This is the same pattern as WP-042's `SHADOW`
model state, and for the same reason: a policy change that flips a decision
somewhere nobody expected is discovered in a report rather than in an incident.

Coverage telemetry answers the complementary question: which rules have never
fired? A rule that has never fired is either dead or protecting something that has
never been attempted.

### Decision-log redaction and WORM export (T05)

Decision logs contain the inputs — which include the content being judged. They
are simultaneously the audit trail and a data-class hazard, and they need
redaction on the way in and immutability once written.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/WP-009_control_exception_catalog.md) | `Control Catalog` · `ExceptionPolicy` · `NonWaivableBlocker registry` · `Control-test mapping` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |

### Full prerequisite closure

**41 of 141 packages (29%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-055` |

### What acceptance of this package releases

- **Directly unblocked:** 11 — `WP-057` · `WP-058` · `WP-059` · `WP-060` · `WP-061` · `WP-075` · `WP-097` · `WP-099` · `WP-101` · `WP-102` · `WP-123`
- **Transitively reachable:** **77 of 141 packages (55%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **25** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Policy Platform Lead |
| Independent verifier | Safety / Security / Internal Audit |
| Gates touched | `G0–G10` · `Platform` |
| Controls | `CTL-GOV-02` · `CTL-DAT-02` · `CTL-SEC-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-18 — D3 Data to a Public Provider](../12_ACCEPTANCE_SCENARIOS/ACC-18_d3_public_route.md) | Critical | No public provider call is made; a secure or local eligible route is chosen if one exists, otherwise the task is `BLOCKED`, and an audit record is written. |
| [ACC-24 — Policy Bundle Rollback](../12_ACCEPTANCE_SCENARIOS/ACC-24_policy_bundle_rollback.md) | High | The previous bundle is restored atomically, decision logs and bundle digests are preserved, open tasks are re-evaluated and no unsafe temporary allow is granted. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/ACC-26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/WP-009_control_exception_catalog.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Control Catalog` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `ExceptionPolicy` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `NonWaivableBlocker registry` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Control-test mapping` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Policy Platform Lead** carries the acceptance decision; **Safety / Security / Internal Audit** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-056-T01 | Establish the policy repository and its module boundaries | Implementation owner | Commit / configuration / record reference |
| WP-056-T02 | Apply the input-document and decision API standard | Implementation owner | Commit / configuration / record reference |
| WP-056-T03 | Write the unit, negative and property test harness | Implementation owner | Commit / configuration / record reference |
| WP-056-T04 | Establish signed bundle build, promotion and rollback | Implementation owner | Commit / configuration / record reference |
| WP-056-T05 | Bind decision-log redaction and WORM export | Implementation owner | Commit / configuration / record reference |
| WP-056-T06 | Add shadow evaluation with drift and coverage telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `OPA platform`
- `Policy bundle v1`
- `Policy test suite`
- `Bundle promotion pipeline`
- `Decision log pipeline`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-056_opa_policy_platform.tests.md`](WP-056_opa_policy_platform.tests.md).

- Denial of a D3 route, a T4 action and a self-review
- Denial under an expired exception
- Bundle rollback
- Fail-closed behaviour on unknown input
- A shadow decision diff
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-056_opa_policy_platform.acceptance.md`](WP-056_opa_policy_platform.acceptance.md), together with what this package still cannot establish.

- [ ] An untested or unsigned bundle cannot reach production.
- [ ] Every decision carries a rule ID, a bundle digest and its obligations.
- [ ] If policy is unavailable, critical actions fail closed.
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

- A control not exercised by a negative test is an assumption.
- Default-allow egress anywhere in the chain nullifies every other isolation control.
- Sandbox escape is tested by attempting it, not by reading the configuration.

## Rollback / compensation

A faulty bundle returns atomically to the previous signed version; decision history is preserved and an impact scan is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
