#!/usr/bin/env python3
"""Write the derived analysis sections into every work package document.

Responsibility
    A work package document states its own dependencies and stops there. That
    leaves the three questions a reader actually needs unanswered: what must
    already be `ACCEPTED` before this can start (the *closure*, not the direct
    list), what this package releases when it is accepted (the reverse edge,
    which appears nowhere in the plan), and where it sits on the critical path.
    All three are computable from `package_dependency_matrix.csv`, so none of
    them should be written by hand.

Invariant
    Everything between a ``<!-- generated:… -->`` marker and its ``<!-- /generated -->``
    is derived from the repository. Editing inside a block is overwritten on the
    next run and reported by ``--check``. Everything outside a block is
    hand-authored and is never touched by this script.

    This makes a work package file **partly generated**, which is a regime this
    plan did not previously have. The rule is therefore stated in the file
    itself, at the top of each block, rather than only in a guide someone may
    not have read.

Why the reverse edge matters
    "WP-026 blocks 22 packages" is the single most decision-relevant fact about
    WP-026, and before this script it was in no document — only latent in a CSV
    column that names the opposite direction. A programme that cannot see its
    own bottlenecks sequences itself by workstream number instead of by leverage.

Exit codes
    0 — every block matches what the repository implies.  1 — drift, or a
    package document that cannot be parsed.

Usage
    python3 scripts/expand_packages.py            # rewrite the blocks
    python3 scripts/expand_packages.py --check    # fail on drift
"""
from __future__ import annotations

import argparse
import csv
import functools
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
MATRIX = PLAN / "00_PROGRAM" / "package_dependency_matrix.csv"
SCENARIOS = PLAN / "12_ACCEPTANCE_SCENARIOS"

OPEN = "<!-- generated:{name} — produced by scripts/expand_packages.py; do not edit inside this block -->"
CLOSE = "<!-- /generated:{name} -->"

# Wave membership, from 00_PROGRAM/02_wave_and_dependency_map.md. Ranges are
# inclusive. WP-000 and the tooling wave are named explicitly because neither
# follows the numeric sequence.
WAVES = [
    ("WB — Bootstrap", {0}),
    ("W0 — Programme lock", set(range(1, 11))),
    ("W1 — Contract spine", set(range(11, 21))),
    ("W2 — Platform backbone", set(range(21, 32)) | {51} | set(range(55, 60))),
    ("W3 — Control and runtime", set(range(32, 51)) | {52, 53, 54, 60}),
    ("W4 — Knowledge and evidence", set(range(61, 91))),
    ("W5 — Human and visibility", set(range(91, 102))),
    ("W6 — Vertical integration", set(range(102, 116))),
    ("W7 — Commissioning", set(range(116, 120))),
    ("W8 — Cutover", {120, 121}),
    ("W9 — Day-2", set(range(122, 131))),
    ("W-T — Tooling", set(range(131, 141))),
]

# The critical path as the wave map draws it. Membership is a claim the plan
# makes about itself, so it is quoted rather than recomputed: a package can sit
# at the deepest level and still not be on the path the programme manages by.
DOCUMENTED_CRITICAL_PATH = {
    "WP-001", "WP-005", "WP-006", "WP-007", "WP-011", "WP-012", "WP-020",
    "WP-021", "WP-025", "WP-026", "WP-028", "WP-031", "WP-051", "WP-056",
    "WP-058", "WP-032", "WP-035", "WP-047", "WP-049", "WP-062", "WP-077",
    "WP-102", "WP-103", "WP-104", "WP-105", "WP-106", "WP-115",
    "WP-116", "WP-117", "WP-118", "WP-119", "WP-120",
}


# ---- loading ---------------------------------------------------------------
def load_packages() -> dict[str, dict]:
    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8")))
    packages = {}
    for row in rows:
        pid = row["package_id"].strip()
        packages[pid] = {
            "id": pid,
            "title": row["title"].strip(),
            "workstream": row["workstream"].strip(),
            "effort": row["effort"].strip(),
            "owner": row["owner"].strip(),
            "verifier": row["verifier"].strip(),
            "deps": [d.strip() for d in row["hard_dependencies"].split(";")
                     if d.strip() and d.strip() != "—"],
            "gates": [g.strip() for g in re.split(r"[;,]", row["gates"]) if g.strip()],
            # The matrix uses ";" in most rows and "," in others; both are separators.
            "controls": [c.strip() for c in re.split(r"[;,]", row["controls"]) if c.strip()],
            "scenarios": [s.strip() for s in re.split(r"[;,]", row["scenarios"])
                          if s.strip() and s.strip() != "—"],
        }
    return packages


