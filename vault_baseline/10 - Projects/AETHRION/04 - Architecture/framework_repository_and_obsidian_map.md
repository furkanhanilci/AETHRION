---
title: "AETHRION — Repository and Obsidian Map"
airl_id: AETHRION-REPO-VAULT-MAP
type: reference
category: vault
status: active
summary: "Which surface owns what: the repository holds canonical work, the vault holds human thinking, and the generated areas are projections of the first into the second."
generated: false
tags:
  - aethrion/architecture
  - aethrion/project
cssclasses:
  - aethrion-reference
---

# AETHRION — Repository and Obsidian Map

Shows where every part of the framework is kept.
**The repository root and the framework root are the same**; the Bridge is one
component inside the framework, not the framework itself.

## Canonical roots

| Area | Location | Role |
|---|---|---|
| Framework repository | `/home/otonom/Desktop/FH/AETHRION/` | The Git repository root — code, plan, skills, documents, evidence |
| Remote | `github.com/furkanhanilci/AETHRION` | private, `main` |
| Obsidian vault | `/home/otonom/Documents/Obsidian Vault/` | The user-facing project knowledge space |
| SILBO model worktree | `/home/otonom/silbo-fix-005/` | A separate model/evaluation area; never mixed with the framework |

## Repository structure

```text
AI_RESEARCH_FRAMEWORK/            ← the Git repository root
├── src/
│   ├── airl_bridge/              The Bridge component (Zotero → SQLite → Obsidian → MCP)
│   └── airl_framework/           The shared contract core
├── tests/                        The test suite
├── skills/                       38 execution skills (the Skill Registry)
├── planning/
│   └── commissioning/            WP-001–140, ACC-01–40 — CANONICAL, hash-sealed
├── docs/
│   ├── architecture/             Target architecture and skill layer design
│   ├── review/                   Independent review instructions and reports
│   ├── ARCHITECTURE_V0.md        The architecture of the working vertical slice
│   └── OPERATIONS.md             The operations guide
├── schemas/                      Shared contract schemas
├── delivery/                     Per-package evidence packages
├── deploy/                       systemd unit files
├── scripts/                      Acceptance, smoke and mirror-generation scripts
├── vault_baseline/               A versioned copy of the Obsidian vault
├── data/                         SQLite and projection backups (not in Git)
└── .venv/                        The virtual environment (not in Git)
```

## Plan integrity

`planning/commissioning/00_PROGRAM/SHA256SUMS.txt` seals the plan tree. Verify
from the repository root:

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

> The plan is kept in **one canonical copy**. The `01 - Commissioning/` tree in
> Obsidian is a reading and navigation mirror; **if content changes, the canonical
> file changes first**, then the mirror is regenerated.

## The Obsidian project tree

```text
10 - Projects/AETHRION/
├── 00_navigation_and_execution_cockpit.md   execution state and the next step
├── 01 - Commissioning/                      the plan mirror (generated)
├── 02 - Reviews/                            independent review instructions and results
├── 03 - Implementation/                     implementation steps
├── 04 - Architecture/                       architecture and maps (generated)
├── 05 - Evidence/                           test, hash and acceptance evidence
├── 06 - Components/                         component status
├── 07 - Skills/                             52 skills in seven groups (generated)
├── implementation_log.md                    the step-by-step log
└── aethrion_current_status_and_roadmap.md
```

## Generated versus human-authored

Three areas of the Obsidian project tree are **generated** and must never be
edited in place:

| Area | Generated from | Generator |
|---|---|---|
| `01 - Commissioning/` | `planning/commissioning/` | `scripts/mirror_plan.py` |
| `02 - Reviews/`, `04 - Architecture/` | `docs/` | `scripts/mirror_vault.py` |
| `07 - Skills/` | `skills/` | `scripts/mirror_vault.py` |
| `70 - Literature Sets/Zotero Sources/` | the canonical source registry | the Bridge API |

Everything else in the vault is human-authored and is never overwritten by a
generator.

Both scripts accept `--check`: they write nothing and exit non-zero if the mirror
has drifted from what would be generated. That is the drift check intended for
CI.

```bash
python scripts/mirror_plan.py  "$VAULT/10 - Projects/AETHRION/01 - Commissioning" --check
python scripts/mirror_vault.py "$VAULT/10 - Projects/AETHRION" --check
```

## Vault root structure

| Area | Content | Who writes |
|---|---|---|
| `00 - Home` | The entry page | human |
| `01 - Inbox` | Unclassified temporary notes | human |
| `10 - Projects` | Project trees | human + generators (see above) |
| `20 - Source Notes` | Human synthesis | **human only** |
| `30 - Concepts` · `40 - Claims` · `50 - Decisions` · `60 - Runs` | Knowledge areas | human |
| `70 - Literature Sets` root | Curated sets | human |
| `70 - Literature Sets/Zotero Sources` | **An automatic projection** | **the Bridge — never edited by hand** |
| `80 - Daily` | The daily working note | human |
| `90 - Archive` | Closed or superseded material | human |
| `_Templates` | Note templates | human |

## Naming conventions

- **Folder and file names are English.** No product-code prefixes.
- Obsidian notes use `lowercase_snake_case.md`.
- Each folder index is `<area>_index.md` (`reviews_index`, `skills_index`, …).
  Reason: repeated names such as `README` make Obsidian shortlinks ambiguous.
- Skill files use `lowercase-hyphen`, matching the skill name exactly.
- Plan mirror files map `WP-001_x.md` → `wp_001_x.md` and `ACC-01_x.md` →
  `acc_01_x.md`; the generator reproduces this rule and rewrites intra-plan links
  to match.

## The boundary rule

Code and technical deliverables stay in the repository; user-facing project
status, decisions, review instructions, evidence and the roadmap stay visible in
the Obsidian project tree. The copy relationship between the two is verified by
hash and by the `--check` mode of the generators.
