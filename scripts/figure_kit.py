#!/usr/bin/env python3
"""Dependency-free SVG primitives with real text metrics, for the AIRL-OS figures.

Responsibility
    Provide the smallest drawing layer that can *guarantee* text fits the box it
    is drawn in. Every figure under ``docs/figures`` is generated from source
    rather than hand-drawn, so a caption that overflows its node is a bug in this
    module or its callers — never something to nudge by hand in the SVG.

Invariant
    ``Canvas.cell`` never emits text wider than the box it was given. It wraps
    first, then shrinks toward ``MIN_SIZE``, and if the text still does not fit
    it raises. A figure that cannot be laid out honestly fails the build instead
    of shipping broken.

Why the metrics are here
    An SVG has no layout engine, so the generator must measure text itself. The
    table below is the Helvetica AFM advance-width set (units per 1000 em), which
    matches the rendering of the Helvetica/Arial/Liberation/DejaVu stack closely
    enough for layout decisions with a safety margin applied.

Design constants
    Canvases are capped at 1200 user units so that, set 180 mm wide, one unit is
    ~0.425 pt. ``MIN_SIZE`` 16 therefore lands at ~6.8 pt, the floor for
    publication figure text.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from html import escape

# Okabe–Ito, chosen for colour-vision safety.
BLUE = "#0072B2"      # model production
ORANGE = "#E69F00"    # frozen artifact
GREEN = "#009E73"     # mechanical check
VERM = "#D55E00"      # human authority
PURPLE = "#CC79A7"    # revision / feedback
SKY = "#56B4E9"       # supporting
INK = "#1A1A1A"
MUTE = "#63666A"
RULE = "#C8C8C8"
PAPER = "#FFFFFF"

FONT = "Helvetica, Arial, 'Liberation Sans', 'DejaVu Sans', sans-serif"
MONO = "'DejaVu Sans Mono', 'Liberation Mono', Menlo, monospace"

MIN_SIZE = 16.0
PAD = 14.0            # horizontal padding inside a cell
SAFETY = 1.03         # metrics margin: real stacks vary slightly from Helvetica

# Helvetica advance widths, units per 1000 em.
_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667, "'": 191,
    "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333, ".": 278, "/": 278,
    ":": 278, ";": 278, "<": 584, "=": 584, ">": 584, "?": 556, "@": 1015,
    "[": 278, "\\": 278, "]": 278, "^": 469, "_": 556, "`": 333,
    "{": 334, "|": 260, "}": 334, "~": 584,
    "A": 667, "B": 667, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778, "H": 722,
    "I": 278, "J": 500, "K": 667, "L": 556, "M": 833, "N": 722, "O": 778, "P": 667,
    "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722, "V": 667, "W": 944, "X": 667,
    "Y": 667, "Z": 611,
    "a": 556, "b": 556, "c": 500, "d": 556, "e": 556, "f": 278, "g": 556, "h": 556,
    "i": 222, "j": 222, "k": 500, "l": 222, "m": 833, "n": 556, "o": 556, "p": 556,
    "q": 556, "r": 333, "s": 500, "t": 278, "u": 556, "v": 500, "w": 722, "x": 500,
    "y": 500, "z": 500,
    "—": 1000, "–": 556, "·": 278, "×": 584, "≈": 549, "→": 1000, "≤": 549, "≥": 549,
}
for _d in "0123456789":
    _W[_d] = 556


def text_width(s: str, size: float, weight: str = "400") -> float:
    """Advance width of ``s`` in user units, with a small safety margin."""
    total = sum(_W.get(ch, 600) for ch in s)
    bold = 1.055 if weight in ("600", "700", "bold") else 1.0
    return total / 1000.0 * size * bold * SAFETY


def wrap(text: str, size: float, max_w: float, weight: str = "400") -> list[str]:
    """Greedy word wrap. Long single words are kept whole and reported by fit()."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if cur and text_width(trial, size, weight) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines or [""]


def fit(text: str, max_w: float, size: float, weight: str = "400",
        max_lines: int = 3, min_size: float = MIN_SIZE) -> tuple[list[str], float]:
    """Wrap, then shrink, until the text fits ``max_w`` in at most ``max_lines``.

    Raises when it cannot: a figure that will not lay out honestly must fail the
    build rather than ship with clipped text.
    """
    current = size
    while current >= min_size:
        lines = wrap(text, current, max_w, weight)
        if len(lines) <= max_lines and all(
                text_width(line, current, weight) <= max_w for line in lines):
            return lines, current
        current -= 0.5
    lines = wrap(text, min_size, max_w, weight)
    widest = max(text_width(line, min_size, weight) for line in lines)
    raise ValueError(
        f"cannot fit {text!r} into {max_w:.0f}u in {max_lines} lines at >= "
        f"{min_size}u (needs {len(lines)} lines, widest {widest:.0f}u)")


