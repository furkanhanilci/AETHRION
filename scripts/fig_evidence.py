#!/usr/bin/env python3
"""Figure 3 — the evidence chain, and how much of it exists.

Five-second message
    A claim is admissible only if it resolves backwards to an exact source span
    and forwards to a signed, logged attestation — and today exactly one link of
    that chain is implemented.

Archetype
    Serpentine chain with a status channel, plus an attached attestation
    sub-chain. The status encoding is the point of the figure: an architecture
    diagram that does not say which parts exist is a wish, not a description.

Encoding
    Solid stroke, filled  = implemented and verified locally
    Dashed stroke, hollow = designed, not built
    Colour marks the kind of object, never the status; status is carried by
    stroke pattern and an explicit label, so the distinction survives greyscale
    printing and colour-vision deficiency.

Sources
    docs/architecture/AIRL_OS_ARCHITECTURE.md §3, §8, §10
    docs/architecture/AIRL_OS_EXTERNAL_STANDARDS.md §3
    planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, VERM,
                        Canvas, tint)

W, H = 1200, 906
L = 24
NW, NH, NGAP = 206, 74, 32

# label, sublabel, accent, built?
CHAIN = [
    ("Source", "the paper", ORANGE, True),
    ("SourceRepresentation", "parsed · hashed", ORANGE, True),
    ("EvidenceSpan", "the exact sentence", GREEN, False),
    ("ClaimVersion", "what we assert", BLUE, False),
    ("ExperimentRun", "what we ran", BLUE, False),
    ("Review", "who challenged it", PURPLE, False),
    ("Reproduction", "does it hold again", GREEN, False),
    ("DecisionRecord", "a human accepted it", VERM, False),
    ("Publication", "scope-checked prose", VERM, False),
    ("Monitoring", "does it still hold", PURPLE, False),
]
ROW_LEN = 5


def node_xy(i: int, top: float) -> tuple[float, float]:
    row, col = divmod(i, ROW_LEN)
    if row % 2 == 1:                       # serpentine: right to left
        col = ROW_LEN - 1 - col
    return L + col * (NW + NGAP), top + row * (NH + 78)


def main() -> None:
    c = Canvas(W, H)
    c.text(L, 46, "The evidence chain — and how much of it exists",
           size=30, weight="700", anchor="start")
    c.text(L, 76, "Nothing becomes knowledge by being asserted. It becomes knowledge by surviving a chain in which every link is addressable",
           size=17, fill=MUTE, anchor="start")
    c.text(L, 98, "in both directions: from a published sentence back to the source span, and from a retracted source forward to every dependent claim.",
           size=17, fill=MUTE, anchor="start")

    # legend
    ly = 132
    c.rect(L, ly - 14, 26, 17, fill=tint(GREEN, 0.30), stroke=INK, sw=1.8, rx=3)
    c.text(L + 34, ly, "implemented and verified locally", size=16, anchor="start")
    c.rect(L + 300, ly - 14, 26, 17, fill="#FFFFFF", stroke=MUTE, sw=1.4, rx=3, dash="5 4")
    c.text(L + 334, ly, "designed, not built", size=16, anchor="start")
    c.text(L + 520, ly, "Colour marks the kind of object, never its status.", size=16,
           anchor="start", fill=MUTE)

    top = 176
    for i, (name, sub, accent, built) in enumerate(CHAIN):
        x, y = node_xy(i, top)
        c.cell(x, y, NW, NH, name, sub,
               accent=accent if built else MUTE,
               fill=tint(accent, 0.18) if built else "#FFFFFF",
               stroke_override=INK if built else MUTE,
               sw=2.0 if built else 1.4, dash=None if built else "5 4",
               head_fill=INK if built else MUTE)
        if built:
            c.text(x + NW / 2, y - 10, "working", size=16, weight="700", fill=GREEN)

    # connectors
    for i in range(len(CHAIN) - 1):
        x0, y0 = node_xy(i, top)
        x1, y1 = node_xy(i + 1, top)
        solid = CHAIN[i][3] and CHAIN[i + 1][3]
        stroke = INK if solid else MUTE
        dash = None if solid else "5 4"
        if y0 == y1:
            direction = 1 if x1 > x0 else -1
            sx = x0 + NW if direction == 1 else x0
            ex = x1 if direction == 1 else x1 + NW
            c.path(f"M {sx} {y0 + NH / 2} L {ex - 6 * direction} {y0 + NH / 2}",
                   stroke=stroke, sw=1.8, dash=dash)
        else:                               # drop to the next serpentine row
            mx = x0 + NW / 2
            c.path(f"M {mx} {y0 + NH} L {mx} {y1 - 8}", stroke=stroke, sw=1.8, dash=dash)

    # revision loop: monitoring back to the claim
    mx0, my0 = node_xy(9, top)
    cx1, cy1 = node_xy(3, top)
    loop_y = my0 + NH + 30
    c.path(f"M {mx0 + NW / 2} {my0 + NH} L {mx0 + NW / 2} {loop_y} "
           f"L {cx1 + NW / 2} {loop_y} L {cx1 + NW / 2} {cy1 + NH + 6}",
           stroke=PURPLE, sw=1.8, dash="6 4", marker="arrowsm")
    c.text((mx0 + cx1) / 2 + NW / 2, loop_y - 8,
           "supersede · revise · retract — VERIFIED is not a permanent state",
           size=16, fill=PURPLE)

    # ---- attestation sub-chain -------------------------------------------
    ay = loop_y + 54
    c.hrule(L, W - L, ay, stroke=RULE, sw=1.2)
    ay += 30
    c.text(L, ay, "What makes a link admissible: the attestation behind every acceptance",
           size=20, weight="700", anchor="start")
    ay += 20

    steps = [("EvidenceManifest", "tests · environment"), ("in-toto Statement", "subject + predicate"),
             ("DSSE envelope", "signed as one unit"), ("Sigstore", "keyless, OIDC-bound"),
             ("Rekor", "transparency record"), ("OpenTimestamps", "external time anchor")]
    sw_, sh, sg = 178, 62, 18
    for i, (name, sub) in enumerate(steps):
        x = L + i * (sw_ + sg)
        c.cell(x, ay, sw_, sh, name, sub, accent=MUTE, fill="#FFFFFF", sw=1.4,
               dash="5 4", head_size=17, head_fill=MUTE)
        if i:
            c.path(f"M {x - sg} {ay + sh / 2} L {x - 6} {ay + sh / 2}",
                   stroke=MUTE, sw=1.6, dash="4 4")
    c.text(L, ay + sh + 26,
           "Rekor is a tamper-evident record for signed metadata, not an artifact store: WP-026 is deferred behind it, not cancelled.",
           size=16, anchor="start", fill=MUTE)

    # ---- blockers ---------------------------------------------------------
    by = ay + sh + 52
    bw = (W - 2 * L - 24) / 2
    for i, (tag, title, body) in enumerate((
            ("C1", "Evidence bootstrap",
             "Storage half addressed on paper by WP-000. No manifest has been issued, signed or logged."),
            ("C2", "Independent verification",
             "Who may verify in a one-person operation is undecided; no standard answers it."))):
        x = L + i * (bw + 24)
        c.rect(x, by, bw, 92, fill=tint(VERM, 0.08), stroke=VERM, sw=1.6)
        c.text(x + 16, by + 30, tag, size=21, weight="700", anchor="start", fill=VERM)
        c.para(x + 16 + 38, by + 30, title, bw - 70, size=18, weight="600", fill=INK,
               max_lines=1)
        c.para(x + 16, by + 58, body, bw - 32, size=16, fill=INK, max_lines=2, lh=21)
    c.para(L, by + 118,
           "Until both are resolved no work package can reach ACCEPTED — which is why nine of the ten links above are "
           "drawn hollow.",
           W - 2 * L, size=16, fill=INK, weight="500")

    out = Path(__file__).resolve().parent.parent / "docs" / "figures" / "airl_os_evidence_chain.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/airl_os_evidence_chain.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
