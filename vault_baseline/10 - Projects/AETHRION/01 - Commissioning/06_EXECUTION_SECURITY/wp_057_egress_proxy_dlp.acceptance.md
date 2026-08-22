---
title: "WP-057 — Default-Deny Egress Proxy, DLP and Allowlist — Acceptance Criteria"
aliases:
  - "WP-057 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-057 — Default-Deny Egress Proxy, DLP and Allowlist — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-057` |
| Work package | [`WP-057` — Default-Deny Egress Proxy, DLP and Allowlist](wp_057_egress_proxy_dlp.md) |
| Companion | [test procedures](wp_057_egress_proxy_dlp.tests.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Red Team / Privacy Owner** — the independent verifier |
| Accountable owner | Network Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-057` |

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

Each criterion names the test case in [`WP-057_egress_proxy_dlp.tests.md`](wp_057_egress_proxy_dlp.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The proxy cannot be bypassed, and arbitrary DNS resolution is refused.
- [ ] The allowlist is enforced on **all five dimensions** — domain, IP, method,
      purpose, data class — with a separate denial demonstrated for each. A domain
      allowlist alone permits exfiltration to a permitted host.
- [ ] Response size and MIME constraints each refuse.
- [ ] Secret and PII detectors block and alert **within otherwise allowed
      requests**.
- [ ] **A planted canary is detected and blocked**, and the detector suite **fails
      when the canary is removed** rather than reporting clean. A detector that has
      never fired is indistinguishable from one that does not work.
- [ ] Sustained volume to an **allowed** destination raises an alert against a
      baseline — the categorical controls cannot see slow exfiltration through a
      permitted route.
- [ ] Every permitted request logs destination, method, purpose, data class, size,
      identity and outcome.
- [ ] **The emergency deny path has been exercised**: all egress stops within the
      declared time, the action is audited, and restoring leaves a complete
      incident record. An emergency control first used in an emergency is untested.
- [ ] Egress exceptions with no approver, and with an expired approval, are both
      refused.

## What this package cannot establish

> **Detectors are the weakest layer and must be described as such.** Regexes for
> secrets and PII catch known shapes; an encoder, a cipher or an unusual encoding
> defeats them. The real boundary is the data class on the request and the ceiling
> on the destination — ADR-003's rule that a detector is defence in depth, never
> the boundary. Any later package that treats a clean DLP scan as authorisation has
> misread this one.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Network Security Lead** is assigned accountable; an implementer is named; **Red Team / Privacy Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-051` — Four Trust Zones and Network Segmentation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-055` — SPIFFE/SPIRE Workload Identity and Vault — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-056` — OPA Policy Platform and Bundle Distribution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Red Team / Privacy Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-16` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-32` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-SEC-02` failing its effectiveness test.
- [ ] `CTL-OBS-02` failing its effectiveness test.

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
