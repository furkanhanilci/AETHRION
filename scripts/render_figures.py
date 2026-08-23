#!/usr/bin/env python3
"""Rasterise every figure so a human — or an agent — can actually look at one.

Why this exists
    ``check_figures.py`` measures strings against boxes. It cannot see a
    connector drawn through a heading, a background stripe sitting under the row
    it should be behind, a label overwritten by a panel placed on top of it, or
    a column with three hundred units of dead space beneath it. Those are not
    hypothetical: every one was in this corpus while the checker reported zero
    overflows, and every one was found by rendering the SVG and looking at it.

    The package's own instruction says it plainly: *a successful generator is
    not evidence that the composition is readable.*

What it is not
    Not a check. It produces images and exits; nothing here passes or fails.
    Rendering is the step that makes inspection possible, and inspection is
    still a human act. It is deliberately outside the verification bundle for
    that reason — a bundle row that said "figures rendered" would read as
    "figures reviewed", which is the overclaim this repository exists to refuse.

Renderer
    Headless Chrome, because it is the one SVG engine already present on this
    machine and it renders the same font metrics the browser will. If it is
    absent the script says so and exits non-zero rather than pretending.

Usage
    python3 scripts/render_figures.py [--out DIR]
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "docs" / "figures"
VIEWBOX = re.compile(r'viewBox="0 0 (\d+) (\d+)"')
CANDIDATES = ("google-chrome", "chromium", "chromium-browser", "google-chrome-stable")


def browser() -> str | None:
    return next((c for c in CANDIDATES if shutil.which(c)), None)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None,
                        help="directory for the PNGs (default: a temp dir, printed)")
    args = parser.parse_args()

    exe = browser()
    if exe is None:
        print("no headless browser found — looked for: " + ", ".join(CANDIDATES),
              file=sys.stderr)
        print("figures were NOT rendered, and this is reported rather than skipped",
              file=sys.stderr)
        return 1

    out = Path(args.out) if args.out else Path("/tmp") / "aethrion-figures"
    out.mkdir(parents=True, exist_ok=True)

    figures = sorted(FIGURES.glob("*.svg"))
    for figure in figures:
        found = VIEWBOX.search(figure.read_text(encoding="utf-8"))
        if not found:
            print(f"  ✗ {figure.name}: no viewBox, cannot size the render")
            continue
        width, height = (int(v) for v in found.groups())
        subprocess.run(
            [exe, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             f"--screenshot={out / (figure.stem + '.png')}",
             f"--window-size={width},{height + 16}", f"file://{figure}"],
            capture_output=True, timeout=180)

    print(f"{len(figures)} figures rendered to {out} using {exe}")
    print("Nothing here is a check. Open them and look — the defects this step "
          "exists for are the ones no measurement catches: a line through a "
          "heading, a panel over a label, a column of dead space.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
