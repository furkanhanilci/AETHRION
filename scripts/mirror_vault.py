#!/usr/bin/env python3
"""Generate the whole Obsidian project mirror from canonical repository content.

The Obsidian project tree under ``<vault>/10 - Projects/AETHRION/`` is generated
area by area, and a page is generated exactly when this script or
``mirror_plan.py`` names it:

* ``01 - Commissioning/`` — the plan (delegated to ``mirror_plan.py``)
* ``02 - Reviews/``, ``04 - Architecture/``, ``03 - Implementation/``,
  ``05 - Evidence/``, ``06 - Components/`` — documents from ``docs/`` and the
  folder-level ``README``s that index the repository's own directories
* ``07 - Skills/`` — the skill registry, grouped
* the project root — ``README.md``, ``AGENTS.md``, ``CLAUDE.md`` and
  ``docs/README.md``, the four maps a reader opens first

Everything else in that tree is human-authored. The mirror refuses to write over
a page whose frontmatter says ``generated: false``, because the areas above hold
curated notes beside the projection and two of them once sat at names this map
tried to claim.

Links between mirrored documents are translated into vault-relative form, so a
link that resolves in the repository also resolves in the vault. Links that
point *out* of the mirrored subset — a skill's prompt templates, its agent
definitions, ``docs/ARCHITECTURE_V0.md`` — are left exactly as written and do
not resolve in Obsidian. That is deliberate: the mirror carries a subset, and a
link this script does not understand is safer visibly broken than silently
repointed at the wrong note. ``scripts/check_vault.py`` counts them on every
run and prints the total, so the number is never written down here — it was
recorded as "eleven" while the real figure had grown to thirty-one.

Usage:
    python scripts/mirror_vault.py <vault-project-dir> [--check]
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vault_frontmatter

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
    "04 - Architecture/adr_004_mechanism_assimilation.md":
        "architecture/ADR-004_mechanism_assimilation.md",
    "04 - Architecture/adr_005_epistemic_memory_separation.md":
        "architecture/ADR-005_epistemic_memory_separation.md",
    "04 - Architecture/adr_006_discovery_search_graph.md":
        "architecture/ADR-006_discovery_search_graph.md",
    "04 - Architecture/adr_007_frozen_evaluator_and_verified_values.md":
        "architecture/ADR-007_frozen_evaluator_and_verified_values.md",
    "04 - Architecture/adr_008_verification_taxonomy.md":
        "architecture/ADR-008_verification_taxonomy.md",
    "04 - Architecture/adr_009_publication_as_projection.md":
        "architecture/ADR-009_publication_as_projection.md",
    "04 - Architecture/adr_010_policy_backend.md":
        "architecture/ADR-010_policy_backend.md",
    "04 - Architecture/adr_011_multi_agent_execution_invariant.md":
        "architecture/ADR-011_multi_agent_execution_invariant.md",
    "04 - Architecture/adr_012_dual_disciplines.md":
        "architecture/ADR-012_dual_disciplines.md",
    "04 - Architecture/adr_013_blackboard_and_sparse_communication.md":
        "architecture/ADR-013_blackboard_and_sparse_communication.md",
    "04 - Architecture/adr_014_canonical_authority_and_split_brain.md":
        "architecture/ADR-014_canonical_authority_and_split_brain.md",
    "04 - Architecture/adr_015_adaptive_assurance_routing.md":
        "architecture/ADR-015_adaptive_assurance_routing.md",
    "04 - Architecture/adr_016_human_preliminary_judgment.md":
        "architecture/ADR-016_human_preliminary_judgment.md",
    "04 - Architecture/adr_017_benchmark_isolation.md":
        "architecture/ADR-017_benchmark_isolation.md",
    "04 - Architecture/adr_018_specification_to_code_conformance.md":
        "architecture/ADR-018_specification_to_code_conformance.md",
    "04 - Architecture/adr_019_supply_chain_and_upstream_standard.md":
        "architecture/ADR-019_supply_chain_and_upstream_standard.md",
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

    # Added because plan and architecture documents link to these and the links
    # landed on nothing in the vault. `check_vault.py` counted 31 such links; a
    # cross-reference that resolves in the repository and not in the projection
    # is a defect of the projection, not of the document.
    "05 - Evidence/current_ready_queue.md": "READY.md",
    "02 - Reviews/findings_register.md": "FINDINGS.md",
    # NOT under `01 - Commissioning/` — that subtree belongs to mirror_plan.py,
    # which replaces it wholesale. Two mirrors writing into one directory is a
    # canonical-ownership conflict, and mirror_plan's stray-file refusal caught
    # it on the first run.
    "04 - Architecture/aethrion_v2_candidates.md": "V2_CANDIDATES.md",
    "03 - Implementation/operations_runbook.md": "OPERATIONS.md",
    "03 - Implementation/executing_a_work_package.md": "EXECUTING_A_WORK_PACKAGE.md",
    "04 - Architecture/aethrion_architecture_v0.md": "ARCHITECTURE_V0.md",
}

# The folder-level documents, which live outside `docs/` and are therefore keyed
# by a repository-relative path.
#
# These are the notes that make a folder navigable: `docs/architecture/README.md`
# is the index of the twenty architecture notes, `docs/review/README.md` is the
# index of the reviews, and `README.md` is the index of the repository itself.
# The mirror carried every leaf document and none of the maps, so the vault held
# twenty architecture notes in a folder with no way in, and a reader who opened
# `04 - Architecture/` saw an alphabetical list rather than a structure. A
# projection that omits precisely the documents describing the structure is not a
# smaller projection; it is a flatter one.
REPO_MAP = {
    # The repository's own front door, its operating manual, and the harness note.
    "aethrion_repository_index.md": "README.md",
    "agent_operating_manual.md": "AGENTS.md",
    "claude_code_operating_notes.md": "CLAUDE.md",
    "documentation_index.md": "docs/README.md",

    # Folder indexes, each landing in the vault folder it indexes.
    # NOT `reviews_index.md` / `architecture_index.md`: the vault curates notes
    # under those names by hand. The repository's index of a document folder and
    # a reader's map of the same area are two documents, and the first must not
    # take the second's name — on the first run of this map it overwrote both.
    "02 - Reviews/review_corpus_index.md": "docs/review/README.md",
    "04 - Architecture/architecture_corpus_index.md": "docs/architecture/README.md",
    "04 - Architecture/schemas_index.md": "schemas/README.md",
    "04 - Architecture/upstream_lineage_register.md": "provenance/README.md",
    "03 - Implementation/scripts_index.md": "scripts/README.md",
    "03 - Implementation/tests_index.md": "tests/README.md",
    "03 - Implementation/deployment_index.md": "deploy/README.md",
    "03 - Implementation/claude_harness_index.md": ".claude/README.md",
    "06 - Components/Bridge/bridge_index.md": "src/airl_bridge/README.md",
    "06 - Components/framework_core_index.md": "src/airl_framework/README.md",

    # The delivery area — the evidence the plan produces.
    "05 - Evidence/delivery_index.md": "delivery/README.md",
    # NOT `wp_000_...`: `vault_frontmatter.derive` reads that prefix as a work
    # package and would give this page a package's type, tags and status.
    "05 - Evidence/delivery_wp_000_package.md": "delivery/WP-000/README.md",
    "05 - Evidence/measurements_index.md": "delivery/measurements/README.md",
    "05 - Evidence/specimen_index.md": "delivery/specimen/README.md",
    "05 - Evidence/signing_keys_index.md": "delivery/_keys/README.md",
}

# One map, repository-relative, so a link between any two mirrored documents can
# be resolved without knowing which map it came from.
SOURCES: dict[str, str] = {rel: f"docs/{src}" for rel, src in DOC_MAP.items()}
SOURCES.update(REPO_MAP)

BANNER = (
    "> [!info] Generated view\n"
    "> This note is generated from `{source}` in the repository. Edit the\n"
    "> canonical file and regenerate; edits made here are overwritten.\n\n"
)


def _relink(text: str, src: str, rel: str, src_to_vault: dict[str, str]) -> str:
    """Rewrite links between mirrored documents into vault-relative form.

    A link is rewritten only when its target is itself mirrored. Anything else
    is left exactly as written, because a link this function does not
    understand is safer visibly broken than silently repointed.
    """
    src_dir = PurePosixPath(src).parent
    out_dir = PurePosixPath(rel).parent

    def repl(match: re.Match[str]) -> str:
        target, frag = match.group(1), match.group(2) or ""
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        try:
            resolved = str(PurePosixPath(os.path.normpath(str(src_dir / target))))
        except ValueError:
            return match.group(0)
        vault = src_to_vault.get(resolved)
        if vault is None:
            return match.group(0)
        return f"]({os.path.relpath(vault, str(out_dir))}{frag})"

    return re.sub(r"\]\(([^)#\s]+\.md)(#[^)]*)?\)", repl, text)


def _is_human_note(path: Path) -> bool:
    """True when the file on disk declares itself hand-authored.

    The vault holds curated notes beside the projection, and two of them —
    `reviews_index.md` and `architecture_index.md` — sat at names this map tried
    to claim. Nothing stopped the write; the notes were recoverable only because
    `vault_baseline/` is tracked. A projection may create and replace its own
    pages and must never replace anyone else's.
    """
    if not path.is_file() or path.suffix != ".md":
        return False
    try:
        head = path.read_text(encoding="utf-8")[:2000]
    except (OSError, UnicodeDecodeError):
        return False
    return bool(re.search(r"^generated:\s*false\s*$", head, re.M))


def build() -> dict[str, bytes]:
    out: dict[str, bytes] = {}

    # Repository path -> vault path, so links between mirrored documents survive
    # the rename the mirror performs. Without this a link that resolves in the
    # repository lands on nothing in the vault, which is how the corpus grew a
    # set of broken links that only existed in the projection.
    src_to_vault = {src: rel for rel, src in SOURCES.items()}

    for rel, src in SOURCES.items():
        text = (REPO / src).read_text(encoding="utf-8")
        # Figures live beside the architecture notes in the vault, so the
        # repository-relative image paths are rewritten to vault-relative ones.
        text = text.replace("](../figures/", "](figures/").replace("](figures/README.md)",
                                                                   "](aethrion_figure_specification.md)")
        text = _relink(text, src, rel, src_to_vault)
        front = vault_frontmatter.derive(
            vault_rel=rel, source=src, text=text,
            generator="mirror_vault.py")
        out[rel] = (front + BANNER.format(source=src) + text).encode("utf-8")

    for group, names in GROUPS.items():
        for name in names:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            vault_rel = f"07 - Skills/{group}/{name}.md"
            # A skill already carries its own YAML frontmatter for the Agent
            # Skills format. Its keys are the skill contract, not Obsidian's, so
            # the vault block is prepended and the original is left untouched.
            front = vault_frontmatter.derive(
                vault_rel=vault_rel, source=f"skills/{name}/SKILL.md",
                text=text, generator="mirror_vault.py")
            body = front + BANNER.format(source=f"skills/{name}/SKILL.md") + text
            out[vault_rel] = body.encode("utf-8")

    for svg in sorted((DOCS / "figures").glob("*.svg")):
        out[f"04 - Architecture/figures/{svg.name}"] = svg.read_bytes()

    # The logo is a projection of docs/assets/branding/aethrion-logo.png, kept
    # byte-identical. Obsidian resolves ``![[aethrion-logo.png]]`` by filename,
    # so the landing page needs a copy that lives inside the vault.
    out["_assets/aethrion-logo.png"] = (DOCS / "assets" / "branding" / "aethrion-logo.png").read_bytes()

    # Skill notes live under their group folder in the vault, so a link to
    # ``name/SKILL.md`` has to carry the group or it lands nowhere.
    group_of = {name: group for group, names in GROUPS.items() for name in names}
    text = (SKILLS / "README.md").read_text(encoding="utf-8")

    def _skill_link(match: re.Match[str]) -> str:
        name = match.group(1)
        group = group_of.get(name)
        return f"]({group}/{name}.md)" if group else match.group(0)

    text = re.sub(r"\]\((?!http)([a-z0-9-]+)/SKILL\.md\)", _skill_link, text)
    # skills/README.md reaches the architecture corpus as ``../docs/...``; the
    # same mapping used for the mirrored documents applies here.
    for src, vault in src_to_vault.items():
        text = text.replace(f"](../{src})", f"]({os.path.relpath(vault, '07 - Skills')})")
    out["07 - Skills/skills_index.md"] = (
        vault_frontmatter.derive(
            vault_rel="07 - Skills/skills_index.md", source="skills/README.md",
            text=text, generator="mirror_vault.py")
        + BANNER.format(source="skills/README.md") + text
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
    written = 0
    for rel, payload in generated.items():
        path = args.target / rel
        if args.check:
            if not path.exists():
                drift.append(f"missing: {rel}")
            elif path.read_bytes() != payload:
                drift.append(f"differs: {rel}")
            continue
        if path.is_file() and path.read_bytes() == payload:
            continue          # byte-identical: leave the file, and its mtime, alone
        if _is_human_note(path):
            raise SystemExit(
                f"refusing to overwrite a hand-authored note: {rel}\n"
                "  its frontmatter says `generated: false`, so it is somebody's\n"
                "  writing, not a projection. Give the mirrored page its own name."
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        written += 1

    if args.check:
        for line in drift:
            print(line)
        print(f"{len(generated)} generated files, {len(drift)} drift entries")
        return 1 if drift else 0

    print(f"{len(generated)} files to {args.target} — {written} written, "
          f"{len(generated) - written} unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
