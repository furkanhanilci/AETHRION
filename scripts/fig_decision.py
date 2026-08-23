#!/usr/bin/env python3
"""Figure 16 — a human decision, and the order that makes it a judgement.

Five-second message
    The human writes their assessment first, and it is sealed before the
    recommendation is reachable. Everything after that is measurable: the
    distance between what they thought and what they decided.

Why this figure exists
    `ADR-016` had no figure, and its content is an ORDERING — which is the one
    thing prose is worst at making binding. "The human decides" is already drawn
    at G8 in the lifecycle; what is not drawn anywhere is that a decision taken
    after reading a confident recommendation and a decision taken before it are
    different events that produce identical records.

    Anchoring is an effect, not a preference. Shown a recommendation first, a
    decider converges on it, and the DecisionRecord afterwards is
    indistinguishable from one reached independently. The seal is the only thing
    that can tell them apart later — the same mechanism the cohort uses in
    ADR-011, applied to the one actor the whole system defers to.

Archetype
    A time-ordered lane with a hard seal boundary, and beneath it the two
    outcomes that are NOT a decision. Time runs left to right and the barrier is
    vertical, because the claim is about order.

Sources
    docs/architecture/ADR-016_human_preliminary_judgment.md
    planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-156, ACC-110–112
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
    H = 1000
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "A human decision, and the order that makes it a judgement",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "A DecisionRecord signed after reading a confident recommendation and one signed before it look "
               "identical. That is the whole problem: the record cannot carry the difference, so the PROCEDURE has "
               "to. The preliminary assessment is written first and sealed, and only then does the recommendation "
               "become reachable through any interface.",
               tw, size=18, lh=24)

    # ---------------------------------------------------- the ordered lane
    sy = y + 38
    c.text(L, sy, "1 · The order, and the boundary that enforces it",
           size=21, weight="700", anchor="start")
    ly = sy + 26
    bw, bh, gap = 210, 118, 24
    steps = [
        ("packet", "evidence, dissent and open findings — no recommendation in it", ORANGE),
        ("preliminary", "the human's own reading, written before any advice", VERM),
        ("SEAL", "digest fixed; checkable long after the fact", ORANGE),
        ("recommendation", "the AI may now advise, and only advise", BLUE),
        ("decision", "signed, with the delta from the preliminary recorded", VERM),
    ]
    for i, (head, body, col) in enumerate(steps):
        bx = L + i * (bw + gap)
        c.cell(bx, ly, bw, bh, head, body, accent=col,
               head_size=18, body_size=16, max_body_lines=4)
        if i:
            c.path(f"M {bx - gap + 3} {ly + bh / 2} L {bx - 5} {ly + bh / 2}",
                   stroke=RULE, sw=1.8, marker="arrowsm")

    barrier_x = L + 3 * (bw + gap) - gap / 2
    c.path(f"M {barrier_x} {ly - 14} L {barrier_x} {ly + bh + 6}",
           stroke=VERM, sw=3.0, marker=None)
    c.text(barrier_x, ly - 22, "nothing to the right is reachable until the seal exists",
           size=16, weight="700", fill=VERM)

    gy = ly + bh + 38
    c.para(L, gy,
           "The DecisionDelta is the point of sealing. It is the measured distance between what the human thought "
           "and what the human signed — a quantity that does not exist unless the first was recorded before the "
           "second was influenced. A delta of zero on every decision is not agreement; it is the signature of a "
           "ratification process. ACC-110, ACC-112.",
           tw, size=17, fill=MUTE, lh=22, max_lines=3)

    # ------------------------------------------- what is not a decision
    ny = gy + 3 * 22 + 32
    c.text(L, ny, "2 · Three things that are not decisions",
           size=21, weight="700", anchor="start")
    ny2 = ny + 26
    cards = [
        ("a timeout", "escalates, through every interface. It never becomes an "
                      "approval, and no queue length changes that", VERM),
        ("INSUFFICIENT_BASIS", "a first-class outcome, not a failure to decide. "
                               "The packet was not enough, and saying so is the "
                               "correct answer", ORANGE),
        ("an attention score", "may order a queue and may not decide anything. "
                               "authority=false is a field, not a convention", MUTE),
    ]
    cw = (tw - 2 * 20) / 3
    for i, (head, body, col) in enumerate(cards):
        c.cell(L + i * (cw + 20), ny2, cw, 132, head, body, accent=col,
               head_size=18, body_size=16, max_head_lines=2, max_body_lines=5)

    # -------------------------------------------------- friction symmetry
    fy = ny2 + 132 + 32
    c.text(L, fy, "3 · Friction symmetry — the asymmetry that quietly decides",
           size=21, weight="700", anchor="start")
    fy2 = fy + 26
    half = (tw - 26) / 2
    c.cell(L, fy2, half, 140, "Accepting a recommendation",
           "One click, no justification required, no record of what was weighed. "
           "This is the path of least resistance and it is the one the system "
           "makes cheapest.",
           accent=MUTE, head_size=19, body_size=16, max_body_lines=5)
    c.cell(L + half + 26, fy2, half, 140, "Rejecting one",
           "A written reason, a named alternative, a re-review. Every step is "
           "defensible on its own, and together they price disagreement.",
           accent=MUTE, head_size=19, body_size=16, max_body_lines=5)

    by = fy2 + 140 + 20
    req_h = 104
    c.rect(L, by, tw, req_h, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, by + 28, "The requirement", size=19, weight="700",
           anchor="start", fill=VERM)
    c.para(L + 18, by + 50,
           "Accepting and rejecting must cost the same. A system where agreement is one click and disagreement is "
           "a form has not left the decision to the human — it has left them the option of disagreeing, which is a "
           "different thing, and the difference does not appear anywhere in the record. ACC-112.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    ny3 = by + req_h + 30
    c.para(L, ny3,
           "Status: specified, not built. WP-156 owns it; there is no HumanPreliminaryAssessment record, no "
           "DecisionDelta and no measurement of friction anywhere in this repository.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_decision.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_decision.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
