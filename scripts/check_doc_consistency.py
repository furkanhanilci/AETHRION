#!/usr/bin/env python3
"""Check that documents agree with the repository, and with themselves.

Responsibility
    Two failure classes are checked here, both of which a hash seal, a link
    checker and a schema validator all miss:

    1. **Declared counts that drift from reality.** A document says "46
       scenarios" while 51 exist. Nothing is corrupt; the prose is simply wrong.
    2. **A document that contradicts its own header.** A decision record whose
       status says ACCEPTED while its summary still says the decision field is
       blank.

Invariant
    Any number a document states about the repository is derived from the
    repository when the document is touched — never remembered.

Audit findings
    An external readiness review found both classes in this corpus: the
    commissioning inventory kept "46" after the range moved to ACC-51, because a
    later edit changed the range and broke the exact match the count edit
    depended on; and ADR-001's summary still described its own decision as
    unmade after it had been taken. Both are exactly the drift
    `docs/DOCUMENT_STANDARD.md` §3 rule 2 forbids, so the rule now has a check.

Exit codes
    0 — documents agree with the repository and with themselves.  1 — drift.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"


def derive() -> dict[str, int]:
    """Ground truth, computed rather than recalled."""
    packages = [p for p in PLAN.rglob("WP-*.md") if re.match(r"^WP-\d{3}_", p.name)]
    scenarios = [p for p in (PLAN / "12_ACCEPTANCE_SCENARIOS").glob("ACC-*.md")
                 if re.match(r"^ACC-\d{2}_", p.name)]
    skills = [d for d in (ROOT / "skills").iterdir()
              if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").exists()]
    seal = (PLAN / "00_PROGRAM" / "SHA256SUMS.txt").read_text().strip().splitlines()
    markdown = list(PLAN.rglob("*.md"))
    figures = list((ROOT / "docs" / "figures").glob("*.svg"))
    numbered = [p for p in packages if p.name != "WP-000_interim_evidence_policy.md"]
    return {
        "packages": len(numbered),            # WP-001..140, excluding the bootstrap
        "package_documents": len(packages),   # including WP-000
        "scenarios": len(scenarios),
        "skills": len(skills),
        "sealed": len(seal),
        "plan_markdown": len(markdown),
        "figures": len(figures),
        "highest_scenario": max(int(p.name[4:6]) for p in scenarios),
    }


# (file, regex with one capturing group, truth key, human description)
RULES: list[tuple[str, str, str, str]] = [
    ("planning/commissioning/README.md",
     r"\| Work packages \| \*\*(\d+)\*\*", "packages", "work packages"),
    ("planning/commissioning/README.md",
     r"\| Work package documents in total \| \*\*(\d+)\*\*", "package_documents", "package documents"),
    ("planning/commissioning/README.md",
     r"\| Acceptance scenarios \| \*\*(\d+)\*\*", "scenarios", "acceptance scenarios"),
    ("planning/commissioning/README.md",
     r"\| Markdown files under this tree \| (\d+) \|", "plan_markdown", "plan markdown files"),
    ("planning/commissioning/README.md",
     r"\| Files covered by the hash seal \| (\d+) ", "sealed", "sealed files"),
    ("README.md", r"(\d+) package documents, \d+ scenarios", "package_documents", "package documents"),
    ("README.md", r"\d+ package documents, (\d+) scenarios", "scenarios", "acceptance scenarios"),
    ("README.md", r"Skill registry \((\d+) skills", "skills", "skills"),
    ("README.md", r"plan seal (\d+)/\d+", "sealed", "sealed files"),
    ("README.md", r"Skills: (\d+)/\d+ conform", "skills", "skills"),
    ("README.md", r"Figures: (\d+)/\d+ match", "figures", "figures"),
    ("skills/README.md", r"All (\d+) conform to the Agent Skills", "skills", "skills"),
    ("skills/README.md", r"\| Scope \| All (\d+) skills", "skills", "skills"),
    ("docs/figures/README.md", r"There are (\w+) of them rather than one", "figures", "figures"),
]
WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}


def check_counts(truth: dict[str, int]) -> list[str]:
    problems = []
    for rel, pattern, key, label in RULES:
        path = ROOT / rel
        if not path.is_file():
            problems.append(f"{rel}: file missing, rule cannot be checked")
            continue
        text = path.read_text(encoding="utf-8")
        matches = re.findall(pattern, text)
        if not matches:
            problems.append(f"{rel}: no statement of {label} found (pattern drifted)")
            continue
        for raw in matches:
            value = WORDS.get(raw.lower(), None) if not raw.isdigit() else int(raw)
            if value is None:
                problems.append(f"{rel}: cannot read {label} value {raw!r}")
            elif value != truth[key]:
                problems.append(f"{rel}: says {value} {label}, repository has {truth[key]}")
    return problems


CONTRADICTIONS = (
    ("not taken", "the decision field still reads '(not taken)'"),
    ("leaves the decision field blank", "the summary still says the decision is unmade"),
    ("decision required before", "the header still says a decision is required"),
)


def check_decision_records() -> list[str]:
    """A record whose status is ACCEPTED must not still describe itself as open."""
    problems = []
    for path in sorted((ROOT / "docs" / "architecture").glob("ADR-*.md")):
        text = path.read_text(encoding="utf-8")
        status = re.search(r"\| Status \| (.+?) \|", text)
        if not status or "ACCEPTED" not in status.group(1):
            continue
        for needle, description in CONTRADICTIONS:
            if needle in text:
                problems.append(f"{path.relative_to(ROOT)}: status is ACCEPTED but {description}")
    return problems


def main() -> int:
    truth = derive()
    print("derived from the repository: " +
          " · ".join(f"{k} {v}" for k, v in truth.items() if k != "highest_scenario"))

    problems = check_counts(truth) + check_decision_records()
    for problem in problems:
        print(f"  ✗ {problem}")

    if problems:
        print(f"\n{len(problems)} inconsistenc{'y' if len(problems) == 1 else 'ies'} — documents FAIL")
        return 1
    print("\ndocuments agree with the repository and with themselves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
