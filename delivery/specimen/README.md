# Specimen document

| Field | Value |
|---|---|
| Document type | Worked example |
| Scope | One technical report, built from this repository's own measurements |
| Sibling documents | `../../skills/authoring-research-documents/SKILL.md` |
| Status | Source passes the resolution checks; **never rendered** — no toolchain is installed |
| Date | 2026-08-22 |

**In one paragraph.** This exists to exercise the authoring pipeline on real
data rather than on an invented example. Every number in it comes from
`../measurements/`, every reference resolves in a public authority, and it makes
no claim beyond what those two measurements support. It is deliberately narrow —
a specimen that overclaimed would be a poor demonstration of a discipline built
to prevent overclaiming.

| File | Is |
|---|---|
| `airl-measurement-report.qmd` | The document source, in Quarto Markdown |
| `references.bib` | Three verified references, each cited in the text |

```bash
uv run python scripts/check_document.py delivery/specimen/airl-measurement-report.qmd
```

That checks placeholders, citation resolution and cross-reference resolution. It
proves references **resolve**; it does not prove they **support**.

## What it demonstrated by failing

Checking this specimen corrected the checker twice on first contact: sentence
punctuation was being captured into citation keys, and every unreferenced section
anchor was being flagged when only figures, tables and equations must be
referenced. Both are recorded in the implementation log, because a tool corrected
by real use is worth more than one that was never used.

## Not rendered

Quarto, Pandoc, Typst, LaTeX and MyST are absent from this environment, so no PDF
or DOCX exists. The authoring backend has not been chosen either — the bake-off
is specified and unexecuted in
`../../skills/authoring-research-documents/references/authoring-backend-bakeoff.md`.
