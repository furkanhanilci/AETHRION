#!/usr/bin/env python3
"""Create and maintain the two companion documents every work package needs.

Why a package is three documents
    A package card answers *what is this and what does it depend on*. It is read
    at refinement, by someone deciding whether the package can start. The test
    procedure is read months later by whoever runs the tests, and the acceptance
    criteria are read by an **independent verifier** who must reach a verdict
    without having done the work.

    Those are three readers with three questions, and folding them into one file
    means the verifier reads implementation notes to find the criterion, and the
    tester reads dependency analysis to find the command. Splitting them is also
    what makes the verifier's document *frozen-packet-able*: `00_PROGRAM/06`
    requires a reviewer to work from a package they can be handed, and a criteria
    document that is a section inside the producer's working card is not that.

Structure
    The companions follow the information items of **ISO/IEC/IEEE 29119-3:2021** —
    the common elements of §5.2 (unique identifier, approval authority, status,
    references) and the dynamic test process items of §8 (test design, test
    coverage items, test cases, test procedure, test data requirements, test
    environment requirements, readiness reports, execution log, incident report),
    plus the completion report of §7.4. The standard is adopted for its
    *document structure*, not its process: this programme's evidence layers
    E0–E5 and its gate model come from `00_PROGRAM/06`, not from 29119-2.

Invariant
    Everything between a ``<!-- generated:… -->`` marker and its closing marker is
    derived and is rewritten on every run. Everything else is authored and is
    preserved. A first run creates the file with the scaffolding and empty
    authored sections; later runs never touch what a human wrote.

Exit codes
    0 — every companion matches what the plan implies.  1 — drift or a missing
    companion.

Usage
    python3 scripts/make_package_companions.py            # create / refresh
    python3 scripts/make_package_companions.py --check    # fail on drift
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"
MATRIX = PLAN / "00_PROGRAM" / "package_dependency_matrix.csv"
SCENARIOS = PLAN / "12_ACCEPTANCE_SCENARIOS"

OPEN = "<!-- generated:{name} — produced by scripts/make_package_companions.py; do not edit inside this block -->"
CLOSE = "<!-- /generated:{name} -->"

# Evidence layers, from 00_PROGRAM/06_evidence_and_acceptance_strategy.md.
LAYERS = {
    "E0": ("Structural", "Does the file, schema or reference exist?"),
    "E1": ("Mechanical", "Is the behaviour correct under a deterministic test?"),
    "E2": ("Security", "Is the forbidden path actually blocked?"),
    "E3": ("Independent review", "Did an actor outside the producer examine the semantics?"),
    "E4": ("Reproduction", "Does the same package run again in a clean environment?"),
    "E5": ("Operations", "Are failure, restore and observability correct?"),
}

# Which layers a package must satisfy, from the gates it touches. Cheap layers
# always apply; the expensive ones are earned by what the package can break.
GATE_LAYERS = {
    "G5": "E4", "G7": "E4", "G6": "E3", "G8": "E3",
    "Platform": "E5", "Day-2": "E5", "Cutover": "E5", "Commissioning": "E5",
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_packages() -> dict[str, dict]:
    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8")))
    out = {}
    for row in rows:
        pid = row["package_id"].strip()
        out[pid] = {
            "id": pid,
            "title": row["title"].strip(),
            "workstream": row["workstream"].strip(),
            "effort": row["effort"].strip(),
            "owner": row["owner"].strip(),
            "verifier": row["verifier"].strip(),
            "deps": [d.strip() for d in row["hard_dependencies"].split(";")
                     if d.strip() and d.strip() != "—"],
            "gates": [g.strip() for g in re.split(r"[;,]", row["gates"]) if g.strip()],
            "controls": [c.strip() for c in re.split(r"[;,]", row["controls"]) if c.strip()],
            "scenarios": [s.strip() for s in re.split(r"[;,]", row["scenarios"])
                          if s.strip() and s.strip() != "—"],
        }
    return out


def find_cards() -> dict[str, Path]:
    return {p.name[:6]: p for p in PLAN.rglob("WP-*.md")
            if re.match(r"^WP-\d{3}_", p.name)
            and not p.name.endswith((".tests.md", ".acceptance.md"))}


def card_sections(text: str) -> dict[str, list[str]]:
    """Deliverables, tasks and the risk lines the companions have to cover."""
    deliverables = []
    block = re.search(r"## Mandatory deliverables\n(.*?)\n## ", text, re.S)
    if block:
        deliverables = [m.group(1) for line in block.group(1).splitlines()
                        if (m := re.match(r"-\s+`(.+?)`\s*$", line.strip()))]
    tasks = re.findall(r"^\| (WP-\d{3}-T\d{2}) \| (.+?) \|", text, re.M)
    return {"deliverables": deliverables, "tasks": tasks}


def layers_for(package: dict) -> list[str]:
    required = {"E0", "E1", "E2"}          # never optional: exist, behave, refuse
    for gate in package["gates"]:
        for key, layer in GATE_LAYERS.items():
            if gate.startswith(key):
                required.add(layer)
    if package["scenarios"]:
        required.add("E3")                  # a scenario implies an outside reader
    if package["effort"] == "L":
        required.add("E3")
    return sorted(required)


# ---- generated blocks ------------------------------------------------------
def block_identity(package: dict, kind: str, card_rel: str) -> list[str]:
    other = "acceptance criteria" if kind == "tests" else "test procedures"
    other_file = card_rel.replace(".md", f".{'acceptance' if kind == 'tests' else 'tests'}.md")
    label = "TP" if kind == "tests" else "AC"
    return [
        "| Field | Value |",
        "|---|---|",
        f"| Unique identifier | `{label}-{package['id']}` |",
        f"| Work package | [`{package['id']}` — {package['title']}]({Path(card_rel).name}) |",
        f"| Companion | [{other}]({Path(other_file).name}) |",
        f"| Workstream | `{package['workstream']}` |",
        f"| Approval authority | **{package['verifier']}** — the independent verifier |",
        f"| Accountable owner | {package['owner']} |",
        "| Status at baseline | `NOT_STARTED` |",
        "| Change history | `git log --follow` on this file; the plan seal covers its bytes |",
        "| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |",
        "| Live state | `python3 scripts/progress.py show " + package["id"] + "` |",
    ]


def block_strategy(package: dict) -> list[str]:
    required = layers_for(package)
    lines = [
        "The evidence layers this package must satisfy, derived from the gates it "
        "touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: "
        "**cheap layers run first**, because an independent reviewer's attention is "
        "the expensive resource and should not be spent on what a mechanical check "
        "would have caught.",
        "",
        "| Layer | Question it answers | Required here | Why |",
        "|---|---|:--:|---|",
    ]
    for key, (name, question) in LAYERS.items():
        needed = key in required
        if key in ("E0", "E1"):
            why = "never optional — the artifact must exist and behave"
        elif key == "E2":
            why = "never optional — a control that has not been observed refusing is prose"
        elif key == "E3":
            reasons = []
            if package["scenarios"]:
                reasons.append(f"bound to {len(package['scenarios'])} acceptance scenario(s)")
            if package["effort"] == "L":
                reasons.append("effort class L")
            why = " · ".join(reasons) if needed else "no scenario and not L"
        elif key == "E4":
            why = ("touches " + " / ".join(g for g in package["gates"] if g.startswith(("G5", "G7")))
                   if needed else "no execution or reproduction gate")
        else:
            why = ("touches " + " / ".join(g for g in package["gates"]
                                           if g.startswith(("Platform", "Day-2", "Cutover", "Commissioning")))
                   if needed else "no platform or day-2 gate")
        lines.append(f"| **{key}** {name} | {question} | {'**yes**' if needed else 'no'} | {why} |")
    lines += [
        "",
        f"**Applicable layers: {' · '.join(required)}.** A layer marked *no* is not a "
        "waiver: it means this package cannot produce that evidence, and a claim "
        "that needs it must be earned by a package that can.",
    ]
    return lines


def block_environment(package: dict, packages: dict) -> list[str]:
    lines = [
        "ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a "
        "description, a responsibility and the period it is needed for. An item "
        "without a named responsibility is an item nobody will have provisioned on "
        "the day the tests run.",
        "",
        "| Item | Description | Responsibility | Period needed |",
        "|---|---|---|---|",
        f"| Target revision | The single commit every result is bound to | {package['owner']} | For the whole test run; results from two revisions are not evidence |",
        f"| Environment manifest | Hardware, image digest, SBOM — captured, not described | {package['owner']} | Captured at the start of the run |",
        "| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |",
        f"| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | {package['verifier']} | At completion |",
    ]
    for dep in package["deps"]:
        if dep in packages:
            lines.append(f"| `{dep}` accepted output | {packages[dep]['title']} | {packages[dep]['owner']} | Before the first test case runs |")
    lines += [
        "",
        "### Environment readiness report — §8.8",
        "",
        "Every row must be checked before the first test case. An unchecked row is a "
        "stop condition, not a risk to manage.",
        "",
        "- [ ] The target revision is pinned and recorded.",
        "- [ ] The environment manifest has been **captured** from the running "
        "environment rather than written from intention.",
        "- [ ] The workspace is isolated from the producer's working tree.",
        "- [ ] Every dependency listed above is `ACCEPTED` "
        "(`python3 scripts/ready_queue.py`).",
        "- [ ] The evidence sink is reachable and a specimen manifest verifies.",
        "- [ ] The rollback or compensation path named on the package card can "
        "actually be exercised in this environment.",
    ]
    return lines


def block_data(package: dict) -> list[str]:
    return [
        "ISO/IEC/IEEE 29119-3 §8.5 and §8.7. Test data is a **deliverable of this "
        "package**, not a by-product of running it: a test whose fixture cannot be "
        "regenerated cannot be re-run, and a result that cannot be re-run is an "
        "anecdote.",
        "",
        "| Requirement | Rule |",
        "|---|---|",
        "| Provenance | Every fixture is either synthetic or a licensed extract with its licence recorded. Personal or production data is never a fixture |",
        "| Data class | Every fixture carries a `DataClass`; a fixture above D2 requires the matching `ExecutionProfile` |",
        "| Regeneration | Each fixture is regenerated from a committed script or manifest, byte-identically |",
        "| Negative fixtures | Every schema and every control has at least one fixture that **must fail**. A test set with no failing fixture proves nothing |",
        "| Independence | Fixtures are not shared with any evaluation golden set (`PR-15` — eval contamination) |",
        "",
        "### Test data readiness report — §8.7",
        "",
        "- [ ] Every fixture regenerates byte-identically from its committed source.",
        "- [ ] Every fixture carries a `DataClass` and, above D2, an `ExecutionProfile`.",
        "- [ ] At least one **negative** fixture exists per schema and per control.",
        "- [ ] No fixture overlaps an evaluation golden set.",
        "- [ ] Fixture licences permit the retention this test run requires.",
    ]


def block_coverage(package: dict, sections: dict, scenarios: dict) -> list[str]:
    lines = [
        "ISO/IEC/IEEE 29119-3 §8.3.2. A coverage item is something the tests must "
        "reach. The two sources are mechanical: every mandatory deliverable of this "
        "package, and every acceptance scenario bound to it. A coverage item with no "
        "test case is a gap, and it is listed here so the gap is visible rather than "
        "assumed away.",
        "",
        "| # | Coverage item | Source | Covered by |",
        "|---:|---|---|---|",
    ]
    index = 1
    for item in sections["deliverables"]:
        lines.append(f"| C{index:02d} | `{item}` | Mandatory deliverable | *(name the test case)* |")
        index += 1
    for task_id, task in sections["tasks"]:
        lines.append(f"| C{index:02d} | {task} | {task_id} | *(name the test case)* |")
        index += 1
    for sid in package["scenarios"]:
        scenario = scenarios.get(sid)
        if scenario:
            lines.append(f"| C{index:02d} | {scenario['title']} | [{sid}](../12_ACCEPTANCE_SCENARIOS/{scenario['file']}) — {scenario['severity']} | *(name the test case)* |")
            index += 1
    lines += [
        "",
        f"**{index - 1} coverage items.** Every one must appear in the *Covered by* "
        "column of at least one test case below before this package can reach "
        "`TECH_COMPLETE`.",
    ]
    return lines


def block_exit(package: dict) -> list[str]:
    return [
        "The run is complete when every line holds. These are conditions on the "
        "**testing**, not on the package: a complete test run that found defects is "
        "complete.",
        "",
        "- [ ] Every coverage item above is named by at least one executed test case.",
        "- [ ] Every executed test case has an actual result and a verdict (§8.9).",
        "- [ ] Every case at layer **E2** has been observed to **fail** in its "
        "negative direction. A control that has only ever passed has not been tested.",
        "- [ ] Every deviation from this procedure is recorded in the completion "
        "report (§7.4.3) — including cases that were skipped and why.",
        "- [ ] Every incident raised has a severity, a priority and a status (§8.11).",
        "- [ ] All results are bound to **one** target revision.",
        "- [ ] The residual risk list is written, with an owner and an expiry for each "
        "entry (§7.4.7).",
        "",
        "> **Not an exit condition.** That every test passed. A procedure that can "
        "only complete on success has no way to report a defect, which is the "
        "outcome it exists to produce.",
    ]


def block_dod(package: dict, packages: dict) -> list[str]:
    lines = [
        "From `00_PROGRAM/05_definition_of_ready_and_done.md`, instantiated for this "
        "package. Every line is a condition on **evidence**, not on effort.",
        "",
        "### Definition of Ready",
        "",
        "- [ ] The package purpose and its single delivery boundary are written.",
        "- [ ] Out-of-scope items are written down.",
        f"- [ ] **{package['owner']}** is assigned accountable; an implementer is "
        f"named; **{package['verifier']}** is assigned verifier and is "
        "**independent of the producer** under WP-007's profile.",
    ]
    if package["deps"]:
        for dep in package["deps"]:
            title = packages.get(dep, {}).get("title", "")
            lines.append(f"- [ ] `{dep}` — {title} — is `ACCEPTED` (not `TECH_COMPLETE`).")
    else:
        lines.append("- [ ] No hard dependency; this package can start once the "
                     "programme is authorised.")
    lines += [
        "- [ ] `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential "
        "scope are classified — all four, with no `UNKNOWN`.",
        "- [ ] Acceptance criteria name **a number, a threshold or a command**. "
        "`00_PROGRAM/05` states that the generic template criteria are not "
        "measurable in the sense meant here; refinement is where that is fixed.",
        "- [ ] Migration, rollback or compensation behaviour is defined.",
        "- [ ] A three-point `O`/`M`/`P` estimate exists and capacity is reserved.",
        "",
        "### Definition of Done — package acceptance",
        "",
        "- [ ] Every acceptance criterion below passed **on the same target revision**.",
        "- [ ] Test results are bound to artifact hashes and an environment manifest.",
        f"- [ ] **{package['verifier']}** verified **independently of the producer** "
        "and did not see the producer's working trace.",
        "- [ ] Security, data and policy **negative** tests passed.",
        "- [ ] Contract compatibility and downstream consumer tests are green.",
        "- [ ] No open Critical or High finding. Accepted Medium/Low risks each carry "
        "a named owner and an expiry.",
        "- [ ] Rollback or compensation was exercised at least once, and the result "
        "is referenced.",
        "- [ ] Working evidence exists via a dashboard, alert or audit query — not "
        "only via a test log.",
        "- [ ] The `EvidenceManifest` is signed and verifies, and its `limitations` "
        "list is present.",
        "",
        "### Definition of Commissioned",
        "",
    ]
    if package["scenarios"]:
        lines.append("An `ACCEPTED` package is still not production-ready. Every "
                     "scenario below must pass **on the same release candidate**:")
        lines.append("")
        for sid in package["scenarios"]:
            lines.append(f"- [ ] `{sid}` passes. A `SKIPPED` scenario on a Critical row "
                         "does not count as a pass.")
    else:
        lines.append("**No acceptance scenario names this package.** It can reach "
                     "`ACCEPTED` on its own evidence and cannot reach `COMMISSIONED` "
                     "through a scenario, because there is none to pass. "
                     "`00_PROGRAM/11`'s completeness rule calls this an incomplete "
                     "entry rather than a shorter one.")
    return lines


def block_nonwaivable(package: dict) -> list[str]:
    lines = [
        "From `00_PROGRAM/07_programme_risk_register.md`: *critical security, "
        "identity, evidence, reproduction and data blockers cannot be lowered by a "
        "numeric total.* The score exists for prioritisation; it is not a waiver "
        "mechanism.",
        "",
        "The following cannot be waived on this package under any residual-risk "
        "acceptance:",
        "",
        "- [ ] Identity and correlation failures.",
        "- [ ] Data routing across a trust-zone boundary without policy.",
        "- [ ] Artifact integrity or lineage loss.",
        "- [ ] A reviewer independence violation.",
        "- [ ] A missing or unverifiable `EvidenceManifest`.",
    ]
    for control in package["controls"]:
        lines.append(f"- [ ] `{control}` failing its effectiveness test.")
    lines += [
        "",
        "> A package with an open item above is `BLOCKED`, not `ACCEPTED with "
        "conditions`. The distinction is the reason the list exists.",
    ]
    return lines


def load_scenarios() -> dict[str, dict]:
    out = {}
    for path in sorted(SCENARIOS.glob("ACC-*.md")):
        m = re.match(r"^ACC-\d{2}", path.name)
        if not m:
            continue
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^# ACC-\d{2} — (.+)$", text, re.M)
        severity = re.search(r"\|\s*Severity\s*\|\s*\*\*(.+?)\*\*", text)
        then = re.search(r"\*\*Then:\*\* (.+?)\n", text)
        out[m.group(0)] = {
            "id": m.group(0), "file": path.name,
            "title": title.group(1).strip() if title else m.group(0),
            "severity": severity.group(1) if severity else "",
            "then": then.group(1).strip() if then else "",
        }
    return out


# ---- assembly --------------------------------------------------------------
def splice(text: str, name: str, body: list[str]) -> str:
    open_marker, close_marker = OPEN.format(name=name), CLOSE.format(name=name)
    block = "\n".join([open_marker, "", *body, "", close_marker])
    pattern = re.compile(re.escape(open_marker) + r".*?" + re.escape(close_marker), re.S)
    if not pattern.search(text):
        raise KeyError(name)
    return pattern.sub(lambda _: block, text)


def skeleton(package: dict, kind: str, card_rel: str, scenarios: dict) -> str:
    label = "Test Procedures" if kind == "tests" else "Acceptance Criteria"
    if kind == "tests":
        authored = [
            "## Test cases",
            "",
            "<!-- authored: one row per case; each must name a coverage item above. -->",
            "",
            "*Not yet authored. Until this section is written the package cannot reach "
            "`READY`: `00_PROGRAM/05` requires the acceptance measurement method to be "
            "reachable before work starts.*",
            "",
            "## How to execute",
            "",
            "*Not yet authored.*",
            "",
        ]
        sections = [
            ("Document identity", "identity"),
            ("Test strategy extract — §8.2.5", "strategy"),
            ("Test environment requirements — §8.6", "environment"),
            ("Test data requirements — §8.5", "data"),
            ("Test coverage items — §8.3.2", "coverage"),
        ]
        tail = [
            "## Test execution log — §8.10",
            "",
            "One row per executed case. The log is evidence and is written **as the "
            "run happens**, not reconstructed afterwards.",
            "",
            "| Case | Date/time (UTC) | Executed by | Revision | Actual result | Verdict | Evidence |",
            "|---|---|---|---|---|---|---|",
            "| | | | | | | |",
            "",
            "## Incident reporting — §8.11",
            "",
            "Any deviation between an actual and an expected result raises an incident "
            "carrying timing, originator, context, description, the originator's "
            "assessment of **severity** and **priority**, the risk, and a status. An "
            "incident is not closed by the person who raised it deciding it was "
            "probably fine: `00_PROGRAM/06` requires a reproducer result before a "
            "critical finding can be closed.",
            "",
            "| Incident | Raised | Case | Severity | Priority | Risk | Status | Disposition |",
            "|---|---|---|---|---|---|---|---|",
            "| | | | | | | | |",
            "",
            "## Test completion report — §7.4",
            "",
            "Written once, at the end of the run, and handed to the verifier with the "
            "evidence package.",
            "",
            "- **Summary of testing performed:**",
            "- **Deviations from this procedure** (including every skipped case and why):",
            "- **Completion evaluation** against the exit criteria below:",
            "- **Factors that blocked progress:**",
            "- **Test measures** (cases executed / passed / failed / blocked; coverage items reached):",
            "- **Residual risks**, each with an owner and an expiry:",
            "- **Test deliverables** produced:",
            "- **Reusable test assets:**",
            "- **Lessons learned:**",
            "",
            "## Exit criteria",
            "",
            OPEN.format(name="exit"),
            "",
            CLOSE.format(name="exit"),
            "",
        ]
    else:
        authored = [
            "## Package-specific acceptance criteria",
            "",
            "<!-- authored: every criterion needs a number, a threshold or a command, "
            "and a named test case. -->",
            "",
            "*Not yet authored.*",
            "",
            "## What this package cannot establish",
            "",
            "*Not yet authored.*",
            "",
        ]
        sections = [
            ("Document identity", "identity"),
            ("How to read a criterion", "howto"),
        ]
        tail = [
            "## Programme-level gates",
            "",
            OPEN.format(name="dod"),
            "",
            CLOSE.format(name="dod"),
            "",
            "## Non-waivable items",
            "",
            OPEN.format(name="nonwaivable"),
            "",
            CLOSE.format(name="nonwaivable"),
            "",
            "## Verifier's decision",
            "",
            "Completed by the independent verifier, not by the producer. "
            "**Issuance is not acceptance** — a package that has produced evidence "
            "and has not been verified is `TECH_COMPLETE`.",
            "",
            "| Field | Value |",
            "|---|---|",
            "| Verifier | |",
            "| Independence profile applied | R1 / R2 declared-partial / R3 — see ADR-001 |",
            "| Dimensions **not** met | *(an R2 profile that lists only its strengths is not a declaration)* |",
            "| Target revision verified | |",
            "| Decision | `PENDING` / `ACCEPTED` / `REJECTED` |",
            "| Date | |",
            "| Conditions and their expiry | |",
            "",
        ]

    head = [
        f"# {package['id']} — {package['title']} — {label}",
        "",
    ]
    body: list[str] = []
    for title, marker in sections:
        body += [f"## {title}", "", OPEN.format(name=marker), "", CLOSE.format(name=marker), ""]
    return "\n".join(head + body + authored + tail)


def build(package: dict, kind: str, card: Path, scenarios: dict, existing: str | None) -> str:
    card_rel = card.name
    text = existing if existing is not None else skeleton(package, kind, card_rel, scenarios)
    sections = card_sections(card.read_text(encoding="utf-8"))
    packages = PACKAGES

    text = splice(text, "identity", block_identity(package, kind, card_rel))
    if kind == "tests":
        text = splice(text, "strategy", block_strategy(package))
        text = splice(text, "environment", block_environment(package, packages))
        text = splice(text, "data", block_data(package))
        text = splice(text, "coverage", block_coverage(package, sections, scenarios))
        text = splice(text, "exit", block_exit(package))
    else:
        text = splice(text, "howto", [
            "A criterion belongs here only if it can **fail**. `00_PROGRAM/05` lists "
            "what is not evidence, and the first entry is an implementer's free-text "
            "declaration of success.",
            "",
            "| A criterion states | Not |",
            "|---|---|",
            "| a number, a threshold or a command | \"works correctly\" |",
            "| the observation that would falsify it | \"has been reviewed\" |",
            "| the test case that decides it | \"all tests pass\" |",
            "| what it does **not** establish | silence about its own limits |",
            "",
            "Each criterion names the test case in "
            f"[`{card_rel.replace('.md', '.tests.md')}`]({card_rel.replace('.md', '.tests.md')}) "
            "that decides it. A criterion with no test case cannot be verified, and a "
            "test case that decides no criterion is not part of acceptance.",
        ])
        text = splice(text, "dod", block_dod(package, packages))
        text = splice(text, "nonwaivable", block_nonwaivable(package))
    return text


PACKAGES: dict[str, dict] = {}


def main() -> int:
    global PACKAGES
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    PACKAGES = load_packages()
    cards = find_cards()
    scenarios = load_scenarios()

    created = updated = drift = 0
    for pid in sorted(PACKAGES):
        card = cards.get(pid)
        if card is None:
            print(f"  ✗ {pid}: no package card")
            return 1
        for kind in ("tests", "acceptance"):
            path = card.with_name(card.name.replace(".md", f".{kind}.md"))
            existing = path.read_text(encoding="utf-8") if path.is_file() else None
            text = build(PACKAGES[pid], kind, card, scenarios, existing)
            if existing is None:
                if args.check:
                    print(f"  ✗ {pid}: {kind} companion missing")
                    drift += 1
                else:
                    path.write_text(text, encoding="utf-8")
                    created += 1
            elif text != existing:
                if args.check:
                    print(f"  ✗ {pid}: {kind} generated block does not match the plan")
                    drift += 1
                else:
                    path.write_text(text, encoding="utf-8")
                    updated += 1

    if args.check:
        print(f"{len(PACKAGES) * 2} companion documents checked, {drift} drift entries")
        return 1 if drift else 0
    print(f"{len(PACKAGES) * 2} companion documents — {created} created, {updated} refreshed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
