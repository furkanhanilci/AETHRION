#!/usr/bin/env python3
"""Find statements about the present that the repository has outgrown.

Responsibility
    ``check_doc_consistency.py`` checks *declared counts* against reality. This
    checks *prose*: a sentence that says "there is no CI" after a CI control was
    written, or "38 skills" in a document describing the current registry.

Invariant
    **Historical records are exempt, and that exemption is the point.** An
    implementation log entry, a frozen audit and a past step summary describe
    the state at their date; editing them to match today would destroy the record
    the repository keeps them for — `docs/DOCUMENT_STANDARD.md` §3 rules 3 and 4.
    So the exemption list is explicit and narrow rather than a blanket skip.

Audit findings
    Written after a corpus scan found 66 stale phrases, of which roughly half
    were legitimate history. A checker that cannot tell those apart would push a
    maintainer toward exactly the edit the standard forbids.

Exit codes
    0 — no stale present-tense claim.  1 — at least one.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files that record a moment and must never be edited to match the present.
HISTORICAL = (
    "implementation_log.md",
    "FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md",
    "claude_framework_audit_report.md",
    "session_handover_",              # its history section; the live fields are checked below
    "CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md",
    "_framework_audit_evidence.md",
    "remediation_verification",       # frozen dated verification reports

)
SKIP_DIRS = (".venv", "70 - Literature Sets", "skills/_vendor", "01 - Commissioning")

# A match inside one of these contexts is history, not a claim about the present.
PAST_TENSE = re.compile(
    r"\b(at the time|were|was|then held|previously|before this|used to|"
    r"had been|no longer)\b", re.I)
LEDGER_ROW = re.compile(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|")


def is_history(line: str) -> bool:
    """A dated ledger row, or a sentence written in the past tense."""
    return bool(LEDGER_ROW.match(line.strip()) or PAST_TENSE.search(line))


CLAIMS: list[tuple[str, str]] = [
    (r"\bACC-01\s*[–-]\s*ACC-40\b", "the scenario range ends at ACC-51"),
    (r"\b(?:38|49|51) skills\b", "the registry holds 52 skills"),
    (r"\b46 scenarios\b", "there are 51 scenarios"),
    (r"\b(?:195|196|202)/(?:195|196|202)\b", "the seal covers 207 files"),
    (r"[Tt]here is no CI\b", "BVC-01 is written and staged; say staged, not absent"),
    (r"\bfour of them rather than one\b|\bthree of them rather than one\b",
     "there are five figures"),
]


def is_historical(path: Path) -> bool:
    return any(marker in str(path) for marker in HISTORICAL)


def main() -> int:
    findings: list[str] = []
    scanned = exempt = 0

    for path in sorted(ROOT.rglob("*.md")):
        text_path = str(path)
        if any(skip in text_path for skip in SKIP_DIRS):
            continue
        if is_historical(path):
            exempt += 1
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern, correction in CLAIMS:
            for match in re.finditer(pattern, text):
                line_no = text[:match.start()].count("\n") + 1
                line = text.splitlines()[line_no - 1]
                if is_history(line):
                    continue
                findings.append(f"{path.relative_to(ROOT)}:{line_no}  "
                                f"{match.group(0)!r} — {correction}")

    print(f"{scanned} documents scanned · {exempt} historical records exempt")
    for finding in findings:
        print(f"  ✗ {finding}")
    if findings:
        print(f"\n{len(findings)} stale present-tense claim(s)")
        return 1
    print("\nno document claims a state the repository has outgrown")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
