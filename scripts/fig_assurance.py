#!/usr/bin/env python3
"""Figure 12 — what "machines verify" means, and what a document may assert.

Five-second message
    "Verify" was one word doing two incompatible jobs. Split into four classes,
    the non-waivable rule becomes coherent — and the publication compiler
    becomes something that refuses rather than something that writes.

Why this figure exists
    This project's thesis sentence is "agents produce, machines verify, humans
    decide". Calling a language model's entailment judgement "mechanical
    verification" lends the certainty of a hash comparison to a check with an
    error rate, in the one place the architecture is supposed to be most
    careful. The figure draws the boundary that repairs it.

Archetype
    A four-band ladder from certain to human, followed by the refusal path that
    consumes it. The colour break between V1 and V2 is the whole argument.

Sources
    docs/architecture/ADR-008_verification_taxonomy.md,
    docs/architecture/ADR-009_publication_as_projection.md,
    planning/commissioning/08_EVIDENCE_ASSURANCE/WP-087, WP-090
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import (BLUE, GREEN, INK, MUTE, ORANGE, PURPLE, RULE, SKY,
                        VERM, Canvas, tint)

ROOT = Path(__file__).resolve().parent.parent
W, L = 1200, 24

CLASSES = [
    ("V0", "Deterministic", GREEN,
     "digest comparison · schema validation · signature · reference resolution · artifact existence",
     "Same authoritative input, same answer, always. Never invokes a model",
     "non-waivable"),
    ("V1", "Computational or statistical", GREEN,
     "score recomputation · statistical test · GRIM and statcheck consistency · tolerance comparison",
     "Deterministic given pinned software, configuration and input snapshot",
     "non-waivable"),
    ("V2", "Model-mediated semantic", ORANGE,
     "citation entailment · claim scope and overclaim · method–code alignment · prior-art overlap",
     "A judgement with a false-positive and a false-negative rate, whether or not anyone measured them",
     "requires a current qualification"),
    ("V3", "Human scientific judgement", VERM,
     "residual methodological interpretation · high-risk arbitration · G8 · integrity findings",
     "Authority, not throughput",
     "authority"),
]


def main() -> None:
    H = 1400
    c = Canvas(W, H)
    tw = W - 2 * L

    c.text(L, 48, "What “machines verify” means, and what a document may assert",
           size=30, weight="700", anchor="start")
    y = c.para(L, 80,
               "One word was carrying two jobs: a hash comparison that is either right or wrong, and a language "
               "model deciding whether a cited passage supports a sentence. Calling both mechanical manufactures "
               "confidence. Four classes separate them, and the boundary that matters is between V1 and V2.",
               tw, size=18, lh=24)

    # ------------------------------------------------------------------ ladder
    ly = y + 38
    row_h = 118
    for i, (code, name, col, examples, prop, waiver) in enumerate(CLASSES):
        ry = ly + i * row_h
        c.rect(L, ry, tw, row_h - 12, fill=tint(col, 0.08), stroke=col, sw=1.8)
        c.rect(L, ry, 78, row_h - 12, fill=tint(col, 0.30), stroke=col, sw=1.8)
        c.text(L + 39, ry + 44, code, size=27, weight="700", fill=INK)
        c.text(L + 96, ry + 30, name, size=20, weight="700", anchor="start")
        c.para(L + 96, ry + 54, examples, tw - 400, size=16, fill=MUTE, lh=20, max_lines=2)
        c.para(L + 96, ry + 92, prop, tw - 400, size=16, fill=INK, lh=20, max_lines=1)
        c.para(W - L - 280, ry + 30, waiver, 264, size=17, fill=col, lh=21,
               max_lines=2, weight="700")
        if i == 1:
            c.path(f"M {L} {ry + row_h - 6} L {W - L} {ry + row_h - 6}",
                   stroke=VERM, sw=3.0, marker=None)
            c.text(W - L, ry + row_h + 14, "certain  ·  above this line          "
                                           "has an error rate  ·  below it",
                   size=17, weight="700", fill=VERM, anchor="end")

    # ------------------------------------------------------------ the repaired rule
    ry2 = ly + len(CLASSES) * row_h + 26
    rule_h = 126
    c.rect(L, ry2, tw, rule_h, fill=tint(VERM, 0.10), stroke=VERM, sw=2.0)
    c.text(L + 18, ry2 + 28, "Why the split repairs the gate rule rather than weakening it",
           size=19, weight="700", anchor="start", fill=VERM)
    c.para(L + 18, ry2 + 52,
           "The gate rule is that a mechanical check runs first and cannot be overridden by a model. That is "
           "right for V0 and V1. Applied to V2 it says something absurd — that a model's judgement cannot be "
           "overridden by a model. So “mechanical” now means V0 and V1, a V2 result is a finding routed to "
           "review, and only V0 and V1 failures are absolute. And “deterministic” means for a PINNED input "
           "snapshot: resolving a reference asks a service whose answer changes the day a paper is retracted, "
           "which is a V0 check that is repeatable rather than timeless.",
           tw - 36, size=17, fill=INK, lh=22, max_lines=4)

    # --------------------------------------------------------- one check, four classes
    dy = ry2 + rule_h + 38
    qs = [("Does the reference exist and resolve?", "V0", GREEN),
          ("Does the locator resolve in this representation?", "V0", GREEN),
          ("Does the quoted span match the source digest?", "V0/V1", GREEN),
          ("Does the passage support the sentence?", "V2", ORANGE),
          ("Does the sentence claim more than it supports?", "V2", ORANGE)]
    # Counted, not typed. The heading said "four questions" beside a list of
    # five — in the figure whose subject is that one word was carrying two jobs.
    words = {3: "three", 4: "four", 5: "five", 6: "six"}
    classes = len({cls for _, cls, _ in qs})
    c.text(L, dy, f"One “citation audit” is {words.get(len(qs), len(qs))} questions "
                  f"with {words.get(classes, classes)} different statuses",
           size=21, weight="700", anchor="start")
    qy = dy + 24
    qw = (tw - 4 * 14) / 5
    for i, (q, cls, col) in enumerate(qs):
        c.cell(L + i * (qw + 14), qy, qw, 116, cls, q, accent=col,
               head_size=20, body_size=16, max_body_lines=4)
    c.para(L, qy + 148,
           "Existing is not supporting. The reference-verification measurement already in this repository reports "
           "27 of 33 sources corroborated — that says records exist in public authorities, not that any claim is "
           "supported by them. ACC-76 plants a sentence whose citation is real, resolvable and on topic and does "
           "not support it: the V0 checks must pass and the V2 checks must fail.",
           tw, size=17, fill=MUTE, lh=22, max_lines=3)

    # ------------------------------------------------------------ compiler refusals
    cy = qy + 148 + 3 * 22 + 34
    c.text(L, cy, "What the publication compiler refuses",
           size=21, weight="700", anchor="start")
    cy2 = cy + 24
    refusals = [("no ClaimVersion", "a factual sentence with nothing behind it — ACC-52", VERM),
                ("no VerifiedValue", "a number the value registry does not carry — ACC-53", VERM),
                ("unsupported", "a real citation that does not support the sentence — ACC-76", ORANGE),
                ("unqualified judge", "a V2 verdict with no current qualification — ACC-61", ORANGE)]
    rw = (tw - 3 * 16) / 4
    for i, (head, body, col) in enumerate(refusals):
        c.cell(L + i * (rw + 16), cy2, rw, 100, head, body, accent=col,
               head_size=18, body_size=16, max_body_lines=3)
    c.para(L, cy2 + 134,
           "Structural and editorial text is marked with a text_role and passes, so the check discriminates "
           "rather than blocking all prose. A declared rounding of a registered value passes and records its "
           "display transform. A verifier that fails everything is not a verifier, which is why every critical "
           "detector carries a known-positive that must fail and a known-negative that must pass — and the suite "
           "fails if a planted control stays silent.",
           tw, size=17, fill=INK, lh=22, max_lines=4)

    ny = cy2 + 114 + 4 * 22 + 22
    c.para(L, ny,
           "Status: no verifier is built and none is qualified. The V0 checks that run today — the plan seal, "
           "the evidence attestation, the reference resolver — are reclassified by this taxonomy, not created "
           "by it.",
           tw, size=16, fill=MUTE, lh=21, max_lines=2)

    out = ROOT / "docs" / "figures" / "aethrion_assurance.svg"
    out.write_text(c.render(), encoding="utf-8")
    print(f"wrote docs/figures/aethrion_assurance.svg  ({W}×{H})")


if __name__ == "__main__":
    main()
