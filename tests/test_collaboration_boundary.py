"""The boundary ADR-020 draws, held shut by tests rather than by intention.

Adopting a collaboration substrate is attractive precisely because it removes a
large amount of work that differentiates nothing. The cost is that the substrate
arrives fast, present and full of text that looks like instructions, and every
convenience it offers is a way of quietly acquiring authority it was never
granted.

Nothing here is built, so these are not integration tests. They are tests on the
*registers and the plan* — the artifacts that decide what the integration will be
allowed to do — and they exist because the boundary is cheapest to hold now, when
it costs an assertion, rather than after an adapter exists and holding it costs a
migration.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import acquisition_model as model                                 # noqa: E402

BACKEND = "CMP-045"
ADR = ROOT / "docs" / "architecture" / "ADR-020_collaboration_backend_and_runtime.md"


def _components() -> list[dict]:
    return json.loads(model.COMPONENTS.read_text(encoding="utf-8"))["entries"]


def _upstreams() -> list[dict]:
    return json.loads(model.UPSTREAMS.read_text(encoding="utf-8"))["entries"]


def _entry(entries: list[dict], eid: str) -> dict:
    return next(e for e in entries if e["id"] == eid)


def test_the_decision_record_exists_and_is_accepted() -> None:
    assert ADR.is_file()
    status = re.search(r"\| Status \| (.+?) \|", ADR.read_text(encoding="utf-8"))
    assert status and "ACCEPTED" in status.group(1)


def test_the_backend_is_a_replaceable_backend_and_not_a_dependency() -> None:
    """An OPTIONAL_BACKEND carries the obligation that the choice is recorded.

    A DEPENDENCY would not: it would say the thing is called and be silent about
    whether anything else could be.
    """
    backend = _entry(_components(), BACKEND)
    assert backend["adoption"] == "OPTIONAL_BACKEND"
    assert backend["selection"], "a backend with no recorded qualification was chosen by whoever wrote it down first"


def test_the_backend_states_what_it_may_never_decide() -> None:
    backend = _entry(_components(), BACKEND)
    boundary = backend["authority_boundary"].lower()
    for forbidden in ("claimversion", "gate", "decisionrecord", "blackboard"):
        assert forbidden in boundary, f"the boundary does not mention {forbidden}"
    assert "never" in boundary or "not" in boundary


def test_the_removal_test_is_written_down_where_it_can_be_run() -> None:
    """"Remove the backend and say what disappears" is the whole architecture
    test, and an architecture test that lives only in an ADR is an intention."""
    backend = _entry(_components(), BACKEND)
    assert "removing the backend" in backend["authority_boundary"].lower()

    card = model.packages()["WP-148"].read_text(encoding="utf-8")
    assert "backend-loss" in card.lower() or "Backend loss" in card
    tests = model.packages()["WP-148"].with_name(
        model.packages()["WP-148"].name.replace(".md", ".tests.md")
    ).read_text(encoding="utf-8")
    assert "Destroy every room" in tests, "the removal test has no procedure"


def test_no_runtime_is_adopted_as_the_only_one() -> None:
    """A runtime layer with one runtime is not a runtime layer."""
    runtimes = [e for e in _components()
                if e["adoption"] == "OPTIONAL_BACKEND"
                and "AgentRuntimeProfile" in (e.get("owned_contract") or "")]
    assert len(runtimes) >= 3, "the ACP layer must stay plural to be worth having"
    for entry in runtimes:
        assert entry["selection"], entry["id"]


def test_a_runtime_is_never_recorded_as_a_role() -> None:
    hermes = next(e for e in _components() if e["name"].startswith("Hermes"))
    assert "not a role" in hermes["not_used"].lower()


def test_the_pinned_adaptation_is_legal_and_still_has_not_moved() -> None:
    """The licence was read at the source, so R7 no longer refuses the mode.

    What must not happen next is the quiet step: a pin and a permissive licence
    make an adaptation *legal*, and `ADR-004` still requires upstream behaviour
    captured in tests before any code is taken. This test fails the moment the
    entry claims to be adapting without that suite.
    """
    manifest = _entry(_upstreams(), "ASM-060")
    assert manifest["assimilation"] == "DIRECT_ADAPT"
    assert manifest["licence"] == "Apache-2.0"
    assert manifest["licence_verified"], "a permissive mode with no date the licence was read"
    assert manifest["pinned_commit"] and len(manifest["pinned_commit"]) == 40
    assert manifest["drift_status"] == "PINNED"
    assert manifest["source_files"], "a direct adaptation with no named file list"

    # The load-bearing half. If this ever passes trivially, check why.
    assert manifest["characterization_suite"] is None
    assert manifest["status"] == "PROPOSED", (
        "the entry left PROPOSED without a characterisation suite — R5 exists to "
        "refuse exactly this")
    assert not manifest["local_modules"], (
        "a local module exists for an entry that has not been characterised — "
        "code moved before the suite that would detect divergence")


def test_a_pinned_commit_is_a_commit_and_not_a_branch() -> None:
    import re
    for entry in _upstreams():
        pin = entry.get("pinned_commit")
        if pin is None:
            assert entry.get("drift_status") == "NOT_PINNED", entry["id"]
            continue
        assert re.fullmatch(r"[0-9a-f]{40}", pin), f"{entry['id']}: {pin!r} is not a digest"
        assert entry.get("drift_status") != "NOT_PINNED", entry["id"]


def test_the_vendored_engineering_skills_are_registered_rather_than_only_noticed() -> None:
    superpowers = _entry(_upstreams(), "ASM-066")
    assert superpowers["assimilation"] == "VENDORED"
    assert superpowers["pinned_commit"] and len(superpowers["pinned_commit"]) == 40
    assert superpowers["licence"] == "MIT"
    assert len(superpowers["source_files"]) == 11
    for path in superpowers["source_files"]:
        assert (ROOT / path).is_dir(), path
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    assert superpowers["pinned_commit"] in notice, (
        "the register and NOTICE must agree on the pin, or one of them is decorative")


def test_every_buzz_entry_says_what_is_not_taken() -> None:
    for entry in _components() + _upstreams():
        blob = json.dumps(entry).lower()
        if "buzz" not in blob:
            continue
        excluded = entry.get("not_used") or entry.get("not_taken") or ""
        assert excluded.strip(), f"{entry['id']} takes something and says nothing about what it does not"


def test_the_affected_packages_carry_the_decision() -> None:
    """A decision reaches the package that executes it, or it reaches nobody."""
    for pid in ("WP-046", "WP-047", "WP-048", "WP-148", "WP-149",
                "WP-150", "WP-153", "WP-154", "WP-159"):
        text = model.packages()[pid].read_text(encoding="utf-8")
        assert "ADR-020" in text, f"{pid} was patched by the delta and does not cite the decision"


def test_a_completion_signal_is_never_a_package_state() -> None:
    card = model.packages()["WP-154"].read_text(encoding="utf-8")
    assert "TECH_COMPLETE" in card and "DONE" in card
    assert re.search(r"`DONE`[^.]*not[^.]*`TECH_COMPLETE`|"
                     r"not[^.]*`TECH_COMPLETE`[^.]*`ACCEPTED`", card, re.S), (
        "the one guard this package must carry is that a chat message is not a state")


def test_every_figure_generator_is_actually_run() -> None:
    """make_figures listed sixteen generators against twenty-one figures, so five
    were never regenerated while the drift check reported zero drift."""
    import make_figures
    generators = {p.stem for p in (ROOT / "scripts").glob("fig_*.py")} - {"figure_kit"}
    assert generators == set(make_figures.MODULES), (
        f"generators never run: {sorted(generators - set(make_figures.MODULES))}")
