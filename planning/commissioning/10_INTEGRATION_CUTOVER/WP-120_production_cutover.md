# WP-120 — Production Cutover and Go-Live Decision

## Package card

| Field | Value |
|---|---|
| Work package | `WP-120` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Executive Sponsor / Program Lead |
| Independent verifier | Commissioning Board / Internal Audit |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118, WP-119 |
| Related gates | Cutover |
| Related controls | All controls |
| Related acceptance scenarios | every scenario whose `Acceptance phase` is `PRE_GO_LIVE`; the set is derived, never enumerated here, because an enumeration drifts the moment a scenario is added |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-120_production_cutover.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-120_production_cutover.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

On the strength of the signed commissioning dossier and the rehearsal, the change freeze, migration and promotion, smoke and integrity tests, traffic enablement and the formal Go-Live `DecisionRecord` are executed.


## Analysis
### What this package actually decides

The single moment the programme has been building toward, and the decision it
encodes is that **production opens once, integrated**.

`planning/commissioning/README.md` §1 states it: the programme is developed
incrementally *but is not opened to production with capabilities missing*. A
staged opening would let a partially commissioned system carry real research, which
is the outcome the whole plan exists to prevent.

### The go/no-go decision is the deliverable (T06)

Everything else here is procedure. The `DecisionRecord` is the artifact, and
`00_PROGRAM/10` fixes its preconditions: zero open critical findings, zero open high
findings or a time-boxed board-accepted residual, two restore rehearsals, and the
whole entry-condition list.

### Abort must remain available until the last moment (T06)

`00_PROGRAM/10` requires rollback/abort thresholds and decision owners to be
explicit, and WP-001 makes abort authority non-delegable and separate from the
sponsor. A cutover that becomes unabortable partway has removed its own safety.

### The restore point comes before anything moves (T02)

Not a backup — a **verified** restore point, with the owner check completed. An
untested restore point at cutover is `PR-13` at the worst possible moment.

### Traffic enablement is sequenced, and the sequence is reversible (T05)

Controlled sequence, each step observed, each step reversible. This is the one place
where "integrated cutover" and "staged enablement" are compatible: the *capabilities*
open together; the *traffic* arrives in a controlled order.

### The post-cutover audit snapshot closes the record (T07)

A hash-chained snapshot immediately after cutover is the baseline every later
integrity check compares against.

### Baseline v1.3.0 — the slices exercise the cohort, and the regression injects faults

The vertical slices and the cutover path grow to cover what this baseline adds,
and one package changes character.

**WP-107 becomes the engineering completion slice.** Requirement and
specification → worktree → TDD → code review → CI → supply-chain attestation →
signed artifact → **eligibility to produce scientific evidence**. That last arrow
is the junction between the two disciplines, and before this baseline nothing
proved it end to end.

**The other slices exercise the collaboration plane**: a compiled cohort, sealed
initial positions, typed delta exchange over a sparse topology, an adaptive
assurance route, a fingerprinted reproduction and a firewalled benchmark run.

**The regression suite gains injections rather than cases.** Faulty agent,
malicious agent, split brain, duplicate and out-of-order events, communication
degradation under budget pressure, and benchmark contamination. These are
failures that are invisible in a healthy run and obvious only in a post-mortem,
which is why they are caused deliberately rather than waited for.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |
| [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md) | `Chaos test suite/results` · `Steady-state hypotheses` · `Recovery/integrity report` · `Resilience sign-off` |
| [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md) | `Load test suite/results` · `Capacity model` · `Bottleneck/tuning report` · `Cost/headroom forecast` |
| [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md) | `Operational Readiness Review` · `Runbook execution records` · `On-call simulation` · `Training/ownership sign-offs` |
| [WP-119 — Controlled Pilot and Cutover Rehearsal](../10_INTEGRATION_CUTOVER/WP-119_pilot_cutover_rehearsal.md) | `Pilot dossier` · `Cutover rehearsal log` · `Usability/ops findings` · `Rollback proof` |

