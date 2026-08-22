#!/usr/bin/env python3
"""Figure 2 — role authority, and the constraints that replace headcount.

Five-second message
    Fourteen durable functions ordered by the authority they hold and what each
    can block — and because a role is a function rather than a person, one
    operator may hold several, with legality decided by separation constraints
    instead of by counting people.

Archetype
    An authority ladder (panel a) plus a worked constraint resolution (panel b).
    Deliberately not an org chart: an org chart implies people, which is exactly
    the misreading this figure exists to prevent.

Sources
    docs/architecture/AETHRION_ROLES.md §2, §3, §5
    docs/architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md §3.1
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MONO, MUTE, PURPLE, RULE, VERM,
                        Canvas, fit, text_width, tint)

W = 1200
L = 24
AMBER = "#B8860B"

TIERS = [
    ("Tier I — human authority: the actor may never be a model", VERM, [
        ("Project Decision Owner", "H", "G8 · G9", "signs; decides what the lab believes"),
        ("Safety / Data Owner", "H", "all gates", "owns the data class"),
        ("Research Integrity Officer", "H+X", "all gates", "mechanical flags, human judgement"),
        ("Assurance Lead", "H+X", "G6 · G7", "assigns reviewers; not a model"),
    ]),
    ("Tier II — ownership: the human decides, the model drafts", AMBER, [
        ("Scientific Owner", "H+M", "G2", "writes the decision question"),
        ("Statistical Methods Owner", "H+M", "G2 · G4 · G6", "locks the analysis plan"),
        ("Evidence Lead", "H+M", "G3", "freezes the literature set"),
        ("Engineering Owner", "M+H", "G4 · G5", "produces code; human approves"),
    ]),
    ("Tier III — production: the model produces, the human approves", BLUE, [
        ("Research Software Engineer", "M+H", "G7", "reproducibility · badges"),
        ("Data Steward", "M+H", "G1 · G9", "datasets · identifiers"),
        ("Red Team Lead", "M+H", "G4", "pre-mortem · control injection"),
    ]),
    ("Tier IV — mechanical-first: the check precedes the judgement", GREEN, [
        ("Scientific Editor", "X+M", "G9", "scope conformance is mechanical"),
        ("Knowledge Steward", "X+M", "G0", "contradiction sweeps"),
        ("Metascience Lead", "H+X", "nothing", "measures the laboratory itself"),
    ]),
]
ACTOR_COLOUR = {"X": GREEN, "M": BLUE, "H": VERM}
ACTOR_NAME = {"X": "mechanical", "M": "model", "H": "human"}
CARD_W, CARD_H, CARD_GAP = 277, 116, 10
H = 1268


def actor_strip(c: Canvas, x: float, y: float, spec: str) -> float:
    present = set(spec.split("+"))
    for i, key in enumerate(("X", "M", "H")):
        cx = x + i * 26
        colour = ACTOR_COLOUR[key]
        if key in present:
            c.rect(cx, y, 21, 18, fill=tint(colour, 0.55), stroke=colour, sw=1.4, rx=3)
            c.text(cx + 10.5, y + 13.5, key, size=16, weight="700")
        else:
            c.rect(cx, y, 21, 18, fill="#FFFFFF", stroke=RULE, sw=1.0, rx=3)
    return x + 3 * 26


def main() -> None:
    c = Canvas(W, H)
    tw = W - 2 * L
    c.text(L, 48, "Who is accountable, and why that is not a headcount",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "Fourteen durable functions, ordered by the authority they hold. A role is a function rather than a "
               "person: one operator may hold several of them, and which combinations remain independent is decided "
               "by constraint rather than by counting people.",
               tw, size=18, lh=24)

    # actor legend
    ly = y + 34
    c.text(L, ly, "Actor composition", size=17, weight="600", anchor="start")
    lx = L + text_width("Actor composition", 17, "600") + 26
    for key in ("X", "M", "H"):
        colour = ACTOR_COLOUR[key]
        c.rect(lx, ly - 14, 21, 18, fill=tint(colour, 0.55), stroke=colour, sw=1.4, rx=3)
        c.text(lx + 10.5, ly, key, size=16, weight="700")
        c.text(lx + 29, ly, ACTOR_NAME[key], size=16, anchor="start", fill=MUTE)
        lx += 29 + text_width(ACTOR_NAME[key], 16) + 26
    c.text(lx, ly, "an empty slot means that actor class does not participate",
           size=16, anchor="start", fill=MUTE)

    y = ly + 40
    c.text(L, y, "(a)  Authority tiers", size=20, weight="700", anchor="start")
    y += 20

    for title, colour, roles in TIERS:
        c.rect(L, y, tw, 32, fill=tint(colour, 0.14), stroke=colour, sw=1.4, rx=4)
        lines, sz = fit(title, tw - 28, 17, "600", max_lines=1, min_size=15)
        c.text(L + 14, y + 22, lines[0], size=sz, weight="600", anchor="start")
        y += 40
        for i, (name, actors, blocks, note) in enumerate(roles):
            x = L + i * (CARD_W + CARD_GAP)
            never = blocks == "nothing"
            c.rect(x, y, CARD_W, CARD_H, fill="#FFFFFF", stroke=colour, sw=1.6, rx=5)
            inner = CARD_W - 28
            nl, ns = fit(name, inner, 18, "600", max_lines=2)
            ny = y + 26
            for line in nl:
                c.text(x + 14, ny, line, size=ns, weight="600", anchor="start")
                ny += ns + 4
            after = actor_strip(c, x + 14, ny - 2, actors)
            tag = "blocks nothing" if never else f"blocks {blocks}"
            tl, ts = fit(tag, x + CARD_W - 14 - (after + 10), 16, "600",
                         max_lines=1, min_size=14)
            c.text(after + 10, ny + 12, tl[0], size=ts, weight="600", anchor="start",
                   fill=MUTE if never else colour)
            c.para(x + 14, ny + 42, note, inner, size=16, max_lines=2)
        y += CARD_H + 18

    y = c.para(L, y + 4,
               "The Metascience Lead blocks nothing by design: a function that both measures the laboratory and can "
               "veto its work acquires an interest in the numbers.",
               tw, size=16, lh=21)

    # ---- panel (b) --------------------------------------------------------
    y += 30
    c.hrule(L, W - L, y, sw=1.2)
    y += 30
    c.text(L, y, "(b)  How one operator legally holds several roles",
           size=20, weight="700", anchor="start")
    y += 20

    bw, bh = 520, 196
    c.rect(L, y, bw, bh, fill=tint(INK, 0.03), stroke=RULE, sw=1.2)
    c.text(L + 16, y + 30, "RoleBinding", size=18, weight="700", anchor="start")
    rows = [("role_id", "statistical_methods_owner", INK),
            ("actor.human", "one operator", INK),
            ("must_be_independent_from", "experiment_analyst", PURPLE),
            ("can_combine_with", "scientific_owner", GREEN),
            ("cannot_combine_with", "final_independent_verifier", VERM)]
    ry = y + 62
    key_w = max(text_width(k + ":", 15) for k, _, _ in rows)
    for key, val, colour in rows:
        c.text(L + 16, ry, key + ":", size=15, anchor="start", fill=MUTE, family=MONO)
        c.text(L + 16 + key_w + 12, ry, val, size=15, anchor="start", fill=colour,
               weight="600", family=MONO)
        ry += 26

    ax = L + bw + 30
    c.cell(ax, y + 8, 250, 66, "Constraint engine", "admits or refuses each binding",
           accent=INK, sw=1.6)
    c.path(f"M {L + bw + 4} {y + 41} L {ax - 6} {y + 41}", stroke=INK, sw=1.8)
    ok_y, no_y = y + 96, y + 152
    c.cell(ax, ok_y, 250, 46, "ADMITTED", "", accent=GREEN, sw=1.8, head_size=17)
    c.cell(ax, no_y, 250, 46, "REFUSED", "", accent=VERM, sw=1.8, head_size=17)
    c.path(f"M {ax + 125} {y + 74} L {ax + 125} {ok_y - 4}", stroke=GREEN, sw=1.8, marker="arrowsm")
    c.path(f"M {ax + 125} {ok_y + 46} L {ax + 125} {no_y - 4}", stroke=VERM, sw=1.8, marker="arrowsm")
    c.para(ax + 262, ok_y + 20, "may also hold scientific_owner", 200, size=16, max_lines=2)
    c.para(ax + 262, no_y + 20, "may not also verify its own work", 200, size=16, max_lines=2)

    y += bh + 26
    c.para(L, y,
           "Independence stops being a question of how many people exist and becomes one of which combinations remain "
           "admissible. ADR-001 settles what that means for a solo operator: R1 proceeds solo, R2 proceeds and is "
           "declared partial in the record, and R3 is BLOCKED outright rather than waived. The constraint is now "
           "enforced instead of argued about — and BLOCKED means a class of work this repository cannot accept alone.",
           tw, size=17, fill=INK, lh=23, max_lines=4)

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "aethrion_roles.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_roles.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
