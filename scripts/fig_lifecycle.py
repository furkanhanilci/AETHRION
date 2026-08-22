#!/usr/bin/env python3
"""Figure 1 — the AIRL-OS research lifecycle, G0 to G10.

Five-second message
    Every gate resolves in the same order — the mechanical check runs first and
    cannot be overridden, a model may produce but never decide, a human holds
    authority — and three gates admit no model at all.

Archetype
    Staged process on the vertical axis (time) crossed with actor class on the
    horizontal axis (authority). Not a left-to-right pipeline: the research
    topology is a *matrix*, because the interesting question at every gate is
    not "what comes next" but "who is allowed to act".

Sources
    docs/architecture/AIRL_OS_ARCHITECTURE.md §5, §6
    docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md §3.2
    Every visible string is taken from those documents.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, FONT, GREEN, INK, MUTE, ORANGE, PURPLE, RULE,
                        VERM, Canvas, tint)

W, H = 1200, 1268
L = 20            # page margin
GUT = 54          # left gutter reserved for the revision paths
C0 = L + GUT      # first column origin
COLS = [("Gate", 160), ("Mechanical — runs first, cannot be overridden", 280),
        ("Model — produces, never decides", 280), ("Human — authority", 178),
        ("Frozen output", 168)]
GAP = 10
ROW_H, ROW_GAP = 60, 6
TOP = 236

ROWS = [
    ("G0", "Intake", ["duplicate search", "embedding + graph index"], ["triage"],
     ["greenlight"], ["IntakeRecord"], None),
    ("G1", "Charter", ["RiskProfile → AssuranceClass", "policy engine, not a model"],
     ["charter draft", "risk vector proposal"], ["writes the", "decision question"],
     ["ProjectCharter", "ControlPlan"], None),
    ("G2", "Protocol", ["template completeness", "placeholder sweep"],
     ["protocol draft · pre-mortem", "different-family review"],
     ["Scientific + Statistical", "Owner sign"], ["ProtocolManifest"], None),
    ("G2b", "Analysis plan", ["—"], ["plan draft · power analysis"],
     ["Statistical Methods", "Owner locks"],
     ["AnalysisPlanManifest", "InPrincipleAcceptance"], "confirmatory only"),
    ("G3", "Literature", ["GROBID · DOI resolution", "dedup · hashing · PRISMA-S"],
     ["query plan · screening", "declared stopping rule"], ["Evidence Lead", "freezes"],
     ["LiteratureSetManifest"], None),
    ("G4", "Baseline", ["the baseline run"], ["compute plan", "red-team pre-mortem"],
     ["budget approval"], ["BaselineBundle", "FalsificationPlan"], None),
    ("G5", "Execute", ["the experiment itself"], ["NO MODEL"], ["—"],
     ["ExperimentRun"], None),
    ("G6", "Assurance", ["statcheck · GRIM · GRIMMER", "entailment · hashes"],
     ["blind + adversarial review", "different provider family"],
     ["—"], ["ReviewRecord", "ProducerResponse"], None),
    ("G7a", "Reproduction", ["same manifest, same seed", "deterministic"], ["NO MODEL"],
     ["—"], ["reproduction result"], None),
    ("G7b", "Replication", ["distribution test"], ["—"], ["RSE assigns", "the badge"],
     ["replication verdict"], None),
    ("G8", "Decision", ["package completeness"], ["recommendation only"],
     ["DECIDES", "human only, under quota"], ["DecisionRecord"], None),
    ("G9", "Publish", ["scope conformance", "RO-Crate · hashes"], ["text draft"],
     ["Decision Owner", "+ Editor"], ["PublicationPackage"], None),
    ("G10", "Monitor", ["Crossref · Retraction Watch", "CVE feeds"], ["signal triage"],
     ["decides on a", "material signal"], ["supersession records"], None),
]
BRANCH_AFTER = 2          # the research_mode router sits between G2 and G2b
BRANCH_H = 54
NO_MODEL_ROWS = {6, 8}    # G5 and G7a — the model column is deliberately empty


def col_x(i: int) -> float:
    return C0 + sum(w + GAP for _, w in COLS[:i])


def main() -> None:
    c = Canvas(W, H)

    # ---- title block ------------------------------------------------------
    c.text(L, 46, "The AIRL-OS research lifecycle", size=30, weight="700", anchor="start")
    c.text(L, 76, "Eleven gates. At each, the same resolution order: mechanical first and unwaivable,",
           size=18, fill=MUTE, anchor="start")
    c.text(L, 99, "then model production, then human authority. Reading down is time; across is who may act.",
           size=18, fill=MUTE, anchor="start")
    c.text(L, 124, "The empty cells at G5 and G7a are the design, not an omission.",
           size=18, fill=INK, anchor="start", weight="600")

    # ---- legend -----------------------------------------------------------
    ly = 166
    items = [(GREEN, "mechanical check"), (BLUE, "model production"),
             (VERM, "human authority"), (ORANGE, "frozen artifact")]
    x = L
    for colour, label in items:
        c.rect(x, ly - 13, 26, 16, fill=tint(colour, 0.35), stroke=colour, sw=1.6, rx=3)
        c.text(x + 34, ly, label, size=17, anchor="start", fill=INK)
        x += 34 + len(label) * 8.6 + 34
    c.hatch(x, ly - 13, 26, 16)
    c.text(x + 34, ly, "no model admitted", size=17, anchor="start")
    x += 34 + 17 * 8.6 + 34
    c.path(f"M {x} {ly - 5} L {x + 26} {ly - 5}", stroke=PURPLE, sw=2.0, marker="arrowsm")
    c.text(x + 34, ly, "revision path", size=17, anchor="start")

    # ---- column headers ---------------------------------------------------
    hy = TOP - 16
    for i, (name, w) in enumerate(COLS):
        cx = col_x(i) + w / 2
        colour = {1: GREEN, 2: BLUE, 3: VERM, 4: ORANGE}.get(i, MUTE)
        c.text(cx, hy, name, size=17, weight="600", fill=colour, spacing=0.3)
    c.hrule(C0, W - L, TOP - 4, stroke=RULE, sw=1.2)

    # ---- rows -------------------------------------------------------------
    y = TOP + 6
    row_y: dict[int, float] = {}
    for idx, (gid, gname, mech, model, human, art, note) in enumerate(ROWS):
        if idx == BRANCH_AFTER + 1:
            by = y
            c.rect(col_x(0), by, W - L - col_x(0), BRANCH_H, fill=tint(PURPLE, 0.10),
                   stroke=PURPLE, sw=1.4, dash="5 4")
            c.text(col_x(0) + 14, by + 24, "research_mode?", size=18, weight="600",
                   anchor="start", fill=PURPLE)
            c.text(col_x(0) + 14, by + 44, "the classification is fail-closed: absent or ambiguous resolves to confirmatory",
                   size=16, anchor="start", fill=MUTE)
            opts = [("exploratory", "skips G2b — may never claim confirmatory"),
                    ("replication", "locked replication contract"),
                    ("confirmatory", "G2b + in-principle acceptance")]
            ox = col_x(1) + 60
            for name, expl in opts:
                c.text(ox, by + 24, name, size=17, weight="600", anchor="start", fill=PURPLE)
                c.text(ox, by + 44, expl, size=16, anchor="start", fill=MUTE)
                ox += 306
            y += BRANCH_H + ROW_GAP

        row_y[idx] = y
        # gate cell
        c.rect(col_x(0), y, COLS[0][1], ROW_H, fill=tint(INK, 0.05), stroke=RULE, sw=1.2)
        c.text(col_x(0) + 16, y + 27, gid, size=21, weight="700", anchor="start", fill=INK)
        c.text(col_x(0) + 16, y + 47, gname, size=17, anchor="start", fill=MUTE)
        if note:
            c.text(col_x(0) + COLS[0][1] - 10, y + 47, note, size=16, anchor="end", fill=PURPLE)

        for ci, (content, colour) in enumerate(
                ((mech, GREEN), (model, BLUE), (human, VERM), (art, ORANGE)), start=1):
            x0, w = col_x(ci), COLS[ci][1]
            empty = content == ["—"]
            no_model = ci == 2 and idx in NO_MODEL_ROWS
            if no_model:
                c.hatch(x0, y, w, ROW_H)
                c.text(x0 + w / 2, y + 28, "no model in the loop", size=17,
                       weight="600", fill=MUTE)
                c.text(x0 + w / 2, y + 47, "unless the model is the subject" if idx == 6
                       else "it reproduces or it does not", size=16, fill=MUTE)
                continue
            if empty:
                c.text(x0 + w / 2, y + 36, "—", size=19, fill=RULE)
                continue
            strong = (ci == 3 and content[0] == "DECIDES")
            c.rect(x0, y, w, ROW_H, fill=tint(colour, 0.13),
                   stroke=colour, sw=2.4 if strong else 1.5)
            first_size = 18 if not strong else 19
            if len(content) == 1:
                c.text(x0 + w / 2, y + 36, content[0], size=first_size,
                       weight="600" if strong else "500", fill=INK)
            else:
                c.text(x0 + w / 2, y + 27, content[0], size=first_size,
                       weight="600" if strong else "500", fill=INK)
                c.text(x0 + w / 2, y + 47, content[1], size=16, fill=MUTE)
        y += ROW_H + ROW_GAP

    # ---- revision paths, drawn in the left gutter -------------------------
    def arc(from_idx: int, to_idx: int, label: str, lane: int) -> None:
        """Route a revision path down the left gutter, one vertical lane each."""
        x = C0 - 14 - lane * 22
        y0 = row_y[from_idx] + ROW_H / 2
        y1 = row_y[to_idx] + ROW_H / 2
        c.path(f"M {col_x(0)} {y0} L {x} {y0} L {x} {y1} L {col_x(0)} {y1}",
               stroke=PURPLE, sw=1.8, dash="6 4", marker="arrowsm")
        my = (y0 + y1) / 2
        c.parts.append(
            f'<text x="{x - 7}" y="{my}" font-family="{FONT}" font-size="16" '
            f'fill="{PURPLE}" text-anchor="middle" '
            f'transform="rotate(-90 {x - 7} {my})">{label}</text>')

    arc(12, 2, "a material signal reopens the protocol", 0)
    arc(7, 2, "ProtocolChallenge", 1)

    # ---- honest status note ----------------------------------------------
    ny = y + 14
    c.hrule(L, W - L, ny, stroke=RULE, sw=1.2)
    c.text(L, ny + 26, "Status", size=18, weight="700", anchor="start", fill=VERM)
    c.text(L + 62, ny + 26,
           "None of this lifecycle is implemented. The only working component today is the literature bridge that feeds G3;",
           size=17, anchor="start", fill=INK)
    c.text(L + 62, ny + 47,
           "every other cell above is a design commitment, and no work package has reached ACCEPTED.",
           size=17, anchor="start", fill=INK)

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "airl_os_lifecycle.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote {out.relative_to(out.parents[2])}  ({W}×{H})")


if __name__ == "__main__":
    main()
