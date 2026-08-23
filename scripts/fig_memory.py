#!/usr/bin/env python3
"""Figure 11 — the six epistemic memories, and which one may support a claim.

Five-second message
    There is no such thing as "the memory". What the system remembers is split
    six ways by epistemic status, and only one of the six may stand behind a
    claim.

Why this figure exists
    The default agent design writes everything into one store and retrieves by
    similarity. Drawn that way, a raw evaluator output and a stale debugging
    note look identical — which is exactly how a reusable lesson ends up cited
    as evidence. This figure draws the axes that actually differ.

Archetype
    A comparison table whose columns are the properties that decide authority,
    with the immutable and the decaying stores at opposite ends and the
    isolation rule stated as its own band.

Sources
    docs/architecture/ADR-005_epistemic_memory_separation.md,
    planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-146
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

# store, what it holds, immutable, decays, may support a claim, accent
STORES = [
    ("Evidence", "raw source representations, evaluator outputs, exact spans, signed manifests",
     "yes", "never", "YES — subject to admissibility", ORANGE),
    ("Finding", "what a set of evidence was interpreted to mean: supported, refuted, inconclusive",
     "versioned", "no", "indirectly — a claim is drafted from it", GREEN),
    ("Search experience", "plan, code, metric, parent edges, mechanism tags, outcome of each candidate",
     "append", "yes, archivable", "no", BLUE),
    ("Procedural", "reusable method and debugging lessons, and why an approach could not be applied",
     "versioned", "yes, revalidated", "no", SKY),
    ("Principle", "the working beliefs beneath a hypothesis, and the evidence challenging them",
     "versioned", "supersedable", "no — a belief is not a claim", PURPLE),
    ("Human intervention", "every approve, reject, edit, guidance, rollback and abort, with before and after",
     "yes", "never", "as decision evidence only", VERM),
]


def main() -> None:
    row_h = 78
    H = 250 + len(STORES) * row_h + 520
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "Six memories, and only one of them may support a claim",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "A raw evaluator output, a failed experiment, a debugging lesson and a working scientific principle "
               "do not have the same standing. They differ on whether they may support a claim, whether they may "
               "change, whether they may expire and who may read them. One store cannot hold four regimes, and the "
               "failure it ends in is a stale note being cited as evidence.",
               tw, size=18, lh=24)

    # ------------------------------------------------------------------ table
    hy = y + 40
    c1, c2, c3, c4 = 210, 372, 132, 150
    c5 = tw - c1 - c2 - c3 - c4 - 40
    xs = [L, L + c1 + 10, L + c1 + c2 + 20, L + c1 + c2 + c3 + 30, L + c1 + c2 + c3 + c4 + 40]
    for x, head, col in zip(xs,
                            ["Store", "What it holds", "Immutable", "Decays",
                             "May support a claim"],
                            [INK, INK, MUTE, MUTE, ORANGE]):
        c.text(x, hy, head, size=17, weight="700", anchor="start", fill=col)
    c.hrule(L, W - L, hy + 12, sw=1.6, stroke=INK)

    top = hy + 26
    for i, (name, holds, imm, dec, claim, col) in enumerate(STORES):
        ry = top + i * row_h
        if i % 2:
            c.rect(L, ry + 8, tw, row_h - 8, fill=tint(MUTE, 0.05), stroke="none", sw=0)
        c.rect(L, ry + 8, 5, row_h - 26, fill=col, stroke="none", sw=0, rx=2)
        c.text(xs[0] + 16, ry + 30, name, size=18, weight="600", anchor="start")
        c.para(xs[1], ry + 26, holds, c2 - 12, size=16, fill=MUTE, lh=20, max_lines=3)
        c.text(xs[2], ry + 30, imm, size=16, anchor="start", fill=INK)
        c.text(xs[3], ry + 30, dec, size=16, anchor="start", fill=INK)
        c.para(xs[4], ry + 26, claim, c5, size=16,
               fill=ORANGE if claim.startswith("YES") else MUTE, lh=20, max_lines=3,
               weight="700" if claim.startswith("YES") else "400")

    ly = top + len(STORES) * row_h + 4
    c.hrule(L, W - L, ly, sw=1.6, stroke=INK)

    # ------------------------------------------------------- the two extremes
    ey = ly + 30
    c.text(L, ey, "The two extremes are what force the split",
           size=21, weight="700", anchor="start")
    ey2 = ey + 22
    half = (tw - 26) / 2
    c.cell(L, ey2, half, 132,
           "Evidence never decays",
           "A source can be retracted and its status changes; the bytes do not. That is not conservatism — a "
           "claim anchored to a retracted source has to stay traversable after the retraction, or the G10 "
           "impact scan has nothing to walk.",
           accent=ORANGE, head_size=19, body_size=16, max_body_lines=5)
    c.cell(L + half + 26, ey2, half, 132,
           "Procedural memory must",
           "“This library needs that flag” is true about a version on a date, and it goes stale silently — "
           "no error, no signal, just advice that stopped applying. It is versioned, it expires and it is "
           "revalidated.",
           accent=SKY, head_size=19, body_size=16, max_body_lines=5)

    # ---------------------------------------------------------- isolation band
    iy = ey2 + 132 + 34
    indep_h = 112
    c.rect(L, iy, tw, indep_h, fill=tint(VERM, 0.10), stroke=VERM, sw=2.0)
    c.text(L + 18, iy + 28, "Memory is an independence question, not only a retrieval one",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, iy + 52,
           "Independence is usually asked as who reviews. It is also what the reviewer can read. A reviewer able "
           "to query the producer's search experience inherits the producer's dead ends and framing — the review "
           "is anchored, and nothing in the record shows it, because the actor really is different. So blind "
           "review excludes the producer's search and procedural memory by default. ACC-72 and ACC-79.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    # ------------------------------------------------------------ derived note
    dy = iy + indep_h + 34
    c.text(L, dy, "Derived, and therefore droppable", size=19, weight="700", anchor="start")
    c.para(L, dy + 24,
           "Vector indexes, the graph projection and the research map are read models over the canonical stores. "
           "They make retrieval fast; nothing lives in them, and any of them can be dropped and rebuilt — ACC-71 "
           "requires exactly that rebuild to be lossless. An embedding index that cannot be regenerated from "
           "PostgreSQL and the object store is a defect, not a store.",
           tw, size=17, fill=MUTE, lh=22, max_lines=4)

    ny = dy + 24 + 4 * 22 + 26
    c.text(L, ny, "Status: no store is implemented. WP-146 specifies the taxonomy; the evidence store's first "
                  "slice depends on WP-026, which does not exist either.",
           size=16, anchor="start", fill=MUTE, style="italic")

    out = ROOT / "docs" / "figures" / "aethrion_memory.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_memory.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
