#!/usr/bin/env python3
"""Figure 14 — one canonical owner per kind of state, and everything else rebuildable.

Five-second message
    One owner per kind of truth — a rule about ownership, not a number of
    stores. Split brain does not arrive as a
    crash — it arrives as a projection that is quietly ahead of the store it
    projects, read by something that trusts it.

Why this figure exists
    The count was the defect. This paragraph said "seven plausible answers" and
    then listed eight components, and the sentence would have been wrong again
    the day a ninth arrived — because a reader who memorises "seven stores" has
    memorised the wrong thing entirely. The invariant is one owner per KIND of
    state; the number of components is an implementation detail that changes.

    An authority matrix written as prose reads as obvious and is violated within
    a sprint, because the violation is always locally reasonable: write to the
    index too, it is faster; trust the event payload, it is right there. Drawn
    with the write path and the injections beside it, the rule becomes a shape
    rather than a list of good intentions.

Archetype
    An ownership table with a write-path sequence and an injection suite,
    because the third column is what makes the first two testable.

Sources
    docs/architecture/ADR-014_canonical_authority_and_split_brain.md,
    planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-159, ACC-119
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

ROWS = [
    ("Gate and lifecycle position", "Temporal", "an event announcing a transition is a notification", ORANGE),
    ("Scientific domain records", "PostgreSQL", "Neo4j, pgvector and OpenSearch project it", ORANGE),
    ("Artifact bytes and digests", "Immutable object store", "any local copy is a cache", ORANGE),
    ("Human decisions", "Signed DecisionRecord", "a message about a decision is not one", VERM),
    ("Cognitive scratch state", "LangGraph, bounded to one task", "it cannot transition a gate", BLUE),
    ("Experiment telemetry", "MLflow", "operational only — never a scientific result", MUTE),
    ("Literature working surface", "Zotero, human regions respected", "the Source Registry owns bibliographic identity", SKY),
    ("Human synthesis surface", "Obsidian, human regions respected", "generated regions are projections and say so", SKY),
]


def main() -> None:
    row_h = 60
    H = 300 + len(ROWS) * row_h + 620
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "One canonical owner per kind of state", size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "Ask “where does this live?” of any fact in this system and several components answer "
               "plausibly — a workflow engine, a relational store, an object store, an event bus, a graph "
               "projection, a vector index and two human workspaces. The invariant is not how many "
               "there are; it is that each KIND of state has exactly one owner, and everything else "
               "is a projection that can be destroyed and rebuilt without loss.",
               tw, size=18, lh=24)

    # ------------------------------------------------------------------ table
    hy = y + 36
    c1, c2 = 300, 330
    c3 = tw - c1 - c2 - 30
    c.text(L, hy, "State", size=17, weight="700", anchor="start", fill=INK)
    c.text(L + c1 + 15, hy, "Canonical owner", size=17, weight="700", anchor="start", fill=ORANGE)
    c.text(L + c1 + c2 + 30, hy, "Everything else", size=17, weight="700", anchor="start", fill=MUTE)
    c.hrule(L, W - L, hy + 12, sw=1.6, stroke=INK)

    top = hy + 24
    for i, (state, owner, rest, col) in enumerate(ROWS):
        ry = top + i * row_h
        if i % 2:
            c.rect(L, ry - 14, tw, row_h - 6, fill=tint(MUTE, 0.05), stroke="none", sw=0)
        c.rect(L, ry + 8, 5, row_h - 24, fill=col, stroke="none", sw=0, rx=2)
        c.para(L + 16, ry + 26, state, c1 - 20, size=17, fill=INK, lh=20, max_lines=2, weight="600")
        c.para(L + c1 + 15, ry + 26, owner, c2 - 15, size=17, fill=col, lh=20, max_lines=2, weight="600")
        c.para(L + c1 + c2 + 30, ry + 26, rest, c3, size=16, fill=MUTE, lh=20, max_lines=2)

    ly = top + len(ROWS) * row_h + 6
    c.hrule(L, W - L, ly, sw=1.6, stroke=INK)

    ky = ly + 22
    c.rect(L, ky, tw, 56, fill=tint(ORANGE, 0.10), stroke=ORANGE, sw=1.6)
    c.para(L + 16, ky + 24,
           "The line that does the most work: MLflow answers what the system DID. An EvidenceManifest plus the run "
           "registry answers what may be BELIEVED. Operational telemetry is not provenance.",
           tw - 32, size=17, fill=INK, lh=21, max_lines=2)

    # ------------------------------------------------------------- write path
    wy = ky + 56 + 32
    c.text(L, wy, "The write path — the ordering is the mechanism",
           size=21, weight="700", anchor="start")
    wy2 = wy + 26
    steps = [("canonical txn\n+ outbox", "committed ATOMICALLY, together", ORANGE),
             ("publisher", "reads the outbox afterwards", BLUE),
             ("consumer", "validates identity and version", BLUE),
             ("re-reads canonical", "never promotes a payload to truth", GREEN)]
    sw_ = (tw - 3 * 18) / 4
    for i, (head, body, col) in enumerate(steps):
        bx = L + i * (sw_ + 18)
        c.cell(bx, wy2, sw_, 92, head.replace("\n", " "), body, accent=col,
               head_size=17, body_size=16, max_head_lines=2, max_body_lines=3)
        if i:
            c.path(f"M {bx - 15} {wy2 + 46} L {bx - 5} {wy2 + 46}",
                   stroke=RULE, sw=1.8, marker="arrowsm")
    c.para(L, wy2 + 124,
           "Getting this backwards is the standard way a distributed system acquires two truths: publish first, "
           "commit second, and a crash between them leaves an event describing something that never happened.",
           tw, size=17, fill=MUTE, lh=22, max_lines=2)

    # --------------------------------------------------------- injection suite
    iy = wy2 + 124 + 2 * 22 + 28
    c.text(L, iy, "Why it is an injection suite and not a property",
           size=21, weight="700", anchor="start")
    iy2 = iy + 26
    inj = ["kill the publisher after the DB commit",
           "deliver the same event twice",
           "deliver events out of order",
           "return a cancelled task's late result",
           "drop a projection and rebuild it",
           "replay a workflow after a restart",
           "two concurrent gate transitions"]
    iw = (tw - 2 * 14) / 3
    for i, label in enumerate(inj):
        bx = L + (i % 3) * (iw + 14)
        by = iy2 + (i // 3) * 62
        c.cell(bx, by, iw, 54, label, "", accent=PURPLE, head_size=17, max_head_lines=3)

    fy = iy2 + 3 * 62 + 8
    c.rect(L, fy, tw, 88, fill=tint(VERM, 0.10), stroke=VERM, sw=2.2)
    c.text(L + 18, fy + 28, "A silent divergence is the failure", size=19, weight="700",
           anchor="start", fill=VERM)
    c.para(L + 18, fy + 50,
           "Every injection must end with canonical state correct and the projection agreeing, or with an "
           "explicit recorded failure. Split brain is invisible in a healthy system and obvious only in a "
           "post-mortem, so nothing short of causing one demonstrates it would be caught. ACC-119.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=3)

    ny = fy + 88 + 26
    c.para(L, ny,
           "Status: one store in the table exists — SQLite behind the Zotero bridge. Temporal, PostgreSQL, the "
           "object store, NATS, Neo4j and MLflow are unimplemented, and the injection suite has never run.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_authority.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_authority.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
