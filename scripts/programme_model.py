#!/usr/bin/env python3
"""The one place the programme's shape is read from.

Responsibility
    Load the canonical programme: packages with their phases, waves and scenario
    bindings; scenarios with their acceptance phases; the wave and phase
    registries; the baseline identity. Every generator, validator and figure
    that needs any of those imports it from here.

Why this module exists at all
    Because the same fact had three homes and they disagreed. Wave membership
    was hard-coded in ``expand_packages.py`` and again in ``fig_waves.py``, both
    stopping at ``WP-140``, while ``02_wave_and_dependency_map.md`` described
    W-S and W-R in prose. The figure rendered *"141 work-package documents"*
    while the repository held 160, and every check passed: the containment check
    measures text boxes, the drift check compares the figure to the generator
    that produced it, and the count checker had no rule for a number inside an
    SVG. A deterministic generator reproduced a false claim exactly.

    Phase was worse, because it was never written down at all. It was inferred
    from a workstream folder name in one place and from ``range(122, 131)`` in
    another, and the second could only see scenario→package edges — so both of
    the real deadlocks, which are package→package edges, were invisible.

The rule this module enforces by construction
    A fact with one owner cannot disagree with itself. Nothing here computes a
    wave from a number range or a phase from a folder name; both are columns in
    ``package_dependency_matrix.csv``, one row per package, and this module
    refuses to load a matrix where either is missing or unknown.

One owner for the WP↔ACC binding
    A scenario document's "Related packages" row is the only place that relation
    is written. The matrix used to carry the reverse of it in a ``scenarios``
    column, and the two disagreed on 98 of 120 scenarios — including eleven
    PRE_GO_LIVE scenarios the column bound to Day-2 packages, invisible because
    the validator read the document and the generator read the column. The
    column was removed rather than synchronised.

Selector resolution
    ``resolve_scenarios`` returns the union of a package's explicit bindings and
    whatever its selector matches, each carrying *why it is present*. That
    provenance is the point: a reviewer reading a generated commissioning
    checklist must be able to see which rows were chosen deliberately and which
    arrived because they match a rule.
"""
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field, replace
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
MATRIX = PLAN / "00_PROGRAM" / "package_dependency_matrix.csv"
METADATA = PLAN / "00_PROGRAM" / "programme_metadata.json"
ACC_DIR = PLAN / "12_ACCEPTANCE_SCENARIOS"

EARLY_PHASES = {"BOOTSTRAP", "PRE_GO_LIVE", "CUTOVER"}
LATE_PHASES = {"POST_GO_LIVE_HYPERCARE", "DAY2_CONTINUOUS"}


class ProgrammeModelError(Exception):
    """The canonical model cannot be loaded. Never degrade to a default."""


@dataclass(frozen=True)
class Package:
    id: str
    title: str
    workstream: str
    phase: str
    wave: str
    effort: str
    owner: str
    verifier: str
    deps: tuple[str, ...]
    gates: tuple[str, ...]
    controls: tuple[str, ...]
    explicit_scenarios: tuple[str, ...]
    selector: str


@dataclass(frozen=True)
class Scenario:
    id: str
    title: str
    severity: str
    category: str
    phase: str
    packages: tuple[str, ...]
    then: str
    path: Path


