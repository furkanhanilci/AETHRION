---
title: "WP-120 — Production Cutover and Go-Live Decision — Test Procedures"
aliases:
  - "WP-120 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-120_production_cutover.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w8
  - aethrion/effort/l
  - aethrion/gate/cutover
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-120 — Production Cutover and Go-Live Decision — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-120` |
| Work package | [`WP-120` — Production Cutover and Go-Live Decision](wp_120_production_cutover.md) |
| Companion | [acceptance criteria](wp_120_production_cutover.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board / Internal Audit** — the independent verifier |
| Accountable owner | Executive Sponsor / Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-120` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 118 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Cutover |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Executive Sponsor / Program Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Executive Sponsor / Program Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Commissioning Board / Internal Audit | At completion |
| `WP-115` accepted output | Full System Regression and Commissioning Dossier | Platform Assurance Lead | Before the first test case runs |
| `WP-116` accepted output | Resilience, Chaos and Failure-Injection Commissioning | SRE Lead | Before the first test case runs |
| `WP-117` accepted output | Performance, Capacity and Load Commissioning | Capacity Engineering Lead | Before the first test case runs |
| `WP-118` accepted output | Operational Readiness, On-Call and Runbook Simulation | SRE Lead | Before the first test case runs |
| `WP-119` accepted output | Controlled Pilot and Cutover Rehearsal | Program Lead | Before the first test case runs |

### Environment readiness report — §8.8

Every row must be checked before the first test case. An unchecked row is a stop condition, not a risk to manage.

- [ ] The target revision is pinned and recorded.
- [ ] The environment manifest has been **captured** from the running environment rather than written from intention.
- [ ] The workspace is isolated from the producer's working tree.
- [ ] Every dependency listed above is `ACCEPTED` (`python3 scripts/ready_queue.py`).
- [ ] The evidence sink is reachable and a specimen manifest verifies.
- [ ] The rollback or compensation path named on the package card can actually be exercised in this environment.

<!-- /generated:environment -->

## Test data requirements — §8.5

<!-- generated:data — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.5 and §8.7. Test data is a **deliverable of this package**, not a by-product of running it: a test whose fixture cannot be regenerated cannot be re-run, and a result that cannot be re-run is an anecdote.

| Requirement | Rule |
|---|---|
| Provenance | Every fixture is either synthetic or a licensed extract with its licence recorded. Personal or production data is never a fixture |
| Data class | Every fixture carries a `DataClass`; a fixture above D2 requires the matching `ExecutionProfile` |
| Regeneration | Each fixture is regenerated from a committed script or manifest, byte-identically |
| Negative fixtures | Every schema and every control has at least one fixture that **must fail**. A test set with no failing fixture proves nothing |
| Independence | Fixtures are not shared with any evaluation golden set (`PR-15` — eval contamination) |

### Test data readiness report — §8.7

- [ ] Every fixture regenerates byte-identically from its committed source.
- [ ] Every fixture carries a `DataClass` and, above D2, an `ExecutionProfile`.
- [ ] At least one **negative** fixture exists per schema and per control.
- [ ] No fixture overlaps an evaluation golden set.
- [ ] Fixture licences permit the retention this test run requires.

<!-- /generated:data -->

## Test coverage items — §8.3.2

<!-- generated:coverage — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.3.2. A coverage item is something the tests must reach. The two sources are mechanical: every mandatory deliverable of this package, and every acceptance scenario bound to it. A coverage item with no test case is a gap, and it is listed here so the gap is visible rather than assumed away.

