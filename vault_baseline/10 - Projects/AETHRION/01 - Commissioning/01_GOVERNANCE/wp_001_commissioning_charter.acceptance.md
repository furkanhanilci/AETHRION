---
title: "WP-001 — Commissioning Charter and Programme Authority — Acceptance Criteria"
aliases:
  - "WP-001 acceptance"
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/01_GOVERNANCE/WP-001_commissioning_charter.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/s
  - aethrion/gate/program
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-001 — Commissioning Charter and Programme Authority — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-001` |
| Work package | [`WP-001` — Commissioning Charter and Programme Authority](wp_001_commissioning_charter.md) |
| Companion | [test procedures](wp_001_commissioning_charter.tests.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Internal Audit / Commissioning Board** — the independent verifier |
| Accountable owner | Executive Sponsor |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-001` |

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

Each criterion names the test case in [`WP-001_commissioning_charter.tests.md`](wp_001_commissioning_charter.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The charter is **signed** by the Executive Sponsor, and the signature is
      bound to a specific document revision digest.
- [ ] Cutover authority and abort authority are held by **named individuals**, not
      by bodies, and both are recorded as **non-delegable**.
- [ ] Every authority reference in the charter resolves to a role in the catalogue
      or to an explicitly declared gap — zero unresolved references.
- [ ] All three tabletops (authority collision, abort, vacancy) resolve **from the
      charter text alone**, and each record quotes the clause that resolved it.
- [ ] Every KPI carries a measurement method and an owner; every anti-metric
      carries the failure it detects and a review threshold.
- [ ] The anti-metric set includes, at minimum, G10 reversal rate,
      acceptance-despite-adversarial-rejection rate, and median human decision time.
- [ ] Stop/pivot conditions each name an observable and a numeric threshold.
- [ ] The budget envelope states a hard limit and the fail-closed behaviour at it.
- [ ] An `Executive DecisionRecord` records the approval, its date, its scope and
      what it does **not** authorise.
- [ ] Where the independent verifier does not exist, the gap is **declared** in the
      charter with a residual-risk owner and an expiry — not left implicit.

## What this package cannot establish

> **Deliberately not measurable here.** Whether the outcome is the right outcome.
> The charter fixes what the programme is for; nothing in this package can tell
> you it should be for that. That judgement belongs to the sponsor and is
> re-opened by the stop/pivot conditions, which is why they must be falsifiable.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Executive Sponsor** is assigned accountable; an implementer is named; **Internal Audit / Commissioning Board** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] No hard dependency; this package can start once the programme is authorised.
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit / Commissioning Board** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

**No acceptance scenario names this package.** It can reach `ACCEPTED` on its own evidence and cannot reach `COMMISSIONED` through a scenario, because there is none to pass. `00_PROGRAM/11`'s completeness rule calls this an incomplete entry rather than a shorter one.

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
- [ ] `CTL-GOV-01` failing its effectiveness test.

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
