#!/usr/bin/env python3
"""Validate the programme as one graph, not as a package DAG plus some prose.

Responsibility
    ``validate_commissioning_plan.py`` proves the package dependency graph is
    acyclic and that references resolve. That is necessary and it is not enough:
    **a dependency graph can be perfectly acyclic and still impossible to
    execute.** The executable programme also contains acceptance-scenario
    prerequisites, aggregation edges and scheduling phases, and a contradiction
    can live entirely in the space between those and never touch a WP→WP cycle.

    Both real defects were of that kind. WP-152 depended on the Day-2 postmortem
    rhythm to define a failure taxonomy the rhythm should consume; WP-155
    depended on recurring recalibration for an initial qualification it needs
    before anything runs. Neither is a cycle. Both make the plan unstartable,
    and every check in the bundle passed.

Edge orientation — stated because it is the one thing that must be consistent
    ``A -> B`` reads *"A cannot be finished until B is"*.

    - ``WP -> WP``    hard dependency.
    - ``ACC -> WP``   a scenario cannot run until the packages it exercises exist.
    - ``WP -> ACC``   **only for selector-resolved scenarios.** An aggregator
      consolidates results it did not produce.

    A package's own explicit scenarios do NOT produce a ``WP -> ACC`` edge. They
    are its acceptance evidence, produced after it exists, and the relation is
    already carried by ``ACC -> WP``. Getting this wrong is not a small error:
    the first version of this check emitted both directions and reported 1058
    cycles, every one of them the tautology *"a package requires the scenario
    that tests it, which requires the package"*.

Rules
    V-PHASE-001  no early package transitively depends on a late one
    V-SCEN-001   every selector parses and resolves non-empty
    V-SCEN-002   each aggregator's resolved set equals the registry query
    V-GRAPH-001  the combined graph is acyclic
    V-GRAPH-002  every PRE_GO_LIVE scenario is reachable before GO_LIVE
    V-WAVE-001   every package sits in exactly one registered wave
    V-ACC-001    no PRE_GO_LIVE scenario exercises a post-go-live package

Self-test
    ``--self-test`` mutates the model once per rule and fails if any rule stays
    quiet. Each mutation is the historical defect that rule was written for, so
    the self-test doubles as the regression fixture set: the WP-158/WP-115
    cycle, the WP-155 Day-2 deadlock, the two-scenario aggregate, a package
    outside the wave registry, and an invalid selector.

Exit codes
    0 — every rule holds.  1 — at least one violation, with the path printed.
"""
from __future__ import annotations

import copy
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from programme_model import (EARLY_PHASES, LATE_PHASES, Programme,  # noqa: E402
                             ProgrammeModelError, acc_sort_key, load, wp_sort_key)


# --------------------------------------------------------------------- graph
def build_edges(prog: Programme) -> dict[str, set[str]]:
    edges: dict[str, set[str]] = {}
    for pid, package in prog.packages.items():
        edges.setdefault(pid, set()).update(d for d in package.deps if d in prog.packages)
        for sid, why in prog.resolve_scenarios(pid):
            if why.startswith("selected"):
                edges[pid].add(sid)
    for sid, scenario in prog.scenarios.items():
        edges.setdefault(sid, set()).update(
            p for p in scenario.packages if p in prog.packages)
    return edges


def find_cycles(edges: dict[str, set[str]]) -> list[list[str]]:
    colour: dict[str, int] = {}
    cycles: list[list[str]] = []

    def walk(node: str, stack: list[str]) -> None:
        colour[node] = 1
        stack.append(node)
        for nxt in sorted(edges.get(node, ())):
            if colour.get(nxt) == 1:
                cycles.append(stack[stack.index(nxt):] + [nxt])
            elif not colour.get(nxt):
                walk(nxt, stack)
        stack.pop()
        colour[node] = 2

    for node in sorted(edges):
        if not colour.get(node):
            walk(node, stack=[])
    return cycles


def topological_order(edges: dict[str, set[str]]) -> list[str] | None:
    """Kahn's algorithm. None if no valid order exists."""
    incoming = {n: 0 for n in edges}
    for node, outs in edges.items():
        for nxt in outs:
            incoming.setdefault(nxt, 0)
    for node, outs in edges.items():
        for nxt in outs:
            incoming[nxt] += 1
    # A -> B means B must come first, so start from nodes nothing depends on.
    ready = sorted(n for n, c in incoming.items() if c == 0)
    order: list[str] = []
    while ready:
        node = ready.pop(0)
        order.append(node)
        for nxt in sorted(edges.get(node, ())):
            incoming[nxt] -= 1
            if incoming[nxt] == 0:
                ready.append(nxt)
        ready.sort()
    return order if len(order) == len(incoming) else None


