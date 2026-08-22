---
title: "WP-049 — Tool Registry and Tool Broker Core — Acceptance Criteria"
aliases:
  - "WP-049 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/gate/engineering
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-049 — Tool Registry and Tool Broker Core — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-049` |
| Work package | [`WP-049` — Tool Registry and Tool Broker Core](wp_049_tool_registry_broker.md) |
| Companion | [test procedures](wp_049_tool_registry_broker.tests.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Security Architect / Internal Audit** — the independent verifier |
| Accountable owner | Tool Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-049` |

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

Each criterion names the test case in [`WP-049_tool_registry_broker.tests.md`](wp_049_tool_registry_broker.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every link in the chain refuses independently: unsigned definition, invalid
      schema, missing purpose, out-of-scope actor, data-class ceiling, policy
      denial — **six separate refusal transcripts**.
- [ ] **The same envelope key produces one effect**, including under concurrent
      submission; the duplicate returns the original receipt.
- [ ] Credentials reach a tool only as a **scoped, time-limited lease**. An expired
      lease is refused and a revoked lease stops an effect in flight.
- [ ] **No agent runtime holds a connector credential**, verified by scan. Agents
      produce intent; the broker performs the effect.
- [ ] **Tool output containing an instruction changes no scope** and is returned as
      data inside an explicit boundary marker — `ACC-05` and ADR-003, in the one
      place the boundary is actually crossed.
- [ ] Secret-shaped strings are redacted before the output reaches an agent
      context, and every output carries provenance naming tool, target, time and
      lease.
- [ ] Every external effect produces a `ToolReceipt`, and a task's full set of
      external effects **reconstructs from receipts alone**.

## What this package cannot establish

> **The boundary marker is a mitigation, not the boundary.** ADR-003 is explicit:
> a detector is defence in depth, never the boundary itself. Wrapping untrusted
> output in a marker reduces the chance a model treats it as instruction; the
> *actual* control is that the model's authority is fixed by the `TaskContract`
> and cannot be widened by anything it reads. Any package that starts relying on
> the marker rather than on the scope has inverted the design.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Tool Platform Lead** is assigned accountable; an implementer is named; **Security Architect / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-011` — Identity and End-to-End Correlation Standard — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-015` — Event Envelope, Subject and Schema Taxonomy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-028` — NATS JetStream and Transactional Outbox Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-046` — LangGraph Bounded Cognition Runtime — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security Architect / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-05` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-12` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
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
- [ ] `CTL-SEC-01` failing its effectiveness test.
- [ ] `CTL-SEC-03` failing its effectiveness test.

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
