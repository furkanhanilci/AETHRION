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

    A later inspection found the failure class this checker itself creates: it
    catches exactly the numbers someone wrote a rule for, and every count that
    had drifted — the test count in four documents, the bundle size in three, the
    attestation's subject count, the figure count in the runbook — was one nobody
    had. Rules for those now exist. The class does not close, which is why the
    derived line is printed: the honest reading of a pass is "the registered
    numbers agree", not "no number is stale".

Exit codes
    0 — documents agree with the repository and with themselves.  1 — drift.
"""
from __future__ import annotations

import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
sys.path.insert(0, str(ROOT / "scripts"))


def derive() -> dict[str, int]:
    """Ground truth, computed rather than recalled."""
    def _is(kind: str, name: str) -> bool:
        return bool(re.match(r"^WP-\d{3}_", name)) and name.endswith(f".{kind}.md")

    all_wp = [p for p in PLAN.rglob("WP-*.md") if re.match(r"^WP-\d{3}_", p.name)]
    test_procedures = [p for p in all_wp if _is("tests", p.name)]
    acceptance_criteria = [p for p in all_wp if _is("acceptance", p.name)]
    packages = [p for p in all_wp
                if p not in test_procedures and p not in acceptance_criteria]
    scenarios = [p for p in (PLAN / "12_ACCEPTANCE_SCENARIOS").glob("ACC-*.md")
                 if re.match(r"^ACC-\d{2}_", p.name)]
    skills = [d for d in (ROOT / "skills").iterdir()
              if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").exists()]
    seal = (PLAN / "00_PROGRAM" / "SHA256SUMS.txt").read_text().strip().splitlines()
    markdown = list(PLAN.rglob("*.md"))
    figures = list((ROOT / "docs" / "figures").glob("*.svg"))
    numbered = [p for p in packages if p.name != "WP-000_interim_evidence_policy.md"]

    # Counts that drifted in six places while this checker reported "documents
    # agree": nothing was wrong with the rules, there simply were none for these.
    tests = sum(len(re.findall(r"^\s*def test_", p.read_text(encoding="utf-8"), re.M))
                for p in sorted((ROOT / "tests").glob("test_*.py")))
    import write_status                      # the bundle is the authority on its own size
    bundle_checks = len(write_status.CHECKS) + 1         # + the seal, inserted at run time
    envelope = json.loads((ROOT / "delivery" / "WP-000" / "evidence.dsse.json")
                          .read_text(encoding="utf-8"))
    subjects = len(json.loads(base64.b64decode(envelope["payload"]))["subject"])

    return {
        "test_procedures": len(test_procedures),
        "acceptance_criteria": len(acceptance_criteria),
        "tests": tests,
        "bundle_checks": bundle_checks,
        "attestation_subjects": subjects,
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
     r"\| Test procedure documents \| \*\*(\d+)\*\*", "test_procedures", "test procedure documents"),
    ("planning/commissioning/README.md",
     r"\| Acceptance criteria documents \| \*\*(\d+)\*\*", "acceptance_criteria", "acceptance criteria documents"),
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

    # Added after an inspection found the test count stale in four documents and
    # nine places, the bundle size stale in three, and the attestation's subject
    # count stale in one — none of them covered by a rule above.
    ("README.md", r"systemd units · (\d+) tests<br/>", "tests", "tests"),
    ("README.md", r"uv run pytest\s+# (\d+) tests", "tests", "tests"),
    ("README.md", r"(\d+)/\d+ tests pass", "tests", "tests"),
    ("README.md", r"plan seal · (\d+) status checks", "bundle_checks", "bundle checks"),
    ("README.md", r"One command runs all (\w+)\.", "bundle_checks", "bundle checks"),
    ("README.md", r"signature OK, (\d+) subject digests OK", "attestation_subjects", "attestation subjects"),
    ("docs/architecture/AETHRION_ARCHITECTURE.md", r"systemd units · (\d+) tests<br/>", "tests", "tests"),
    ("docs/architecture/AETHRION_ARCHITECTURE.md", r"plan seal · (\d+) status checks", "bundle_checks", "bundle checks"),
    ("tests/README.md", r"\| Scope \| The (\d+) tests that run today \|", "tests", "tests"),
    ("tests/README.md", r"— (\d+) passing; coverage is narrow", "tests", "tests"),
    ("tests/README.md", r"\*\*In one paragraph\.\*\* ([A-Za-z-]+) tests cover", "tests", "tests"),
    ("tests/README.md", r"uv run pytest\s+# all (\d+)", "tests", "tests"),
    ("docs/OPERATIONS.md", r"uv run pytest\s+# (\d+) tests", "tests", "tests"),
    ("docs/OPERATIONS.md", r"Expected: `(\d+) passed`", "tests", "tests"),
    ("docs/OPERATIONS.md", r"`(\d+) figures, 0 drift, 0 overflow`", "figures", "figures"),
]
def _words() -> dict[str, int]:
    """Every spelled-out number from one to ninety-nine.

    This was a hand-written dictionary that happened to reach *forty-five*. The
    suite then grew to forty-six, `tests/README.md` was updated correctly, and
    the checker read the new word as an unknown and reported the old number —
    a consistency check that fails a document for being right. The list of
    numbers is not a judgement, so it is generated.
    """
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
             "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]
    out = {units[n]: n for n in range(1, 10)}
    out |= {teens[n - 10]: n for n in range(10, 20)}
    for n in range(20, 100):
        word = tens[n // 10] + (f"-{units[n % 10]}" if n % 10 else "")
        out[word] = n
    return out


WORDS = _words()


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
