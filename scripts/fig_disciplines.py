#!/usr/bin/env python3
"""Figure 15 — two disciplines, four pairs that rhyme, and why substituting one fails.

Five-second message
    Engineering and scientific discipline are not two vocabularies for one
    practice. Four of their skills sound like synonyms, and each substitution
    produces work that passes its own checks and answers the wrong question.

Why this figure exists
    `ADR-012` is one of the most-referenced decision records in the corpus and
    had no figure. Its content is a *distinction*, and a distinction written as
    prose is exactly what a reader skims — the four pairs read as a glossary
    rather than as four ways to be wrong. Drawn as a facing matrix with the
    failure spelled out between the halves, the resemblance becomes the point
    rather than a footnote.

    It also has a live consumer now. `check_skill_baseline.py` R3 requires both
    halves of every pair to stay in different families and both to stay routable
    — because seventeen skills were reachable by no chain from the router, and
    two of them were the scientific halves drawn here while their engineering
    counterparts sat in the router table.

Archetype
    A facing pair matrix. Left column engineering, right column scientific, and
    the middle column is not a connector — it is the sentence that says what
    breaks. Nothing in this figure is a pipeline, because the relationship is
    correspondence, not sequence.

Sources
    docs/architecture/ADR-012_dual_disciplines.md §2
    skills/_baseline/routing.json — non_synonym_pairs
    scripts/check_skill_baseline.py — rule R3
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

# The pairs are read from the baseline fixture, not retyped here. Same rule the
# rest of the corpus follows: a figure that carries its own copy of a fact will
# eventually carry a different one.
PAIRS_FILE = ROOT / "skills" / "_baseline" / "routing.json"

FAILURE = {
    "test-driven-development":
        "Passing tests on an analysis reshaped after seeing the data is a "
        "correct implementation of a compromised study.",
    "requesting-code-review":
        "A reviewer who approves the diff has said nothing about the inference.",
    "systematic-debugging":
        "Debugging assumes the expectation is right. Treating every anomaly as "
        "a bug is how a discovery gets fixed.",
    "dispatching-parallel-agents":
        "One decomposes work with a single right answer. The other produces a "
        "spread, because the answer is not known.",
}


def main() -> None:
    pairs = json.loads(PAIRS_FILE.read_text(encoding="utf-8"))["non_synonym_pairs"]
    row_h = 116
    H = 300 + len(pairs) * row_h + 214
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "Two disciplines, and the four pairs that get conflated",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "A research adaptation EXTENDS its engineering counterpart; it does not replace it. Building the "
               "ledger that stores preregistrations is test-driven-development work, however scientific the noun "
               "sounds. The four rows below are the places that rule is hardest to hold, because each pair commits "
               "to something before an outcome and the resemblance stops there.",
               tw, size=18, lh=24)

    # column headers
    hy = y + 38
    col_w = 268
    mid_x = L + col_w + 26
    mid_w = tw - 2 * col_w - 52
    c.text(L + col_w / 2, hy, "ENGINEERING", size=18, weight="700", fill=BLUE)
    c.text(mid_x + mid_w / 2, hy, "substituting one for the other produces…",
           size=17, weight="700", fill=VERM)
    c.text(W - L - col_w / 2, hy, "SCIENTIFIC", size=18, weight="700", fill=GREEN)
    c.hrule(L, W - L, hy + 12, sw=1.6, stroke=INK)

    top = hy + 28
    for i, pair in enumerate(pairs):
        ry = top + i * row_h
        if i % 2:
            c.rect(L, ry - 14, tw, 102, fill=tint(MUTE, 0.05), stroke="none", sw=0)

        eng = pair["engineering"]
        c.cell(L, ry, col_w, 74, eng, "", accent=BLUE,
               head_size=17, max_head_lines=2)

        sci = pair["scientific"]
        label = " · ".join(sci)
        c.cell(W - L - col_w, ry, col_w, 74, label, "", accent=GREEN,
               head_size=17, max_head_lines=3)

        # The middle is the content. Two short arrows meeting the failure text,
        # so the eye reads inward rather than left-to-right as a flow.
        c.path(f"M {L + col_w + 4} {ry + 37} L {mid_x + 10} {ry + 37}",
               stroke=RULE, sw=1.6, marker="arrowsm")
        c.path(f"M {W - L - col_w - 4} {ry + 37} L {mid_x + mid_w - 10} {ry + 37}",
               stroke=RULE, sw=1.6, marker="arrowsm")
        c.para(mid_x + 22, ry + 22, FAILURE[eng], mid_w - 44,
               size=16, fill=INK, lh=20, max_lines=4)

    ly = top + len(pairs) * row_h + 4
    c.hrule(L, W - L, ly, sw=1.6, stroke=INK)

    # ---- what makes this checkable rather than advisory --------------------
    ny = ly + 26
    c.text(L, ny, "Why this is a control and not a glossary",
           size=21, weight="700", anchor="start")
    ny2 = ny + 26
    cards = [
        ("different families", "each half carries a different airl.domain, so a "
         "router that sees one family cannot choose between them", BLUE),
        ("both halves routable", "a scientific half unreachable while its "
         "engineering counterpart is routable sends the task to the wrong one", VERM),
        ("R3, with a mutation", "collapse a pair into one family and the rule "
         "must refuse — a check nobody has watched fail is not a check", GREEN),
    ]
    cw = (tw - 2 * 18) / 3
    for i, (head, body, col) in enumerate(cards):
        c.cell(L + i * (cw + 18), ny2, cw, 118, head, body, accent=col,
               head_size=18, body_size=16, max_head_lines=2, max_body_lines=5)

    fy = ny2 + 118 + 22
    c.rect(L, fy, tw, 102, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, fy + 28, "The failure this prevented, already once",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, fy + 50,
           "dispatching-parallel-analysts was reachable by no chain of references from the router while "
           "dispatching-parallel-agents sat in its table. A task needing independent analyses would have routed to "
           "the one that decomposes work with a single right answer — not through a bad judgement, but through the "
           "correct option being absent.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    out = ROOT / "docs" / "figures" / "aethrion_disciplines.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_disciplines.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
