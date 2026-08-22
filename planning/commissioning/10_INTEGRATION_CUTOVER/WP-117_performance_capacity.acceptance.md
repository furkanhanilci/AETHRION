# WP-117 — Performance, Capacity and Load Commissioning — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-117` |
| Work package | [`WP-117` — Performance, Capacity and Load Commissioning](WP-117_performance_capacity.md) |
| Companion | [test procedures](WP-117_performance_capacity.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **SRE / FinOps / Assurance** — the independent verifier |
| Accountable owner | Capacity Engineering Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-117` |

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

Each criterion names the test case in [`WP-117_performance_capacity.tests.md`](WP-117_performance_capacity.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] The workload envelope is **approved before measurement**, states its **fan-out
      assumption**, and results from an unapproved envelope are not accepted as
      evidence.
- [ ] Services, queues and the end-to-end journey all meet their targets at the
      envelope, with latency reported as **distributions**.
- [ ] **The binding constraint is identified and named** rather than the test simply
      passing.
- [ ] **Exceeding the envelope produces backpressure** — queue and signal — not
      failure and not silent degradation. **Any path that degrades quality under
      load is a finding**: quality degradation is the failure mode research cannot
      tolerate.
- [ ] Fan-out is measured with council review and sweeps active, and exceeding the
      declared cap is refused before dispatch.
- [ ] **The assurance queue does not grow without bound at envelope throughput**, and
      assurance is neither starved nor preempted under saturation. `PR-04` is a
      capacity property before it is a process one.
- [ ] **The human attention quota is not exceeded at envelope throughput** — and if
      it is, **the envelope is reduced**, because human decision capacity is a hard
      quota rather than a throughput target.
- [ ] The cost curve is produced and the envelope's full-load cost is stated;
      headroom is a number against each binding constraint, and the plan names the
      next constraint and at what growth it binds.

## What this package cannot establish

> **The binding constraint is a person, and load testing cannot move it.** Every
> other bottleneck here can be scaled with money. The human decision quota cannot,
> and `00_PROGRAM/08` is explicit that there is no express-review mode. A capacity
> plan whose growth path requires more decisions per day than a person can consider
> properly has planned a failure, and reducing the envelope is the correct response
> rather than raising the quota.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Capacity Engineering Lead** is assigned accountable; an implementer is named; **SRE / FinOps / Assurance** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-053` — Kueue Queue, Quota and Priority Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-096` — OpenTelemetry End-to-End Correlation Spine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-098` — Grafana and the Six Operational Graphs — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-100` — Cost Ledger, Budget Envelopes and FinOps — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-101` — Service Catalogue, SLOs and Alert/Runbook Binding — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-115` — Full System Regression and Commissioning Dossier — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **SRE / FinOps / Assurance** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-CST-01` failing its effectiveness test.
- [ ] `CTL-OBS-01` failing its effectiveness test.

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
