---
title: "WP-052 — Kubernetes Cluster and Node Pool Baseline — Acceptance Criteria"
aliases:
  - "WP-052 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-052 — Kubernetes Cluster and Node Pool Baseline — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-052` |
| Work package | [`WP-052` — Kubernetes Cluster and Node Pool Baseline](wp_052_kubernetes_cluster.md) |
| Companion | [test procedures](wp_052_kubernetes_cluster.tests.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **SRE / Security** — the independent verifier |
| Accountable owner | Platform Infrastructure Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-052` |

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

Each criterion names the test case in [`WP-052_kubernetes_cluster.tests.md`](wp_052_kubernetes_cluster.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Five node pools exist, and the control plane is replicated across failure
      domains.
- [ ] **Scheduling onto the untrusted pool without an explicit toleration is
      refused**, and no service workload is ever co-resident with an untrusted one.
- [ ] A workload without a D3 profile cannot reach the secure pool.
- [ ] Privileged containers, host mounts and host networking are each refused
      separately.
- [ ] Namespace quotas refuse at admission.
- [ ] **The assurance capacity reserve admits assurance work while the cluster is
      full of research work.** A laboratory that can be starved out of checking
      itself has an availability problem that presents as a quality problem.
- [ ] D3+ volumes are encrypted and on the declared storage class; exposure outside
      the declared ingress is refused.
- [ ] **The upgrade runbook has been rehearsed in staging** and its gaps recorded —
      an unrehearsed upgrade happens under pressure or does not happen at all.
- [ ] A cluster restore brings back a known workload; a node drain loses nothing.

## What this package cannot establish

> **Pool separation is a blast-radius control, not a containment guarantee.** It
> assumes the kernel boundary holds; WP-054's gVisor layer exists because that
> assumption is the one an attacker attacks. Separation means a successful escape
> lands somewhere with nothing worth reaching — which is a smaller claim than
> containment and a more defensible one.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Platform Infrastructure Lead** is assigned accountable; an implementer is named; **SRE / Security** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-027` — Git, OCI Registry and Build Provenance Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-051` — Four Trust Zones and Network Segmentation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **SRE / Security** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-27` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-33` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OPS-03` failing its effectiveness test.

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
