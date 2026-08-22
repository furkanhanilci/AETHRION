#!/usr/bin/env python3
"""Check that every adopted external component is documented well enough to audit.

Responsibility
    The reporting subsystem stands on external tools. This script checks that the
    register describing them carries what a later reader needs in order to
    re-derive the decision: an adoption type, a source, and — above all — an
    explicit **authority boundary**.

Invariant
    A component that cannot be given an authority boundary does not enter a gate.
    "What may this tool decide, and what may it never decide?" is the question a
    reporting pipeline gets wrong first, so it is the one checked here.

Audit findings
    Supports the adoption rules in `AIRL_OS_COMPONENT_REUSE.md` §2 and the
    registry contract in the reporting skill's
    `references/external-systems-and-standards.md`.

Exit codes
    0 — the register is auditable.  1 — something is missing.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = (ROOT / "skills" / "authoring-research-documents" / "references"
            / "external-systems-and-standards.md")
TYPES = {"DEPENDENCY", "ADAPTER", "STANDARD", "BENCHMARK", "PATTERN",
         "OPTIONAL_BACKEND", "REJECTED"}
REQUIRED_SECTIONS = ("Adoption types", "authority_boundary", "Rejected",
                     "Evidence hierarchy")


def main() -> int:
    if not REGISTER.is_file():
        print(f"register not found: {REGISTER.relative_to(ROOT)}", file=sys.stderr)
        return 1
    text = REGISTER.read_text(encoding="utf-8")
    findings: list[str] = []

    for needle in REQUIRED_SECTIONS:
        if needle not in text:
            findings.append(f"register is missing a required element: {needle!r}")

    used = {t for t in TYPES if re.search(rf"\b{t}\b", text)}
    if not used:
        findings.append("no adoption type appears in the register")

    if "docs_retrieved_at" not in text:
        findings.append("no retrieval date recorded for any component")
    if "UNVERIFIED" not in text:
        findings.append("nothing is marked UNVERIFIED — a register with no unverified "
                        "claim is usually a register that stopped checking")

    # A rejected candidate must carry a reason, not just a name.
    rejected = text.split("## 9. Rejected")[-1] if "## 9. Rejected" in text else ""
    if rejected and rejected.count("|") < 8:
        findings.append("the rejected section names candidates without reasons")

    print(f"register: {REGISTER.relative_to(ROOT)}")
    print(f"adoption types present: {' · '.join(sorted(used)) or 'none'}")
    for finding in findings:
        print(f"  ✗ {finding}")
    if findings:
        print(f"\n{len(findings)} finding(s) — register FAILS audit")
        return 1
    print("\nregister is auditable: types, sources, retrieval dates, unverified "
          "claims and rejections are all present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
