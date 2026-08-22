# Rendering, Export and Packaging

## Reproducible rendering

A formal document has a canonical source, a deterministic render command, a
declared bibliography and template, output hashes, a render log and recorded
tool versions.

```yaml
RenderManifest:
  document_id:
  source_digest:
  bibliography_digest:
  claim_matrix_digest:
  template_digest:
  csl_digest:
  renderer:
  renderer_version:
  render_command:
  generated_at:
  output_files:
    - path:
      sha256:
  format_profile:
  venue_profile:
  qa_report:
  limitations:
```

`limitations` is not optional. A manifest that records only success is a
marketing artifact.

## Backends

| Output | Backend | Note |
|---|---|---|
| PDF | Typst, or LaTeX where the venue requires it | Venue mandate wins over preference |
| DOCX | Pandoc/Quarto with a reference template | Company or venue `reference.docx` where one exists |
| HTML | Quarto | WCAG 2.2 contract applies |
| LaTeX/Typst source | the chosen backend | Some venues want source, not PDF |
| **JATS** | Quarto | Semantic interchange — **never the authoring format** |
| **MECA** | Quarto, when `jats` is an output format | Submission exchange archive |

Formats are produced **only when the contract requires them**.

## JATS and MECA

JATS is an interchange representation; humans do not author in it. A JATS export
is validated against the applicable **JATS4R** recommendations, because
JATS-valid is not JATS-reusable.

MECA packages a submission — manuscript source, metadata, figures, supplements,
transfer information. Not required for internal reports.

## The packaging ladder

```
DocumentSource            editable canonical source
      ↓ render
RenderedDocument          PDF · DOCX · HTML — an artifact, not a verdict
      ↓ + evidence, QA, provenance, hashes, human decision
PublicationPackage        the evidence-bound bundle
      ↓ project for a target
SubmissionExchangePackage MECA · publisher zip · upload bundle
```

> **A rendered document does not become a `PublicationPackage` because the render
> succeeded.** The step between them is claims resolving, QA recorded, provenance
> captured and a human deciding at G9.

## Software, data and research objects

A package that ships software or data uses the right identity for each rather
than flattening everything into a journal-style citation: **DOI/DataCite**
(4.7 adds `SWHID` as a related-identifier type), **SWHID** for source code,
**CITATION.cff** for citable software, **Croissant** for datasets, **RO-Crate**
and **Workflow Run RO-Crate** for runs.

When a document reports computational results, the chain is explicit:

```
paragraph · table · figure → ClaimVersion → ExperimentRun → Workflow Run RO-Crate
```

**The document points at the run record. The document is not the run record.**

## Toolchain availability

None of Quarto, Pandoc, Typst, LaTeX, Vale or LanguageTool is installed in the
environment where this was written; Docker is. **No rendering path in this file
has been executed here**, and nothing in the repository may claim otherwise —
see `authoring-backend-bakeoff.md`.
