#!/usr/bin/env python3
"""Generate the Obsidian reading mirror of the canonical commissioning plan.

The canonical plan lives in ``planning/commissioning/``. The Obsidian tree under
``<vault>/10 - Projects/AETHRION/01 - Commissioning/`` is a
**generated** reading copy: content changes go into the canonical file first and
propagate from here. Editing the mirror directly creates a divergence the plan
seal cannot detect, because the seal does not cover the mirror.

Usage:
    python scripts/mirror_plan.py <target-commissioning-dir> [--check]

``--check`` writes nothing and exits non-zero if the mirror differs from what
would be generated (the drift check intended for CI).
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CANON = REPO / "planning" / "commissioning"

# Files copied verbatim so that the mirror can be integrity-checked too.
VERBATIM = {"00_PROGRAM/package_dependency_matrix.csv", "00_PROGRAM/SHA256SUMS.txt"}


def mirror_name(rel: Path) -> str:
    """Map a canonical file name onto its Obsidian mirror name."""
    name = rel.name
    if name == "README.md":
        return "commissioning_index.md" if rel.parent == Path(".") else name
    m = re.match(r"^(WP|ACC)-(\d+)_(.+\.md)$", name)
    if m:
        return f"{m.group(1).lower()}_{m.group(2)}_{m.group(3)}"
    return name


def rewrite_links(text: str) -> str:
    """Rewrite intra-plan links to the mirror naming convention."""
    def repl(match: re.Match[str]) -> str:
        prefix, kind, num, tail = match.groups()
        return f"{prefix}{kind.lower()}_{num}_{tail}"

    return re.sub(r"(\]\([^)]*?/)(WP|ACC)-(\d+)_([^)]+\.md\))", repl, text)


def build() -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    for src in sorted(CANON.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(CANON)
        if rel.as_posix() in VERBATIM:
            out[(rel.parent / mirror_name(rel)).as_posix()] = src.read_bytes()
            continue
        if src.suffix != ".md":
            continue
        text = rewrite_links(src.read_text(encoding="utf-8"))
        out[(rel.parent / mirror_name(rel)).as_posix()] = text.encode("utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--force", action="store_true",
                        help="replace the target even if it holds files this mirror "
                             "does not generate; this deletes them")
    args = parser.parse_args()

    generated = build()
    target: Path = args.target

    if args.check:
        drift: list[str] = []
        existing = {
            p.relative_to(target).as_posix()
            for p in target.rglob("*")
            if p.is_file()
        }
        for rel, payload in generated.items():
            path = target / rel
            if not path.exists():
                drift.append(f"missing: {rel}")
            elif path.read_bytes() != payload:
                drift.append(f"differs: {rel}")
        for rel in sorted(existing - set(generated)):
            drift.append(f"extra:   {rel}")
        for line in drift:
            print(line)
        print(f"{len(generated)} generated files, {len(drift)} drift entries")
        return 1 if drift else 0

    if target.exists():
        # This script replaces the target wholesale, so a mistyped path is a
        # data-loss event rather than a failed run. Refuse any directory that
        # holds files this mirror did not generate: an existing mirror is a
        # subset of `generated`, anything else is somebody's data.
        strays = sorted(
            p.relative_to(target).as_posix()
            for p in target.rglob("*")
            if p.is_file() and p.relative_to(target).as_posix() not in generated
        )
        if strays and not args.force:
            print(f"refusing to replace {target}", file=sys.stderr)
            print(
                f"  it holds {len(strays)} file(s) this mirror does not generate, "
                "so it is not a plan mirror:",
                file=sys.stderr,
            )
            for rel in strays[:5]:
                print(f"    {rel}", file=sys.stderr)
            if len(strays) > 5:
                print(f"    ... and {len(strays) - 5} more", file=sys.stderr)
            print(
                "  the plan mirror lives at "
                "'<vault>/10 - Projects/AETHRION/01 - Commissioning'; "
                "pass --force only if you mean to delete the files listed above.",
                file=sys.stderr,
            )
            return 2
        shutil.rmtree(target)
    for rel, payload in generated.items():
        path = target / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    print(f"wrote {len(generated)} files to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
