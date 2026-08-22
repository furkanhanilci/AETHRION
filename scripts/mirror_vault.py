#!/usr/bin/env python3
"""Generate the whole Obsidian project mirror from canonical repository content.

The Obsidian project tree under
``<vault>/10 - Projects/AETHRION/`` contains three generated areas:

* ``01 - Commissioning/`` — the plan (delegated to ``mirror_plan.py``)
* ``02 - Reviews/`` and ``04 - Architecture/`` — the ``docs/`` documents
* ``07 - Skills/`` — the skill registry, grouped

Everything else in that tree is human-authored and is never touched here.

Usage:
    python scripts/mirror_vault.py <vault-project-dir> [--check]
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
DOCS = REPO / "docs"

# Canonical skill name → Obsidian group folder.
GROUPS = {
    "A - Meta": ["using-aethrion", "writing-skills"],
    "B - Discipline": [
        "preregistration-discipline", "verification-before-completion",
        "evidence-before-claim", "scope-discipline", "independence-discipline",
    ],
    "C - Process": [
        "framing-research", "writing-protocols", "writing-analysis-plans",
        "executing-experiments", "agent-driven-research",
        "dispatching-parallel-analysts", "using-isolated-environments",
        "finishing-a-project",
    ],
    "D - Review": [
        "requesting-review", "receiving-review", "blind-reviewing",
        "adversarial-reviewing", "arbitrating-disagreement",
    ],
    "E - Research": [
        "investigating-anomalies", "investigating-integrity-concerns",
        "searching-literature", "screening-sources", "extracting-evidence",
        "anchoring-spans", "curating-zotero", "building-review-packets",
    ],
    "I - Reporting": ["producing-figures", "reporting-results",
                      "authoring-research-documents"],
    "F - Metascience": [
        "calibrating-confidence", "measuring-agreement", "injecting-controls",
    ],
    "G - Communication": [
        "notifying-humans", "routing-decision-requests",
        "receiving-external-messages", "escalating-and-paging",
        "publishing-digests", "submitting-external-records",
        "monitoring-external-feeds",
    ],
    # Vendored from obra/superpowers — engineering discipline for building
    # AETHRION itself. Mirrored read-only like every other generated area.
    "H - Engineering": [
        "test-driven-development", "brainstorming", "writing-plans",
        "executing-plans", "subagent-driven-development",
        "dispatching-parallel-agents", "systematic-debugging",
        "using-git-worktrees", "requesting-code-review",
        "receiving-code-review", "finishing-a-development-branch",
    ],
}

DOC_MAP = {
    "04 - Architecture/adr_001_solo_operator_independence.md":
        "architecture/ADR-001_solo_operator_independence.md",
    "04 - Architecture/adr_002_bootstrap_verification_control.md":
        "architecture/ADR-002_bootstrap_verification_control.md",
    "04 - Architecture/adr_003_trusted_control_and_policy.md":
        "architecture/ADR-003_trusted_control_and_policy.md",
    "05 - Evidence/current_status.md":
        "STATUS.md",
    "04 - Architecture/aethrion_document_standard.md":
        "DOCUMENT_STANDARD.md",
    "04 - Architecture/aethrion_component_reuse.md":
        "architecture/AETHRION_COMPONENT_REUSE.md",
    "04 - Architecture/aethrion_related_systems.md":
        "architecture/AETHRION_RELATED_SYSTEMS.md",
    "04 - Architecture/aethrion_roles.md":
        "architecture/AETHRION_ROLES.md",
    "04 - Architecture/aethrion_figure_specification.md":
        "figures/README.md",
    "04 - Architecture/aethrion_architecture.md":
        "architecture/AETHRION_ARCHITECTURE.md",
    "04 - Architecture/aethrion_external_standards.md":
        "architecture/AETHRION_EXTERNAL_STANDARDS.md",
    "04 - Architecture/aethrion_foundation.md":
        "architecture/FOUNDATION.md",
    "02 - Reviews/claude_framework_audit_report.md":
        "review/FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md",
    "02 - Reviews/remediation_verification_2026-08-22.md":
        "review/2026-08-22_remediation_verification.md",
    "02 - Reviews/claude_full_framework_review_prompt.md":
        "review/CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md",
    "04 - Architecture/aethrion_ideal_structure.md":
        "architecture/AETHRION_IDEAL_STRUCTURE.md",
    "04 - Architecture/aethrion_skill_layer.md":
        "architecture/AETHRION_SKILL_LAYER.md",
    "04 - Architecture/aethrion_role_model_assignment.md":
        "architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md",
    "04 - Architecture/aethrion_naming_and_terminology.md":
        "branding.md",
    "04 - Architecture/aethrion_branding_assets.md":
        "assets/branding/README.md",
}

BANNER = (
    "> [!info] Generated view\n"
    "> This note is generated from `{source}` in the repository. Edit the\n"
    "> canonical file and regenerate; edits made here are overwritten.\n\n"
)


def build() -> dict[str, bytes]:
    out: dict[str, bytes] = {}

    for rel, src in DOC_MAP.items():
        text = (DOCS / src).read_text(encoding="utf-8")
        # Figures live beside the architecture notes in the vault, so the
        # repository-relative image paths are rewritten to vault-relative ones.
        text = text.replace("](../figures/", "](figures/").replace("](figures/README.md)",
                                                                   "](aethrion_figure_specification.md)")
        out[rel] = (BANNER.format(source=f"docs/{src}") + text).encode("utf-8")

    for group, names in GROUPS.items():
        for name in names:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            body = BANNER.format(source=f"skills/{name}/SKILL.md") + text
            out[f"07 - Skills/{group}/{name}.md"] = body.encode("utf-8")

    for svg in sorted((DOCS / "figures").glob("*.svg")):
        out[f"04 - Architecture/figures/{svg.name}"] = svg.read_bytes()

    # The logo is a projection of docs/assets/branding/aethrion-logo.png, kept
    # byte-identical. Obsidian resolves ``![[aethrion-logo.png]]`` by filename,
    # so the landing page needs a copy that lives inside the vault.
    out["_assets/aethrion-logo.png"] = (DOCS / "assets" / "branding" / "aethrion-logo.png").read_bytes()

    text = (SKILLS / "README.md").read_text(encoding="utf-8")
    text = re.sub(r"\]\((?!http)([a-z0-9-]+)/SKILL\.md\)", r"](\1.md)", text)
    out["07 - Skills/skills_index.md"] = (
        BANNER.format(source="skills/README.md") + text
    ).encode("utf-8")

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path,
                        help="the project root inside the vault, i.e. "
                             "'<vault>/10 - Projects/AETHRION' — not the vault root")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    generated = build()
    drift: list[str] = []
    for rel, payload in generated.items():
        path = args.target / rel
        if args.check:
            if not path.exists():
                drift.append(f"missing: {rel}")
            elif path.read_bytes() != payload:
                drift.append(f"differs: {rel}")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)

    if args.check:
        for line in drift:
            print(line)
        print(f"{len(generated)} generated files, {len(drift)} drift entries")
        return 1 if drift else 0

    print(f"wrote {len(generated)} files to {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
