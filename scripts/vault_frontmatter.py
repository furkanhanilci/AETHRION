#!/usr/bin/env python3
"""Derive the Obsidian frontmatter for a mirrored page.

Why this exists
    The repository writes documents to `docs/DOCUMENT_STANDARD.md`, whose header
    is a ``| Field | Value |`` table. Obsidian cannot read that table: its
    queries, its Bases, its graph colouring and its `aliases` resolution all read
    **YAML frontmatter**, and the mirrors copied the canonical text verbatim.

    The measured consequence was that 302 of the 306 mirrored pages carried no
    frontmatter at all, so the vault's own landing page — which runs
    ``query path:"10 - Projects" ["status":"active"]`` — returned nothing, and no
    mirrored page could be reached by tag, status or type. A second brain whose
    pages cannot be queried is a folder of files.

    This module does not change the document standard. It **adds** the Obsidian
    layer at projection time, derived from the canonical content, so the vault
    gains metadata the repository never has to carry.

Invariant
    Every field is derived from canonical content or from the unsealed progress
    ledger. **Nothing here reads a wall clock.** A `generated_at` refreshed on
    every mirror run would rewrite all 306 pages every time, which is the same
    defect the projection and the status page were both fixed for.

Provenance
    The field set follows the page schema used by ``Ar9av/obsidian-wiki``
    (title · category · tags · sources · summary), adapted to AETHRION's own
    vocabulary: `type` and `status` come from `docs/DOCUMENT_STANDARD.md`, and
    `source` is a single canonical path rather than a list, because a mirrored
    page has exactly one source of truth and naming it is the point.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MATRIX = REPO / "planning" / "commissioning" / "00_PROGRAM" / "package_dependency_matrix.csv"
PROGRESS = REPO / "delivery" / "progress.json"

# Wave membership, mirroring 00_PROGRAM/02_wave_and_dependency_map.md.
_WAVES = [
    ("wb", {0}), ("w0", set(range(1, 11))), ("w1", set(range(11, 21))),
    ("w2", set(range(21, 32)) | {51} | set(range(55, 60))),
    ("w3", set(range(32, 51)) | {52, 53, 54, 60}),
    ("w4", set(range(61, 91))), ("w5", set(range(91, 102))),
    ("w6", set(range(102, 116))), ("w7", set(range(116, 120))),
    ("w8", {120, 121}), ("w9", set(range(122, 131))), ("wt", set(range(131, 141))),
    ("ws", set(range(141, 148))), ("wr", set(range(148, 160))),
]


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


def _yaml(value: str) -> str:
    """Quote deterministically; a title with a colon is otherwise invalid YAML."""
    return json.dumps(value, ensure_ascii=False)


def _packages() -> dict[str, dict[str, str]]:
    if not MATRIX.is_file():
        return {}
    return {row["package_id"]: row for row in csv.DictReader(MATRIX.open(encoding="utf-8"))}


def _progress() -> dict[str, str]:
    if not PROGRESS.is_file():
        return {}
    data = json.loads(PROGRESS.read_text(encoding="utf-8"))
    return {pid: entry.get("state", "") for pid, entry in data.get("packages", {}).items()}


_PACKAGES = _packages()
_PROGRESS = _progress()


def _title(text: str, fallback: str) -> str:
    """The document's own title.

    Two cases the naive "first ``#`` line" rule gets wrong, both found in the
    corpus. ``README.md`` centres its title in an ``<h1>`` tag for GitHub and its
    first Markdown heading is a section 130 lines down, so the naive rule titled
    the repository index *Architecture* — colliding with the architecture index,
    which is genuinely called that. And a document whose first heading is a
    ``##`` has no title of its own; a ``#`` appearing later is a section.
    """
    html = re.search(r"<h1[^>]*>\s*(.+?)\s*</h1>", text, re.I | re.S)
    first = re.search(r"^(#{1,6})\s+(.+?)\s*$", text, re.M)
    if html and (first is None or html.start() < first.start()):
        return re.sub(r"<[^>]+>", "", html.group(1)).strip()
    if first and first.group(1) == "#":
        return first.group(2).strip()
    return fallback


def _status(text: str) -> str:
    """The controlled-vocabulary status from the document's own header table."""
    match = re.search(r"^\|\s*Status\s*\|\s*(.+?)\s*\|", text, re.M)
    if not match:
        return ""
    raw = match.group(1)
    known = re.search(r"`?(WORKING|TECH_COMPLETE|ACCEPTED|SPECIFIED|PROPOSED|"
                      r"DESIGNED|DEPRECATED)`?", raw)
    return known.group(1) if known else ""


