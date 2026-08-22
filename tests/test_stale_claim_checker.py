"""The stale-claim checker must catch the defects it was widened to catch.

Why this exists
    An external review found two stale claims in a corpus whose STATUS page said
    there were none. The checker was green because it was a list of literal
    regexes, and its coverage was narrower than the sentence it printed. Widening
    it fixed that once; this test is what stops it narrowing again.

    It plants the two defects verbatim — the transparency-log claim the interim
    attestation profile explicitly disclaims, and an audit finding described as
    undecided after a decision record decided it — and fails if either survives.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PLANTED = (
    "The `EvidenceManifest` is issued as a signed in-toto attestation recorded "
    "in a public transparency log and anchored in time.\n\n"
    "Which combinations count as independent in a one-person operation is an "
    "undecided question, and finding C2 stays that way.\n"
)


def _run() -> str:
    result = subprocess.run(
        [sys.executable, "scripts/check_stale_claims.py"],
        cwd=ROOT, capture_output=True, text=True,
    )
    return result.stdout


def test_corpus_is_currently_clean() -> None:
    assert "stale present-tense claim" not in _run()


def test_checker_catches_both_planted_defects(tmp_path: Path) -> None:
    probe = ROOT / "docs" / "_stale_probe.md"
    probe.write_text(PLANTED, encoding="utf-8")
    try:
        hits = [line for line in _run().splitlines() if "_stale_probe" in line]
    finally:
        probe.unlink()

    assert len(hits) == 2, f"checker missed a planted defect: {hits}"
    joined = " ".join(hits)
    assert "transparency log" in joined
    assert "C2" in joined


def test_corrections_quote_current_numbers() -> None:
    """A checker whose own advice has gone stale is worse than no checker."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import check_stale_claims as checker

    sealed = len(
        (ROOT / "planning" / "commissioning" / "00_PROGRAM" / "SHA256SUMS.txt")
        .read_text(encoding="utf-8").strip().splitlines()
    )
    figures = len(list((ROOT / "docs" / "figures").glob("*.svg")))
    advice = " ".join(correction for _, correction in checker.CLAIMS)

    assert f"the seal covers {sealed} files" in advice
    assert f"there are {figures} figures" in advice
