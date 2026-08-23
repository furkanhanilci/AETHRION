---
title: "WP-111 — Reliability, Event and FinOps Acceptance Package — Acceptance Criteria"
aliases:
  - "WP-111 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-111_reliability_finops_acceptance.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-111 — Reliability, Event and FinOps Acceptance Package — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-111` |
| Work package | [`WP-111` — Reliability, Event and FinOps Acceptance Package](wp_111_reliability_finops_acceptance.md) |
| Companion | [test procedures](wp_111_reliability_finops_acceptance.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **FinOps / Control Plane Reviewer** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-111` |

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

Each criterion names the test case in [`WP-111_reliability_finops_acceptance.tests.md`](wp_111_reliability_finops_acceptance.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] All scenarios bind to **one release candidate**.
- [ ] **At the hard budget limit no new expensive work opens and the workflow pauses
      without losing state**, and resuming repeats nothing — invariant 9, measured.
- [ ] A provider outage fails over to an **admitted** profile or **fails closed**.
      It never silently reaches an unqualified model, because that would falsify the
      run manifest.
- [ ] **Exactly one business effect** survives duplicate delivery, worker loss,
      DLQ repair and retry after partial failure — invariant 2, demonstrated four
      ways.
- [ ] A workflow deployment against open executions produces **no nondeterminism
      error**.
- [ ] Preemption checkpoints and resumes; preempting a workload with no checkpoint
      contract is refused.
- [ ] **A tool call that succeeds externally and fails to return is reconciled**, and
      where it cannot be resolved the effect is **recorded as uncertain with an
      owner** — not reported as either completed or failed.
- [ ] **Workflow-state RPO is measured as 0** and the number recorded; integrity
      queries hold after every fault.
- [ ] Invoice variance opens a case **with an owner**; an unassigned variance is
      refused.
- [ ] **Every alert in these scenarios reached its owner with a measured response
      time**, and every relevant runbook was **executed** with its gaps recorded.

## What this package cannot establish

> **These are the faults that were anticipated.** Ten scenarios drawn from the risk
> register, run under controlled injection. The outage that actually takes the
> system down will plausibly be a combination none of them models — which is why
> WP-116's chaos work runs unscripted and why `00_PROGRAM/07` closes a risk on a
> control-effectiveness test with a re-evaluation date rather than on a single pass.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **SRE Lead** is assigned accountable; an implementer is named; **FinOps / Control Plane Reviewer** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-040` — Workflow Replay, Versioning and Failure Test Suite — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-053` — Kueue Queue, Quota and Priority Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-083` — ExperimentBatch and Staged Execution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-100` — Cost Ledger, Budget Envelopes and FinOps — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-109` — Acceptance Scenario Registry and Harness — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **FinOps / Control Plane Reviewer** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-09` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-10` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-11` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-12` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-13` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-14` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-29` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-33` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-34` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-35` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-01` failing its effectiveness test.
- [ ] `CTL-OPS-02` failing its effectiveness test.
- [ ] `CTL-CST-01` failing its effectiveness test.
- [ ] `CTL-CST-02` failing its effectiveness test.

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
