# WP-138 — External Records and Persistent Identifiers — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-138` |
| Work package | [`WP-138` — External Records and Persistent Identifiers](WP-138_external_records_persistent_identifiers.md) |
| Companion | [test procedures](WP-138_external_records_persistent_identifiers.tests.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Project Decision Owner** — the independent verifier |
| Accountable owner | Data Steward |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-138` |

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

Each criterion names the test case in [`WP-138_external_records_persistent_identifiers.tests.md`](WP-138_external_records_persistent_identifiers.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] **A protocol is pre-registered externally before any run**, carrying an
      external timestamp that a sceptical reader can verify. Registering after data
      exists is **refused as pre-registration** and permitted only as a declared
      exploratory registration. The embargo option preserves the timestamp without
      forcing disclosure.
- [ ] **A Zenodo deposit issues a DOI that resolves externally**, and the deposited
      digests match the local package.
- [ ] **Author identity binds to ORCID** and resolves outside the system.
- [ ] `CITATION.cff`, CodeMeta and **Croissant** are all generated and valid, and the
      deposit is navigable by tooling that knows nothing of this system.
- [ ] **A deposit requires the operator to type `SUBMIT`.** Agent-initiated and
      automated deposits are refused — a deposit is irreversible and permanently
      public, and this friction is deliberate in a system where agents initiate most
      actions.
- [ ] Content failing the licence or privacy release checks is refused.
- [ ] A superseding deposit issues a new DOI, **leaves the prior version resolvable**,
      and links the two.
- [ ] A failed deposit is recorded as **not deposited**, with nothing partially
      public.

## What this package cannot establish

> **This is the first package that produces evidence a sceptic can check.**
> Everything before it is verifiable only by someone who trusts the operator's
> infrastructure — `AGENTS.md` §11's *internal consistency* limit, and
> `airl-interim-v0.1`'s own `limitations` list. An external registration and a DOI
> move a narrow but real set of claims outside that boundary: **the protocol existed
> at this time**, and **this package is publicly retrievable**. They say nothing
> about whether the research is correct.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Data Steward** is assigned accountable; an implementer is named; **Project Decision Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-090` — PublicationPackage, RO-Crate and Provenance Export — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-131` — Notification Broker Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Project Decision Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-30` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-45` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-EPI-01` failing its effectiveness test.

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
