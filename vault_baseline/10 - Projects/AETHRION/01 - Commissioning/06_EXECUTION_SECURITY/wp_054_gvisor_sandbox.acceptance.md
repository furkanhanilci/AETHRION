---
title: "WP-054 — gVisor Sandbox and Execution Cell Lifecycle — Acceptance Criteria"
aliases:
  - "WP-054 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/engineering
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-054 — gVisor Sandbox and Execution Cell Lifecycle — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-054` |
| Work package | [`WP-054` — gVisor Sandbox and Execution Cell Lifecycle](wp_054_gvisor_sandbox.md) |
| Companion | [test procedures](wp_054_gvisor_sandbox.tests.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Red Team / SRE** — the independent verifier |
| Accountable owner | Execution Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-054` |

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

Each criterion names the test case in [`WP-054_gvisor_sandbox.tests.md`](wp_054_gvisor_sandbox.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every execution pod runs under the declared RuntimeClass and seccomp profile,
      and an elevated capability request is refused.
- [ ] **Attestation happens before execution**: unsigned images, images with no
      SBOM, and mutable-tag references are each refused **before any process
      starts**.
- [ ] A second task sees nothing from the first; reads and writes outside the
      declared scope are refused.
- [ ] CPU, memory, wall-clock and process limits each terminate or refuse — a run
      truncated by a limit is **marked**, never silently shortened.
- [ ] Direct network access is denied; only the egress proxy path exists.
- [ ] Artifacts are hashed before teardown and land in **quarantine**, not the
      canonical store. Producing an artifact is not the same as trusting it.
- [ ] **The cell is destroyed unconditionally** — on success, on failure, on
      timeout, and when the capture step itself errored. All four demonstrated.
- [ ] An escape indicator alerts **and takes a forensic snapshot before teardown**,
      containing enough to investigate: process list, filesystem diff, network
      attempts.

## What this package cannot establish

> **Layered, not guaranteed.** gVisor reduces the kernel surface a workload can
> reach; it does not eliminate it, and no sandbox vendor claims otherwise. The
> design assumes this boundary can fail, which is why WP-052 puts untrusted work
> on nodes with nothing worth reaching and why WP-060 attacks it on a schedule.
> A package that claimed containment rather than *reduction plus detection plus
> blast-radius limitation* would be overstating what a sandbox is.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Execution Security Lead** is assigned accountable; an implementer is named; **Red Team / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-027` — Git, OCI Registry and Build Provenance Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-052` — Kubernetes Cluster and Node Pool Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-053` — Kueue Queue, Quota and Priority Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Red Team / SRE** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-15` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-17` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-54` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-55` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-SEC-04` failing its effectiveness test.
- [ ] `CTL-SEC-05` failing its effectiveness test.

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