def find_documents() -> dict[str, Path]:
    return {p.name[:6]: p for p in PLAN.rglob("WP-*.md")
            if re.match(r"^WP-\d{3}_", p.name)
            and not p.name.endswith((".tests.md", ".acceptance.md"))}


def load_deliverables(documents: dict[str, Path]) -> dict[str, list[str]]:
    """What each package hands to the packages that depend on it."""
    out: dict[str, list[str]] = {}
    for pid, path in documents.items():
        text = path.read_text(encoding="utf-8")
        block = re.search(r"## Mandatory deliverables\n(.*?)\n## ", text, re.S)
        items = []
        if block:
            for line in block.group(1).splitlines():
                match = re.match(r"-\s+`(.+?)`\s*$", line.strip())
                if match:
                    items.append(match.group(1))
        out[pid] = items
    return out


def load_scenarios() -> dict[str, dict]:
    out = {}
    for path in sorted(SCENARIOS.glob("ACC-*.md")):
        match = re.match(r"^ACC-\d{2,3}", path.name)
        if not match:
            continue
        text = path.read_text(encoding="utf-8")
        def field(pattern, default=""):
            found = re.search(pattern, text, re.M)
            return found.group(1).strip() if found else default
        out[match.group(0)] = {
            "id": match.group(0),
            "title": field(r"^# ACC-\d{2,3} — (.+)$", "").strip(),
            "severity": field(r"\| Severity \| \*\*(.+?)\*\* \|"),
            "category": field(r"\| Category \| (.+?) \|"),
            "phase": field(r"\| Acceptance phase \| `(.+?)`"),
            "then": field(r"\*\*Then:\*\* (.+?)\n"),
            "path": path,
        }
    return out


# ---- graph -----------------------------------------------------------------
def build_graph(packages: dict[str, dict]):
    forward = {pid: [d for d in p["deps"] if d in packages] for pid, p in packages.items()}
    reverse: dict[str, list[str]] = defaultdict(list)
    for pid, deps in forward.items():
        for dep in deps:
            reverse[dep].append(pid)

    @functools.lru_cache(maxsize=None)
    def depth(pid: str) -> int:
        return 1 + max((depth(d) for d in forward.get(pid, [])), default=0)

    @functools.lru_cache(maxsize=None)
    def closure(pid: str) -> frozenset[str]:
        out: set[str] = set()
        for dep in forward.get(pid, []):
            out.add(dep)
            out |= closure(dep)
        return frozenset(out)

    @functools.lru_cache(maxsize=None)
    def blast(pid: str) -> frozenset[str]:
        out: set[str] = set()
        for child in reverse.get(pid, []):
            out.add(child)
            out |= blast(child)
        return frozenset(out)

    return forward, dict(reverse), depth, closure, blast


def wave_of(pid: str) -> str:
    number = int(pid.split("-")[1])
    for name, members in WAVES:
        if number in members:
            return name
    return "unassigned"


