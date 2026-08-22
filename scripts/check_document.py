#!/usr/bin/env python3
"""Mechanical checks over a research document source.

Responsibility
    Check the three things about a document source that can be checked without
    judgement: no unresolved placeholder survives, every citation key resolves to
    a bibliography entry, and every cross reference resolves to a label that
    exists.

Invariant
    This script proves resolution, never support. A citation that resolves may
    still fail to support the sentence citing it; that question belongs to a
    human or to a measured entailment checker, and calling this "verification of
    the document" would be the overstatement the repository exists to prevent.

Audit findings
    Implements the mechanical half of `skills/authoring-research-documents`
    phase 9, and the placeholder rule that keeps `TODO` out of a rendered
    artifact.

Supported sources
    Quarto/Pandoc Markdown (``.qmd``/``.md``) with ``@key`` citations and
    ``@fig-``/``@tbl-``/``@eq-``/``@sec-`` cross references.

Exit codes
    0 — every check passed.  1 — at least one finding.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|XXX|PLACEHOLDER|lorem ipsum)\b", re.I)
# @key, but not an email, not a cross-reference prefix
CITATION = re.compile(r"(?<![\w@/])@([a-zA-Z][\w:.#$%&+?<>~/-]*)")
XREF_PREFIXES = ("fig-", "tbl-", "eq-", "sec-", "lst-", "thm-")
# A figure, table or equation that is never referenced is a finding. A section
# anchor is not: sections carry labels for linking and navigation, and demanding
# a cross reference to each one would penalise correct documents.
MUST_BE_REFERENCED = ("fig-", "tbl-", "eq-")
TRAILING = ".,;:)]}\'\""
LABEL = re.compile(r"\{#((?:fig|tbl|eq|sec|lst|thm)-[\w-]+)")
BIB_ENTRY = re.compile(r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", re.M)


def bibliography_keys(source: Path, declared: str | None) -> tuple[set[str], Path | None]:
    candidates = []
    if declared:
        candidates.append(source.parent / declared)
    candidates += sorted(source.parent.glob("*.bib"))
    for path in candidates:
        if path.is_file():
            return set(BIB_ENTRY.findall(path.read_text(encoding="utf-8"))), path
    return set(), None


def declared_bibliography(text: str) -> str | None:
    match = re.search(r"^bibliography:\s*(\S+)\s*$", text, re.M)
    return match.group(1) if match else None


def check(source: Path) -> list[str]:
    text = source.read_text(encoding="utf-8")
    findings: list[str] = []

    for match in PLACEHOLDERS.finditer(text):
        line = text[:match.start()].count("\n") + 1
        findings.append(f"placeholder {match.group(0)!r} at line {line}")

    labels = set(LABEL.findall(text))
    keys, bib_path = bibliography_keys(source, declared_bibliography(text))

    citations, xrefs = set(), set()
    for match in CITATION.finditer(text):
        # Markdown puts sentence punctuation directly against a key; the key
        # stops before it. Without this, "@fig-stack." resolves to nothing.
        token = match.group(1).rstrip(TRAILING)
        (xrefs if token.startswith(XREF_PREFIXES) else citations).add(token)

    for ref in sorted(xrefs):
        if ref not in labels:
            findings.append(f"cross reference @{ref} resolves to no label")
    for label in sorted(labels):
        if label.startswith(MUST_BE_REFERENCED) and label not in xrefs:
            findings.append(f"{{#{label}}} is never referenced in the text — "
                            f"a figure, table or equation that no sentence points at "
                            f"is decoration")

    if citations and bib_path is None:
        findings.append(f"{len(citations)} citation key(s) but no bibliography file found")
    else:
        for key in sorted(citations - keys):
            findings.append(f"citation @{key} resolves to no bibliography entry")
        for key in sorted(keys - citations):
            findings.append(f"bibliography entry {key} is never cited")

    print(f"{source.name}: {len(citations)} citations · {len(xrefs)} cross references · "
          f"{len(labels)} labels · bibliography {bib_path.name if bib_path else 'none'}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("documents", nargs="+", type=Path)
    args = parser.parse_args()

    total = 0
    for source in args.documents:
        if not source.is_file():
            print(f"not found: {source}", file=sys.stderr)
            return 1
        findings = check(source)
        for finding in findings:
            print(f"  ✗ {finding}")
        total += len(findings)

    print(f"\n{len(args.documents)} document(s), {total} finding(s)")
    if total:
        return 1
    print("resolution checks passed — this proves references resolve, not that they support")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
