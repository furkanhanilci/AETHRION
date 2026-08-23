#!/usr/bin/env python3
"""Check that documents agree with the repository, and with themselves.

Responsibility
    Two failure classes are checked here, both of which a hash seal, a link
    checker and a schema validator all miss:

    1. **Declared counts that drift from reality.** A document says "46
       scenarios" while 51 exist. Nothing is corrupt; the prose is simply wrong.
    2. **A document that contradicts its own header.** A decision record whose
       status says ACCEPTED while its summary still says the decision field is
       blank.

Invariant
    Any number a document states about the repository is derived from the
    repository when the document is touched — never remembered.

Audit findings
    An external readiness review found both classes in this corpus: the
    commissioning inventory kept "46" after the range moved to ACC-51, because a
    later edit changed the range and broke the exact match the count edit
    depended on; and ADR-001's summary still described its own decision as
    unmade after it had been taken. Both are exactly the drift
    `docs/DOCUMENT_STANDARD.md` §3 rule 2 forbids, so the rule now has a check.

    A later inspection found the failure class this checker itself creates: it
    catches exactly the numbers someone wrote a rule for, and every count that
    had drifted — the test count in four documents, the bundle size in three, the
    attestation's subject count, the figure count in the runbook — was one nobody
    had. Rules for those now exist. The class does not close, which is why the
    derived line is printed: the honest reading of a pass is "the registered
    numbers agree", not "no number is stale".

Exit codes
    0 — documents agree with the repository and with themselves.  1 — drift.
"""
from __future__ import annotations

import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
sys.path.insert(0, str(ROOT / "scripts"))


