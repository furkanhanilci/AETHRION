# Local Knowledge Architecture — V0

> System-wide context and diagrams: [`AIRL_OS_ARCHITECTURE.md`](architecture/AIRL_OS_ARCHITECTURE.md).

## Purpose

This vertical slice treats Zotero as the source authority, SQLite as the
canonical integration layer, Obsidian as the readable knowledge workspace, and
Hermes as a read-only agent access surface.

It is deliberately small. Its job is to prove that a full evidence path can run
end to end before any of the larger infrastructure exists.

```text
Zotero Local API (read-only)
        |
        v
AIRL Bridge API @ 127.0.0.1:8765
        |
        +--> SQLite/WAL canonical source registry
        |
        +--> Obsidian: 70 - Literature Sets/Zotero Sources
        |
        +--> Hermes MCP: five read-only tools
```

## Obsidian layout

```text
00 - Home/
  ai_research_framework_home.md
01 - Inbox/
10 - Projects/
  AI Research Framework/
    00_navigation_and_execution_cockpit.md
    ai_research_framework_current_status_and_roadmap.md
    01 - Commissioning/  02 - Reviews/  03 - Implementation/
    04 - Architecture/   05 - Evidence/ 06 - Components/  07 - Skills/
20 - Source Notes/                 # human synthesis
30 - Concepts/
40 - Claims/
50 - Decisions/
60 - Runs/
70 - Literature Sets/
  literature_sets.md               # human curation
  Zotero Sources/                  # automatically managed branch
    00 - Control Dashboard/
    01 - Journal Articles/
    02 - Conference Papers/
    03 - Reports and Preprints/
80 - Daily/
90 - Archive/
_Templates/
```

## Invariants

1. The Bridge and the Zotero connection listen on the local machine only.
2. Ingest from Zotero is read-only. There is no API key and no write operation.
3. The `Zotero Sources` branch is regenerated and is not hand-edited.
4. Human synthesis lives in `20 - Source Notes`; curated sets live at the root of
   `70 - Literature Sets`.
5. Generated files are named from the article title; a stable
   `Zotero ITEMKEY` suffix is used only for same-title collisions.
6. Possible duplicates are reported. Nothing is merged or deleted automatically.
7. Hermes is offered only status, search, detail, category and duplicate-report
   tools.
8. Synchronisation is repeatable; the same Zotero item retains the same canonical
   identity.

## Authority boundaries

| Component | Reads | Writes |
|---|---|---|
| Zotero Local API | Source metadata | Nothing |
| Bridge API | Source records | Local SQLite and the automatic Obsidian branch |
| Hermes MCP | Five catalogue operations | Nothing |
| Human | The entire vault | Everything except the automatic Zotero branch |

## Known limitations

These are real and documented rather than deferred:

| Limitation | Effect | Finding |
|---|---|---|
| Ingest capped at 100 records, no pagination | Silent partial sync above 100 sources | H1 |
| No deletion reconciliation | Sources removed in Zotero persist as ghosts | H2 |
| `zotero_write_enabled` is a constant | The read-only guarantee is asserted, not tested | H3 |
| Unauthenticated mutating endpoints on loopback | Local CSRF and DNS-rebinding exposure | M1 |
| Silent truncation at 10,000 rows | Projection would drop sources beyond that | M9 |

## Deferred scope

Zotero write-back, automatic duplicate merging, bidirectional Obsidian
synchronisation, remote API exposure, Temporal/LangGraph/Kubernetes, and
production identity infrastructure are outside V0. None of them should be
enabled without their own acceptance criteria and a rollback plan.
