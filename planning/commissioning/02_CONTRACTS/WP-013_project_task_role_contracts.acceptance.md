# WP-013 — Project, Task, Role and Skill Contract Schemas — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-013` |
| Work package | [`WP-013` — Project, Task, Role and Skill Contract Schemas](WP-013_project_task_role_contracts.md) |
| Companion | [test procedures](WP-013_project_task_role_contracts.tests.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Governance Lead** — the independent verifier |
| Accountable owner | Control Plane Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-013` |

<!-- /generated:identity -->

## How to read a criterion

<!-- generated:howto — produced by scripts/make_package_companions.py; do not edit inside this block -->

A criterion belongs here only if it can **fail**. `00_PROGRAM/05` lists what is not evidence, and the first entry is an implementer's free-text declaration of success.

| A criterion states | Not |
|---|---|
| a number, a threshold or a command | "works correctly" |
| the observation that would falsify it | "has been reviewed" |
| the test case that decides it | "all tests pass" |
| what it does **not** establish | silence about its own limits |

Each criterion names the test case in [`WP-013_project_task_role_contracts.tests.md`](WP-013_project_task_role_contracts.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All five contracts validate, and every canonical contract is **free of
      provider-specific fields** by both a mechanical scan and an independent
      semantic review.
- [ ] `TaskContract` carries `skill_bundle_hash`, `work_domain`, `research_mode`
      and `execution_path` as mandatory fields.
- [ ] `skill_bundle_hash` reaches the **evidence chain**, and two runs under
      different skill bundles are distinguishable in it.
- [ ] Comparing results produced under different skill bundles is refused or
      flagged non-comparable.
- [ ] An unset classification field fails **closed** — most restrictive path, and
      flagged.
- [ ] `AgentResult.gaps` and `.assumptions` are non-empty on real tasks where gaps
      exist. The measured non-empty rate across at least ten tasks is reported;
      **a rate of zero fails**.
- [ ] `RoleBinding` rejects a producer/verifier collision through a **separation
      constraint**, and legally accepts multiple roles when no constraint is
      violated.
- [ ] Compatibility is enforced mechanically: an added optional field is
      compatible, a changed field type is not, and republishing a registered
      version is rejected.
- [ ] Every published contract example validates against its own schema.

## What this package cannot establish

> **The field most likely to become decoration.** `AgentResult.assumptions`. It
> costs a model nothing to return an empty list, and an empty list reads as
> "no assumptions" rather than "not implemented". Measuring the non-empty rate is
> the only defence, and it belongs in the acceptance evidence rather than in a
> dashboard nobody opens.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Control Plane Lead** is assigned accountable; an implementer is named; **Governance Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-003` — Role Catalogue and RACI Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-004` — Human Decision, SLA, Delegation and Escalation Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-005` — Research Risk and Assurance Profile — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-007` — IndependenceProfile and Separation-of-Duties Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Governance Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

**No acceptance scenario names this package.** It can reach `ACCEPTED` on its own evidence and cannot reach `COMMISSIONED` through a scenario, because there is none to pass. `00_PROGRAM/11`'s completeness rule calls this an incomplete entry rather than a shorter one.

<!-- /generated:dod -->

## Non-waivable items

<!-- generated:nonwaivable — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/07_programme_risk_register.md`: *critical security, identity, evidence, reproduction and data blockers cannot be lowered by a numeric total.* The score exists for prioritisation; it is not a waiver mechanism.

The following cannot be waived on this package under any residual-risk acceptance:

- [ ] Identity and correlation failures.
- [ ] Data routing across a trust-zone boundary without policy.
- [ ] Artifact integrity or lineage loss.
- [ ] A reviewer independence violation.
- [ ] A missing or unverifiable `EvidenceManifest`.
- [ ] `CTL-GOV-01` failing its effectiveness test.
- [ ] `CTL-DAT-02` failing its effectiveness test.

> A package with an open item above is `BLOCKED`, not `ACCEPTED with conditions`. The distinction is the reason the list exists.

<!-- /generated:nonwaivable -->

## Verifier's decision

Completed by the independent verifier, not by the producer. **Issuance is not acceptance** — a package that has produced evidence and has not been verified is `TECH_COMPLETE`.

| Field | Value |
|---|---|
| Verifier | |
| Independence profile applied | R1 / R2 declared-partial / R3 — see ADR-001 |
| Dimensions **not** met | *(an R2 profile that lists only its strengths is not a declaration)* |
| Target revision verified | |
| Decision | `PENDING` / `ACCEPTED` / `REJECTED` |
| Date | |
| Conditions and their expiry | |
