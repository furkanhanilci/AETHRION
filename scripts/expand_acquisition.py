#!/usr/bin/env python3
"""Write the acquisition and assimilation contract into every work package.

Responsibility
    An implementer opens one package document and starts work. Everything they
    need in order to start correctly has to be in that document, and one thing
    persistently was not: **which parts of this package are already solved
    somewhere else, and on what terms.**

    That was not a research gap. `AETHRION_COMPONENT_REUSE.md` had decided which
    running implementation each control stands on, and `provenance/upstreams.json`
    had decided which mechanisms are copied and which are reimplemented — with a
    licence position, an authority boundary and a `not_taken` list for each. The
    gap was **binding**: the decision lived in the architecture corpus and the
    work lived in a package, and nothing joined them.

    So WP-144 specified a candidate state machine without mentioning that AIDE is
    a registered `DIRECT_ADAPT` source for exactly that mechanism; WP-153
    specified a budget ledger without mentioning BATS; and WP-041 named LiteLLM
    in its title while no register knew the component existed. An implementer
    working only from the package would have rebuilt what was already decided,
    or copied what was not yet permitted to move.

Why the unresolved column is the point
    Every entry in both registers is `PROPOSED`. Printing "AIDE · DIRECT_ADAPT"
    and stopping would read as permission to go and copy a file, which ADR-004
    refuses until a pin, a file list and a characterisation suite exist. The
    block therefore states the obligation that is still open, in the words of the
    rule that requires it, and the package is not `READY` while any remains.

Invariant
    Everything between the marker and its close is derived from
    `provenance/upstreams.json` and `provenance/components.json`. Editing inside
    the block is overwritten on the next run and reported by ``--check``.
    Everything outside it is hand-authored and never touched.

Exit codes
    0 — every block matches what the registers imply.  1 — drift.

Usage
    python3 scripts/expand_acquisition.py            # rewrite the blocks
    python3 scripts/expand_acquisition.py --check    # fail on drift
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import acquisition_model as model                                 # noqa: E402

NAME = "implementation-sources"
OPEN = (f"<!-- generated:{NAME} — produced by scripts/expand_acquisition.py; "
        f"do not edit inside this block -->")
CLOSE = f"<!-- /generated:{NAME} -->"
HEADING = "## Implementation acquisition and assimilation"
ANCHOR = "## Implementation tasks"

# The residue. Emitted for every package, including packages with no registered
# source at all, because silence cannot distinguish "nothing was taken" from
# "nobody recorded what was taken" — and an implementer has to be able to tell.
NATIVE_ROW = (
    "| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the "
    "authority boundaries and the integration this package specifies | "
    "All of it | — |"
)


cell = model.cell

def render(package: str, rows: list[dict]) -> list[str]:
    out: list[str] = []
    add = out.append

    add("**What is already solved elsewhere, and on what terms.** Before the "
        "first task starts, an implementer has to know which parts of this "
        "package are called at runtime, which are copied and refactored, which "
        "are reimplemented from a specification, and which have no upstream at "
        "all. Those decisions are recorded in "
        "[`provenance/upstreams.json`](../../../provenance/upstreams.json) — "
        "mechanisms assimilated into this repository's own code — and in "
        "[`provenance/components.json`](../../../provenance/components.json) — "
        "components adopted at runtime. This block is derived from both, so a "
        "decision and the place it is used cannot drift apart.")
    add("")

    if not rows:
        add("### No registered source names this package")
        add("")
        add(f"Neither register binds an upstream mechanism or a runtime component "
            f"to `{package}`, so every deliverable below is **`BUILD_NATIVE`**.")
        add("")
        add("That is a statement about the registers, not a finding that no "
            "upstream exists. If refinement identifies one, it is recorded in the "
            "register **first** and appears here on the next generation — a "
            "component named in this document without a register entry is a "
            "defect that `scripts/check_wp_implementation_sources.py` reports.")
        add("")
        add("| Source | Mode | What is taken | AETHRION owns | Unresolved |")
        add("|---|---|---|---|---|")
        add(NATIVE_ROW)
        add("")
        add("**Acquisition readiness — nothing to resolve.** No acquisition "
            "obligation stands between this package and `READY`.")
        return out

    add("### Acquisition map")
    add("")
    add("| Source | Mode | What is taken | AETHRION owns | Unresolved |")
    add("|---|---|---|---|---|")
    for row in rows:
        count = len(row["unresolved"])
        mark = f"**{count}**" if count else "none"
        add(f"| `{row['id']}` — {cell(row['name'], 90)} | `{row['mode']}` | "
            f"{cell(row['taken'])} | {cell(row['owned'])} | {mark} |")
    add(NATIVE_ROW)
    add("")

    add("### What each source may never decide")
    add("")
    add("An adopted mechanism supplies a signal, never a verdict. The recurring "
        "failure of adoption is not a component behaving badly but a component "
        "quietly acquiring authority, which is why every register entry states "
        "this before it is taken.")
    add("")
    add("| Source | May never decide | Deliberately not taken |")
    add("|---|---|---|")
    for row in rows:
        add(f"| `{row['id']}` | {cell(row['boundary'], 400)} | "
            f"{cell(row['not_taken'], 300)} |")
    add("")

    # A note exists on an entry when the plain row would mislead. The case it
    # was written for: PaperQA2 is adopted at runtime as an ADAPTER *and* three
    # of its mechanisms are reimplemented natively. Both are true, and an
    # implementer who sees one row asks the wrong question — "am I using this or
    # rewriting it?" — so where a note exists it is printed.
    noted = [r for r in rows if (r.get("notes") or "").strip()]
    if noted:
        add("### Where a plain row would mislead")
        add("")
        for row in noted:
            add(f"- **`{row['id']}`** — {cell(row['notes'], 600)}")
        add("")

    open_rows = [r for r in rows if r["unresolved"]]
    if open_rows:
        add("### Unresolved before implementation")
        add("")
        add("Each item below is an obligation its mode creates, quoted from the "
            "rule that creates it. None can be met from a session with no "
            "network access, and none may be assumed satisfied.")
        add("")
        for row in open_rows:
            add(f"**`{row['id']}` — {cell(row['name'], 110)}** · `{row['mode']}` "
                f"· status `{row['status']}`")
            add("")
            for item in row["unresolved"]:
                add(f"- {item}")
            add("")
    else:
        add("### Unresolved before implementation")
        add("")
        add("**None.** Every obligation the modes above create has been met.")
        add("")

    total = sum(len(r["unresolved"]) for r in rows)
    if total:
        add(f"**Acquisition readiness — {total} obligation"
            f"{'s' if total != 1 else ''} open across "
            f"{len(open_rows)} of {len(rows)} sources.** "
            f"`00_PROGRAM/05_definition_of_ready_and_done.md` requires the "
            f"acquisition surface of a package to be classified and its "
            f"obligations resolved before the package is `READY`; "
            f"`scripts/ready_queue.py` holds it back until they are.")
    else:
        add(f"**Acquisition readiness — resolved.** All {len(rows)} registered "
            f"sources have met the obligations their modes create.")
    return out


def splice(text: str, body: list[str]) -> str:
    block = "\n".join([OPEN, "", *body, "", CLOSE])
    pattern = re.compile(re.escape(OPEN) + r".*?" + re.escape(CLOSE), re.S)
    if not pattern.search(text):
        raise KeyError(NAME)
    return pattern.sub(lambda _: block, text)


def ensure_section(text: str) -> str:
    """Insert the heading once, immediately before the implementation tasks.

    Position is deliberate: the reader has just been told what must exist before
    the first task starts, and the next thing they read is the task list. The
    question *do I build this or take it* belongs between the two.
    """
    if f"generated:{NAME}" in text:
        return text
    section = f"{HEADING}\n\n{OPEN}\n\n{CLOSE}\n\n"
    if ANCHOR not in text:
        raise KeyError(f"no {ANCHOR!r} anchor")
    return text.replace(ANCHOR, section + ANCHOR, 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if any block differs from what the registers imply")
    args = parser.parse_args()

    documents = model.packages()
    drift, written, bound = [], 0, 0
    for pid, path in sorted(documents.items()):
        rows = model.rows_for(pid)
        bound += 1 if rows else 0
        original = path.read_text(encoding="utf-8")
        text = splice(ensure_section(original), render(pid, rows))
        if text != original:
            if args.check:
                drift.append(pid)
            else:
                path.write_text(text, encoding="utf-8")
                written += 1

    if args.check:
        for pid in drift:
            print(f"  ✗ {pid}: acquisition block does not match the registers")
        print(f"{len(documents)} package documents checked, {len(drift)} drift entries")
        return 1 if drift else 0

    unresolved = model.unresolved_packages()
    print(f"{len(documents)} package documents, {written} rewritten — "
          f"{bound} bound to a registered source, "
          f"{len(unresolved)} with an unresolved acquisition obligation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