# ---- rendering -------------------------------------------------------------
def render_dependencies(pid, packages, forward, reverse, depth, closure, blast,
                        deliverables, documents, scenarios, max_depth) -> list[str]:
    package = packages[pid]
    direct = forward[pid]
    prereqs = sorted(closure(pid))
    dependants = sorted(reverse.get(pid, []))
    radius = sorted(blast(pid))
    total = len(packages)

    lines: list[str] = []
    add = lines.append

    add("### Direct hard dependencies")
    add("")
    if not direct:
        add("**None.** This package depends on nothing and can start at `t0`. "
            "Only two packages in the programme have this property.")
    else:
        add(f"{len(direct)}, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — "
            f"before this package is `READY`.")
        add("")
        add("| Package | Supplies to this package |")
        add("|---|---|")
        for dep in direct:
            supplies = deliverables.get(dep) or []
            named = " · ".join(f"`{s}`" for s in supplies[:4]) if supplies else "—"
            link = documents[dep].relative_to(documents[pid].parent.parent)
            add(f"| [{dep} — {packages[dep]['title']}](../{link.as_posix()}) | {named} |")
    add("")

    add("### Full prerequisite closure")
    add("")
    if not prereqs:
        add("**Empty.** Nothing has to happen before this package.")
    else:
        percent = round(100 * len(prereqs) / total)
        add(f"**{len(prereqs)} of {total} packages ({percent}%)** must reach `ACCEPTED` "
            f"before this one can begin — the direct list above plus everything "
            f"they in turn require. This is the number that determines when the "
            f"package can actually start; the direct list is only its last layer.")
        add("")
        by_level: dict[int, list[str]] = defaultdict(list)
        for prereq in prereqs:
            by_level[depth(prereq)].append(prereq)
        add("| Level | Packages |")
        add("|---:|---|")
        for level in sorted(by_level):
            add(f"| {level} | {' · '.join('`' + p + '`' for p in sorted(by_level[level]))} |")
    add("")

    add("### What acceptance of this package releases")
    add("")
    if not dependants:
        add("**Nothing.** No package names this one as a hard dependency, so accepting "
            "it unblocks no other work. That is normal for a terminal package and is "
            "worth knowing before it is prioritised over one that unblocks many.")
    else:
        percent = round(100 * len(radius) / total)
        add(f"- **Directly unblocked:** {len(dependants)} — "
            f"{' · '.join('`' + d + '`' for d in dependants)}")
        add(f"- **Transitively reachable:** **{len(radius)} of {total} packages ({percent}%)** "
            f"cannot be accepted until this one is.")
        add("")
        add("The transitive figure is the leverage number. It does not appear anywhere "
            "else in the plan, and it is the one that should drive sequencing when two "
            "packages are otherwise equally ready.")
    add("")

    add("### Position in the programme")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Wave | {wave_of(pid)} |")
    add(f"| Dependency depth | level **{depth(pid)}** of {max_depth} |")
    add(f"| On the documented critical path | "
        f"{'**yes** — `02_wave_and_dependency_map.md` names it' if pid in DOCUMENTED_CRITICAL_PATH else 'no'} |")
    add(f"| Effort class | **{package['effort']}** |")
    add(f"| Accountable owner | {package['owner']} |")
    add(f"| Independent verifier | {package['verifier']} |")
    add(f"| Gates touched | {' · '.join('`' + g + '`' for g in package['gates']) or '—'} |")
    add(f"| Controls | {' · '.join('`' + c + '`' for c in package['controls']) or '—'} |")
    add("")

    add("### Acceptance scenarios that exercise this package")
    add("")
    bound = [scenarios[s] for s in package["scenarios"] if s in scenarios]
    if not bound:
        add("**None.** No acceptance scenario names this package.")
        add("")
        add("> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: "
            "*a row with a primary package but no acceptance column is a capability "
            "nobody will ever be asked to demonstrate.* This package can reach "
            "`ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through "
            "a scenario, because there is none to pass.")
    else:
        add("`COMMISSIONED` requires every scenario below to pass **on the same release "
            "candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.")
        add("")
        add("| Scenario | Severity | What it must show |")
        add("|---|---|---|")
        for scenario in bound:
            then = scenario["then"].replace("|", "\\|")
            link = f"../12_ACCEPTANCE_SCENARIOS/{scenario['path'].name}"
            add(f"| [{scenario['id']} — {scenario['title']}]({link}) | {scenario['severity']} | {then} |")
    return lines


