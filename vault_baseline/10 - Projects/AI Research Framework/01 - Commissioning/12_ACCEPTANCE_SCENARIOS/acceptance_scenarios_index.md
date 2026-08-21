# ACC-01–ACC-40 Sistem Kabul Senaryoları

Bu dizin production commissioning için kırk bağlayıcı senaryoyu içerir. Her senaryo aynı release candidate üzerinde, bağımsız witness ile ve imzalı evidence manifesti üreterek çalıştırılır.

| Senaryo | Kategori | Severity | Owner | İlgili paketler |
|---|---|---|---|---|
| [ACC-01 — Human Seed Literature](acc_01_human_seed_literature.md) | Research/Literature | Critical | Knowledge Lead | WP-065, WP-062, WP-069, WP-072, WP-103 |
| [ACC-02 — Agent-Used Source Write-Back](acc_02_agent_used_source_writeback.md) | Research/Literature | Critical | Evidence Lead | WP-066, WP-072, WP-103 |
| [ACC-03 — Duplicate ve Metadata Collision](acc_03_duplicate_collision.md) | Research/Literature | High | Source Resolver Lead | WP-062, WP-067, WP-094, WP-103 |
| [ACC-04 — Retraction Impact](acc_04_retraction_impact.md) | Research/Monitoring | Critical | Knowledge Monitoring Lead | WP-063, WP-037, WP-108, WP-106 |
| [ACC-05 — Prompt-Injection PDF](acc_05_prompt_injection_pdf.md) | Security/Literature | Critical | Content Security Lead | WP-058, WP-060, WP-103 |
| [ACC-06 — Planner Self-Approval Attempt](acc_06_plan_self_approval.md) | Governance/Assurance | Critical | Assurance Lead | WP-007, WP-088, WP-102, WP-105 |
| [ACC-07 — Reviewer Order Bias](acc_07_reviewer_order_bias.md) | Model/Eval | High | Eval Office | WP-043, WP-088, WP-126 |
| [ACC-08 — Strong Counter-Test](acc_08_strong_counter_test.md) | Research/Assurance | Critical | Falsification Lead | WP-077, WP-087, WP-088, WP-089, WP-105 |
| [ACC-09 — Budget Hard Stop](acc_09_budget_hard_stop.md) | FinOps/Reliability | Critical | FinOps Lead | WP-053, WP-083, WP-100, WP-111 |
| [ACC-10 — Primary Model Provider Outage](acc_10_provider_outage.md) | Reliability/Model | High | Model Platform Lead | WP-041, WP-045, WP-111 |
| [ACC-11 — No Eligible Fallback](acc_11_no_eligible_fallback.md) | Reliability/Model | Critical | Model Platform Lead | WP-041, WP-045, WP-111 |
| [ACC-12 — Duplicate Event Delivery](acc_12_duplicate_event.md) | Reliability/Event | Critical | Event Platform Lead | WP-028, WP-039, WP-111 |
| [ACC-13 — Temporal Worker Crash](acc_13_temporal_worker_crash.md) | Reliability/Control | Critical | Control Plane Lead | WP-031, WP-040, WP-111 |
| [ACC-14 — Workflow Code Deploy ve Replay](acc_14_workflow_code_deploy.md) | Reliability/Control | Critical | Platform Assurance Lead | WP-032, WP-040, WP-111 |
| [ACC-15 — Sandbox Escape Attempt](acc_15_sandbox_escape.md) | Security/Execution | Critical | Execution Security Lead | WP-054, WP-060, WP-112 |
| [ACC-16 — Egress Exfiltration Attempt](acc_16_egress_exfiltration.md) | Security/Network | Critical | Network Security Lead | WP-057, WP-060, WP-112 |
| [ACC-17 — Unsigned veya Mutable Image](acc_17_unsigned_image.md) | Security/Supply Chain | Critical | Supply Chain Security Lead | WP-027, WP-059, WP-112 |
| [ACC-18 — D3 Data to Public Provider](acc_18_d3_public_route.md) | Security/Privacy | Critical | Safety & Governance Owner | WP-041, WP-056, WP-057, WP-112 |
| [ACC-19 — Clean-Room Reproduction Pass](acc_19_clean_room_pass.md) | Evidence/Reproduction | High | Reproducibility Lead | WP-084, WP-085, WP-105, WP-113 |
| [ACC-20 — Clean-Room Reproduction Fail](acc_20_clean_room_fail.md) | Evidence/Reproduction | Critical | Reproducibility Lead | WP-084, WP-085, WP-105, WP-113 |
| [ACC-21 — Derived Graph Corruption ve Rebuild](acc_21_graph_corruption.md) | Data/Knowledge | High | Knowledge Data Lead | WP-030, WP-074, WP-113, WP-114 |
| [ACC-22 — Obsidian Human Edit Preservation](acc_22_obsidian_human_edit.md) | Knowledge | High | Knowledge Lead | WP-073, WP-074, WP-113 |
| [ACC-23 — Artifact Overwrite Attempt](acc_23_artifact_overwrite.md) | Data/Integrity | Critical | Data Platform Lead | WP-026, WP-087, WP-104, WP-113 |
| [ACC-24 — Policy Bundle Rollback](acc_24_policy_bundle_rollback.md) | Security/Governance | High | Policy Platform Lead | WP-056, WP-112 |
| [ACC-25 — Human Approval Forgery](acc_25_human_approval_forgery.md) | Security/Governance | Critical | Governance Lead | WP-038, WP-055, WP-093, WP-112 |
| [ACC-26 — Approval, Delegation ve Exception Expiry](acc_26_approval_expiry.md) | Governance | Critical | Safety & Governance Owner | WP-004, WP-009, WP-038, WP-093, WP-112 |
| [ACC-27 — Regional/Management Plane DR](acc_27_regional_dr.md) | Operations/DR | Critical | SRE Lead | WP-114, WP-129 |
| [ACC-28 — Zotero Full Resync](acc_28_zotero_full_resync.md) | Literature/DR | High | Knowledge Platform Lead | WP-067, WP-103, WP-114 |
| [ACC-29 — Provider Invoice Variance](acc_29_invoice_variance.md) | FinOps | Medium | FinOps Lead | WP-100, WP-111, WP-127 |
| [ACC-30 — Publication Completeness](acc_30_publication_completeness.md) | Publication/Evidence | Critical | Provenance Curator | WP-080, WP-090, WP-106, WP-113 |
| [ACC-31 — Superseded Publication](acc_31_superseded_publication.md) | Publication/Monitoring | High | Publication Owner | WP-090, WP-106, WP-108, WP-113 |
| [ACC-32 — Secret in Prompt/Trace](acc_32_secret_in_trace.md) | Security/Observability | Critical | AI Observability Lead | WP-057, WP-097, WP-112 |
| [ACC-33 — Kueue Preemption](acc_33_kueue_preemption.md) | Execution/Reliability | High | Compute Platform Lead | WP-053, WP-083, WP-111 |
| [ACC-34 — DLQ Repair ve Corrected Replay](acc_34_dlq_repair.md) | Event/Reliability | High | Event Platform Lead | WP-028, WP-039, WP-111 |
| [ACC-35 — Tool Partial Failure](acc_35_tool_partial_failure.md) | Tool/Reliability | Critical | Tool Platform Lead | WP-049, WP-050, WP-111 |
| [ACC-36 — Model Snapshot Drift](acc_36_model_snapshot_drift.md) | Model/Monitoring | Critical | Eval Office | WP-042, WP-044, WP-108, WP-124 |
| [ACC-37 — Evaluation Set Contamination](acc_37_eval_contamination.md) | Model/Eval/Security | Critical | Eval Office | WP-043, WP-060, WP-112, WP-124 |
| [ACC-38 — Critical Reviewer Unavailable](acc_38_reviewer_unavailable.md) | Assurance/Operations | High | Assurance Lead | WP-045, WP-088, WP-105, WP-113, WP-126 |
| [ACC-39 — Negative Research Result](acc_39_negative_result.md) | Research/Portfolio | Medium | Scientific Owner | WP-081, WP-082, WP-083, WP-104, WP-113 |
| [ACC-40 — Complete Project Audit Export](acc_40_audit_export.md) | Audit/Operations | Critical | Internal Audit Lead | WP-099, WP-106, WP-109, WP-112, WP-114 |

## Commissioning kuralı

- Critical senaryo SKIP/waiver ile PASS sayılamaz.
- Kırk senaryonun tamamı aynı RC digest ve bundle baseline'ında çalışır.
- Yeni RC oluşursa en az etkilenen senaryolar ve platform baseline regression yeniden koşulur.
- Nihai go-live şartı: `40/40 PASS`, sıfır açık Critical finding ve doğrulanmış Commissioning Dossier.
