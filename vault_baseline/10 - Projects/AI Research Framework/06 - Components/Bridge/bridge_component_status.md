# Bridge Component Status

The Bridge is not the whole AI Research Framework; it is the first working
component, providing the Zotero → canonical source store → Obsidian projection →
Hermes read-only flow.

## Current evidence

- The Zotero Local API read-only boundary is defined.
- The FastAPI Bridge and the SQLite source registry exist.
- The Obsidian projection and Hermes read-only access exist.
- The initial contract foundation sits under `src/airl_framework/`.
- Test evidence and implementation history are kept in [[implementation_log]].

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
