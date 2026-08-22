---
title: "Scripts"
type: index
category: implementation
status: WORKING
summary: "These scripts are where this repository's central claim — machines verify — is either true or empty."
source: "scripts/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/execution
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `scripts/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Scripts

| Field | Value |
|---|---|
| Document type | Index — every script, what it verifies, and what it cannot |
| Scope | The verification bundle, the generators, and the working tooling |
| Sibling documents | `../docs/OPERATIONS.md` · `../deploy/bvc-01-verify.yml` |
| Status | `WORKING` — every script here runs; several are in the verification bundle |
| Date | 2026-08-22 |

**In one paragraph.** These scripts are where this repository's central claim —
*machines verify* — is either true or empty. Each one states what it proves and,
just as importantly, what it does not: a citation checker proves that a reference
resolves, never that it supports the sentence citing it. Anything that generates
a file is authoritative over that file, and editing its output by hand is a
defect rather than a shortcut.

---

## 1. Verification — the bundle

| Script | Proves | Cannot see |
|---|---|---|
| `validate_skills.py` | 52 skills conform to the Agent Skills format and the AIRL metadata contract, with upstream provenance pinned | whether a skill changes agent behaviour |
| `validate_commissioning_plan.py` | identifiers exist · **WP↔ACC references resolve both ways** · the dependency graph is acyclic · acceptance phases are valid · **go-live is feasible** · no stale ranges · catalogue parity | whether the plan is a *good* plan |
| `check_doc_consistency.py` | every count a document states matches the repository; no decision record contradicts its own status | anything outside the declared numbers |
| `check_stale_claims.py` | no document claims a state the repository has outgrown — while **exempting genuine history** | prose that is merely wrong rather than stale |
| `check_figures.py` | no text escapes the box it was drawn in, re-measured from the rendered SVG | whether a figure communicates |
| `check_document.py` | placeholders, citation resolution, cross-reference resolution in a document source | whether a citation *supports* its sentence |
| `check_reporting_registry.py` | every adopted component has a type, a source, a retrieval date and an **authority boundary** | whether the adoption was wise |

## 2. Generators — output is derived, never hand-edited

| Script | Generates | Drift check |
|---|---|---|
| `check_agent_guide.py` | every path, command and count in `AGENTS.md` and `CLAUDE.md` resolves against this repository | — |
| `ready_queue.py` | which packages can be started today, from plan dependencies plus the unsealed ledger | `--check` |
| `progress.py` | moves a package between states and **refuses** what the plan forbids, citing the document that forbids it | — |
| `make_figures.py` | all nine figures, then runs containment | `--check` |
| `fig_lifecycle.py` · `fig_roles.py` · `fig_evidence.py` · `fig_stack.py` · `fig_reporting.py` | one figure each — lifecycle, roles, evidence chain, stack, reporting | via `make_figures.py` |
| `fig_waves.py` · `fig_trust.py` · `fig_verification.py` · `fig_topology.py` | one figure each — commissioning waves, ADR-003 trust boundary, the verification bundle, repository/vault topology | via `make_figures.py` |
| `figure_kit.py` | *(library)* SVG primitives with real text metrics; **fails the build** rather than clipping text | — |
| `make_plan_indexes.py` | a README for each of the 14 commissioning workstreams | `--check` |
| `mirror_plan.py` · `mirror_vault.py` | the generated areas of the Obsidian vault | `--check` |
| `write_status.py` | `docs/STATUS.md` by running the bundle | `--check` |

## 3. Working tooling

| Script | Does | Honest limit |
|---|---|---|
| `evidence_manifest.py` | issues and verifies `EvidenceManifest` attestations — in-toto Statement, DSSE envelope, Ed25519 signature, interim time anchor | profile `airl-interim-v0.1`: **local key, no transparency log**. Tamper-evident, **not externally witnessed** |
| `verify_references.py` | resolves the source registry against Crossref, OpenAlex and arXiv | measures **existence**, not support |
| `monitor_sources.py` | sweeps Crossref for retractions, corrections and expressions of concern | **fails if its positive control stays silent**; blind to sources with no DOI |
| `mcp_smoke.py` | asserts the exact five-tool read-only MCP boundary | needs a live Bridge |
| `acceptance_v0.py` | 11 data-independent structural checks | needs a live Bridge and a local Zotero |

## 4. Which run where

```
BVC-01 (deploy/bvc-01-verify.yml, written but not active)
    pytest · validate_skills · validate_commissioning_plan
    check_doc_consistency · check_stale_claims · check_reporting_registry
    sha256sum -c · make_figures --check

Manual, because they need something CI does not have
    mcp_smoke · acceptance_v0          a live Bridge, a local Zotero library
    mirror_plan --check · mirror_vault --check   the operator's Obsidian vault
    verify_references · monitor_sources          network access
```

## 5. The rule these scripts exist to enforce

> **A check that cannot fail proves nothing.** `monitor_sources.py` carries a
> known-retracted positive control and exits non-zero if it stays silent;
> `figure_kit` raises rather than shrinking text below legibility;
> `check_stale_claims.py` was itself corrected after it flagged legitimate
> history. Each of those is the same rule applied to the tooling that applies it.