| # | Coverage item | Source | Covered by |
|---:|---|---|---|
| C01 | `Cutover execution log` | Mandatory deliverable | *(name the test case)* |
| C02 | `Go-Live DecisionRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `Production release manifest` | Mandatory deliverable | *(name the test case)* |
| C04 | `Smoke/integrity results` | Mandatory deliverable | *(name the test case)* |
| C05 | `Audit snapshot` | Mandatory deliverable | *(name the test case)* |
| C06 | Freeze the final RC, policy, schema, model, tool and infrastructure digests | WP-120-T01 | *(name the test case)* |
| C07 | Take the pre-cutover backup and restore point and run the owner check | WP-120-T02 | *(name the test case)* |
| C08 | Apply the IaC/GitOps deployment and migration steps | WP-120-T03 | *(name the test case)* |
| C09 | Run the service, contract, security and integrity smoke tests | WP-120-T04 | *(name the test case)* |
| C10 | Enable traffic, user access and monitoring in a controlled sequence | WP-120-T05 | *(name the test case)* |
| C11 | Record the go / no-go / abort decision with its evidence | WP-120-T06 | *(name the test case)* |
| C12 | Take the post-cutover audit snapshot | WP-120-T07 | *(name the test case)* |
| C13 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C14 | Agent-Used Source Write-Back | [ACC-02](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) — Critical | *(name the test case)* |
| C15 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) — High | *(name the test case)* |
| C16 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |
| C17 | Prompt-Injection PDF | [ACC-05](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) — Critical | *(name the test case)* |
| C18 | Planner Self-Approval Attempt | [ACC-06](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) — Critical | *(name the test case)* |
| C19 | Reviewer Order Bias | [ACC-07](../12_ACCEPTANCE_SCENARIOS/acc_07_reviewer_order_bias.md) — High | *(name the test case)* |
| C20 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) — Critical | *(name the test case)* |
| C21 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C22 | Primary Model Provider Outage | [ACC-10](../12_ACCEPTANCE_SCENARIOS/acc_10_provider_outage.md) — High | *(name the test case)* |
| C23 | No Eligible Fallback | [ACC-11](../12_ACCEPTANCE_SCENARIOS/acc_11_no_eligible_fallback.md) — Critical | *(name the test case)* |
| C24 | Duplicate Event Delivery | [ACC-12](../12_ACCEPTANCE_SCENARIOS/acc_12_duplicate_event.md) — Critical | *(name the test case)* |
| C25 | Temporal Worker Crash | [ACC-13](../12_ACCEPTANCE_SCENARIOS/acc_13_temporal_worker_crash.md) — Critical | *(name the test case)* |
| C26 | Workflow Code Deployment and Replay | [ACC-14](../12_ACCEPTANCE_SCENARIOS/acc_14_workflow_code_deploy.md) — Critical | *(name the test case)* |
| C27 | Sandbox Escape Attempt | [ACC-15](../12_ACCEPTANCE_SCENARIOS/acc_15_sandbox_escape.md) — Critical | *(name the test case)* |
| C28 | Egress Exfiltration Attempt | [ACC-16](../12_ACCEPTANCE_SCENARIOS/acc_16_egress_exfiltration.md) — Critical | *(name the test case)* |
| C29 | Unsigned or Mutable Image | [ACC-17](../12_ACCEPTANCE_SCENARIOS/acc_17_unsigned_image.md) — Critical | *(name the test case)* |
| C30 | D3 Data to a Public Provider | [ACC-18](../12_ACCEPTANCE_SCENARIOS/acc_18_d3_public_route.md) — Critical | *(name the test case)* |
| C31 | Clean-Room Reproduction Pass | [ACC-19](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) — High | *(name the test case)* |
| C32 | Clean-Room Reproduction Failure | [ACC-20](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) — Critical | *(name the test case)* |
| C33 | Derived Graph Corruption and Rebuild | [ACC-21](../12_ACCEPTANCE_SCENARIOS/acc_21_graph_corruption.md) — High | *(name the test case)* |
| C34 | Obsidian Human Edit Preservation | [ACC-22](../12_ACCEPTANCE_SCENARIOS/acc_22_obsidian_human_edit.md) — High | *(name the test case)* |
| C35 | Artifact Overwrite Attempt | [ACC-23](../12_ACCEPTANCE_SCENARIOS/acc_23_artifact_overwrite.md) — Critical | *(name the test case)* |
| C36 | Policy Bundle Rollback | [ACC-24](../12_ACCEPTANCE_SCENARIOS/acc_24_policy_bundle_rollback.md) — High | *(name the test case)* |
| C37 | Human Approval Forgery | [ACC-25](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) — Critical | *(name the test case)* |
| C38 | Approval, Delegation and Exception Expiry | [ACC-26](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) — Critical | *(name the test case)* |
| C39 | Regional / Management Plane DR | [ACC-27](../12_ACCEPTANCE_SCENARIOS/acc_27_regional_dr.md) — Critical | *(name the test case)* |
| C40 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |
| C41 | Provider Invoice Variance | [ACC-29](../12_ACCEPTANCE_SCENARIOS/acc_29_invoice_variance.md) — Medium | *(name the test case)* |
| C42 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) — Critical | *(name the test case)* |
| C43 | Superseded Publication | [ACC-31](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) — High | *(name the test case)* |
| C44 | Secret in Prompt or Trace | [ACC-32](../12_ACCEPTANCE_SCENARIOS/acc_32_secret_in_trace.md) — Critical | *(name the test case)* |
| C45 | Kueue Preemption | [ACC-33](../12_ACCEPTANCE_SCENARIOS/acc_33_kueue_preemption.md) — High | *(name the test case)* |
| C46 | DLQ Repair and Corrected Replay | [ACC-34](../12_ACCEPTANCE_SCENARIOS/acc_34_dlq_repair.md) — High | *(name the test case)* |
| C47 | Tool Partial Failure | [ACC-35](../12_ACCEPTANCE_SCENARIOS/acc_35_tool_partial_failure.md) — Critical | *(name the test case)* |
| C48 | Model Snapshot Drift | [ACC-36](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) — Critical | *(name the test case)* |
| C49 | Evaluation Set Contamination | [ACC-37](../12_ACCEPTANCE_SCENARIOS/acc_37_eval_contamination.md) — Critical | *(name the test case)* |
| C50 | Critical Reviewer Unavailable | [ACC-38](../12_ACCEPTANCE_SCENARIOS/acc_38_reviewer_unavailable.md) — High | *(name the test case)* |
| C51 | Negative Research Result | [ACC-39](../12_ACCEPTANCE_SCENARIOS/acc_39_negative_result.md) — Medium | *(name the test case)* |
| C52 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |
| C53 | Outbound Notification Exceeds the Channel Data-Class Ceiling | [ACC-41](../12_ACCEPTANCE_SCENARIOS/acc_41_notification_data_class_ceiling.md) — Critical | *(name the test case)* |
| C54 | Notification Broker Unavailable During an Escalating Condition | [ACC-42](../12_ACCEPTANCE_SCENARIOS/acc_42_notification_broker_outage.md) — High | *(name the test case)* |
| C55 | Escalation Timeout and Dead-Man's Switch | [ACC-43](../12_ACCEPTANCE_SCENARIOS/acc_43_escalation_and_dead_mans_switch.md) — Critical | *(name the test case)* |
| C56 | Inbound Content Attempts to Act as an Instruction | [ACC-44](../12_ACCEPTANCE_SCENARIOS/acc_44_inbound_message_is_not_an_instruction.md) — Critical | *(name the test case)* |
| C57 | Irreversible External Record Submission | [ACC-45](../12_ACCEPTANCE_SCENARIOS/acc_45_external_record_submission.md) — Critical | *(name the test case)* |
| C58 | Task Runs With No Skill Loaded | [ACC-46](../12_ACCEPTANCE_SCENARIOS/acc_46_skill_not_loaded.md) — Critical | *(name the test case)* |
| C59 | Harness Starts Without the Skill Bootstrap | [ACC-47](../12_ACCEPTANCE_SCENARIOS/acc_47_skill_bootstrap_missing.md) — Critical | *(name the test case)* |
| C60 | Wrong or Competing Skill Selected | [ACC-48](../12_ACCEPTANCE_SCENARIOS/acc_48_wrong_skill_selected.md) — High | *(name the test case)* |
| C61 | Non-Waivable Skill Ignored Under Pressure | [ACC-49](../12_ACCEPTANCE_SCENARIOS/acc_49_skill_ignored_under_pressure.md) — Critical | *(name the test case)* |
| C62 | Procedure Lost to Context Compaction or Restart | [ACC-50](../12_ACCEPTANCE_SCENARIOS/acc_50_skill_lost_on_compaction.md) — High | *(name the test case)* |
| C63 | Upstream Change Invalidates a Derived Skill | [ACC-51](../12_ACCEPTANCE_SCENARIOS/acc_51_upstream_skill_drift.md) — High | *(name the test case)* |
| C64 | Claimless Publication Assertion | [ACC-52](../12_ACCEPTANCE_SCENARIOS/acc_52_claimless_publication_assertion.md) — Critical | *(name the test case)* |
| C65 | Unverified Numeric Result | [ACC-53](../12_ACCEPTANCE_SCENARIOS/acc_53_unverified_numeric_result.md) — Critical | *(name the test case)* |
| C66 | Producer Attempts Evaluator Mutation | [ACC-54](../12_ACCEPTANCE_SCENARIOS/acc_54_evaluator_mutation_attempt.md) — Critical | *(name the test case)* |
| C67 | Hidden Evaluation Data Access Attempt | [ACC-55](../12_ACCEPTANCE_SCENARIOS/acc_55_hidden_evaluation_data_access.md) — Critical | *(name the test case)* |
| C68 | Confirmatory Result Without a Frozen Analysis Plan | [ACC-56](../12_ACCEPTANCE_SCENARIOS/acc_56_confirmatory_without_frozen_plan.md) — Critical | *(name the test case)* |
| C69 | Hypothesis In-Place Mutation Attempt | [ACC-57](../12_ACCEPTANCE_SCENARIOS/acc_57_hypothesis_in_place_mutation.md) — High | *(name the test case)* |
| C70 | Cross-Branch Fusion Lineage | [ACC-58](../12_ACCEPTANCE_SCENARIOS/acc_58_cross_branch_fusion_lineage.md) — High | *(name the test case)* |
| C71 | Discovery Search Stagnation | [ACC-59](../12_ACCEPTANCE_SCENARIOS/acc_59_discovery_search_stagnation.md) — High | *(name the test case)* |
| C72 | Failed Smoke Candidate Promotion Attempt | [ACC-60](../12_ACCEPTANCE_SCENARIOS/acc_60_failed_smoke_promotion.md) — Critical | *(name the test case)* |
| C73 | Unqualified Semantic Verifier | [ACC-61](../12_ACCEPTANCE_SCENARIOS/acc_61_unqualified_semantic_verifier.md) — Critical | *(name the test case)* |
| C74 | Semantic Verifier Recorded as Mechanical | [ACC-62](../12_ACCEPTANCE_SCENARIOS/acc_62_verifier_class_misdeclaration.md) — High | *(name the test case)* |
| C75 | Failed Experiment Must Be Recorded | [ACC-63](../12_ACCEPTANCE_SCENARIOS/acc_63_failed_experiment_recorded.md) — High | *(name the test case)* |
| C76 | Implementation Failure Must Not Refute a Hypothesis | [ACC-64](../12_ACCEPTANCE_SCENARIOS/acc_64_implementation_failure_not_refutation.md) — Critical | *(name the test case)* |
| C77 | Reproduction in the Producer Environment | [ACC-65](../12_ACCEPTANCE_SCENARIOS/acc_65_reproduction_in_producer_environment.md) — Critical | *(name the test case)* |
| C78 | Standalone Reproduction Package | [ACC-66](../12_ACCEPTANCE_SCENARIOS/acc_66_standalone_reproduction_package.md) — Critical | *(name the test case)* |
| C79 | Claim–Code–Result Consistency Failure | [ACC-67](../12_ACCEPTANCE_SCENARIOS/acc_67_claim_code_result_consistency.md) — Critical | *(name the test case)* |
| C80 | Human Intervention Without an Audit Record | [ACC-68](../12_ACCEPTANCE_SCENARIOS/acc_68_human_intervention_audit.md) — Critical | *(name the test case)* |
| C81 | Human Decision Timeout Must Not Auto-Approve | [ACC-69](../12_ACCEPTANCE_SCENARIOS/acc_69_decision_timeout_no_autoapproval.md) — Critical | *(name the test case)* |
| C82 | EvidenceGap Lifecycle | [ACC-70](../12_ACCEPTANCE_SCENARIOS/acc_70_evidence_gap_lifecycle.md) — High | *(name the test case)* |
| C83 | Multi-Parent Artifact Lineage | [ACC-71](../12_ACCEPTANCE_SCENARIOS/acc_71_artifact_multi_parent_lineage.md) — Critical | *(name the test case)* |
| C84 | Reviewer Isolation Before Review Lock | [ACC-72](../12_ACCEPTANCE_SCENARIOS/acc_72_reviewer_isolation_before_lock.md) — Critical | *(name the test case)* |
| C85 | Missing Upstream Lineage or Licence | [ACC-74](../12_ACCEPTANCE_SCENARIOS/acc_74_missing_upstream_lineage.md) — High | *(name the test case)* |
| C86 | Literature Retrieval Budget and Stopping Rule | [ACC-75](../12_ACCEPTANCE_SCENARIOS/acc_75_retrieval_budget_and_stopping_rule.md) — High | *(name the test case)* |
| C87 | Unsupported Publication Sentence | [ACC-76](../12_ACCEPTANCE_SCENARIOS/acc_76_unsupported_publication_sentence.md) — Critical | *(name the test case)* |
| C88 | VerifiedValue Rebinding Attempt | [ACC-77](../12_ACCEPTANCE_SCENARIOS/acc_77_verified_value_rebinding.md) — Critical | *(name the test case)* |
| C89 | Raw Evidence Versus Interpretation | [ACC-78](../12_ACCEPTANCE_SCENARIOS/acc_78_raw_evidence_versus_interpretation.md) — Critical | *(name the test case)* |
| C90 | Epistemic Memory Retention Violation | [ACC-79](../12_ACCEPTANCE_SCENARIOS/acc_79_memory_retention_violation.md) — High | *(name the test case)* |
| C91 | Multi-Agent Cohort Required | [ACC-081](../12_ACCEPTANCE_SCENARIOS/acc_081_multi_agent_cohort_required.md) — Critical | *(name the test case)* |
| C92 | Independent-First Embargo | [ACC-082](../12_ACCEPTANCE_SCENARIOS/acc_082_independent_first_embargo.md) — Critical | *(name the test case)* |
| C93 | Typed Inter-Agent Message | [ACC-083](../12_ACCEPTANCE_SCENARIOS/acc_083_typed_inter_agent_message.md) — High | *(name the test case)* |
| C94 | Delta-Only Communication | [ACC-084](../12_ACCEPTANCE_SCENARIOS/acc_084_delta_only_communication.md) — High | *(name the test case)* |
| C95 | A Blackboard Entry Is Not Evidence | [ACC-085](../12_ACCEPTANCE_SCENARIOS/acc_085_blackboard_entry_is_not_evidence.md) — Critical | *(name the test case)* |
| C96 | Sparse Topology Preserves Quality | [ACC-086](../12_ACCEPTANCE_SCENARIOS/acc_086_sparse_topology_quality_preservation.md) — High | *(name the test case)* |
| C97 | Communication Optimisation Rollback | [ACC-087](../12_ACCEPTANCE_SCENARIOS/acc_087_communication_optimization_rollback.md) — High | *(name the test case)* |
| C98 | Strategic Silence Never Silences a Blocker | [ACC-088](../12_ACCEPTANCE_SCENARIOS/acc_088_strategic_silence_never_silences_a_blocker.md) — Critical | *(name the test case)* |
| C99 | Sycophancy Anchor Attack | [ACC-089](../12_ACCEPTANCE_SCENARIOS/acc_089_sycophancy_anchor_attack.md) — Critical | *(name the test case)* |
| C100 | False Consensus Cannot Close a Challenge | [ACC-090](../12_ACCEPTANCE_SCENARIOS/acc_090_false_consensus.md) — Critical | *(name the test case)* |
| C101 | Faulty Agent Output Does Not Propagate | [ACC-091](../12_ACCEPTANCE_SCENARIOS/acc_091_faulty_agent_challenge.md) — Critical | *(name the test case)* |
| C102 | Inspector Reviews High-Consequence Output | [ACC-092](../12_ACCEPTANCE_SCENARIOS/acc_092_inspector_high_consequence_review.md) — High | *(name the test case)* |
| C103 | A Malicious Agent Cannot Bind Authority | [ACC-093](../12_ACCEPTANCE_SCENARIOS/acc_093_malicious_agent_cannot_bind_authority.md) — Critical | *(name the test case)* |
| C104 | An Unattributable Failure Is `UNKNOWN` | [ACC-094](../12_ACCEPTANCE_SCENARIOS/acc_094_failure_cause_unknown.md) — High | *(name the test case)* |
| C105 | Failure Taxonomy Routing | [ACC-095](../12_ACCEPTANCE_SCENARIOS/acc_095_failure_taxonomy_routing.md) — High | *(name the test case)* |
| C106 | A Refuted Memory Does Not Re-Enter Reasoning | [ACC-096](../12_ACCEPTANCE_SCENARIOS/acc_096_refuted_memory_mask.md) — High | *(name the test case)* |
| C107 | Proactive Reminder of a Frozen Constraint | [ACC-097](../12_ACCEPTANCE_SCENARIOS/acc_097_proactive_frozen_constraint_reminder.md) — High | *(name the test case)* |
| C108 | Memory Poisoning Attempt | [ACC-098](../12_ACCEPTANCE_SCENARIOS/acc_098_memory_poisoning_attempt.md) — Critical | *(name the test case)* |
| C109 | Budget Degrades Communication, Not the Cohort | [ACC-099](../12_ACCEPTANCE_SCENARIOS/acc_099_communication_budget_degradation.md) — Critical | *(name the test case)* |
| C110 | Token Ledger Classification | [ACC-100](../12_ACCEPTANCE_SCENARIOS/acc_100_token_ledger_classification.md) — High | *(name the test case)* |
| C111 | Reserved Assurance Budget Is Unreachable | [ACC-101](../12_ACCEPTANCE_SCENARIOS/acc_101_budget_hard_stop_reserved_assurance.md) — Critical | *(name the test case)* |
| C112 | Deterministic Tool-Result Reuse | [ACC-102](../12_ACCEPTANCE_SCENARIOS/acc_102_tool_result_reuse.md) — Medium | *(name the test case)* |
| C113 | Minor Specification Drift Is Recorded | [ACC-103](../12_ACCEPTANCE_SCENARIOS/acc_103_scientific_minor_spec_drift.md) — High | *(name the test case)* |
| C114 | Major Specification Drift Blocks Confirmatory Status | [ACC-104](../12_ACCEPTANCE_SCENARIOS/acc_104_scientific_major_spec_drift.md) — Critical | *(name the test case)* |
| C115 | A Claim Without a Complete Evidence Chain | [ACC-105](../12_ACCEPTANCE_SCENARIOS/acc_105_claim_without_evidence_chain.md) — Critical | *(name the test case)* |
| C116 | A Number Without a VerifiedValue | [ACC-106](../12_ACCEPTANCE_SCENARIOS/acc_106_numeric_value_without_verifiedvalue.md) — Critical | *(name the test case)* |
| C117 | Expired Verifier Qualification | [ACC-107](../12_ACCEPTANCE_SCENARIOS/acc_107_expired_verifier_qualification.md) — Critical | *(name the test case)* |
| C118 | Escalation Is Not Selective Enforcement | [ACC-108](../12_ACCEPTANCE_SCENARIOS/acc_108_selective_verifier_escalation.md) — Critical | *(name the test case)* |
| C119 | Verifier Abstention Is a Valid Result | [ACC-109](../12_ACCEPTANCE_SCENARIOS/acc_109_verifier_abstention_is_valid.md) — High | *(name the test case)* |
| C120 | Human Preliminary Assessment Precedes the Recommendation | [ACC-110](../12_ACCEPTANCE_SCENARIOS/acc_110_human_preliminary_assessment.md) — Critical | *(name the test case)* |
| C121 | Insufficient Basis Is Reachable | [ACC-111](../12_ACCEPTANCE_SCENARIOS/acc_111_human_insufficient_basis.md) — High | *(name the test case)* |
| C122 | Correction Friction Symmetry | [ACC-112](../12_ACCEPTANCE_SCENARIOS/acc_112_correction_friction_symmetry.md) — High | *(name the test case)* |
| C123 | Producer to Evaluator Leakage | [ACC-113](../12_ACCEPTANCE_SCENARIOS/acc_113_producer_evaluator_leakage.md) — Critical | *(name the test case)* |
| C124 | Reproduction Environment Lineage | [ACC-114](../12_ACCEPTANCE_SCENARIOS/acc_114_reproduction_in_producer_environment_hardened.md) — Critical | *(name the test case)* |
| C125 | Missing Model Execution Fingerprint | [ACC-115](../12_ACCEPTANCE_SCENARIOS/acc_115_missing_model_execution_fingerprint.md) — Critical | *(name the test case)* |
| C126 | Distributional Reproduction for a Hosted Model | [ACC-116](../12_ACCEPTANCE_SCENARIOS/acc_116_distributional_hosted_model_reproduction.md) — High | *(name the test case)* |
| C127 | Prompt Injection Meets a Capability Gate | [ACC-117](../12_ACCEPTANCE_SCENARIOS/acc_117_prompt_injection_capability_gate.md) — Critical | *(name the test case)* |
| C128 | Search-Time Benchmark Contamination | [ACC-118](../12_ACCEPTANCE_SCENARIOS/acc_118_benchmark_search_time_contamination.md) — Critical | *(name the test case)* |
| C129 | Destructive Projection Rebuild | [ACC-119](../12_ACCEPTANCE_SCENARIOS/acc_119_derived_projection_destructive_rebuild.md) — Critical | *(name the test case)* |
| C130 | Missing Upstream Licence or Provenance | [ACC-120](../12_ACCEPTANCE_SCENARIOS/acc_120_missing_upstream_license_provenance.md) — High | *(name the test case)* |

**130 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Entry conditions** | **E2** | Attempt cutover with any go-live entry condition unmet | **Refused**, naming the condition | One refusal per unmet condition |
| **TC-02** Open critical | **E2** | Attempt with an open Critical finding | Refused | Refusal transcript |
| **TC-03** Expired residual | **E2** | Attempt with a residual-risk acceptance past its expiry | Refused — an expired acceptance is an open finding | Refusal transcript |
| **TC-04** Two rehearsals | **E2** | Attempt with only one restore rehearsal | Refused | Refusal transcript |
| **TC-05** **Digest freeze** | **E1** | Freeze RC, policy, schema, model, tool and infrastructure digests | All six recorded; the set is signed | Freeze record |
| **TC-06** Unfrozen component | **E2** | Attempt with any component referenced by tag | Refused (WP-027) | Refusal transcript |
| **TC-07** **Verified restore point** | **E1** | Take the pre-cutover backup and **verify it** | Restore point verified, not merely taken; owner check complete | Verification record |
| **TC-08** Unverified restore point | **E2** | Proceed with an unverified backup | **Refused** — `PR-13` at the worst possible moment | Refusal transcript |
| **TC-09** Deployment | **E1** | Apply IaC/GitOps deployment and migrations | Applied; a second apply is a no-op | Deployment record |
| **TC-10** Migration rollback ready | **E1** | Confirm each migration has a rehearsed rollback | All do | Migration report |
| **TC-11** Service smoke | **E1** | Run the service smoke tests | All pass on the promoted RC | Smoke report |
| **TC-12** Contract smoke | **E1** | Run contract tests | Every producer/consumer pair green | Contract report |
| **TC-13** Security smoke | **E1** | Run the security smoke set | Fail-closed behaviours confirmed on the live configuration | Security report |
| **TC-14** **Integrity smoke** | **E1** | Run the integrity queries | Referential closure holds post-migration | Integrity report |
| **TC-15** **Sequenced enablement** | **E1** | Enable traffic, access and monitoring in the declared order | Each step observed before the next; **each reversible** | Enablement log |
| **TC-16** Reverse a step | **E1** | Reverse one enablement step | Reverses cleanly | Reversal transcript |
| **TC-17** **Abort available** | **E1** | Confirm abort is available at each stage | Available throughout, including after promotion | Abort readiness record |
| **TC-18** Abort exercised | **E1** | Exercise abort at a declared threshold in the rehearsal environment | Returns to the verified restore point | Abort transcript |
| **TC-19** Abort authority | **E2** | Attempt abort by an unauthorised actor, and delegate it | Both refused (WP-001, WP-004) | Two refusals |
| **TC-20** **Go-Live `DecisionRecord`** | **E1** | Record the decision | Names the actor, the evidence, the residual risks with owners and expiries, and **what was not authorised** | `DecisionRecord` |
| **TC-21** No-go reachable | **E1** | Confirm `no-go` and `abort` are recordable outcomes | Both supported | Decision options |
| **TC-22** **Post-cutover snapshot** | **E1** | Take the audit snapshot | Hash-chained; verifies standalone; becomes the baseline for later checks | Snapshot |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-120 # dependencies and their states
python3 scripts/ready_queue.py         # this package must appear under "Ready now"
```

