# WP-062 — Source Identity Resolution, Deduplication and Merge — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-062` |
| Work package | [`WP-062` — Source Identity Resolution, Deduplication and Merge](WP-062_source_identity_resolver.md) |
| Companion | [test procedures](WP-062_source_identity_resolver.tests.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / Citation Auditor** — the independent verifier |
| Accountable owner | Source Resolver Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-062` |

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

Each criterion names the test case in [`WP-062_source_identity_resolver.tests.md`](WP-062_source_identity_resolver.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every identifier form normalises to canonical form, and Crossref lookups go
      **through the broker** rather than direct.
- [ ] **Every match decision names the features and the rule that produced it.**
      No opaque score decides a merge — `PR-02`'s early signal is unexplainable
      decisions, and a curator cannot review one.
- [ ] Two distinct works sharing a title are **not merged** (`ACC-03`); they queue
      as a `ConflictCase`.
- [ ] A preprint and its published version are **linked as versions, not merged**.
- [ ] Ambiguous pairs reach the curator queue with both candidates and the reason.
- [ ] **A split resolves prior citations to a disambiguation state**, never to an
      arbitrarily chosen side.
- [ ] Precision, recall and the **false-merge rate are reported as measured numbers**
      against a held-out known-item set, and **the auto-merge threshold is derived
      from that rate** rather than chosen.
- [ ] Duplicate queue depth, auto-merge rate and curator decisions are observable.

## What this package cannot establish

> **The asymmetry must stay in the design.** A false merge combines two works and
> silently corrupts every claim citing either; a false split wastes a curator's
> time. They are not symmetric errors and the threshold must not be tuned as if
> they were. If a single number has to be reported about this package, it is the
> **false-merge rate** — and the honest target for it is zero, with everything
> uncertain going to a human.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Source Resolver Lead** is assigned accountable; an implementer is named; **Knowledge Curator / Citation Auditor** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-050` — Initial Tool Connector Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-058` — Untrusted Content Quarantine and Prompt-Injection Firewall — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-061` — Canonical Source Registry Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Knowledge Curator / Citation Auditor** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-03` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-28` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-01` failing its effectiveness test.

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
