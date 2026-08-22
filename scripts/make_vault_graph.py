#!/usr/bin/env python3
"""Colour the Obsidian graph from the vault's own tag vocabulary.

Why this exists
    A graph where every node is the same colour shows that the vault is connected
    and nothing else. Colouring by *kind* turns it into an instrument: the sealed
    plan, the procedures that test it, the criteria that accept it, the literature
    it stands on and the skills that execute it become separable at a glance, and
    the thing you are looking for is the shape that is missing.

    The most useful group is the one that marks absence — `authoring/pending`.
    A cluster of pending nodes around one workstream is a real fact about the
    programme that no status page states as directly.

Palette
    The same **Okabe-Ito** set the figures use (`scripts/figure_kit.py`), so the
    vault graph and the published diagrams mean the same thing by the same colour.
    Okabe-Ito is chosen because it stays distinguishable under the common forms of
    colour vision deficiency — a graph legible only to trichromats is a graph with
    a silent readership limit.

    Colour carries meaning here, and never carries it alone: every group is also a
    tag, so the same distinction survives in search, in queries and in the
    taxonomy page for a reader who cannot use the colour at all.

Mutual exclusion
    Obsidian applies one group per node, and the resolution order between
    overlapping groups is not something to depend on. Every query below is
    therefore written to be **mutually exclusive** with `-tag:` exclusions, so the
    result does not change if that order does.

Invariant
    Generated from `vault_frontmatter.taxonomy()`. A tag that is not in the
    controlled vocabulary cannot be coloured, and a group whose tag has been
    retired fails `--check` rather than silently matching nothing.

Usage
    python3 scripts/make_vault_graph.py <vault>            # write graph.json
    python3 scripts/make_vault_graph.py <vault> --check    # fail on drift
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import make_vault_theme as theme
import vault_frontmatter

# Okabe-Ito, matching scripts/figure_kit.py. The comment on each line is the
# meaning that colour already carries in the figures, so the two agree.
BLUE = "#0072B2"      # model production
ORANGE = "#E69F00"    # frozen artifact
GREEN = "#009E73"     # mechanical check
VERM = "#D55E00"      # human authority
PURPLE = "#CC79A7"    # revision / feedback
SKY = "#56B4E9"       # reference material
YELLOW = "#F0E442"    # external source
MUTE = "#63666A"      # navigation

# Two additions from Paul Tol's muted palette, chosen because they stay
# distinguishable alongside Okabe-Ito under the same colour-vision conditions.
# They separate the vault's two halves: the projection of the repository, and
# the second brain the researcher writes in.
TEAL = "#44AA99"      # human synthesis — the second brain
WINE = "#882255"      # project workspace — cockpit, status, evidence, components

# (label, query, colour, why this colour). Order is presentational only — the
# queries are mutually exclusive, so it does not decide anything.
GROUPS = [
    ("Unauthored — needs work",
     "tag:#aethrion/authoring/pending",
     VERM,
     "human authority: these are the documents waiting on judgement, and the "
     "cluster shape is the most useful thing the graph shows"),

    ("Work package",
     "tag:#aethrion/work-package -tag:#aethrion/test-procedure "
     "-tag:#aethrion/acceptance-criteria",
     ORANGE,
     "frozen artifact: the sealed plan"),

    ("Test procedure",
     "tag:#aethrion/test-procedure -tag:#aethrion/authoring/pending",
     GREEN,
     "mechanical check: how a package is tested"),

    ("Acceptance criteria",
     "tag:#aethrion/acceptance-criteria -tag:#aethrion/authoring/pending",
     BLUE,
     "the verifier's document — read by someone who did not do the work"),

    ("Acceptance scenario",
     "tag:#aethrion/acceptance-scenario",
     PURPLE,
     "revision / feedback: what the system must demonstrate end to end"),

    ("Architecture and decisions",
     "tag:#aethrion/architecture",
     SKY,
     "reference material: the target design and its ADRs"),

    ("Skill",
     "tag:#aethrion/skill",
     BLUE,
     "model production: the discipline agents execute under"),

    ("Literature source",
     "tag:#aethrion/source",
     YELLOW,
     "external source: projected from Zotero, never authored here"),

    ("Index and navigation",
     "tag:#aethrion/index -tag:#aethrion/source",
     MUTE,
     "navigation: hubs rather than content"),

    ("Review and findings",
     "tag:#aethrion/review",
     PURPLE,
     "revision / feedback: frozen audits and the findings register"),

    # The groups below were added after an audit found 30 nodes taking no colour
    # at all: the programme documents, the project workspace, the human areas,
    # the daily notes and the templates. A node with no group is a node the graph
    # cannot say anything about, which is the one thing this view exists to fix.

    ("Programme document",
     "tag:#aethrion/commissioning -tag:#aethrion/work-package "
     "-tag:#aethrion/acceptance-scenario -tag:#aethrion/index",
     ORANGE,
     "frozen artifact: 00_PROGRAM is the plan's own constitution, so it shares "
     "the plan's colour"),

    ("Project workspace",
     "tag:#aethrion/project OR tag:#aethrion/plan OR tag:#aethrion/cockpit OR "
     "tag:#aethrion/status OR tag:#aethrion/roadmap OR tag:#aethrion/handover OR "
     "tag:#aethrion/execution OR tag:#aethrion/evidence OR tag:#aethrion/component",
     WINE,
     "where the operator works: cockpit, status, handover, evidence, components"),

    ("Human synthesis",
     "tag:#aethrion/claim OR tag:#aethrion/concept OR tag:#aethrion/decision OR "
     "tag:#aethrion/run OR tag:#aethrion/source-note OR "
     "tag:#aethrion/literature-set OR tag:#aethrion/inbox OR tag:#aethrion/archive",
     TEAL,
     "the second brain: the areas a human writes in, distinct from everything "
     "projected from the repository"),

    ("Daily note",
     "tag:#aethrion/daily",
     MUTE,
     "navigation: entered by date rather than by link"),

    ("Template",
     'path:"_Templates"',
     MUTE,
     "navigation: deliberately unlinked, and not content"),

    # A note takes its colour from a tag; an attachment has no frontmatter and so
    # has no tag. The graph draws them anyway — nine figures, the logo, the seal
    # file, the dependency matrix and the projection manifest — and every one of
    # them was a grey dot among 670 coloured ones. `path:` is the only predicate
    # that reaches a file with no metadata.
    ("Attachment and data file",
     'path:".svg" OR path:".png" OR path:".txt" OR path:".csv" OR path:".json"',
     YELLOW,
     "external source: figures and data files, carried rather than authored"),
]

# Settings worth fixing alongside the colours. Everything else in graph.json is
# the operator's own view state and is left exactly as found.
VIEW = {
    "showArrow": True,        # a knowledge graph without direction is a blob
    "showTags": False,        # tag nodes would swamp 650 pages
    "showOrphans": True,      # an orphan is a finding, so it must stay visible
    "textFadeMultiplier": -1.5,   # keep labels readable when zoomed out
    "collapse-color-groups": False,
}


def rgb_int(hex_colour: str) -> int:
    """Obsidian stores a colour as a decimal integer."""
    return int(hex_colour.lstrip("#"), 16)


def colour_groups() -> list[dict]:
    vocabulary = set(vault_frontmatter.taxonomy())
    unknown = []
    for label, query, _, _ in GROUPS:
        for token in query.split():
            if token == "OR" or token.startswith("path:"):
                continue
            tag = token.lstrip("-").removeprefix("tag:#")
            if tag.startswith("aethrion/") and tag not in vocabulary:
                unknown.append((label, tag))
    if unknown:
        for label, tag in unknown:
            print(f"  ✗ group {label!r} matches `{tag}`, which is not in the "
                  f"controlled vocabulary", file=sys.stderr)
        raise SystemExit(1)
    return [{"query": query, "color": {"a": 1, "rgb": rgb_int(colour)}}
            for _, query, colour, _ in GROUPS]


def build(existing: dict) -> dict:
    out = dict(existing)
    out["colorGroups"] = colour_groups()
    out.update(VIEW)
    return out


def legend_page() -> str:
    lines = [
        "---",
        'title: "Graph Legend"',
        "type: index",
        "cssclasses:",
        "  - aethrion-index",
        "category: vault",
        "status: active",
        'summary: "What each colour in the graph view means, and why colour is '
        'never the only carrier of the distinction."',
        "generated: true",
        "provenance: scripts/make_vault_graph.py",
        "tags:",
        "  - aethrion/index",
        "---",
        "",
        "# Graph Legend",
        "",
        "> [!info] Generated view",
        "> Produced by `scripts/make_vault_graph.py`, which also writes",
        "> `.obsidian/graph.json`. Change the generator, not this page.",
        "",
        "The graph is coloured by **kind**, using the same Okabe-Ito palette as the",
        "figures in `docs/figures/` — so a colour means the same thing in a diagram",
        "and in the graph. Okabe-Ito is used because it stays distinguishable under",
        "the common forms of colour vision deficiency. Two colours from Paul Tol's",
        "muted palette were added to separate the vault's two halves: the projection",
        "of the repository, and the second brain the researcher writes in.",
        "",
        "**Every page takes a colour.** An audit found thirty nodes matching no group",
        "— the programme documents, the project workspace, the human areas, the daily",
        "notes and the templates — and a node with no group is a node the graph cannot",
        "say anything about, which is the one thing this view exists to fix.",
        "",
        "**Colour never carries a distinction alone.** Every group below is also a",
        "tag, so the same separation is available in search, in a query and in",
        "[[_meta/taxonomy|the taxonomy]] to a reader who cannot use the colour.",
        "",
        "| | Group | Tag | Why this colour |",
        "|---|---|---|---|",
    ]
    for label, query, colour, why in GROUPS:
        tag = query.split()[0].removeprefix("tag:#")
        swatch = f'<span style="display:inline-block;width:0.9em;height:0.9em;background:{colour};border-radius:2px"></span>'
        lines.append(f"| {swatch} `{colour}` | {label} | `{tag}` | {why} |")
    lines += [
        "",
        "## The group worth watching",
        "",
        "**Unauthored — needs work.** Every package is three documents, and the two",
        "companions carry judgement rather than derivation. An unauthored one says",
        "so rather than pretending otherwise, and in the graph they cluster: a dense",
        "patch of that colour around one workstream is a fact about the programme",
        "that no status page states as directly.",
        "",
        "Track the count on [[10 - Projects/AETHRION/authoring_progress|Authoring Progress]].",
        "",
        "## Where these colours appear",
        "",
        "The graph is one surface. `scripts/make_vault_theme.py` generates a CSS",
        "snippet — loaded natively from `.obsidian/snippets/`, no plugin — that",
        f"carries the same {len(theme.TOKENS)} colours to:",
        "",
        "| Surface | What is coloured |",
        "|---|---|",
        "| File explorer | Each top-level area gets a left border in its colour, so the shape of the vault is legible before anything is opened |",
        "| File explorer | `.tests.md` and `.acceptance.md` are tinted, separating a package's three documents at a glance |",
        "| Note body | Every page declares `cssclasses: [aethrion-<type>]`, so its headings, internal links, table headers, quotes and rules carry the page's own colour |",
        "| Side panels | Backlinks, outgoing links, the tag pane, the outline and bookmarks take the colour of what they are — navigation, structure, vocabulary |",
        "| Tag pills | Every `aethrion/` namespace takes its group colour |",
        "| The `type` property | Shown on every generated page, coloured by kind |",
        "| Search results | Test and acceptance documents are distinguishable in a result list |",
        "| Callouts | *Generated view* is muted; **warning** stays loud, because it marks the two places this vault destroys work |",
        "",
        "Every colour is defined twice — once for the light theme, once for dark —",
        "so switching theme does not lose the mapping.",
        "",
        "## Orphans stay visible",
        "",
        "`showOrphans` is on deliberately. An unreachable page is a finding —",
        "`scripts/check_vault.py` reports it in the verification bundle — and hiding",
        "it in the view would remove the only place it is obvious.",
        "",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    config = args.vault / ".obsidian" / "graph.json"
    legend = args.vault / "10 - Projects" / "AETHRION" / "graph_legend.md"

    existing = json.loads(config.read_text(encoding="utf-8")) if config.is_file() else {}
    wanted = build(existing)
    rendered = json.dumps(wanted, indent=2, ensure_ascii=False) + "\n"
    wanted_legend = legend_page()

    drift = []
    if not config.is_file() or config.read_text(encoding="utf-8") != rendered:
        drift.append(str(config.relative_to(args.vault)))
    if not legend.is_file() or legend.read_text(encoding="utf-8") != wanted_legend:
        drift.append(str(legend.relative_to(args.vault)))

    if args.check:
        for entry in drift:
            print(f"  ✗ {entry} does not match the generator")
        print(f"{len(GROUPS)} colour groups checked, {len(drift)} drift entries")
        return 1 if drift else 0

    config.parent.mkdir(parents=True, exist_ok=True)
    config.write_text(rendered, encoding="utf-8")
    legend.parent.mkdir(parents=True, exist_ok=True)
    legend.write_text(wanted_legend, encoding="utf-8")
    print(f"wrote {len(GROUPS)} colour groups and the legend to {args.vault}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
