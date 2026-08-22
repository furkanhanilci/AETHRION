# WP-055 — SPIFFE/SPIRE Workload Identity and Vault — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-055` |
| Work package | [`WP-055` — SPIFFE/SPIRE Workload Identity and Vault](WP-055_spiffe_vault_identity.md) |
| Companion | [test procedures](WP-055_spiffe_vault_identity.tests.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Security / Internal Audit** — the independent verifier |
| Accountable owner | Identity Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-055` |

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

Each criterion names the test case in [`WP-055_spiffe_vault_identity.tests.md`](WP-055_spiffe_vault_identity.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] One trust domain, attested agents, and every workload identity matching its
      registration selectors.
- [ ] **An SVID copied into a different pod does not work.** Identity is
      non-transferable, which is what every later independence claim rests on.
- [ ] An unregistered workload receives no identity and can call nothing.
- [ ] **No long-lived shared secret exists in any service**, verified by scan.
- [ ] Credentials are issued as **short-lived, purpose-bound leases**: using one
      for another purpose is refused, using one past its TTL is refused, and
      revocation takes effect immediately.
- [ ] Rotation happens without restarting workloads.
- [ ] Human authentication requires MFA, and **the human identity is bound to a G8
      decision at the moment it is taken**. A decision attributed to the wrong
      actor invalidates the independence it was meant to establish.
- [ ] Break-glass requires **two approvers**, or the single-operator gap is
      **declared** with a residual-risk owner and an expiry — the same discipline
      ADR-001 applied to R3. Quietly implementing a one-person path and calling it
      two-person fails.
- [ ] Break-glass opens an incident, is time-limited, and creates a reconciliation
      task.

## What this package cannot establish

> **Two-person control is the one requirement a solo laboratory cannot satisfy.**
> The correct outcome here is a declaration, not an implementation that pretends.
> ADR-001 already models the form: name what is missing, name who carries the
> residual risk, and give it an expiry. A break-glass that requires two approvals
> from the same person is worse than one that requires one, because it looks like
> a control.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Identity Platform Lead** is assigned accountable; an implementer is named; **Security / Internal Audit** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-004` — Human Decision, SLA, Delegation and Escalation Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-016` — PolicyDecision, Control and Exception Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-021` — Development, Staging and Production Environment Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-031` — Temporal Platform, Namespaces and HA — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-051` — Four Trust Zones and Network Segmentation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-052` — Kubernetes Cluster and Node Pool Baseline — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security / Internal Audit** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-25` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-26` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-SEC-03` failing its effectiveness test.
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
