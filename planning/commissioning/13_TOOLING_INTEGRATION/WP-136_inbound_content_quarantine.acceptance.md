# WP-136 — Inbound Content Quarantine and Channel Allowlist — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-136` |
| Work package | [`WP-136` — Inbound Content Quarantine and Channel Allowlist](WP-136_inbound_content_quarantine.md) |
| Companion | [test procedures](WP-136_inbound_content_quarantine.tests.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Safety & Governance Owner** — the independent verifier |
| Accountable owner | Content Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-136` |

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

Each criterion names the test case in [`WP-136_inbound_content_quarantine.tests.md`](WP-136_inbound_content_quarantine.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Channels and senders are allowlisted; unlisted sources are **not processed**.
- [ ] SPF, DKIM, DMARC and bot identity are all verified and recorded — **and
      verification is not authorisation**: a verified message containing an
      instruction still has none extracted.
- [ ] Macro-bearing documents, embedded scripts and malformed containers are each
      refused or quarantined, and attachments parse **inside an ephemeral cell**.
- [ ] **All inbound content is wrapped in `<untrusted-external-content>`
      unconditionally.** Making the tagging depend on a detector's verdict is
      refused — a detector that decides when to tag will eventually decide not to.
- [ ] **No instruction is extracted from inbound content**: an action, a wider scope,
      a credential change and an apparent claim of operator authority all leave the
      agent's scope unchanged, and each attempt is audited.
- [ ] Legitimate **values** are usable as data with provenance recorded.
- [ ] Inbound content lands in quarantine and reaches a **terminal disposition** —
      promoted with a decision or rejected with a reason.
- [ ] Inbound rate and size limits both refuse.

## What this package cannot establish

> **Tagging is a mitigation; the scope is the boundary.** Wrapping inbound content
> reduces the chance a model treats it as instruction. The guarantee is that the
> agent's authority is fixed by its `TaskContract` and cannot be widened by anything
> it reads — TC-12 exists because that property must hold even when the tagging
> fails, and ADR-003 says so directly: a detector is defence in depth, never the
> boundary.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Content Security Lead** is assigned accountable; an implementer is named; **Safety & Governance Owner** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-058` — Untrusted Content Quarantine and Prompt-Injection Firewall — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-131` — Notification Broker Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-132` — Channel Registry and Data-Class Ceiling — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Safety & Governance Owner** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-05` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-44` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