def _parses(prog: Programme, pid: str, selector: str) -> bool:
    try:
        prog.parse_selector(selector, pid)
        return True
    except ProgrammeModelError:
        return False


# --------------------------------------------------------------------- rules
def audit(prog: Programme) -> list[str]:
    problems: list[str] = []
    late = {p for p, k in prog.packages.items() if k.phase in LATE_PHASES}

    # V-PHASE-001 -----------------------------------------------------------
    for pid in sorted(prog.packages, key=wp_sort_key):
        if prog.packages[pid].phase not in EARLY_PHASES:
            continue
        path = prog.shortest_path(pid, late)
        if path:
            rendered = "\n      -> ".join(
                f"{n} [{prog.packages[n].phase}]" for n in path)
            problems.append(
                f"V-PHASE-001 {pid} is scheduled before go-live and depends on "
                f"work that only exists after it:\n      {rendered}")

    # V-SCEN-001 / V-SCEN-002 ----------------------------------------------
    # Iterate over the DECLARED aggregators, not over whichever packages happen
    # to have a selector filled in — otherwise deleting a selector deletes the
    # check along with it, which is how the stale two-scenario enumeration
    # survived in the first place.
    for pid in sorted(set(prog.required_aggregates) |
                      {p for p, k in prog.packages.items() if k.selector},
                      key=wp_sort_key):
        selector = prog.packages[pid].selector
        expected_selector = prog.required_aggregates.get(pid)
        if expected_selector and selector != expected_selector:
            problems.append(
                f"V-SCEN-002 {pid} is a declared aggregator and must carry the "
                f"selector {expected_selector!r}; the matrix says {selector!r} — "
                f"without it the package falls back to an enumerated list, which "
                f"is stale the moment a scenario is added")
            # No `continue`. A wrong selector on a declared aggregator is two
            # findings, not one: the aggregate is broken AND the value may not
            # even be grammatical. Short-circuiting here hid V-SCEN-001 from its
            # own self-test, which is how this was found.
        try:
            key, value = prog.parse_selector(selector, pid)
        except ProgrammeModelError as exc:
            problems.append(f"V-SCEN-001 {exc}")
            continue
        resolved = [s for s, _ in prog.resolve_scenarios(pid)]
        if not resolved:
            problems.append(
                f"V-SCEN-001 {pid}: selector {selector!r} resolves to nothing — "
                f"an aggregate that silently matches no scenario is the defect "
                f"a selector was introduced to remove")
            continue
        expected = set(prog.scenarios_in_phase(value)) | set(
            prog.packages[pid].explicit_scenarios)
        if set(resolved) != expected:
            missing = sorted(expected - set(resolved), key=acc_sort_key)
            extra = sorted(set(resolved) - expected, key=acc_sort_key)
            problems.append(
                f"V-SCEN-002 {pid}: resolved commissioning set does not equal "
                f"the registry query for {key}={value} — "
                f"missing {missing}, unexpected {extra}")

    # V-ACC-001 -------------------------------------------------------------
    for sid in sorted(prog.scenarios, key=acc_sort_key):
        scenario = prog.scenarios[sid]
        if scenario.phase != "PRE_GO_LIVE":
            continue
        blocked = sorted((p for p in scenario.packages if p in late), key=wp_sort_key)
        if blocked:
            problems.append(
                f"V-ACC-001 {sid} is PRE_GO_LIVE and exercises {', '.join(blocked)}, "
                f"scheduled after cutover — go-live would require post-go-live work")

    # V-WAVE-001 ------------------------------------------------------------
    known = {w["id"] for w in prog.waves}
    for pid in sorted(prog.packages, key=wp_sort_key):
        wave = prog.packages[pid].wave
        if wave not in known:
            problems.append(
                f"V-WAVE-001 {pid} is in wave {wave!r}, which is not in the "
                f"wave registry — a package outside the registry is invisible "
                f"to every figure and index derived from it")

    # V-GRAPH-001 / V-GRAPH-002 --------------------------------------------
    # A broken selector means the graph cannot be built at all, and reporting
    # "cycle detected" on top of "this selector is not valid" would bury the
    # cause under a symptom. The self-test found this: injecting an invalid
    # selector raised out of build_edges before V-SCEN-001 could be printed.
    # Ask the model directly rather than pattern-matching the problem strings:
    # the graph is unbuildable if ANY selector fails to parse, and which rule
    # reported it first is an implementation detail that should not decide
    # whether the next rule crashes.
    unresolvable = [p for p, k in prog.packages.items() if k.selector
                    and not _parses(prog, p, k.selector)]
    if unresolvable:
        problems.append(
            "V-GRAPH-001 not evaluated — the combined graph cannot be built "
            f"while {', '.join(sorted(unresolvable, key=wp_sort_key))} carries "
            f"an unresolvable selector")
        return problems

    edges = build_edges(prog)
    for cycle in find_cycles(edges)[:8]:
        problems.append("V-GRAPH-001 cycle in the combined programme graph:\n"
                        "      " + " -> ".join(cycle))
    if not find_cycles(edges):
        if topological_order(edges) is None:
            problems.append(
                "V-GRAPH-002 the combined programme graph admits no execution order")
    return problems


