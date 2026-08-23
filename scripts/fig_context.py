#!/usr/bin/env python3
"""Figure 19 — context projection: what an agent is shown, and what is masked.

Five-second message
    An agent never receives the project. It receives a projection assembled for
    one invocation — and the interesting part is not what was left out to save
    tokens, but what was left out because reading it would compromise the work.

Why this figure exists
    Context minimisation is normally an efficiency story, and told that way it
    is uninteresting and slightly suspect: the system hides things from its own
    agents to save money. The architecture's reason is the opposite one.

    A reviewer who can read the producer's dead ends inherits the producer's
    framing, and the review is anchored before it starts. A refuted conclusion
    that survives compaction comes back as current. Both are epistemic failures
    that a larger context window makes *worse*, not better — which is why the
    projection is a control rather than a budget measure, and why it belongs in
    a figure rather than in a sentence about tokens.

Archetype
    A single invocation drawn as a funnel, with two exclusion reasons kept
    visually distinct — cost on one side, independence on the other — and the
    mask lifecycle beneath it.

Sources
    docs/architecture/ADR-005_epistemic_memory_separation.md
    planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-151
    ACC-096, ACC-097, ACC-098, ACC-072, ACC-079
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24


def main() -> None:
    H = 980
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "Context projection — what is shown, and why the rest is not",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "An agent never receives the project. It receives a projection assembled for one invocation. Two "
               "different reasons remove material from it, and collapsing them is the mistake: one is cost, and one "
               "is independence. A larger context window fixes the first and makes the second WORSE.",
               tw, size=18, lh=24)

    # ------------------------------------------------ the two exclusion reasons
    sy = y + 38
    c.text(L, sy, "1 · Two reasons to leave something out, and only one is about tokens",
           size=21, weight="700", anchor="start")
    sy2 = sy + 26
    half = (tw - 24) / 2
    c.cell(L, sy2, half, 150, "Left out because it costs",
           "Superseded drafts, resolved threads, material already summarised. "
           "Removing it is a saving and nothing more: if the window were "
           "infinite, including it would do no harm.",
           accent=MUTE, head_size=19, body_size=16, max_body_lines=5)
    c.cell(L + half + 24, sy2, half, 150, "Left out because reading it would compromise the work",
           "The producer's dead ends, framing and search experience. A reviewer "
           "who reads them inherits them, and the review is anchored before it "
           "starts. An infinite window makes this worse — ACC-072, ACC-079.",
           accent=VERM, head_size=19, body_size=16, max_body_lines=5)

    # ------------------------------------------------------ the projection itself
    py = sy2 + 150 + 36
    c.text(L, py, "2 · What one invocation is assembled from",
           size=21, weight="700", anchor="start")
    py2 = py + 26
    lanes = [
        ("frozen constraints", "the protocol, the analysis plan, the gate", ORANGE),
        ("evidence in scope", "only what this claim rests on", GREEN),
        ("the task itself", "one step, with its acceptance condition", BLUE),
        ("peer deltas", "material differences, never a transcript", PURPLE),
    ]
    lw = (tw - 3 * 14) / 4
    for i, (head, body, col) in enumerate(lanes):
        c.cell(L + i * (lw + 14), py2, lw, 96, head, body, accent=col,
               head_size=17, body_size=16, max_head_lines=2, max_body_lines=3)

    ay = py2 + 96 + 30
    bw_ = 320
    bx = L + (tw - bw_) / 2
    for i in range(4):
        x = L + i * (lw + 14) + lw / 2
        c.path(f"M {x} {py2 + 96 + 6} L {x} {ay - 18} L {bx + bw_ / 2} {ay - 18} "
               f"L {bx + bw_ / 2} {ay - 5}", stroke=RULE, sw=1.4, marker="arrowsm")
    c.rect(bx, ay, bw_, 72, fill=tint(BLUE, 0.12), stroke=BLUE, sw=2.4)
    c.text(bx + bw_ / 2, ay + 30, "ContextProjectionRecord", size=20, weight="700", fill=BLUE)
    c.text(bx + bw_ / 2, ay + 54, "what was shown, and what was masked", size=16, fill=MUTE)

    # ------------------------------------------------------ the mask lifecycle
    my = ay + 72 + 36
    c.text(L, my, "3 · A mask is not a delete", size=21, weight="700", anchor="start")
    my2 = my + 26
    steps = [("refuted", "a conclusion the evidence stopped supporting", VERM),
             ("masked", "removed from the reasoning context", PURPLE),
             ("still queryable", "as history, by anyone asking about history", GREEN),
             ("never returns", "not as current, on any reload — ACC-096", ORANGE)]
    sw_ = (tw - 3 * 14) / 4
    for i, (head, body, col) in enumerate(steps):
        sx = L + i * (sw_ + 14)
        c.cell(sx, my2, sw_, 92, head, body, accent=col,
               head_size=18, body_size=16, max_head_lines=1, max_body_lines=3)
        if i:
            c.path(f"M {sx - 14 + 2} {my2 + 46} L {sx - 5} {my2 + 46}",
                   stroke=RULE, sw=1.6, marker="arrowsm")

    fy = my2 + 92 + 28
    note_h = 112
    c.rect(L, fy, tw, note_h, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, fy + 28, "The two failures this prevents, and they pull opposite ways",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, fy + 50,
           "A refuted conclusion surviving compaction and returning as current — and a frozen constraint dropping "
           "out of context so the step that would violate it proceeds unchallenged. One asks for less to be "
           "carried forward and the other for more, which is why the projection is assembled per invocation rather "
           "than trimmed from a running transcript. ACC-096, ACC-097.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=4)

    ny = fy + note_h + 32
    c.para(L, ny,
           "Status: specified, not built. WP-151 owns it; there is no projection record, no mask and no "
           "memory intervention anywhere in this repository.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_context.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_context.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
