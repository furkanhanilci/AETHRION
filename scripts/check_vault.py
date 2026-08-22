#!/usr/bin/env python3
"""Lint the Obsidian vault: links, frontmatter, tag vocabulary, orphans.

Responsibility
    Obsidian is the human knowledge workspace — the second brain — and until now
    nothing checked it. The repository has twelve checks and the vault had none,
    so a broken link, a page no query could see, or a tag invented on the spot
    was invisible until somebody happened to click it.

    A vault is a graph, and the failure modes of a graph are structural: a link
    that resolves to nothing, a page nothing links to, a tag that fragments a
    concept into two ("aethrion/work-package" and "aethrion/workpackage" are two
    nodes to a query and one idea to a reader).

Provenance
    The check set is adapted from ``Ar9av/obsidian-wiki``'s ``lint.py`` — broken
    links, missing frontmatter, duplicate titles, orphan pages, controlled tag
    vocabulary. What differs is what counts as required: this vault's generated
    pages must name their canonical `source`, because a projection that cannot
    say what it is a projection of is indistinguishable from an original.

What it cannot see
    Whether a note is any good, whether a link is the *right* link, or whether
    the human areas hold anything at all. It checks that the graph is
    well-formed, which is a different claim from the vault being useful.

Exit codes
    0 — the vault is well-formed.  1 — findings.  2 — the vault is not there.

Usage
    python3 scripts/check_vault.py                       # the repository baseline
    python3 scripts/check_vault.py "<vault path>"        # the operator's vault
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import vault_frontmatter

DEFAULT_VAULT = REPO / "vault_baseline"
SKIP_DIRS = {".obsidian", ".git", ".trash"}

# Templates are deliberately unlinked and deliberately share a `{{title}}`
# placeholder heading; daily notes are entered by date, not by link.
UNLINKED_BY_DESIGN = ("_Templates/", "80 - Daily/")

REQUIRED_ON_GENERATED = ("title", "type", "category", "generated", "tags")
REQUIRED_ON_HUMAN = ("type", "tags")

# Pages produced by a generator rather than projected from a canonical file.
DERIVED_WITHOUT_A_SOURCE = ("_meta/taxonomy.md",
                            "10 - Projects/AETHRION/graph_legend.md")

FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.S)
WIKILINK = re.compile(r"!?\[\[([^\]#|]+?)(?:\\?\|[^\]]*?)?(?:#[^\]]*?)?\]\]")


# A fenced block is not prose. Mermaid writes a node as ``ID[["label"]]``, which
# is character-for-character a wikilink, and the corpus draws mermaid diagrams in
# `README.md`, the architecture notes and the plan. Scanning raw text reported
# `README.md`'s "no such edge exists" node as a link to a missing page.
FENCED = re.compile(r"^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$",
                    re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def prose(text: str) -> str:
    """`text` with fenced blocks and inline code removed, lines preserved."""
    without = FENCED.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    return INLINE_CODE.sub("", without)
# Link targets in this vault contain spaces — every top-level folder is named
# like "07 - Skills" — so the target class must not exclude whitespace. Excluding
# it silently matched nothing across the whole Skills tree and reported 42
# well-linked pages as orphans.
MDLINK = re.compile(r"\[[^\]]*\]\(([^)]+?\.(?:md|png|jpg|jpeg|svg|pdf|csv|txt))(?:#[^)]*)?\)")
FIELD = re.compile(r"^([A-Za-z_][\w-]*):", re.M)


def slug(text: str) -> str:
    return text.strip().rstrip("\\").lower().replace(" ", "-")


def iter_files(vault: Path) -> list[Path]:
    return [p for p in sorted(vault.rglob("*"))
            if p.is_file() and not any(part in SKIP_DIRS for part in p.parts)]


def frontmatter_of(text: str) -> tuple[set[str], list[str], str]:
    match = FRONTMATTER.match(text)
    if not match:
        return set(), [], ""
    block = match.group(1)
    fields = set(FIELD.findall(block))
    tags = re.findall(r"^\s+-\s+([\w/\-]+)\s*$",
                      re.search(r"^tags:\n((?:\s+-.*\n?)*)", block, re.M).group(1)
                      if re.search(r"^tags:\n((?:\s+-.*\n?)*)", block, re.M) else "", re.M)
    title = ""
    title_match = re.search(r'^title:\s*"?(.*?)"?\s*$', block, re.M)
    if title_match:
        title = title_match.group(1)
    return fields, tags, title


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", nargs="?", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--strict-orphans", action="store_true",
                        help="treat orphan pages as findings rather than reporting them")
    args = parser.parse_args()
    vault: Path = args.vault
    if not vault.is_dir():
        print(f"no vault at {vault}", file=sys.stderr)
        return 2

    files = iter_files(vault)
    pages = [p for p in files if p.suffix == ".md"]
    by_name: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        by_name[slug(path.stem)].append(path)
        by_name[slug(path.name)].append(path)

    vocabulary = set(vault_frontmatter.taxonomy())
    incoming: Counter[str] = Counter()
    broken_wiki: list[tuple[str, str]] = []
    outside: list[tuple[str, str]] = []
    missing_front: list[tuple[str, list[str]]] = []
    unknown_tags: list[tuple[str, str]] = []
    no_source: list[str] = []
    titles: dict[str, list[str]] = defaultdict(list)

    for path in pages:
        rel = path.relative_to(vault).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        fields, tags, title = frontmatter_of(text)

        # Classified by the value, not by the field's presence: a human page that
        # honestly declares `generated: false` is still a human page.
        generated = re.search(r"^generated:\s*true\s*$", text, re.M) is not None
        required = REQUIRED_ON_GENERATED if generated else REQUIRED_ON_HUMAN
        missing = [f for f in required if f not in fields]
        if missing and not rel.startswith("_Templates/"):
            missing_front.append((rel, missing))
        # A page derived from a generator rather than projected from one
        # canonical file names a provenance and no source.
        if generated and "source" not in fields and rel not in DERIVED_WITHOUT_A_SOURCE:
            no_source.append(rel)
        for tag in tags:
            if tag.startswith("aethrion/") and tag not in vocabulary:
                unknown_tags.append((rel, tag))
        if title and not rel.startswith("_Templates/"):
            titles[title.strip().lower()].append(rel)

        for raw in WIKILINK.findall(prose(text)):
            target = slug(raw.split("/")[-1])
            if target == slug(path.stem):
                continue
            if target in by_name:
                incoming[target] += 1
            else:
                broken_wiki.append((rel, raw.strip()))
        for href in MDLINK.findall(text):
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / href).resolve()
            if resolved.is_file():
                incoming[slug(resolved.stem)] += 1
            else:
                # A link out of the mirrored subset. mirror_vault.py leaves these
                # exactly as written on purpose: a link it cannot map is safer
                # visibly broken than silently repointed at the wrong note.
                outside.append((rel, href))

    taxonomy_drift: list[str] = []
    taxonomy_page = vault / "_meta" / "taxonomy.md"
    if not taxonomy_page.is_file():
        taxonomy_drift.append("_meta/taxonomy.md is missing — run "
                              "scripts/vault_frontmatter.py --write <vault>")
    elif taxonomy_page.read_text(encoding="utf-8") != vault_frontmatter.taxonomy_page():
        taxonomy_drift.append("_meta/taxonomy.md does not match the generator")

    orphans = [p.relative_to(vault).as_posix() for p in pages
               if incoming[slug(p.stem)] == 0
               and not p.relative_to(vault).as_posix().startswith(UNLINKED_BY_DESIGN)]
    duplicate_titles = {t: paths for t, paths in titles.items() if len(paths) > 1}

    findings = 0

    def report(label: str, rows: list, fatal: bool = True, limit: int = 8) -> None:
        nonlocal findings
        if not rows:
            print(f"  ✅ {label}: none")
            return
        mark = "✗" if fatal else "•"
        print(f"  {mark} {label}: {len(rows)}")
        for row in rows[:limit]:
            print(f"      {row if isinstance(row, str) else ' → '.join(map(str, row))}")
        if len(rows) > limit:
            print(f"      … and {len(rows) - limit} more")
        if fatal:
            findings += len(rows)

    print(f"vault: {vault}")
    print(f"{len(pages)} pages · {len(files) - len(pages)} attachments · "
          f"{len(vocabulary)} tags in the controlled vocabulary\n")
    report("broken wikilinks", broken_wiki)
    report("generated pages missing required frontmatter", missing_front)
    report("generated pages that do not name a source", no_source)
    report("tags outside the controlled vocabulary", unknown_tags)
    report("duplicate titles", [f"{t} → {', '.join(p)}" for t, p in duplicate_titles.items()])
    report("controlled vocabulary page drift", taxonomy_drift)
    for script, label_ in (("make_vault_graph.py", "graph colouring"),
                           ("make_vault_theme.py", "vault-wide colouring")):
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts" / script), str(vault), "--check"],
            capture_output=True, text=True)
        report(f"{label_} drift",
               [] if result.returncode == 0 else
               [l.strip().lstrip("✗ ") for l in result.stdout.splitlines() if "✗" in l])
    report("orphan pages (nothing links to them)", orphans, fatal=args.strict_orphans)
    report("links out of the mirrored subset (left as written by design)",
           outside, fatal=False)

    print()
    if findings:
        print(f"{findings} vault finding(s) — the vault is not well-formed")
        return 1
    print("the vault is well-formed: every link resolves, every generated page "
          "names its source, and every tag is in the controlled vocabulary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
