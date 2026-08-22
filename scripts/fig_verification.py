#!/usr/bin/env python3
"""Figure 8 — the verification bundle: what the repository proves about itself.

Five-second message
    Ten checks keep the corpus honest about its own state; none of them can
    tell you whether the research is any good.

Archetype
    A claim/evidence pairing with an explicit blind-spot column. The blind
    spots are the reason the figure exists: a green dashboard that does not
    say what it cannot see is a misleading instrument.

Sources
    docs/STATUS.md (generated), scripts/README.md, docs/architecture/AIRL_OS_VERIFICATION.md
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, fit, text_width, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

CHECKS = [
    ("Test suite", "pytest", "the bridge code behaves as its tests describe",
     "the tests were written by the same author as the code", GREEN),
    ("Skill registry", "validate_skills.py", "every skill parses and carries the AIRL metadata contract",
     "no skill has been run against a task and scored", BLUE),
    ("Plan seal", "seal_commissioning_plan.py", "221 planning files are byte-identical to the sealed baseline",
     "a sealed document can still be wrong", PURPLE),
    ("Plan semantics", "validate_commissioning_plan.py", "identifiers resolve, references are bidirectional, the DAG is acyclic",
     "feasibility of the work itself is not modelled", PURPLE),
    ("Workstream indexes", "make_plan_indexes.py --check", "every generated index matches its directory",
     "nothing about the content of what is indexed", MUTE),
    ("Declared counts", "check_doc_consistency.py", "numbers written in prose match the repository",
     "only the numbers that were registered as rules", ORANGE),
    ("Stale claims", "check_stale_claims.py", "no document claims a state the repository has outgrown",
     "a claim can be current and still false", ORANGE),
    ("Figure drift", "check_doc_consistency.py", "the figure inventory matches the files on disk",
     "whether a figure argues its point", BLUE),
    ("Figure containment", "check_figures.py", "no glyph in any figure overflows its box, re-measured independently",
     "typography, not meaning", BLUE),
    ("Reporting register", "check_reporting_registry.py", "every external claim has a type, a source and a retrieval date",
     "whether the source actually says it", GREEN),
]


def main() -> None:
    row_h = 62
    H = 300 + len(CHECKS) * row_h + 240
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "The verification bundle, and its blind spots", size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "One command runs everything below and refuses to pass on a warning. This is the machine half of "
               "“agents produce, machines verify, humans decide”. Each row states the claim the check earns and, "
               "beside it, the claim it does not — because a bundle that reports only green teaches its reader to "
               "trust it for things it never examined.",
               tw, size=18, lh=24)

    hy = y + 34
    c1, c2 = 250, 452
    c3 = tw - c1 - c2 - 28
    c.text(L, hy, "Check", size=17, weight="700", anchor="start", fill=INK)
    c.text(L + c1 + 14, hy, "What it proves", size=17, weight="700", anchor="start", fill=GREEN)
    c.text(L + c1 + c2 + 28, hy, "What it cannot see", size=17, weight="700", anchor="start", fill=VERM)
    c.hrule(L, W - L, hy + 12, sw=1.6, stroke=INK)

    top = hy + 24
    for i, (name, script, proves, blind, colour) in enumerate(CHECKS):
        ry = top + i * row_h
        if i % 2:
            c.rect(L, ry, tw, row_h - 6, fill=tint(MUTE, 0.05), stroke="none", sw=0)
        c.rect(L, ry + 8, 5, row_h - 24, fill=colour, stroke="none", sw=0, rx=2)
        c.text(L + 16, ry + 26, name, size=18, weight="600", anchor="start")
        c.text(L + 16, ry + 46, script, size=16, anchor="start", fill=MUTE)
        c.para(L + c1 + 14, ry + 26, proves, c2 - 14, size=17, fill=INK, lh=21, max_lines=2)
        c.para(L + c1 + c2 + 28, ry + 26, blind, c3, size=17, fill=MUTE, lh=21, max_lines=2)

    ly = top + len(CHECKS) * row_h + 10
    c.hrule(L, W - L, ly, sw=1.6, stroke=INK)

    # The loop
    py = ly + 26
    c.text(L, py + 4, "Why it holds: the bundle is not allowed to be optional", size=21, weight="700", anchor="start")
    steps = [("A document changes", "prose, plan, skill or figure", BLUE),
             ("Truth is re-derived", "counts and inventories come from the repository, never from memory", BLUE),
             ("The bundle runs", "any warning is a failure; there is no advisory tier", PURPLE),
             ("STATUS.md is rewritten", "generated, never hand-edited, and its own --check catches editing", GREEN),
             ("Evidence is reissued", "the manifest is signed again and verifies, or the change does not land", VERM)]
    sy = py + 28
    bw = (tw - 4 * 14) / 5
    for i, (h, b, col) in enumerate(steps):
        bx = L + i * (bw + 14)
        c.cell(bx, sy, bw, 104, h, b, accent=col, head_size=17, body_size=16,
               max_head_lines=2, max_body_lines=4)
        if i:
            c.path(f"M {bx - 13} {sy + 52} L {bx - 3} {sy + 52}", stroke=RULE, sw=1.8, marker="arrowsm")
    c.path(f"M {L + bw / 2} {sy + 104} L {L + bw / 2} {sy + 122} L {L + tw - bw / 2} {sy + 122} "
           f"L {L + tw - bw / 2} {sy + 104}", stroke=RULE, sw=1.6, dash="5 4", marker=None)

    ny = sy + 104 + 44
    c.text(L, ny + 24, "Honest limit", size=18, weight="700", anchor="start", fill=VERM)
    c.para(L + 118, ny + 24,
           "Everything here is internal consistency. The bundle can confirm that this repository says the same thing "
           "everywhere, that its plan is well-formed and that its evidence verifies — and all of that would still "
           "hold for a corpus describing a system that does not work. External truth enters through exactly two "
           "doors: reference verification against Crossref, OpenAlex and arXiv, and the benchmarks named in the "
           "adoption matrix, none of which has been run.",
           W - L - (L + 118), size=17, fill=INK, lh=23)

    out = ROOT / "docs" / "figures" / "airl_os_verification.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/airl_os_verification.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
