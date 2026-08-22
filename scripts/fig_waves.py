#!/usr/bin/env python3
"""Figure 6 — the commissioning programme: waves, gate, and what is reachable.

Five-second message
    141 packages run in eleven waves behind one bootstrap package and one
    cutover, and today exactly one of them has produced anything.

Archetype
    A dependency ladder with a progress channel. Not a Gantt chart: the plan has
    no dates, and drawing time it does not have would be an invention.

Derived
    Package counts come from the plan itself, so this figure cannot disagree
    with it.

Sources
    planning/commissioning/00_PROGRAM/02_wave_and_dependency_map.md
    planning/commissioning/README.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, fit, text_width, tint)

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
W, L = 1200, 24

WAVES = [
    ("WB", "Bootstrap", "makes acceptance possible", [0, 0], VERM),
    ("W0", "Programme lock", "scope, ownership, acceptance", [1, 10], BLUE),
    ("W1", "Contract spine", "identity and schema ownership", [11, 20], BLUE),
    ("W2", "Platform backbone", "environment, data, artifacts", [21, 31], BLUE),
    ("W3", "Control and runtime", "workflow, model, sandbox", [32, 60], BLUE),
    ("W4", "Knowledge and evidence", "literature, claims, runs, review", [61, 90], GREEN),
    ("W5", "Human and visibility", "cockpit, decisions, telemetry", [91, 101], GREEN),
    ("W6", "Vertical integration", "slices and acceptance suite", [102, 115], ORANGE),
    ("W7", "Commissioning", "security, resilience, pilot", [116, 119], ORANGE),
    ("W8", "Cutover", "rehearsal, go-live, hypercare", [120, 121], VERM),
    ("W9", "Day-2", "continuous assurance", [122, 130], PURPLE),
    ("WT", "Tooling", "notification, records, timestamping", [131, 140], MUTE),
]


def count(lo: int, hi: int) -> int:
    return len([p for p in PLAN.rglob("WP-*.md")
                if re.match(r"^WP-(\d{3})_", p.name) and lo <= int(p.name[3:6]) <= hi])


def main() -> None:
    rows = [(code, name, note, count(lo, hi), colour) for code, name, note, (lo, hi), colour in WAVES]
    total = sum(r[3] for r in rows)
    H = 300 + len(rows) * 62 + 190
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "The commissioning programme, and how far it has run", size=30,
           weight="700", anchor="start")
    y = c.para(L, 80,
               f"{total} work-package documents in eleven waves, behind one bootstrap package that makes acceptance "
               "possible at all and in front of a single production cutover. Waves are dependency order, not dates: "
               "the plan has none, and drawing time it does not have would be an invention.",
               tw, size=18, lh=24)
    y = c.para(L, y + 26,
               "One package has produced anything. Everything below it is written, sealed and unstarted.",
               tw, size=18, fill=INK, weight="600", lh=24)

    ly = y + 34
    x = L
    for colour, label in ((VERM, "gate or boundary"), (BLUE, "foundation"),
                          (GREEN, "research capability"), (ORANGE, "integration"),
                          (PURPLE, "after go-live")):
        c.rect(x, ly - 13, 24, 17, fill=tint(colour, 0.30), stroke=colour, sw=1.5, rx=3)
        c.text(x + 32, ly, label, size=16, anchor="start")
        x += 32 + text_width(label, 16) + 26

    top = ly + 34
    code_w, name_w = 66, 272
    bar_x = L + code_w + name_w + 24
    bar_max = W - L - bar_x - 150
    widest = max(r[3] for r in rows) or 1

    for i, (code, name, note, n, colour) in enumerate(rows):
        ry = top + i * 62
        started = code == "WB"
        c.rect(L, ry, code_w, 50, fill=tint(colour, 0.16), stroke=colour, sw=1.6)
        c.text(L + code_w / 2, ry + 31, code, size=19, weight="700")
        lines, sz = fit(name, name_w - 16, 18, "600", max_lines=1, min_size=16)
        c.text(L + code_w + 14, ry + 22, lines[0], size=sz, weight="600", anchor="start")
        c.para(L + code_w + 14, ry + 42, note, name_w - 16, size=16, max_lines=1)

        width = max(26, bar_max * n / widest) if n else 26
        c.rect(bar_x, ry + 12, width, 26,
               fill=tint(colour, 0.20 if started else 0.10),
               stroke=colour if started else MUTE, sw=2.0 if started else 1.2,
               dash=None if started else "5 4", rx=4)
        label = f"{n} package" + ("" if n == 1 else "s")
        c.text(bar_x + width + 10, ry + 30, label, size=16, anchor="start",
               fill=INK if started else MUTE, weight="600" if started else "400")
        if started:
            c.text(bar_x + width + 10 + text_width(label, 16, "600") + 12, ry + 30,
                   "TECH_COMPLETE", size=16, weight="700", fill=VERM, anchor="start")

        if i:
            c.path(f"M {L + code_w / 2} {ry - 12} L {L + code_w / 2} {ry - 2}",
                   stroke=RULE, sw=1.6, marker="arrowsm")

    gy = top + len(rows) * 62 + 6
    c.rect(L, gy, tw, 56, fill=tint(VERM, 0.08), stroke=VERM, sw=1.6, dash="5 4")
    c.para(L + 16, gy + 24,
           "Between W7 and W8 sits the only irreversible step: every PRE_GO_LIVE acceptance scenario passes on one "
           "release candidate, and a human signs. A Day-2 rhythm can never be a precondition of the go-live that "
           "precedes it — the defect baseline v1.0.1 was created to fix.",
           tw - 32, size=16, lh=21, max_lines=3)

    ny = gy + 56 + 18
    c.hrule(L, W - L, ny, sw=1.2)
    c.text(L, ny + 30, "Status", size=18, weight="700", anchor="start", fill=VERM)
    c.para(L + 70, ny + 30,
           "No package is ACCEPTED. WP-000 is TECH_COMPLETE: its tooling runs and a specimen manifest verifies, but "
           "issuance is not acceptance. The literature bridge that works today was built before this plan and sits "
           "inside W4's territory without being any of its packages.",
           W - L - (L + 70), size=17, fill=INK, lh=23)

    out = ROOT / "docs" / "figures" / "aethrion_waves.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_waves.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
