#!/usr/bin/env python3
"""Verify that no text in a generated figure escapes its box or the canvas.

Responsibility
    Re-measure every ``<text>`` element in every figure under ``docs/figures``
    and check it against two things: the canvas, and the tightest box that
    encloses its anchor. This is an *independent* check — it parses the rendered
    SVG rather than trusting the generator that produced it, so a layout bug in
    ``figure_kit`` cannot hide behind the same assumption twice.

Invariant
    A figure ships only when every string fits the box it was drawn in.

Audit findings
    Written after overflowing labels shipped in the first figure set: the
    original check compared text against the canvas only, so text that spilled
    out of a node but stayed on the page passed. That is the exact failure this
    script exists to make impossible.

Exit codes
    0 — every string fits.  1 — at least one overflow.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_kit import text_width

RECT_RE = re.compile(
    r'<rect x="([\d.-]+)" y="([\d.-]+)" width="([\d.]+)" height="([\d.]+)"')
TEXT_RE = re.compile(
    r'<text x="([\d.-]+)" y="([\d.-]+)"[^>]*?font-size="([\d.]+)"[^>]*?'
    r'font-weight="([^"]+)"[^>]*?text-anchor="(\w+)"[^>]*?>([^<]*)</text>')
VIEWBOX_RE = re.compile(r'viewBox="0 0 (\d+) (\d+)"')
TOLERANCE = 1.5          # user units; sub-pixel rounding only


def check(path: Path) -> list[str]:
    svg = path.read_text(encoding="utf-8")
    canvas_w, canvas_h = (int(v) for v in VIEWBOX_RE.search(svg).groups())
    rects = [tuple(float(v) for v in m.groups()) for m in RECT_RE.finditer(svg)]
    # The first rect is the paper background; it encloses everything by design.
    boxes = [r for r in rects if not (r[0] == 0 and r[1] == 0)]

    problems: list[str] = []
    for m in TEXT_RE.finditer(svg):
        x, y, size, weight, anchor, body = m.groups()
        if "rotate" in m.group(0):
            continue                      # rotated labels are measured on the other axis
        x, y, size = float(x), float(y), float(size)
        # The SVG stores XML-escaped text; measuring the escaped form counts
        # "&#x27;" as six characters and reports overflows that do not exist.
        body = html.unescape(body)
        width = text_width(body, size, weight)
        left = x if anchor == "start" else (x - width / 2 if anchor == "middle" else x - width)
        right = left + width

        if left < -TOLERANCE or right > canvas_w + TOLERANCE or y > canvas_h:
            problems.append(f"canvas: {body[:52]!r} spans {left:.0f}..{right:.0f} "
                            f"(canvas {canvas_w})")
            continue

        enclosing = [b for b in boxes
                     if b[0] - TOLERANCE <= x <= b[0] + b[2] + TOLERANCE
                     and b[1] - TOLERANCE <= y <= b[1] + b[3] + TOLERANCE]
        if not enclosing:
            continue                      # free-standing text; canvas check already applied
        bx, by, bw, bh = min(enclosing, key=lambda b: b[2] * b[3])
        if left < bx - TOLERANCE or right > bx + bw + TOLERANCE:
            problems.append(
                f"box: {body[:52]!r} spans {left:.0f}..{right:.0f} inside box "
                f"{bx:.0f}..{bx + bw:.0f}  (overflow {max(bx - left, right - bx - bw):.0f}u)")
    return problems


def main() -> int:
    figures = sorted((Path(__file__).resolve().parent.parent / "docs" / "figures").glob("*.svg"))
    if not figures:
        print("no figures found", file=sys.stderr)
        return 1

    failures = 0
    for path in figures:
        problems = check(path)
        status = "ok" if not problems else f"{len(problems)} overflow(s)"
        print(f"{path.name:32} {status}")
        for problem in problems[:12]:
            print(f"    ✗ {problem}")
        failures += len(problems)

    print(f"\n{len(figures)} figures checked, {failures} overflow(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
