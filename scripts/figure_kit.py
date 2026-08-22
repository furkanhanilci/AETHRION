#!/usr/bin/env python3
"""Dependency-free SVG primitives for the AIRL-OS publication figures.

Responsibility
    Provide the smallest possible drawing layer — boxes, lanes, orthogonal
    connectors, text — so that every figure in ``docs/figures`` is generated
    deterministically from source rather than hand-drawn and hand-maintained.

Invariant
    Figures are *derived artifacts*. Nothing here invents content: every visible
    string in a figure comes from the calling module, which in turn takes it
    from the architecture documents. A figure that says something the corpus
    does not say is a defect, not a design choice.

Design constants
    Canvas widths are capped at 1200 user units so that, scaled to a 180 mm
    double-column figure, one user unit is ~0.425 pt. The minimum font size used
    anywhere is therefore 17 units ≈ 7.2 pt, which is the floor most publishers
    accept for figure text.

Palette
    Okabe–Ito, chosen for colour-vision deficiency safety. Colour is never the
    only channel: actor class is additionally encoded by row position, and build
    status by stroke pattern (solid = working, dashed = specified, not built).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from html import escape

# Okabe–Ito
BLUE = "#0072B2"      # model
ORANGE = "#E69F00"    # frozen artifact
GREEN = "#009E73"     # mechanical
VERM = "#D55E00"      # human authority
PURPLE = "#CC79A7"    # feedback / revision
SKY = "#56B4E9"       # supporting
INK = "#1A1A1A"
MUTE = "#6B6B6B"
RULE = "#C8C8C8"
PAPER = "#FFFFFF"

FONT = "'Helvetica Neue', Helvetica, Arial, 'DejaVu Sans', sans-serif"
MONO = "'SF Mono', 'DejaVu Sans Mono', Menlo, monospace"


def tint(hex_colour: str, alpha: float) -> str:
    """Blend a hue toward paper white; keeps fills light enough for black text."""
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    r, g, b = (round(c + (255 - c) * (1 - alpha)) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


@dataclass
class Canvas:
    width: int
    height: int
    parts: list[str] = field(default_factory=list)

    # -- primitives ---------------------------------------------------------
    def rect(self, x, y, w, h, fill=PAPER, stroke=INK, sw=1.6, rx=4, dash=None, opacity=1.0):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def text(self, x, y, s, size=19, fill=INK, anchor="middle", weight="400",
             family=FONT, spacing=0, style="normal"):
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}">{escape(s)}</text>')

    def lines(self, x, y, rows, size=17, fill=INK, anchor="middle", lh=21, weight="400"):
        for i, row in enumerate(rows):
            self.text(x, y + i * lh, row, size=size, fill=fill, anchor=anchor, weight=weight)

    def path(self, d, stroke=INK, sw=1.6, dash=None, marker="arrow", fill="none", opacity=1.0):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker})"' if marker else ""
        self.parts.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-opacity="{opacity}" stroke-linecap="round" stroke-linejoin="round"{da}{mk}/>')

    def hrule(self, x1, x2, y, stroke=RULE, sw=1.0, dash=None):
        self.path(f"M {x1} {y} L {x2} {y}", stroke=stroke, sw=sw, dash=dash, marker=None)

    def hatch(self, x, y, w, h, colour=MUTE):
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="url(#hatch)" '
            f'stroke="{colour}" stroke-width="1.2" stroke-dasharray="4 3"/>')

    # -- composites ---------------------------------------------------------
    def node(self, x, y, w, h, title, sub=(), accent=BLUE, dash=None, sw=1.8,
             title_size=19, sub_size=16, fill_alpha=0.16):
        self.rect(x, y, w, h, fill=tint(accent, fill_alpha), stroke=accent, sw=sw, dash=dash)
        cx = x + w / 2
        block = 1 + len(sub)
        top = y + h / 2 - (block - 1) * 10 + 6
        self.text(cx, top, title, size=title_size, weight="600")
        for i, s in enumerate(sub):
            self.text(cx, top + 20 + i * 18, s, size=sub_size, fill=MUTE)

    def render(self) -> str:
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="100%" role="img">\n'
            '<defs>\n'
            '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto-start-reverse">\n'
            '    <path d="M 0 1 L 9 5 L 0 9 z" fill="context-stroke"/>\n  </marker>\n'
            '  <marker id="arrowsm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" '
            'markerHeight="5.5" orient="auto-start-reverse">\n'
            '    <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="context-stroke"/>\n  </marker>\n'
            '  <pattern id="hatch" width="7" height="7" patternTransform="rotate(45)" '
            'patternUnits="userSpaceOnUse">\n'
            f'    <line x1="0" y1="0" x2="0" y2="7" stroke="{RULE}" stroke-width="2.2"/>\n'
            '  </pattern>\n'
            '</defs>\n'
            f'<rect width="{self.width}" height="{self.height}" fill="{PAPER}"/>\n')
        return head + "\n".join(self.parts) + "\n</svg>\n"