def derive() -> dict[str, int]:
    """Ground truth, computed rather than recalled."""
    def _is(kind: str, name: str) -> bool:
        return bool(re.match(r"^WP-\d{3}_", name)) and name.endswith(f".{kind}.md")

    all_wp = [p for p in PLAN.rglob("WP-*.md") if re.match(r"^WP-\d{3}_", p.name)]
    test_procedures = [p for p in all_wp if _is("tests", p.name)]
    acceptance_criteria = [p for p in all_wp if _is("acceptance", p.name)]
    packages = [p for p in all_wp
                if p not in test_procedures and p not in acceptance_criteria]
    scenarios = [p for p in (PLAN / "12_ACCEPTANCE_SCENARIOS").glob("ACC-*.md")
                 if re.match(r"^ACC-\d{2,3}_", p.name)]
    skills = [d for d in (ROOT / "skills").iterdir()
              if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").exists()]
    seal = (PLAN / "00_PROGRAM" / "SHA256SUMS.txt").read_text().strip().splitlines()
    markdown = list(PLAN.rglob("*.md"))
    figures = list((ROOT / "docs" / "figures").glob("*.svg"))
    numbered = [p for p in packages if p.name != "WP-000_interim_evidence_policy.md"]

    # Counts that drifted in six places while this checker reported "documents
    # agree": nothing was wrong with the rules, there simply were none for these.
    tests = sum(len(re.findall(r"^\s*def test_", p.read_text(encoding="utf-8"), re.M))
                for p in sorted((ROOT / "tests").glob("test_*.py")))
    import write_status                      # the bundle is the authority on its own size
    bundle_checks = len(write_status.CHECKS) + 1         # + the seal, inserted at run time
    envelope = json.loads((ROOT / "delivery" / "WP-000" / "evidence.dsse.json")
                          .read_text(encoding="utf-8"))
    subjects = len(json.loads(base64.b64decode(envelope["payload"]))["subject"])

    return {
        "test_procedures": len(test_procedures),
        "acceptance_criteria": len(acceptance_criteria),
        "tests": tests,
        "bundle_checks": bundle_checks,
        "attestation_subjects": subjects,
        "packages": len(numbered),            # WP-001..140, excluding the bootstrap
        "package_documents": len(packages),   # including WP-000
        "scenarios": len(scenarios),
        "skills": len(skills),
        "sealed": len(seal),
        "plan_markdown": len(markdown),
        "figures": len(figures),
        "highest_scenario": max(int(re.match(r"^ACC-(\d{2,3})_", p.name).group(1))
                               for p in scenarios),
    }


# (file, regex with one capturing group, truth key, human description)
RULES: list[tuple[str, str, str, str]] = [
    ("planning/commissioning/README.md",
     r"\| Work packages \| \*\*(\d+)\*\*", "packages", "work packages"),
    ("planning/commissioning/README.md",
     r"\| Work package documents in total \| \*\*(\d+)\*\*", "package_documents", "package documents"),
    ("planning/commissioning/README.md",
     r"\| Acceptance scenarios \| \*\*(\d+)\*\*", "scenarios", "acceptance scenarios"),
    ("planning/commissioning/README.md",
     r"\| Markdown files under this tree \| (\d+) \|", "plan_markdown", "plan markdown files"),
    ("planning/commissioning/README.md",
     r"\| Test procedure documents \| \*\*(\d+)\*\*", "test_procedures", "test procedure documents"),
    ("planning/commissioning/README.md",
     r"\| Acceptance criteria documents \| \*\*(\d+)\*\*", "acceptance_criteria", "acceptance criteria documents"),
    ("planning/commissioning/README.md",
     r"\| Files covered by the hash seal \| (\d+) ", "sealed", "sealed files"),
    ("README.md", r"(\d+) package documents, \d+ scenarios", "package_documents", "package documents"),
    ("README.md", r"\d+ package documents, (\d+) scenarios", "scenarios", "acceptance scenarios"),
    ("README.md", r"Skill registry \((\d+) skills", "skills", "skills"),
    ("README.md", r"plan seal (\d+)/\d+", "sealed", "sealed files"),
    ("README.md", r"Skills: (\d+)/\d+ conform", "skills", "skills"),
    ("README.md", r"Figures: (\d+)/\d+ match", "figures", "figures"),
    ("skills/README.md", r"All (\d+) conform to the Agent Skills", "skills", "skills"),
    ("skills/README.md", r"\| Scope \| All (\d+) skills", "skills", "skills"),
    ("docs/figures/README.md", r"There are (\w+) of them rather than one", "figures", "figures"),

    # Added after an inspection found the test count stale in four documents and
    # nine places, the bundle size stale in three, and the attestation's subject
    # count stale in one — none of them covered by a rule above.
    ("README.md", r"systemd units · (\d+) tests<br/>", "tests", "tests"),
    ("README.md", r"uv run pytest\s+# (\d+) tests", "tests", "tests"),
    ("README.md", r"(\d+)/\d+ tests pass", "tests", "tests"),
    ("README.md", r"plan seal · (\d+) status checks", "bundle_checks", "bundle checks"),
    ("README.md", r"One command runs all (\w+)\.", "bundle_checks", "bundle checks"),
    ("README.md", r"signature OK, (\d+) subject digests OK", "attestation_subjects", "attestation subjects"),
    ("docs/architecture/AETHRION_ARCHITECTURE.md", r"systemd units · (\d+) tests<br/>", "tests", "tests"),
    ("docs/architecture/AETHRION_ARCHITECTURE.md", r"plan seal · (\d+) status checks", "bundle_checks", "bundle checks"),
    ("tests/README.md", r"\| Scope \| The (\d+) tests that run today \|", "tests", "tests"),
    ("tests/README.md", r"— (\d+) passing; coverage is narrow", "tests", "tests"),
    # Either a spelled-out number or a digit. The spelled table is generated for
    # one to ninety-nine (finding I12); past that the spelled form is a phrase
    # with spaces in it, and demanding one would make the checker refuse a
    # correct document — which is exactly the defect I12 recorded.
    ("tests/README.md", r"\*\*In one paragraph\.\*\* ([A-Za-z-]+|\d+) tests cover", "tests", "tests"),
    ("tests/README.md", r"uv run pytest\s+# all (\d+)", "tests", "tests"),
    ("docs/OPERATIONS.md", r"uv run pytest\s+# (\d+) tests", "tests", "tests"),
    ("docs/OPERATIONS.md", r"Expected: `(\d+) passed`", "tests", "tests"),
    ("docs/OPERATIONS.md", r"`(\d+) figures, 0 drift, 0 overflow`", "figures", "figures"),
]
def _words() -> dict[str, int]:
    """Every spelled-out number from one to ninety-nine.

    This was a hand-written dictionary that happened to reach *forty-five*. The
    suite then grew to forty-six, `tests/README.md` was updated correctly, and
    the checker read the new word as an unknown and reported the old number —
    a consistency check that fails a document for being right. The list of
    numbers is not a judgement, so it is generated.
    """
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
             "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]
    out = {units[n]: n for n in range(1, 10)}
    out |= {teens[n - 10]: n for n in range(10, 20)}
    for n in range(20, 100):
        word = tens[n // 10] + (f"-{units[n % 10]}" if n % 10 else "")
        out[word] = n
    return out


WORDS = _words()


def check_counts(truth: dict[str, int]) -> list[str]:
    problems = []
    for rel, pattern, key, label in RULES:
        path = ROOT / rel
        if not path.is_file():
            problems.append(f"{rel}: file missing, rule cannot be checked")
            continue
        text = path.read_text(encoding="utf-8")
        matches = re.findall(pattern, text)
        if not matches:
            problems.append(f"{rel}: no statement of {label} found (pattern drifted)")
            continue
        for raw in matches:
            value = WORDS.get(raw.lower(), None) if not raw.isdigit() else int(raw)
            if value is None:
                problems.append(f"{rel}: cannot read {label} value {raw!r}")
            elif value != truth[key]:
                problems.append(f"{rel}: says {value} {label}, repository has {truth[key]}")
    return problems


CONTRADICTIONS = (
    ("not taken", "the decision field still reads '(not taken)'"),
    ("leaves the decision field blank", "the summary still says the decision is unmade"),
    ("decision required before", "the header still says a decision is required"),
)


def check_decision_records() -> list[str]:
    """A record whose status is ACCEPTED must not still describe itself as open."""
    problems = []
    for path in sorted((ROOT / "docs" / "architecture").glob("ADR-*.md")):
        text = path.read_text(encoding="utf-8")
        status = re.search(r"\| Status \| (.+?) \|", text)
        if not status or "ACCEPTED" not in status.group(1):
            continue
        for needle, description in CONTRADICTIONS:
            if needle in text:
                problems.append(f"{path.relative_to(ROOT)}: status is ACCEPTED but {description}")
    return problems



def check_matrix_references() -> list[str]:
    """Every WP/ACC identifier named in the scope coverage matrix must exist.

    The matrix answers "does any architecture area lack an implementation and
    acceptance owner". A row citing a package that was renamed reads exactly
    like a row citing one that exists, so the document could report full
    coverage while pointing at nothing — and the closed-row sections are where
    that is most likely, because a row is closed once and read forever after.

    Deliberately shallow. This checks that the identifiers RESOLVE. Whether the
    named package genuinely satisfies the gap is a human judgement and stays
    one: the failure this matrix guards against is closing a row because a
    similarly-named package appeared, and a checker that matched names would
    endorse exactly that.
    """
    matrix = PLAN / "00_PROGRAM" / "11_scope_coverage_matrix.md"
    if not matrix.exists():
        return []
    text = matrix.read_text(encoding="utf-8")
    packages = {p.name[:6] for p in PLAN.rglob("WP-*.md")
                if re.match(r"^WP-\d{3}_", p.name)}
    scenarios = {re.match(r"^(ACC-\d{2,3})_", p.name).group(1)
                 for p in (PLAN / "12_ACCEPTANCE_SCENARIOS").glob("ACC-*.md")
                 if re.match(r"^ACC-\d{2,3}_", p.name)}

    problems = []
    for match in re.finditer(r"\bWP-(\d{3})\b", text):
        pid = f"WP-{match.group(1)}"
        if pid not in packages:
            line = text[:match.start()].count("\n") + 1
            problems.append(
                f"11_scope_coverage_matrix.md:{line}: names {pid}, which is not "
                f"a package in the plan")
    # Ranges like "ACC-081–120" name their endpoints; both must resolve.
    for match in re.finditer(r"\bACC-(\d{2,3})\b", text):
        sid = f"ACC-{match.group(1)}"
        if sid not in scenarios:
            line = text[:match.start()].count("\n") + 1
            problems.append(
                f"11_scope_coverage_matrix.md:{line}: names {sid}, which is not "
                f"a scenario in the plan")
    return problems


def check_baseline_agreement() -> list[str]:
    """One baseline identity, named in one place, agreed everywhere it appears.

    `programme_metadata.json` owns it. `delivery/progress.json` carries it too
    because progress lives outside the seal and must still say which
    specification it is progress against — so the two are compared rather than
    one being derived, and a disagreement is a hard failure.
    """
    meta = PLAN / "00_PROGRAM" / "programme_metadata.json"
    ledger = ROOT / "delivery" / "progress.json"
    if not (meta.exists() and ledger.exists()):
        return []
    canonical = json.loads(meta.read_text(encoding="utf-8"))["commissioning_baseline"]["version"]
    recorded = json.loads(ledger.read_text(encoding="utf-8")).get("baseline")
    if recorded != canonical:
        return [f"delivery/progress.json says baseline {recorded!r}; "
                f"00_PROGRAM/programme_metadata.json says {canonical!r}"]
    return []



# Checks the CI workflow is not expected to run, each with the resource it needs
# that a runner does not have. Declared here rather than inferred, so adding a
# check to the bundle forces a decision: automate it, or say why not.
CI_MANUAL = {
    "scripts/check_vault.py": "the operator's Obsidian vault",
    "scripts/mcp_smoke.py": "a live Bridge",
    "scripts/acceptance_v0.py": "a live Bridge and a local Zotero library",
}


def check_ci_covers_the_bundle() -> list[str]:
    """The CI workflow must run every bundle check it can, or say why it cannot.

    `fig_verification.py` already refuses to draw a figure that under-reports the
    bundle. Nothing applied the same rule to the workflow, and the workflow was
    running thirteen of twenty checks — so activating CI would have produced a
    green badge covering two thirds of the bundle, which is a worse artifact than
    no badge at all.

    Only `run:` lines count. An earlier version of this rule matched the whole
    file and passed on a script that appeared solely in a comment listing what
    the workflow does NOT run — the comment satisfying the check that the comment
    exists to explain.
    """
    workflow = ROOT / "deploy" / "bvc-01-verify.yml"
    if not workflow.exists():
        return []
    text = workflow.read_text(encoding="utf-8")
    executed = "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("#")
    )

    sys.path.insert(0, str(ROOT / "scripts"))
    import write_status

    problems = []
    for name, command, _ in write_status.CHECKS:
        script = next((c for c in command if str(c).startswith("scripts/")), None)
        if script is None:
            continue
        if script in executed:
            continue
        if script in CI_MANUAL:
            if script not in text:
                problems.append(
                    f"deploy/bvc-01-verify.yml: {script} is declared manual "
                    f"(needs {CI_MANUAL[script]}) but the workflow never says so")
            continue
        problems.append(
            f"deploy/bvc-01-verify.yml: the bundle runs {name} ({script}) and "
            f"the workflow does not. Either add it, or declare it in CI_MANUAL "
            f"with the resource a runner lacks — a CI badge that covers part of "
            f"the bundle while looking like all of it is worse than no badge")
    for script in sorted(CI_MANUAL):
        if script in executed:
            problems.append(
                f"deploy/bvc-01-verify.yml runs {script}, which is declared "
                f"manual — the declaration is now wrong, not the workflow")
    return problems


def main() -> int:
    truth = derive()
    print("derived from the repository: " +
          " · ".join(f"{k} {v}" for k, v in truth.items() if k != "highest_scenario"))

    problems = (check_counts(truth) + check_decision_records()
                + check_matrix_references() + check_baseline_agreement()
                + check_ci_covers_the_bundle())
    for problem in problems:
        print(f"  ✗ {problem}")

    if problems:
        print(f"\n{len(problems)} inconsistenc{'y' if len(problems) == 1 else 'ies'} — documents FAIL")
        return 1
    print("\ndocuments agree with the repository and with themselves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
