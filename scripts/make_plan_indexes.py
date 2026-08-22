#!/usr/bin/env python3
"""Generate a README for every commissioning workstream, from the packages in it.

Responsibility
    Fourteen directories hold 141 work-package documents and 51 acceptance
    scenarios with no way in. This writes each directory's index **from the files
    it contains**, so a reader arriving at a folder learns what it is for, what
    is in it, what each package depends on, and what is adopted rather than
    built.

Invariant
    These indexes are derived. Editing one by hand is a defect: the next run
    overwrites it, and `--check` fails the build in the meantime. That is
    deliberate — a hand-maintained index of 141 packages drifts within a week.

Audit findings
    Written after a structural audit found that no workstream directory had an
    index, so the plan could only be navigated by knowing package numbers in
    advance.

Usage
    python3 scripts/make_plan_indexes.py [--check]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "planning" / "commissioning"

PURPOSE = {
    "00_PROGRAM": ("Programme documents", "How the programme is run: the plan's own rules, the "
                   "target state, the wave map, the catalogue, definitions of ready and done, "
                   "the evidence strategy, risk, capacity, change control, the go-live "
                   "checklist and scope coverage."),
    "01_GOVERNANCE": ("Governance and policy", "Who decides, under what authority, with which "
                      "assurance class — and the bootstrap package that makes acceptance "
                      "possible at all."),
    "02_CONTRACTS": ("Canonical contracts", "The identity, manifest, event, policy, source, "
                     "claim and run schemas that every plane binds to. A contract with no "
                     "consumer is a parallel universe, which is why these come before services."),
    "03_FOUNDATION": ("Platform foundation", "Databases, object storage, event transport, "
                      "derived read models and CI — the substrate every later service assumes."),
    "04_CONTROL_EVENT": ("Control and event planes", "Temporal as the process authority and "
                         "NATS as event transport. Events carry notifications; they never "
                         "carry authority."),
    "05_MODEL_AGENT_TOOL": ("Model, agent and tool platform", "Model gateway, capability "
                            "registry, qualification, routing, the agent runtime, the role and "
                            "skill registries, harness adapters and the tool broker."),
    "06_EXECUTION_SECURITY": ("Execution and security", "Sandboxing, workload identity, policy "
                              "enforcement, secrets, egress and untrusted-content handling."),
    "07_LITERATURE_KNOWLEDGE": ("Literature and knowledge", "Source identity, representation, "
                                "search, screening, deduplication, trust and the knowledge "
                                "graph. The one area with a working vertical slice today."),
    "08_EVIDENCE_ASSURANCE": ("Evidence and assurance", "The claim and evidence ledger, "
                              "extraction, entailment, run registry, clean rooms, review "
                              "orchestration, reproduction and the publication package."),
    "09_EXPERIENCE_OBSERVABILITY": ("Experience and observability", "The cockpit, gate timeline, "
                                    "decision queue, literature workbench, telemetry, cost and "
                                    "audit surfaces."),
    "10_INTEGRATION_CUTOVER": ("Integration and cutover", "Vertical slices, the full-system "
                               "regression, the commissioning dossier and the single production "
                               "cutover."),
    "11_DAY2_OPERATIONS": ("Day-2 operations", "The recurring rhythms after go-live: service "
                           "cadence, control effectiveness, requalification, calibration, "
                           "FinOps, incident learning and drills. **A Day-2 rhythm can never be "
                           "a precondition of the go-live that precedes it.**"),
    "12_ACCEPTANCE_SCENARIOS": ("Acceptance scenarios", "The binding scenarios for production "
                                "commissioning. Roughly half pass by demonstrating that the "
                                "system correctly **refused** to act."),
    "13_TOOLING_INTEGRATION": ("Tooling and external integration", "Notification, escalation, "
                               "decision routing, inbound quarantine, external feeds, "
                               "persistent identifiers, timestamping and liveness."),
}
FIELD = lambda name, text: (re.search(rf"^\| {name} \| (.+?) \|\s*$", text, re.M) or [None, "—"])[1]


def build(directory: Path) -> str:
    name = directory.name
    title, purpose = PURPOSE.get(name, (name, ""))
    packages, scenarios = [], []
    for path in sorted(directory.glob("*.md")):
        if path.name.lower().endswith("index.md") or path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        heading = re.search(r"^# (.+)$", text, re.M)
        heading = heading.group(1) if heading else path.stem
        if path.name.startswith("WP-"):
            packages.append((path.name, heading, FIELD("Hard dependencies", text),
                             FIELD("Current status", text),
                             "## Adopted component" in text))
        elif path.name.startswith("ACC-"):
            scenarios.append((path.name, heading, FIELD("Severity", text),
                              FIELD("Acceptance phase", text)))

    out = [f"# {name} — {title}", "",
           "| Field | Value |", "|---|---|",
           "| Document type | Index — **generated** from the files in this directory |",
           f"| Scope | {title.lower()} |",
           "| Sibling documents | `../README.md` · `../00_PROGRAM/03_package_catalogue.md` |",
           "| Status | Regenerated by `scripts/make_plan_indexes.py`; **never edited by hand** |", "",
           f"**In one paragraph.** {purpose}", ""]

    if packages:
        out += ["---", "", f"## Work packages ({len(packages)})", "",
                "| Package | Title | Hard dependencies | Status | Adopted component |",
                "|---|---|---|---|:--:|"]
        for filename, heading, deps, status, adopted in packages:
            short = heading.split("—", 1)[-1].strip()
            deps = (deps or "—").replace("**", "")
            if len(deps) > 60:
                deps = deps[:57] + "…"
            out.append(f"| [{filename[:6]}]({filename}) | {short} | {deps} | "
                       f"{status.split('—')[0].strip()} | {'✅' if adopted else ''} |")
        out.append("")
        out.append("A ✅ marks a package that stands on an adopted external component rather "
                   "than building the capability here — see "
                   "`docs/architecture/AETHRION_COMPONENT_REUSE.md`.")
        out.append("")

    if scenarios:
        out += ["---", "", f"## Acceptance scenarios ({len(scenarios)})", "",
                "| Scenario | Title | Severity | Phase |", "|---|---|---|---|"]
        for filename, heading, severity, phase in scenarios:
            short = heading.split("—", 1)[-1].strip()
            out.append(f"| [{filename[:6]}]({filename}) | {short} | "
                       f"{severity.replace('**','')} | {phase.replace('`','')} |")
        out += ["", "`PRE_GO_LIVE` scenarios must pass before cutover. `DAY2_CONTINUOUS` "
                "scenarios are armed at cutover and exercised afterwards.", ""]

    out += ["---", "", "## Reading order", "",
            "1. `../README.md` — how the plan is organised and how it is verified",
            "2. `../00_PROGRAM/00_how_to_use_this_plan.md` — the execution rules",
            "3. This index — what lives in this workstream",
            "4. The package or scenario itself", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    drift, written = [], 0
    for directory in sorted(PLAN.iterdir()):
        if not directory.is_dir():
            continue
        text = build(directory)
        target = directory / "README.md"
        if args.check:
            if not target.is_file() or target.read_text() != text:
                drift.append(directory.name)
        else:
            target.write_text(text)
            written += 1

    if args.check:
        for name in drift:
            print(f"  drift: {name}/README.md")
        print(f"{len(list(PLAN.iterdir()))} directories checked, {len(drift)} drift entries")
        return 1 if drift else 0
    print(f"wrote {written} workstream indexes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
