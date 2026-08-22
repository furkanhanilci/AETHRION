#!/usr/bin/env python3
"""Figure 1 — the AIRL-OS research lifecycle, G0 to G10.

Five-second message
    Every gate resolves in the same order — the mechanical check runs first and
    cannot be overridden, a model may produce but never decide, a human holds
    authority — and two gates admit no model at all.

Archetype
    A matrix, not a pipeline: gates on the vertical axis (time) crossed with
    actor class on the horizontal (authority). The interesting question at each
    gate is not "what comes next" but "who is allowed to act", and a left-to-right
    pipeline cannot express that.

Layout contract
    Every cell's text is fitted against the cell's inner width by
    ``figure_kit.Canvas.cell``. Nothing is positioned by eye, and a string that
    will not fit fails the build.

Sources
    docs/architecture/AIRL_OS_ARCHITECTURE.md §5, §6
    docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md §3.2
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, FONT, GREEN, INK, MUTE, ORANGE, PURPLE, RULE,
                        VERM, Canvas, fit, tint)

W = 1200
L, GUT = 24, 56
C0 = L + GUT
COLS = [("Gate", 150), ("Mechanical — runs first, unwaivable", 255),
        ("Model — produces, never decides", 255), ("Human — authority", 185),
        ("Frozen output", 215)]
GAP = 10
ROW_H, ROW_GAP = 72, 7
TOP = 246
BRANCH_H = 82

# gate, name, mechanical, model, human, frozen output, note
ROWS = [
    ("G0", "Intake", ("duplicate search", "embedding + graph index"),
     ("triage", ""), ("greenlight", ""), ("IntakeRecord", ""), ""),
    ("G1", "Charter", ("RiskProfile → AssuranceClass", "a policy engine, not a model"),
     ("charter draft", "risk vector proposal"), ("writes the decision question", ""),
     ("ProjectCharter", "ControlPlan"), ""),
    ("G2", "Protocol", ("template completeness", "placeholder sweep"),
     ("protocol draft", "pre-mortem · Stage-1 review"), ("Scientific + Statistical Owner sign", ""),
     ("ProtocolManifest", ""), ""),
    ("G2b", "Analysis plan", ("—", ""), ("plan draft", "power analysis"),
     ("Statistical Methods Owner locks", ""),
     ("AnalysisPlanManifest", "InPrincipleAcceptance"), "confirmatory"),
    ("G3", "Literature", ("GROBID · DOI · dedup", "hashing · PRISMA-S report"),
     ("query plan · screening", "declared stopping rule"), ("Evidence Lead freezes", ""),
     ("LiteratureSetManifest", ""), ""),
    ("G4", "Baseline", ("the baseline run", ""), ("compute plan", "red-team pre-mortem"),
     ("budget approval", ""), ("BaselineBundle", "FalsificationPlan"), ""),
    ("G5", "Execute", ("the experiment itself", ""), ("NO MODEL", "unless it is the subject"),
     ("—", ""), ("ExperimentRun", ""), ""),
    ("G6", "Assurance", ("statcheck · GRIM · GRIMMER", "entailment · hashes"),
     ("blind + adversarial review", "different provider family"), ("—", ""),
     ("ReviewRecord", "ProducerResponse"), ""),
    ("G7a", "Reproduction", ("same manifest, same seed", "deterministic"),
     ("NO MODEL", "it reproduces or it does not"), ("—", ""),
     ("reproduction result", ""), ""),
    ("G7b", "Replication", ("distribution test", ""), ("—", ""),
     ("RSE assigns the badge", ""), ("replication verdict", ""), ""),
    ("G8", "Decision", ("package completeness", ""), ("recommendation only", ""),
     ("DECIDES", "human only, under quota"), ("DecisionRecord", ""), ""),
    ("G9", "Publish", ("scope conformance", "RO-Crate · hashes"), ("text draft", ""),
     ("Decision Owner + Editor", ""), ("PublicationPackage", ""), ""),
    ("G10", "Monitor", ("Crossref · Retraction Watch", "CVE feeds"), ("signal triage", ""),
     ("decides on a material signal", ""), ("supersession records", ""), ""),
]
BRANCH_AFTER = 2
NO_MODEL_ROWS = {6, 8}
H = TOP + len(ROWS) * (ROW_H + ROW_GAP) + BRANCH_H + ROW_GAP + 132


def col_x(i: int) -> float:
    return C0 + sum(w + GAP for _, w in COLS[:i])


def main() -> None:
    c = Canvas(W, H)
    text_w = W - 2 * L

    c.text(L, 48, "The AIRL-OS research lifecycle", size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "Eleven gates. At each of them the same resolution order holds: the mechanical check runs first and "
               "cannot be overridden by a model, a model may then produce but never decide, and a human holds "
               "authority only where the gate carries it.",
               text_w, size=18, lh=24)
    y = c.para(L, y + 26,
               "Reading down the figure is time. Reading across is who may act. The hatched cells are not gaps in the "
               "design — they are the design: G5 and G7a admit no model at all.",
               text_w, size=18, fill=INK, weight="500", lh=24)

    # legend
    ly = y + 34
    x = L
    for colour, label in ((GREEN, "mechanical check"), (BLUE, "model production"),
                          (VERM, "human authority"), (ORANGE, "frozen artifact")):
        c.rect(x, ly - 13, 26, 17, fill=tint(colour, 0.35), stroke=colour, sw=1.5, rx=3)
        c.text(x + 34, ly, label, size=16, anchor="start")
        from figure_kit import text_width
        x += 34 + text_width(label, 16) + 30
    c.hatch(x, ly - 13, 26, 17)
    c.text(x + 34, ly, "no model admitted", size=16, anchor="start")
    from figure_kit import text_width
    x += 34 + text_width("no model admitted", 16) + 30
    c.path(f"M {x} {ly - 4} L {x + 26} {ly - 4}", stroke=PURPLE, sw=2.0, marker="arrowsm")
    c.text(x + 34, ly, "revision path", size=16, anchor="start")

    # column headers
    for i, (name, w) in enumerate(COLS):
        colour = {1: GREEN, 2: BLUE, 3: VERM, 4: ORANGE}.get(i, MUTE)
        lines, sz = fit(name, w, 16, "600", max_lines=1, min_size=13)
        c.text(col_x(i) + w / 2, TOP - 14, lines[0], size=sz, weight="600", fill=colour)
    c.hrule(C0, W - L, TOP - 4, sw=1.2)

    yy = TOP + 8
    row_y: dict[int, float] = {}
    for idx, (gid, gname, mech, model, human, art, note) in enumerate(ROWS):
        if idx == BRANCH_AFTER + 1:
            c.rect(col_x(0), yy, W - L - col_x(0), BRANCH_H, fill=tint(PURPLE, 0.09),
                   stroke=PURPLE, sw=1.4, dash="5 4")
            c.text(col_x(0) + 16, yy + 26, "research_mode?", size=18, weight="600",
                   anchor="start", fill=PURPLE)
            c.para(col_x(0) + 16, yy + 50,
                   "fail-closed: absent or ambiguous resolves to confirmatory",
                   COLS[0][1] + COLS[1][1] - 24, size=16, max_lines=2)
            ox = col_x(2) - 40
            for name, expl in (("exploratory", "skips G2b; may never claim confirmatory"),
                               ("replication", "locked replication contract"),
                               ("confirmatory", "G2b + in-principle acceptance")):
                c.text(ox, yy + 26, name, size=17, weight="600", anchor="start", fill=PURPLE)
                c.para(ox, yy + 48, expl, 230, size=16, max_lines=2)
                ox += 246
            yy += BRANCH_H + ROW_GAP

        row_y[idx] = yy
        c.rect(col_x(0), yy, COLS[0][1], ROW_H, fill=tint(INK, 0.045), stroke=RULE, sw=1.2)
        c.text(col_x(0) + 16, yy + 30, gid, size=21, weight="700", anchor="start")
        c.para(col_x(0) + 16, yy + 50, gname, COLS[0][1] - 28, size=16, max_lines=1)
        if note:
            c.para(col_x(0) + 16, yy + 66, note + " only", COLS[0][1] - 28, size=16,
                   fill=PURPLE, max_lines=2)

        for ci, (content, colour) in enumerate(
                ((mech, GREEN), (model, BLUE), (human, VERM), (art, ORANGE)), start=1):
            x0, w = col_x(ci), COLS[ci][1]
            head, body = content
            if ci == 2 and idx in NO_MODEL_ROWS:
                c.hatch(x0, yy, w, ROW_H)
                c.cell(x0, yy, w, ROW_H, "no model in the loop", body, accent=MUTE,
                       draw_box=False, head_fill=MUTE, head_size=17)
                continue
            if head == "—":
                c.text(x0 + w / 2, yy + ROW_H / 2 + 6, "—", size=19, fill=RULE)
                continue
            decisive = head == "DECIDES"
            c.cell(x0, yy, w, ROW_H, head, body, accent=colour,
                   sw=2.6 if decisive else 1.5, head_size=19 if decisive else 18,
                   max_head_lines=3 if not body else 2)
        yy += ROW_H + ROW_GAP

    # revision paths, routed down the reserved gutter
    def arc(from_idx: int, to_idx: int, label: str, lane: int) -> None:
        x = C0 - 16 - lane * 24
        y0, y1 = row_y[from_idx] + ROW_H / 2, row_y[to_idx] + ROW_H / 2
        c.path(f"M {col_x(0)} {y0} L {x} {y0} L {x} {y1} L {col_x(0)} {y1}",
               stroke=PURPLE, sw=1.8, dash="6 4", marker="arrowsm")
        span = abs(y0 - y1) - 40
        lines, sz = fit(label, span, 16, "400", max_lines=1, min_size=14)
        my = (y0 + y1) / 2
        c.parts.append(
            f'<text x="{x - 7:.1f}" y="{my:.1f}" font-family="{FONT}" font-size="{sz:g}" '
            f'fill="{PURPLE}" text-anchor="middle" '
            f'transform="rotate(-90 {x - 7:.1f} {my:.1f})">{label}</text>')

    arc(12, 2, "a material signal reopens the protocol", 0)
    arc(7, 2, "ProtocolChallenge", 1)

    ny = yy + 16
    c.hrule(L, W - L, ny, sw=1.2)
    c.text(L, ny + 30, "Status", size=18, weight="700", anchor="start", fill=VERM)
    c.para(L + 70, ny + 30,
           "None of this lifecycle is implemented. The only working component today is the literature bridge that "
           "feeds G3; every other cell above is a design commitment, and no work package has reached ACCEPTED.",
           W - L - (L + 70), size=17, fill=INK, lh=23)

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "airl_os_lifecycle.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/airl_os_lifecycle.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
