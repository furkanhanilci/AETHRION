"""A figure can be reproducible, well-laid-out and false. These are the checks that notice.

`aethrion_waves.svg` rendered *"141 work-package documents"* while the registry
held 160, and `aethrion_topology.svg` said *"221 planning files, byte-identical
to baseline v1.0.5"* three baselines and 410 files later. Both regenerated
byte-identically every time, both passed the containment check, and both passed
the count checker — which enforces a derived count only where a rule names the
document and the pattern, and no rule named an SVG.

That is the lesson worth keeping: **a deterministic generator reproduces a false
claim exactly as faithfully as a true one.** A drift check comparing a figure to
its generator can only confirm the generator has not changed its mind.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_document_hygiene as hygiene       # noqa: E402
import check_figure_semantics as semantics     # noqa: E402


# --- figure semantics --------------------------------------------------------

@pytest.fixture(scope="module")
def facts():
    return semantics.registry()


def test_every_figure_claim_matches_the_repository(facts) -> None:
    assert semantics.audit(facts) == []


def test_a_grown_package_registry_is_detected(facts) -> None:
    """The historical defect: the registry moves, the figure does not."""
    moved = dict(facts, packages=facts["packages"] + 19)
    problems = semantics.audit(moved)
    assert any("work-package documents" in p for p in problems)


def test_a_promoted_baseline_is_detected(facts) -> None:
    """`aethrion_topology.svg` carried `v1.0.5` through three baselines."""
    moved = dict(facts, baseline="v9.9.9")
    assert any("baseline" in p for p in semantics.audit(moved))


def test_a_grown_seal_is_detected(facts) -> None:
    moved = dict(facts, sealed=facts["sealed"] + 7)
    assert any("planning files" in p for p in semantics.audit(moved))


def test_the_self_test_entry_point_reports_no_silent_mutation() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_figure_semantics.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 produced no finding" in result.stdout


def test_the_generator_to_figure_mapping_is_read_not_guessed() -> None:
    """`fig_evidence.py` writes `aethrion_evidence_chain.svg`.

    A rule that assumed `fig_X.py → aethrion_X.svg` reported two findings where
    there was no defect. A checker that invents a naming convention and then
    enforces it is worse than no checker, because its findings look like the
    real ones.
    """
    outputs = semantics.figure_outputs()
    assert outputs["fig_evidence.py"] == "aethrion_evidence_chain.svg"
    for svg in outputs.values():
        assert (ROOT / "docs" / "figures" / svg).exists(), svg


def test_the_wave_bars_sum_to_the_registry(facts) -> None:
    """Every package in exactly one wave, checked from the rendered figure."""
    assert semantics.check_wave_coverage(facts) == []


# --- document hygiene --------------------------------------------------------

def test_no_governed_document_has_a_structural_defect() -> None:
    assert hygiene.audit() == {}


def test_every_hygiene_code_fires_on_its_own_specimen() -> None:
    with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
        for code, body in hygiene.SPECIMENS.items():
            probe = Path(tmp) / f"{code.lower()}.md"
            probe.write_text(body, encoding="utf-8")
            assert code in hygiene.audit([probe]), code
            probe.unlink()


def test_no_hygiene_code_fires_on_a_well_formed_document() -> None:
    """The half that decides whether the checker survives contact with the corpus."""
    with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
        probe = Path(tmp) / "clean.md"
        probe.write_text(hygiene.CLEAN, encoding="utf-8")
        assert not (set(hygiene.audit([probe])) & set(hygiene.SPECIMENS))


def test_vendored_skills_are_exempt_from_hygiene_findings() -> None:
    """CLAUDE.md forbids rewriting the vendored eleven.

    One of them carries a repeated H3. Fixing it here would silently fork a file
    that claims to be byte-identical to a named upstream commit, so the exemption
    is derived from each skill's own `airl.upstream_repository` rather than kept
    as a list somebody must remember to extend.
    """
    exempt = hygiene.vendored_skills()
    assert "skills/test-driven-development/" in exempt
    governed = {str(p.relative_to(ROOT)) for p in hygiene.governed()}
    assert not any(g.startswith("skills/test-driven-development/") for g in governed)


def test_the_hygiene_self_test_reports_both_directions() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_document_hygiene.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 undetected" in result.stdout
    assert "0 rule(s) fired on a well-formed document" in result.stdout
