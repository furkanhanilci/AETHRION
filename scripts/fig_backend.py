#!/usr/bin/env python3
"""Figure — the adopted substrate, and the boundary it may never cross.

Five-second message
    AETHRION owns two contracts. Everything adopted sits *underneath* them, and
    the architecture is only correct while removing any of it loses no science.

Archetype
    A stack with two rules drawn as rules rather than as boxes. The contracts are
    horizontal boundary bars, not layers: a layer is a thing you can replace, and
    a boundary is the thing that lets you. Beside the stack, the removal test —
    because a boundary claim is only meaningful if someone has said what happens
    when the thing below it is taken away.

Encoding
    Fill        = ownership: vermilion = AETHRION's, blue = adopted
    Stroke      = build status: solid = exists, dashed = specified and unbuilt
    Bar         = an AETHRION-owned contract, drawn as a boundary
    Right panel = what survives the backend's disappearance, and what must

Why the removal test is on the figure rather than in the caption
    It is the only part a reader can check. Every other statement here is an
    intention; "destroy the rooms and the claims are still there" is a test with
    an outcome, and WP-148-T12 is where it gets run.

Sources
    docs/architecture/ADR-020 — the decision, the five owners, the removal test
    provenance/components.json — CMP-045, CMP-046, CMP-047, CMP-048
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, fit, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24
OWNED, ADOPTED = VERM, BLUE

# label, body, owned?, built?
STACK = [
    ("Scientific authority", "gates · ClaimVersion · EvidenceSpan · VerifiedValue · "
     "DecisionRecord · protocol freeze", True, False),
    ("Task and cohort compilation",
     "cognitive functions, independence and topology — decided before any runtime is named",
     True, False),
    ("__BAR__", "CollaborationBackend — AETHRION says what collaboration must happen", None, None),
    ("Collaboration substrate", "identities · teams · rooms · message transport · presence · "
     "runtime attachment", False, False),
    ("__BAR__", "AgentRuntime — qualify · start_session · send_task · collect_result",
     None, None),
    ("Cognitive runtimes", "Hermes · Codex · Claude Code · Buzz Agent · future ACP-compatible "
     "runtimes — a preference is not an architecture", False, False),
    ("Discipline", "AETHRION scientific and shared skills · the eleven vendored Superpowers "
     "engineering skills", True, True),
    ("Tool and execution boundary",
     "ToolIntent → Tool Broker → PolicyDecision → Execution Broker → sandbox", True, False),
]

KEEPS = [
    "gate state", "claims and evidence spans", "verified values",
    "protocol freeze", "human decisions", "experiment lineage",
    "reproduction records", "publication assertions", "accepted artifacts",
]
LOSES = ["active rooms", "agent presence", "message history projection",
         "operational coordination"]

NEVER = [
    ("A message is not an instruction", "and messaging is not authorisation"),
    ("An identity is not a RoleBinding", "attribution and authority are different questions"),
    ("A room is not the blackboard", "and channel history is not a ContextProjection"),
    ("An approval is not a decision", "a backend cannot move G8 or G9"),
]


def main() -> None:
    rows = len(STACK)
    row_h, bar_h, gap = 74, 40, 12
    body_h = sum(bar_h if s[0] == "__BAR__" else row_h for s in STACK) + gap * (rows - 1)
    # Provisional; the canvas is re-cut once both columns have been laid out.
    H = 250 + body_h + 210
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 46, "The adopted substrate, and the boundary it may never cross",
           size=30, weight="700", anchor="start")
    y = c.para(L, 78,
               "AETHRION owns two contracts and everything adopted sits underneath them. That ordering is the "
               "whole decision: a collaboration substrate carries what the compiler decided, a runtime executes a "
               "cognitive function that was chosen before the runtime was, and neither of them decides anything. "
               "None of it is built — ADR-020 fixes the boundary before any code moves, which is the only point at "
               "which fixing it is cheap.",
               tw, size=18, lh=24)

    top = y + 40
    col = 700
    rx = L + col + 34
    rw = tw - col - 34

    yy = top
    for head, body, owned, built in STACK:
        if head == "__BAR__":
            c.rect(L, yy, col, bar_h, fill=tint(INK, 0.06), stroke=INK, sw=2.0, rx=3)
            c.text(L + 14, yy + bar_h / 2 + 6, "CONTRACT", size=14, weight="700",
                   anchor="start", fill=INK)
            c.text(L + 118, yy + bar_h / 2 + 6, body, size=16, anchor="start", fill=INK)
            yy += bar_h + gap
            continue
        accent = OWNED if owned else ADOPTED
        c.cell(L, yy, col, row_h, head, body, accent=accent,
               dash=None if built else "6 4", max_body_lines=2)
        tag = "AETHRION" if owned else "adopted"
        c.text(L + col - 10, yy + 17, tag, size=13, weight="700", anchor="end",
               fill=accent)
        if head == "Collaboration substrate":
            c.text(L + 12, yy + 17, "Buzz — first candidate", size=13,
                   weight="700", anchor="start", fill=accent)
        yy += row_h + gap

    # ---- the removal test -------------------------------------------------
    # SVG paints in document order, so the panel is measured and drawn *before*
    # its content. Drawing it afterwards filled the box over its own text — an
    # empty green rectangle that every mechanical check passed.
    intro_lines, _ = fit("The test that decides whether the boundary is real rather than "
                         "asserted — WP-148-T12 runs it.", rw - 32, 16, max_lines=3)
    panel_h = (56 + len(intro_lines) * 20 + 30 + 22 + len(LOSES) * 21
               + 14 + 36 + len(KEEPS) * 21 + 10)
    c.rect(rx, top, rw, panel_h, fill=tint(GREEN, 0.05), stroke=GREEN, sw=1.6)
    c.text(rx + 16, top + 30, "Remove the substrate. What goes?", size=19,
           weight="700", anchor="start")
    ry = c.para(rx + 16, top + 56,
                "The test that decides whether the boundary is real rather than "
                "asserted — WP-148-T12 runs it.",
                rw - 32, size=16, lh=20)

    ry += 30
    c.text(rx + 16, ry, "Acceptable to lose", size=16, weight="700",
           anchor="start", fill=MUTE)
    ry += 22
    for item in LOSES:
        c.text(rx + 22, ry, f"·  {item}", size=16, anchor="start", fill=MUTE)
        ry += 21

    ry += 14
    c.hrule(rx + 16, rx + rw - 16, ry - 8, stroke=RULE, sw=1.2)
    c.text(rx + 16, ry + 14, "Must survive — or the integration is wrong",
           size=16, weight="700", anchor="start", fill=VERM)
    ry += 36
    for item in KEEPS:
        c.text(rx + 22, ry, f"·  {item}", size=16, anchor="start", fill=INK)
        ry += 21

    WHERE = [("the boundary", "ADR-020"),
             ("substrate and runtimes", "provenance/components.json"),
             ("mechanisms taken", "provenance/upstreams.json"),
             ("contracts and refusals", "WP-047 · WP-048 · WP-148")]
    wy = top + panel_h + 20
    box_h = 56 + len(WHERE) * 44
    c.rect(rx, wy, rw, box_h, fill=tint(MUTE, 0.05), stroke=MUTE, sw=1.4, dash="5 4")
    c.text(rx + 16, wy + 28, "Where the decision is written down", size=18,
           weight="700", anchor="start")
    for i, (label, where) in enumerate(WHERE):
        yy2 = wy + 56 + i * 44
        c.text(rx + 22, yy2 + 12, label, size=16, anchor="start", fill=MUTE)
        c.text(rx + 22, yy2 + 32, where, size=16, weight="600", anchor="start", fill=INK)

    # ---- what it may never decide ----------------------------------------
    by = max(top + body_h, wy + box_h) + 40
    c.hrule(L, W - L, by - 14, sw=1.6, stroke=INK)
    c.text(L, by + 14, "Four things the substrate may never decide", size=20,
           weight="700", anchor="start")
    cw = (tw - 3 * 14) / 4
    for i, (head, body) in enumerate(NEVER):
        c.cell(L + i * (cw + 14), by + 30, cw, 92, head, body, accent=ORANGE,
               head_size=17, body_size=16, max_head_lines=2, max_body_lines=3)

    ny = by + 30 + 92 + 32
    c.text(L, ny, "Convenience is the attack surface", size=18, weight="700",
           anchor="start", fill=VERM)
    c.para(L, ny + 26,
           "The substrate makes exactly one thing very easy — put every actor in one room — and that single "
           "convenience undoes round-zero independence, the sealed initial position, the sparse default and the "
           "delta-only rule at once. A backend that cannot enforce the compiled topology fails qualification; the "
           "topology is never relaxed to fit a backend.",
           tw, size=16, fill=INK, lh=21)

    bottom = ny + 26 + 4 * 21 + 30
    if bottom > H:
        c.height = H = int(bottom)

    out = ROOT / "docs" / "figures" / "aethrion_backend.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_backend.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