def _summary(text: str) -> str:
    """The document's own one-paragraph statement, or the first real sentence."""
    match = re.search(r"\*\*In one paragraph\.\*\*\s*(.+?)(?:\n\n|\Z)", text, re.S)
    if not match:
        match = re.search(r"^##\s+Purpose[^\n]*\n+(.+?)(?:\n\n|\Z)", text, re.S | re.M)
    if not match:
        return ""
    body = " ".join(match.group(1).split())
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)      # links → their text
    body = re.sub(r"[*`_]", "", body)
    sentence = re.split(r"(?<=[.!?])\s+", body)[0]
    return sentence[:300].strip()


def _wave(number: int) -> str:
    for name, members in _WAVES:
        if number in members:
            return name
    return "unassigned"


def _work_package(pid: str, text: str) -> tuple[str, list[str], list[str], str]:
    row = _PACKAGES.get(pid, {})
    number = int(pid.split("-")[1])
    tags = [
        "aethrion/commissioning",
        "aethrion/work-package",
        f"aethrion/workstream/{_slug(row.get('workstream', 'unassigned'))}",
        f"aethrion/wave/{_wave(number)}",
    ]
    if row.get("effort"):
        tags.append(f"aethrion/effort/{row['effort'].lower()}")
    for gate in re.split(r"[;,]", row.get("gates", "")):
        gate = gate.strip()
        if gate:
            tags.append(f"aethrion/gate/{_slug(gate)}")
    state = _PROGRESS.get(pid, "NOT_STARTED")
    tags.append(f"aethrion/state/{_slug(state)}")
    aliases = [pid, f"{pid} — {_title(text, pid).split('—', 1)[-1].strip()}"]
    return "work-package", tags, aliases, state


# The project-root maps are cited across the corpus by their repository
# filename. Without an alias `[[AGENTS]]` resolves to nothing in the vault.
# `CLAUDE.md` opens with `# AETHRION` because it sits beside `README.md` in a
# repository that is called that. As a page among 668 others the heading is not a
# title — it collides with the repository index and tells a reader nothing about
# what the note holds. Only a document whose repository heading is written for a
# different context belongs here.
_ROOT_TITLES = {
    "claude_code_operating_notes.md": "Claude Code Operating Notes",
}

_ROOT_ALIASES = {
    "aethrion_repository_index.md": ["README", "Repository Index"],
    "agent_operating_manual.md": ["AGENTS", "AGENTS.md", "Operating Manual"],
    "claude_code_operating_notes.md": ["CLAUDE", "CLAUDE.md"],
    "documentation_index.md": ["docs/README", "Documentation Index"],
}


