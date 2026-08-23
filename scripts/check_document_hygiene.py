#!/usr/bin/env python3
"""Structural defects in governed documents, reported as distinct error codes.

Responsibility
    The other checkers ask whether a document says something *false*. This one
    asks whether it is *well-formed*: a heading emitted twice, a relative link
    that resolves to nothing, a generated block opened and never closed, a
    companion document whose package no longer exists.

    None of these makes a plan unsafe on its own, and that is exactly why they
    accumulate. Nineteen package documents carried the heading
    ``## Dependency and prerequisite analysis`` twice — once written by hand and
    once emitted by the generator above its marker — and regenerated cleanly
    forever, because the drift check compares only what is *inside* a marker.

Distinct codes, on purpose
    ``DUPLICATE_HEADING``, ``BROKEN_RELATIVE_LINK``, ``UNBALANCED_GENERATED_MARKER``,
    ``ORPHAN_COMPANION``, ``MISSING_COMPANION``. One code per defect class so CI
    output can be triaged rather than read start to finish, and so a rule can be
    seen to fire on its own kind.

What it deliberately does not scan
    ``data/`` holds projection backups full of ``zotero://`` URIs, and the
    vendored skills are upstream's to keep well-formed. A checker that reports
    sixty-six findings about backup files is a checker that gets muted.

Exit codes
    0 — no structural defect.  1 — at least one, grouped by code.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = ("vault_baseline", ".venv", ".git", "skills/_vendor", "data/",
        "delivery/specimen", "node_modules")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
EXTERNAL = ("http://", "https://", "mailto:", "zotero://", "obsidian://", "#")
OPEN_MARKER = re.compile(r"<!--\s*generated:([a-z-]+)\s")
CLOSE_MARKER = re.compile(r"<!--\s*/generated:([a-z-]+)\s*-->")


def vendored_skills() -> set[str]:
    """Skills copied verbatim from upstream, identified by their own metadata.

    `CLAUDE.md`: *"Do not rewrite the vendored eleven. They keep upstream
    attribution, their licence and their pinned commit; changes belong upstream
    or in a native skill."* A hygiene finding inside one of them is a finding
    against `obra/superpowers`, and fixing it here would silently fork a file
    that claims to be byte-identical to a named commit.

    Read from the skill's `airl.upstream_repository` rather than from a list
    kept here, so vendoring a twelfth skill does not require remembering this.
    """
    out = set()
    skills = ROOT / "skills"
    if not skills.exists():
        return out
    for skill in skills.iterdir():
        card = skill / "SKILL.md"
        if card.exists() and "airl.upstream_repository" in card.read_text(
                encoding="utf-8", errors="replace"):
            out.add(f"skills/{skill.name}/")
    return out


def governed() -> list[Path]:
    skip = SKIP + tuple(sorted(vendored_skills()))
    return [p for p in sorted(ROOT.rglob("*.md"))
            if not any(s in str(p.relative_to(ROOT)) for s in skip)]


def audit(paths: list[Path] | None = None) -> dict[str, list[str]]:
    found: dict[str, list[str]] = defaultdict(list)
    paths = paths if paths is not None else governed()

    for path in paths:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()

        # DUPLICATE_HEADING — the same H2/H3 twice in one document.
        seen: dict[str, int] = {}
        for number, line in enumerate(lines, 1):
            if not re.match(r"^#{2,3} \S", line):
                continue
            key = line.strip()
            if key in seen:
                found["DUPLICATE_HEADING"].append(
                    f"{rel}:{number}  {key!r} — first written at line {seen[key]}")
            else:
                seen[key] = number

        # BROKEN_RELATIVE_LINK
        for match in LINK.finditer(text):
            target = match.group(1)
            if target.startswith(EXTERNAL):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not (path.parent / target).exists():
                number = text[:match.start()].count("\n") + 1
                found["BROKEN_RELATIVE_LINK"].append(f"{rel}:{number}  → {target}")

        # UNBALANCED_GENERATED_MARKER
        opened = OPEN_MARKER.findall(text)
        closed = CLOSE_MARKER.findall(text)
        for name in sorted(set(opened) | set(closed)):
            if opened.count(name) != closed.count(name):
                found["UNBALANCED_GENERATED_MARKER"].append(
                    f"{rel}  generated:{name} opened {opened.count(name)}×, "
                    f"closed {closed.count(name)}× — a block that is never "
                    f"closed swallows everything after it into generated space")

    # ORPHAN_COMPANION / MISSING_COMPANION
    plan = ROOT / "planning" / "commissioning"
    cards = {p.name[:6] for p in plan.rglob("WP-*.md")
             if re.match(r"^WP-\d{3}_", p.name)
             and not p.name.endswith((".tests.md", ".acceptance.md"))}
    for suffix in (".tests.md", ".acceptance.md"):
        companions = {p.name[:6]: p for p in plan.rglob(f"WP-*{suffix}")}
        for pid, p in sorted(companions.items()):
            if pid not in cards:
                found["ORPHAN_COMPANION"].append(
                    f"{p.relative_to(ROOT)} — no card named {pid} exists")
        for pid in sorted(cards - set(companions)):
            found["MISSING_COMPANION"].append(f"{pid} has no {suffix} companion")
    return dict(found)


# ----------------------------------------------------------------- self-test
SPECIMENS = {
    "DUPLICATE_HEADING":
        "# Doc\n\n## Analysis\n\ntext\n\n## Analysis\n\nmore\n",
    "BROKEN_RELATIVE_LINK":
        "# Doc\n\nSee [the plan](./no_such_file_anywhere.md).\n",
    "UNBALANCED_GENERATED_MARKER":
        "# Doc\n\n<!-- generated:thing — produced by x; do not edit -->\n\nbody\n",
}
# The clean specimen lives in a temporary directory inside the repository, so
# its relative link must resolve from there. The first version pointed two
# levels up and landed outside the repository — the rule was right and the
# specimen was wrong, which the self-test reported as the rule being noisy.
CLEAN = (
    "# Doc\n\n## Analysis\n\nSee [the guide](../AGENTS.md) and "
    "[an anchor](#analysis).\n\n"
    "<!-- generated:thing — produced by x; do not edit -->\nbody\n"
    "<!-- /generated:thing -->\n\n### Analysis\n"
)


def self_test() -> int:
    """Each code must fire on a document written to trip it, and stay quiet otherwise."""
    import tempfile
    silent, noisy = [], []
    with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
        folder = Path(tmp)
        for code, body in SPECIMENS.items():
            probe = folder / f"{code.lower()}.md"
            probe.write_text(body, encoding="utf-8")
            if code not in audit([probe]):
                silent.append(code)
            probe.unlink()
        probe = folder / "clean.md"
        probe.write_text(CLEAN, encoding="utf-8")
        for code in audit([probe]):
            if code in SPECIMENS:
                noisy.append(code)
    print(f"{len(SPECIMENS)} defect specimens injected · {len(silent)} undetected · "
          f"{len(noisy)} rule(s) fired on a well-formed document")
    for code in silent:
        print(f"  ✗ {code} did not fire on a document written to trip it")
    for code in noisy:
        print(f"  ✗ {code} fired on the clean specimen")
    if silent or noisy:
        return 1
    print("every hygiene code was observed firing, and none fired on clean prose")
    return 0


def main() -> int:
    if "--self-test" in sys.argv[1:]:
        return self_test()
    paths = governed()
    found = audit(paths)
    total = sum(len(v) for v in found.values())
    print(f"{len(paths)} governed documents · {len(SPECIMENS) + 2} defect classes")
    for code in sorted(found):
        print(f"  ✗ {code} ({len(found[code])})")
        for item in found[code][:10]:
            print(f"      {item}")
        if len(found[code]) > 10:
            print(f"      … and {len(found[code]) - 10} more")
    if total:
        print(f"\n{total} structural defect(s)")
        return 1
    print("no duplicate heading, broken relative link, unbalanced generated "
          "marker or orphaned companion in any governed document")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
