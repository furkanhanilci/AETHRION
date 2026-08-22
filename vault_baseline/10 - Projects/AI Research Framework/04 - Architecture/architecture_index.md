# Architecture Index

The target architecture, the repository map and the operational skill layer.

## Documents

| Document | The question it answers |
|---|---|
| [[10 - Projects/AI Research Framework/04 - Architecture/framework_repository_and_obsidian_map\|Repository and Obsidian Map]] | What is kept where? |
| [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure\|AIRL-OS Ideal Structure]] | **What** should be added? |
| [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer\|AIRL-OS Skill Layer]] | **How** should it be executed? |
| [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_role_model_assignment\|Role → Model Assignment]] | **Who** executes it — human / model / code? |

## The six planes, plus the proposal

| Plane | Owner | Status |
|---|---|---|
| Experience | Obsidian + Cockpit | V0 in place |
| Control | Temporal | planned |
| Event | NATS JetStream | planned |
| Cognition | LangGraph + RoleContract | planned |
| Execution | Kubernetes + Broker + Sandbox | planned |
| Evidence & Ops | Registries + WORM | V0 partial (SQLite) |
| **Metascience & Calibration** | **proposed** | **awaiting decision** |

## The canonical-copy boundary

The canonical copies of these notes live under `docs/architecture/`. The notes
here are a generated Obsidian mirror, identical in content. **If content changes,
the canonical file changes first** and the mirror is regenerated with
`scripts/mirror_vault.py`.