Record the revision in the execution log header. **Results from two revisions are
not evidence** — `00_PROGRAM/05` requires all criteria to pass on the same one.

### Running a case

1. Work in an isolated workspace (`skills/using-isolated-environments`), not in
   the producer's tree.
2. Run the case exactly as written. A deviation is recorded in the completion
   report (§7.4.3), never silently absorbed.
3. Capture the **actual** result verbatim — not a summary of it (§8.9).
4. Compare against the expected result and record a verdict.
5. On any mismatch, raise an incident (§8.11) before continuing.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-120 --gate Cutover \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-120/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-120
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_120_production_cutover.acceptance.md) reaches the decision — issuance is not acceptance.

## Test execution log — §8.10

One row per executed case. The log is evidence and is written **as the run happens**, not reconstructed afterwards.

| Case | Date/time (UTC) | Executed by | Revision | Actual result | Verdict | Evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

## Incident reporting — §8.11

Any deviation between an actual and an expected result raises an incident carrying timing, originator, context, description, the originator's assessment of **severity** and **priority**, the risk, and a status. An incident is not closed by the person who raised it deciding it was probably fine: `00_PROGRAM/06` requires a reproducer result before a critical finding can be closed.

| Incident | Raised | Case | Severity | Priority | Risk | Status | Disposition |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Test completion report — §7.4

