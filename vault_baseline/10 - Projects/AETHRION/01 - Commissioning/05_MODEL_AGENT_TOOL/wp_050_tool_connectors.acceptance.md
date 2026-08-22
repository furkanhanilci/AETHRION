---
title: "WP-050 — Initial Tool Connector Package — Acceptance Criteria"
aliases:
  - "WP-050 acceptance"
cssclasses:
  - aethrion-acceptance-criteria
type: acceptance-criteria
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-050_tool_connectors.acceptance.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/state/not-started
  - aethrion/acceptance-criteria
  - aethrion/authoring/authored
---

# WP-050 — Initial Tool Connector Package — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-050` |
| Work package | [`WP-050` — Initial Tool Connector Package](wp_050_tool_connectors.md) |
| Companion | [test procedures](wp_050_tool_connectors.tests.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Security / Connector Owners** — the independent verifier |
| Accountable owner | Tool Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-050` |

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

Each criterion names the test case in [`WP-050_tool_connectors.tests.md`](wp_050_tool_connectors.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every connector has a **least-privilege profile**, and the web connector is
      refused an off-allowlist host at both the connector and the egress proxy.
- [ ] Fetched content carrying an instruction changes no scope and is returned
      quarantined (`ACC-05`).
- [ ] Crossref reports *not found* distinctly from *clean* — an absent record is
      never a clean record.
- [ ] **The Zotero read connector refuses every non-`GET` method, driven through
      the whole sync flow.** This is the behavioural test finding **H3** has been
      open for, and it closes it.
- [ ] A write to a personal Zotero record is refused — `00_PROGRAM/01` invariant 5.
- [ ] **Proposing and applying are separate connectors**: a proposal changes
      nothing in Zotero, a human applies it as the actor, and applying through the
      read or candidate connector is refused (`ACC-02`).
- [ ] Git writes outside the allowed-path manifest are refused; object-store
      overwrites are refused; MLflow records references rather than copies.
- [ ] A notification exceeding a channel's data ceiling is refused.
- [ ] **All three compensation kinds are demonstrated**: reversible (branch
      deleted), invalidation (artifact marked, not deleted), and irreversible
      (recorded uncompensated with an owner, plus a correction). The third must be
      representable — pretending an irreversible effect was undone is the failure.
- [ ] Every connector passes the same broker contract suite.

## What this package cannot establish

> **Least privilege bounds reach, not judgement.** These connectors make it
> impossible for an agent to touch what it should not. They do nothing about an
> agent touching exactly what it should, in exactly the permitted way, for the
> wrong reason — which is why every external effect produces a `ToolReceipt` and
> why G6's review reads them.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **Tool Platform Lead** is assigned accountable; an implementer is named; **Security / Connector Owners** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-049` — Tool Registry and Tool Broker Core — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Security / Connector Owners** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-01` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-02` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-05` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.
- [ ] `ACC-35` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-LIT-03` failing its effectiveness test.
- [ ] `CTL-OPS-01` failing its effectiveness test.
- [ ] `CTL-SEC-01` failing its effectiveness test.

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
