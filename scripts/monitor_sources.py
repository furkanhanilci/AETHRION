#!/usr/bin/env python3
"""G10 monitoring, first slice — has the evidence base changed under us?

Responsibility
    Ask a public bibliographic authority whether any source in the canonical
    registry has since been retracted, corrected, or made the subject of an
    expression of concern, and report what depends on it.

Why this is the first slice of G10
    The lifecycle's closing claim is that `VERIFIED` is not a permanent state: a
    published claim must be revisable when its evidence base moves. Crossref now
    carries Retraction Watch data in its production API and exposes it as
    `update-to` / `updated-by` relations, so the smallest honest version of G10
    is a DOI sweep — no new infrastructure required.

Invariant
    **A clean report proves nothing unless the check can fire.** Every run
    includes a positive control: a DOI known to be retracted. If the control
    does not raise a signal, the run fails, because a monitor that cannot detect
    a retraction is indistinguishable from one that reports none.

    This is the metascience plane's control-injection principle applied to the
    smallest possible check, and it is the reason this script exits non-zero on
    a silent control.

    The registry is opened read-only. Monitoring observes and reports; deciding
    what a signal means is a human judgement at G10.

Audit findings
    Addresses the monitoring half of finding **H2**-adjacent concerns and gives
    G10 a working component. It does **not** implement claim impact analysis:
    nothing here maps a retracted source to dependent claims, because the Claim
    Ledger does not exist yet. That gap is stated in the report rather than
    papered over.

Usage
    uv run python scripts/monitor_sources.py
    uv run python scripts/monitor_sources.py --report delivery/measurements/monitoring.json
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "airl_bridge.sqlite3"
CROSSREF = "https://api.crossref.org/works"
UA = "AETHRION source monitoring (+https://github.com/furkanhanilci/AETHRION)"

# A retracted paper used as a positive control. If the check cannot see this,
# it cannot see anything, and a clean report would be meaningless.
POSITIVE_CONTROL = "10.1016/S0140-6736(20)31180-6"
MATERIAL = {"retraction", "expression_of_concern", "withdrawal", "removal"}


@dataclass
class Signal:
    airl_id: str
    doi: str
    title: str
    relation: str          # update-to | updated-by
    signal_type: str
    counterpart_doi: str
    materiality: str       # MATERIAL | INFORMATIONAL


def normalise_doi(doi: str) -> str:
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", (doi or "").strip()).lower()


def collect(client: httpx.Client, doi: str) -> list[tuple[str, str, str]]:
    """Return (relation, type, counterpart doi) for every update relation."""
    try:
        response = client.get(f"{CROSSREF}/{normalise_doi(doi)}", timeout=25)
        if response.status_code != 200:
            return []
        message = response.json()["message"]
    except (httpx.HTTPError, KeyError, ValueError):
        return []
    found = []
    for relation in ("update-to", "updated-by"):
        for entry in message.get(relation, []) or []:
            found.append((relation, (entry.get("type") or "unknown").lower(),
                          entry.get("DOI", "")))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    if not DB.is_file():
        print(f"registry not found at {DB}", file=sys.stderr)
        return 1

    connection = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        "SELECT airl_id, title, doi FROM sources WHERE doi IS NOT NULL AND doi != ''"
        " ORDER BY airl_id").fetchall()
    total = connection.execute("SELECT COUNT(*) FROM sources").fetchone()[0]
    connection.close()

    signals: list[Signal] = []
    with httpx.Client(headers={"User-Agent": UA}, follow_redirects=True) as client:
        print(f"sweeping {len(rows)} of {total} sources that carry a DOI\n")
        for index, row in enumerate(rows, 1):
            for relation, signal_type, counterpart in collect(client, row["doi"]):
                materiality = "MATERIAL" if signal_type in MATERIAL else "INFORMATIONAL"
                signals.append(Signal(row["airl_id"], row["doi"], row["title"] or "",
                                      relation, signal_type, counterpart, materiality))
            mark = "!" if any(s.airl_id == row["airl_id"] for s in signals) else "."
            print(f"[{index:>3}/{len(rows)}] {mark} {(row['title'] or '')[:64]}")

        # -- positive control ------------------------------------------------
        control = collect(client, POSITIVE_CONTROL)
        control_fired = any(t in MATERIAL for _, t, _ in control)

    material = [s for s in signals if s.materiality == "MATERIAL"]
    print("\n" + "-" * 60)
    print(f"sources swept        {len(rows)} (of {total}; {total - len(rows)} carry no DOI)")
    print(f"material signals     {len(material)}")
    print(f"informational        {len(signals) - len(material)}")
    print(f"positive control     {'FIRED — the check can detect a retraction' if control_fired else 'SILENT'}")

    for signal in material:
        print(f"  ! {signal.signal_type} on {signal.doi} — {signal.title[:50]}")

    print("\nA source that carries no DOI is invisible to this sweep, and a clean")
    print("report over a DOI-less registry would be a false reassurance.")
    print("Claim impact analysis is NOT implemented: nothing here maps a retracted")
    print("source to the claims that depend on it, because no Claim Ledger exists.")

    if args.report:
        args.report.write_text(json.dumps({
            "check": "g10/source-monitoring",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "authority": "crossref",
            "sources_total": total,
            "sources_with_doi": len(rows),
            "sources_without_doi": total - len(rows),
            "material_signals": len(material),
            "informational_signals": len(signals) - len(material),
            "positive_control": {"doi": POSITIVE_CONTROL, "fired": control_fired},
            "claim_impact_analysis": "not implemented — no Claim Ledger exists",
            "signals": [asdict(s) for s in signals],
        }, indent=2) + "\n")
        print(f"\nreport written to {args.report}")

    if not control_fired:
        print("\nFAIL: the positive control did not fire, so a clean report means nothing.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
