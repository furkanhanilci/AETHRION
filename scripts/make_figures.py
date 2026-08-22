#!/usr/bin/env python3
"""Regenerate every publication figure under ``docs/figures``.

Figures are derived artifacts, exactly like the Obsidian mirrors: the canonical
source is the architecture corpus, the generator is version-controlled, and the
SVG is reproducible from a clean checkout. Editing an SVG by hand is therefore a
defect — change the generator.

Run:  python3 scripts/make_figures.py [--check]

``--check`` regenerates into memory and reports drift instead of writing, so CI
can fail when a figure no longer matches its generator.
"""
from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

MODULES = ("fig_lifecycle", "fig_roles", "fig_evidence", "fig_stack")
MIN_FONT_UNITS = 16          # ≈ 6.8 pt when the figure is set 180 mm wide


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    out_dir = ROOT / "docs" / "figures"
    before = {p.name: p.read_bytes() for p in out_dir.glob("*.svg")}

    for name in MODULES:
        importlib.import_module(name).main()

    # Layout is not trusted to the generator that produced it: re-measure the
    # rendered SVG and fail if any string escaped the box it was drawn in.
    import check_figures
    if check_figures.main() != 0:
        print("figure containment check FAILED", file=sys.stderr)
        return 1

    drift = []
    for path in sorted(out_dir.glob("*.svg")):
        if before.get(path.name) != path.read_bytes():
            drift.append(path.name)

    if args.check:
        for name in drift:
            print(f"  drift: {name}")
        print(f"{len(list(out_dir.glob('*.svg')))} figures, {len(drift)} drift entries")
        return 1 if drift else 0

    print(f"{len(list(out_dir.glob('*.svg')))} figures written to docs/figures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
