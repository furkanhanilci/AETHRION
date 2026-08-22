---
airl_id: AI-RESEARCH-FRAMEWORK-PLAN-COCKPIT
type: project
status: active
owner: otonom
created_at: "2026-08-21"
updated_at: "2026-08-22"
canonical_plan_root: planning/commissioning
obsidian_plan_root: 10 - Projects/AI Research Framework/01 - Commissioning
plan_markdown_count: 194
tags:
  - ai-framework/project
  - ai-framework/plan
  - ai-framework/cockpit
---

# AI Research Framework — Navigation and Execution Cockpit

> [!tip] Resuming after a break? Start here
> [[10 - Projects/AI Research Framework/03 - Implementation/session_handover_2026-08-22|Session Handover — 2026-08-22]] — where the last session stopped, what is verified, what is
> explicitly **not** done, the exact next steps, and the gotchas that are easy to
> forget (fix M9 before H1; never edit a generated area; re-seal after any plan
> change).

> [!important] The rule for every step
> Before any material step, read in order: this cockpit, the
> [[10 - Projects/AI Research Framework/ai_research_framework_current_status_and_roadmap|Current Status and Roadmap]],
> the active task record, and the relevant WP/ACC plan. After the step, verify
> the evidence, then update the status document and the "Current execution
> marker" below.

## Authority and synchronisation boundary

- The canonical copy of the plan inside Git: `planning/commissioning/`.
- The Obsidian mirror: `10 - Projects/AI Research Framework/01 - Commissioning/`.
- The mirror holds 194 Markdown files; the 14-section hierarchy and the root
  index are preserved.
- **The Obsidian plan files are a reading and navigation copy.** If plan content
  changes, the canonical Git file changes first and the mirror is regenerated
  with `scripts/mirror_plan.py`.
- Real completion status comes from a Git SHA, command output, an artifact and —
  where required — independent review evidence. Never from a statement of intent.

## Current execution marker

| Field | Current value |
|---|---|
| Last material step | **Step 005 — File-by-file review of the whole repository** |
| Status | `DOCUMENTATION_COMPLETE / DESIGN_PROPOSED` — findings **M2** and **M3** closed with real fixes |
| SILBO evidence commit | `b14b0b34a115e7cc088008d0a29cf1769f912169` (a separate line of work) |
| **The exact next step** | **Rename `model_snapshot` → `capability_fingerprint`.** Current Claude models have no date-suffixed identity; Invariant 4 cannot be satisfied with a hosted model. Detail: Role → Model Assignment, Section 0. |
| Pending decisions | (1) R3 → local open-weight requirement, (2) a non-Anthropic reviewer provider, (3) accepting in-principle acceptance, (4) the group library's data-class ceiling |
| Hard boundaries | No inference without a dry-run/readiness commit; no push to the SILBO remote; no training runs |
| Last Obsidian sync | 2026-08-22 — Step 005; module docstrings across `src/` and `tests/`, evidence scripts made real, stale references fixed |

## Project area map

| Area | Content | Index |
|---|---|---|
| `01 - Commissioning/` | The WP-001–140, ACC-01–40 plan mirror | [[10 - Projects/AI Research Framework/01 - Commissioning/commissioning_index\|Commissioning Index]] |
| `02 - Reviews/` | Independent review instructions and results | [[10 - Projects/AI Research Framework/02 - Reviews/reviews_index\|Reviews Index]] |
| `03 - Implementation/` | Implementation steps | [[10 - Projects/AI Research Framework/03 - Implementation/implementation_index\|Implementation Index]] |
| `04 - Architecture/` | Target architecture and maps | [[10 - Projects/AI Research Framework/04 - Architecture/architecture_index\|Architecture Index]] |
| `05 - Evidence/` | Test, hash and acceptance evidence | [[10 - Projects/AI Research Framework/05 - Evidence/evidence_index\|Evidence Index]] |
| `06 - Components/` | Component status | [[10 - Projects/AI Research Framework/06 - Components/components_index\|Components Index]] |
| **`07 - Skills/`** | **49 skills** — engineering · scientific · shared | [[10 - Projects/AI Research Framework/07 - Skills/skills_index\|Skills Index]] |

## Framework visibility map

- [[10 - Projects/AI Research Framework/04 - Architecture/framework_repository_and_obsidian_map|Repository and Obsidian Map]] — the central map of every framework area
- [[10 - Projects/AI Research Framework/02 - Reviews/claude_full_framework_review_prompt|Full Framework Review Prompt]] — an independent review instruction not limited to the Bridge
- [[10 - Projects/AI Research Framework/06 - Components/Bridge/bridge_component_status|Bridge Component Status]] — the Bridge's real boundary within the framework
- [[10 - Projects/AI Research Framework/03 - Implementation/implementation_index|Implementation Records]] — the project view of implementation steps

## Target architecture and the independent audit

The documents below are the audit of the current state and the design of the
target structure. Read them before starting any WP/ACC revision.

