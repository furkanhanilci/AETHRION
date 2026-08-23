#!/usr/bin/env python3
"""Figure 5 — the document production pipeline, and where it may not decide.

Five-second message
    A document is produced by a pipeline that runs evidence → claims → structure
    → prose → figures → QA → render, and the renderer's success is not the
    decision: publication remains a human act at G9.

Archetype
    A staged pipeline with an authority band. A plain left-to-right flow would
    imply that the last stage concludes the work, which is the exact error this
    subsystem exists to prevent — so authority is drawn as a separate channel.

Sources
    skills/authoring-research-documents/SKILL.md — the phase list
    references/reporting-architecture.md — the four package objects
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, fit, text_width, tint)

W = 1200
L = 24
STAGES = [
    ("Evidence", "sources · runs · gaps · contradictions", GREEN),
    ("Claims", "typed, scoped, before any prose", GREEN),
    ("Structure", "archetype · outline · narrative", BLUE),
    ("Draft", "section by section from the matrix", BLUE),
    ("Figures & tables", "inventory first, then produced", BLUE),
    ("QA", "scientific · statistical · guideline · language · venue", ORANGE),
    ("Render", "only the formats the contract requires", ORANGE),
    ("Artifact QA", "inspect the PDF, not the source", ORANGE),
    ("Review", "through the existing review skills", PURPLE),
]
LADDER = [
    ("DocumentSource", "the editable canonical source", GREEN, True),
    ("RenderedDocument", "an artifact, not a verdict", BLUE, False),
    ("PublicationPackage", "claims resolved · QA · provenance · hashes", ORANGE, False),
    ("SubmissionExchange", "MECA · publisher bundle", PURPLE, False),
]
H = 1010


def main() -> None:
    c = Canvas(W, H)
    tw = W - 2 * L
    c.text(L, 48, "How a document is produced, and what may decide", size=30,
           weight="700", anchor="start")
    y = c.para(L, 80,
               "The pipeline runs evidence first and formatting last. A renderer exiting zero means the document "
               "rendered; it says nothing about whether the document is true, complete or publishable.",
               tw, size=18, lh=24)
    y = c.para(L, y + 26,
               "Every external tool below produces a signal. None of them decides.",
               tw, size=18, fill=INK, weight="600", lh=24)

    # ---- stage ladder -----------------------------------------------------
    y += 44
    c.text(L, y, "(a)  The pipeline — formatting is downstream", size=20,
           weight="700", anchor="start")
    y += 18
    cols, gap = 3, 12
    row_gap = 34          # room for the wrap connector to run in
    cw = (tw - (cols - 1) * gap) / cols
    ch = 74
    for i, (head, body, colour) in enumerate(STAGES):
        row, col = divmod(i, cols)
        x = L + col * (cw + gap)
        yy = y + row * (ch + row_gap)
        c.cell(x, yy, cw, ch, f"{i}. {head}", body, accent=colour, sw=1.6,
               head_size=18, max_body_lines=2)
        if col < cols - 1 and i < len(STAGES) - 1:
            c.path(f"M {x + cw + 1} {yy + ch / 2} L {x + cw + gap - 3} {yy + ch / 2}",
                   stroke=MUTE, sw=1.4, marker="arrowsm")
        elif col == cols - 1 and i < len(STAGES) - 1:
            # The wrap. Without it the grid carried arrows WITHIN each row and
            # nothing between them, so the only thing telling a reader that
            # stage 2 leads to stage 3 was the numbering — a sequence repaired
            # by its own labels. Routed round the right edge and back along the
            # row gap, clear of every cell.
            cx_end = x + cw / 2
            mid = yy + ch + row_gap / 2
            nx = L + cw / 2
            c.path(f"M {cx_end} {yy + ch + 1} L {cx_end} {mid} "
                   f"L {nx} {mid} L {nx} {yy + ch + row_gap - 3}",
                   stroke=MUTE, sw=1.4, dash="4 3", marker="arrowsm")
            c.text((cx_end + nx) / 2, mid - 6, "continues", size=15, fill=MUTE)
    y += 3 * (ch + row_gap) + 4

    c.para(L, y,
           "Stages 0 to 2 finish before a renderer is chosen. A document whose first decision was its template has "
           "already skipped the only stage that could have stopped it.",
           tw, size=16, lh=21)

    # ---- packaging ladder -------------------------------------------------
    y += 52
    c.hrule(L, W - L, y, sw=1.2)
    y += 30
    c.text(L, y, "(b)  Four objects that are not the same thing", size=20,
           weight="700", anchor="start")
    y += 18
    lw = (tw - 3 * 14) / 4
    for i, (head, body, colour, built) in enumerate(LADDER):
        x = L + i * (lw + 14)
        c.cell(x, y, lw, 88, head, body, accent=colour,
               fill=tint(colour, 0.16 if built else 0.07),
               stroke_override=colour if built else MUTE,
               sw=2.2 if built else 1.3, dash=None if built else "5 4",
               head_size=17, head_fill=INK if built else MUTE, max_body_lines=3)
        if i:
            c.path(f"M {x - 14 + 1} {y + 44} L {x - 4} {y + 44}", stroke=MUTE,
                   sw=1.5, marker="arrowsm")
    y += 88

    c.para(L, y + 26,
           "A rendered document does not become a publication package because rendering succeeded. Between them sit "
           "resolved claims, recorded QA, captured provenance — and a human decision at G9.",
           tw, size=17, fill=INK, lh=23)

    # ---- authority band ---------------------------------------------------
    y += 78
    c.rect(L, y, tw, 96, fill=tint(VERM, 0.07), stroke=VERM, sw=1.6)
    c.text(L + 16, y + 30, "Authority", size=19, weight="700", anchor="start", fill=VERM)
    rows = [("Quarto · Pandoc · Typst", "render · resolve references"),
            ("Crossref · OpenAlex", "say a record exists"),
            ("Vale · LanguageTool", "suggest wording"),
            ("veraPDF", "test PDF rules")]
    x = L + 130
    for name, may in rows:
        c.para(x, y + 30, name, 240, size=16, weight="600", fill=INK, max_lines=2)
        c.para(x, y + 70, "may: " + may, 236, size=16, max_lines=2)
        x += 254
    c.para(L + 16, y + 70, "None of them", 108, size=16, weight="600", fill=VERM, max_lines=2)

    ny = y + 96 + 18
    c.hrule(L, W - L, ny, sw=1.2)
    c.text(L, ny + 30, "Status", size=18, weight="700", anchor="start", fill=VERM)
    c.para(L + 70, ny + 30,
           "The skill, its reference modules and the resolution checks exist and run. No renderer is installed here, "
           "so no document in this repository has been rendered, and the authoring backend has not been chosen — the "
           "bake-off is specified and unexecuted.",
           W - L - (L + 70), size=17, fill=INK, lh=23)

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "aethrion_reporting.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_reporting.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
