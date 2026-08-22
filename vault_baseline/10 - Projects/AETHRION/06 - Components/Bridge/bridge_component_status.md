---
title: "Bridge Component Status"
airl_id: AETHRION-BRIDGE-STATUS
type: reference
category: vault
status: active
summary: "The Zotero-to-Obsidian bridge: what runs, what is tested, and the findings still open against it."
generated: false
tags:
  - aethrion/component
  - aethrion/status
cssclasses:
  - aethrion-reference
---

# Bridge Component Status

The Bridge is not the whole AETHRION; it is the first working
component, providing the Zotero → canonical source store → Obsidian projection →
Hermes read-only flow.

## Current evidence

- The Zotero Local API read-only boundary is defined.
- The FastAPI Bridge and the SQLite source registry exist.
- The Obsidian projection and Hermes read-only access exist.
- The initial contract foundation sits under `src/airl_framework/`.
- Test evidence and implementation history are kept in [[implementation_log]].

## Checks that now run against it

| Check | Result |
|---|---|
| Reference verification against Crossref · OpenAlex · arXiv | **27/33 corroborated (81.8 %)** |
| Retraction sweep against Crossref | 15 of 33 swept, 0 material signals, control fired |
| MCP boundary | five read-only tools; exits 1 when the Bridge is down |

**18 of 33 sources carry no DOI** and are invisible to the retraction sweep — a
clean report over them would be false reassurance.

## Known limitation

Ingest is hard-capped at 100 records: there is no pagination and no incremental
`since=` sync. Once the library exceeds 100 sources, synchronisation becomes
**silently partial**. See finding **H1** in the audit report.

## Not yet equivalent to the full framework

The control/event, model/agent/tool, execution security, evidence assurance,
observability, integration cutover and Day-2 operations packages are **not**
covered by the Bridge. They are tracked as plan items and separate deliverables.

## Related records

- [[framework_repository_and_obsidian_map]]
- [[00_navigation_and_execution_cockpit]]
- [[implementation_log]]
- [[claude_full_framework_review_prompt]]
