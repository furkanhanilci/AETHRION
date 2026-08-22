#!/usr/bin/env python3
"""Verify that the agent onboarding guide describes this repository.

Why this exists
    ``AGENTS.md`` is the first thing a new agent or maintainer reads, and it is
    the one document whose whole value is being trustworthy on arrival. A path
    that has moved or a count that has drifted there is worse than the same
    error elsewhere: it is the error a reader has no way to detect, because they
    have nothing else loaded yet.

What it checks
    * Every repository path the guide names in backticks exists.
    * Every ``scripts/*.py`` it tells the reader to run exists.
    * Every number it states about the repository is currently true.

What it cannot check
    Whether the prose is *right*. It confirms the guide points at things that
    exist; it cannot confirm that what it says about them is a fair description.

Exit codes
    0 — the guide matches the repository.  1 — it does not.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ("AGENTS.md", "CLAUDE.md")

# Backticked strings that look like repository paths rather than prose.
PATHISH = re.compile(r"`([A-Za-z0-9_./-][A-Za-z0-9_./ -]*\.(?:py|md|json|txt|yml|svg|toml)|"
                     r"[a-z_]+/[A-Za-z0-9_./ -]*)`")
SCRIPT = re.compile(r"\b(?:python3|uv run python) (scripts/[a-z_]+\.py)")

# Ignore things that are field names, globs, external repos or shell fragments.
IGNORE = re.compile(r"[*<>{}]|^https?:|^obra/|^airl\.|^sha256:|^skills/_vendor/$")


def resolve(raw: str) -> str | None:
    """Map a backticked string onto a repository path, or None if it is prose.

    Guides write paths the way a reader needs them, not the way a filesystem
    does: a bare script name, a command line, a path relative to the plan root.
    Each of those is a real reference and each must resolve.
    """
    text = raw.strip().rstrip("/")
    for prefix in ("uv run python ", "python3 ", "python "):
        if text.startswith(prefix):
            text = text[len(prefix):].split()[0]
    if not text or "*" in text:
        return None
    if (ROOT / text).exists():
        return text
    # A bare script name means scripts/, and a plan-relative path means the plan.
    for base in ("scripts", "planning/commissioning", "docs", "docs/architecture",
                 "planning/commissioning/00_PROGRAM"):
        if (ROOT / base / text).exists():
            return f"{base}/{text}"
    # Anything that still looks like a path is a genuine miss; prose is not.
    return text if ("/" in text or text.endswith((".py", ".md", ".json", ".svg", ".yml"))) else None


def counts() -> dict[str, int]:
    plan = ROOT / "planning" / "commissioning"
    seal = plan / "00_PROGRAM" / "SHA256SUMS.txt"
    return {
        "sealed": len(seal.read_text(encoding="utf-8").strip().splitlines()),
        "packages": len([p for p in plan.rglob("WP-*.md") if re.match(r"^WP-\d{3}_", p.name)]),
        "scenarios": len(list((plan / "12_ACCEPTANCE_SCENARIOS").glob("ACC-*.md"))),
        "skills": len([d for d in (ROOT / "skills").iterdir()
                       if d.is_dir() and (d / "SKILL.md").exists()]),
        "figures": len(list((ROOT / "docs" / "figures").glob("*.svg"))),
        "scripts": len(list((ROOT / "scripts").glob("*.py"))),
        "workstreams": len([d for d in plan.iterdir()
                            if d.is_dir() and (d / "README.md").exists()]),
        # The bundle size is stated in three places in the guides. Derive it
        # from the generated status page rather than from the check list in
        # write_status.py: one row there is produced by a function rather than a
        # subprocess, so counting the list undercounts the bundle by one.
        "checks": len(re.findall(r"^\| .+ \| [✅❌⚠️]",
                                 (ROOT / "docs" / "STATUS.md").read_text(encoding="utf-8"),
                                 re.M)),
    }


# Each rule: a regex over the guide, and the count it must equal.
NUMBERS = [
    (r"\*\*(\d+) files, hash-sealed\*\*", "sealed"),
    (r"(\d+) hash-sealed files", "sealed"),
    (r"WP-000[–-]140, ACC-01[–-](\d+)", "scenarios"),
    (r"(\d+) packages, \d+ scenarios", "packages"),
    (r"\d+ packages, (\d+) scenarios", "scenarios"),
    (r"(\d+) skills — \d+ vendored", "skills"),
    (r"\| (\d+) skills \|", "skills"),
    (r"(\d+) SVG figures", "figures"),
    (r"— (\d+) scripts", "scripts"),
    (r"the (\d+) workstream", "workstreams"),
    (r"must print \*\*(\d+)/\d+\*\*", "checks"),
    (r"must print (\d+)/\d+", "checks"),
    (r"the (\d+)-check bundle", "checks"),
]


def main() -> int:
    real = counts()
    problems: list[str] = []
    checked_paths = checked_scripts = checked_numbers = 0

    for name in GUIDES:
        guide = ROOT / name
        if not guide.exists():
            problems.append(f"{name} is missing — it is the entry point")
            continue
        text = guide.read_text(encoding="utf-8")

        for match in PATHISH.finditer(text):
            raw = match.group(1).strip()
            if IGNORE.search(raw):
                continue
            candidate = resolve(raw)
            if candidate is None:
                continue
            checked_paths += 1
            if not (ROOT / candidate).exists():
                problems.append(f"{name}: path does not exist — {raw}")

        for match in SCRIPT.finditer(text):
            checked_scripts += 1
            if not (ROOT / match.group(1)).exists():
                problems.append(f"{name}: command names a missing script — {match.group(1)}")

        for pattern, key in NUMBERS:
            for match in re.finditer(pattern, text):
                checked_numbers += 1
                stated = int(match.group(1))
                if stated != real[key]:
                    problems.append(
                        f"{name}: says {stated} for {key}, repository has {real[key]}")

    print(f"agent guide: {checked_paths} paths · {checked_scripts} commands · "
          f"{checked_numbers} counts checked")
    for problem in problems:
        print(f"  ✗ {problem}")
    if problems:
        print(f"\n{len(problems)} problem(s) — the entry point does not match the repository")
        return 1
    print("\nthe agent guide matches the repository")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
