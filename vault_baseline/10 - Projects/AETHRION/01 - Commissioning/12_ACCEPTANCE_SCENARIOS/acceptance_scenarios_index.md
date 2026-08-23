---
title: "ACC-01 – ACC-120 System Acceptance Scenarios"
cssclasses:
  - aethrion-index
type: index
category: commissioning
status: SPECIFIED
summary: "These are the binding scenarios for production commissioning."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/acceptance_scenarios_index.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/index
---

# ACC-01 – ACC-120 System Acceptance Scenarios

| Field | Value |
|---|---|
| Document type | Index — generated from the scenario files |
| Scope | All system acceptance scenarios, their severity, owner and acceptance phase |
| Sibling documents | `../00_PROGRAM/06_evidence_and_acceptance_strategy.md` · `../00_PROGRAM/10_go_live_checklist.md` |
| Status | `SPECIFIED` — every scenario is written; **none has ever been run** |
| Date | 2026-08-22 |

**In one paragraph.** These are the binding scenarios for production commissioning. Every one runs on the same release candidate, with an independent witness, and produces a signed evidence manifest. Roughly half pass by demonstrating that the system correctly **refused** to act — a scenario that verifies a refusal is as important as one that verifies a success. Each scenario declares an **acceptance phase**: `PRE_GO_LIVE` scenarios must pass before cutover, while `DAY2_CONTINUOUS` scenarios describe recurring operational rhythms that cannot be a precondition of the go-live that precedes them.

---

## 1. Acceptance phases

| Phase | Meaning | Gate on go-live |
|---|---|---|
| `PRE_GO_LIVE` | Must PASS on the release candidate before cutover | **Blocking** |
| `DAY2_CONTINUOUS` | A recurring rhythm, armed and scheduled at cutover and exercised afterwards | Armed, not passed |

> **Why the split exists.** Baseline v1.0 required all scenarios to pass before WP-120 cutover, while six of them referenced Day-2 packages that hard-depend on WP-121 programme closure — which happens *after* cutover. That made go-live require work that can only exist after go-live. The phase field breaks the cycle: initial qualification is `PRE_GO_LIVE` and owned by a commissioning package, while the recurring counterpart stays in Day-2 and is named in the scenario's `Recurring counterpart` field.

---

## 2. Scenario index

