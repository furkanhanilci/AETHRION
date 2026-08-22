# Components Index

Framework components and their real status. **A component being planned does not
mean it has been built.**

## Component status

| Component | Status | Record |
|---|---|---|
| **Bridge** (Zotero → SQLite → Obsidian → MCP) | ✅ **WORKING** | [[10 - Projects/AI Research Framework/06 - Components/Bridge/bridge_component_status\|Bridge Component Status]] |
| Contract core (`airl_framework`) | ⚠️ `TECH_COMPLETE` — no production consumer | — |
| Skill Registry (52 skills) | ✅ format-conformant and checked · 📐 **behaviour untested** | [[skills_index]] |
| Reference verification (CoE check 1) | ✅ **WORKING and measured** — 27/33 corroborated | `scripts/verify_references.py` |
| Source monitoring (first slice of G10) | ✅ **WORKING** — positive control fires | `scripts/monitor_sources.py` |
| Evidence attestation (WP-000 interim) | ✅ **WORKING** — `airl-interim-v0.1`, no transparency log | `scripts/evidence_manifest.py` |
| Plan semantics validator | ✅ **WORKING** | `scripts/validate_commissioning_plan.py` |
| Document + registry checkers | ✅ **WORKING** | `scripts/check_document.py`, `check_reporting_registry.py` |
| Figure generators (5) | ✅ **WORKING** — generated and containment-checked | `scripts/fig_*.py` |
| BVC-01 verification on push | 📐 written, **not active** | `deploy/bvc-01-verify.yml` |
| Authoring toolchain (Quarto etc.) | ⬜ **not installed** — bake-off unrun | — |
| Temporal / Gate Service | ⬜ not built | — |
| NATS / Outbox | ⬜ not built | — |
| Source Registry (PostgreSQL) | ⬜ not built (SQLite V0 exists) | — |
| Claim / Evidence Ledger | ⬜ not built | — |
| Tool Broker / Execution Broker | ⬜ not built | — |
| **Notification Broker** | 📐 **proposed** | Skill Layer, Section 4-G |
| Model Gateway / Capability Registry | ⬜ not built | — |
| Metascience plane | 📐 proposed | Ideal Structure, Section C |

**Notation:** ✅ working · ⚠️ partial · 📐 designed · ⬜ not built

## The boundary

The Bridge is the framework's **first vertical slice**, not its root. The Bridge
working does not mean the 140 work packages have been built.
