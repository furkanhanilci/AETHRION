---
title: "Framework Audit Evidence — 2026-08-22"
airl_id: AETHRION-AUDIT-EVIDENCE-2026-08-22
type: evidence
category: vault
status: active
summary: "The evidence captured alongside the 2026-08-21 framework audit. Frozen."
generated: false
tags:
  - aethrion/evidence
  - aethrion/review
cssclasses:
  - aethrion-evidence
---

# Framework Audit Evidence — 2026-08-22

Evidence collected during the independent audit **by fresh execution**. Every row
is bound to a reproducible command.

Related report:
[[10 - Projects/AETHRION/02 - Reviews/claude_framework_audit_report|Claude Framework Audit Report]]

## E1 — Mechanical verification

| Command | Exit | Result |
|---|---:|---|
| `uv run pytest -q` | 0 | **20 passed**, 1 warning (pydantic forward-ref) |
| `sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt` | 0 | **all OK**, 0 FAILED |
| `diff -rq vault_baseline "$VAULT"` | — | no content difference (only `.obsidian/` config) |

## E5 — Operations

| Check | Result |
|---|---|
| `systemctl --user is-active airl-bridge.service` | `active` |
| `systemctl --user is-active airl-bridge-sync.timer` | `active` |
| `GET /health` | `{"status":"ok","version":"0.1.0","zotero_write_enabled":false}` |
| `GET /ready` | `{"status":"ready","zotero":"reachable","source_count":33}` |
| SQLite | 33 sources · 25 sync runs · last 8 runs `SUCCEEDED` |
| Source distribution | journalArticle 25 · report 6 · conferencePaper 2 |

> **Caveat on `zotero_write_enabled`:** this field is a hard-coded constant, not a
> measured control. It is **not** evidence that writing is disabled. See finding
> **H3**.

## Git state

| Field | Value |
|---|---|
| HEAD (at audit time) | `6c849bd` |
| origin/main | `6c849bd` — 0 ahead / 0 behind |
| Working tree | clean (at audit time) |
| Tracked files | 434 |
| Remote | `github.com/furkanhanilci/AETHRION` (private) |

## Plan integrity analysis (by script)

| Measure | Result |
|---|---|
| WP file ↔ CSV match | 130/130, none missing, none extra |
| Dependency graph | **no cycles**, forward dependencies **0** |
| Markdown links inside the plan | 1011 links, **0 broken** (in all three copies) |
| WP template ratio (repeated verbatim in ≥120/130 files) | **59.2%** |
| ACC template ratio (≥36/40) | **48.8%** |
| Unique lines per WP | ~25 |
| WP ↔ ACC cross-reference | CSV and the ACC documents **differ in 39/40 cases** |
| WPs with no ACC reference | **62/130** |
| WPs whose ACC field is a placeholder | **39/130** |
| Distinct `owner` roles | **73** |
| Distinct `verifier` roles | **114** |
| Effort distribution | L: 83 · M: 42 · S: 5 |

## Obsidian integrity

| Measure | Before the audit | After |
|---|---|---|
| Note count | 246 | 246 + 38 skills + 8 index notes |
| Wikilinks | 103, 0 broken | re-verified |
| Template path config | ❌ pointed at a non-existent folder | ✅ `_Templates` |
| Daily-note folder | ❌ absent, cluttering the root | ✅ `80 - Daily` |
| Dataview | ❌ not installed → queries dead | ✅ converted to core-search syntax |
| Duplicate note names | `README` ×2, `readme` ×2 | ✅ 0 |

## Areas that could not be verified

| Area | Reason |
|---|---|
| The SILBO FIX-004/005a/005 acceptance chain | A separate repository, out of scope |
| The Hermes `tools.include` five-tool restriction | The configuration lives outside the repository |
| GitHub branch protection rules | Read-only boundary |
| Running `acceptance_v0.py` | It writes to the live service and depends on personal data |
| The true total record count in Zotero | Zotero was not queried directly |
