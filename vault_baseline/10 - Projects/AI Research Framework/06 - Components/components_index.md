# Components Index

Framework components and their real status. **A component being planned does not
mean it has been built.**

## Component status

| Component | Status | Record |
|---|---|---|
| **Bridge** (Zotero → SQLite → Obsidian → MCP) | ✅ **WORKING** | [[10 - Projects/AI Research Framework/06 - Components/Bridge/bridge_component_status\|Bridge Component Status]] |
| Contract core (`airl_framework`) | ⚠️ `TECH_COMPLETE` — no production consumer | — |
| Skill Registry | 📐 designed, not yet tested | [[skills_index]] |
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
