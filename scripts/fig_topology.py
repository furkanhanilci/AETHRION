#!/usr/bin/env python3
"""Figure 9 — where things live: repository, vault, and the outside world.

Five-second message
    The repository is the only place anything is authored; the vault is a
    one-way mirror; the outside world is read-only.

Archetype
    A source-of-truth topology with direction on every edge. Direction is the
    content: a two-way sync between a repository and a note vault would create
    a second place to be wrong in, and this figure exists to say it does not.

Sources
    scripts/mirror_vault.py, docs/architecture/AETHRION_ARCHITECTURE.md,
    scripts/verify_references.py, scripts/monitor_sources.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, text_width, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24


def main() -> None:
    H = 1000
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "Where things live, and which way they move", size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "Three surfaces, and only one of them is authoritative. Everything is written in the Git repository. "
               "The Obsidian vault is produced from it and is never edited back. External bibliographic services are "
               "read at verification time and their answers are recorded, never assumed. Every arrow below points "
               "one way, and that is the design, not a simplification of it.",
               tw, size=18, lh=24)

    # Column 1: authoring surface
    top = y + 34
    col_w = 330
    col_h = 396
    c.rect(L, top, col_w, col_h, fill=tint(BLUE, 0.06), stroke=BLUE, sw=2.2)
    c.text(L + 16, top + 30, "Git repository", size=21, weight="700", anchor="start", fill=BLUE)
    c.para(L + 16, top + 52, "The single source of truth. Authored by humans and agents; reviewed as a diff.",
           col_w - 32, size=16, lh=21, max_lines=2)
    authored = [("Hand-authored", "architecture, decision records, planning corpus, skills", INK),
                ("Generated, committed", "STATUS.md, workstream indexes, figures — never hand-edited", PURPLE),
                ("Sealed", "221 planning files, byte-identical to baseline v1.0.4", VERM),
                ("Signed", "evidence manifests, Ed25519, interim profile", GREEN)]
    for i, (h, b, col) in enumerate(authored):
        c.cell(L + 16, top + 96 + i * 74, col_w - 32, 66, h, b, accent=col,
               head_size=17, body_size=16, max_head_lines=1, max_body_lines=3)

    # Column 2: transforms
    tx = L + col_w + 44
    t_w = 300
    c.text(tx, top + 30, "Transforms", size=21, weight="700", anchor="start", fill=MUTE)
    c.para(tx, top + 52, "Deterministic, re-runnable, and each one has a --check mode that fails on drift.",
           t_w, size=16, lh=21, max_lines=2)
    transforms = [("make_figures.py", "regenerates all figures, then re-measures them independently"),
                  ("write_status.py", "re-derives the status page from the bundle it just ran"),
                  ("make_plan_indexes.py", "rebuilds every workstream index from its directory"),
                  ("mirror_vault.py", "projects documents and figures into the vault layout")]
    for i, (h, b) in enumerate(transforms):
        c.cell(tx, top + 96 + i * 74, t_w, 66, h, b, accent=MUTE, head_size=17, body_size=16,
               max_head_lines=1, max_body_lines=3, dash="5 3")
        ax = L + col_w
        cy = top + 96 + i * 74 + 33
        c.path(f"M {ax + 6} {cy} L {tx - 6} {cy}", stroke=RULE, sw=1.6, marker="arrowsm")

    # Column 3: vault
    vx = tx + t_w + 44
    v_w = W - L - vx
    c.rect(vx, top, v_w, col_h, fill=tint(GREEN, 0.06), stroke=GREEN, sw=2.2, dash="6 4")
    c.text(vx + 16, top + 30, "Obsidian vault", size=21, weight="700", anchor="start", fill=GREEN)
    c.para(vx + 16, top + 52, "A reading surface. Regenerated wholesale; anything typed here is lost on the next mirror.",
           v_w - 32, size=16, lh=21, max_lines=2)
    groups = [("01–03", "Overview, decisions, implementation notes"),
              ("04", "Architecture, with the figures copied alongside"),
              ("05", "Evidence, including the mirrored status page"),
              ("06–09", "Planning corpus, reporting, reference material")]
    for i, (h, b) in enumerate(groups):
        c.cell(vx + 16, top + 96 + i * 74, v_w - 32, 66, h, b, accent=GREEN,
               head_size=17, body_size=16, max_head_lines=1, max_body_lines=3)
        cy = top + 96 + i * 74 + 33
        c.path(f"M {tx + t_w + 6} {cy} L {vx + 10} {cy}", stroke=GREEN, sw=1.8, marker="arrowsm")

    c.rect(vx + 16, top + col_h - 40, v_w - 32, 28, fill=tint(VERM, 0.12), stroke=VERM, sw=1.4, rx=4)
    c.text(vx + v_w / 2, top + col_h - 21, "no path leads back", size=17, weight="700", fill=VERM)

    # Outside world
    oy = top + col_h + 34
    c.rect(L, oy, tw, 148, fill=tint(ORANGE, 0.05), stroke=ORANGE, sw=2.0, dash="6 4")
    c.text(L + 16, oy + 30, "Outside world — read-only, and recorded when read", size=21,
           weight="700", anchor="start", fill=ORANGE)
    ext = [("Crossref", "primary DOI resolution; title match at 0.82"),
           ("OpenAlex", "fallback when Crossref is silent"),
           ("arXiv", "preprints and identifiers Crossref does not hold"),
           ("Positive control", "a known-live DOI; if it goes quiet, the sweep fails loudly")]
    bw = (tw - 32 - 3 * 14) / 4
    for i, (h, b) in enumerate(ext):
        c.cell(L + 16 + i * (bw + 14), oy + 58, bw, 74, h, b,
               accent=VERM if i == 3 else ORANGE, head_size=17, body_size=16,
               max_head_lines=1, max_body_lines=3)
    c.path(f"M {L + tw / 2} {oy} L {L + tw / 2} {top + col_h + 6}", stroke=ORANGE, sw=1.8,
           marker="arrowsm", dash="5 4")

    ny = oy + 148 + 26
    c.hrule(L, W - L, ny, sw=1.2)
    c.text(L, ny + 30, "Reality", size=18, weight="700", anchor="start", fill=VERM)
    c.para(L + 80, ny + 30,
           "Of 33 registered references, 27 verify against these services and 18 carry no DOI at all, which is why "
           "the sweep reports coverage rather than a pass. The mirror is one-way by construction, not by convention: "
           "it overwrites, so the failure mode of editing the vault is losing that edit, not corrupting the source.",
           W - L - (L + 80), size=17, fill=INK, lh=23)

    out = ROOT / "docs" / "figures" / "aethrion_topology.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_topology.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
