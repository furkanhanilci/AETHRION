"""The lineage checker must be able to fail, and must fail for the right reasons.

`ADR-004` makes taking a mechanism from another project an auditable act: a
pinned commit, a licence read at the source, a characterisation suite written
before the code moves, and a statement of what the mechanism may never decide.
None of that is worth anything if the checker enforcing it cannot be observed
refusing — a checker that has never failed reports "no findings" and "no
detector" in identical words.

`check_upstream_lineage.py --self-test` injects a defect per rule and reports any
rule that stays silent. These tests bind that guarantee to the suite, so a rule
cannot be weakened without something going red: the self-test is only a control
while something forces it to run.
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_upstream_lineage as lineage       # noqa: E402


@pytest.fixture(scope="module")
def register() -> dict:
    return lineage.load()


@pytest.fixture(scope="module")
def packages() -> set[str]:
    return lineage.known_packages()


def test_the_register_as_committed_passes(register, packages) -> None:
    assert lineage.audit(register, packages) == []


def test_every_rule_can_be_made_to_fire() -> None:
    """The guarantee the register's credibility rests on."""
    result = subprocess.run(
        [sys.executable, "scripts/check_upstream_lineage.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 silent" in result.stdout


def test_generated_index_is_not_hand_edited(register) -> None:
    """`provenance/README.md` is derived; editing it is a defect, not a change."""
    expected = lineage.render(register)
    assert lineage.INDEX.read_text(encoding="utf-8") == expected


# --- the four rules that carry ADR-004's actual obligations --------------------

def mutate(register: dict, fn) -> dict:
    copied = copy.deepcopy(register)
    fn(copied["entries"])
    return copied


def first_of(entries: list[dict], assimilation: str) -> dict:
    return next(e for e in entries if e["assimilation"] == assimilation)


def test_direct_adaptation_cannot_proceed_without_a_pin(register, packages) -> None:
    broken = mutate(register, lambda es: first_of(es, "DIRECT_ADAPT").update(status="ADAPTING"))
    problems = lineage.audit(broken, packages)
    assert any("no pinned commit" in p for p in problems)
    assert any("no characterisation suite" in p for p in problems)


def test_a_branch_name_is_not_a_pin(register, packages) -> None:
    broken = mutate(register, lambda es: es[0].update(pinned_commit="main",
                                                      drift_status="PINNED"))
    assert any("not a 40-character digest" in p for p in lineage.audit(broken, packages))


def test_a_reimplementation_may_not_carry_source_files(register, packages) -> None:
    """If files moved, the decision was direct adaptation and a licence obligation went unrecorded."""
    broken = mutate(register, lambda es: first_of(es, "ADAPTIVE_REIMPLEMENT")
                    .update(source_files=["upstream/thing.py"]))
    assert any("the decision was DIRECT_ADAPT" in p for p in lineage.audit(broken, packages))


def test_every_adopted_mechanism_states_what_it_may_never_decide(register, packages) -> None:
    broken = mutate(register, lambda es: es[0].update(authority_boundary="   "))
    assert any("no authority boundary" in p for p in lineage.audit(broken, packages))


def test_an_unverified_licence_bounds_the_decision(register, packages) -> None:
    """Only DEFER or REJECT may rest on a licence nobody has read."""
    broken = mutate(register, lambda es: first_of(es, "ADAPTIVE_REIMPLEMENT")
                    .update(licence="UNVERIFIED"))
    assert any("UNVERIFIED" in p for p in lineage.audit(broken, packages))


# --- the honesty property this register exists to keep visible ----------------

def test_no_entry_claims_code_has_moved_while_leaving_the_pin_empty(register) -> None:
    """`status` is the honest field. An entry cannot be both under way and unpinned."""
    for entry in register["entries"]:
        if entry["status"] in {"ADAPTING", "ACCEPTED"}:
            assert entry["pinned_commit"], entry["id"]
            assert entry["source_files"] or entry["assimilation"] != "DIRECT_ADAPT", entry["id"]


def test_references_into_the_plan_resolve(register, packages) -> None:
    for entry in register["entries"]:
        for ref in entry["work_packages"]:
            assert ref in packages, f"{entry['id']} references {ref}"


def test_the_register_is_valid_json_with_the_declared_vocabularies(register) -> None:
    types = set(register["assimilation_types"])
    statuses = set(register["statuses"])
    for entry in register["entries"]:
        assert entry["assimilation"] in types, entry["id"]
        assert entry["status"] in statuses, entry["id"]
    # the file is the authority; json.loads round-trips it without loss
    raw = json.loads(lineage.REGISTER.read_text(encoding="utf-8"))
    assert raw == register
