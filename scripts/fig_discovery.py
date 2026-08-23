#!/usr/bin/env python3
"""Figure 10 — the discovery search graph, and where its numbers stop.

Five-second message
    Search proposes candidates and spends compute. It never decides anything —
    every number it produces is a priority, and the only door into the evidence
    path runs through a frozen evaluator.

Why this figure exists
    The search loop is the part of an AI research system that works best and
    leaves the worst record. Drawn as "agent tries things", it looks like
    progress; drawn as a typed graph with an authority boundary, the two
    questions a reviewer actually asks become visible — *where did this
    candidate come from*, and *why is this number believable*.

Archetype
    A state machine over a funnel, with a hard vertical boundary. The boundary
    is the point of the figure: everything left of it is the producer's, and
    nothing left of it can write a result.

Sources
    docs/architecture/ADR-006_discovery_search_graph.md,
    docs/architecture/ADR-007_frozen_evaluator_and_verified_values.md,
    planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-144, WP-145
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

    c.text(L, 48, "The discovery search graph, and where its numbers stop",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "Candidates are proposed, executed and scored in a typed graph. Two distinctions carry the whole "
               "design: repairing an implementation is a different node state from changing a mechanism, and the "
               "official number comes from an evaluator the producer cannot reach. Everything the graph computes "
               "is a priority for spending compute — never a confidence about the world.",
               tw, size=18, lh=24)

    # ---------------------------------------------------------------- states
    sy = y + 40
    c.text(L, sy, "1 · Node states — why DEBUG is not a comment",
           size=21, weight="700", anchor="start")

    ny = sy + 22
    bw, bh, gap = 244, 104, 26

    # ADR-006 §2 draws a BRANCH, and this panel used to draw a row:
    # DRAFT → DEBUG → IMPROVE → FUSE, four cells with arrows between them. That
    # topology says a candidate passes through every state in order, which is
    # false and inverts what the states are for. The question "did the parent
    # execute?" is what selects DEBUG or IMPROVE — they are alternatives, never
    # successive — and a figure that draws them in a line teaches a reader that
    # debugging precedes improving.
    col_x = [L, L + 300, L + 300 + bw + gap]
    mid = ny + bh + 20

    c.cell(col_x[0], mid, 210, bh, "DRAFT", "a new candidate for the question",
           accent=BLUE, head_size=19, body_size=16, max_body_lines=3)

    qx = col_x[0] + 210 + 30
    c.path(f"M {col_x[0] + 210} {mid + bh / 2} L {qx - 4} {mid + bh / 2}",
           stroke=RULE, sw=1.8, marker="arrowsm")
    c.text(qx + 26, mid + bh / 2 - 8, "did the parent", size=17, weight="700", fill=INK)
    c.text(qx + 26, mid + bh / 2 + 12, "execute?", size=17, weight="700", fill=INK)

    branch_x = col_x[1]
    top_y, bot_y = ny, ny + bh + 40 + bh - 26
    c.path(f"M {qx + 120} {mid + bh / 2} L {branch_x - 34} {mid + bh / 2} "
           f"L {branch_x - 34} {top_y + bh / 2} L {branch_x - 5} {top_y + bh / 2}",
           stroke=ORANGE, sw=1.8, marker="arrowsm")
    c.text(branch_x - 60, top_y + bh / 2 - 8, "no", size=17, weight="700", fill=ORANGE)
    c.path(f"M {qx + 120} {mid + bh / 2} L {branch_x - 34} {mid + bh / 2} "
           f"L {branch_x - 34} {bot_y + bh / 2} L {branch_x - 5} {bot_y + bh / 2}",
           stroke=GREEN, sw=1.8, marker="arrowsm")
    c.text(branch_x - 60, bot_y + bh / 2 - 8, "yes", size=17, weight="700", fill=GREEN)

    c.cell(branch_x, top_y, bw, bh, "DEBUG",
           "the parent did not run. The mechanism is unchanged",
           accent=ORANGE, head_size=19, body_size=16, max_body_lines=3)
    c.cell(branch_x, bot_y, bw, bh, "IMPROVE",
           "the parent ran. The mechanism is changed",
           accent=GREEN, head_size=19, body_size=16, max_body_lines=3)

    # DEBUG's own exhaustion edge, which the row layout had no room to show.
    c.path(f"M {branch_x + bw} {top_y + bh / 2} L {col_x[2] - 6} {top_y + bh / 2}",
           stroke=ORANGE, sw=1.6, dash="5 4", marker="arrowsm")
    c.cell(col_x[2], top_y, bw, bh, "FailedApproach",
           "attempts exhausted — classified IMPLEMENTATION",
           accent=VERM, head_size=19, body_size=16, max_body_lines=3)

    c.path(f"M {branch_x + bw} {bot_y + bh / 2} L {col_x[2] - 6} {bot_y + bh / 2}",
           stroke=PURPLE, sw=1.8, marker="arrowsm")
    c.cell(col_x[2], bot_y, bw, bh, "FUSE",
           "mechanisms from two or more branches, each one named",
           accent=PURPLE, head_size=19, body_size=16, max_body_lines=3)
    c.text(col_x[2] + bw / 2, bot_y - 10, "≥ 2 branches", size=16, fill=PURPLE)

    fy = bot_y + bh + 26
    c.rect(L, fy, tw, 62, fill=tint(VERM, 0.10), stroke=VERM, sw=1.6)
    c.text(L + 16, fy + 26, "The distinction this state buys", size=17, weight="700",
           anchor="start", fill=VERM)
    c.para(L + 16, fy + 46,
           "A candidate that fails to compile has said nothing about the hypothesis. Recorded as \"tried a "
           "different approach\", an implementation defect becomes evidence about a scientific question — and the "
           "record cannot be told apart from one where the idea genuinely failed. ACC-64.",
           tw - 32, size=16, fill=INK, lh=20, max_lines=2)

    # ---------------------------------------------------------------- edges
    ey = fy + 62 + 40
    c.text(L, ey, "2 · Edge classes — what may change an ancestry, and what may not",
           size=21, weight="700", anchor="start")
    ry = ey + 22
    ew = (tw - 2 * gap) / 3
    edges = [
        ("PRIMARY_PARENT", "the ancestry and credit path. Acyclic, and the spine reproduction depends on", INK),
        ("REFERENCE", "reads another branch without changing this node's ancestry", SKY),
        ("FUSION_INPUT", "a real multi-parent inheritance, with each mechanism attributed", PURPLE),
    ]
    for i, (head, body, col) in enumerate(edges):
        bx = L + i * (ew + gap)
        c.cell(bx, ry, ew, 96, head, body, accent=col,
               head_size=18, body_size=16, max_body_lines=3)

    # ---------------------------------------------------------------- funnel
    uy = ry + 96 + 40
    c.text(L, uy, "3 · The fidelity funnel, and the boundary the producer cannot cross",
           size=21, weight="700", anchor="start")

    py = uy + 26
    split = L + 660
    panel_h = 250

    c.rect(L, py, split - L - 22, panel_h, fill=tint(BLUE, 0.06), stroke=BLUE, sw=1.4, dash="6 4")
    c.text(L + 14, py + 24, "PRODUCER ZONE", size=16, weight="700", anchor="start", fill=BLUE)

    c.rect(split + 22, py, W - L - split - 22, panel_h,
           fill=tint(VERM, 0.08), stroke=VERM, sw=1.8)
    c.text(split + 36, py + 24, "EVALUATOR ZONE", size=16, weight="700", anchor="start", fill=VERM)

    # the boundary
    c.path(f"M {split} {py - 12} L {split} {py + panel_h + 12}", stroke=VERM, sw=3.0, marker=None)
    c.text(split, py - 20, "policy and sandbox boundary", size=16, weight="600", fill=VERM)

    tiers = [("SMOKE", "cheap subset · does it run at all", GREEN),
             ("VERIFY", "multiple seeds · variance and protocol conformance", GREEN),
             ("FULL", "full resources · the preregistered official evaluator", ORANGE)]
    ty = py + 44
    tier_w = split - L - 60
    for i, (head, body, col) in enumerate(tiers):
        c.cell(L + 14 + i * 12, ty + i * 66, tier_w - i * 24, 56, head, body, accent=col,
               head_size=18, body_size=16, max_body_lines=2)
        if i:
            c.path(f"M {L + 14 + tier_w / 2} {ty + i * 66 - 10} L {L + 14 + tier_w / 2} {ty + i * 66 - 2}",
                   stroke=RULE, sw=1.8, marker="arrowsm")
    c.text(L + 14, ty + 3 * 66 + 4, "a tier a threshold refused is not promoted on a recommendation",
           size=16, anchor="start", fill=MUTE, weight="600")

    ex, ew2 = split + 36, W - L - split - 50
    c.cell(ex, py + 44, ew2, 56, "frozen evaluator code",
           "digest pinned in the EvaluationContract", accent=VERM,
           head_size=17, body_size=16, max_body_lines=2)
    c.cell(ex, py + 108, ew2, 56, "hidden material",
           "no producer read path exists", accent=VERM,
           head_size=17, body_size=16, max_body_lines=2)
    c.cell(ex, py + 164, ew2, 62, "RawEvaluatorArtifact  →  VerifiedValue",
           "stored immutably before any agent reads it", accent=ORANGE,
           head_size=17, body_size=16, max_body_lines=2)
    c.path(f"M {split + 6} {py + 190} L {ex - 6} {py + 190}", stroke=VERM, sw=2.0, marker="arrow")
    c.text(split + 14, py + 182, "signed candidate commit", size=16, anchor="start", fill=VERM)

    # ---------------------------------------------------------------- stops
    ky = py + panel_h + 40
    c.text(L, ky, "4 · Stopping is a control, and a stop is not an acceptance",
           size=21, weight="700", anchor="start")
    ky2 = ky + 22
    stops = [("cost · rounds · compute", "the campaign governor", PURPLE),
             ("convergence patience", "no frontier improvement", PURPLE),
             ("stagnation", "diversity collapse, repeated failures", PURPLE),
             ("reserved budget", "VERIFY, FULL and G7 are unreachable from exploration", ORANGE)]
    sw_ = (tw - 3 * gap) / 4
    for i, (head, body, col) in enumerate(stops):
        c.cell(L + i * (sw_ + gap), ky2, sw_, 92, head, body, accent=col,
               head_size=17, body_size=16, max_body_lines=3)

    # ---------------------------------------------------------------- rule
    fy2 = ky2 + 92 + 34
    c.rect(L, fy2, tw, 88, fill=tint(VERM, 0.10), stroke=VERM, sw=2.0)
    c.text(L + 18, fy2 + 28, "The forbidden conversion", size=19, weight="700",
           anchor="start", fill=VERM)
    c.para(L + 18, fy2 + 50,
           "A selection score, a normalised rank, a tournament position and a frontier metric are all priorities "
           "for spending compute. Writing any of them into a ClaimVersion, a VerifiedValue, a GateRecord or a "
           "publication is refused by schema and by policy — not discouraged by documentation. "
           "STOPPED_BY_BUDGET satisfies no gate: a campaign that ran out of money has demonstrated nothing.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    ny2 = fy2 + 88 + 26
    c.text(L, ny2, "Status: nothing in this figure is built. WP-144 and WP-145 specify it; there is no "
                   "search graph, no selector, no governor and no campaign runtime.",
           size=16, anchor="start", fill=MUTE, style="italic")

    out = ROOT / "docs" / "figures" / "aethrion_discovery.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_discovery.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
