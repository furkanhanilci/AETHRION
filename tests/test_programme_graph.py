"""The programme must be executable, and the check that says so must be able to fail.

A dependency graph can be perfectly acyclic and still impossible to execute.
That is not a subtlety — it is what the v1.3.0 baseline was: `WP-152` needed the
Day-2 postmortem rhythm to define a failure taxonomy that rhythm should consume,
`WP-155` needed recurring recalibration for an initial qualification it must have
before anything runs, and the two cutover aggregators bound two acceptance
scenarios while their own cards said the set was derived. Every check in the
bundle passed, because no check combined package edges with scenario edges,
aggregation edges and scheduling phases.

These tests hold the repaired shape in place and, more importantly, hold the
*detector* in place: `--self-test` injects each historical defect and fails if
the rule written for it stays quiet.
"""
from __future__ import annotations

import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_programme_graph as graph          # noqa: E402
import programme_model                          # noqa: E402


@pytest.fixture(scope="module")
def prog():
    return programme_model.load()


def mutated(prog, fn):
    import copy
    clone = copy.deepcopy(prog)
    fn(clone)
    return clone


# --- the programme as committed ---------------------------------------------

def test_the_programme_as_committed_is_executable(prog) -> None:
    assert graph.audit(prog) == []


def test_every_rule_can_be_made_to_fire() -> None:
    """The guarantee the graph's credibility rests on."""
    result = subprocess.run(
        [sys.executable, "scripts/check_programme_graph.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 rule(s) stayed silent" in result.stdout


# --- the four historical defects, as regression fixtures --------------------

def test_a_pre_go_live_package_may_not_depend_on_a_day2_package(prog) -> None:
    """WP-155 → WP-126. The plan had no valid starting order and nothing said so."""
    broken = mutated(prog, lambda p: (
        p.packages.__setitem__("WP-155", replace(p.packages["WP-155"],
                                                 deps=p.packages["WP-155"].deps + ("WP-126",))),
        graph._reset_forward(p)))
    problems = graph.audit(broken)
    assert any(x.startswith("V-PHASE-001") for x in problems)
    # The diagnostic must name the path, not merely the fact.
    assert any("WP-126 [DAY2_CONTINUOUS]" in x for x in problems)


def test_the_benchmark_firewall_may_not_depend_on_the_regression_that_aggregates_it(prog) -> None:
    """WP-158 → WP-115, with ACC-118 pulled in by WP-115's selector: a cycle.

    It was invisible while the aggregate was a stale two-item list, because the
    edge that closes the loop only exists once the selector resolves properly.
    Fixing the aggregate is what made this defect reachable.
    """
    broken = mutated(prog, lambda p: (
        p.packages.__setitem__("WP-158", replace(p.packages["WP-158"],
                                                 deps=p.packages["WP-158"].deps + ("WP-115",))),
        graph._reset_forward(p)))
    problems = graph.audit(broken)
    assert any(x.startswith("V-GRAPH-001") for x in problems)
    assert any("WP-158" in x and "ACC-118" in x for x in problems)


def test_removing_an_aggregate_selector_is_a_failure_not_a_silence(prog) -> None:
    """The check must not be switchable off by deleting the thing it checks.

    With V-SCEN-002 iterating over packages that *have* a selector, deleting
    WP-115's made the rule pass in silence and restored the two-scenario
    enumeration it exists to prevent. It now iterates over the aggregators
    declared in programme_metadata.json.
    """
    broken = mutated(prog, lambda p: p.packages.__setitem__(
        "WP-115", replace(p.packages["WP-115"], selector="")))
    assert any(x.startswith("V-SCEN-002") for x in graph.audit(broken))


def test_an_unknown_selector_key_is_refused_rather_than_resolving_to_nothing(prog) -> None:
    broken = mutated(prog, lambda p: p.packages.__setitem__(
        "WP-115", replace(p.packages["WP-115"], selector="workstream=15")))
    problems = graph.audit(broken)
    assert any(x.startswith("V-SCEN-001") for x in problems)
    assert any("not evaluated" in x for x in problems), (
        "an unresolvable selector must suspend the graph rules, not crash them")


# --- the properties the repair established ----------------------------------

def test_the_cutover_aggregators_resolve_every_pre_go_live_scenario(prog) -> None:
    expected = set(prog.scenarios_in_phase("PRE_GO_LIVE"))
    assert len(expected) > 100, "guard: the registry should hold most scenarios pre-go-live"
    for pid in prog.required_aggregates:
        resolved = {s for s, _ in prog.resolve_scenarios(pid)}
        assert resolved == expected, pid


def test_adding_a_pre_go_live_scenario_reaches_the_aggregators_with_no_package_edit(prog) -> None:
    """The property the whole selector exists for."""
    before = {s for s, _ in prog.resolve_scenarios("WP-115")}
    grown = mutated(prog, lambda p: p.scenarios.__setitem__(
        "ACC-999", replace(next(iter(p.scenarios.values())),
                           id="ACC-999", phase="PRE_GO_LIVE")))
    after = {s for s, _ in grown.resolve_scenarios("WP-115")}
    assert after - before == {"ACC-999"}


def test_a_day2_scenario_does_not_enter_the_pre_go_live_aggregate(prog) -> None:
    day2 = set(prog.scenarios_in_phase("DAY2_CONTINUOUS"))
    assert day2, "guard: there are Day-2 scenarios to exclude"
    assert not day2 & {s for s, _ in prog.resolve_scenarios("WP-120")}


def test_every_scenario_resolves_to_at_least_one_package(prog) -> None:
    """The matrix bound 91 of 120 before the binding acquired a single owner."""
    unbound = [s for s, sc in prog.scenarios.items() if not sc.packages]
    assert unbound == []


def test_the_wp_acc_binding_has_exactly_one_owner(prog) -> None:
    """There must be no scenario column left in the matrix to disagree with.

    Two sources disagreed on 98 of 120 scenarios, including eleven PRE_GO_LIVE
    scenarios the column bound to Day-2 packages. The column was removed rather
    than synchronised, and this test is what stops it coming back.
    """
    import csv
    header = next(csv.reader(
        (ROOT / "planning" / "commissioning" / "00_PROGRAM"
         / "package_dependency_matrix.csv").open(encoding="utf-8")))
    assert "scenarios" not in header and "explicit_scenarios" not in header
