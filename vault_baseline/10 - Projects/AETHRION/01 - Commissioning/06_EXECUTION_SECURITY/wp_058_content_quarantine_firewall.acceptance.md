---
title: "WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall — Acceptance Criteria"
aliases:
  - "WP-058 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-058` |
| Work package | [`WP-058` — Untrusted Content Quarantine and Prompt-Injection Firewall](wp_058_content_quarantine_firewall.md) |
| Companion | [test procedures](wp_058_content_quarantine_firewall.tests.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Red Team / Knowledge Lead** — the independent verifier |
| Accountable owner | Content Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-058` |

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

Each criterion names the test case in [`WP-058_content_quarantine_firewall.tests.md`](wp_058_content_quarantine_firewall.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] External content lands in **quarantine**, and a canonical-plane identity
      cannot read it.
- [ ] MIME mismatch, malware, archive bombs and oversize content are each refused
      separately; licence-restricted content falls back to hash-only.
- [ ] **Parsing runs inside an ephemeral cell**, and a parser exploit is contained
      and destroyed with it.
- [ ] Text, metadata, links and scripts are returned as **separate channels**.
      A parser returning one blob has merged what the model should read with what
      an attacker wrote.
- [ ] **Active content is never executed** and is returned inert.
- [ ] **`ACC-05`: an injected instruction in a PDF abstract is tagged untrusted,
      wrapped in an explicit boundary marker, and leaves the agent's tool scope
      unchanged.** This closes the gap the Bridge's MCP server documents against
      itself today.
- [ ] The extraction tool profile is T0/T1 read-only; a write or network attempt is
      refused.
- [ ] Extracted text carries provenance: source, representation hash, parser and
      parser version.
- [ ] Every quarantined item reaches a **terminal disposition** — promoted with a
      decision or rejected with a reason. Nothing is left pending.

## What this package cannot establish

> **The marker is not the control.** ADR-003: *a detector is defence in depth,
> never the boundary.* Wrapping untrusted text reduces the chance a model treats it
> as instruction; the guarantee is that the agent's authority is fixed by its
> `TaskContract` and cannot be widened by anything it reads. TC-13 exists because
> that is the property that has to hold even when the tagging fails.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Content Security Lead** is assigned accountable; an implementer is named; **Red Team / Knowledge Lead** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-014` — Artifact, Dataset and Immutable Manifest Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-017` — Source Registry and Literature Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-050` — Initial Tool Connector Package — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-051` — Four Trust Zones and Network Segmentation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-054` — gVisor Sandbox and Execution Cell Lifecycle — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-056` — Policy Decision Point and Bundle Distribution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-057` — Default-Deny Egress Proxy, DLP and Allowlist — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Red Team / Knowledge Lead** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-05` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-SEC-01` failing its effectiveness test.
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
