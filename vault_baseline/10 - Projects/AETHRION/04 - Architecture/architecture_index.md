---
title: "Architecture Index"
airl_id: AETHRION-ARCHITECTURE-INDEX
type: index
category: vault
status: active
summary: "The target design, its decision records, and the distance between them and what runs."
generated: false
tags:
  - aethrion/index
  - aethrion/architecture
---

# Architecture Index

The target architecture, the repository map and the operational skill layer.

## Documents

| Document | The question it answers |
|---|---|
| [[10 - Projects/AETHRION/04 - Architecture/framework_repository_and_obsidian_map\|Repository and Obsidian Map]] | What is kept where? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_ideal_structure\|AETHRION Ideal Structure]] | **What** should be added? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_skill_layer\|AETHRION Skill Layer]] | **How** should it be executed? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_role_model_assignment\|Role → Model Assignment]] | **Who** executes it — human / model / code? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_architecture\|AETHRION Architecture]] | **What is this system?** — the diagrammed entry point |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_roles\|Role Definitions]] | What may each role never do, and which roles may combine? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_external_standards\|External Standards]] | What is adopted rather than invented? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_component_reuse\|Component Reuse]] | Which mature implementation does each control stand on? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_foundation\|Foundation]] | What does the whole system rest on, before any component is chosen? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_branding_assets\|Branding Assets]] | Which mark is canonical, and where may it be used? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_related_systems\|Related Systems]] | How does this compare to Science One, PaperQA2, AI Scientist? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_document_standard\|Document Standard]] | How is every document here written? |
| [[10 - Projects/AETHRION/04 - Architecture/aethrion_figure_specification\|Figure Specification]] | How are the figures produced and checked? |

## Decision records

| ADR | Decision | Status |
|---|---|---|
| [[10 - Projects/AETHRION/04 - Architecture/adr_001_solo_operator_independence\|ADR-001]] | Solo-operator independence — R1 solo · R2 declared-partial · **R3 blocked** | **ACCEPTED** |
| [[10 - Projects/AETHRION/04 - Architecture/adr_002_bootstrap_verification_control\|ADR-002]] | BVC-01 bootstrap verification control | **ACCEPTED** — written, **not active** |
| [[10 - Projects/AETHRION/04 - Architecture/adr_003_trusted_control_and_policy\|ADR-003]] | Trusted control / untrusted data · Cedar · anomaly ⇒ deny | **ACCEPTED** — not built |

## Figures

Generated, never hand-edited — `docs/figures/`:
lifecycle · roles · evidence chain · target stack · reporting pipeline.

## The six planes, plus the proposal

| Plane | Owner | Status |
|---|---|---|
| Experience | Obsidian + Cockpit | V0 in place |
| Control | Temporal | planned |
| Event | NATS JetStream | planned |
| Cognition | LangGraph + RoleContract | planned |
| Execution | Kubernetes + Broker + Sandbox | planned |
| Evidence & Operations | registries, ledgers, object store | planned |
| **Metascience** (7th, proposed) | calibration, control injection, claim survival | proposal |
| Evidence & Ops | Registries + WORM | V0 partial (SQLite) |
| **Metascience & Calibration** | **proposed** | **awaiting decision** |

## The canonical-copy boundary

The canonical copies of these notes live under `docs/architecture/`. The notes
here are a generated Obsidian mirror, identical in content. **If content changes,
the canonical file changes first** and the mirror is regenerated with
`scripts/mirror_vault.py`.