def derive(*, vault_rel: str, source: str, text: str, generator: str) -> str:
    """Return the YAML frontmatter block for one mirrored page."""
    stem = Path(vault_rel).stem
    title = _title(text, stem)
    aliases: list[str] = []
    status = _status(text)

    # A package is three documents; each is a different type in the vault so a
    # query can ask for "every acceptance criteria document still unauthored".
    companion = re.match(r"^wp_(\d{3})_.+\.(tests|acceptance)$", stem)
    if companion:
        pid = f"WP-{companion.group(1)}"
        kind = companion.group(2)
        page_type = "test-procedure" if kind == "tests" else "acceptance-criteria"
        _, base_tags, _, state = _work_package(pid, text)
        tags = [t for t in base_tags] + [f"aethrion/{page_type}"]
        authored = "Not yet authored" not in text
        tags.append(f"aethrion/authoring/{'authored' if authored else 'pending'}")
        lines = ["---", f"title: {_yaml(title)}", "aliases:",
                 f"  - {_yaml(f'{pid} {kind}')}",
                 f"cssclasses:", f"  - aethrion-{page_type}",
                 f"type: {page_type}", "category: commissioning",
                 f"status: {state}",
                 f"source: {_yaml(source)}", "generated: false",
                 f"provenance: {generator}", "tags:"]
        lines += [f"  - {tag}" for tag in dict.fromkeys(tags)]
        lines.append("---")
        return "\n".join(lines) + "\n\n"

    wp = re.match(r"^wp_(\d{3})_", stem)
    acc = re.match(r"^acc_(\d{2})_", stem)

    if wp:
        pid = f"WP-{wp.group(1)}"
        page_type, tags, aliases, status = _work_package(pid, text)
        category = "commissioning"
    elif acc:
        sid = f"ACC-{acc.group(1)}"
        page_type, category = "acceptance-scenario", "commissioning"
        severity = re.search(r"\|\s*Severity\s*\|\s*\*\*(.+?)\*\*", text)
        phase = re.search(r"\|\s*Acceptance phase\s*\|\s*`(.+?)`", text)
        tags = ["aethrion/commissioning", "aethrion/acceptance-scenario"]
        if severity:
            tags.append(f"aethrion/severity/{_slug(severity.group(1))}")
        if phase:
            tags.append(f"aethrion/phase/{_slug(phase.group(1))}")
        aliases = [sid]
    elif vault_rel.startswith("07 - Skills/"):
        page_type, category = "skill", "skill"
        domain = re.search(r'airl\.domain:\s*"?([\w-]+)', text)
        origin = re.search(r'airl\.origin:\s*"?([\w-]+)', text)
        tags = ["aethrion/skill"]
        if domain:
            tags.append(f"aethrion/skill-family/{_slug(domain.group(1))}")
        if origin:
            tags.append(f"aethrion/skill-origin/{_slug(origin.group(1))}")
        aliases = [stem]
        status = status or "WORKING"
    elif vault_rel.startswith("02 - Reviews/"):
        page_type, category = "review", "review"
        tags = ["aethrion/review"]
    elif re.match(r"^04 - Architecture/adr_\d+", vault_rel):
        page_type, category = "decision-record", "architecture"
        tags = ["aethrion/architecture", "aethrion/adr"]
        aliases = [stem.replace("adr_", "ADR-").replace("_", " ", 1).split(" ")[0].upper()]
    elif vault_rel.startswith("04 - Architecture/"):
        page_type, category = "reference", "architecture"
        tags = ["aethrion/architecture"]
    elif vault_rel.startswith("03 - Implementation/"):
        page_type = "index" if stem.endswith("_index") else "reference"
        category = "implementation"
        tags = ["aethrion/execution"]
    elif vault_rel.startswith("05 - Evidence/"):
        page_type = "index" if stem.endswith("_index") else "reference"
        category = "evidence"
        tags = ["aethrion/evidence"]
    elif vault_rel.startswith("06 - Components/"):
        page_type = "index" if stem.endswith("_index") else "reference"
        category = "component"
        tags = ["aethrion/component"]
    elif "/" not in vault_rel:
        # The project root holds the repository's own maps: its front door, its
        # operating manual and the index of `docs/`. They are the entry points to
        # everything below, so they are typed as indexes wherever a reader lands.
        page_type, category = "index", "project"
        tags = ["aethrion/project"]
        aliases = _ROOT_ALIASES.get(vault_rel, [])
        title = _ROOT_TITLES.get(vault_rel, title)
    elif stem.endswith("_index") or stem == "commissioning_index":
        page_type, category = "index", "commissioning"
        tags = ["aethrion/index"]
    elif stem == "README":
        page_type, category = "index", "commissioning"
        tags = ["aethrion/index", "aethrion/workstream-index"]
    else:
        page_type, category = "reference", "commissioning"
        tags = ["aethrion/commissioning"]

    # An index is an index in whichever area it lives, and the graph colours and
    # the vault's own queries read this tag rather than the folder name.
    if page_type == "index" and "aethrion/index" not in tags:
        tags = tags + ["aethrion/index"]

    lines = ["---", f"title: {_yaml(title)}"]
    if aliases:
        lines.append("aliases:")
        lines += [f"  - {_yaml(a)}" for a in dict.fromkeys(a for a in aliases if a)]
    # `cssclasses` is Obsidian's own hook for styling a note's body. Without it a
    # page's colour stopped at the file explorer and the graph: open the note and
    # its headings, links, tables and quotes were the same default as every other
    # page. The class carries the type, so the snippet colours the body from the
    # same mapping the explorer and the graph already use.
    lines += ["cssclasses:", f"  - aethrion-{page_type}",
              f"type: {page_type}", f"category: {category}"]
    if status:
        lines.append(f"status: {status}")
    summary = _summary(text)
    if summary:
        lines.append(f"summary: {_yaml(summary)}")
    lines += [
        f"source: {_yaml(source)}",
        "generated: true",
        f"provenance: {generator}",
        "tags:",
    ]
    lines += [f"  - {tag}" for tag in dict.fromkeys(tags)]
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def taxonomy() -> list[str]:
    """Every tag this module can emit — the controlled vocabulary, derived."""
    tags = {
        "aethrion/commissioning", "aethrion/work-package",
        "aethrion/acceptance-scenario", "aethrion/architecture", "aethrion/adr",
        "aethrion/review", "aethrion/skill", "aethrion/index",
        "aethrion/workstream-index",
    }
    for row in _PACKAGES.values():
        tags.add(f"aethrion/workstream/{_slug(row['workstream'])}")
        if row.get("effort"):
            tags.add(f"aethrion/effort/{row['effort'].lower()}")
        for gate in re.split(r"[;,]", row.get("gates", "")):
            if gate.strip():
                tags.add(f"aethrion/gate/{_slug(gate)}")
    for name, _ in _WAVES:
        tags.add(f"aethrion/wave/{name}")
    for state in ("NOT_STARTED", "IN_PROGRESS", "TECH_COMPLETE", "ACCEPTED",
                  "INTEGRATED", "BLOCKED"):
        tags.add(f"aethrion/state/{_slug(state)}")
    for severity in ("Critical", "High", "Medium", "Low"):
        tags.add(f"aethrion/severity/{_slug(severity)}")
    for phase in ("PRE_GO_LIVE", "DAY2_CONTINUOUS"):
        tags.add(f"aethrion/phase/{_slug(phase)}")
    for family in ("engineering", "scientific-research", "shared"):
        tags.add(f"aethrion/skill-family/{family}")
    for origin in ("airl-native", "superpowers"):
        tags.add(f"aethrion/skill-origin/{origin}")

    # The human areas of the vault. These are not generated, but they are part
    # of the same vocabulary: a tag invented on the spot fragments a concept
    # into two nodes a query cannot join.
    tags |= {
        "aethrion/project", "aethrion/plan", "aethrion/cockpit",
        "aethrion/status", "aethrion/roadmap", "aethrion/handover",
        "aethrion/execution", "aethrion/evidence", "aethrion/component",
        "aethrion/daily", "aethrion/inbox", "aethrion/archive",
        "aethrion/concept", "aethrion/claim", "aethrion/decision",
        "aethrion/run", "aethrion/source-note", "aethrion/literature-set",
        "aethrion/foundation", "aethrion/contracts",
    }
    # The bridge projection. Emitted by src/airl_bridge/obsidian.py, which is
    # the only writer outside these mirrors.
    tags |= {"aethrion/test-procedure", "aethrion/acceptance-criteria",
             "aethrion/authoring/authored", "aethrion/authoring/pending"}
    tags |= {"aethrion/source", "aethrion/has-doi",
             "aethrion/source-catalog", "aethrion/duplicate-review"}
    # Read from the source text rather than importing: these scripts run under a
    # bare `python3`, and airl_bridge.catalog pulls in pydantic through models.
    catalog = (REPO / "src" / "airl_bridge" / "catalog.py").read_text(encoding="utf-8")
    for item_type, folder in re.findall(r'"(\w+)":\s*"([^"]+)"', catalog):
        tags.add(f"aethrion/source-category/{_slug(folder)}")
        tags.add(f"aethrion/item-type/{item_type.lower()}")
    for folder in re.findall(r'DEFAULT_SOURCE_FOLDER\s*=\s*"([^"]+)"', catalog):
        tags.add(f"aethrion/source-category/{_slug(folder)}")
    return sorted(tags)


