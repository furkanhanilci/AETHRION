#!/usr/bin/env python3
"""Figure 2 — role authority and the separation constraints that replace headcount.

Five-second message
    Fourteen durable functions sorted by the authority they hold and what each
    can block — and because a role is a function rather than a person, one
    operator may hold several of them, with legality decided by separation
    constraints instead of headcount.

Archetype
    Authority ladder (panel a) plus a worked constraint resolution (panel b).
    Deliberately not an org chart: an org chart implies people, which is the
    misreading this figure exists to prevent.

Sources
    docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md A1-A8
    docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md §3.1
    docs/architecture/AIRL_OS_ARCHITECTURE.md §6.1
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, PURPLE, RULE, VERM, Canvas, tint)

W, H = 1200, 1166
L = 24

# name, actors (X mechanical / M model / H human), blocks, note
TIERS = [
    ("Human authority — the actor may never be a model", VERM, [
        ("Project Decision Owner", "H", "G8 · G9", "signs; decides what the lab believes"),
        ("Safety / Data Owner", "H", "all gates", "owns the data class"),
        ("Research Integrity Officer", "H+X", "all gates", "mechanical triggers, human judgement"),
        ("Assurance Lead", "H+X", "G6 · G7", "assigns reviewers; not a model"),
    ]),
    ("Ownership — the human decides, the model drafts", "#B8860B", [
        ("Scientific Owner", "H+M", "G2", "writes the decision question"),
        ("Statistical Methods Owner", "H+M", "G2 · G4 · G6", "locks the analysis plan"),
        ("Evidence Lead", "H+M", "G3", "freezes the literature set"),
        ("Engineering Owner", "M+H", "G4 · G5", "produces code; human approves"),
    ]),
    ("Production — the model produces, the human approves", BLUE, [
        ("Research Software Engineer", "M+H", "G7", "reproducibility · badges"),
        ("Data Steward", "M+H", "G1 · G9", "datasets · identifiers"),
        ("Red Team Lead", "M+H", "G4", "pre-mortem · control injection"),
    ]),
    ("Mechanical-first — the check precedes the judgement", GREEN, [
        ("Scientific Editor", "X+M", "G9", "scope conformance is mechanical"),
        ("Knowledge Steward", "X+M", "G0", "contradiction sweeps"),
        ("Metascience Lead", "H+X", "nothing", "measures the laboratory itself"),
    ]),
]

ACTOR_COLOUR = {"X": GREEN, "M": BLUE, "H": VERM}
ACTOR_NAME = {"X": "mechanical", "M": "model", "H": "human"}

CARD_W, CARD_H, CARD_GAP = 277, 96, 10


def actor_strip(c: Canvas, x: float, y: float, spec: str) -> None:
    """Three slots, filled when that actor class participates in the role."""
    present = set(spec.split("+"))
    for i, key in enumerate(("X", "M", "H")):
        cx = x + i * 26
        colour = ACTOR_COLOUR[key]
        if key in present:
            c.rect(cx, y, 21, 18, fill=tint(colour, 0.55), stroke=colour, sw=1.4, rx=3)
            c.text(cx + 10.5, y + 13.5, key, size=16, weight="700", fill=INK)
        else:
            c.rect(cx, y, 21, 18, fill="#FFFFFF", stroke=RULE, sw=1.0, rx=3)


def main() -> None:
    c = Canvas(W, H)
    c.text(L, 46, "Who is accountable, and why that is not a headcount",
           size=30, weight="700", anchor="start")
    c.text(L, 76, "Fourteen durable functions, ordered by the authority they hold. A role is a function, not a person:",
           size=18, fill=MUTE, anchor="start")
    c.text(L, 99, "one operator may hold several, and which combinations stay independent is decided by constraint rather than by counting people.",
           size=17, fill=MUTE, anchor="start")

    # legend for the actor strip
    lx = L
    c.text(lx, 132, "Actor composition", size=16, weight="600", anchor="start", fill=INK)
    lx += 150
    for key in ("X", "M", "H"):
        colour = ACTOR_COLOUR[key]
        c.rect(lx, 119, 21, 18, fill=tint(colour, 0.55), stroke=colour, sw=1.4, rx=3)
        c.text(lx + 10.5, 132.5, key, size=16, weight="700")
        c.text(lx + 28, 132, ACTOR_NAME[key], size=16, anchor="start", fill=MUTE)
        lx += 28 + len(ACTOR_NAME[key]) * 8.4 + 26
    c.text(lx, 132, "an empty slot means that actor class does not participate", size=16,
           anchor="start", fill=MUTE)

    c.text(L, 172, "(a)  Authority tiers", size=20, weight="700", anchor="start")

    y = 190
    for title, colour, roles in TIERS:
        c.rect(L, y, W - 2 * L, 30, fill=tint(colour, 0.14), stroke=colour, sw=1.4, rx=4)
        c.text(L + 12, y + 21, title, size=17, weight="600", anchor="start", fill=INK)
        y += 38
        for i, (name, actors, blocks, note) in enumerate(roles):
            x = L + i * (CARD_W + CARD_GAP)
            never_blocks = blocks == "nothing"
            c.rect(x, y, CARD_W, CARD_H, fill="#FFFFFF", stroke=colour, sw=1.6, rx=5)
            c.text(x + 14, y + 26, name, size=17, weight="600", anchor="start")
            actor_strip(c, x + 14, y + 38, actors)
            tag_colour = MUTE if never_blocks else colour
            c.text(x + 96, y + 52, ("blocks " + blocks) if not never_blocks else "blocks nothing",
                   size=16, weight="600", anchor="start", fill=tag_colour)
            c.text(x + 14, y + 80, note, size=16, anchor="start", fill=MUTE)
        y += CARD_H + 20

    c.text(L, y - 6,
           "The Metascience Lead blocks nothing by design: a function that both measures the laboratory and can veto its work",
           size=16, anchor="start", fill=MUTE)
    c.text(L, y + 14, "acquires an interest in the numbers.", size=16, anchor="start", fill=MUTE)

    # ---- panel b ----------------------------------------------------------
    y += 34
    c.hrule(L, W - L, y, stroke=RULE, sw=1.2)
    y += 28
    c.text(L, y, "(b)  How one operator legally holds several roles", size=20,
           weight="700", anchor="start")
    y += 22

    bx, bw = L, 560
    c.rect(bx, y, bw, 186, fill=tint(INK, 0.03), stroke=RULE, sw=1.2)
    c.text(bx + 16, y + 28, "RoleBinding", size=18, weight="700", anchor="start", fill=INK)
    rows = [
        ("role_id", "statistical_methods_owner", INK),
        ("actor.human", "one operator", INK),
        ("must_be_independent_from", "experiment_analyst", PURPLE),
        ("can_combine_with", "scientific_owner", GREEN),
        ("cannot_combine_with", "final_independent_verifier", VERM),
    ]
    ry = y + 56
    for key, val, colour in rows:
        c.text(bx + 16, ry, key + ":", size=16, anchor="start", fill=MUTE,
               family="'DejaVu Sans Mono', monospace")
        c.text(bx + 268, ry, val, size=16, anchor="start", fill=colour, weight="600",
               family="'DejaVu Sans Mono', monospace")
        ry += 26

    ax = bx + bw + 34
    c.node(ax, y + 6, 250, 62, "Constraint engine",
           ["admits or refuses each binding"], accent=INK, sw=1.6)
    c.path(f"M {bx + bw + 8} {y + 37} L {ax - 6} {y + 37}", stroke=INK, sw=1.8)

    ok_y, no_y = y + 92, y + 148
    c.node(ax, ok_y, 250, 46, "ADMITTED", ["also holds scientific_owner"],
           accent=GREEN, sw=1.8)
    c.node(ax, no_y, 250, 46, "REFUSED", ["cannot also verify its own work"],
           accent=VERM, sw=1.8)
    c.path(f"M {ax + 125} {y + 68} L {ax + 125} {ok_y - 4}", stroke=GREEN, sw=1.8, marker="arrowsm")
    c.path(f"M {ax + 125} {ok_y + 46} L {ax + 125} {no_y - 4}", stroke=VERM, sw=1.8, marker="arrowsm")

    nx = ax + 268
    for i, line in enumerate((
            "Independence stops being",
            "a question of how many",
            "people exist, and becomes",
            "one of which combinations",
            "remain admissible.")):
        c.text(nx, y + 30 + i * 21, line, size=16, anchor="start", fill=MUTE)
    c.text(nx, y + 152, "Open decision — C2", size=17, weight="700", anchor="start", fill=VERM)
    for i, line in enumerate((
            "Which combinations count as",
            "independent in a one-person",
            "operation is not yet decided.")):
        c.text(nx, y + 174 + i * 21, line, size=16, anchor="start", fill=INK)

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "airl_os_roles.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/airl_os_roles.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
