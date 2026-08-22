---
title: "WP-041 — LiteLLM Model Gateway Foundation — Acceptance Criteria"
aliases:
  - "WP-041 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g2-g7
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-041 — LiteLLM Model Gateway Foundation — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-041` |
| Work package | [`WP-041` — LiteLLM Model Gateway Foundation](wp_041_litellm_gateway.md) |
| Companion | [test procedures](wp_041_litellm_gateway.tests.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Security / FinOps / SRE** — the independent verifier |
| Accountable owner | Model Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-041` |

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

Each criterion names the test case in [`WP-041_litellm_gateway.tests.md`](wp_041_litellm_gateway.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **No component outside the gateway holds a provider credential**, verified by
      a scan, and a direct provider call from an agent runtime is blocked by egress
      policy.
- [ ] Every call carries project, role and workload identity; an unauthenticated
      call is refused.
- [ ] D3 content is refused to a provider not permitted for that class, and
      residency constraints route only to permitted regions.
- [ ] Rate limiting throttles cleanly and the circuit breaker opens on repeated
      failure.
- [ ] **Fallback selects only models admitted for the role.** With no admitted
      fallback available the call **fails closed** — it never silently reaches an
      unqualified model, because that would falsify the run manifest.
- [ ] Secrets and personal data in a prompt do **not** appear in usage or cost
      events. Redaction happens in the gateway, not in each caller.
- [ ] Every completed call emits a cost event with the correlation identifier and
      token counts.
- [ ] A hosted-model call records a **capability fingerprint plus full I/O**, and
      does not claim a snapshot pin it does not have.
- [ ] The cache never returns a response for a different prompt, and D3+ content is
      never served from cache.

## What this package cannot establish

> **The gateway cannot make a model call reproducible.** For hosted models the
> strongest available record is a capability fingerprint and a complete
> input/output log — `00_PROGRAM/01` states the constraint against invariant 4.
> Deterministic reproduction requires local open-weight models with a weight-file
> hash, which is a WP-044 admission decision and an operating cost, not something
> this gateway can supply.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Model Platform Lead** is assigned accountable; an implementer is named; **Security / FinOps / SRE** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security / FinOps / SRE** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-DAT-02` failing its effectiveness test.
- [ ] `CTL-CST-01` failing its effectiveness test.
- [ ] `CTL-MOD-01` failing its effectiveness test.

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
