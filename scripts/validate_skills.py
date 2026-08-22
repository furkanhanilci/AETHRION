#!/usr/bin/env python3
"""Mechanically validate the AETHRION skill registry.

Responsibility
    Check every ``skills/*/SKILL.md`` against two rule sets at once:
    the Agent Skills open format (agentskills.io) and the AIRL metadata
    contract laid out in ``docs/architecture/AETHRION_SKILL_LAYER.md`` §14.

Invariant
    A skill that does not load in a stock harness governs nothing. Conformance
    to the open format is therefore not cosmetic — it *is* the bootstrap, and
    this script is the mechanical check that keeps it true.

Audit findings
    Closes the "38 skills exist, none of them loads" half of the skill-layer
    gap. Does **not** address whether a skill changes agent behaviour; that
    needs a baseline behaviour test (see ``writing-skills``), which this script
    deliberately does not claim to provide.

Exit codes
    0 — every skill conforms.  1 — at least one violation.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
DOMAINS = {"engineering", "scientific-research", "shared"}
ORIGINS = {"airl-native", "superpowers"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_META = ("airl.version", "airl.domain", "airl.origin")
BODY_LINE_BUDGET = 500          # agentskills.io recommendation
DESCRIPTION_MAX = 1024          # agentskills.io hard limit


def parse_frontmatter(text: str):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        return None, None
    top, meta, key = {}, {}, None
    for line in match.group(1).splitlines():
        if line.startswith("  ") and key == "metadata":
            sub = re.match(r"^\s+([A-Za-z0-9_.-]+):\s*(.*)$", line)
            if sub:
                meta[sub.group(1)] = sub.group(2).strip().strip('"')
            continue
        field = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if field:
            key = field.group(1)
            top[key] = field.group(2).strip().strip('"')
    return top, (meta, match.group(2))


def validate(path: Path) -> list[str]:
    slug = path.parent.name
    top, rest = parse_frontmatter(path.read_text())
    if top is None:
        return [f"{slug}: no YAML frontmatter"]
    meta, body = rest
    problems: list[str] = []

    for field in sorted(set(top) - SPEC_FIELDS):
        problems.append(f"{slug}: '{field}' is not an Agent Skills field — move it under metadata")

    name = top.get("name", "")
    if not name:
        problems.append(f"{slug}: 'name' is required")
    elif name != slug:
        problems.append(f"{slug}: name '{name}' does not match its directory")
    elif not NAME_RE.match(name) or len(name) > 64:
        problems.append(f"{slug}: name violates the naming rules")

    description = top.get("description", "")
    if not description:
        problems.append(f"{slug}: 'description' is required")
    elif len(description) > DESCRIPTION_MAX:
        problems.append(f"{slug}: description is {len(description)} chars (max {DESCRIPTION_MAX})")

    for field in REQUIRED_META:
        if field not in meta:
            problems.append(f"{slug}: metadata is missing {field}")

    domain = meta.get("airl.domain")
    if domain and domain not in DOMAINS:
        problems.append(f"{slug}: airl.domain '{domain}' is not one of {sorted(DOMAINS)}")

    origin = meta.get("airl.origin")
    if origin and origin not in ORIGINS:
        problems.append(f"{slug}: airl.origin '{origin}' is not one of {sorted(ORIGINS)}")

    # Provenance: anything derived from or vendored out of upstream must be pinned.
    derived = meta.get("airl.derived_from") or (origin == "superpowers")
    if derived:
        commit = meta.get("airl.upstream_commit", "")
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            problems.append(f"{slug}: upstream provenance is not pinned to a full commit sha")

    if origin == "superpowers" and domain != "engineering":
        problems.append(f"{slug}: vendored upstream skills must carry domain 'engineering'")

    lines = body.count("\n")
    if lines > BODY_LINE_BUDGET:
        # Vendored prose is upstream's to fix; editing it would break provenance.
        level = "warn" if origin == "superpowers" else "fail"
        problems.append(f"[{level}] {slug}: body is {lines} lines "
                        f"(budget {BODY_LINE_BUDGET}) — move detail into references/")

    return problems


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    skills = sorted(p for p in root.glob("skills/*/SKILL.md"))
    if not skills:
        print("no skills found", file=sys.stderr)
        return 1

    findings: list[str] = []
    for path in skills:
        findings.extend(validate(path))
    warnings = [f for f in findings if f.startswith("[warn]")]
    problems = [f for f in findings if not f.startswith("[warn]")]

    families: dict[str, int] = {}
    for path in skills:
        top, rest = parse_frontmatter(path.read_text())
        if rest:
            domain = rest[0].get("airl.domain", "unknown")
            families[domain] = families.get(domain, 0) + 1

    print(f"{len(skills)} skills: " + " · ".join(f"{k} {v}" for k, v in sorted(families.items())))
    for warning in warnings:
        print(f"  ! {warning.removeprefix('[warn] ')}")
    if problems:
        print(f"\n{len(problems)} violation(s):")
        for problem in problems:
            print(f"  ✗ {problem.removeprefix('[fail] ')}")
        return 1
    print("all skills conform to the Agent Skills format and the AIRL metadata contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
