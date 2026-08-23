---
title: "WP-115 — Full System Regression and Commissioning Dossier — Acceptance Criteria"
aliases:
  - "WP-115 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-115_full_system_regression.acceptance.md"
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

# WP-115 — Full System Regression and Commissioning Dossier — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-115` |
| Work package | [`WP-115` — Full System Regression and Commissioning Dossier](wp_115_full_system_regression.md) |
| Companion | [test procedures](wp_115_full_system_regression.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board** — the independent verifier |
| Accountable owner | Platform Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-115` |

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

Each criterion names the test case in [`WP-115_full_system_regression.tests.md`](wp_115_full_system_regression.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The RC is frozen with **every bundle version recorded**, and **every scenario
      result binds to that one RC**. A result from a different revision is refused —
      mixed-revision evidence is explicitly not accepted.
- [ ] **All 51 `PRE_GO_LIVE` scenarios are accounted for**, not the 46 the task list
      names, and a missing one is detected as a gap.
- [ ] All seven evidence classes consolidate and verify; altering one fails
      verification by name.
- [ ] **Open Critical findings refuse consolidation**, and **the five non-waivable
      classes cannot be waived at all** — security, identity, evidence, reproduction,
      data. Five separate refusals.
- [ ] A High accepted as residual risk requires board acceptance, an owner and an
      expiry, and **an expired acceptance becomes an open finding again**.
- [ ] **The scorecard includes the uncomfortable numbers**: manual-witness count,
      skip count, flake rate and monitoring coverage fraction — not only KPIs and
      SLOs. A scorecard omitting them is refused.
- [ ] **The board can reach `BLOCKED`**, and the verdict records its reasons. A
      review that can only produce `READY` is a formality.
- [ ] The dossier signature covers every consolidated artifact by digest, and a
      post-signature change fails verification.

## What this package cannot establish

> **The first honest verdict is `BLOCKED`.** As `docs/STATUS.md` records: no package
> is `ACCEPTED`, no scenario has been run, R3 is blocked under ADR-001, and CI does
> not exist. The dossier's value at that point is not that it authorises go-live —
> it is that it states, with evidence, exactly what is missing. A dossier that
> produced `READY` from the current state would be the most dangerous artifact this
> programme could generate.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Platform Assurance Lead** is assigned accountable; an implementer is named; **Commissioning Board** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-110` — Research and Literature Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-111` — Reliability, Event and FinOps Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-112` — Security and Privacy Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-113` — Evidence, Reproduction and Publication Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-114` — Operations, DR and Restore Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Commissioning Board** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-01` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-02` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-03` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-04` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-05` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-06` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-07` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-08` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-09` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-10` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-11` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-12` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-13` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-14` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-15` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-16` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-17` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-18` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-19` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-20` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-21` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-22` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-23` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-24` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-25` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-26` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-27` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-28` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-29` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-30` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-31` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-32` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-33` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-34` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-35` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-36` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-37` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-38` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-39` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-40` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-41` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-42` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-43` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-44` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-45` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-46` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-47` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-48` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-49` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-50` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-51` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-52` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-53` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-54` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-55` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-56` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-57` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-58` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-59` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-60` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-61` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-62` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-63` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-64` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-65` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-66` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-67` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-68` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-69` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-70` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-71` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-72` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-74` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-75` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-76` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-77` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-78` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-79` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-081` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-082` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-083` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-084` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-085` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-086` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-087` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-088` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-089` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-090` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-091` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-092` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-093` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-094` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-095` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-096` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-097` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-098` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-099` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-100` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-101` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-102` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-103` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-104` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-105` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-106` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-107` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-108` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-109` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-110` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-111` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-112` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-113` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-114` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-115` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-116` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-117` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-118` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-119` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-120` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `All controls` failing its effectiveness test.

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