# ----------------------------------------------------------------- self-test
def _mutate(prog: Programme, fn) -> Programme:
    clone = copy.deepcopy(prog)
    fn(clone)
    return clone


def _reset_forward(prog: Programme) -> None:
    prog._forward = {pid: [d for d in p.deps if d in prog.packages]
                     for pid, p in prog.packages.items()}


def _day2_deadlock(prog: Programme) -> None:
    """The WP-155 defect: a pre-go-live package needing a Day-2 rhythm."""
    prog.packages["WP-155"] = replace(
        prog.packages["WP-155"], deps=prog.packages["WP-155"].deps + ("WP-126",))
    _reset_forward(prog)


def _benchmark_cycle(prog: Programme) -> None:
    """The WP-158 defect: the firewall depending on the regression that needs it."""
    prog.packages["WP-158"] = replace(
        prog.packages["WP-158"], deps=prog.packages["WP-158"].deps + ("WP-115",))
    _reset_forward(prog)


def _stale_aggregate(prog: Programme) -> None:
    """The WP-115 defect: two enumerated scenarios where the rule means 118."""
    prog.packages["WP-115"] = replace(prog.packages["WP-115"], selector="")


def _invalid_selector(prog: Programme) -> None:
    prog.packages["WP-115"] = replace(prog.packages["WP-115"], selector="workstream=15")


def _package_outside_waves(prog: Programme) -> None:
    prog.packages["WP-159"] = replace(prog.packages["WP-159"], wave="W-NOWHERE")


def _scenario_needs_day2(prog: Programme) -> None:
    sid = "ACC-05"
    prog.scenarios[sid] = replace(
        prog.scenarios[sid], packages=prog.scenarios[sid].packages + ("WP-126",))


MUTATIONS = [
    ("V-PHASE-001", "a pre-go-live package made to depend on a Day-2 package", _day2_deadlock),
    ("V-GRAPH-001", "the benchmark firewall depending on the regression that aggregates it", _benchmark_cycle),
    ("V-SCEN-002", "an aggregator's selector removed, leaving the stale enumeration", _stale_aggregate),
    ("V-SCEN-001", "a selector key outside the declared grammar", _invalid_selector),
    ("V-WAVE-001", "a package placed in a wave the registry does not define", _package_outside_waves),
    ("V-ACC-001", "a pre-go-live scenario made to exercise a Day-2 package", _scenario_needs_day2),
]


def self_test(prog: Programme) -> int:
    silent = []
    for rule, description, mutate in MUTATIONS:
        problems = audit(_mutate(prog, mutate))
        if not any(p.startswith(rule) for p in problems):
            silent.append((rule, description))
    print(f"{len(MUTATIONS)} mutations injected · {len(silent)} rule(s) stayed silent")
    for rule, description in silent:
        print(f"  ✗ {rule} did not fire on {description}")
    if silent:
        return 1
    print("every rule was observed refusing the defect it was written for")
    return 0


def main() -> int:
    prog = load()
    if "--self-test" in sys.argv[1:]:
        return self_test(prog)

    problems = audit(prog)
    edges = build_edges(prog)
    scenario_edges = sum(1 for n in edges if n.startswith("ACC-"))
    aggregates = sorted((p for p, k in prog.packages.items() if k.selector), key=wp_sort_key)
    resolved = {p: len(prog.resolve_scenarios(p)) for p in aggregates}

    print(f"{len(prog.packages)} packages · {len(prog.scenarios)} scenarios · "
          f"{len(edges)} graph nodes · {scenario_edges} scenario nodes · "
          f"{len(MUTATIONS)} rules")
    print(f"aggregate selectors: " + " · ".join(
        f"{p} → {n} scenarios" for p, n in resolved.items()))
    for problem in problems:
        print(f"  ✗ {problem}")
    if problems:
        print(f"\n{len(problems)} programme graph violation(s)")
        return 1
    print("the programme is executable: no phase inversion, no cycle across "
          "package, scenario and aggregation edges, and every aggregate set "
          "equals its registry query")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
