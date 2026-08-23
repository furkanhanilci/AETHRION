#!/usr/bin/env python3
"""Figure — the compilation order, and the five levels it must not collapse.

Five-second message
    Cognitive functions are compiled first and a runtime is matched to them
    second. Reversing that order lets a harness shape the cohort.

Archetype
    A left-to-right pipeline over a ladder. The pipeline is the order; the ladder
    is what the order protects. They belong on one figure because the ladder is
    unreadable as an abstraction — *role is not cognitive function* means nothing
    until you can see where in the pipeline each level is decided.

Encoding
    Pipeline    = compilation sequence, one stage per decision
    Ladder      = the five levels, top to bottom by authority, each with the
                  failure that follows from collapsing it into the next
    Refusal bar = compile-time refusals, vermilion because they stop the task

Why refusals are drawn and warnings are not
    A compiler that warns is a compiler whose warnings are read once. Every item
    in the bottom band stops compilation and names the rule that stopped it.

Sources
    docs/architecture/ADR-020 §4 — the five levels
    planning/commissioning/05_MODEL_AGENT_TOOL/WP-047 — the sequence, the refusals
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

STAGES = [
    ("Task", "classified, with its risk and assurance route", PURPLE),
    ("Cognitive functions", "what must be thought, and by how many independent minds", VERM),
    ("Cohort", "minimum sufficient — no spare actor, no cut expertise", VERM),
    ("Runtime match", "which qualified profile can satisfy each function", BLUE),
    ("Deployment plan", "backend-neutral: topology, embargo, skills, workspaces", GREEN),
    ("Sessions", "projected onto the backend and attached over ACP", BLUE),
]

LADDER = [
    ("RoleContract / RoleBinding", "governance authority — who may decide what",
     "a backend identity starts implying authority nobody granted it", VERM),
    ("Cognitive function", "the epistemic job — Statistician, Adversarial Reviewer",
     "independence stops being measurable, because the profile has nothing to measure", VERM),
    ("Model profile", "the admitted model and its snapshot",
     "requalification silently stops applying", ORANGE),
    ("Runtime profile", "the harness executing the loop",
     "“we used Hermes” starts being offered as a description of the method", BLUE),
    ("Backend identity", "the operational actor in a room",
     "attribution is mistaken for authorisation", BLUE),
]

REFUSALS = [
    "too few independent contributions for a substantial task",
    "a required specialist with no qualified runtime",
    "a backend that cannot enforce round-zero isolation",
    "a skill bundle that cannot be materialised",
    "a verifier independence that cannot be satisfied",
    "a message type or capability the backend does not support",
    "a budget that fits only by dropping cohort or assurance",
]


def main() -> None:
    H = 1030
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 46, "Cognition is chosen first; the runtime is chosen second",
           size=30, weight="700", anchor="start")
    y = c.para(L, 78,
               "The Task Compiler never emits “a Hermes agent”. It emits a cognitive function, a role "
               "contract, capability and context requirements and an independence constraint — and a runtime "
               "selector matches a qualified profile to those afterwards. Selecting the runtime first and then "
               "inventing roles that fit it is how a cohort comes to be shaped by a harness rather than by the "
               "question.",
               tw, size=18, lh=24)

    # ---- pipeline ---------------------------------------------------------
    top = y + 42
    n = len(STAGES)
    gapx = 16
    bw = (tw - gapx * (n - 1)) / n
    for i, (head, body, colour) in enumerate(STAGES):
        x = L + i * (bw + gapx)
        c.cell(x, top, bw, 126, head, body, accent=colour, head_size=18,
               body_size=16, max_head_lines=2, max_body_lines=4)
        if i:
            c.path(f"M {x - gapx + 2} {top + 63} L {x - 3} {top + 63}",
                   stroke=INK, sw=1.8, marker="arrowsm")

    c.text(L, top + 150, "AETHRION decides all six. The last two are projections of the first four, "
           "never inputs to them.", size=16, anchor="start", fill=MUTE)

    # ---- the ladder -------------------------------------------------------
    ly = top + 186
    c.hrule(L, W - L, ly - 16, sw=1.6, stroke=INK)
    c.text(L, ly + 12, "Five levels, and the failure that follows from collapsing each into the next",
           size=20, weight="700", anchor="start")

    ry = ly + 40
    row_h, gapy = 76, 10
    c1, c2 = 300, 330
    c3 = tw - c1 - c2 - 28
    c.text(L + 14, ry - 6, "Level", size=15, weight="700", anchor="start", fill=MUTE)
    c.text(L + c1 + 14, ry - 6, "What it is", size=15, weight="700", anchor="start", fill=MUTE)
    c.text(L + c1 + c2 + 28, ry - 6, "Collapse it and", size=15, weight="700",
           anchor="start", fill=VERM)
    for i, (head, what, breaks, colour) in enumerate(LADDER):
        yy = ry + i * (row_h + gapy)
        c.rect(L, yy, c1, row_h, fill=tint(colour, 0.13), stroke=colour, sw=1.6)
        c.para(L + 14, yy + 30, head, c1 - 28, size=18, weight="600", fill=INK,
               lh=21, max_lines=2)
        c.para(L + c1 + 14, yy + 26, what, c2 - 14, size=17, fill=INK, lh=21, max_lines=3)
        c.para(L + c1 + c2 + 28, yy + 26, breaks, c3, size=17, fill=MUTE, lh=21, max_lines=3)

    # ---- refusals ---------------------------------------------------------
    by = ry + len(LADDER) * (row_h + gapy) + 26
    c.rect(L, by, tw, 132, fill=tint(VERM, 0.07), stroke=VERM, sw=1.8)
    c.text(L + 18, by + 30, "Compilation refuses — it does not warn", size=19,
           weight="700", anchor="start", fill=VERM)
    half = (tw - 56) / 2
    for i, item in enumerate(REFUSALS):
        col, row = divmod(i, 4)
        c.text(L + 22 + col * (half + 12), by + 54 + row * 20, f"·  {item}",
               size=16, anchor="start", fill=INK)

    out = ROOT / "docs" / "figures" / "aethrion_runtime.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_runtime.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
