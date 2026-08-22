#!/usr/bin/env python3
"""Generate the Obsidian reading mirror of the canonical commissioning plan.

The canonical plan lives in ``planning/commissioning/``. The Obsidian tree under
``<vault>/10 - Projects/AETHRION/01 - Commissioning/`` is a
**generated** reading copy: content changes go into the canonical file first and
propagate from here. Editing the mirror directly creates a divergence the plan
seal cannot detect, because the seal does not cover the mirror.

Usage:
    python scripts/mirror_plan.py <target-commissioning-dir> [--check]

``--check`` writes nothing and exits non-zero if the mirror differs from what
would be generated (the drift check intended for CI).
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mirror_vault
import vault_frontmatter

REPO = Path(__file__).resolve().parent.parent
CANON = REPO / "planning" / "commissioning"

# Files copied verbatim so that the mirror can be integrity-checked too.
VERBATIM = {"00_PROGRAM/package_dependency_matrix.csv", "00_PROGRAM/SHA256SUMS.txt"}


def mirror_name(rel: Path) -> str:
    """Map a canonical file name onto its Obsidian mirror name."""
    name = rel.name
    if name == "README.md":
        return "commissioning_index.md" if rel.parent == Path(".") else name
    m = re.match(r"^(WP|ACC)-(\d+)_(.+\.md)$", name)
    if m:
        return f"{m.group(1).lower()}_{m.group(2)}_{m.group(3)}"
    return name


def companion_kind(name: str) -> str:
    """`tests`, `acceptance`, or `""` for a package card."""
    for kind in ("tests", "acceptance"):
        if re.match(rf"^WP-\d{{3}}_.+\.{kind}\.md$", name):
            return kind
    return ""


# Repository document -> its place in the vault, taken from mirror_vault's own
# map so the two cannot disagree. A plan file linking `../../../docs/READY.md`
# resolves in the repository and used to land on nothing in Obsidian; those links
# are the whole of `check_vault.py`'s "out of the mirrored subset" count.
def _docs_in_vault() -> dict[str, str]:
    import mirror_vault
    return {src: rel for rel, src in mirror_vault.DOC_MAP.items()}


def rewrite_doc_links(text: str, depth: int) -> str:
    """Point a plan file's links to `docs/` at the mirrored copies.

    ``depth`` is how far the file sits below the commissioning root, so the
    relative path back out to `10 - Projects/AETHRION/` is computed rather than
    guessed.
    """
    mapping = _docs_in_vault()
    up = "../" * (depth + 1)          # out of the file's directory, then out of
                                      # `01 - Commissioning` itself

    def repl(match: re.Match[str]) -> str:
        prefix, target, frag = match.group(1), match.group(2), match.group(3) or ""
        vault_rel = mapping.get(target)
        if vault_rel is None:
            return match.group(0)     # not mirrored: leave it visibly unresolved
        return f"]({up}{vault_rel}{frag})"

    return re.sub(r"(\]\()(?:\.\./)+docs/([^)#\s]+\.md)(#[^)]*)?\)",
                  lambda m: repl(m), text)


def rewrite_links(text: str) -> str:
    """Rewrite intra-plan links to the mirror naming convention."""
    def repl(match: re.Match[str]) -> str:
        prefix, kind, num, tail = match.groups()
        return f"{prefix}{kind.lower()}_{num}_{tail}"

    # The directory prefix is optional: a link to a sibling package is written
    # ``](WP-001_x.md)`` with no slash in it, and requiring one left every
    # same-directory link in the generated indexes pointing at a name the mirror
    # had already renamed.
    return re.sub(r"(\]\((?:[^)]*?/)?)(WP|ACC)-(\d+)_([^)]+\.md\))", repl, text)


def build() -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    for src in sorted(CANON.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(CANON)
        if rel.as_posix() in VERBATIM:
            out[(rel.parent / mirror_name(rel)).as_posix()] = src.read_bytes()
            continue
        if src.suffix != ".md":
            continue
        text = rewrite_links(src.read_text(encoding="utf-8"))
        text = rewrite_doc_links(text, len(rel.parent.parts) if rel.parent != Path(".") else 0)
        vault_rel = (rel.parent / mirror_name(rel)).as_posix()
        # Obsidian reads YAML frontmatter, not the document standard's header
        # table, so the projection adds it. Without this the vault's own queries
        # cannot see a single mirrored page.
        front = vault_frontmatter.derive(
            vault_rel=f"01 - Commissioning/{vault_rel}",
            source=f"planning/commissioning/{rel.as_posix()}",
            text=text,
            generator="mirror_plan.py",
        )
        out[vault_rel] = (front + text).encode("utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--force", action="store_true",
                        help="replace the target even if it holds files this mirror "
                             "does not generate; this deletes them")
    args = parser.parse_args()

    generated = build()
    target: Path = args.target

    if args.check:
        drift: list[str] = []
        existing = {
            p.relative_to(target).as_posix()
            for p in target.rglob("*")
            if p.is_file()
        }
        for rel, payload in generated.items():
            path = target / rel
            if not path.exists():
                drift.append(f"missing: {rel}")
            elif path.read_bytes() != payload:
                drift.append(f"differs: {rel}")
        for rel in sorted(existing - set(generated)):
            drift.append(f"extra:   {rel}")
        for line in drift:
            print(line)
        print(f"{len(generated)} generated files, {len(drift)} drift entries")
        return 1 if drift else 0

    if target.exists():
        # This script replaces the target wholesale, so a mistyped path is a
        # data-loss event rather than a failed run. Refuse any directory that
        # holds files this mirror did not generate: an existing mirror is a
        # subset of `generated`, anything else is somebody's data.
        strays = sorted(
            p.relative_to(target).as_posix()
            for p in target.rglob("*")
            if p.is_file() and p.relative_to(target).as_posix() not in generated
        )
        if strays and not args.force:
            print(f"refusing to replace {target}", file=sys.stderr)
            print(
                f"  it holds {len(strays)} file(s) this mirror does not generate, "
                "so it is not a plan mirror:",
                file=sys.stderr,
            )
            for rel in strays[:5]:
                print(f"    {rel}", file=sys.stderr)
            if len(strays) > 5:
                print(f"    ... and {len(strays) - 5} more", file=sys.stderr)
            print(
                "  the plan mirror lives at "
                "'<vault>/10 - Projects/AETHRION/01 - Commissioning'; "
                "pass --force only if you mean to delete the files listed above.",
                file=sys.stderr,
            )
            return 2
    # Differential, not replace-wholesale. The previous implementation removed the
    # target tree and rewrote it, which had two costs. The first is the hazard
    # `AGENTS.md` §10 records: pointed at a vault root it deleted the vault. The
    # second is quieter and was found by a reader who could not see their own
    # updates — Obsidian watches this directory, and deleting the tree underneath a
    # running app breaks its watcher, so it keeps showing a stale index of files
    # that no longer exist at those inodes.
    #
    # Writing only what changed keeps every unchanged file, and its inode, exactly
    # where the editor is watching it.
    existing = {
        p.relative_to(target).as_posix(): p
        for p in target.rglob("*") if p.is_file()
    } if target.exists() else {}

    written = removed = 0
    for rel, payload in generated.items():
        path = target / rel
        if path.is_file() and path.read_bytes() == payload:
            continue                      # byte-identical: leave the file alone
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        written += 1

    for rel in sorted(set(existing) - set(generated)):
        existing[rel].unlink()
        removed += 1

    # Remove directories the mirror emptied, and nothing else.
    for directory in sorted((p for p in target.rglob("*") if p.is_dir()),
                            key=lambda p: len(p.parts), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()

    print(f"{len(generated)} files to {target} — {written} written, "
          f"{removed} removed, {len(generated) - written} unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