@dataclass
class Programme:
    packages: dict[str, Package]
    scenarios: dict[str, Scenario]
    waves: list[dict]
    phases: list[dict]
    baseline: dict
    grammar: dict
    required_aggregates: dict[str, str]
    _forward: dict[str, list[str]] = field(default_factory=dict)

    # ---- graph ------------------------------------------------------------
    def forward(self, pid: str) -> list[str]:
        return self._forward.get(pid, [])

    def closure(self, pid: str) -> set[str]:
        seen: set[str] = set()
        stack = list(self.forward(pid))
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            stack.extend(self.forward(n))
        return seen

    def shortest_path(self, src: str, targets: set[str]) -> list[str] | None:
        """The shortest dependency path from src into targets, for diagnostics.

        A validator that prints "cycle detected" has told the reader nothing
        they can act on. Printing the path — with each node's phase — turns a
        failure into an instruction.
        """
        from collections import deque
        queue = deque([(src, [src])])
        seen = {src}
        while queue:
            node, path = queue.popleft()
            for dep in self.forward(node):
                if dep in seen:
                    continue
                seen.add(dep)
                if dep in targets:
                    return path + [dep]
                queue.append((dep, path + [dep]))
        return None

    # ---- selectors --------------------------------------------------------
    def resolve_scenarios(self, pid: str) -> list[tuple[str, str]]:
        """(scenario_id, why) pairs — explicit bindings plus selector matches.

        Sorted numerically rather than lexically, because ACC-9 must not sort
        after ACC-118 in a checklist a human reads top to bottom.
        """
        package = self.packages[pid]
        resolved: dict[str, str] = {}
        for sid in package.explicit_scenarios:
            if sid not in self.scenarios:
                raise ProgrammeModelError(
                    f"{pid} binds {sid}, which is not in the scenario registry")
            resolved[sid] = "explicit binding"
        if package.selector:
            key, value = self.parse_selector(package.selector, pid)
            for sid, scenario in self.scenarios.items():
                if scenario.phase == value:
                    resolved.setdefault(sid, f"selected by {key}={value}")
        return [(sid, resolved[sid]) for sid in sorted(resolved, key=acc_sort_key)]

    def parse_selector(self, selector: str, pid: str = "?") -> tuple[str, str]:
        if "=" not in selector:
            raise ProgrammeModelError(
                f"{pid}: selector {selector!r} is not key=value")
        key, _, value = selector.partition("=")
        allowed = self.grammar["keys"]
        if key not in allowed:
            raise ProgrammeModelError(
                f"{pid}: selector key {key!r} is not one of {sorted(allowed)}")
        if value not in allowed[key]:
            raise ProgrammeModelError(
                f"{pid}: selector value {value!r} is not one of {allowed[key]}")
        return key, value

    def scenarios_in_phase(self, phase: str) -> list[str]:
        return sorted((s for s, sc in self.scenarios.items() if sc.phase == phase),
                      key=acc_sort_key)

    def wave_name(self, wave_id: str) -> str:
        for wave in self.waves:
            if wave["id"] == wave_id:
                return f"{wave['id']} — {wave['name']}"
        raise ProgrammeModelError(f"wave {wave_id!r} is not in the wave registry")


def acc_sort_key(sid: str) -> tuple[int, str]:
    m = re.match(r"ACC-(\d+)", sid)
    return (int(m.group(1)), sid) if m else (10 ** 9, sid)


def wp_sort_key(pid: str) -> tuple[int, str]:
    m = re.match(r"WP-(\d+)", pid)
    return (int(m.group(1)), pid) if m else (10 ** 9, pid)


def _split(value: str, seps: str = ";") -> tuple[str, ...]:
    parts = re.split(f"[{seps}]", value) if len(seps) > 1 else value.split(seps)
    return tuple(p.strip() for p in parts if p.strip() and p.strip() != "—")


