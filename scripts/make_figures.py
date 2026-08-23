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

MODULES = (
    "fig_lifecycle",
    "fig_roles",
    "fig_evidence",
    "fig_stack",
    "fig_reporting",
    "fig_waves",
    "fig_trust",
    "fig_verification",
    "fig_topology",
    "fig_discovery",
    "fig_memory",
    "fig_assurance",
    "fig_collaboration",
    "fig_authority",
    "fig_backend",
    "fig_runtime",
    # These five existed as generators and were never in this list. The drift
    # check ran over every SVG in the directory and reported "21 figures, 0
    # drift" while regenerating sixteen of them — so five figures could be
    # edited by hand, or left stale by a change to their generator, and the
    # bundle would agree with itself. Found when an edit to fig_context.py
    # produced no change in the figure it draws.
    "fig_compiler",
    "fig_context",
    "fig_decision",
    "fig_disciplines",
    "fig_reproduction",
)
MIN_FONT_UNITS = 16          # ≈ 6.8 pt when the figure is set 180 mm wide


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    out_dir = ROOT / "docs" / "figures"
    before = {p.name: p.read_bytes() for p in out_dir.glob("*.svg")}

    # A generator absent from MODULES is a figure this command silently does not
    # produce, and the drift check below cannot tell that apart from a figure
    # that did not change. The list is therefore checked against the directory
    # rather than trusted.
    generators = {p.stem for p in (ROOT / "scripts").glob("fig_*.py")} - {"figure_kit"}
    unlisted = sorted(generators - set(MODULES))
    if unlisted:
        print(f"generators not in MODULES, so never run: {unlisted}", file=sys.stderr)
        return 1

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