def taxonomy_page() -> str:
    """`_meta/taxonomy.md` — the vocabulary as a note, so the vault documents itself.

    Generated, and deliberately so: a controlled vocabulary maintained by hand
    is the thing it exists to prevent.
    """
    groups: dict[str, list[str]] = {}
    for tag in taxonomy():
        parts = tag.split("/")
        key = "/".join(parts[:2]) if len(parts) > 2 else "top level"
        groups.setdefault(key, []).append(tag)

    lines = [
        "---",
        'title: "Tag Taxonomy"',
        "type: index",
        "cssclasses:",
        "  - aethrion-index",
        "category: vault",
        "status: active",
        'summary: "The controlled tag vocabulary. A tag outside this list '
        'fragments one idea into two nodes no query can join."',
        "generated: true",
        "provenance: scripts/vault_frontmatter.py",
        "tags:",
        "  - aethrion/index",
        "---",
        "",
        "# Tag Taxonomy",
        "",
        "> [!info] Generated view",
        "> Produced by `scripts/vault_frontmatter.py` and checked by",
        "> `scripts/check_vault.py`. Add a tag to the generator, not to this page.",
        "",
        f"**{len(taxonomy())} tags.** Every tag under the `aethrion/` namespace that any "
        "writer into this vault may emit — the two mirrors and the bridge projection. "
        "A tag outside this list is a lint finding, because "
        "`aethrion/work-package` and `aethrion/workpackage` are one idea to a reader "
        "and two nodes to a query.",
        "",
        "| Group | Tags |",
        "|---|---|",
    ]
    for key in sorted(groups):
        lines.append(f"| `{key}` | {' · '.join('`' + t + '`' for t in sorted(groups[key]))} |")
    lines += [
        "",
        "## Namespaces outside `aethrion/`",
        "",
        "`silbo/*` marks a deliberately separate subproject and is not governed here.",
        "`zotero_tags` in a projected source note is the human author's own keyword "
        "list, reproduced faithfully and never normalised — it is data, not vocabulary.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, metavar="VAULT",
                        help="write <VAULT>/_meta/taxonomy.md")
    args = parser.parse_args()
    if args.write:
        out = args.write / "_meta" / "taxonomy.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(taxonomy_page(), encoding="utf-8")
        print(f"wrote {out} — {len(taxonomy())} tags")
    else:
        print(f"{len(taxonomy())} tags in the controlled vocabulary")
        for tag in taxonomy():
            print(f"  {tag}")
