# WP-024 — CI Foundation and Deterministic Quality Gates — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-024` |
| Work package | [`WP-024` — CI Foundation and Deterministic Quality Gates](WP-024_ci_quality_gates.md) |
| Companion | [test procedures](WP-024_ci_quality_gates.tests.md) |
| Workstream | `03_FOUNDATION` |
| Approval authority | **Mechanical Verifier** — the independent verifier |
| Accountable owner | Engineering Productivity Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-024` |

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

Each criterion names the test case in [`WP-024_ci_quality_gates.tests.md`](WP-024_ci_quality_gates.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A pipeline runs on every push and pins **one** target revision across all
      jobs.
- [ ] Cheap checks report before expensive ones, demonstrated by timing on a run
      containing both a formatting error and a failing integration test.
- [ ] **Six gates each fail a build at least once**: lint, type, schema
      compatibility, policy, architecture/import direction, and security advisory.
      A gate that has never failed has not been shown to be a gate.
- [ ] A passing run emits `verification-summary.json` that validates against its
      schema and names the target revision.
- [ ] That artifact is accepted directly by `evidence_manifest.py` as a subject —
      **no hand transcription** anywhere in the acceptance path.
- [ ] Built images carry signed provenance that verifies.
- [ ] Every quarantined test has an owner and a clearing deadline, and **passing
      the deadline fails the build** rather than continuing to skip.
- [ ] The number of quarantined tests is published as a run metric.
- [ ] BVC-01 is retired or explicitly superseded once this platform runs — a
      temporary control that outlives its retirement package is a permanent one.

## What this package cannot establish

> **What this package closes and what it does not.** It closes finding **H5** and,
> with it, the qualifier on every other acceptance criterion in this plan. It does
> **not** make the checks correct: `AGENTS.md` §11 states that all of them are
> internal consistency and would hold for a corpus describing a system that does
> not work. CI turns "someone ran this" into "this cannot regress"; it does not
> turn either into "this is true".

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Engineering Productivity Lead** is assigned accountable; an implementer is named; **Mechanical Verifier** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-022` — Repository Topology and Code Ownership — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-023` — Git, Worktree and Protected-Path Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Mechanical Verifier** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-SUP-01` failing its effectiveness test.
- [ ] `CTL-OPS-02` failing its effectiveness test.

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
