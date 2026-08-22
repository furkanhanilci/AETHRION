---
title: "WP-039 — Event Consumer, DLQ and Safe Replay Framework — Acceptance Criteria"
aliases:
  - "WP-039 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/04_CONTROL_EVENT/WP-039_event_consumer_dlq_replay.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/04-control-event
  - aethrion/wave/w3
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-039 — Event Consumer, DLQ and Safe Replay Framework — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-039` |
| Work package | [`WP-039` — Event Consumer, DLQ and Safe Replay Framework](wp_039_event_consumer_dlq_replay.md) |
| Companion | [test procedures](wp_039_event_consumer_dlq_replay.tests.md) |
| Workstream | `04_CONTROL_EVENT` |
| Approval authority | **SRE / Security** — the independent verifier |
| Accountable owner | Event Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-039` |

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

Each criterion names the test case in [`WP-039_event_consumer_dlq_replay.tests.md`](wp_039_event_consumer_dlq_replay.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Idempotency, ACK ordering and DLQ handling live in the **SDK**, not in each
      handler.
- [ ] A duplicate delivery produces one business effect.
- [ ] **The canonical commit happens before the ACK**: a crash between them causes
      redelivery, not loss. The reversed ordering is **caught by the conformance
      suite**.
- [ ] Poison events reach the DLQ with reason, attempt count and original
      causation; retries follow the declared backoff.
- [ ] DLQ repair forms no loop and processes exactly once.
- [ ] `replay_mode=dry-run` changes **nothing**; `replay_mode=rebuild` updates
      projections and performs **no external effect**. Both demonstrated
      separately, and a replay with no mode is refused.
- [ ] Consumer lag and DLQ depth alert on a stall — the failure mode is silence,
      so the alert is the only signal.
- [ ] **The conformance suite fails a consumer that skips a guarantee**, naming
      which one. A suite that every consumer passes on the first try has not been
      shown to test anything.

## What this package cannot establish

> **The SDK cannot make a handler correct.** It guarantees each event is delivered
> at least once and applied at most once. Whether the handler's *effect* is the
> right effect is the consuming package's problem, and no amount of delivery
> discipline detects a correctly-once-applied wrong write.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Event Platform Lead** is assigned accountable; an implementer is named; **SRE / Security** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-015` — Event Envelope, Subject and Schema Taxonomy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-028` — NATS JetStream and Transactional Outbox Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-032` — ProjectLifecycle Workflow Skeleton — is `ACCEPTED` (not `TECH_COMPLETE`).
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

- [ ] `ACC-12` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-34` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
