# Reporting Architecture — Where This Subsystem Sits

**In one paragraph.** Document production is **cross-cutting**, not a new
authority plane. It can generate a protocol report at G2, a literature report at
G3, an experiment report at G5, an assurance report at G6/G7, a decision memo at
G8 and a manuscript at G9 — but **only the relevant gate decides what the
document means operationally.** A rendered document is an artifact; whether it
may be published is a G9 decision made by a human.

## The layers, and what each may decide

```
HUMAN / EXPERIENCE
  Zotero — literature, PDFs, annotations, metadata curation
  Obsidian — notes, synthesis, planning
  Cockpit — project state, gates, findings, decisions
        │
        ▼
AUTHORING ORCHESTRATOR
  DocumentContract · EvidenceInventory · ClaimCitationMatrix
  DocumentOutline · DocumentSource
        │
        ├── AuthoringBackend ......... Quarto/Pandoc · MyST (optional)
        ├── BibliographyAdapter ...... Zotero · Better BibTeX · CSL · Crossref
        ├── Figure subsystem ......... producing-figures
        ├── Table/equation subsystem
        ├── PublicationMetadata ...... ORCID · ROR · CRediT · DataCite · CITATION.cff
        ├── QA ....................... AIRL evidence and scope checks · citation and
        │                              crossref checks · CoE Audit · Vale ·
        │                              LanguageTool (local) · guideline resolver ·
        │                              WCAG · veraPDF
        ├── RenderBackend ............ Typst · LaTeX · DOCX reference template · HTML
        └── Export ................... PublicationPackage · JATS · MECA · venue bundle
        │
        ▼
G9 — HUMAN-CONTROLLED PUBLICATION DECISION
```

## Four objects that are not the same thing

Conflating these is the most common way an evidence chain is lost:

| Object | Is | Is not |
|---|---|---|
| **DocumentSource** | The editable canonical source | The rendered artifact |
| **RenderedDocument** | A PDF/DOCX/HTML generated from a source version | Evidence of correctness |
| **PublicationPackage** | The evidence-bound bundle: source, bibliography, figures, tables, supplements, metadata, QA, provenance, hashes | A zip of outputs |
| **SubmissionExchangePackage** | A target-specific projection — MECA, publisher zip, upload bundle | The canonical record |

> **A rendered document does not become a `PublicationPackage` because rendering
> succeeded.** It becomes one when its claims resolve, its QA is recorded, its
> provenance is captured and a human decides.

## Six separations that must not collapse

| Layer | Question |
|---|---|
| **Scientific truth** | What may be claimed? |
| **Document architecture** | What structure communicates it? |
| **Narrative** | In what order does the reader meet it? |
| **Visual communication** | What must be seen rather than read? |
| **Presentation** | Fonts, margins, venue template |
| **Output** | Which formats, and packaged how? |

A single generative pass that produces "a polished paper" collapses all six, and
the first casualty is always the first row.

## Continuous manuscript discipline

The document project is Git-backed, and a material change answers: which claims
changed · which citations · which figures or tables · which evidence links ·
which venue or template · which rendered artifacts · why · who approved.

**Not every change is a scientific revision.** Separate editorial-only changes
from semantic, evidence, result and template changes — recording a typo fix as a
claim revision destroys the signal the revision log exists to carry.

## Integration boundaries

- **Zotero stays the human bibliographic workspace.** No AIRL-only library UI is
  built to duplicate it.
- **Obsidian stays the human knowledge workspace.** No renderer writes into
  unrestricted human notes; generated projections live in generated areas only.
- **The Claim Ledger stays canonical.** The `ClaimCitationMatrix` is a *document
  projection* of it, never a second claim model.
