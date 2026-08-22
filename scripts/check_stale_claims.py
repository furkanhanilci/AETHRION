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
# Reporting verbs matter as much as past tense here. A change record that says
# a document "said X — it is not" quotes the defect in order to deny it, and
# flagging that quotation would push a maintainer to delete the record of the
# correction, which is the edit DOCUMENT_STANDARD.md §3 rule 4 forbids.
PAST_TENSE = re.compile(
    r"\b(at the time|were|was|then held|previously|before this|used to|"
    r"had been|no longer|said|claimed|stated|corrected|it is not|"
    r"does not|did not)\b", re.I)
LEDGER_ROW = re.compile(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|")


def is_history(line: str) -> bool:
    """A dated ledger row, or a sentence written in the past tense."""
    return bool(LEDGER_ROW.match(line.strip()) or PAST_TENSE.search(line))


def _sealed() -> int:
    seal = ROOT / "planning" / "commissioning" / "00_PROGRAM" / "SHA256SUMS.txt"
    return len(seal.read_text(encoding="utf-8").strip().splitlines())


def _skills() -> int:
    return len([d for d in (ROOT / "skills").iterdir()
                if d.is_dir() and (d / "SKILL.md").exists()])


def _figures() -> int:
    return len(list((ROOT / "docs" / "figures").glob("*.svg")))


def _scenarios() -> int:
    return len(list((ROOT / "planning" / "commissioning" / "12_ACCEPTANCE_SCENARIOS")
                    .glob("ACC-*.md")))


# The corrections quote numbers, so they are derived rather than typed. A
# checker whose own advice has gone stale is worse than no checker: it tells a
# maintainer to write a wrong number with the authority of a passing build.
# This list said "the seal covers 207 files" while the seal covered 221.
CLAIMS: list[tuple[str, str]] = [
    (r"\bACC-01\s*[–-]\s*ACC-40\b", f"the scenario range ends at ACC-{_scenarios():02d}"),
    (r"\b(?:38|49|51) skills\b", f"the registry holds {_skills()} skills"),
    (r"\b46 scenarios\b", f"there are {_scenarios()} scenarios"),
    (r"\b(?:195|196|202|207)/(?:195|196|202|207)\b", f"the seal covers {_sealed()} files"),
    (r"[Tt]here is no CI\b", "BVC-01 is written and staged; say staged, not absent"),
    (r"\b(?:three|four|five|six|seven|eight) of them rather than one\b",
     f"there are {_figures()} figures"),
]

# ---------------------------------------------------------------------------
# Semantic checks. The three above this line match a literal that somebody
# thought to write down. These derive the truth from the repository and then
# look for prose that disagrees with it, which is the class of defect the
# literal list kept missing.
# ---------------------------------------------------------------------------

# Deliberately narrow. A decision record makes a question *decided*; it does not
# make the thing it decided *built*. "H5 remains open" is true — ADR-002 chose a
# control and the CI platform is still absent — so implementation-absence wording
# is left alone and only decision-shaped wording is flagged.
UNDECIDED = re.compile(
    r"\b(undecided|not yet decided|an open question|open decision|"
    r"is still open|remains an open question|no standard answers it)\b", re.I)


def resolved_findings() -> dict[str, str]:
    """Audit findings that an ACCEPTED decision record has closed."""
    out: dict[str, str] = {}
    for adr in sorted((ROOT / "docs" / "architecture").glob("ADR-*.md")):
        text = adr.read_text(encoding="utf-8")
        status = next((l for l in text.splitlines() if l.startswith("| Status")), "")
        if "ACCEPTED" not in status:
            continue
        for match in re.finditer(r"finding\s+\**([CHM]\d+)\**", text):
            out.setdefault(match.group(1), adr.name)
    return out


def contradictions() -> list[tuple[re.Pattern[str], str]]:
    """Claims the repository can currently disprove about itself."""
    rules: list[tuple[re.Pattern[str], str]] = []

    # The attestation profile states what it does not cover. A document may not
    # claim an assurance the issued manifest explicitly disclaims.
    policy = (ROOT / "planning" / "commissioning" / "01_GOVERNANCE"
              / "WP-000_interim_evidence_policy.md")
    if policy.exists() and "not submitted to a transparency log" in policy.read_text(
            encoding="utf-8"):
        rules.append((
            # Matches any phrasing that puts the manifest in a transparency
            # log. The first version of this rule required the word "recorded"
            # and missed "as a signed in-toto attestation in a public
            # transparency log" two files away.
            re.compile(r"in a public transparency log", re.I),
            "WP-000 runs the interim profile and is NOT in a transparency log",
        ))

    # The specimen states whether it has been rendered; nothing may say otherwise.
    specimen = ROOT / "delivery" / "specimen" / "README.md"
    if specimen.exists() and "never rendered" in specimen.read_text(encoding="utf-8"):
        rules.append((
            re.compile(r"\bspecimen\s+rendered\b", re.I),
            "delivery/specimen/README.md says never rendered — no toolchain installed",
        ))

    return rules


def paragraphs(text: str):
    """Yield (first_line_number, paragraph). Claims wrap across lines."""
    line_no = 1
    for block in text.split("\n\n"):
        yield line_no, block
        line_no += block.count("\n") + 2


def is_historical(path: Path) -> bool:
    return any(marker in str(path) for marker in HISTORICAL)


def main() -> int:
    findings: list[str] = []
    scanned = exempt = 0
    contradiction_rules = contradictions()
    closed = resolved_findings()

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

        for pattern, correction in contradiction_rules:
            for match in re.finditer(pattern, text):
                line_no = text[:match.start()].count("\n") + 1
                if is_history(text.splitlines()[line_no - 1]):
                    continue
                findings.append(f"{path.relative_to(ROOT)}:{line_no}  "
                                f"{match.group(0)!r} — {correction}")

        # A decision record closes a finding; prose may not still call it open.
        # The record itself is exempt, because it narrates the state it closed.
        if not path.name.startswith("ADR-"):
            for line_no, raw_block in paragraphs(text):
                # Bold and italics land in the middle of the phrases being
                # matched — "is **still open**" — so emphasis is stripped first.
                block = raw_block.replace("**", "").replace("*", "").replace("_", " ")
                if not UNDECIDED.search(block) or is_history(block):
                    continue
                for finding_id, adr in closed.items():
                    # The id must be introduced as an audit finding. "C2" also
                    # names a proposal item in AETHRION_IDEAL_STRUCTURE.md, and
                    # matching a bare token would flag an unrelated table.
                    if re.search(rf"finding\s+\**{finding_id}\b", block, re.I):
                        findings.append(
                            f"{path.relative_to(ROOT)}:{line_no}  "
                            f"calls {finding_id} undecided — decided by {adr}")

    print(f"{scanned} documents scanned · {exempt} historical records exempt · "
          f"{len(CLAIMS)} literal rules · {len(contradiction_rules)} derived "
          f"contradiction rules · {len(closed)} closed finding(s) tracked")
    for finding in findings:
        print(f"  ✗ {finding}")
    if findings:
        print(f"\n{len(findings)} stale present-tense claim(s)")
        return 1
    print("\nno document contradicts the rules above — which is narrower than "
          "\"nothing is stale\", and the count of rules is printed so the gap "
          "stays visible")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
