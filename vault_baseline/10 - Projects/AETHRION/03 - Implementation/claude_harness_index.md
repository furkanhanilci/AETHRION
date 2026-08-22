---
title: "Harness configuration"
cssclasses:
  - aethrion-index
type: index
category: implementation
status: WORKING
summary: "A skill that does not load governs nothing, so the registry has to be reachable by the harness actually in use."
source: ".claude/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/execution
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `.claude/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Harness configuration

| Field | Value |
|---|---|
| Document type | Component note |
| Scope | How the skill registry reaches an agent in this repository |
| Sibling documents | `../skills/README.md` |
| Status | `WORKING` for Claude Code; **unverified everywhere else** |
| Date | 2026-08-22 |

**In one paragraph.** A skill that does not load governs nothing, so the registry
has to be reachable by the harness actually in use. `skills` here is a symlink to
`../skills`, which is what makes the 52-skill registry visible to Claude Code.
Every other harness is *format-compatible* and **unverified** — the Agent Skills
format is implemented by Codex, OpenCode, Cursor, Copilot, Gemini CLI and Hermes
Agent, but nothing in this repository has confirmed that any of them loads these
files, and ACC-47 is the scenario that would.

| Entry | Is |
|---|---|
| `skills` → `../skills` | The registry, made discoverable to Claude Code |
| `settings.local.json` | Local permission allowlist — **git-ignored**, machine-specific |

> **Format conformance is not verified loading, and verified loading is not
> verified behaviour.** All three are separate claims, and this repository can
> currently support only the first.
