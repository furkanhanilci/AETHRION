#!/usr/bin/env python3
"""Figure 4 — the target stack: what AIRL-OS builds, and what it stands on.

Five-second message
    Almost every layer of this system is a mature component someone else
    maintains; what AIRL-OS owns is the control layer that decides which
    evidence, having passed which gate, permits which claim to be accepted.

Archetype
    A layered stack crossed with an adoption channel. Not an architecture
    diagram of boxes-and-arrows: the question this figure answers is not *what
    talks to what* but *what do we build versus what do we stand on*, so
    adoption type is a first-class visual channel rather than a caption.

Encoding
    Fill      = adoption type (owned · dependency · standard · pattern · benchmark)
    Stroke    = build status: solid = implemented here, dashed = not built
    Position  = layer

Sources
    docs/architecture/AIRL_OS_COMPONENT_REUSE.md — every component and its type
    docs/architecture/ADR-003 — the security row
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, fit, text_width, tint)

W = 1200
L = 24
OWNED, DEP, STD, PAT, BEN = VERM, BLUE, GREEN, PURPLE, ORANGE

# layer, [(label, type, built)]
LAYERS = [
    ("Human authority", [("Decision Owner signs G8 · G9", OWNED, True)]),
    ("AIRL control layer — G0 to G10", [
        ("Gate semantics · evidence admissibility · independence · claim lifecycle", OWNED, False)]),
    ("Research", [("PaperQA2", DEP, False), ("ASReview", DEP, False),
                  ("GROBID", DEP, False), ("Pub2TEI", DEP, False),
                  ("Crossref · OpenAlex · arXiv", DEP, True)]),
    ("Execution", [("Cedar policy", DEP, False), ("Tool Broker", OWNED, False),
                   ("sandbox backend", DEP, False), ("CaMeL control/data split", PAT, False)]),
    ("Assurance", [("Inspect AI", DEP, False), ("AgentDojo", BEN, False),
                   ("CoE Audit", BEN, False), ("statcheck · GRIM · SPRITE", DEP, False),
                   ("PaperBench pattern", PAT, False)]),
    ("Evidence core", [("AIRL-SEPIO profile via LinkML", STD, False),
                       ("Claim · Evidence · Review", OWNED, False)]),
    ("Provenance", [("Workflow Run RO-Crate", STD, False), ("Croissant 1.1", STD, False),
                    ("SWHID ISO/IEC 18670", STD, False), ("MLflow · OpenTelemetry", DEP, False)]),
    ("Attestation", [("in-toto · DSSE", STD, True), ("Sigstore · Rekor", DEP, False),
                     ("OpenTimestamps", DEP, False)]),
    ("Storage", [("object-lock WORM", DEP, False), ("lakeFS working data", DEP, False)]),
    ("External witness", [("OSF Registries", DEP, False), ("DOI", STD, False),
                          ("nanopublication export", DEP, False)]),
    ("Monitoring", [("Crossref Retraction Watch", DEP, True)]),
]
LEGEND = [(OWNED, "AIRL-owned"), (DEP, "dependency"), (STD, "standard"),
          (PAT, "pattern"), (BEN, "benchmark")]

LABEL_W, ROW_GAP, PAD_X = 208, 9, 10
CHIP_H, MIN_CHIP = 46, 118


def main() -> None:
    rows = []
    for name, chips in LAYERS:
        rows.append((name, chips))
    H = 300 + len(rows) * (CHIP_H + ROW_GAP) + 150
    c = Canvas(W, H)

    c.text(L, 48, "What AIRL-OS builds, and what it stands on", size=30,
           weight="700", anchor="start")
    y = c.para(L, 80,
               "Almost every layer here is a component someone else maintains and tests. What this project owns is "
               "the control layer: which evidence, having passed which gate, permits which claim to be accepted.",
               W - 2 * L, size=18, lh=24)
    y = c.para(L, y + 26,
               "Adoption type is drawn, not captioned, because 'reuse' is not one thing — a dependency, a standard, "
               "a pattern and a benchmark create entirely different obligations.",
               W - 2 * L, size=18, fill=INK, weight="500", lh=24)

    # legend
    ly = y + 34
    x = L
    for colour, label in LEGEND:
        c.rect(x, ly - 13, 24, 17, fill=tint(colour, 0.30), stroke=colour, sw=1.5, rx=3)
        c.text(x + 32, ly, label, size=16, anchor="start")
        x += 32 + text_width(label, 16) + 26
    c.rect(x, ly - 13, 24, 17, fill="#FFFFFF", stroke=INK, sw=2.0, rx=3)
    c.text(x + 32, ly, "implemented here", size=16, anchor="start", weight="600")
    x += 32 + text_width("implemented here", 16, "600") + 26
    c.rect(x, ly - 13, 24, 17, fill="#FFFFFF", stroke=MUTE, sw=1.3, rx=3, dash="5 4")
    c.text(x + 32, ly, "not built", size=16, anchor="start")

    top = ly + 34
    avail = W - L - (L + LABEL_W + 14)
    for index, (name, chips) in enumerate(rows):
        ry = top + index * (CHIP_H + ROW_GAP)
        c.rect(L, ry, LABEL_W, CHIP_H, fill=tint(INK, 0.045), stroke=RULE, sw=1.2)
        lines, sz = fit(name, LABEL_W - 24, 17, "600", max_lines=2)
        ty = ry + CHIP_H / 2 - (len(lines) - 1) * 9 + 6
        for line in lines:
            c.text(L + 12, ty, line, size=sz, weight="600", anchor="start")
            ty += sz + 3

        x0 = L + LABEL_W + 14
        widths = []
        for label, _, _ in chips:
            widths.append(max(MIN_CHIP, text_width(label, 16) + 2 * PAD_X + 8))
        scale = min(1.0, (avail - (len(chips) - 1) * 8) / sum(widths))
        cx = x0
        for (label, kind, built), width in zip(chips, widths):
            width *= scale
            c.cell(cx, ry, width, CHIP_H, label, "", accent=kind,
                   fill=tint(kind, 0.16 if built else 0.07),
                   stroke_override=kind if built else MUTE,
                   sw=2.2 if built else 1.2, dash=None if built else "5 4",
                   head_size=16, head_weight="600" if built else "400",
                   head_fill=INK if built else MUTE, max_head_lines=2)
            cx += width + 8

    # the G10 loop, drawn down the right margin
    first_y = top + 1 * (CHIP_H + ROW_GAP) + CHIP_H / 2
    last_y = top + (len(rows) - 1) * (CHIP_H + ROW_GAP) + CHIP_H / 2
    rx = W - L + 2
    c.path(f"M {W - L - 2} {last_y} L {rx} {last_y} L {rx} {first_y} L {W - L - 2} {first_y}",
           stroke=PURPLE, sw=1.6, dash="6 4", marker="arrowsm")

    ny = top + len(rows) * (CHIP_H + ROW_GAP) + 16
    c.hrule(L, W - L, ny, sw=1.2)
    c.text(L, ny + 30, "Status", size=18, weight="700", anchor="start", fill=VERM)
    c.para(L + 70, ny + 30,
           "Three cells are implemented: bibliographic corroboration, retraction monitoring, and the in-toto/DSSE "
           "envelope in its interim profile. Everything else is a decision, not a component that runs. The control "
           "layer this project owns is the least built part of the stack.",
           W - L - (L + 70), size=17, fill=INK, lh=23)

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "airl_os_stack.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/airl_os_stack.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
