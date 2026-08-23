---
title: "WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release — Acceptance Criteria"
aliases:
  - "WP-107 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-107_engineering_vertical_slice.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/engineering
  - aethrion/gate/g5-g9
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-107` |
| Work package | [`WP-107` — Engineering Vertical Slice — Spec, Worktree, Signed Release](wp_107_engineering_vertical_slice.md) |
| Companion | [test procedures](wp_107_engineering_vertical_slice.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Independent Technical Reviewer / Reproducer** — the independent verifier |
| Accountable owner | Engineering Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-107` |

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

Each criterion names the test case in [`WP-107_engineering_vertical_slice.tests.md`](wp_107_engineering_vertical_slice.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Both a B-class and a C-class change run, and their paths **visibly diverge** in
      review depth, reproduction requirement and approval. If they do not, the risk
      classification is decoration.
- [ ] The specification names a command or a threshold; an untestable one is refused.
- [ ] **The plan reality check catches a reference to something that does not
      exist**, before implementation rather than during review.
- [ ] A change touching a protected path is refused **at the worktree boundary**,
      and a task description requesting wider scope does not widen it.
- [ ] **Four CI gates each fail a build**: lint, type, schema, security.
- [ ] **The frozen diff shows zero producer-trace artifacts**, and a seeded
      authorship signal in commit structure or comments is **detected** — a diff
      leaks authorship in ways prose does not.
- [ ] **The correction loop re-freezes**: a HIGH finding produces a correction, a
      new frozen package and a re-review. Merging with an open BLOCKER is refused.
- [ ] A finding is independently reproduced and then confirmed or dismissed **with a
      reason**.
- [ ] A forbidden import is refused by the architecture gate.
- [ ] The release is digest-pinned and signed with verifying provenance, and the
      **human merge decision records a rationale, requires MFA and names residual
      risk**.

## What this package cannot establish

> **The engineering path is governed; it is not thereby safe.** These controls bound
> what an agent may touch, ensure a human decides the merge, and make the review
> independent. They do nothing about a correct-looking change that is wrong in a
> way no reviewer noticed and no test covers — which is the same plausibility
> failure the research path faces, and why `PR-12`'s *false rigor* applies to code
> as much as to claims.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Engineering Lead** is assigned accountable; an implementer is named; **Independent Technical Reviewer / Reproducer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-023` — Git, Worktree and Protected-Path Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-024` — CI Foundation and Deterministic Quality Gates — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-027` — Git, OCI Registry and Build Provenance Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-032` — ProjectLifecycle Workflow Skeleton — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-045` — Policy Router and Minimum-Sufficient Model Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-047` — Role and Skill Registries, and the Task Compiler — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-048` — Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-054` — gVisor Sandbox and Execution Cell Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-059` — Supply-Chain Admission, Sigstore and SLSA Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-082` — Run Registry and MLflow Lineage Integration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-086` — Frozen and Blind Review Package Builder — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-087` — Mechanical Verification Engine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-089` — DisagreementCase and Evidence-Weighted Arbitration — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-090` — PublicationPackage, RO-Crate and Provenance Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-096` — OpenTelemetry End-to-End Correlation Spine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-154` — Engineering Discipline and Specification Conformance — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Independent Technical Reviewer / Reproducer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-17` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-23` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-GOV-02` failing its effectiveness test.
- [ ] `CTL-SUP-01` failing its effectiveness test.

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
