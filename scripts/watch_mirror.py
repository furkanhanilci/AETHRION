#!/usr/bin/env python3
"""Keep the Obsidian vault current while the repository is being edited.

Why this exists
    The mirrors are correct and manual, so the vault is only as fresh as the last
    time someone remembered. During a long editing session that gap is the whole
    session: the repository moves and Obsidian shows the state it had hours ago,
    which is the same defect as a stale generated page — a reader trusts what they
    are looking at.

    This watcher closes it. It notices a change in the canonical sources and
    regenerates the projections, so the vault is a view rather than a snapshot.

What it will not do
    ``mirror_plan.py`` **replaces its target directory**, and `AGENTS.md` §10
    records that it once deleted an entire vault when pointed at a root instead of
    the commissioning subtree. Running that automatically deserves more caution
    than running it by hand, so this watcher:

    * hard-codes the subtree, never accepting a root;
    * refuses to start if a target does not already look like a mirror;
    * runs each mirror's own ``--check`` first and writes **only** when it reports
      drift, so a quiet repository produces no writes at all;
    * never passes ``--force``, so the mirrors' own stray-file refusal still
      applies on every run.

    It also touches nothing outside the generated areas. The human areas of the
    vault are not projections and are not its business.

Detection
    Polling, not inotify: `inotify-tools` is not installed here and a pure-Python
    poll over ~600 files costs a few milliseconds. The signature is
    (path, mtime_ns, size) — enough to notice an edit, cheap enough to run every
    two seconds.

Usage
    python3 scripts/watch_mirror.py                       # foreground, ctrl-C to stop
    python3 scripts/watch_mirror.py --once                # one pass, then exit
    python3 scripts/watch_mirror.py --interval 5          # slower poll
    systemctl --user start aethrion-mirror.service        # as a service
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE_VAULT = Path("/home/otonom/Documents/Obsidian Vault")
BASELINE_VAULT = ROOT / "vault_baseline"

# Canonical sources whose changes the vault projects.
#
# Derived from the mirror's own source map rather than listed here. The list was
# written by hand and then the mirror grew eighteen sources outside `docs/` —
# `AGENTS.md`, `scripts/README.md`, `src/*/README.md` — none of which this
# watcher looked at, so editing the operating manual left the vault showing the
# previous one with nothing reporting a difference. A watcher that does not watch
# what the mirror reads is the silent-staleness failure one level down.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mirror_vault  # noqa: E402  (after sys.path)

WATCHED = [
    ROOT / "planning" / "commissioning",
    ROOT / "docs",
    ROOT / "skills",
    ROOT / "delivery" / "progress.json",
    *sorted({ROOT / src for src in mirror_vault.SOURCES.values()
             if not src.startswith("docs/")}),
]

PROJECT_SUBTREE = Path("10 - Projects") / "AETHRION"
COMMISSIONING_SUBTREE = PROJECT_SUBTREE / "01 - Commissioning"


def signature() -> frozenset[tuple[str, int, int]]:
    """A cheap fingerprint of every watched file."""
    out: set[tuple[str, int, int]] = set()
    for base in WATCHED:
        if base.is_file():
            stat = base.stat()
            out.add((str(base), stat.st_mtime_ns, stat.st_size))
            continue
        for path in base.rglob("*"):
            if path.is_file():
                stat = path.stat()
                out.add((str(path), stat.st_mtime_ns, stat.st_size))
    return frozenset(out)


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=ROOT,
                          capture_output=True, text=True)


def looks_like_a_mirror(vault: Path) -> str | None:
    """Refuse anything that is not already a projection of this repository."""
    if not vault.is_dir():
        return f"{vault} does not exist"
    project = vault / PROJECT_SUBTREE
    commissioning = vault / COMMISSIONING_SUBTREE
    if not project.is_dir():
        return f"{project} is not there — this is not an AETHRION vault"
    if not commissioning.is_dir():
        return f"{commissioning} is not there — refusing to create a plan mirror from scratch"
    if not (commissioning / "commissioning_index.md").is_file():
        return f"{commissioning} holds no commissioning index — it may not be a mirror"
    return None


def sync(vault: Path, *, label: str) -> list[str]:
    """Regenerate the projections in one vault. Returns what was rewritten."""
    written: list[str] = []
    targets = [
        ("plan", "scripts/mirror_plan.py", str(vault / COMMISSIONING_SUBTREE)),
        ("docs and skills", "scripts/mirror_vault.py", str(vault / PROJECT_SUBTREE)),
    ]
    for name, script, target in targets:
        # Check first. A quiet repository must produce no writes at all: the
        # mirrors replace their target, and a needless replace is a needless risk.
        check = run(script, target, "--check")
        if check.returncode == 0:
            continue
        result = run(script, target)
        if result.returncode != 0:
            print(f"  ✗ {label} {name}: {result.stderr.strip().splitlines()[-1] if result.stderr.strip() else 'failed'}",
                  flush=True)
            continue
        written.append(f"{label} {name}")

    # The vocabulary page and the graph colouring are derived from the same
    # taxonomy the pages are tagged with, so they follow the same regeneration.
    run("scripts/vault_frontmatter.py", "--write", str(vault))
    for script, what in (("scripts/make_vault_graph.py", "graph colouring"),
                         ("scripts/make_vault_theme.py", "vault-wide colouring")):
        if run(script, str(vault), "--check").returncode != 0:
            run(script, str(vault))
            written.append(f"{label} {what}")
    return written


def pass_once(verbose: bool = True) -> None:
    for vault, label in ((BASELINE_VAULT, "baseline"), (LIVE_VAULT, "vault")):
        problem = looks_like_a_mirror(vault)
        if problem:
            if verbose:
                print(f"  · skipping {label}: {problem}", flush=True)
            continue
        written = sync(vault, label=label)
        for entry in written:
            print(f"  ✓ regenerated {entry}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--once", action="store_true",
                        help="run a single pass and exit")
    parser.add_argument("--interval", type=float, default=2.0,
                        help="seconds between polls (default 2)")
    parser.add_argument("--settle", type=float, default=1.5,
                        help="seconds of quiet required before regenerating "
                             "(default 1.5) — an editor writing several files "
                             "should produce one regeneration, not several")
    args = parser.parse_args()

    for vault, label in ((BASELINE_VAULT, "baseline"), (LIVE_VAULT, "vault")):
        problem = looks_like_a_mirror(vault)
        print(f"{label}: {'watching ' + str(vault) if not problem else 'SKIPPED — ' + problem}",
              flush=True)

    if args.once:
        pass_once()
        return 0

    print(f"polling {len(WATCHED)} source trees every {args.interval}s; "
          f"regenerating after {args.settle}s of quiet", flush=True)
    previous = signature()
    pending_since: float | None = None

    while True:
        time.sleep(args.interval)
        try:
            current = signature()
        except OSError:
            continue                      # a file vanished mid-walk; try again
        if current != previous:
            previous = current
            pending_since = time.monotonic()
            continue
        if pending_since is not None and time.monotonic() - pending_since >= args.settle:
            pending_since = None
            print("change detected — regenerating", flush=True)
            pass_once(verbose=False)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nstopped", flush=True)
