#!/usr/bin/env python3
"""Figure 18 — the Task Compiler: what a task becomes before an agent runs.

Five-second message
    Nothing about the execution is chosen by the agent. The cohort, the
    topology, the context, the budget and the assurance route are all compiled
    from the task's own properties, and the count of agents is an output rather
    than a setting.

Why this figure exists
    The compiler is named in `ADR-011`, `ADR-013` and `WP-047`, and it is the
    single component that decides most of what the collaboration plane does — yet
    the corpus draws it nowhere. That is a real gap rather than a missing
    picture: read as prose, "the Task Compiler emits a cohort" sounds like a
    configuration step, and the property that matters is the opposite one.
    **Agent count is derived.** A task that needs three independent cognitive
    functions gets three; a task that needs one gets one; and neither is a knob
    a deadline can turn.

    Drawn as a fan-in of task properties and a fan-out of contracts, with the
    refusal path beside it, the derivation becomes the shape of the figure.

Archetype
    Fan-in to a single compilation step, fan-out to typed contracts, with a
    refusal branch that leaves the compiler rather than passing through it.

Sources
    docs/architecture/ADR-011_multi_agent_execution_invariant.md §6
    docs/architecture/ADR-013_blackboard_and_sparse_communication.md §4
    planning/commissioning/05_MODEL_AGENT_TOOL/WP-047, WP-042
    planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-148, WP-153, ACC-081
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

# what the compiler reads — ADR-013 §4 names these
INPUTS = [
    ("task class", "what kind of work this is"),
    ("scientific phase", "which gate it sits before"),
    ("roles required", "the governance functions in play"),
    ("evidence dependencies", "what it must read to proceed"),
    ("independence requirement", "the assurance class it inherits"),
    ("budget", "what is affordable, and what is reserved"),
]

# what it emits — ADR-011 §6
OUTPUTS = [
    ("AgentCohort", "the actors, and why each is there", BLUE),
    ("CognitiveDiversityProfile", "independence across five dimensions", BLUE),
    ("CommunicationTopology", "which edge may carry which message type", PURPLE),
    ("ContextProjection", "what each actor is shown, and what is masked", PURPLE),
    ("ResearchBudgetContract", "spend, and the reserve exploration cannot reach", ORANGE),
    ("AssuranceRoute", "V0–V3 per claim, chosen before the work starts", GREEN),
]


def main() -> None:
    H = 1130
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "The Task Compiler — what a task becomes before an agent runs",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "The number of agents is an OUTPUT, not a setting. A task that needs three independent cognitive "
               "functions compiles to three; one that needs one compiles to one; and neither is a knob a deadline "
               "can turn. Everything below is derived from the task's own properties before any agent is invoked, "
               "which is what makes “was this reviewed independently?” a query rather than an assertion.",
               tw, size=18, lh=24)

    # ---------------------------------------------------------------- fan-in
    sy = y + 38
    c.text(L, sy, "1 · What it reads", size=21, weight="700", anchor="start")
    iy = sy + 24
    iw, ih = 258, 62
    for i, (head, body) in enumerate(INPUTS):
        row, col = divmod(i, 3)
        c.cell(L + col * (iw + 14), iy + row * (ih + 12), iw, ih, head, body,
               accent=MUTE, head_size=17, body_size=16,
               max_head_lines=1, max_body_lines=2)

    in_bottom = iy + 2 * (ih + 12) - 12

    # -------------------------------------------------------- the compilation
    cy = in_bottom + 46
    cw_ = 420
    cx = L + (tw - cw_) / 2
    c.rect(cx, cy, cw_, 78, fill=tint(BLUE, 0.12), stroke=BLUE, sw=2.4)
    c.text(cx + cw_ / 2, cy + 32, "Task Compiler", size=22, weight="700", fill=BLUE)
    c.text(cx + cw_ / 2, cy + 58, "WP-047 · derives, never asks", size=16, fill=MUTE)

    for i in range(3):
        x = L + i * (iw + 14) + iw / 2
        c.path(f"M {x} {in_bottom + 2} L {x} {in_bottom + 20}",
               stroke=RULE, sw=1.4, marker="arrowsm")
    c.path(f"M {cx + cw_ / 2} {cy - 22} L {cx + cw_ / 2} {cy - 5}",
           stroke=RULE, sw=1.6, marker="arrowsm")

    # ------------------------------------------------------------- fan-out
    oy = cy + 78 + 38
    c.text(L, oy, "2 · The contracts it emits — every one binding, none optional",
           size=21, weight="700", anchor="start")
    oy2 = oy + 30
    ow, oh = 372, 74
    for i, (head, body, col) in enumerate(OUTPUTS):
        row, colm = divmod(i, 3)
        ox = L + colm * (ow + 12)
        c.cell(ox, oy2 + row * (oh + 12), ow, oh, head, body, accent=col,
               head_size=17, body_size=16, max_head_lines=1, max_body_lines=2)
    out_bottom = oy2 + 2 * (oh + 12) - 12

    c.path(f"M {cx + cw_ / 2} {cy + 78 + 2} L {cx + cw_ / 2} {cy + 78 + 20}",
           stroke=RULE, sw=1.6, marker="arrowsm")
    for i in range(3):
        x = L + i * (ow + 12) + ow / 2
        c.path(f"M {x} {oy2 - 22} L {x} {oy2 - 5}", stroke=RULE, sw=1.4, marker="arrowsm")

    # ------------------------------------------------------- the refusal path
    ry = out_bottom + 38
    c.text(L, ry, "3 · The output that is not a cohort", size=21, weight="700",
           anchor="start")
    ry2 = ry + 24
    half = (tw - 22) / 2
    c.cell(L, ry2, half, 118, "Compilation refuses",
           "A task needing independent review that cannot be given it does not "
           "compile to one agent with a note. It compiles to nothing, and the "
           "refusal names what was missing — ACC-081.",
           accent=VERM, head_size=19, body_size=16, max_body_lines=5)
    c.cell(L + half + 22, ry2, half, 118, "BLOCKED_BUDGET",
           "A task that cannot afford its required assurance is blocked or asks "
           "for a scope reduction. It does not proceed more cheaply — ACC-101.",
           accent=VERM, head_size=19, body_size=16, max_body_lines=5)

    fy = ry2 + 118 + 24
    note_h = 106
    c.rect(L, fy, tw, note_h, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, fy + 28, "Why this is a compiler and not a configuration file",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, fy + 50,
           "Every cost pressure a multi-agent system experiences argues for fewer agents, and a setting can be "
           "turned down. A derivation cannot: the cohort follows from the task, so reducing it means changing what "
           "the task claims to be — which is a scope decision, made in the open, by a human.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    ny = fy + note_h + 28
    c.para(L, ny,
           "Status: specified, not built. WP-047 owns the compiler and emits no cohort today; WP-042 records that it "
           "must stop emitting a bare skill list. Nothing in this figure runs.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_compiler.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_compiler.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