### Full prerequisite closure

**120 of 160 packages (75%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` · `WP-154` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |
| 47 | `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` |
| 48 | `WP-115` |
| 49 | `WP-116` · `WP-117` |
| 50 | `WP-118` |
| 51 | `WP-119` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-121`
- **Transitively reachable:** **10 of 160 packages (6%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W8 — Cutover |
| Dependency depth | level **52** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Executive Sponsor / Program Lead |
| Independent verifier | Commissioning Board / Internal Audit |
| Gates touched | `Cutover` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

This package is an **aggregator**: its commissioning set is the registry query `phase=PRE_GO_LIVE`, evaluated at generation time. Adding a scenario in that phase adds it here, and nobody has to remember to. The `Why` column below distinguishes the rows that arrived by rule from the ones bound deliberately — an aggregate that cannot be audited row by row is a list with extra steps.

| Scenario | Severity | Why |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/ACC-02_agent_used_source_writeback.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-03 — Duplicate and Metadata Collision](../12_ACCEPTANCE_SCENARIOS/ACC-03_duplicate_collision.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/ACC-05_prompt_injection_pdf.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-06_plan_self_approval.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-07 — Reviewer Order Bias](../12_ACCEPTANCE_SCENARIOS/ACC-07_reviewer_order_bias.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/ACC-09_budget_hard_stop.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-10 — Primary Model Provider Outage](../12_ACCEPTANCE_SCENARIOS/ACC-10_provider_outage.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-11 — No Eligible Fallback](../12_ACCEPTANCE_SCENARIOS/ACC-11_no_eligible_fallback.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-12 — Duplicate Event Delivery](../12_ACCEPTANCE_SCENARIOS/ACC-12_duplicate_event.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-13 — Temporal Worker Crash](../12_ACCEPTANCE_SCENARIOS/ACC-13_temporal_worker_crash.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-14 — Workflow Code Deployment and Replay](../12_ACCEPTANCE_SCENARIOS/ACC-14_workflow_code_deploy.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-15 — Sandbox Escape Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-15_sandbox_escape.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-16 — Egress Exfiltration Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-16_egress_exfiltration.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-17 — Unsigned or Mutable Image](../12_ACCEPTANCE_SCENARIOS/ACC-17_unsigned_image.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-18 — D3 Data to a Public Provider](../12_ACCEPTANCE_SCENARIOS/ACC-18_d3_public_route.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/ACC-19_clean_room_pass.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/ACC-20_clean_room_fail.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-21 — Derived Graph Corruption and Rebuild](../12_ACCEPTANCE_SCENARIOS/ACC-21_graph_corruption.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-22 — Obsidian Human Edit Preservation](../12_ACCEPTANCE_SCENARIOS/ACC-22_obsidian_human_edit.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-23 — Artifact Overwrite Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-23_artifact_overwrite.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-24 — Policy Bundle Rollback](../12_ACCEPTANCE_SCENARIOS/ACC-24_policy_bundle_rollback.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/ACC-25_human_approval_forgery.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/ACC-26_approval_expiry.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-27 — Regional / Management Plane DR](../12_ACCEPTANCE_SCENARIOS/ACC-27_regional_dr.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-28 — Zotero Full Resync](../12_ACCEPTANCE_SCENARIOS/ACC-28_zotero_full_resync.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-29 — Provider Invoice Variance](../12_ACCEPTANCE_SCENARIOS/ACC-29_invoice_variance.md) | Medium | selected by phase=PRE_GO_LIVE |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/ACC-31_superseded_publication.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-32 — Secret in Prompt or Trace](../12_ACCEPTANCE_SCENARIOS/ACC-32_secret_in_trace.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-33 — Kueue Preemption](../12_ACCEPTANCE_SCENARIOS/ACC-33_kueue_preemption.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-34 — DLQ Repair and Corrected Replay](../12_ACCEPTANCE_SCENARIOS/ACC-34_dlq_repair.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-35 — Tool Partial Failure](../12_ACCEPTANCE_SCENARIOS/ACC-35_tool_partial_failure.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-36 — Model Snapshot Drift](../12_ACCEPTANCE_SCENARIOS/ACC-36_model_snapshot_drift.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-37 — Evaluation Set Contamination](../12_ACCEPTANCE_SCENARIOS/ACC-37_eval_contamination.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-38 — Critical Reviewer Unavailable](../12_ACCEPTANCE_SCENARIOS/ACC-38_reviewer_unavailable.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-39 — Negative Research Result](../12_ACCEPTANCE_SCENARIOS/ACC-39_negative_result.md) | Medium | selected by phase=PRE_GO_LIVE |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/ACC-40_audit_export.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling](../12_ACCEPTANCE_SCENARIOS/ACC-41_notification_data_class_ceiling.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-42 — Notification Broker Unavailable During an Escalating Condition](../12_ACCEPTANCE_SCENARIOS/ACC-42_notification_broker_outage.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-43 — Escalation Timeout and Dead-Man's Switch](../12_ACCEPTANCE_SCENARIOS/ACC-43_escalation_and_dead_mans_switch.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-44 — Inbound Content Attempts to Act as an Instruction](../12_ACCEPTANCE_SCENARIOS/ACC-44_inbound_message_is_not_an_instruction.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-45 — Irreversible External Record Submission](../12_ACCEPTANCE_SCENARIOS/ACC-45_external_record_submission.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-46 — Task Runs With No Skill Loaded](../12_ACCEPTANCE_SCENARIOS/ACC-46_skill_not_loaded.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-47 — Harness Starts Without the Skill Bootstrap](../12_ACCEPTANCE_SCENARIOS/ACC-47_skill_bootstrap_missing.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-48 — Wrong or Competing Skill Selected](../12_ACCEPTANCE_SCENARIOS/ACC-48_wrong_skill_selected.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-49 — Non-Waivable Skill Ignored Under Pressure](../12_ACCEPTANCE_SCENARIOS/ACC-49_skill_ignored_under_pressure.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-50 — Procedure Lost to Context Compaction or Restart](../12_ACCEPTANCE_SCENARIOS/ACC-50_skill_lost_on_compaction.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-51 — Upstream Change Invalidates a Derived Skill](../12_ACCEPTANCE_SCENARIOS/ACC-51_upstream_skill_drift.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-52 — Claimless Publication Assertion](../12_ACCEPTANCE_SCENARIOS/ACC-52_claimless_publication_assertion.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-53 — Unverified Numeric Result](../12_ACCEPTANCE_SCENARIOS/ACC-53_unverified_numeric_result.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-54 — Producer Attempts Evaluator Mutation](../12_ACCEPTANCE_SCENARIOS/ACC-54_evaluator_mutation_attempt.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-55 — Hidden Evaluation Data Access Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-55_hidden_evaluation_data_access.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-56 — Confirmatory Result Without a Frozen Analysis Plan](../12_ACCEPTANCE_SCENARIOS/ACC-56_confirmatory_without_frozen_plan.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-57 — Hypothesis In-Place Mutation Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-57_hypothesis_in_place_mutation.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-58 — Cross-Branch Fusion Lineage](../12_ACCEPTANCE_SCENARIOS/ACC-58_cross_branch_fusion_lineage.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-59 — Discovery Search Stagnation](../12_ACCEPTANCE_SCENARIOS/ACC-59_discovery_search_stagnation.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-60 — Failed Smoke Candidate Promotion Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-60_failed_smoke_promotion.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-61 — Unqualified Semantic Verifier](../12_ACCEPTANCE_SCENARIOS/ACC-61_unqualified_semantic_verifier.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-62 — Semantic Verifier Recorded as Mechanical](../12_ACCEPTANCE_SCENARIOS/ACC-62_verifier_class_misdeclaration.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-63 — Failed Experiment Must Be Recorded](../12_ACCEPTANCE_SCENARIOS/ACC-63_failed_experiment_recorded.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-64 — Implementation Failure Must Not Refute a Hypothesis](../12_ACCEPTANCE_SCENARIOS/ACC-64_implementation_failure_not_refutation.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-65 — Reproduction in the Producer Environment](../12_ACCEPTANCE_SCENARIOS/ACC-65_reproduction_in_producer_environment.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-66 — Standalone Reproduction Package](../12_ACCEPTANCE_SCENARIOS/ACC-66_standalone_reproduction_package.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-67 — Claim–Code–Result Consistency Failure](../12_ACCEPTANCE_SCENARIOS/ACC-67_claim_code_result_consistency.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-68 — Human Intervention Without an Audit Record](../12_ACCEPTANCE_SCENARIOS/ACC-68_human_intervention_audit.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-69 — Human Decision Timeout Must Not Auto-Approve](../12_ACCEPTANCE_SCENARIOS/ACC-69_decision_timeout_no_autoapproval.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-70 — EvidenceGap Lifecycle](../12_ACCEPTANCE_SCENARIOS/ACC-70_evidence_gap_lifecycle.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-71 — Multi-Parent Artifact Lineage](../12_ACCEPTANCE_SCENARIOS/ACC-71_artifact_multi_parent_lineage.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-72 — Reviewer Isolation Before Review Lock](../12_ACCEPTANCE_SCENARIOS/ACC-72_reviewer_isolation_before_lock.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-74 — Missing Upstream Lineage or Licence](../12_ACCEPTANCE_SCENARIOS/ACC-74_missing_upstream_lineage.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-75 — Literature Retrieval Budget and Stopping Rule](../12_ACCEPTANCE_SCENARIOS/ACC-75_retrieval_budget_and_stopping_rule.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-76 — Unsupported Publication Sentence](../12_ACCEPTANCE_SCENARIOS/ACC-76_unsupported_publication_sentence.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-77 — VerifiedValue Rebinding Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-77_verified_value_rebinding.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-78 — Raw Evidence Versus Interpretation](../12_ACCEPTANCE_SCENARIOS/ACC-78_raw_evidence_versus_interpretation.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-79 — Epistemic Memory Retention Violation](../12_ACCEPTANCE_SCENARIOS/ACC-79_memory_retention_violation.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-081 — Multi-Agent Cohort Required](../12_ACCEPTANCE_SCENARIOS/ACC-081_multi_agent_cohort_required.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-082 — Independent-First Embargo](../12_ACCEPTANCE_SCENARIOS/ACC-082_independent_first_embargo.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-083 — Typed Inter-Agent Message](../12_ACCEPTANCE_SCENARIOS/ACC-083_typed_inter_agent_message.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-084 — Delta-Only Communication](../12_ACCEPTANCE_SCENARIOS/ACC-084_delta_only_communication.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-085 — A Blackboard Entry Is Not Evidence](../12_ACCEPTANCE_SCENARIOS/ACC-085_blackboard_entry_is_not_evidence.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-086 — Sparse Topology Preserves Quality](../12_ACCEPTANCE_SCENARIOS/ACC-086_sparse_topology_quality_preservation.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-087 — Communication Optimisation Rollback](../12_ACCEPTANCE_SCENARIOS/ACC-087_communication_optimization_rollback.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-088 — Strategic Silence Never Silences a Blocker](../12_ACCEPTANCE_SCENARIOS/ACC-088_strategic_silence_never_silences_a_blocker.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-089 — Sycophancy Anchor Attack](../12_ACCEPTANCE_SCENARIOS/ACC-089_sycophancy_anchor_attack.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-090 — False Consensus Cannot Close a Challenge](../12_ACCEPTANCE_SCENARIOS/ACC-090_false_consensus.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-091 — Faulty Agent Output Does Not Propagate](../12_ACCEPTANCE_SCENARIOS/ACC-091_faulty_agent_challenge.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-092 — Inspector Reviews High-Consequence Output](../12_ACCEPTANCE_SCENARIOS/ACC-092_inspector_high_consequence_review.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-093 — A Malicious Agent Cannot Bind Authority](../12_ACCEPTANCE_SCENARIOS/ACC-093_malicious_agent_cannot_bind_authority.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-094 — An Unattributable Failure Is `UNKNOWN`](../12_ACCEPTANCE_SCENARIOS/ACC-094_failure_cause_unknown.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-095 — Failure Taxonomy Routing](../12_ACCEPTANCE_SCENARIOS/ACC-095_failure_taxonomy_routing.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-096 — A Refuted Memory Does Not Re-Enter Reasoning](../12_ACCEPTANCE_SCENARIOS/ACC-096_refuted_memory_mask.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-097 — Proactive Reminder of a Frozen Constraint](../12_ACCEPTANCE_SCENARIOS/ACC-097_proactive_frozen_constraint_reminder.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-098 — Memory Poisoning Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-098_memory_poisoning_attempt.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-099 — Budget Degrades Communication, Not the Cohort](../12_ACCEPTANCE_SCENARIOS/ACC-099_communication_budget_degradation.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-100 — Token Ledger Classification](../12_ACCEPTANCE_SCENARIOS/ACC-100_token_ledger_classification.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-101 — Reserved Assurance Budget Is Unreachable](../12_ACCEPTANCE_SCENARIOS/ACC-101_budget_hard_stop_reserved_assurance.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-102 — Deterministic Tool-Result Reuse](../12_ACCEPTANCE_SCENARIOS/ACC-102_tool_result_reuse.md) | Medium | selected by phase=PRE_GO_LIVE |
| [ACC-103 — Minor Specification Drift Is Recorded](../12_ACCEPTANCE_SCENARIOS/ACC-103_scientific_minor_spec_drift.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-104 — Major Specification Drift Blocks Confirmatory Status](../12_ACCEPTANCE_SCENARIOS/ACC-104_scientific_major_spec_drift.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-105 — A Claim Without a Complete Evidence Chain](../12_ACCEPTANCE_SCENARIOS/ACC-105_claim_without_evidence_chain.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-106 — A Number Without a VerifiedValue](../12_ACCEPTANCE_SCENARIOS/ACC-106_numeric_value_without_verifiedvalue.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-107 — Expired Verifier Qualification](../12_ACCEPTANCE_SCENARIOS/ACC-107_expired_verifier_qualification.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-108 — Escalation Is Not Selective Enforcement](../12_ACCEPTANCE_SCENARIOS/ACC-108_selective_verifier_escalation.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-109 — Verifier Abstention Is a Valid Result](../12_ACCEPTANCE_SCENARIOS/ACC-109_verifier_abstention_is_valid.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-110 — Human Preliminary Assessment Precedes the Recommendation](../12_ACCEPTANCE_SCENARIOS/ACC-110_human_preliminary_assessment.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-111 — Insufficient Basis Is Reachable](../12_ACCEPTANCE_SCENARIOS/ACC-111_human_insufficient_basis.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-112 — Correction Friction Symmetry](../12_ACCEPTANCE_SCENARIOS/ACC-112_correction_friction_symmetry.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-113 — Producer to Evaluator Leakage](../12_ACCEPTANCE_SCENARIOS/ACC-113_producer_evaluator_leakage.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-114 — Reproduction Environment Lineage](../12_ACCEPTANCE_SCENARIOS/ACC-114_reproduction_in_producer_environment_hardened.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-115 — Missing Model Execution Fingerprint](../12_ACCEPTANCE_SCENARIOS/ACC-115_missing_model_execution_fingerprint.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-116 — Distributional Reproduction for a Hosted Model](../12_ACCEPTANCE_SCENARIOS/ACC-116_distributional_hosted_model_reproduction.md) | High | selected by phase=PRE_GO_LIVE |
| [ACC-117 — Prompt Injection Meets a Capability Gate](../12_ACCEPTANCE_SCENARIOS/ACC-117_prompt_injection_capability_gate.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-118 — Search-Time Benchmark Contamination](../12_ACCEPTANCE_SCENARIOS/ACC-118_benchmark_search_time_contamination.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-119 — Destructive Projection Rebuild](../12_ACCEPTANCE_SCENARIOS/ACC-119_derived_projection_destructive_rebuild.md) | Critical | selected by phase=PRE_GO_LIVE |
| [ACC-120 — Missing Upstream Licence or Provenance](../12_ACCEPTANCE_SCENARIOS/ACC-120_missing_upstream_license_provenance.md) | High | selected by phase=PRE_GO_LIVE |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md), [WP-119 — Controlled Pilot and Cutover Rehearsal](../10_INTEGRATION_CUTOVER/WP-119_pilot_cutover_rehearsal.md)
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
| `Commissioning Dossier` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `RC evidence manifest` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Finding/risk register snapshot` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Readiness scorecard` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Board verdict` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Faulty-agent, split-brain and contamination regression` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Chaos test suite/results` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Steady-state hypotheses` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Recovery/integrity report` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Resilience sign-off` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Load test suite/results` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity model` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Bottleneck/tuning report` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Cost/headroom forecast` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity sign-off` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Operational Readiness Review` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Runbook execution records` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `On-call simulation` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Training/ownership sign-offs` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Pilot dossier` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Cutover rehearsal log` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Usability/ops findings` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Rollback proof` | `WP-119` | `python3 scripts/progress.py show WP-119` |
| `Go/no-go recommendation` | `WP-119` | `python3 scripts/progress.py show WP-119` |

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
- **Executive Sponsor / Program Lead** carries the acceptance decision; **Commissioning Board / Internal Audit** must verify independently of whoever implements.
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
| WP-120-T01 | Freeze the final RC, policy, schema, model, tool and infrastructure digests | Implementation owner | Commit / configuration / record reference |
| WP-120-T02 | Take the pre-cutover backup and restore point and run the owner check | Implementation owner | Commit / configuration / record reference |
| WP-120-T03 | Apply the IaC/GitOps deployment and migration steps | Implementation owner | Commit / configuration / record reference |
| WP-120-T04 | Run the service, contract, security and integrity smoke tests | Implementation owner | Commit / configuration / record reference |
| WP-120-T05 | Enable traffic, user access and monitoring in a controlled sequence | Implementation owner | Commit / configuration / record reference |
| WP-120-T06 | Record the go / no-go / abort decision with its evidence | Implementation owner | Commit / configuration / record reference |
| WP-120-T07 | Take the post-cutover audit snapshot | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cutover execution log`
- `Go-Live DecisionRecord`
- `Production release manifest`
- `Smoke/integrity results`
- `Audit snapshot`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-120_production_cutover.tests.md`](WP-120_production_cutover.tests.md).

- The preflight checklist
- Deployment and migration
- Security, identity and route smoke tests
- Workflow, source, claim and artifact integrity
- Abort and rollback readiness
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-120_production_cutover.acceptance.md`](WP-120_production_cutover.acceptance.md), together with what this package still cannot establish.

- [ ] The Commissioning Dossier is READY.
- [ ] Every `PRE_GO_LIVE` scenario PASSes, with open critical findings = 0.
- [ ] Every production digest is signed and pinned.
- [ ] The go-live decision is taken by named executives, SRE and Safety.
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

At the abort threshold traffic is closed and the last verified baseline is restored per the GitOps and database plan; newly written immutable records are never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
