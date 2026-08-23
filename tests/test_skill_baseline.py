"""The routing half of skill behaviour, held in place.

`docs/STATUS.md` carried *"skills conform to a format; none has a behaviour
baseline"* for as long as the registry existed. That sentence was two claims
wearing one: whether a skill can be **reached**, and whether loading it changes
what an agent does. Only the second needs a model runtime. The first was simply
never checked — and seventeen of fifty-two skills failed it.

The consequence was not abstract. `dispatching-parallel-analysts` was
unreachable while `dispatching-parallel-agents` sat in the router table, so a
task needing genuinely independent analyses routed to the skill that decomposes
work with one right answer. `ADR-012` forbids exactly that substitution, and it
would have been reached not by bad judgement but by the correct option being
absent.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_skill_baseline as baseline       # noqa: E402


@pytest.fixture(scope="module")
def fixtures() -> dict:
    return json.loads(baseline.FIXTURES.read_text(encoding="utf-8"))


def test_the_routing_baseline_holds() -> None:
    assert baseline.audit() == []


def test_every_skill_is_reachable_from_the_router(fixtures) -> None:
    names = baseline.registry()
    found = baseline.reachable_from(fixtures["reachability"]["root"],
                                    baseline.references(names))
    assert names - found - set(fixtures["reachability"]["exempt"]) == set()


def test_every_rule_can_be_made_to_fire() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_skill_baseline.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 rule(s) stayed silent" in result.stdout


def test_the_four_pairs_stay_in_different_families(fixtures) -> None:
    """A router that sees one family cannot choose between two members of it."""
    for pair in fixtures["non_synonym_pairs"]:
        engineering = baseline.domain_of(pair["engineering"])
        for sci in pair["scientific"]:
            assert engineering != baseline.domain_of(sci), pair


def test_both_halves_of_every_pair_are_routable(fixtures) -> None:
    """The specific defect: the scientific half absent, the engineering half present.

    That is worse than both being absent. With neither routable a task stalls
    and someone looks; with one routable it proceeds, plausibly, into the wrong
    discipline.
    """
    names = baseline.registry()
    found = baseline.reachable_from(fixtures["reachability"]["root"],
                                    baseline.references(names))
    for pair in fixtures["non_synonym_pairs"]:
        assert pair["engineering"] in found
        for sci in pair["scientific"]:
            assert sci in found, f"{sci} unreachable while {pair['engineering']} is not"


def test_each_governed_skill_still_contains_its_own_core_rule(fixtures) -> None:
    """A skill can drift out of the rule it exists to state and still parse."""
    for name, rule in fixtures["content_invariants"].items():
        text = baseline.skill_text(name).lower()
        for phrase in rule["must_contain"]:
            assert phrase.lower() in text, f"{name}: {rule['why']}"


# --- the honesty property, which is the reason this file can be trusted ------

def test_the_execution_layer_is_reported_as_unrun_and_never_as_passing(fixtures) -> None:
    """A behaviour baseline that printed PASS for work that did not happen would
    convert an honest gap into a false assurance — the exact failure this whole
    system is built against."""
    execution = fixtures["execution_fixtures"]
    assert "never run" in execution["status"].lower()
    assert execution["blocked_by"]
    assert execution["fixtures"], "the corpus must exist even though it cannot run"

    result = subprocess.run(
        [sys.executable, "scripts/check_skill_baseline.py"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0
    assert "not run" in result.stdout
    assert "never run" in result.stdout


def test_the_execution_fixtures_name_real_skills(fixtures) -> None:
    """The corpus is worthless if it points at skills that do not exist.

    It cannot be run today, which makes this the only check standing between it
    and quiet rot.
    """
    names = baseline.registry()
    for fixture in fixtures["execution_fixtures"]["fixtures"]:
        assert fixture["expect_skill"] in names, fixture["id"]
        assert fixture["markers"], fixture["id"]
        assert fixture["expect_family"] in {"engineering", "scientific-research", "shared"}


def test_the_hardest_fixture_is_the_one_that_reads_scientific_and_is_not(fixtures) -> None:
    """SBF-08 exists because ADR-012's rule runs in a direction people forget.

    Research adaptations *extend* their engineering counterparts; they do not
    replace them. Building the Claim Ledger that stores preregistrations is
    test-driven-development work, however scientific the noun sounds.
    """
    hard = next(f for f in fixtures["execution_fixtures"]["fixtures"]
                if f["id"] == "SBF-08")
    assert hard["expect_family"] == "engineering"
    assert hard["expect_skill"] == "test-driven-development"
    assert "why_hard" in hard
