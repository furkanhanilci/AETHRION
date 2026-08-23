"""The regression rules must be able to fire, and must stay quiet where prose is correct.

`35_DEFINITION_OF_DONE_FINAL_AUDIT.md` ends with a list of wordings a final
audit should search for: a single-agent default, a fully-connected topology
presented as the target, a mechanical check doing semantic work, a timeout that
approves, an event treated as authority, a projection treated as canonical, a
published number without its binding, the engineering family demoted to tooling.

Every one of those phrases already appears in this repository — inside a
sentence that forbids it. That is the whole difficulty, and it is why each rule
in `check_stale_claims.py` carries two specimens rather than one. A rule that
matches everything passes a positive-only test; a rule that matches nothing
passes a negative-only test. Both are required, and this module makes something
force them to run.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_stale_claims as stale       # noqa: E402


def test_every_regression_rule_fires_on_its_own_positive_specimen() -> None:
    silent = [r.name for r in stale.REGRESSIONS if not r.fires_on(r.specimen_dirty)]
    assert silent == [], f"rules that never refuse: {silent}"


def test_no_regression_rule_fires_on_its_own_negative_specimen() -> None:
    """The corpus is full of these phrases used correctly; suppression is the hard half."""
    noisy = [r.name for r in stale.REGRESSIONS if r.fires_on(r.specimen_clean)]
    assert noisy == [], f"rules that flag correct prose: {noisy}"


def test_the_self_test_entry_point_reports_zero_silent_rules() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_stale_claims.py", "--self-test"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 silent" in result.stdout and "0 firing" in result.stdout


def test_the_repository_itself_is_clean() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_stale_claims.py"],
        cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout


# --- the two guards, pinned to the defects that produced them -----------------

def timeout_rule() -> stale.Regression:
    return next(r for r in stale.REGRESSIONS if r.name == "a timeout that approves")


def test_a_deliverable_heading_naming_the_absent_branch_is_not_a_regression() -> None:
    """`Timeout escalation path with no approval branch` appears in nine packages.

    It is correct in all nine, and the paragraph guard cannot see why: a bullet
    in a deliverable list has no sentence around it to carry a prohibition. The
    thirty characters before the match are what rescue it.

    Written as three separate functions rather than one parametrised case on
    purpose. `check_doc_consistency.py` derives the repository's test count by
    counting test functions, and every document that states that count is
    checked against it — so a parametrised test makes `pytest` print a number no
    document is allowed to contain. The convention here is that the number a
    reader runs is the number the documents state.
    """
    assert not timeout_rule().fires_on(
        "Timeout escalation path with no approval branch")


def test_a_policy_denying_auto_approval_is_not_a_regression() -> None:
    assert not timeout_rule().fires_on(
        "There is no auto-approval anywhere in the gate policy")


def test_a_count_of_zero_auto_approve_paths_is_not_a_regression() -> None:
    assert not timeout_rule().fires_on(
        "The delegation matrix contains zero auto-approve paths")


def test_an_incidental_negation_does_not_suppress_a_real_regression() -> None:
    """The inverse defect, and the reason the paragraph guard dropped the bare word "not".

    "If the reviewer does not respond ... the gate auto-approves" contains
    "not", and the first version of the guard read that as a refusal.
    """
    rule = next(r for r in stale.REGRESSIONS if r.name == "a timeout that approves")
    assert rule.fires_on(
        "If the reviewer does not respond within 48 hours the gate auto-approves "
        "so the pipeline proceeds.")


def test_a_derived_store_named_beside_canonical_records_is_not_a_claim() -> None:
    """ACC-21 and ACC-119 both describe a projection and the canonical store in one breath.

    The rule once allowed fifty characters between the store's name and the word
    "canonical", which made "the Neo4j/pgvector/OpenSearch derived read model;
    the canonical records are intact" a finding. It is the opposite of one.
    """
    rule = next(r for r in stale.REGRESSIONS
                if r.name == "a projection treated as canonical")
    assert not rule.fires_on(
        "Node, edge and index corruption has been deliberately introduced into "
        "the Neo4j/pgvector/OpenSearch derived read model; the canonical "
        "records are intact.")
    assert rule.fires_on(
        "Neo4j is the canonical store for the scientific record.")


def test_every_rule_names_the_decision_record_it_defends() -> None:
    """A correction that does not say which decision was violated is an opinion."""
    for rule in stale.REGRESSIONS:
        assert any(token in rule.correction
                   for token in ("ADR-", "skills/")), rule.name


# --- the CI workflow may not under-report the bundle it claims to run --------

def test_the_ci_workflow_runs_every_automatable_bundle_check() -> None:
    """`fig_verification.py` refuses to draw a figure that under-reports the
    bundle. Nothing applied the same rule to CI, and CI ran thirteen of twenty
    checks — so activating it would have produced a green badge covering two
    thirds of the bundle, which is worse than no badge."""
    import check_doc_consistency as consistency

    assert consistency.check_ci_covers_the_bundle() == []


def test_a_check_named_only_in_a_comment_does_not_count_as_covered(tmp_path) -> None:
    """The first version of the rule matched the whole file, so a script listed
    in the comment explaining what CI does NOT run satisfied the check that the
    comment exists to explain."""
    import check_doc_consistency as consistency

    workflow = ROOT / "deploy" / "bvc-01-verify.yml"
    original = workflow.read_text(encoding="utf-8")
    line = ("      - name: Every skill is reachable, and its core rule intact\n"
            "        run: uv run python scripts/check_skill_baseline.py\n")
    assert line in original, "fixture drifted; update the line this test removes"
    try:
        workflow.write_text(
            original.replace(line, "      #   scripts/check_skill_baseline.py\n"),
            encoding="utf-8")
        problems = consistency.check_ci_covers_the_bundle()
        assert any("check_skill_baseline" in p for p in problems)
    finally:
        workflow.write_text(original, encoding="utf-8")


def test_every_manually_declared_check_names_the_resource_a_runner_lacks() -> None:
    """A check excused from CI without a reason is a check quietly dropped."""
    import check_doc_consistency as consistency

    for script, reason in consistency.CI_MANUAL.items():
        assert reason and len(reason) > 8, script
        assert (ROOT / script).exists(), script
