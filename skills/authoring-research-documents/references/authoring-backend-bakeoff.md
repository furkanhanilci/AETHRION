# Authoring Backend Bake-off — Protocol and Status

| Field | Value |
|---|---|
| Status | **SPECIFIED · NOT RUN.** No result exists |
| Blocker | Neither Quarto, Pandoc, Typst, LaTeX nor MyST is installed in the environment that wrote this |
| Feasible | **Yes** — Docker is available, so each candidate can run pinned in a container |
| Date | 2026-08-22 |

**In one paragraph.** The authoring stack must be chosen by rendering the same
specimen through each candidate and comparing what survives — not by preferring
the tool with the better documentation. This file fixes the specimen, the
protocol and the scoring so that the comparison, when it is run, is a
measurement rather than a justification. **Until it runs, Quarto is a provisional
default and is labelled as one everywhere it appears.**

## 1. Candidates

| | Stack |
|---|---|
| **A** | Quarto + Pandoc + Typst/LaTeX |
| **B** | MyST |

Both are scientific authoring systems with citations, cross references,
multi-format output and journal templates. Neither is obviously correct without
evidence.

## 2. The specimen must contain

Marketing pages are not compared; **the same document is**. It contains:

- title and metadata · 2–3 authors · ORCID fields · an affiliation with a ROR
- abstract · headings · footnote · acronym
- citations and a bibliography
- an equation **and a reference to it**
- a figure **with a cross reference and alt text**
- a table **with a cross reference**
- an appendix · one supplementary file
- a generated result, if execution is permitted

Cross references and alt text are in the list deliberately: they are where
authoring systems most often differ, and where silent degradation is easiest to
miss.

## 3. Attempted outputs

`HTML` · `PDF` · `DOCX` · `LaTeX or Typst source` · `JATS` · `MECA`

A format a candidate does not support is recorded as unsupported, not as a
failure of the candidate.

## 4. Record per candidate

```yaml
authoring_bakeoff:
  candidate:
  version:
  source_lines:
  successful_outputs:
  failed_outputs:
  citation_integrity:
  crossref_integrity:
  docx_fidelity:
  pdf_fidelity:
  journal_template_compatibility:
  jats_quality:
  meca_support:
  accessibility_support:
  plugin_filter_model:
  provenance_capture:
  deterministic_build:
  build_speed:
  dependency_surface:
  error_legibility:
  override_complexity:
  maintainability:
```

## 5. Weighting, in order

1. document correctness
2. venue compatibility
3. citation and cross-reference integrity
4. reproducibility
5. structured export quality
6. Word interoperability
7. PDF quality
8. maintainability
9. extensibility
10. speed
11. aesthetics

> **Template count is not a criterion.** A stack with four hundred templates and
> silent cross-reference loss is worse than one with forty that never drops a
> reference. Do not weight breadth above correctness.

## 6. The architecture is the same whichever wins

```
AIRL Document Model
        │
   AuthoringBackend
        ├── QuartoBackend
        └── MySTBackend (optional)
```

**The selected renderer never becomes AIRL's canonical research model.** If the
same `DocumentContract`, `ClaimCitationMatrix` and bibliography projection cannot
render through both, the loss of portability is recorded as a finding rather than
discovered later.

## 7. Honest status

No candidate has been installed, no specimen has been rendered, and no cell of
§4 is filled. Any statement that this project "uses Quarto" describes a
**provisional intention**, not a measured decision.