def render_requirements(pid, packages, forward, deliverables, documents) -> list[str]:
    package = packages[pid]
    lines: list[str] = []
    add = lines.append

    add("### Inputs that must exist before the first task starts")
    add("")
    inputs = []
    for dep in forward[pid]:
        for item in deliverables.get(dep, []):
            inputs.append((item, dep))
    if inputs:
        add("Each row is a deliverable of a dependency. Its **absence is a stop "
            "condition**, not a risk to manage: work started against a missing input "
            "is work that will be redone against the real one.")
        add("")
        add("| Required input | Comes from | Accepted? |")
        add("|---|---|---|")
        for item, dep in inputs:
            add(f"| `{item}` | `{dep}` | `python3 scripts/progress.py show {dep}` |")
    else:
        add("**No upstream inputs.** Everything this package needs, it produces.")
    add("")

    add("### Classification that must be recorded before work begins")
    add("")
    add("`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be "
        "classified at refinement. They are not documentation: together they select "
        "the `ExecutionProfile`, and an unclassified package cannot be given one.")
    add("")
    add("| Field | Must state | Recorded at refinement |")
    add("|---|---|---|")
    add("| `DataClass` | D0–D4 for every input and output this package touches | ☐ |")
    add("| `CodeTrust` | provenance of code this package executes | ☐ |")
    add("| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |")
    add("| Network / credential scope | egress destinations and the identity used | ☐ |")
    add("")

    add("### Capacity that must be reserved")
    add("")
    effort = {"S": "small — one owner, one review cycle",
              "M": "medium — a dedicated integration window",
              "L": "large — split into sub-packages if the estimate exceeds the wave"}
    add(f"- **Effort class `{package['effort']}`** — {effort.get(package['effort'], 'unclassified')}.")
    add("- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, "
        "is **mandatory** before this package is `READY`. It is not recorded here because "
        "it depends on real capacity at the time of refinement.")
    add(f"- **{package['owner']}** carries the acceptance decision; "
        f"**{package['verifier']}** must verify independently of whoever implements.")
    add("- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance "
        "capacity stays reserved for correction and re-verification.")
    add("")

    add("### Evidence that must be producible before starting")
    add("")
    add("A package whose evidence cannot be produced is not `READY`, however complete "
        "its design is. Confirm each is reachable:")
    add("")
    add("- The target revision can be pinned, and every test result bound to it.")
    add("- An environment manifest can be captured for the environment the tests run in.")
    add("- The rollback or compensation path named in this document can actually be exercised.")
    add("- A signed `EvidenceManifest` can be issued — today via the interim profile "
        "`airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident "
        "and not externally witnessed**.")
    add("- The verifier can reach the evidence **without** seeing the producer's working trace.")
    return lines


# ---- block surgery ---------------------------------------------------------
def splice(text: str, name: str, body: list[str]) -> str:
    """Replace the named block, or append the section if it is not there yet."""
    open_marker, close_marker = OPEN.format(name=name), CLOSE.format(name=name)
    block = "\n".join([open_marker, "", *body, "", close_marker])
    pattern = re.compile(
        re.escape(open_marker) + r".*?" + re.escape(close_marker), re.S)
    if pattern.search(text):
        return pattern.sub(lambda _: block, text)
    raise KeyError(name)


def ensure_sections(text: str) -> str:
    """Insert the two new headings, once, at their anchor points."""
    if "generated:dependency-analysis" not in text:
        anchor = "## Preconditions — Definition of Ready"
        section = (
            "## Dependency and prerequisite analysis\n\n"
            + OPEN.format(name="dependency-analysis") + "\n\n"
            + CLOSE.format(name="dependency-analysis") + "\n\n"
        )
        text = text.replace(anchor, section + anchor, 1)
    if "generated:execution-requirements" not in text:
        anchor = "## Implementation tasks"
        section = (
            "## Execution requirements\n\n"
            + OPEN.format(name="execution-requirements") + "\n\n"
            + CLOSE.format(name="execution-requirements") + "\n\n"
        )
        text = text.replace(anchor, section + anchor, 1)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail if any generated block differs from what the plan implies")
    args = parser.parse_args()

    packages = load_packages()
    documents = find_documents()
    missing = sorted(set(packages) - set(documents))
    if missing:
        print(f"packages with no document: {missing}")
        return 1

    deliverables = load_deliverables(documents)
    scenarios = load_scenarios()
    forward, reverse, depth, closure, blast = build_graph(packages)
    max_depth = max(depth(pid) for pid in packages)

    drift, written = [], 0
    for pid in sorted(packages):
        path = documents[pid]
        original = path.read_text(encoding="utf-8")
        text = ensure_sections(original)
        text = splice(text, "dependency-analysis", render_dependencies(
            pid, packages, forward, reverse, depth, closure, blast,
            deliverables, documents, scenarios, max_depth))
        text = splice(text, "execution-requirements", render_requirements(
            pid, packages, forward, deliverables, documents))
        if text != original:
            if args.check:
                drift.append(pid)
            else:
                path.write_text(text, encoding="utf-8")
                written += 1

    if args.check:
        for pid in drift:
            print(f"  ✗ {pid}: generated block does not match the plan")
        print(f"{len(packages)} package documents checked, {len(drift)} drift entries")
        return 1 if drift else 0

    print(f"{len(packages)} package documents, {written} rewritten "
          f"({max_depth} dependency levels, {len(scenarios)} scenarios linked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
