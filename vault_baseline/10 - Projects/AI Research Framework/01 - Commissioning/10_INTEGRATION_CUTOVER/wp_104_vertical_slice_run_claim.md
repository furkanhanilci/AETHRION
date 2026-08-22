# WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence

## Package card

| Field | Value |
|---|---|
| Work package | `WP-104` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Scientific Engineering Lead |
| Independent verifier | Methodologist / Evidence Auditor |
| Hard dependencies | WP-035, WP-054, WP-075, WP-076, WP-077, WP-078, WP-079, WP-080, WP-081, WP-082, WP-083, WP-095, WP-096, WP-097, WP-100 |
| Related gates | G4,G5 |
| Related controls | CTL-DAT-01, CTL-EPI-01, CTL-CST-01 |
| Related acceptance scenarios | ACC-08, ACC-09, ACC-23, ACC-32, ACC-39 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A staged run executes from the frozen protocol, literature set and baseline; the result becomes artifacts, evidence spans and a claim dependency and assessment chain.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/wp_054_gvisor_sandbox.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/wp_078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/wp_079_source_trust_cards.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/wp_083_experiment_batch.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md), [WP-097 — Langfuse Model/Agent Tracing and Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/wp_097_langfuse_llm_trace.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-104-T01 | Create the baseline, falsification plan and preflight manifest | Implementation owner | Commit / configuration / record reference |
| WP-104-T02 | Run the staged experiment, smoke run and full run | Implementation owner | Commit / configuration / record reference |
| WP-104-T03 | Verify model, tool, sandbox, artifact and cost correlation | Implementation owner | Commit / configuration / record reference |
| WP-104-T04 | Perform evidence extraction, anchoring, trust and citation audit | Implementation owner | Commit / configuration / record reference |
| WP-104-T05 | Build the claim, dependency and state path, including the negative-result path | Implementation owner | Commit / configuration / record reference |
| WP-104-T06 | Query lineage in the cockpit, the graph and the audit ledger | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Run/claim vertical dossier`
- `Run manifests/artifacts`
- `Claim/Evidence records`
- `Cost/trace/audit evidence`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of a run with a missing manifest
- A hard budget stop
- Denial of an artifact overwrite
- The contradictory-evidence state
- A negative result being retained
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every run carries complete frozen lineage.
- [ ] Material claims are bound to a locator and to source status.
- [ ] A self-declaration never substitutes for mechanical evidence.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

The run or claim is invalidated within the synthetic project; canonical evidence is retained and corrections are made as new versions.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