def tint(hex_colour: str, alpha: float) -> str:
    """Blend a hue toward paper white so black body text keeps its contrast."""
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    r, g, b = (round(c + (255 - c) * (1 - alpha)) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


@dataclass
class Canvas:
    width: int
    height: int
    parts: list[str] = field(default_factory=list)

    # ---- primitives -------------------------------------------------------
    def rect(self, x, y, w, h, fill=PAPER, stroke=INK, sw=1.6, rx=4, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def text(self, x, y, s, size=18, fill=INK, anchor="middle", weight="400",
             family=FONT, style="normal"):
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size:g}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(s)}</text>')

    def para(self, x, y, text_, max_w, size=17, fill=MUTE, weight="400",
             lh=None, anchor="start", max_lines=6) -> float:
        """Left-aligned wrapped paragraph. Returns the y after the last line."""
        lines, sz = fit(text_, max_w, size, weight, max_lines=max_lines)
        step = lh or sz + 6
        for i, line in enumerate(lines):
            self.text(x, y + i * step, line, size=sz, fill=fill, anchor=anchor, weight=weight)
        return y + (len(lines) - 1) * step

    def path(self, d, stroke=INK, sw=1.6, dash=None, marker="arrow", fill="none"):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker})"' if marker else ""
        self.parts.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"{da}{mk}/>')

    def hrule(self, x1, x2, y, stroke=RULE, sw=1.0, dash=None):
        self.path(f"M {x1} {y} L {x2} {y}", stroke=stroke, sw=sw, dash=dash, marker=None)

    def hatch(self, x, y, w, h, colour=MUTE):
        self.parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" '
            f'fill="url(#hatch)" stroke="{colour}" stroke-width="1.3" stroke-dasharray="4 3"/>')

    # ---- composites -------------------------------------------------------
    def cell(self, x, y, w, h, head: str, body: str = "", accent=BLUE, *,
             dash=None, sw=1.6, fill=None, head_size=18, body_size=16,
             head_weight="600", head_fill=INK, body_fill=MUTE, draw_box=True,
             max_head_lines=2, max_body_lines=2, stroke_override=None):
        """A box whose text is guaranteed to fit inside it.

        Text is wrapped and shrunk against the *inner* width, never the canvas,
        which is the check that was missing when these figures first shipped.
        """
        if draw_box:
            self.rect(x, y, w, h, fill=fill if fill else tint(accent, 0.13),
                      stroke=stroke_override or accent, sw=sw, dash=dash)
        inner = w - 2 * PAD
        head_lines, hs = fit(head, inner, head_size, head_weight, max_lines=max_head_lines)
        body_lines, bs = ([], body_size)
        if body:
            body_lines, bs = fit(body, inner, body_size, "400", max_lines=max_body_lines)
        head_step, body_step = hs + 4, bs + 3
        block = len(head_lines) * head_step + (len(body_lines) * body_step + 4 if body_lines else 0)
        cy = y + (h - block) / 2 + hs * 0.82
        cx = x + w / 2
        for line in head_lines:
            self.text(cx, cy, line, size=hs, weight=head_weight, fill=head_fill)
            cy += head_step
        if body_lines:
            cy += 2
            for line in body_lines:
                self.text(cx, cy, line, size=bs, fill=body_fill)
                cy += body_step

    def render(self) -> str:
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="100%" role="img">\n<defs>\n'
            '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto-start-reverse">\n'
            '    <path d="M 0 1 L 9 5 L 0 9 z" fill="context-stroke"/>\n  </marker>\n'
            '  <marker id="arrowsm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" '
            'markerHeight="5.5" orient="auto-start-reverse">\n'
            '    <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="context-stroke"/>\n  </marker>\n'
            '  <pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">\n'
            f'    <line x1="0" y1="0" x2="0" y2="7" stroke="{RULE}" stroke-width="2.2"/>\n'
            '  </pattern>\n</defs>\n'
            f'<rect width="{self.width}" height="{self.height}" fill="{PAPER}"/>\n')
        return head + "\n".join(self.parts) + "\n</svg>\n"
