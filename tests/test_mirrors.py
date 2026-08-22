"""The mirrors must not disturb files they did not change.

A reader could not see their own updates in Obsidian, and the cause was not the
content: `mirror_plan.py` removed its target tree and rewrote it, so a running
editor watching that directory lost every inode it held and kept showing a stale
index.

The same replace-wholesale behaviour is the hazard `AGENTS.md` §10 records, where
the mirror pointed at a vault root deleted the vault.

These tests fix the property that prevents both: a mirror writes what changed and
leaves everything else — including its inode — exactly where it was.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script: str, target: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, f"scripts/{script}", str(target), *args],
        cwd=ROOT, capture_output=True, text=True)


def snapshot(target: Path) -> dict[str, tuple[int, int]]:
    return {
        p.relative_to(target).as_posix(): (p.stat().st_ino, p.stat().st_mtime_ns)
        for p in target.rglob("*") if p.is_file()
    }


def test_plan_mirror_is_differential(tmp_path: Path) -> None:
    """A second run with no source change must write nothing at all."""
    target = tmp_path / "01 - Commissioning"
    target.mkdir(parents=True)
    first = run("mirror_plan.py", target)
    assert first.returncode == 0, first.stderr
    before = snapshot(target)
    assert before, "the mirror produced no files"

    second = run("mirror_plan.py", target)
    assert second.returncode == 0, second.stderr
    after = snapshot(target)

    assert set(after) == set(before)
    changed = [rel for rel in before if after[rel] != before[rel]]
    assert changed == [], f"unchanged sources rewrote {len(changed)} files"
    assert "0 written" in second.stdout


def test_plan_mirror_preserves_inodes_of_unchanged_files(tmp_path: Path) -> None:
    """One changed source must not disturb its neighbours.

    This is the property a running editor depends on: it watches inodes, and a
    tree that is deleted and recreated breaks every watch it holds.
    """
    target = tmp_path / "01 - Commissioning"
    target.mkdir(parents=True)
    assert run("mirror_plan.py", target).returncode == 0
    before = snapshot(target)

    source = ROOT / "planning" / "commissioning" / "01_GOVERNANCE" / \
        "WP-001_commissioning_charter.md"
    original = source.read_text(encoding="utf-8")
    try:
        source.write_text(original + "\n<!-- mirror differential probe -->\n",
                          encoding="utf-8")
        result = run("mirror_plan.py", target)
        assert result.returncode == 0, result.stderr
    finally:
        source.write_text(original, encoding="utf-8")

    after = snapshot(target)
    changed = [rel for rel in before if after[rel] != before[rel]]
    assert len(changed) == 1, f"one source changed but {len(changed)} files moved"
    assert "wp_001" in changed[0]
    assert "1 written" in result.stdout


def test_vault_mirror_leaves_unchanged_files_alone(tmp_path: Path) -> None:
    target = tmp_path / "AETHRION"
    target.mkdir(parents=True)
    assert run("mirror_vault.py", target).returncode == 0
    before = snapshot(target)

    result = run("mirror_vault.py", target)
    assert result.returncode == 0, result.stderr
    after = snapshot(target)

    changed = [rel for rel in before if after[rel] != before[rel]]
    assert changed == [], f"unchanged sources rewrote {len(changed)} files"
    assert "0 written" in result.stdout


def test_vault_mirror_refuses_to_overwrite_a_hand_authored_note(tmp_path: Path) -> None:
    """A projection may replace its own pages and nobody else's.

    The vault curates notes beside the projection. When the mirror grew a map of
    the repository's folder READMEs, two of its targets landed on the names of
    curated notes — `reviews_index.md` and `architecture_index.md` — and nothing
    stopped the write. They were recoverable only because `vault_baseline/` is
    tracked, which is luck, not a control.
    """
    target = tmp_path / "AETHRION"
    assert run("mirror_vault.py", target).returncode == 0

    # Take a page the mirror owns and declare it hand-authored, exactly as a
    # curated note does.
    page = target / "05 - Evidence" / "delivery_index.md"
    original = page.read_text(encoding="utf-8")
    page.write_text(
        original.replace("generated: true", "generated: false") + "\nmine\n",
        encoding="utf-8")
    mine = page.read_text(encoding="utf-8")

    result = run("mirror_vault.py", target)
    assert result.returncode != 0, "the mirror overwrote a hand-authored note"
    assert "refusing to overwrite" in result.stderr + result.stdout
    assert page.read_text(encoding="utf-8") == mine, "the note was modified anyway"


def test_the_watcher_watches_every_source_the_mirror_reads() -> None:
    """A watcher blind to a source is silent staleness, not a quiet vault.

    `WATCHED` was a hand-written list of four paths. The mirror then grew
    eighteen sources outside `docs/` — `AGENTS.md`, `scripts/README.md`,
    `src/*/README.md` — so editing the operating manual left the vault showing
    the previous one and nothing reported a difference.
    """
    sys.path.insert(0, str(ROOT / "scripts"))
    import mirror_vault
    import watch_mirror

    watched = [p.resolve() for p in watch_mirror.WATCHED]
    for src in mirror_vault.SOURCES.values():
        path = (ROOT / src).resolve()
        assert any(path == w or w in path.parents for w in watched), (
            f"{src} is mirrored but nothing watches it")