Written once, at the end of the run, and handed to the verifier with the evidence package.

- **Summary of testing performed:**
- **Deviations from this procedure** (including every skipped case and why):
- **Completion evaluation** against the exit criteria below:
- **Factors that blocked progress:**
- **Test measures** (cases executed / passed / failed / blocked; coverage items reached):
- **Residual risks**, each with an owner and an expiry:
- **Test deliverables** produced:
- **Reusable test assets:**
- **Lessons learned:**

## Exit criteria

<!-- generated:exit — produced by scripts/make_package_companions.py; do not edit inside this block -->

The run is complete when every line holds. These are conditions on the **testing**, not on the package: a complete test run that found defects is complete.

- [ ] Every coverage item above is named by at least one executed test case.
- [ ] Every executed test case has an actual result and a verdict (§8.9).
- [ ] Every case at layer **E2** has been observed to **fail** in its negative direction. A control that has only ever passed has not been tested.
- [ ] Every deviation from this procedure is recorded in the completion report (§7.4.3) — including cases that were skipped and why.
- [ ] Every incident raised has a severity, a priority and a status (§8.11).
- [ ] All results are bound to **one** target revision.
- [ ] The residual risk list is written, with an owner and an expiry for each entry (§7.4.7).

> **Not an exit condition.** That every test passed. A procedure that can only complete on success has no way to report a defect, which is the outcome it exists to produce.

<!-- /generated:exit -->
