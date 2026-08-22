# WP-118 — Operational Readiness, On-Call and Runbook Simulation — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-118` |
| Work package | [`WP-118` — Operational Readiness, On-Call and Runbook Simulation](WP-118_operational_readiness.md) |
| Companion | [test procedures](WP-118_operational_readiness.tests.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Internal Audit / Service Owners** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-118` |

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

Each criterion names the test case in [`WP-118_operational_readiness.tests.md`](WP-118_operational_readiness.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every tier-1 service and incident class has a runbook, stale ones are flagged,
      and **dead links are detected on schedule** rather than during an incident.
- [ ] The rota covers every hour and **the escalation chain terminates in a
      reachable person**, or the gap is declared. Paging and escalation are both
      **measured**.
- [ ] **Both a tabletop and a live simulation are run**, and signing off on a
      tabletop alone is refused. A tabletop tests whether people know what to do; a
      simulation tests whether the procedure survives contact with the system.
- [ ] Break-glass requires **two distinct approvers**, is time-limited, opens an
      incident and creates a reconciliation. **Under a single operator it is refused
      or the gap is declared** — never a one-person path presented as two-person.
- [ ] **The Zotero reconciliation runbook is executed against a library edited since
      the divergence**, with no duplicates and no human edit overwritten. A clean
      fixture is **not accepted as evidence** — the edited library is the risky case.
- [ ] Tool, event, policy and model reconciliation runbooks are each executed and
      each records what diverged.
- [ ] **Every gap found becomes a finding with an owner**, and a rehearsal that found
      nothing is reviewed rather than counted as a clean pass.

## What this package cannot establish

> **Two-person break-glass is the control this laboratory structurally cannot
> satisfy.** The correct output is a declaration, not an implementation that
> pretends. ADR-001 has already modelled the form for reviewer independence, and it
> applies unchanged here: name what is missing, name who carries the residual risk,
> and give it an expiry.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **SRE Lead** is assigned accountable; an implementer is named; **Internal Audit / Service Owners** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-099` — WORM Audit Ledger and Independent Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-101` — Service Catalogue, SLOs and Alert/Runbook Binding — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-114` — Operations, DR and Restore Acceptance Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-115` — Full System Regression and Commissioning Dossier — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-116` — Resilience, Chaos and Failure-Injection Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-117` — Performance, Capacity and Load Commissioning — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Internal Audit / Service Owners** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-OPS-03` failing its effectiveness test.
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
