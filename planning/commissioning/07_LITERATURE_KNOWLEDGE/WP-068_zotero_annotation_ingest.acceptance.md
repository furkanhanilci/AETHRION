# WP-068 — Zotero Annotation → EvidenceCandidate Pipeline — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-068` |
| Work package | [`WP-068` — Zotero Annotation → EvidenceCandidate Pipeline](WP-068_zotero_annotation_ingest.md) |
| Companion | [test procedures](WP-068_zotero_annotation_ingest.tests.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Citation Auditor / Knowledge Curator** — the independent verifier |
| Accountable owner | Evidence Intake Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-068` |

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

Each criterion names the test case in [`WP-068_zotero_annotation_ingest.tests.md`](WP-068_zotero_annotation_ingest.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] A second annotation sync reads nothing; all six annotation fields are
      normalised and recorded.
- [ ] **Every observation binds to a `SourceRepresentation` hash**, not to the work.
      An annotation on an unhashed attachment is refused or held — an unlocatable
      annotation is not an observation.
- [ ] A replaced, differently paginated attachment produces a **mismatch state**,
      distinct from both *resolves* and *wrong*.
- [ ] **Citing an `AnnotationObservation` directly in a claim is refused.** A
      highlight is evidence of what a human thought, not evidence for a proposition
      — the promotion through the evidence contract is the whole boundary.
- [ ] Promotion records the promoting actor and the reason.
- [ ] The same passage highlighted twice, and identical annotations on two copies
      of one paper, both resolve to **one** observation.
- [ ] Editing an annotation versions it and retains the prior text.
- [ ] **Deleting an annotation that supports a claim opens an impact case.** The
      claim does not become silently unsupported — the same loop WP-037 runs for
      retractions, applied to a researcher's change of mind.
- [ ] Every observation names the human who made it.

## What this package cannot establish

> **An observation is evidence about a reader, not about the world.** It records
> that a person marked a passage as interesting. Whether the passage supports the
> claim it is eventually attached to is a judgement made at promotion and reviewed
> at G6 — and `evidence-before-claim` exists because that judgement is the one a
> confident model makes badly.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Evidence Intake Lead** is assigned accountable; an implementer is named; **Citation Auditor / Knowledge Curator** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-058` — Untrusted Content Quarantine and Prompt-Injection Firewall — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-061` — Canonical Source Registry Service — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-063` — Source Representation, Licence and Status Monitoring — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-065` — Personal Zotero Seed Ingest Pipeline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-067` — Zotero Two-Way Sync and Reconciliation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Citation Auditor / Knowledge Curator** verified **independently of the producer** and did not see the producer's working trace.
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
- [ ] `CTL-EPI-01` failing its effectiveness test.
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
