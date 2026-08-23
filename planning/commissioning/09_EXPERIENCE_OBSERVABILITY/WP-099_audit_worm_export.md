# WP-099 — WORM Audit Ledger and Independent Export

## Package card

| Field | Value |
|---|---|
| Work package | `WP-099` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Internal Audit Platform Lead |
| Independent verifier | Independent Auditor / Security |
| Hard dependencies | WP-011, WP-015, WP-016, WP-025, WP-026, WP-028, WP-049, WP-055, WP-056, WP-059, WP-075, WP-082, WP-096 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-01, CTL-OPS-03 |
| Related acceptance scenarios | ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-099_audit_worm_export.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-099_audit_worm_export.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Policy, identity, model, tool, workflow, source, claim, artifact, cost and human decision events are kept in a hash-chained WORM record and exported per project in a verifiable form.


## Analysis
### What this package actually decides

That the record of what happened cannot be edited. A hash chain over canonicalised
events, held in WORM storage, exportable per project with a verifier anyone can
run.

### The chain is what makes deletion detectable (T01)

Immutable storage stops a record being altered. It does not stop one being
**removed** — and a gap in an append-only log looks exactly like a quiet period.

Sequence numbers plus a hash chain make removal detectable: the chain breaks, and
the break names the position. That is the difference between *tamper-resistant* and
*tamper-evident*.

### Canonicalisation is a prerequisite, not a detail (T01)

Two serialisations of one event produce two hashes and the chain becomes
unverifiable across implementations. Key ordering, number formats, unicode
normalisation — the same problem WP-072 solves for the literature manifest, and the
same solution.

### Audit-of-audit (T03)

Reading the audit log is itself an event. Without it, an investigator's access is
invisible, and so is an attacker's. This is the log that catches the unblinding
attempt WP-086 denies and WP-075 records.

### The verifier CLI is the deliverable that makes this external (T05)

An export that only this system can check is an export nobody outside can trust.
A standalone verifier — public key, export, hash chain, signature — is what lets an
auditor confirm the record without access to the running system.

### Gap detection has to run, not exist (T06)

`PR-20`'s shape again: the failure mode is silence. Chain verification runs on a
schedule, and a gap opens an incident rather than waiting for an audit.

### What this package cannot fix

The interim profile. `airl-interim-v0.1` is a local key and a local clock, and the
operator holds the repository, the key, the generator and the store. WORM plus a
hash chain makes tampering detectable **by someone who trusts the operator's
infrastructure**; it does not make the record independently verifiable. WP-139 is
where that changes.

### Baseline v1.3.0 — showing the cost of collaboration, and the shape of a decision

The experience and observability layer gains three things it could not
previously display, because they did not exist to be displayed.

**Collaboration cost.** Coordination overhead ratio, redundant message rate,
useful challenge rate, rounds, and the token ledger's seven categories. A single
cost total says a campaign was expensive; the categories say whether it was
expensive because it did science or because it held a meeting.

**The human decision surface, reordered.** Evidence first, recommendation second,
and a `DecisionDelta` when the second changes the first (`ADR-016`). The queue
uses evidence-delta priority — what changed since the last decision, not the full
state every time. **Attention priority orders and never authorises**, and no
timeout or learned preference produces an approval.

**Verifier abstention, surfaced.** An `ABSTAIN` is an escalation signal and has to
look like one in the interface. A surface that renders it as a soft pass has
undone `ADR-015`.

New SLOs: coordination overhead, challenge rate, contamination and security
findings, and the quality/cost Pareto frontier.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

13, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |
| [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md) | `Admission policies` · `Trust root management` · `CVE/exception workflow` · `Revocation/impact runbook` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |

### Full prerequisite closure

**55 of 160 packages (34%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |
| 30 | `WP-096` |

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-101` · `WP-103` · `WP-106` · `WP-109` · `WP-114` · `WP-118` · `WP-128` · `WP-129` · `WP-152`
- **Transitively reachable:** **29 of 160 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **31** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Internal Audit Platform Lead |
| Independent verifier | Independent Auditor / Security |
| Gates touched | `G0–G10` · `Platform` |
| Controls | `CTL-GOV-01` · `CTL-OPS-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/ACC-40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |
| [ACC-68 — Human Intervention Without an Audit Record](../12_ACCEPTANCE_SCENARIOS/ACC-68_human_intervention_audit.md) | Critical | The edit fails and rolls back. There is no path by which a human action changes canonical state without an atomically written `HumanInterventionRecord` carrying before and after references. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Admission policies` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Trust root management` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `CVE/exception workflow` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Revocation/impact runbook` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Adapted-source admission control` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Run Registry` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Preflight validator` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `MLflow integration` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lineage queries` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lifecycle dashboard` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `RawEvaluatorArtifact` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `VerifiedValue` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `PredictionRecord` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `FailureAssessment` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `ModelExecutionFingerprint` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Internal Audit Platform Lead** carries the acceptance decision; **Independent Auditor / Security** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-099-T01 | Write audit event canonicalisation and the sequence/hash chain | Implementation owner | Commit / configuration / record reference |
| WP-099-T02 | Establish the WORM store, retention and access separation | Implementation owner | Commit / configuration / record reference |
| WP-099-T03 | Add sensitive-field encryption/redaction and audit-of-audit logging | Implementation owner | Commit / configuration / record reference |
| WP-099-T04 | Write the project, time, actor and control export API | Implementation owner | Commit / configuration / record reference |
| WP-099-T05 | Build the signature, manifest and verifier CLI | Implementation owner | Commit / configuration / record reference |
| WP-099-T06 | Add tamper and gap detection with incident triggers | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Audit Ledger`
- `Hash-chain service`
- `Audit export/verify tooling`
- `Retention/access policy`
- `Integrity dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-099_audit_worm_export.tests.md`](WP-099_audit_worm_export.tests.md).

- Detection of a tampered record
- Detection of a missing sequence gap
- Denial of unauthorised delete or modify
- Full project export with chain verification
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-099_audit_worm_export.acceptance.md`](WP-099_audit_worm_export.acceptance.md), together with what this package still cannot establish.

- [ ] An audit administrator cannot alter the records.
- [ ] An export carries the complete policy, model, tool, cost, artifact and decision chain.
- [ ] Retention respects legal hold.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A corrupted replica is restored from an intact WORM copy; a hash gap is a critical incident and a cutover blocker.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
