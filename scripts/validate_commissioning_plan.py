#!/usr/bin/env python3
"""Validate the *semantics* of the commissioning plan, not just its bytes.

Responsibility
    The hash seal proves that sealed files did not change after sealing. It says
    nothing about whether they are consistent with each other. This script
    checks the plan the way a schema validator checks a document: identifiers
    exist, references resolve in both directions, the dependency graph is
    acyclic, waves are feasible, and no work package requires something that can
    only happen after it.

Invariant
    A reference that resolves in one direction must resolve in the other. If a
    work package claims a scenario tests it, that scenario must agree.

Audit findings
    Written after a pre-commissioning review found three defects that the seal
    could not see: acceptance scenario identifiers colliding with the numbers
    the tooling packages already referenced, a go-live requirement that depended
    on Day-2 packages scheduled after go-live, and stale ranges left behind when
    the scenario count changed. All three were *semantic*, and every file
    involved was byte-identical to its sealed state.

Exit codes
    0 — the plan is internally consistent.  1 — at least one defect.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
ACC_DIR = PLAN / "12_ACCEPTANCE_SCENARIOS"

WP_FILE = re.compile(r"^WP-(\d{3})_.+\.md$")
ACC_FILE = re.compile(r"^ACC-(\d{2})_.+\.md$")
FIELD = lambda name: re.compile(rf"^\| {name} \| (.+?) \|\s*$", re.M)
WP_REF = re.compile(r"WP-(\d{3})")
ACC_REF = re.compile(r"ACC-(\d{2})")
DAY2_RANGE = range(122, 131)
PHASES = {"PRE_GO_LIVE", "DAY2_CONTINUOUS"}


def field(text: str, name: str) -> str | None:
    match = FIELD(name).search(text)
    return match.group(1).strip() if match else None


def load() -> tuple[dict, dict]:
    packages, scenarios = {}, {}
    for path in PLAN.rglob("WP-*.md"):
        m = WP_FILE.match(path.name)
        if not m:
            continue
        text = path.read_text(encoding="utf-8")
        pid = f"WP-{m.group(1)}"
        deps = field(text, "Hard dependencies") or ""
        accs = field(text, "Related acceptance scenarios") or ""
        packages[pid] = {
            "path": path,
            "workstream": field(text, "Workstream") or "",
            "deps": sorted({f"WP-{d}" for d in WP_REF.findall(deps)}),
            "accs": sorted({f"ACC-{a}" for a in ACC_REF.findall(accs)}),
            "duplicate_fields": len(FIELD("Related acceptance scenarios").findall(text)),
        }
    for path in sorted(ACC_DIR.glob("ACC-*.md")):
        m = ACC_FILE.match(path.name)
        if not m:
            continue
        text = path.read_text(encoding="utf-8")
        sid = f"ACC-{m.group(1)}"
        phase_raw = field(text, "Acceptance phase") or ""
        scenarios[sid] = {
            "path": path,
            "severity": (field(text, "Severity") or "").strip("*"),
            "packages": sorted({f"WP-{p}" for p in WP_REF.findall(field(text, "Related packages") or "")}),
            "phase": (re.search(r"`(\w+)`", phase_raw).group(1) if "`" in phase_raw else ""),
        }
    return packages, scenarios


def cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    """Return dependency cycles, if any, by iterative depth-first search."""
    colour, found, stack = {}, [], []

    def visit(node: str) -> None:
        colour[node] = 1
        stack.append(node)
        for nxt in graph.get(node, []):
            if colour.get(nxt) == 1:
                found.append(stack[stack.index(nxt):] + [nxt])
            elif colour.get(nxt) is None:
                visit(nxt)
        stack.pop()
        colour[node] = 2

    for node in graph:
        if colour.get(node) is None:
            visit(node)
    return found


def main() -> int:
    packages, scenarios = load()
    errors: list[str] = []
    warnings: list[str] = []

    # 1. identifier hygiene ------------------------------------------------
    for pid, pkg in packages.items():
        if pkg["duplicate_fields"] > 1:
            errors.append(f"{pid}: 'Related acceptance scenarios' appears {pkg['duplicate_fields']} times")

    # 2. references resolve -------------------------------------------------
    for pid, pkg in packages.items():
        for dep in pkg["deps"]:
            if dep not in packages:
                errors.append(f"{pid}: hard dependency {dep} does not exist")
        for acc in pkg["accs"]:
            if acc not in scenarios:
                errors.append(f"{pid}: references {acc}, which does not exist")
    for sid, sc in scenarios.items():
        for pid in sc["packages"]:
            if pid not in packages:
                errors.append(f"{sid}: references {pid}, which does not exist")

    # 3. bidirectional consistency -----------------------------------------
    for pid, pkg in packages.items():
        for acc in pkg["accs"]:
            if acc in scenarios and pid not in scenarios[acc]["packages"]:
                warnings.append(f"{pid} claims {acc} tests it, but {acc} does not list {pid}")

    # 4. dependency graph is acyclic ---------------------------------------
    for cycle in cycles({p: v["deps"] for p, v in packages.items()}):
        errors.append("dependency cycle: " + " → ".join(cycle))

    # 5. acceptance phase is declared and valid ----------------------------
    for sid, sc in scenarios.items():
        if sc["phase"] not in PHASES:
            errors.append(f"{sid}: acceptance phase {sc['phase']!r} is not one of {sorted(PHASES)}")

    # 6. go-live feasibility — the real defect the seal could not see ------
    for sid, sc in scenarios.items():
        if sc["phase"] != "PRE_GO_LIVE":
            continue
        for pid in sc["packages"]:
            number = int(pid.split("-")[1])
            if number in DAY2_RANGE:
                errors.append(
                    f"{sid} is PRE_GO_LIVE but depends on {pid}, a Day-2 package "
                    f"scheduled after cutover — go-live would require post-go-live work")

    # 7. stale ranges -------------------------------------------------------
    highest = max(int(s.split("-")[1]) for s in scenarios)
    stale = re.compile(r"ACC-01\s*[–-]\s*ACC-(\d{2})")
    for path in PLAN.rglob("*.md"):
        for match in stale.finditer(path.read_text(encoding="utf-8")):
            if int(match.group(1)) != highest:
                errors.append(f"{path.relative_to(PLAN)}: stale range {match.group(0)} "
                              f"(highest scenario is ACC-{highest})")

    # 8. index parity -------------------------------------------------------
    index = (ACC_DIR / "acceptance_scenarios_index.md").read_text(encoding="utf-8")
    listed = set(ACC_REF.findall(index))
    for sid in scenarios:
        if sid.split("-")[1] not in listed:
            errors.append(f"{sid} is not listed in the acceptance index")
    claimed = re.search(r"\| Scenarios \| \*\*(\d+)\*\* \|", index)
    if claimed and int(claimed.group(1)) != len(scenarios):
        errors.append(f"index claims {claimed.group(1)} scenarios; {len(scenarios)} exist")

    # 9. catalogue and dependency matrix parity ----------------------------
    catalogue = (PLAN / "00_PROGRAM" / "03_package_catalogue.md").read_text(encoding="utf-8")
    matrix = (PLAN / "00_PROGRAM" / "package_dependency_matrix.csv").read_text(encoding="utf-8")
    for pid in packages:
        if pid not in catalogue:
            errors.append(f"{pid} is missing from the package catalogue")
        if pid not in matrix:
            errors.append(f"{pid} is missing from the dependency matrix")

    # ---- report -----------------------------------------------------------
    print(f"{len(packages)} work packages · {len(scenarios)} acceptance scenarios")
    by_phase = defaultdict(int)
    for sc in scenarios.values():
        by_phase[sc["phase"]] += 1
    print("phases: " + " · ".join(f"{k} {v}" for k, v in sorted(by_phase.items())))

    for warning in warnings:
        print(f"  ! {warning}")
    for error in errors:
        print(f"  ✗ {error}")

    if errors:
        print(f"\n{len(errors)} defect(s), {len(warnings)} warning(s) — plan semantics FAIL")
        return 1
    print(f"\nplan semantics OK ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
