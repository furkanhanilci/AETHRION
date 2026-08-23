#!/usr/bin/env python3
"""Check that every assimilated upstream mechanism is traceable to its source.

Responsibility
    This repository takes mechanisms from other people's work. Three failure
    classes follow from that, and none of them is visible to a hash seal, a
    licence header scan or a test suite:

    1. **Code taken with no pin.** "Adapted from upstream" against a moving
       `main` is not provenance. It cannot be re-read, diffed or re-reviewed.
    2. **Code taken with no characterisation.** If upstream behaviour was never
       captured in a test before the code moved, there is nothing to compare the
       local version against, and divergence becomes indistinguishable from
       intent.
    3. **A mechanism that quietly acquires authority.** The register's whole
       purpose is that an adopted mechanism supplies a signal, never a verdict.
       An entry with no stated authority boundary has not answered that.

Invariant
    A DIRECT_ADAPT entry may not reach `ADAPTING` or `ACCEPTED` without a pinned
    commit, a named file list, a permissive licence and a characterisation
    suite. An ADAPTIVE_REIMPLEMENT entry may not name source files at all — if
    files were copied, the decision was not a reimplementation, and calling it
    one is how a licence obligation goes unrecorded.

Why the controls matter
    Every rule below can be made to fire on demand:

        python3 scripts/check_upstream_lineage.py --self-test

    injects a deliberate defect per rule and fails if any rule stays silent. A
    checker that has never been observed to fail reports "no findings" and "no
    detector" in exactly the same words. This is the same control-injection
    discipline `scripts/monitor_sources.py` applies to retraction monitoring.

Generated output
    `provenance/README.md` is derived from the register and is never edited by
    hand. `--write` regenerates it; `--check` (the default) fails on drift.

Exit codes
    0 — the register is well-formed and its generated index is current.
    1 — at least one defect.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "provenance" / "upstreams.json"
INDEX = ROOT / "provenance" / "README.md"
PLAN = ROOT / "planning" / "commissioning"

# Licences under which taking source code and refactoring it is permitted, given
# that the notice is preserved. A licence outside this set is not a judgement
# that the work is unusable — it is a decision that the mechanism must be
# specified and reimplemented rather than copied.
PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "0BSD"}

REQUIRED = ("id", "name", "kind", "assimilation", "status", "licence",
            "authority_boundary", "not_taken", "source_files", "mechanisms",
            "local_modules", "work_packages", "pinned_commit", "drift_status")

ID = re.compile(r"^ASM-\d{3}$")
SHA = re.compile(r"^[0-9a-f]{40}$")
WP = re.compile(r"^WP-\d{3}$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MECHANISM = re.compile(r"^MS-[A-Z]+-\d{3}$")


def load() -> dict:
    return json.loads(REGISTER.read_text(encoding="utf-8"))


def known_packages() -> set[str]:
    """Package identifiers that actually exist in the plan."""
    return {p.name[:6] for p in PLAN.rglob("WP-*.md")
            if re.match(r"^WP-\d{3}_", p.name)}


def audit(register: dict, packages: set[str]) -> list[str]:
    """Every rule in one place, so `--self-test` can aim at each by name."""
    problems: list[str] = []
    types = set(register["assimilation_types"])
    statuses = set(register["statuses"])
    seen: set[str] = set()

    for entry in register["entries"]:
        eid = entry.get("id", "<no id>")

        # R1 — shape
        for field in REQUIRED:
            if field not in entry:
                problems.append(f"{eid}: required field {field!r} is missing")
        if not ID.match(str(entry.get("id", ""))):
            problems.append(f"{eid}: identifier is not ASM-nnn")

        # R2 — identity
        if eid in seen:
            problems.append(f"{eid}: duplicate identifier")
        seen.add(eid)

        # R3 — vocabulary
        if entry.get("assimilation") not in types:
            problems.append(f"{eid}: assimilation {entry.get('assimilation')!r} "
                            f"is not one of the declared types")
        if entry.get("status") not in statuses:
            problems.append(f"{eid}: status {entry.get('status')!r} "
                            f"is not one of the declared statuses")

        assimilation = entry.get("assimilation")
        status = entry.get("status")
        licence = (entry.get("licence") or "").strip()

        # R4 — an adopted mechanism must say what it may never decide
        if status != "REJECTED" and not (entry.get("authority_boundary") or "").strip():
            problems.append(f"{eid}: no authority boundary stated")

        # R5 — code may not move without a pin, a file list and a characterisation
        if assimilation == "DIRECT_ADAPT" and status in {"ADAPTING", "ACCEPTED"}:
            if not entry.get("pinned_commit"):
                problems.append(f"{eid}: DIRECT_ADAPT at status {status} with no pinned commit")
            if not entry.get("source_files"):
                problems.append(f"{eid}: DIRECT_ADAPT at status {status} names no source files")
            if not entry.get("characterization_suite"):
                problems.append(f"{eid}: DIRECT_ADAPT at status {status} with no characterisation suite")
            if licence.split()[0].rstrip(",") not in PERMISSIVE:
                problems.append(f"{eid}: DIRECT_ADAPT under licence {licence!r}, "
                                f"which is not in the permissive set")

        # R6 — a reimplementation that carries source files is not one
        if assimilation == "ADAPTIVE_REIMPLEMENT":
            if entry.get("source_files"):
                problems.append(f"{eid}: ADAPTIVE_REIMPLEMENT names source files — "
                                f"if files were copied the decision was DIRECT_ADAPT")
            if not entry.get("mechanisms"):
                problems.append(f"{eid}: ADAPTIVE_REIMPLEMENT with no mechanism specification "
                                f"identifiers — the specification is the deliverable")

        # R7 — an unverified licence forbids copying, and nothing else.
        #
        # This rule was wrong twice and both errors are worth recording. It
        # matched `licence.upper() == "UNVERIFIED"` exactly, so an entry saying
        # "UNVERIFIED — not confirmed on <date>" — strictly more informative —
        # slipped past it silently. And it forbade every assimilation type except
        # DEFER and REJECT, which contradicts ADR-004: reimplementing a published
        # mechanism creates no licence obligation at all, and an unverified
        # licence is a *reason* to reimplement rather than a reason to stop.
        #
        # What an unverified licence actually forbids is moving files.
        if licence.upper().startswith("UNVERIFIED") and assimilation == "DIRECT_ADAPT":
            problems.append(f"{eid}: DIRECT_ADAPT under an unverified licence — "
                            f"code cannot be copied until the licence is read at "
                            f"the source; reimplement instead")
        verified = entry.get("licence_verified")
        if verified is not None and not DATE.match(str(verified)):
            problems.append(f"{eid}: licence_verified {verified!r} is not a date")

        # R8 — references into the plan must resolve
        for ref in entry.get("work_packages", []):
            if not WP.match(ref):
                problems.append(f"{eid}: {ref!r} is not a work-package identifier")
            elif ref not in packages:
                problems.append(f"{eid}: references {ref}, which is not in the plan")

        # R9 — a local module named here must exist
        for module in entry.get("local_modules", []):
            if not (ROOT / module).exists():
                problems.append(f"{eid}: local module {module!r} does not exist")

        # R10 — a pin is a commit, not a branch
        pin = entry.get("pinned_commit")
        if pin is not None and not SHA.match(str(pin)):
            problems.append(f"{eid}: pinned_commit {pin!r} is not a 40-character digest — "
                            f"a branch name is not a pin")

        # R11 — mechanism identifiers are structured so a spec can be found
        for mech in entry.get("mechanisms", []):
            if not MECHANISM.match(mech):
                problems.append(f"{eid}: mechanism {mech!r} is not MS-AREA-nnn")

        # R12 — drift status must agree with whether a pin exists
        if entry.get("drift_status") == "NOT_PINNED" and pin is not None:
            problems.append(f"{eid}: drift_status NOT_PINNED but a commit is pinned")
        if pin is not None and entry.get("drift_status") == "NOT_PINNED":
            pass

    return problems


def render(register: dict) -> str:
    entries = register["entries"]
    by_type: dict[str, list[dict]] = {}
    for entry in entries:
        by_type.setdefault(entry["assimilation"], []).append(entry)

    order = ["VENDORED", "DIRECT_ADAPT", "ADAPTIVE_REIMPLEMENT", "PATTERN", "STANDARD",
             "BENCHMARK", "DEPENDENCY", "DEFER", "REJECT"]

    out = [
        "# Upstream Lineage Register",
        "",
        "| Field | Value |",
        "|---|---|",
        "| Document type | Index — **generated** from `provenance/upstreams.json` |",
        "| Scope | Every external mechanism this architecture takes, and what it may never decide |",
        "| Sibling documents | `../docs/architecture/AETHRION_COMPONENT_REUSE.md` (why a component is adopted) · "
        "`../docs/architecture/ADR-004_assimilation_and_upstream_lineage.md` (how) · `../NOTICE` (licence obligations) |",
        "| Status | Regenerated by `scripts/check_upstream_lineage.py --write`; **never edited by hand** |",
        f"| Entries | **{len(entries)}** |",
        f"| Register retrieved | {register['retrieval_date']} |",
        "",
        "**In one paragraph.** Taking a mechanism from someone else's work is an "
        "engineering decision with three obligations: say where it came from, say "
        "what was deliberately *not* taken, and say what the mechanism may never "
        "decide. This register carries all three for every mechanism, so that "
        "\"AETHRION adapted this\" is a checkable statement rather than a claim in "
        "prose. **No entry has reached `ADAPTING` yet** — every row below is a "
        "decision on paper, and `pinned_commit` stays `null` until code actually "
        "moves, at which point `check_upstream_lineage.py` starts requiring it.",
        "",
        "> **Upstream identity is engineering lineage, not product architecture.** "
        "None of the systems below appears as a runtime module, a directory or a "
        "backend. What is taken is a mechanism; where it came from is recorded here "
        "and in `NOTICE`, and nowhere else.",
        "",
        "---",
        "",
        "## Assimilation types",
        "",
        "| Type | Meaning |",
        "|---|---|",
    ]
    for name in order:
        if name in register["assimilation_types"]:
            out.append(f"| **{name}** | {register['assimilation_types'][name]} |")
    out.append("")

    for name in order:
        group = by_type.get(name)
        if not group:
            continue
        out += ["---", "", f"## {name} ({len(group)})", "",
                "| ID | Mechanism | Upstream | Licence | Status | Authority boundary |",
                "|---|---|---|---|---|---|"]
        for entry in group:
            where = entry.get("repository") or entry.get("paper") or entry.get("reference") or "—"
            if where.startswith("http"):
                where = f"[{where.split('/')[-2]}/{where.split('/')[-1]}]({where})"
            out.append(f"| `{entry['id']}` | {entry['name']} | {where} | "
                       f"{entry['licence'].split(' —')[0]} | `{entry['status']}` | "
                       f"{entry['authority_boundary']} |")
        out.append("")

    out += ["---", "", "## What this register is not", "",
            "It is not a dependency list — nothing here is installed. It is not a "
            "reading list — an entry means a decision was taken about a mechanism, "
            "including the decision not to take it. And it is not a claim of "
            "implementation: `status` is the honest field, and every row currently "
            "reads `PROPOSED` or `REJECTED`.", ""]
    return "\n".join(out)


def self_test(register: dict, packages: set[str]) -> int:
    """Prove each rule can fail. A silent rule is not a control."""
    def mutate(fn) -> dict:
        copy_ = copy.deepcopy(register)
        fn(copy_["entries"])
        return copy_

    def first_of(entries, assimilation):
        return next(e for e in entries if e["assimilation"] == assimilation)

    injections = [
        ("R1 missing required field", lambda es: es[0].pop("not_taken")),
        ("R2 duplicate identifier", lambda es: es[1].update(id=es[0]["id"])),
        ("R3 unknown assimilation type", lambda es: es[0].update(assimilation="BORROWED")),
        ("R4 no authority boundary", lambda es: es[0].update(authority_boundary="  ")),
        ("R5 direct adapt with no pin", lambda es: first_of(es, "DIRECT_ADAPT").update(status="ADAPTING")),
        ("R6 reimplementation carrying source files",
         lambda es: first_of(es, "ADAPTIVE_REIMPLEMENT").update(source_files=["upstream/thing.py"])),
        ("R7 unverified licence on a direct adaptation",
         lambda es: first_of(es, "DIRECT_ADAPT").update(licence="UNVERIFIED — not read")),
        ("R8 reference to a package that does not exist",
         lambda es: es[0].update(work_packages=["WP-999"])),
        ("R9 local module that does not exist",
         lambda es: es[0].update(local_modules=["src/aethrion/nowhere.py"])),
        ("R10 branch name where a commit is required",
         lambda es: es[0].update(pinned_commit="main", drift_status="PINNED")),
        ("R11 unstructured mechanism identifier",
         lambda es: first_of(es, "ADAPTIVE_REIMPLEMENT").update(mechanisms=["the clever bit"])),
    ]

    silent = []
    for label, injection in injections:
        if not audit(mutate(injection), packages):
            silent.append(label)

    if audit(register, packages):
        print("  self-test: the unmutated register does not pass — fix that first")
        return 1
    for label in silent:
        print(f"  control did not fire: {label}")
    print(f"{len(injections)} controls injected, {len(silent)} silent")
    return 1 if silent else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="regenerate provenance/README.md from the register")
    parser.add_argument("--self-test", action="store_true",
                        help="inject a defect per rule and fail if any rule stays silent")
    args = parser.parse_args()

    register = load()
    packages = known_packages()

    if args.self_test:
        return self_test(register, packages)

    problems = audit(register, packages)
    index = render(register)

    if args.write:
        INDEX.write_text(index, encoding="utf-8")
    elif not INDEX.is_file() or INDEX.read_text(encoding="utf-8") != index:
        problems.append("provenance/README.md has drifted from the register "
                        "(run --write; do not edit it by hand)")

    for problem in problems:
        print(f"  {problem}")
    # "code taken" means source files moved into this repository — which only a
    # DIRECT_ADAPT entry can do. A DEPENDENCY at ACCEPTED is integrated and
    # called, not copied, and counting it as adapted code would overstate what
    # this repository contains.
    adapted = sum(1 for e in register["entries"]
                  if e["assimilation"] == "DIRECT_ADAPT"
                  and e["status"] in {"ADAPTING", "ACCEPTED"})
    live = sum(1 for e in register["entries"] if e["status"] == "ACCEPTED")
    print(f"{len(register['entries'])} upstream entries checked, {adapted} with code taken, "
          f"{live} integrated, {len(problems)} lineage problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