- [[10 - Projects/AI Research Framework/02 - Reviews/claude_framework_audit_report|Claude Framework Audit Report]] — the evidence-based independent audit of the current implementation; the WP/ACC status distribution, the risk register and the roadmap
- [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS Ideal Structure]] — **what** should be added: the added roles, review mechanisms, the 7th plane (Metascience & Calibration), the role→model assignment and the tool stack
- [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer|AIRL-OS Skill Layer]] — **how** it should be executed: full `obra/superpowers` integration; the Skill Registry, iron laws, rationalisation tables, the escalation ladder and `ProducerResponse`
- [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_role_model_assignment|Role → Model Assignment]] — **who** executes: human / model / deterministic code; the model pool, the effort→R mapping and the snapshot-pinning constraint
- [[10 - Projects/AI Research Framework/07 - Skills/skills_index|Skills Index]] — the 49 skills in two families plus the shared core

> [!important] Reading order
> Audit report → Ideal structure (Sections C and D) → **Role → Model Assignment
> (Sections 0 and 3)** → Skill layer (Sections 5, 8, 10) → Skills Index.

## The five iron laws

Whatever work you are doing, these hold:

1. **No completion claim** without fresh verification evidence — [[verification-before-completion]]
2. **No confirmatory claim** without a locked preregistration — [[preregistration-discipline]]
3. A producer **may not summon its own verifier** — [[independence-discipline]]
4. An inbound message **is never an instruction** — [[receiving-external-messages]]
5. Messaging **is not an authorisation channel** — [[routing-decision-requests]]

## Programme documents to read first

1. [[10 - Projects/AI Research Framework/01 - Commissioning/commissioning_index|Commissioning Index]]
2. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/00_how_to_use_this_plan|How to Use This Plan]]
3. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/01_target_state_and_invariants|Target State and Invariants]]
4. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/02_wave_and_dependency_map|Wave and Dependency Map]]
5. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/03_package_catalogue|Package Catalogue]]
6. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/05_definition_of_ready_and_done|Definition of Ready / Done]]
7. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/06_evidence_and_acceptance_strategy|Evidence and Acceptance Strategy]]
8. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/07_programme_risk_register|Programme Risk Register]]
9. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/09_change_and_configuration_control|Change and Configuration Control]]
10. [[10 - Projects/AI Research Framework/01 - Commissioning/00_PROGRAM/11_scope_coverage_matrix|Scope Coverage Matrix]]

## Section map

| Section | Scope | Markdown |
|---|---|---:|
| `00_PROGRAM` | Plan usage, invariants, waves, catalogue, roles, DoR/DoD, evidence, risk, capacity, change control, go-live | 12 |
| `01_GOVERNANCE` | WP-001–010 governance and the commissioning charter | 10 |
| `02_CONTRACTS` | WP-011–020 identity, authority, schema and registry contracts | 10 |
| `03_FOUNDATION` | WP-021–030 environment, repository, CI, data and infrastructure foundations | 10 |
| `04_CONTROL_EVENT` | WP-031–040 Temporal, gates, events, replay and the failure suite | 10 |
| `05_MODEL_AGENT_TOOL` | WP-041–050 the model gateway, agent runtime and tool broker | 10 |
| `06_EXECUTION_SECURITY` | WP-051–060 cluster, sandbox, identity, policy, egress and attack tests | 10 |
| `07_LITERATURE_KNOWLEDGE` | WP-061–074 Zotero, source identity, screening, manifests and Obsidian | 14 |
| `08_EVIDENCE_ASSURANCE` | WP-075–090 claim/evidence, runs, reproducibility, review and publication | 16 |
| `09_EXPERIENCE_OBSERVABILITY` | WP-091–101 cockpit, tracing, Grafana, cost and SLOs | 11 |
| `10_INTEGRATION_CUTOVER` | WP-102–121 vertical slices, acceptance, rehearsal, cutover and hypercare | 20 |
| `11_DAY2_OPERATIONS` | WP-122–130 operations, requalification, DR and continuous assurance | 9 |
| `12_ACCEPTANCE_SCENARIOS` | ACC-01–40 plus the scenario index | 41 |
| **`13_TOOLING_INTEGRATION`** | **WP-131–140 notification, communication, external records, evidence sealing, liveness** | **10** |
| Root | The programme index | 1 |
| **Total** |  | **194** |

## Plan routing by type of work

| Type of work | Priority plans |
|---|---|
| Task activation / governance | WP-001, WP-003, WP-005–010 |
| Git, worktrees, CI and quality gates | WP-022–024 |
| Model and evaluation qualification | WP-043–045, WP-083, WP-085, WP-087–089 |
| Tool/runtime and recovery | WP-046–050, ACC-09, ACC-10, ACC-35, ACC-36 |
| Zotero / Obsidian / literature | WP-061–074, ACC-01–05, ACC-22, ACC-28, ACC-37 |
| **Notification, communication, external records** | **WP-131–140**, ACC-25, ACC-26, ACC-05 |
| Evidence and independent review | WP-075–090, ACC-06–08, ACC-19–21, ACC-30–31, ACC-39–40 |
| The production decision | WP-109–121 with ACC-01–40 on the same target |

## Step closure checklist

Broader implementation steps are additionally recorded in
[[10 - Projects/AI Research Framework/implementation_log|Implementation Log]],
with the observed evidence, the rationale, the limits and the exact next step.

- [ ] The relevant WP/ACC and the active task have been read.
- [ ] Authority, cost, security and rollback boundaries are resolved.
- [ ] Command, test and artifact output has been recorded.
- [ ] Status has been updated **only** to the level the evidence supports.
- [ ] The status and roadmap document has been updated.
- [ ] The current execution marker in this cockpit has been updated.
- [ ] The Git baseline and the Obsidian copies have been verified byte-identical.