@lru_cache(maxsize=1)
def load() -> Programme:
    meta = json.loads(METADATA.read_text(encoding="utf-8"))
    wave_ids = {w["id"] for w in meta["waves"]}
    phase_ids = {p["id"] for p in meta["scheduling_phases"]}

    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8")))
    required = {"scheduling_phase", "wave_id", "scenario_selector"}
    missing = required - set(rows[0].keys())
    if missing:
        raise ProgrammeModelError(
            f"the matrix is missing {sorted(missing)} — the canonical model "
            f"cannot be reconstructed from folder names and number ranges, "
            f"which is what it replaced")

    packages: dict[str, Package] = {}
    for row in rows:
        pid = row["package_id"].strip()
        phase, wave = row["scheduling_phase"].strip(), row["wave_id"].strip()
        if phase not in phase_ids:
            raise ProgrammeModelError(f"{pid}: unknown scheduling phase {phase!r}")
        if wave not in wave_ids:
            raise ProgrammeModelError(f"{pid}: unknown wave {wave!r}")
        packages[pid] = Package(
            id=pid, title=row["title"].strip(), workstream=row["workstream"].strip(),
            phase=phase, wave=wave, effort=row["effort"].strip(),
            owner=row["owner"].strip(), verifier=row["verifier"].strip(),
            deps=_split(row["hard_dependencies"]),
            gates=_split(row["gates"], ";,"), controls=_split(row["controls"], ";,"),
            explicit_scenarios=(),      # filled from the scenario registry below
            selector=row["scenario_selector"].strip(),
        )

    scenarios: dict[str, Scenario] = {}
    for path in sorted(ACC_DIR.glob("ACC-*.md")):
        m = re.match(r"^(ACC-\d{2,3})_", path.name)
        if not m:
            continue
        text = path.read_text(encoding="utf-8")

        def fld(pattern, default=""):
            found = re.search(pattern, text, re.M)
            return found.group(1).strip() if found else default

        scenarios[m.group(1)] = Scenario(
            id=m.group(1),
            title=fld(r"^# ACC-\d{2,3} — (.+)$"),
            severity=fld(r"\| Severity \| \*\*(.+?)\*\* \|"),
            category=fld(r"\| Category \| (.+?) \|"),
            phase=fld(r"\| Acceptance phase \| `(.+?)`"),
            packages=tuple(sorted({f"WP-{n}" for n in
                                   re.findall(r"WP-(\d{3})", fld(r"\| Related packages \| (.+?) \|"))},
                                  key=wp_sort_key)),
            then=fld(r"\*\*Then:\*\* (.+?)\n"),
            path=path,
        )

    # The WP↔ACC binding has exactly one owner: the scenario document's
    # "Related packages" row. It used to have two — that row and a `scenarios`
    # column in the matrix — and they disagreed on 98 of 120 scenarios. Among
    # the disagreements were eleven PRE_GO_LIVE scenarios the matrix bound to
    # Day-2 packages, which no check could see because the validator read the
    # document and the generator read the column.
    #
    # The column is gone rather than synchronised. A cache with a drift check is
    # still two representations of one fact, and ADR-014's answer to that is not
    # a better check.
    derived: dict[str, list[str]] = {}
    for sid, scenario in scenarios.items():
        for pid in scenario.packages:
            derived.setdefault(pid, []).append(sid)
    for pid, sids in derived.items():
        if pid not in packages:
            raise ProgrammeModelError(
                f"scenario(s) {sorted(sids, key=acc_sort_key)} name {pid}, "
                f"which is not in the package registry")
        packages[pid] = replace(
            packages[pid],
            explicit_scenarios=tuple(sorted(sids, key=acc_sort_key)))

    prog = Programme(packages=packages, scenarios=scenarios, waves=meta["waves"],
                     phases=meta["scheduling_phases"],
                     baseline=meta["commissioning_baseline"],
                     grammar=meta["scenario_selector_grammar"],
                     required_aggregates=meta["aggregate_packages"]["required"])
    prog._forward = {pid: [d for d in p.deps if d in packages]
                     for pid, p in packages.items()}
    return prog


if __name__ == "__main__":
    p = load()
    print(f"{len(p.packages)} packages · {len(p.scenarios)} scenarios · "
          f"{len(p.waves)} waves · {len(p.phases)} phases · "
          f"baseline {p.baseline['version']}")
    for pid in sorted((k for k, v in p.packages.items() if v.selector), key=wp_sort_key):
        r = p.resolve_scenarios(pid)
        n_sel = sum(1 for _, why in r if why.startswith("selected"))
        print(f"  {pid} selector {p.packages[pid].selector!r} resolves {len(r)} "
              f"scenarios ({len(r) - n_sel} explicit, {n_sel} selected)")
