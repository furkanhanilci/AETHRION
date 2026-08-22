#!/usr/bin/env python3
"""Move a work package through its states, and refuse the moves the plan forbids.

Why a script and not an edited file
    ``delivery/progress.json`` could be hand-edited. It should not be. The plan's
    invariants — issuance is not acceptance, a producer may not verify its own
    work, R3 is blocked under ADR-001 — are only invariants if something enforces
    them at the moment of the transition. A JSON file enforces nothing.

What it refuses, and on whose authority
    * Starting a package whose hard dependencies are not ``ACCEPTED``
      — ``00_PROGRAM/05_definition_of_ready_and_done.md``.
    * ``TECH_COMPLETE`` without a signed evidence manifest that verifies
      — ``WP-000_interim_evidence_policy.md``.
    * ``ACCEPTED`` without an independent verifier who is not the accountable
      owner — the role separation in ``AETHRION_ROLES.md`` §5.
    * ``ACCEPTED`` at assurance class R3 — ``ADR-001`` blocks it by design,
      rather than waiving it.

    A refusal prints the document that says so. It is not advice.

Usage
    python3 scripts/progress.py show WP-001
    python3 scripts/progress.py start WP-001
    python3 scripts/progress.py tech-complete WP-001
    python3 scripts/progress.py accept WP-001 --verifier "NAME" --assurance R1
    python3 scripts/progress.py block WP-001 --reason "..."
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# The ledger path is overridable so a test suite never mutates production
# state. It did: `tests/test_progress_cli.py` ran `start WP-011` against the
# real file, and a run that did not reach its restore left WP-011
# `IN_PROGRESS` permanently — after which the test failed on every run and
# the repository's own ready queue was wrong.
LEDGER = Path(os.environ.get("AIRL_PROGRESS_LEDGER",
                             ROOT / "delivery" / "progress.json"))
PLAN = ROOT / "planning" / "commissioning"
RELEASES = {"ACCEPTED", "INTEGRATED"}


def refuse(message: str, authority: str) -> int:
    print(f"refused: {message}", file=sys.stderr)
    print(f"  authority: {authority}", file=sys.stderr)
    return 2


def plan_entry(pid: str) -> dict:
    for path in sorted(PLAN.rglob(f"{pid}_*.md")):
        # The card only. A package is three documents and the companions carry
        # no header table, so matching one of them returned an empty dependency
        # list and `start` stopped refusing what the plan forbids.
        if path.name.endswith((".tests.md", ".acceptance.md")):
            continue
        text = path.read_text(encoding="utf-8")

        def field(name: str) -> str:
            m = re.search(rf"^\|\s*{name}\s*\|(.+?)\|\s*$", text, re.M)
            return m.group(1).strip() if m else ""

        return {
            "path": path,
            "owner": field("Accountable owner"),
            "verifier": field("Independent verifier"),
            "deps": sorted({f"WP-{d}" for d in re.findall(r"WP-(\d{3})",
                                                          field("Hard dependencies"))} - {pid}),
        }
    raise SystemExit(f"no such work package in the plan: {pid}")


def load() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def save(ledger: dict) -> None:
    LEDGER.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "ready_queue.py")],
                   cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("show", "start", "tech-complete", "block"):
        p = sub.add_parser(name)
        p.add_argument("package")
        if name == "block":
            p.add_argument("--reason", required=True)
    p = sub.add_parser("accept")
    p.add_argument("package")
    p.add_argument("--verifier", required=True)
    p.add_argument("--assurance", required=True, choices=["R1", "R2", "R3"])
    args = parser.parse_args()

    pid = args.package.upper()
    ledger = load()
    packages = ledger["packages"]
    if pid not in packages:
        raise SystemExit(f"no such work package in the ledger: {pid}")
    entry = packages[pid]
    state = entry["state"]
    plan = plan_entry(pid)

    if args.command == "show":
        print(f"{pid}  {state}")
        print(f"  owner     {plan['owner']}")
        print(f"  verifier  {plan['verifier']}")
        print(f"  depends   {', '.join(plan['deps']) or '—'}")
        for dep in plan["deps"]:
            print(f"    {dep}  {packages.get(dep, {}).get('state', '?')}")
        if entry.get("note"):
            print(f"  note      {entry['note']}")
        return 0

    if args.command == "start":
        if state != "NOT_STARTED":
            return refuse(f"{pid} is {state}, not NOT_STARTED", "the ledger")
        unmet = [d for d in plan["deps"] if packages.get(d, {}).get("state") not in RELEASES]
        if unmet:
            return refuse(
                f"{pid} depends on {', '.join(unmet)}, none of which is ACCEPTED",
                "00_PROGRAM/05_definition_of_ready_and_done.md — Definition of Ready")
        entry["state"] = "IN_PROGRESS"

    elif args.command == "tech-complete":
        if state != "IN_PROGRESS":
            return refuse(f"{pid} is {state}, not IN_PROGRESS", "the ledger")
        manifest = ROOT / "delivery" / pid / "evidence.dsse.json"
        if not manifest.exists():
            return refuse(
                f"no evidence manifest at delivery/{pid}/evidence.dsse.json",
                "WP-000 — nothing is complete without fresh verification evidence")
        check = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "evidence_manifest.py"),
             "verify", "--manifest", str(manifest)],
            cwd=ROOT, capture_output=True, text=True)
        if check.returncode != 0 or "FAIL" in check.stdout:
            return refuse(f"the manifest for {pid} does not verify",
                          "WP-000 — an unverifiable manifest is not evidence")
        entry["state"] = "TECH_COMPLETE"

    elif args.command == "accept":
        if state != "TECH_COMPLETE":
            return refuse(f"{pid} is {state}; acceptance follows TECH_COMPLETE",
                          "the invariant that issuance is not acceptance")
        if args.assurance == "R3":
            return refuse(
                "R3 work cannot be accepted by this organisation",
                "ADR-001 §6 — R3 is BLOCKED by design, declared rather than waived")
        if args.verifier.strip().lower() == plan["owner"].strip().lower():
            return refuse(
                f"the verifier is the accountable owner ({plan['owner']})",
                "AETHRION_ROLES.md §5 — a producer may not verify its own work")
        entry["state"] = "ACCEPTED"
        entry["verifier"] = args.verifier
        entry["assurance"] = args.assurance
        if args.assurance == "R2":
            entry["note"] = ("accepted under a DECLARED PARTIAL independence profile — "
                             "ADR-001 §6; this limitation travels with the claim")

    elif args.command == "block":
        entry["state"] = "BLOCKED"
        entry["note"] = args.reason

    save(ledger)
    print(f"{pid}: {state} -> {entry['state']}")
    if entry.get("note"):
        print(f"  {entry['note']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
