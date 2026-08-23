"""A decision that never reaches the package executing it has not been made.

The plan decided what to adopt, what to copy and refactor, and what to
reimplement natively. Those decisions were sound, they carried licences and
authority boundaries, and they lived in the architecture corpus while the work
lived in a package document — with nothing joining the two.

The visible shape of the gap: AIDE was a registered `DIRECT_ADAPT` source for
WP-144's candidate state machine and the string "AIDE" appeared nowhere in
WP-144, so an implementer reading only the package would have rewritten a
mechanism the architecture had already decided to take. The mirror image was
WP-041, titled *LiteLLM Model Gateway Foundation*, naming a component no
register knew existed — adoption with no version policy, no failure semantics
and no statement of what it may never decide.

These tests hold both directions shut, and hold shut the two ways the fix could
rot: an obligation quietly treated as met, and a package reaching `READY` with
one still open.
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import acquisition_model as model                                 # noqa: E402
import check_wp_implementation_sources as binding                 # noqa: E402
import expand_acquisition                                         # noqa: E402


def _registers() -> tuple[dict, dict]:
    return (binding.load_components(),
            json.loads(model.UPSTREAMS.read_text(encoding="utf-8")))


def test_every_binding_rule_can_be_made_to_fail() -> None:
    """A checker never observed refusing reports 'no findings' and 'no detector'
    in identical words."""
    result = subprocess.run(
        [sys.executable, "scripts/check_wp_implementation_sources.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 silent" in result.stdout


def test_the_registers_agree_with_the_packages_they_are_bound_to() -> None:
    components, upstreams = _registers()
    documents = model.packages()
    texts = {pid: path.read_text(encoding="utf-8") for pid, path in documents.items()}
    assert binding.audit(components, upstreams, documents, texts) == []


def test_a_registered_source_is_visible_in_the_package_that_executes_it() -> None:
    """The WP-144 case, stated as a rule rather than as an anecdote."""
    for entry_id, _, packages_, _ in [
            r for r in _bindings() if r[2]]:
        for pid in packages_:
            text = model.packages()[pid].read_text(encoding="utf-8")
            assert entry_id in text, (
                f"{pid} is bound to {entry_id} and does not name it — the decision "
                f"reaches nobody who has to act on it")


def _bindings() -> list[tuple]:
    return model.registered_names(with_mode=True)


def test_no_obligation_is_reported_as_met_while_its_field_is_empty() -> None:
    """`PROPOSED` everywhere means every mode's obligation is still open.

    If this ever passes trivially it means the obligation table stopped being
    consulted, which is exactly how a pre-implementation blocker becomes
    decorative.
    """
    components, upstreams = _registers()
    direct = [e for e in upstreams["entries"] if e["assimilation"] == "DIRECT_ADAPT"]
    assert direct, "the register no longer records any direct adaptation"
    for entry in direct:
        open_items = model._unresolved(entry, "DIRECT_ADAPT")
        if entry.get("pinned_commit") is None:
            assert any("pinned" in item for item in open_items)
        if not entry.get("characterization_suite"):
            assert any("characterisation" in item for item in open_items)


def test_an_unresolved_acquisition_holds_a_package_out_of_the_ready_queue() -> None:
    """The rule that makes the block load-bearing rather than informational.

    WP-144 depends on six packages, so today it is blocked on dependencies and
    the acquisition hold is invisible. The hold is what stops it being started
    the moment those six are accepted, so it is tested directly rather than
    waiting for the programme to reach it.
    """
    holds = model.unresolved_packages()
    assert "WP-144" in holds, "WP-144 takes AIDE and MLEvolve and nothing is pinned"
    assert any("ASM-007" in item for item in holds["WP-144"])

    import ready_queue
    packages = ready_queue.load_plan()
    # Everything WP-144 waits on is accepted; only the acquisition is open.
    progress = {pid: {"state": "ACCEPTED"} for pid in packages}
    progress["WP-144"] = {"state": "NOT_STARTED"}
    page = ready_queue.render(copy.deepcopy(packages), progress)

    ready = page.split("## 1. Ready now — ")[1].split("\n")[0]
    held = page.split("## 2. Held — acquisition unresolved — ")[1].split("\n")[0]
    assert int(held) >= 1, "a package with an open acquisition obligation was not held"
    assert "**WP-144**" in page.split("## 2. Held")[1].split("## 3. In flight")[0], (
        "WP-144 has every dependency accepted and an unpinned DIRECT_ADAPT source; "
        "it must appear under Held, not under Ready now")
    assert "**WP-144**" not in page.split("## 1. Ready now")[1].split("## 2. Held")[0]
    assert ready.isdigit()


def test_build_native_is_stated_rather_than_left_to_silence() -> None:
    """An implementer must be able to tell 'no upstream' from 'nobody recorded one'."""
    for pid, path in model.packages().items():
        text = path.read_text(encoding="utf-8")
        assert "`BUILD_NATIVE`" in text, f"{pid} does not classify its own residue"


def test_the_projection_is_current_for_every_package() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/expand_acquisition.py", "--check"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 drift entries" in result.stdout


def test_a_component_entry_states_what_aethrion_keeps_when_it_is_replaced() -> None:
    """Adoption without an owned contract is an architecture, not an adoption —
    the thing ADR-004 refuses in its first sentence."""
    components, _ = _registers()
    for entry in components["entries"]:
        assert (entry.get("owned_contract") or "").strip(), entry["id"]
        assert (entry.get("authority_boundary") or "").strip(), entry["id"]
        assert (entry.get("not_used") or "").strip(), entry["id"]


def test_a_benchmark_never_carries_production_authority() -> None:
    _, upstreams = _registers()
    marks = ("never", "not ", "no ")
    for entry in upstreams["entries"]:
        if entry["assimilation"] != "BENCHMARK":
            continue
        boundary = entry["authority_boundary"].lower()
        assert any(m in boundary for m in marks), (
            f"{entry['id']}: a benchmark measures the system and is never part of "
            f"it; its boundary must say so")


def test_the_table_helper_cannot_break_a_row_or_run_off_the_page() -> None:
    assert "|" not in model.cell("a | b")
    assert "\n" not in model.cell("a\nb")
    assert model.cell("word " * 200).endswith("…")
    assert model.cell("") == "—"


def test_the_generated_block_is_the_only_part_the_generator_touches() -> None:
    """Everything outside the marker is hand-authored and must survive a run."""
    path = model.packages()["WP-144"]
    before = path.read_text(encoding="utf-8")
    outside = before.split(expand_acquisition.OPEN)[0]
    subprocess.run([sys.executable, "scripts/expand_acquisition.py"],
                   cwd=ROOT, capture_output=True, text=True)
    after = path.read_text(encoding="utf-8")
    assert after.split(expand_acquisition.OPEN)[0] == outside
    assert after == before, "a second run changed the document — generation is not stable"
