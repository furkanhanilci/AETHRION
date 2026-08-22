#!/usr/bin/env python3
"""Colour the whole vault, not only the graph.

Why this exists
    `make_vault_graph.py` colours nodes in the graph view. That is one surface.
    A reader spends most of their time in the file explorer, in a note's
    properties and in search results — and in all three, 652 pages look identical.

    This generates a CSS snippet so the same distinction carries everywhere: the
    same eight colours, meaning the same eight things, in the explorer, on tag
    pills, on the `type` property, in the graph legend and on callouts.

    Obsidian loads `.obsidian/snippets/*.css` natively. No plugin, no theme, and
    nothing that breaks when the vault is opened somewhere else — an unrecognised
    snippet is simply not enabled.

Palette
    Okabe-Ito, the same set `scripts/figure_kit.py` uses for the published
    figures and `make_vault_graph.py` uses for the graph. One colour means one
    thing across the repository's diagrams and the vault's surfaces.

    Chosen because it stays distinguishable under the common forms of colour
    vision deficiency. And **colour never carries a distinction alone**: every
    rule below keys off a tag or a path that is equally visible in search, in a
    query and on the taxonomy page.

Both themes
    Every colour is applied through a CSS variable defined once for light and
    once for dark, so a reader who switches theme does not lose the mapping.

Usage
    python3 scripts/make_vault_theme.py <vault>            # write the snippet
    python3 scripts/make_vault_theme.py <vault> --check    # fail on drift
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import make_vault_graph as graph

SNIPPET_NAME = "aethrion.css"

# (variable, light, dark, what it means). Dark variants are lifted slightly so
# they hold contrast against a dark background rather than sinking into it.
TOKENS = [
    ("pending", graph.VERM, "#FF7A33", "unauthored — waiting on judgement"),
    ("package", graph.ORANGE, "#FFB733", "work package — the sealed plan"),
    ("tests", graph.GREEN, "#00C795", "test procedure — mechanical check"),
    ("acceptance", graph.BLUE, "#3FA9E0", "acceptance criteria — the verifier's document"),
    ("scenario", graph.PURPLE, "#E58FBE", "acceptance scenario"),
    ("architecture", graph.SKY, "#7FC9F0", "architecture and decision records"),
    ("source", graph.YELLOW, "#FFF06A", "literature source — projected from Zotero"),
    ("index", graph.MUTE, "#9BA0A6", "index and navigation"),
    ("human", graph.TEAL, "#5FD3C0", "human synthesis — the second brain"),
    ("workspace", graph.WINE, "#C7538A", "project workspace — cockpit, status, evidence"),
]

# Top-level vault areas, coloured in the file explorer so the shape of the vault
# is legible before anything is opened.
AREAS = [
    ("00 - Home", "index"),
    ("01 - Inbox", "human"),
    ("10 - Projects", "package"),
    ("20 - Source Notes", "human"),
    ("30 - Concepts", "human"),
    ("40 - Claims", "human"),
    ("50 - Decisions", "human"),
    ("60 - Runs", "human"),
    ("70 - Literature Sets", "source"),
    ("80 - Daily", "index"),
    ("90 - Archive", "human"),
    ("_Templates", "index"),
    ("_meta", "index"),
]

# The project subtree. Colouring only the top level left the seven areas a reader
# actually navigates — commissioning, reviews, implementation, architecture,
# evidence, components, skills — visually identical.
SUBAREAS = [
    ("10 - Projects/AETHRION/01 - Commissioning", "package"),
    ("10 - Projects/AETHRION/02 - Reviews", "scenario"),
    ("10 - Projects/AETHRION/03 - Implementation", "workspace"),
    ("10 - Projects/AETHRION/04 - Architecture", "architecture"),
    ("10 - Projects/AETHRION/05 - Evidence", "workspace"),
    ("10 - Projects/AETHRION/06 - Components", "workspace"),
    ("10 - Projects/AETHRION/07 - Skills", "acceptance"),
    ("70 - Literature Sets/Zotero Sources", "source"),
]

# Tag namespace -> token. Longest prefix wins, so the specific rules are emitted
# after the general ones.
TAGS = [
    ("aethrion/index", "index"),
    ("aethrion/source", "source"),
    ("aethrion/architecture", "architecture"),
    ("aethrion/adr", "architecture"),
    ("aethrion/skill", "acceptance"),
    ("aethrion/review", "scenario"),
    ("aethrion/acceptance-scenario", "scenario"),
    ("aethrion/work-package", "package"),
    ("aethrion/commissioning", "package"),
    ("aethrion/test-procedure", "tests"),
    ("aethrion/acceptance-criteria", "acceptance"),
    ("aethrion/authoring/pending", "pending"),
    ("aethrion/claim", "human"),
    ("aethrion/concept", "human"),
    ("aethrion/decision", "human"),
    ("aethrion/run", "human"),
    ("aethrion/source-note", "human"),
    ("aethrion/literature-set", "human"),
    ("aethrion/inbox", "human"),
    ("aethrion/archive", "human"),
    ("aethrion/daily", "index"),
    ("aethrion/project", "workspace"),
    ("aethrion/plan", "workspace"),
    ("aethrion/cockpit", "workspace"),
    ("aethrion/status", "workspace"),
    ("aethrion/roadmap", "workspace"),
    ("aethrion/handover", "workspace"),
    ("aethrion/execution", "workspace"),
    ("aethrion/evidence", "workspace"),
    ("aethrion/component", "workspace"),
]

# The `type` property, shown on every generated page.
TYPES = [
    ("work-package", "package"),
    ("test-procedure", "tests"),
    ("acceptance-criteria", "acceptance"),
    ("acceptance-scenario", "scenario"),
    ("decision-record", "architecture"),
    ("reference", "architecture"),
    ("skill", "acceptance"),
    ("review", "scenario"),
    ("source", "source"),
    ("index", "index"),
    ("evidence", "workspace"),
    ("claim", "human"),
    ("concept", "human"),
    ("decision", "human"),
    ("run", "human"),
    ("source-note", "human"),
    ("literature-set", "human"),
    ("project", "workspace"),
]


def render() -> str:
    out: list[str] = [
        "/* AETHRION — vault-wide colouring.",
        " *",
        " * GENERATED by scripts/make_vault_theme.py. Editing this file is lost on",
        " * the next mirror; change the generator instead.",
        " *",
        " * The palette is Okabe-Ito, the same set used by the published figures",
        " * (scripts/figure_kit.py) and the graph view (scripts/make_vault_graph.py),",
        " * so one colour means one thing across every surface.",
        " *",
        " * Colour never carries a distinction on its own: every rule below keys off",
        " * a tag or a path that is equally visible in search, in a query and on",
        " * [[_meta/taxonomy]]. A reader who cannot use the colour loses nothing but",
        " * the shortcut.",
        " */",
        "",
        ".theme-light {",
    ]
    for name, light, _dark, why in TOKENS:
        out.append(f"  --aethrion-{name}: {light};   /* {why} */")
    out += ["}", "", ".theme-dark {"]
    for name, _light, dark, why in TOKENS:
        out.append(f"  --aethrion-{name}: {dark};   /* {why} */")
    out += ["}", "",
            "/* ---- file explorer: the shape of the vault before anything is opened ---- */",
            ""]
    for area, token in AREAS:
        out.append(f'.nav-folder-title[data-path="{area}" i] .nav-folder-title-content,')
        out.append(f'.nav-file-title[data-path^="{area}/" i] .nav-file-title-content {{')
        out.append(f"  border-left: 3px solid var(--aethrion-{token});")
        out.append("  padding-left: 6px;")
        out.append("}")
        out.append("")

    out += ["/* The project subtree — the seven areas a reader actually navigates. */", ""]
    for area, token in SUBAREAS:
        out.append(f'.nav-folder-title[data-path="{area}" i] .nav-folder-title-content,')
        out.append(f'.nav-file-title[data-path^="{area}/" i] .nav-file-title-content {{')
        out.append(f"  border-left: 3px solid var(--aethrion-{token});")
        out.append("  padding-left: 6px;")
        out.append("}")
        out.append("")

    out += ["/* The three documents of a package, separated in the explorer. The suffix",
            " * is the distinction, so this reinforces a name rather than replacing it. */",
            "",
            '.nav-file-title[data-path$=".tests.md" i] .nav-file-title-content {',
            "  color: var(--aethrion-tests);", "}", "",
            '.nav-file-title[data-path$=".acceptance.md" i] .nav-file-title-content {',
            "  color: var(--aethrion-acceptance);", "}", "",
            "/* ---- tag pills ---- */", ""]
    for tag, token in TAGS:
        out.append(f'.tag[href^="#{tag}"], a.tag[href^="#{tag}"] {{')
        out.append(f"  background-color: color-mix(in srgb, var(--aethrion-{token}) 22%, transparent);")
        out.append(f"  border: 1px solid var(--aethrion-{token});")
        out.append("  color: var(--text-normal);")
        out.append("}")
        out.append("")

    out += ["/* ---- the `type` property, shown on every generated page ---- */", ""]
    for value, token in TYPES:
        out.append(f'.metadata-property[data-property-key="type"] '
                   f'.metadata-input-longtext[value="{value}" i],')
        out.append(f'.metadata-property[data-property-key="type"]:has([value="{value}" i]) '
                   f'.metadata-property-key {{')
        out.append(f"  color: var(--aethrion-{token});")
        out.append("  font-weight: 600;")
        out.append("}")
        out.append("")

    out += [
        "/* ---- the status property ---- */",
        "",
        '.metadata-property[data-property-key="status"] .metadata-property-key {',
        "  color: var(--aethrion-index);",
        "}",
        "",
        "/* ---- generated-view banner ---- */",
        "",
        "/* Every projected page opens with a `> [!info] Generated view` callout.",
        " * Tinting it means a reader can tell a projection from an original before",
        " * reading the words — which is the distinction most likely to be missed. */",
        ".callout[data-callout='info'] {",
        "  --callout-color: 99, 102, 106;",
        "}",
        "",
        "/* A warning callout marks the two places this vault destroys work: the",
        " * generated literature area and the plan mirror. Keep it loud. */",
        ".callout[data-callout='warning'] {",
        "  --callout-color: 213, 94, 0;",
        "}",
        "",
        "/* ---- search results ---- */",
        "",
        ".search-result-file-title:has([data-path$='.tests.md' i]) {",
        "  color: var(--aethrion-tests);",
        "}",
        "",
        ".search-result-file-title:has([data-path$='.acceptance.md' i]) {",
        "  color: var(--aethrion-acceptance);",
        "}",
        "",
    ]
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    snippet = args.vault / ".obsidian" / "snippets" / SNIPPET_NAME
    appearance = args.vault / ".obsidian" / "appearance.json"
    wanted = render()

    config = json.loads(appearance.read_text(encoding="utf-8")) if appearance.is_file() else {}
    enabled = list(dict.fromkeys([*config.get("enabledCssSnippets", []), "aethrion"]))
    wanted_config = {**config, "enabledCssSnippets": enabled}
    rendered_config = json.dumps(wanted_config, indent=2, ensure_ascii=False) + "\n"

    drift = []
    if not snippet.is_file() or snippet.read_text(encoding="utf-8") != wanted:
        drift.append(".obsidian/snippets/" + SNIPPET_NAME)
    if not appearance.is_file() or appearance.read_text(encoding="utf-8") != rendered_config:
        drift.append(".obsidian/appearance.json")

    if args.check:
        for entry in drift:
            print(f"  ✗ {entry} does not match the generator")
        print(f"{len(TOKENS)} colour tokens checked, {len(drift)} drift entries")
        return 1 if drift else 0

    snippet.parent.mkdir(parents=True, exist_ok=True)
    snippet.write_text(wanted, encoding="utf-8")
    appearance.write_text(rendered_config, encoding="utf-8")
    print(f"wrote the vault-wide snippet and enabled it in {args.vault}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
