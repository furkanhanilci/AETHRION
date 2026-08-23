#!/usr/bin/env python3
"""Figure 13 — the collaboration plane: keep the cohort, prune the conversation.

Five-second message
    Every cost pressure on a multi-agent system argues for fewer agents. This
    one refuses that lever and optimises what the agents say to each other
    instead — because the second independent look is the whole reason the cohort
    exists.

Why this figure exists
    Drawn as "N agents talking", a cohort looks like an expense with a quality
    argument attached. Drawn with the embargo, the edge policies and the
    degradation ladder, it becomes visible that the expensive part and the
    valuable part are different things — which is the entire content of ADR-011
    and ADR-013 and is very hard to carry in a paragraph.

Archetype
    A left-to-right protocol with a sealed boundary in the middle, over a
    degradation ladder that terminates at a floor it cannot cross.

Sources
    docs/architecture/ADR-011_multi_agent_execution_invariant.md,
    docs/architecture/ADR-013_blackboard_and_sparse_communication.md,
    planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-148, WP-149, WP-150, WP-153
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24


def main() -> None:
    H = 1420
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "The collaboration plane: keep the cohort, prune the conversation",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "Substantial scientific execution needs at least two epistemically independent contributions, and "
               "that is an epistemic requirement rather than a capability one — a cost argument cannot answer it. "
               "So the cohort is fixed and the conversation is optimised. Everything below is a way of spending "
               "fewer tokens without losing the second look.",
               tw, size=18, lh=24)

    # ------------------------------------------------- 1 · independence profile
    sy = y + 38
    c.text(L, sy, "1 · Independence is a profile, not a count",
           size=21, weight="700", anchor="start")
    ny = sy + 22
    dims = [("cognitive function", "methodologist · statistician · skeptic", BLUE),
            ("evidence exposure", "same evidence, or different subsets", BLUE),
            ("peer visibility", "did it see the other first", ORANGE),
            ("model profile", "necessary, not sufficient", MUTE),
            ("prompt perspective", "different framing, or the same twice", MUTE)]
    dw = (tw - 4 * 14) / 5
    for i, (head, body, col) in enumerate(dims):
        c.cell(L + i * (dw + 14), ny, dw, 104, head, body, accent=col,
               head_size=17, body_size=16, max_head_lines=2, max_body_lines=3)
    fy = ny + 104 + 16
    c.rect(L, fy, tw, 56, fill=tint(VERM, 0.10), stroke=VERM, sw=1.6)
    c.para(L + 16, fy + 24,
           "Five instances of one model on one context are ONE contribution. They will agree, and the agreement "
           "carries no information — which is why a cohort of identical profiles is refused and a cohort of three "
           "differentiated ones passes. ACC-081.",
           tw - 32, size=17, fill=INK, lh=21, max_lines=2)

    # ------------------------------------------------- 2 · independent-first
    ey = fy + 56 + 36
    c.text(L, ey, "2 · Independent-first — the order is the mechanism",
           size=21, weight="700", anchor="start")
    py = ey + 26
    bw, bh, gap = 210, 96, 22
    steps = [("round 0", "peer output hidden", BLUE),
             ("position", "each actor writes its own", BLUE),
             ("SEAL", "digests fixed, and checkable later", ORANGE),
             ("deltas", "only material differences exposed", GREEN),
             ("converge", "no unresolved material challenge", PURPLE)]
    for i, (head, body, col) in enumerate(steps):
        bx = L + i * (bw + gap)
        c.cell(bx, py, bw, bh, head, body, accent=col,
               head_size=18, body_size=16, max_body_lines=3)
        if i:
            c.path(f"M {bx - gap + 3} {py + bh / 2} L {bx - 5} {py + bh / 2}",
                   stroke=RULE, sw=1.8, marker="arrowsm")
    c.path(f"M {L + 2 * (bw + gap) - 11} {py - 12} L {L + 2 * (bw + gap) - 11} {py + bh + 12}",
           stroke=VERM, sw=3.0, marker=None)
    c.text(L + 2 * (bw + gap) - 11, py - 20, "embargo lifts here", size=16, weight="700", fill=VERM)

    gy = py + bh + 16
    c.para(L, gy,
           "Anchoring is an effect, not a preference: an actor shown a confident prior answer converges on it, and "
           "the record afterwards shows two agreeing actors — indistinguishable from two that independently agreed. "
           "The seal is the only thing that tells them apart later. A majority cannot close a skeptic's unanswered "
           "objection — ACC-082, ACC-090.",
           tw, size=17, fill=MUTE, lh=22, max_lines=3)

    # ------------------------------------------------- 3 · what crosses an edge
    my = gy + 3 * 22 + 30
    c.text(L, my, "3 · What crosses an edge, and what never does",
           size=21, weight="700", anchor="start")
    my2 = my + 24
    half = (tw - 26) / 2
    c.cell(L, my2, half, 148, "Typed delta + pointer",
           "Ten message types, because a CHALLENGE can be tracked to resolution and a paragraph cannot. "
           "The message carries the change and a digest; the content goes to the artifact store. "
           "Delete the blackboard and no canonical science is lost — ACC-084, ACC-085.",
           accent=GREEN, head_size=19, body_size=16, max_body_lines=6)
    c.cell(L + half + 26, my2, half, 148, "Never: a transcript",
           "A full reasoning transcript passed between agents is a channel through which one agent's error "
           "becomes another's premise. The token saving is the obvious reason to refuse it; that is the "
           "other one.",
           accent=VERM, head_size=19, body_size=16, max_body_lines=6)

    # ------------------------------------------------- 4 · degradation ladder
    ly = my2 + 148 + 36
    c.text(L, ly, "4 · What budget pressure degrades — and the floor it cannot cross",
           size=21, weight="700", anchor="start")
    ly2 = ly + 26
    rungs = [("structured full", GREEN), ("compressed", GREEN),
             ("pointer only", ORANGE), ("silence unless material", ORANGE)]
    rw = (tw - 3 * 16) / 4
    for i, (head, col) in enumerate(rungs):
        bx = L + i * (rw + 16)
        c.cell(bx, ly2, rw, 58, head, "", accent=col, head_size=18, max_head_lines=2)
        if i:
            c.path(f"M {bx - 13} {ly2 + 29} L {bx - 4} {ly2 + 29}",
                   stroke=RULE, sw=1.8, marker="arrowsm")

    fy2 = ly2 + 58 + 14
    c.rect(L, fy2, tw, 92, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, fy2 + 28, "The floor: what budget may never reach",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, fy2 + 52,
           "The cohort. The assurance route. Any non-waivable control. A BLOCKER or a safety message at any "
           "utility threshold. A task that cannot afford its required assurance is BLOCKED_BUDGET or asks for a "
           "scope reduction — it does not proceed more cheaply. ACC-088, ACC-099, ACC-101.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    # ------------------------------------------------- 5 · anchored optimisation
    ay = fy2 + 92 + 30
    c.text(L, ay, "5 · The optimisation is anchored, or it is not an optimisation",
           size=21, weight="700", anchor="start")
    c.para(L, ay + 24,
           "Accepted only when quality stays inside a declared tolerance and coordination cost falls meaningfully. "
           "A regression rolls the topology back automatically. The baseline is the naive fully-connected cohort — "
           "not a single agent, because comparing to one agent measures the cost of having a cohort at all, which "
           "is a decision already taken on other grounds. ACC-086, ACC-087.",
           tw, size=17, fill=INK, lh=22, max_lines=4)

    ny2 = ay + 24 + 4 * 22 + 24
    c.para(L, ny2,
           "Status: none of this is built. WP-148 to WP-150 and WP-153 specify it; there is no cohort record, no "
           "blackboard, no topology compiler, no governor and no baseline harness to measure any of it against.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_collaboration.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_collaboration.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
