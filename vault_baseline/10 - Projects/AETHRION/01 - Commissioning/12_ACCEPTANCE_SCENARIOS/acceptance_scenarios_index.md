# ACC-01 – ACC-51 System Acceptance Scenarios

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
| [ACC-01 — Human Seed Literature](ACC-01_human_seed_literature.md) | Research/Literature | Critical | `PRE_GO_LIVE` | Knowledge Lead | WP-065, WP-062, WP-069, WP-072, WP-103 |
| [ACC-02 — Agent-Used Source Write-Back](ACC-02_agent_used_source_writeback.md) | Research/Literature | Critical | `PRE_GO_LIVE` | Evidence Lead | WP-066, WP-072, WP-103 |
| [ACC-03 — Duplicate and Metadata Collision](ACC-03_duplicate_collision.md) | Research/Literature | High | `PRE_GO_LIVE` | Source Resolver Lead | WP-062, WP-067, WP-094, WP-103 |
| [ACC-04 — Retraction Impact](ACC-04_retraction_impact.md) | Research/Monitoring | Critical | `PRE_GO_LIVE` | Knowledge Monitoring Lead | WP-063, WP-037, WP-108, WP-106 |
| [ACC-05 — Prompt-Injection PDF](ACC-05_prompt_injection_pdf.md) | Security/Literature | Critical | `PRE_GO_LIVE` | Content Security Lead | WP-058, WP-060, WP-103 |
| [ACC-06 — Planner Self-Approval Attempt](ACC-06_plan_self_approval.md) | Governance/Assurance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-007, WP-088, WP-102, WP-105 |
| [ACC-07 — Reviewer Order Bias](ACC-07_reviewer_order_bias.md) | Model/Eval | High | `PRE_GO_LIVE` | Eval Office | WP-043, WP-088 |
| [ACC-08 — Strong Counter-Test](ACC-08_strong_counter_test.md) | Research/Assurance | Critical | `PRE_GO_LIVE` | Falsification Lead | WP-077, WP-087, WP-088, WP-089, WP-105 |
| [ACC-09 — Budget Hard Stop](ACC-09_budget_hard_stop.md) | FinOps/Reliability | Critical | `PRE_GO_LIVE` | FinOps Lead | WP-053, WP-083, WP-100, WP-111 |
| [ACC-10 — Primary Model Provider Outage](ACC-10_provider_outage.md) | Reliability/Model | High | `PRE_GO_LIVE` | Model Platform Lead | WP-041, WP-045, WP-111 |
| [ACC-11 — No Eligible Fallback](ACC-11_no_eligible_fallback.md) | Reliability/Model | Critical | `PRE_GO_LIVE` | Model Platform Lead | WP-041, WP-045, WP-111 |
| [ACC-12 — Duplicate Event Delivery](ACC-12_duplicate_event.md) | Reliability/Event | Critical | `PRE_GO_LIVE` | Event Platform Lead | WP-028, WP-039, WP-111 |
| [ACC-13 — Temporal Worker Crash](ACC-13_temporal_worker_crash.md) | Reliability/Control | Critical | `PRE_GO_LIVE` | Control Plane Lead | WP-031, WP-040, WP-111 |
| [ACC-14 — Workflow Code Deployment and Replay](ACC-14_workflow_code_deploy.md) | Reliability/Control | Critical | `PRE_GO_LIVE` | Platform Assurance Lead | WP-032, WP-040, WP-111 |
| [ACC-15 — Sandbox Escape Attempt](ACC-15_sandbox_escape.md) | Security/Execution | Critical | `PRE_GO_LIVE` | Execution Security Lead | WP-054, WP-060, WP-112 |
| [ACC-16 — Egress Exfiltration Attempt](ACC-16_egress_exfiltration.md) | Security/Network | Critical | `PRE_GO_LIVE` | Network Security Lead | WP-057, WP-060, WP-112 |
| [ACC-17 — Unsigned or Mutable Image](ACC-17_unsigned_image.md) | Security/Supply Chain | Critical | `PRE_GO_LIVE` | Supply Chain Security Lead | WP-027, WP-059, WP-112 |
| [ACC-18 — D3 Data to a Public Provider](ACC-18_d3_public_route.md) | Security/Privacy | Critical | `PRE_GO_LIVE` | Safety & Governance Owner | WP-041, WP-056, WP-057, WP-112 |
| [ACC-19 — Clean-Room Reproduction Pass](ACC-19_clean_room_pass.md) | Evidence/Reproduction | High | `PRE_GO_LIVE` | Reproducibility Lead | WP-084, WP-085, WP-105, WP-113 |
| [ACC-20 — Clean-Room Reproduction Failure](ACC-20_clean_room_fail.md) | Evidence/Reproduction | Critical | `PRE_GO_LIVE` | Reproducibility Lead | WP-084, WP-085, WP-105, WP-113 |
| [ACC-21 — Derived Graph Corruption and Rebuild](ACC-21_graph_corruption.md) | Data/Knowledge | High | `PRE_GO_LIVE` | Knowledge Data Lead | WP-030, WP-074, WP-113, WP-114 |
| [ACC-22 — Obsidian Human Edit Preservation](ACC-22_obsidian_human_edit.md) | Knowledge | High | `PRE_GO_LIVE` | Knowledge Lead | WP-073, WP-074, WP-113 |
| [ACC-23 — Artifact Overwrite Attempt](ACC-23_artifact_overwrite.md) | Data/Integrity | Critical | `PRE_GO_LIVE` | Data Platform Lead | WP-026, WP-087, WP-104, WP-113 |
| [ACC-24 — Policy Bundle Rollback](ACC-24_policy_bundle_rollback.md) | Security/Governance | High | `PRE_GO_LIVE` | Policy Platform Lead | WP-056, WP-112 |
| [ACC-25 — Human Approval Forgery](ACC-25_human_approval_forgery.md) | Security/Governance | Critical | `PRE_GO_LIVE` | Governance Lead | WP-038, WP-055, WP-093, WP-112 |
| [ACC-26 — Approval, Delegation and Exception Expiry](ACC-26_approval_expiry.md) | Governance | Critical | `PRE_GO_LIVE` | Safety & Governance Owner | WP-004, WP-009, WP-038, WP-093, WP-112 |
| [ACC-27 — Regional / Management Plane DR](ACC-27_regional_dr.md) | Operations/DR | Critical | `PRE_GO_LIVE` | SRE Lead | WP-114 |
| [ACC-28 — Zotero Full Resync](ACC-28_zotero_full_resync.md) | Literature/DR | High | `PRE_GO_LIVE` | Knowledge Platform Lead | WP-067, WP-103, WP-114 |
| [ACC-29 — Provider Invoice Variance](ACC-29_invoice_variance.md) | FinOps | Medium | `PRE_GO_LIVE` | FinOps Lead | WP-100, WP-111 |
| [ACC-30 — Publication Completeness](ACC-30_publication_completeness.md) | Publication/Evidence | Critical | `PRE_GO_LIVE` | Provenance Curator | WP-080, WP-090, WP-106, WP-113 |
| [ACC-31 — Superseded Publication](ACC-31_superseded_publication.md) | Publication/Monitoring | High | `PRE_GO_LIVE` | Publication Owner | WP-090, WP-106, WP-108, WP-113 |
| [ACC-32 — Secret in Prompt or Trace](ACC-32_secret_in_trace.md) | Security/Observability | Critical | `PRE_GO_LIVE` | AI Observability Lead | WP-057, WP-097, WP-112 |
| [ACC-33 — Kueue Preemption](ACC-33_kueue_preemption.md) | Execution/Reliability | High | `PRE_GO_LIVE` | Compute Platform Lead | WP-053, WP-083, WP-111 |
| [ACC-34 — DLQ Repair and Corrected Replay](ACC-34_dlq_repair.md) | Event/Reliability | High | `PRE_GO_LIVE` | Event Platform Lead | WP-028, WP-039, WP-111 |
| [ACC-35 — Tool Partial Failure](ACC-35_tool_partial_failure.md) | Tool/Reliability | Critical | `PRE_GO_LIVE` | Tool Platform Lead | WP-049, WP-050, WP-111 |
| [ACC-36 — Model Snapshot Drift](ACC-36_model_snapshot_drift.md) | Model/Monitoring | Critical | `PRE_GO_LIVE` | Eval Office | WP-042, WP-044, WP-108 |
| [ACC-37 — Evaluation Set Contamination](ACC-37_eval_contamination.md) | Model/Eval/Security | Critical | `PRE_GO_LIVE` | Eval Office | WP-043, WP-060, WP-112 |
| [ACC-38 — Critical Reviewer Unavailable](ACC-38_reviewer_unavailable.md) | Assurance/Operations | High | `PRE_GO_LIVE` | Assurance Lead | WP-045, WP-088, WP-105, WP-113 |
| [ACC-39 — Negative Research Result](ACC-39_negative_result.md) | Research/Portfolio | Medium | `PRE_GO_LIVE` | Scientific Owner | WP-081, WP-082, WP-083, WP-104, WP-113 |
| [ACC-40 — Complete Project Audit Export](ACC-40_audit_export.md) | Audit/Operations | Critical | `PRE_GO_LIVE` | Internal Audit Lead | WP-099, WP-106, WP-109, WP-112, WP-114 |
| [ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling](ACC-41_notification_data_class_ceiling.md) | Communication/Security | Critical | `PRE_GO_LIVE` | Platform Security Lead | WP-131, WP-132, WP-133 |
| [ACC-42 — Notification Broker Unavailable During an Escalating Condition](ACC-42_notification_broker_outage.md) | Communication/Reliability | High | `PRE_GO_LIVE` | Platform Operations Lead | WP-131, WP-140 |
| [ACC-43 — Escalation Timeout and Dead-Man's Switch](ACC-43_escalation_and_dead_mans_switch.md) | Communication/Governance | Critical | `PRE_GO_LIVE` | Platform Operations Lead | WP-134, WP-140 |
| [ACC-44 — Inbound Content Attempts to Act as an Instruction](ACC-44_inbound_message_is_not_an_instruction.md) | Security/Communication | Critical | `PRE_GO_LIVE` | Content Security Lead | WP-136, WP-058 |
| [ACC-45 — Irreversible External Record Submission](ACC-45_external_record_submission.md) | External/Governance | Critical | `PRE_GO_LIVE` | Data Steward | WP-138, WP-139 |
| [ACC-46 — Task Runs With No Skill Loaded](ACC-46_skill_not_loaded.md) | Agent/Skill Governance | Critical | `PRE_GO_LIVE` | Assurance Lead | WP-013, WP-046, WP-047, WP-048 |
| [ACC-47 — Harness Starts Without the Skill Bootstrap](ACC-47_skill_bootstrap_missing.md) | Agent/Skill Governance | Critical | `PRE_GO_LIVE` | Model Platform Lead | WP-047, WP-048 |
| [ACC-48 — Wrong or Competing Skill Selected](ACC-48_wrong_skill_selected.md) | Agent/Skill Governance | High | `PRE_GO_LIVE` | Eval Office | WP-043, WP-047 |
| [ACC-49 — Non-Waivable Skill Ignored Under Pressure](ACC-49_skill_ignored_under_pressure.md) | Agent/Skill Governance | Critical | `PRE_GO_LIVE` | Red Team Lead | WP-043, WP-046, WP-088 |
| [ACC-50 — Procedure Lost to Context Compaction or Restart](ACC-50_skill_lost_on_compaction.md) | Agent/Skill Governance | High | `PRE_GO_LIVE` | Control Plane Lead | WP-046, WP-048 |
| [ACC-51 — Upstream Change Invalidates a Derived Skill](ACC-51_upstream_skill_drift.md) | Agent/Skill Governance | High | `PRE_GO_LIVE` | Knowledge Steward | WP-013, WP-047 |

---

## 3. Counts

| Measure | Value |
|---|---:|
| Scenarios | **51** |
| Critical | 33 |
| High | 16 |
| Medium | 2 |
| `PRE_GO_LIVE` | 51 |
| `DAY2_CONTINUOUS` | 0 |

> **No scenario currently carries `DAY2_CONTINUOUS`.** The recurring rhythms are
> owned by the Day-2 packages WP-122 – WP-130 rather than by acceptance
> scenarios; the phase exists so that a Day-2 scenario, if one is written, cannot
> silently become a go-live precondition again.

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
