---
title: "WP-158 — Benchmark Firewall and External Evaluation Qualification — Acceptance Criteria"
aliases:
  - "WP-158 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-158_benchmark_firewall.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g6
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-158 — Benchmark Firewall and External Evaluation Qualification — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-158` |
| Work package | [`WP-158` — Benchmark Firewall and External Evaluation Qualification](wp_158_benchmark_firewall.md) |
| Companion | [test procedures](wp_158_benchmark_firewall.tests.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Assurance Lead / Research Director** — the independent verifier |
| Accountable owner | Eval Office |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-158` |

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

Each criterion names the test case in [`WP-158_benchmark_firewall.tests.md`](wp_158_benchmark_firewall.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A benchmark policy is frozen before the run and cannot be modified during it.
- [ ] Gold answers, private rubrics, hidden tests and grader prompts are
      unreachable from the agent environment under the supported threat model.
- [ ] A run that reached benchmark material is labelled and **never reported as a
      clean score**, and cannot be silently rerun for a clean one.
- [ ] A run under restricted retrieval is reported clean — the scanner
      discriminates rather than flagging everything.
- [ ] An ambiguous hit routes to `REVIEW_REQUIRED` and a human, not to an
      automatic verdict.
- [ ] The efficiency comparison runs against the **naive fully-connected cohort**;
      substituting a single-agent arm is refused.
- [ ] Labels travel with scores into the release dossier.

## What this package cannot establish

> **What this package cannot establish.** That an unlabelled run was clean. The
> scanner looks for known benchmark identifiers and material; a paraphrased
> question or an answer reached through an unrecognised route passes it. The
> honest reading of a clean label is *no known contamination was detected under
> this policy* — which is why the policy, the allowed domains and the log are
> reported alongside the score rather than summarised into it.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Eval Office** is assigned accountable; an implementer is named; **Assurance Lead / Research Director** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-019` — Run, Environment and Reproduction Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-043` — Role-Based Model and Skill Evaluation, and Golden Set Management — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-057` — Default-Deny Egress Proxy, DLP and Allowlist — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-081` — Protocol, Analysis, Baseline and Falsification Registry — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-149` — Sparse Communication Topology and the Scientific Blackboard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Assurance Lead / Research Director** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-086` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-118` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-04` failing its effectiveness test.

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