| Scenario | Category | Severity | Phase | Owner | Related packages |
|---|---|---|---|---|---|
| [ACC-01 — Human Seed Literature](acc_01_human_seed_literature.md) | Research/Literature | Critical | `PRE_GO_LIVE` | Knowledge Lead | WP-035, WP-050, WP-062, WP-064, WP-065, WP-069, WP-070, WP-072, WP-094, WP-103, WP-110, WP-115, WP-119, WP-120 |
| [ACC-02 — Agent-Used Source Write-Back](acc_02_agent_used_source_writeback.md) | Research/Literature | Critical | `PRE_GO_LIVE` | Evidence Lead | WP-050, WP-064, WP-066, WP-070, WP-072, WP-094, WP-103 |
| [ACC-03 — Duplicate and Metadata Collision](acc_03_duplicate_collision.md) | Research/Literature | High | `PRE_GO_LIVE` | Source Resolver Lead | WP-012, WP-061, WP-062, WP-066, WP-067, WP-094, WP-103 |
| [ACC-04 — Retraction Impact](acc_04_retraction_impact.md) | Research/Monitoring | Critical | `PRE_GO_LIVE` | Knowledge Monitoring Lead | WP-037, WP-063, WP-072, WP-075, WP-076, WP-094, WP-095, WP-106, WP-108, WP-137 |
| [ACC-05 — Prompt-Injection PDF](acc_05_prompt_injection_pdf.md) | Security/Literature | Critical | `PRE_GO_LIVE` | Content Security Lead | WP-049, WP-050, WP-051, WP-058, WP-060, WP-103, WP-136 |
| [ACC-06 — Planner Self-Approval Attempt](acc_06_plan_self_approval.md) | Governance/Assurance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-000, WP-003, WP-007, WP-056, WP-060, WP-086, WP-088, WP-102, WP-105, WP-107, WP-147 |
| [ACC-07 — Reviewer Order Bias](acc_07_reviewer_order_bias.md) | Model/Eval | High | `PRE_GO_LIVE` | Eval Office | WP-043, WP-086, WP-088, WP-105 |
| [ACC-08 — Strong Counter-Test](acc_08_strong_counter_test.md) | Research/Assurance | Critical | `PRE_GO_LIVE` | Falsification Lead | WP-018, WP-036, WP-075, WP-077, WP-087, WP-088, WP-089, WP-095, WP-104, WP-105, WP-110 |
| [ACC-09 — Budget Hard Stop](acc_09_budget_hard_stop.md) | FinOps/Reliability | Critical | `PRE_GO_LIVE` | FinOps Lead | WP-041, WP-045, WP-053, WP-060, WP-083, WP-100, WP-104, WP-111, WP-145 |
| [ACC-10 — Primary Model Provider Outage](acc_10_provider_outage.md) | Reliability/Model | High | `PRE_GO_LIVE` | Model Platform Lead | WP-040, WP-041, WP-044, WP-045, WP-111 |
| [ACC-11 — No Eligible Fallback](acc_11_no_eligible_fallback.md) | Reliability/Model | Critical | `PRE_GO_LIVE` | Model Platform Lead | WP-040, WP-041, WP-045, WP-111 |
| [ACC-12 — Duplicate Event Delivery](acc_12_duplicate_event.md) | Reliability/Event | Critical | `PRE_GO_LIVE` | Event Platform Lead | WP-015, WP-028, WP-039, WP-049, WP-111 |
| [ACC-13 — Temporal Worker Crash](acc_13_temporal_worker_crash.md) | Reliability/Control | Critical | `PRE_GO_LIVE` | Control Plane Lead | WP-031, WP-032, WP-040, WP-111 |
| [ACC-14 — Workflow Code Deployment and Replay](acc_14_workflow_code_deploy.md) | Reliability/Control | Critical | `PRE_GO_LIVE` | Platform Assurance Lead | WP-031, WP-032, WP-040, WP-111 |
| [ACC-15 — Sandbox Escape Attempt](acc_15_sandbox_escape.md) | Security/Execution | Critical | `PRE_GO_LIVE` | Execution Security Lead | WP-006, WP-054, WP-060, WP-112 |
| [ACC-16 — Egress Exfiltration Attempt](acc_16_egress_exfiltration.md) | Security/Network | Critical | `PRE_GO_LIVE` | Network Security Lead | WP-051, WP-057, WP-060, WP-112 |
| [ACC-17 — Unsigned or Mutable Image](acc_17_unsigned_image.md) | Security/Supply Chain | Critical | `PRE_GO_LIVE` | Supply Chain Security Lead | WP-027, WP-054, WP-059, WP-060, WP-087, WP-107, WP-112 |
| [ACC-18 — D3 Data to a Public Provider](acc_18_d3_public_route.md) | Security/Privacy | Critical | `PRE_GO_LIVE` | Safety & Governance Owner | WP-006, WP-021, WP-041, WP-045, WP-056, WP-057, WP-060, WP-112 |
| [ACC-19 — Clean-Room Reproduction Pass](acc_19_clean_room_pass.md) | Evidence/Reproduction | High | `PRE_GO_LIVE` | Reproducibility Lead | WP-019, WP-036, WP-077, WP-084, WP-085, WP-105, WP-113 |
| [ACC-20 — Clean-Room Reproduction Failure](acc_20_clean_room_fail.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-019, WP-036, WP-077, WP-084, WP-085, WP-105, WP-113 |
| [ACC-21 — Derived Graph Corruption and Rebuild](acc_21_graph_corruption.md) | Data/Knowledge | High | `PRE_GO_LIVE` | Knowledge Data Lead | WP-012, WP-030, WP-074, WP-095, WP-113, WP-114 |
| [ACC-22 — Obsidian Human Edit Preservation](acc_22_obsidian_human_edit.md) | Knowledge | High | `PRE_GO_LIVE` | Knowledge Lead | WP-012, WP-073, WP-074, WP-113 |
| [ACC-23 — Artifact Overwrite Attempt](acc_23_artifact_overwrite.md) | Data/Integrity | Critical | `PRE_GO_LIVE` | Data Platform Lead | WP-014, WP-026, WP-087, WP-104, WP-107, WP-113, WP-139 |
| [ACC-24 — Policy Bundle Rollback](acc_24_policy_bundle_rollback.md) | Security/Governance | High | `PRE_GO_LIVE` | Policy Platform Lead | WP-009, WP-056, WP-112 |
| [ACC-25 — Human Approval Forgery](acc_25_human_approval_forgery.md) | Security/Governance | Critical | `PRE_GO_LIVE` | Governance Lead | WP-004, WP-038, WP-055, WP-060, WP-093, WP-102, WP-106, WP-112, WP-135 |
| [ACC-26 — Approval, Delegation and Exception Expiry](acc_26_approval_expiry.md) | Governance | Critical | `PRE_GO_LIVE` | Safety & Governance Owner | WP-004, WP-009, WP-038, WP-055, WP-056, WP-059, WP-093, WP-102, WP-112, WP-134, WP-135 |
| [ACC-27 — Regional / Management Plane DR](acc_27_regional_dr.md) | Operations/DR | Critical | `PRE_GO_LIVE` | SRE Lead | WP-021, WP-025, WP-026, WP-052, WP-114 |
| [ACC-28 — Zotero Full Resync](acc_28_zotero_full_resync.md) | Literature/DR | High | `PRE_GO_LIVE` | Knowledge Platform Lead | WP-061, WP-062, WP-067, WP-094, WP-103, WP-114 |
| [ACC-29 — Provider Invoice Variance](acc_29_invoice_variance.md) | FinOps | Medium | `PRE_GO_LIVE` | FinOps Lead | WP-100, WP-111 |
| [ACC-30 — Publication Completeness](acc_30_publication_completeness.md) | Publication/Evidence | Critical | `PRE_GO_LIVE` | Provenance Curator | WP-018, WP-036, WP-072, WP-075, WP-076, WP-080, WP-087, WP-090, WP-095, WP-106, WP-113, WP-138 |
| [ACC-31 — Superseded Publication](acc_31_superseded_publication.md) | Publication/Monitoring | High | `PRE_GO_LIVE` | Publication Owner | WP-037, WP-074, WP-075, WP-090, WP-095, WP-106, WP-108, WP-113, WP-137 |
| [ACC-32 — Secret in Prompt or Trace](acc_32_secret_in_trace.md) | Security/Observability | Critical | `PRE_GO_LIVE` | AI Observability Lead | WP-057, WP-060, WP-097, WP-104, WP-112 |
| [ACC-33 — Kueue Preemption](acc_33_kueue_preemption.md) | Execution/Reliability | High | `PRE_GO_LIVE` | Compute Platform Lead | WP-052, WP-053, WP-083, WP-111 |
| [ACC-34 — DLQ Repair and Corrected Replay](acc_34_dlq_repair.md) | Event/Reliability | High | `PRE_GO_LIVE` | Event Platform Lead | WP-015, WP-028, WP-039, WP-111 |
| [ACC-35 — Tool Partial Failure](acc_35_tool_partial_failure.md) | Tool/Reliability | Critical | `PRE_GO_LIVE` | Tool Platform Lead | WP-038, WP-040, WP-049, WP-050, WP-066, WP-111 |
| [ACC-36 — Model Snapshot Drift](acc_36_model_snapshot_drift.md) | Model/Monitoring | Critical | `PRE_GO_LIVE` | Eval Office | WP-037, WP-042, WP-044, WP-106, WP-108, WP-137 |
| [ACC-37 — Evaluation Set Contamination](acc_37_eval_contamination.md) | Model/Eval/Security | Critical | `PRE_GO_LIVE` | Eval Office | WP-043, WP-044, WP-060, WP-112 |
| [ACC-38 — Critical Reviewer Unavailable](acc_38_reviewer_unavailable.md) | Assurance/Operations | High | `PRE_GO_LIVE` | Assurance Lead | WP-003, WP-007, WP-045, WP-088, WP-105, WP-113 |
| [ACC-39 — Negative Research Result](acc_39_negative_result.md) | Research/Portfolio | Medium | `PRE_GO_LIVE` | Scientific Owner | WP-035, WP-081, WP-082, WP-083, WP-104, WP-113 |
| [ACC-40 — Complete Project Audit Export](acc_40_audit_export.md) | Audit/Operations | Critical | `PRE_GO_LIVE` | Internal Audit Lead | WP-090, WP-099, WP-106, WP-109, WP-112, WP-114, WP-119, WP-139 |
| [ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling](acc_41_notification_data_class_ceiling.md) | Communication/Security | Critical | `PRE_GO_LIVE` | Platform Security Lead | WP-131, WP-132, WP-133 |
| [ACC-42 — Notification Broker Unavailable During an Escalating Condition](acc_42_notification_broker_outage.md) | Communication/Reliability | High | `PRE_GO_LIVE` | Platform Operations Lead | WP-131, WP-140 |
| [ACC-43 — Escalation Timeout and Dead-Man's Switch](acc_43_escalation_and_dead_mans_switch.md) | Communication/Governance | Critical | `PRE_GO_LIVE` | Platform Operations Lead | WP-134, WP-140 |
| [ACC-44 — Inbound Content Attempts to Act as an Instruction](acc_44_inbound_message_is_not_an_instruction.md) | Security/Communication | Critical | `PRE_GO_LIVE` | Content Security Lead | WP-058, WP-136 |
| [ACC-45 — Irreversible External Record Submission](acc_45_external_record_submission.md) | External/Governance | Critical | `PRE_GO_LIVE` | Data Steward | WP-138, WP-139 |
| [ACC-46 — Task Runs With No Skill Loaded](acc_46_skill_not_loaded.md) | Agent/Skill Governance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-013, WP-046, WP-047, WP-048 |
| [ACC-47 — Harness Starts Without the Skill Bootstrap](acc_47_skill_bootstrap_missing.md) | Agent/Skill Governance | Critical | `PRE_GO_LIVE` | Model Platform Lead | WP-047, WP-048 |
| [ACC-48 — Wrong or Competing Skill Selected](acc_48_wrong_skill_selected.md) | Agent/Skill Governance | High | `PRE_GO_LIVE` | Eval Office | WP-013, WP-043, WP-047 |
| [ACC-49 — Non-Waivable Skill Ignored Under Pressure](acc_49_skill_ignored_under_pressure.md) | Agent/Skill Governance | Critical | `PRE_GO_LIVE` | Red Team Lead | WP-043, WP-046, WP-048, WP-088 |
| [ACC-50 — Procedure Lost to Context Compaction or Restart](acc_50_skill_lost_on_compaction.md) | Agent/Skill Governance | High | `PRE_GO_LIVE` | Control Plane Lead | WP-046, WP-048 |
| [ACC-51 — Upstream Change Invalidates a Derived Skill](acc_51_upstream_skill_drift.md) | Agent/Skill Governance | High | `PRE_GO_LIVE` | Knowledge Steward | WP-013, WP-047, WP-115, WP-120 |
| [ACC-52 — Claimless Publication Assertion](acc_52_claimless_publication_assertion.md) | Publication/Evidence | Critical | `PRE_GO_LIVE` | Provenance Curator | WP-018, WP-080, WP-090, WP-106, WP-113 |
| [ACC-53 — Unverified Numeric Result](acc_53_unverified_numeric_result.md) | Publication/Evidence | Critical | `PRE_GO_LIVE` | Provenance Curator | WP-082, WP-087, WP-090, WP-106 |
| [ACC-54 — Producer Attempts Evaluator Mutation](acc_54_evaluator_mutation_attempt.md) | Security/Execution | Critical | `PRE_GO_LIVE` | Execution Security Lead | WP-023, WP-054, WP-083, WP-084 |
| [ACC-55 — Hidden Evaluation Data Access Attempt](acc_55_hidden_evaluation_data_access.md) | Security/Execution | Critical | `PRE_GO_LIVE` | Execution Security Lead | WP-054, WP-057, WP-060, WP-084 |
| [ACC-56 — Confirmatory Result Without a Frozen Analysis Plan](acc_56_confirmatory_without_frozen_plan.md) | Research/Assurance | Critical | `PRE_GO_LIVE` | Research Director | WP-008, WP-081, WP-142 |
| [ACC-57 — Hypothesis In-Place Mutation Attempt](acc_57_hypothesis_in_place_mutation.md) | Data/Integrity | High | `PRE_GO_LIVE` | Evidence Platform Lead | WP-018, WP-143 |
| [ACC-58 — Cross-Branch Fusion Lineage](acc_58_cross_branch_fusion_lineage.md) | Discovery/Evidence | High | `PRE_GO_LIVE` | Experiment Platform Lead | WP-014, WP-144, WP-145 |
| [ACC-59 — Discovery Search Stagnation](acc_59_discovery_search_stagnation.md) | Discovery/FinOps | High | `PRE_GO_LIVE` | Experiment Platform Lead | WP-100, WP-145 |
| [ACC-60 — Failed Smoke Candidate Promotion Attempt](acc_60_failed_smoke_promotion.md) | Experiment/Assurance | Critical | `PRE_GO_LIVE` | Experiment Platform Lead | WP-083, WP-087 |
| [ACC-61 — Unqualified Semantic Verifier](acc_61_unqualified_semantic_verifier.md) | Assurance/Model | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-044, WP-087 |
| [ACC-62 — Semantic Verifier Recorded as Mechanical](acc_62_verifier_class_misdeclaration.md) | Assurance/Contracts | High | `PRE_GO_LIVE` | Chief Architect | WP-018, WP-087 |
| [ACC-63 — Failed Experiment Must Be Recorded](acc_63_failed_experiment_recorded.md) | Experiment/Knowledge | High | `PRE_GO_LIVE` | Experiment Platform Lead | WP-082, WP-146 |
| [ACC-64 — Implementation Failure Must Not Refute a Hypothesis](acc_64_implementation_failure_not_refutation.md) | Research/Integrity | Critical | `PRE_GO_LIVE` | Research Director | WP-082, WP-143, WP-144 |
| [ACC-65 — Reproduction in the Producer Environment](acc_65_reproduction_in_producer_environment.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-007, WP-084, WP-085 |
| [ACC-66 — Standalone Reproduction Package](acc_66_standalone_reproduction_package.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-085, WP-105 |
| [ACC-67 — Claim–Code–Result Consistency Failure](acc_67_claim_code_result_consistency.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-085, WP-087, WP-113 |
| [ACC-68 — Human Intervention Without an Audit Record](acc_68_human_intervention_audit.md) | Governance/Audit | Critical | `PRE_GO_LIVE` | Governance Lead | WP-038, WP-093, WP-099 |
| [ACC-69 — Human Decision Timeout Must Not Auto-Approve](acc_69_decision_timeout_no_autoapproval.md) | Governance | Critical | `PRE_GO_LIVE` | Project Decision Owner | WP-004, WP-093, WP-132 |
| [ACC-70 — EvidenceGap Lifecycle](acc_70_evidence_gap_lifecycle.md) | Evidence/Knowledge | High | `PRE_GO_LIVE` | Evidence Lead | WP-075, WP-077, WP-146 |
| [ACC-71 — Multi-Parent Artifact Lineage](acc_71_artifact_multi_parent_lineage.md) | Data/Integrity | Critical | `PRE_GO_LIVE` | Data Platform Lead | WP-014, WP-026, WP-030 |
| [ACC-72 — Reviewer Isolation Before Review Lock](acc_72_reviewer_isolation_before_lock.md) | Governance/Assurance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-007, WP-086, WP-088, WP-147 |
| [ACC-73 — Upstream Assimilation Drift](acc_73_upstream_assimilation_drift.md) | Supply Chain | High | `DAY2_CONTINUOUS` | Supply Chain Security Lead | WP-059, WP-130, WP-141 |
| [ACC-74 — Missing Upstream Lineage or Licence](acc_74_missing_upstream_lineage.md) | Supply Chain | High | `PRE_GO_LIVE` | Supply Chain Security Lead | WP-024, WP-059, WP-141 |
| [ACC-75 — Literature Retrieval Budget and Stopping Rule](acc_75_retrieval_budget_and_stopping_rule.md) | Research/Literature | High | `PRE_GO_LIVE` | Knowledge Lead | WP-069, WP-071, WP-072 |
| [ACC-76 — Unsupported Publication Sentence](acc_76_unsupported_publication_sentence.md) | Publication/Evidence | Critical | `PRE_GO_LIVE` | Citation Auditor | WP-080, WP-087, WP-090 |
| [ACC-77 — VerifiedValue Rebinding Attempt](acc_77_verified_value_rebinding.md) | Data/Integrity | Critical | `PRE_GO_LIVE` | Evidence Platform Lead | WP-082, WP-087 |
| [ACC-78 — Raw Evidence Versus Interpretation](acc_78_raw_evidence_versus_interpretation.md) | Data/Integrity | Critical | `PRE_GO_LIVE` | Evidence Lead | WP-026, WP-075, WP-077 |
| [ACC-79 — Epistemic Memory Retention Violation](acc_79_memory_retention_violation.md) | Data/Knowledge | High | `PRE_GO_LIVE` | Knowledge Lead | WP-026, WP-146 |
| [ACC-80 — Governed Versus Ungoverned Research Harness](acc_80_governed_versus_ungoverned_harness.md) | Metascience | Medium | `DAY2_CONTINUOUS` | Research Director | WP-043, WP-110, WP-130 |
| [ACC-081 — Multi-Agent Cohort Required](acc_081_multi_agent_cohort_required.md) | Collaboration/Governance | Critical | `PRE_GO_LIVE` | Research Director | WP-047, WP-148 |
| [ACC-082 — Independent-First Embargo](acc_082_independent_first_embargo.md) | Collaboration/Assurance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-148, WP-149 |
| [ACC-083 — Typed Inter-Agent Message](acc_083_typed_inter_agent_message.md) | Collaboration/Contracts | High | `PRE_GO_LIVE` | Chief Architect | WP-015, WP-149 |
| [ACC-084 — Delta-Only Communication](acc_084_delta_only_communication.md) | Collaboration/Efficiency | High | `PRE_GO_LIVE` | Chief Architect | WP-149, WP-150 |
| [ACC-085 — A Blackboard Entry Is Not Evidence](acc_085_blackboard_entry_is_not_evidence.md) | Collaboration/Evidence | Critical | `PRE_GO_LIVE` | Evidence Lead | WP-075, WP-149 |
| [ACC-086 — Sparse Topology Preserves Quality](acc_086_sparse_topology_quality_preservation.md) | Collaboration/Efficiency | High | `PRE_GO_LIVE` | Chief Architect | WP-149, WP-150, WP-158 |
| [ACC-087 — Communication Optimisation Rollback](acc_087_communication_optimization_rollback.md) | Collaboration/Efficiency | High | `PRE_GO_LIVE` | Chief Architect | WP-150 |
| [ACC-088 — Strategic Silence Never Silences a Blocker](acc_088_strategic_silence_never_silences_a_blocker.md) | Collaboration/Safety | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-150 |
| [ACC-089 — Sycophancy Anchor Attack](acc_089_sycophancy_anchor_attack.md) | Collaboration/Assurance | Critical | `PRE_GO_LIVE` | Eval Office | WP-088, WP-148 |
| [ACC-090 — False Consensus Cannot Close a Challenge](acc_090_false_consensus.md) | Collaboration/Assurance | Critical | `PRE_GO_LIVE` | Research Director | WP-089, WP-148 |
| [ACC-091 — Faulty Agent Output Does Not Propagate](acc_091_faulty_agent_challenge.md) | Collaboration/Resilience | Critical | `PRE_GO_LIVE` | Incident Commander / SRE Lead | WP-148, WP-152 |
| [ACC-092 — Inspector Reviews High-Consequence Output](acc_092_inspector_high_consequence_review.md) | Collaboration/Assurance | High | `PRE_GO_LIVE` | Assurance Lead | WP-152, WP-155 |
| [ACC-093 — A Malicious Agent Cannot Bind Authority](acc_093_malicious_agent_cannot_bind_authority.md) | Security/Collaboration | Critical | `PRE_GO_LIVE` | Red Team Lead | WP-060, WP-148, WP-152 |
| [ACC-094 — An Unattributable Failure Is `UNKNOWN`](acc_094_failure_cause_unknown.md) | Resilience/Diagnostics | High | `PRE_GO_LIVE` | Incident Commander / SRE Lead | WP-152 |
| [ACC-095 — Failure Taxonomy Routing](acc_095_failure_taxonomy_routing.md) | Resilience/Diagnostics | High | `PRE_GO_LIVE` | Incident Commander / SRE Lead | WP-082, WP-152 |
| [ACC-096 — A Refuted Memory Does Not Re-Enter Reasoning](acc_096_refuted_memory_mask.md) | Knowledge/Assurance | High | `PRE_GO_LIVE` | Knowledge Lead | WP-146, WP-151 |
| [ACC-097 — Proactive Reminder of a Frozen Constraint](acc_097_proactive_frozen_constraint_reminder.md) | Knowledge/Assurance | High | `PRE_GO_LIVE` | Knowledge Lead | WP-151 |
| [ACC-098 — Memory Poisoning Attempt](acc_098_memory_poisoning_attempt.md) | Security/Knowledge | Critical | `PRE_GO_LIVE` | Content Security Lead | WP-058, WP-146, WP-151 |
| [ACC-099 — Budget Degrades Communication, Not the Cohort](acc_099_communication_budget_degradation.md) | FinOps/Collaboration | Critical | `PRE_GO_LIVE` | FinOps Lead | WP-150, WP-153 |
| [ACC-100 — Token Ledger Classification](acc_100_token_ledger_classification.md) | FinOps/Observability | High | `PRE_GO_LIVE` | FinOps Lead | WP-100, WP-153 |
| [ACC-101 — Reserved Assurance Budget Is Unreachable](acc_101_budget_hard_stop_reserved_assurance.md) | FinOps/Assurance | Critical | `PRE_GO_LIVE` | FinOps Lead | WP-145, WP-153 |
| [ACC-102 — Deterministic Tool-Result Reuse](acc_102_tool_result_reuse.md) | FinOps/Efficiency | Medium | `PRE_GO_LIVE` | FinOps Lead | WP-049, WP-153 |
| [ACC-103 — Minor Specification Drift Is Recorded](acc_103_scientific_minor_spec_drift.md) | Engineering/Assurance | High | `PRE_GO_LIVE` | Chief Architect | WP-081, WP-154 |
| [ACC-104 — Major Specification Drift Blocks Confirmatory Status](acc_104_scientific_major_spec_drift.md) | Engineering/Assurance | Critical | `PRE_GO_LIVE` | Research Director | WP-081, WP-154 |
| [ACC-105 — A Claim Without a Complete Evidence Chain](acc_105_claim_without_evidence_chain.md) | Evidence/Publication | Critical | `PRE_GO_LIVE` | Evidence Lead | WP-075, WP-080, WP-090 |
| [ACC-106 — A Number Without a VerifiedValue](acc_106_numeric_value_without_verifiedvalue.md) | Evidence/Publication | Critical | `PRE_GO_LIVE` | Provenance Curator | WP-082, WP-090 |
| [ACC-107 — Expired Verifier Qualification](acc_107_expired_verifier_qualification.md) | Assurance/Model | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-044, WP-155 |
| [ACC-108 — Escalation Is Not Selective Enforcement](acc_108_selective_verifier_escalation.md) | Assurance/Governance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-155 |
| [ACC-109 — Verifier Abstention Is a Valid Result](acc_109_verifier_abstention_is_valid.md) | Assurance/Model | High | `PRE_GO_LIVE` | Eval Office | WP-044, WP-155 |
| [ACC-110 — Human Preliminary Assessment Precedes the Recommendation](acc_110_human_preliminary_assessment.md) | Governance/Human | Critical | `PRE_GO_LIVE` | Project Decision Owner | WP-093, WP-156 |
| [ACC-111 — Insufficient Basis Is Reachable](acc_111_human_insufficient_basis.md) | Governance/Human | High | `PRE_GO_LIVE` | Project Decision Owner | WP-004, WP-156 |
| [ACC-112 — Correction Friction Symmetry](acc_112_correction_friction_symmetry.md) | Governance/Human | High | `PRE_GO_LIVE` | Project Decision Owner | WP-093, WP-156 |
| [ACC-113 — Producer to Evaluator Leakage](acc_113_producer_evaluator_leakage.md) | Security/Evidence | Critical | `PRE_GO_LIVE` | Execution Security Lead | WP-084, WP-157 |
| [ACC-114 — Reproduction Environment Lineage](acc_114_reproduction_in_producer_environment_hardened.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-085, WP-157 |
| [ACC-115 — Missing Model Execution Fingerprint](acc_115_missing_model_execution_fingerprint.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-082, WP-157 |
| [ACC-116 — Distributional Reproduction for a Hosted Model](acc_116_distributional_hosted_model_reproduction.md) | Evidence/Reproduction | High | `PRE_GO_LIVE` | Reproducibility Lead | WP-085, WP-157 |
| [ACC-117 — Prompt Injection Meets a Capability Gate](acc_117_prompt_injection_capability_gate.md) | Security/Execution | Critical | `PRE_GO_LIVE` | Content Security Lead | WP-058, WP-060, WP-136 |
| [ACC-118 — Search-Time Benchmark Contamination](acc_118_benchmark_search_time_contamination.md) | Evaluation/Integrity | Critical | `PRE_GO_LIVE` | Eval Office | WP-057, WP-158 |
| [ACC-119 — Destructive Projection Rebuild](acc_119_derived_projection_destructive_rebuild.md) | Data/Integrity | Critical | `PRE_GO_LIVE` | Data Platform Lead | WP-030, WP-159 |
| [ACC-120 — Missing Upstream Licence or Provenance](acc_120_missing_upstream_license_provenance.md) | Supply Chain | High | `PRE_GO_LIVE` | Supply Chain Security Lead | WP-059, WP-141, WP-159 |

---

## 3. Counts

| Measure | Value |
|---|---:|
| Scenarios | **120** |
| Critical | 74 |
| High | 42 |
| Medium | 4 |
| `PRE_GO_LIVE` | 118 |
| `DAY2_CONTINUOUS` | 2 |

> **Two scenarios carry `DAY2_CONTINUOUS`** — ACC-73 and ACC-80 — and both do so
> for the same structural reason: each names a Day-2 package, and a `PRE_GO_LIVE`
> scenario that depends on Day-2 work would make go-live require work that can
> only happen after go-live. That is the exact cycle the phase field was
> introduced to break, and `validate_commissioning_plan.py` rule 6 refuses it.
> Every other recurring rhythm remains owned by WP-122 – WP-130 rather than by a
> scenario, and a scenario whose initial qualification is `PRE_GO_LIVE` names its
> Day-2 counterpart in its `Recurring counterpart` field instead.

> These counts are **derived from the scenario files** by `scripts/validate_commissioning_plan.py`, which fails when the index and the files disagree. They are not maintained by hand, because hand-maintained counts are the most common drift in this plan.

---

## 4. Rules

- A Critical scenario can never be counted as PASS through a SKIP or a waiver.
- All `PRE_GO_LIVE` scenarios run against the same RC digest and bundle baseline.
- When a new RC is produced, at minimum the affected scenarios plus the platform baseline regression are rerun.
- Final go-live condition: **every `PRE_GO_LIVE` scenario PASSes**, zero open Critical findings, every `DAY2_CONTINUOUS` scenario armed, and a verified Commissioning Dossier.

## 5. Added after baseline v1.0

| Range | Subject | Why the baseline could not ship without them |
|---|---|---|
| ACC-41 – ACC-45 | Notification ceiling · broker outage · escalation and dead-man's switch · inbound content · external submission | The `13_TOOLING_INTEGRATION` packages referenced these scenario numbers, and the scenarios did not exist |
| ACC-46 – ACC-51 | Skill governance | Nothing tested the skill layer: a registry that loads nowhere, a procedure dropped at compaction, or a non-waivable rule that evaporates under deadline pressure would all have passed commissioning unnoticed |
| ACC-52 – ACC-80 | Evidence-native scientific integrity | Added at baseline v1.2.0. The earlier set tested the platform — isolation, replay, budget, supply chain, notification. It did not test the epistemic path: nothing refused a publication sentence with no claim behind it, a number with no verified value under it, a producer editing its own evaluator, a compile error recorded as a refuted hypothesis, or a reproduction run in the environment that produced the result. Those are the failures this architecture exists to prevent, and none of them had a scenario |
| ACC-081 – ACC-120 | Multi-agent reliability and efficiency | Added at baseline v1.3.0. The set to this point tested a *pipeline*; it did not test a **cohort**. Nothing refused a single-agent downgrade of substantial work, caught a confident wrong answer becoming consensus, stopped a budget optimiser from cutting assurance instead of verbosity, noticed an implementation quietly diverging from a frozen method, or told a benchmark score that had seen the answers from one that had not. These are the failure modes a multi-agent system adds, and none of them had a scenario |

---

## 7. Identifier width

Scenarios up to `ACC-99` carry two digits; `ACC-100` onward carries three. Nothing
was renumbered when the set passed ninety-nine — `ACC-07` is `ACC-07` permanently,
and every existing reference keeps resolving. The validators accept both widths
and sort numerically, so `ACC-100` follows `ACC-99` rather than `ACC-1`.
