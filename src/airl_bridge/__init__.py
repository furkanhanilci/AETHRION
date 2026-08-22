"""AIRL Bridge — the working vertical slice of the AI Research Framework.

    Zotero Local API (read-only)
        → SQLite canonical source registry
        → Obsidian projection
        → Hermes MCP (five read-only tools)

This package is **one component** of the framework, not the framework. The
control plane, event backbone, execution fabric, evidence ledger, observability
and security platform described in ``planning/commissioning/`` do not exist yet.

Module map:

===================  =========================================================
``config``           Settings, plus the loopback and path-containment boundaries
``models``           Transport models for the API surface
``zotero``           The read-only Zotero client — no write path exists
``database``         The canonical V0 registry (SQLite, WAL)
``catalog``          Category mapping and duplicate *reporting*
``obsidian``         The projection — the only code that deletes user files
``service``          Ingest, projection and the sync that combines them
``main``             The FastAPI application
``cli``              The ``airl-bridge`` entry point
``mcp_server``       Five read-only MCP tools for Hermes
===================  =========================================================

Every module docstring names the audit findings that apply to it. Read them
before changing behaviour: several of the properties that look like conveniences
are the reason no human note has been lost.
"""

__version__ = "0.1.0"
