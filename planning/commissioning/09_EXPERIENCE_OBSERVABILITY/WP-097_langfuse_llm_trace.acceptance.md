# WP-097 — Langfuse Model/Agent Tracing and Prompt Governance — Acceptance Criteria

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `AC-WP-097` |
| Work package | [`WP-097` — Langfuse Model/Agent Tracing and Prompt Governance](WP-097_langfuse_llm_trace.md) |
| Companion | [test procedures](WP-097_langfuse_llm_trace.tests.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Privacy/Security / Eval Office** — the independent verifier |
| Accountable owner | AI Observability Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-097` |

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

Each criterion names the test case in [`WP-097_langfuse_llm_trace.tests.md`](WP-097_langfuse_llm_trace.tests.md) that decides it. A criterion with no test case cannot be verified, and a test case that decides no criterion is not part of acceptance.

<!-- /generated:howto -->

## Package-specific acceptance criteria

- [ ] Every trace maps to its AIRL project, workflow, run and task, with correct
      task → node → model → tool nesting.
- [ ] **Every model call names a registered prompt and template version**; an
      unregistered prompt is refused or flagged unpinnable.
- [ ] **No request asks for private chain-of-thought and none is stored**, verified
      by auditing both the requests and the store. A **rationale summary** is stored
      instead — reviewable, and what `AgentResult.assumptions` already requires.
- [ ] **Redaction happens at ingestion**: a secret or personal data in a prompt
      never lands. Read-time redaction is refused, because the unredacted value
      would still be stored.
- [ ] D3 traces route to D3 retention and do not appear in the general project;
      sensitive tool arguments are redacted per their schema.
- [ ] Token counts, latency and cost are recorded and correlated.
- [ ] **The trace store identity cannot read the evaluation golden set** —
      contamination runs both ways (`PR-15`).
- [ ] Traces expire at their data-class retention without human action, and an
      export round-trips with correlation intact.

## What this package cannot establish

> **A rationale summary is what the model says it did, not what it did.** It is
> reviewable and it is not a mechanism trace — a model can produce a plausible
> summary of reasoning it did not perform, which is the same plausibility failure
> the whole repository is built against. Its value is that a reviewer can check the
> stated reasons against the evidence; its limit is that agreement between summary
> and output proves nothing about the process between them.

## Programme-level gates

<!-- generated:dod — produced by scripts/make_package_companions.py; do not edit inside this block -->

From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this package. Every line is a condition on **evidence**, not on effort.

### Definition of Ready

- [ ] The package purpose and its single delivery boundary are written.
- [ ] Out-of-scope items are written down.
- [ ] **AI Observability Lead** is assigned accountable; an implementer is named; **Privacy/Security / Eval Office** is assigned verifier and is **independent of the producer** under WP-007's profile.
- [ ] `WP-006` — ExecutionProfile and Route Policy — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-013` — Project, Task, Role and Skill Contract Schemas — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-020` — Schema Registry, Compatibility and Contract SDK — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-025` — PostgreSQL HA and Registry Data Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-026` — Content-Addressed Object Store and WORM — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-041` — LiteLLM Model Gateway Foundation — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-046` — LangGraph Bounded Cognition Runtime — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-047` — Role and Skill Registries, and the Task Compiler — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-055` — SPIFFE/SPIRE Workload Identity and Vault — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-056` — OPA Policy Platform and Bundle Distribution — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-057` — Default-Deny Egress Proxy, DLP and Allowlist — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `WP-096` — OpenTelemetry End-to-End Correlation Spine — is `ACCEPTED` (not `TECH_COMPLETE`).
- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified — all four, with no `UNKNOWN`.
- [ ] Acceptance criteria name **a number, a threshold or a command**. `00_PROGRAM/05` states that the generic template criteria are not measurable in the sense meant here; refinement is where that is fixed.
- [ ] Migration, rollback or compensation behaviour is defined.
- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.

### Definition of Done — package acceptance

- [ ] Every acceptance criterion below passed **on the same target revision**.
- [ ] Test results are bound to artifact hashes and an environment manifest.
- [ ] **Privacy/Security / Eval Office** verified **independently of the producer** and did not see the producer's working trace.
- [ ] Security, data and policy **negative** tests passed.
- [ ] Contract compatibility and downstream consumer tests are green.
- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry a named owner and an expiry.
- [ ] Rollback or compensation was exercised at least once, and the result is referenced.
- [ ] Working evidence exists via a dashboard, alert or audit query — not only via a test log.
- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` list is present.

### Definition of Commissioned

An `ACCEPTED` package is still not production-ready. Every scenario below must pass **on the same release candidate**:

- [ ] `ACC-32` passes. A `SKIPPED` scenario on a Critical row does not count as a pass.

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
- [ ] `CTL-OBS-02` failing its effectiveness test.
- [ ] `CTL-DAT-03` failing its effectiveness test.

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
