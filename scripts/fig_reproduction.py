#!/usr/bin/env python3
"""Figure 17 — four zones, and the quiet paths between them that are not sandboxes.

Five-second message
    Reproduction proves nothing unless the reproducer could have failed. Four
    zones separate producing from judging — and the leaks that matter are a
    shared cache, an inherited credential and a warm container layer, none of
    which looks like a boundary being crossed.

Why this figure exists
    The corpus draws one boundary — the vertical line in the discovery figure
    that a producer cannot write across. That is the *authority* boundary and it
    is correct. What it does not show is that authority is separated by four
    distinct zones, and that the interesting failures never touch the authority
    edge at all: they arrive through infrastructure the zones happen to share.

    ACC-113 exists precisely because a sandbox-escape test that only attacks the
    sandbox misses every route that does not require one.

Archetype
    Four bounded zones on one row, with the permitted flow drawn above them and
    the leakage paths drawn beneath — so a reader sees that the leaks run
    UNDERNEATH the boundaries rather than through them.

Sources
    docs/architecture/ADR-007_frozen_evaluator.md
    planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-157
    ACC-19, ACC-20, ACC-113, ACC-114, ACC-116
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

ZONES = [
    ("Producer", "writes the method and the code",
     "may never read hidden test material", BLUE),
    ("Evaluator", "runs the frozen contract, emits raw output",
     "its source and hidden data are unreachable from the producer", ORANGE),
    ("Reproducer", "same package, no agent present",
     "no lineage to the producer's environment", GREEN),
    ("Grader", "judges the reproduction independently",
     "did not produce and did not reproduce", PURPLE),
]

LEAKS = [
    ("a shared cache", "the reproduction is fast because it never really ran"),
    ("an inherited credential", "the reproducer reaches what only the producer should"),
    ("a warm container layer", "the environment carries the producer's state"),
    ("a hosted model snapshot", "silently replaced between the two runs"),
]


def main() -> None:
    H = 1140
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "Four zones, and the leaks that are not boundary crossings",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "A reproduction that could not have failed is not evidence. Separating who produces from who judges "
               "is the visible half of that, and it is the half that gets tested. The half that gets missed is "
               "underneath: infrastructure the zones happen to share, where nothing crosses a boundary because the "
               "boundary was never in the path.",
               tw, size=18, lh=24)

    # ------------------------------------------------------------- the zones
    zy = y + 40
    zw = (tw - 3 * 22) / 4
    zh = 158
    for i, (name, does, forbidden, col) in enumerate(ZONES):
        zx = L + i * (zw + 22)
        c.rect(zx, zy, zw, zh, fill=tint(col, 0.07), stroke=col, sw=2.2)
        c.text(zx + zw / 2, zy + 30, name, size=20, weight="700", fill=col)
        c.para(zx + 14, zy + 52, does, zw - 28, size=16, fill=INK, lh=20, max_lines=2)
        c.hrule(zx + 14, zx + zw - 14, zy + 96, stroke=RULE, sw=1.0)
        c.para(zx + 14, zy + 116, forbidden, zw - 28, size=16, fill=VERM,
               lh=20, max_lines=3)
        if i:
            c.path(f"M {zx - 22 + 3} {zy + zh / 2} L {zx - 5} {zy + zh / 2}",
                   stroke=RULE, sw=1.8, marker="arrowsm")

    c.text(L, zy - 12, "permitted flow — artifacts move right, authority never moves left",
           size=16, weight="700", anchor="start", fill=MUTE)

    # -------------------------------------------------------- the leak paths
    ly = zy + zh + 40
    c.text(L, ly, "The paths ACC-113 plants, none of which is an escape",
           size=21, weight="700", anchor="start")
    ly2 = ly + 26
    lw = (tw - 3 * 18) / 4
    for i, (head, body) in enumerate(LEAKS):
        lx = L + i * (lw + 18)
        c.cell(lx, ly2, lw, 118, head, body, accent=VERM,
               head_size=18, body_size=16, max_head_lines=2, max_body_lines=4)
        # drawn as a dashed path running BENEATH the zone row it defeats
        c.path(f"M {lx + lw / 2} {ly2 - 6} L {lx + lw / 2} {zy + zh + 10}",
               stroke=VERM, sw=1.4, dash="4 4", marker="arrowsm")

    # ---------------------------------------------------- what a status means
    sy = ly2 + 118 + 36
    c.text(L, sy, "What a reproduction status is allowed to claim",
           size=21, weight="700", anchor="start")
    sy2 = sy + 26
    rows = [
        ("EXACT", "bit-identical, and only where the substrate can support it. "
                  "A hosted black-box model cannot.", GREEN),
        ("DISTRIBUTIONAL", "within a declared tolerance, with the interval "
                           "reported rather than the point.", ORANGE),
        ("REPEATABILITY", "the run executed despite failing an independence "
                          "check — classified, with the reason, never discarded.", VERM),
    ]
    rw = (tw - 2 * 20) / 3
    for i, (head, body, col) in enumerate(rows):
        c.cell(L + i * (rw + 20), sy2, rw, 130, head, body, accent=col,
               head_size=18, body_size=16, max_head_lines=1, max_body_lines=5)

    fy = sy2 + 130 + 24
    c.rect(L, fy, tw, 88, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, fy + 28, "The rule that makes the zones worth drawing",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, fy + 50,
           "Reproduced status is refused by environment digest lineage, not by declaration. An agent that produced "
           "a result may not reproduce it, and an environment carrying the producer's cached layers has reproduced "
           "the environment rather than the finding. ACC-20, ACC-114.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    ny = fy + 88 + 24
    c.para(L, ny,
           "Status: specified, not built. WP-157 owns the leakage suite; no zone exists, no lineage is computed, "
           "and no injection has ever been run.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_reproduction.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_reproduction.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
