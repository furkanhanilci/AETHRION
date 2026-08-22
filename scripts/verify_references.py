#!/usr/bin/env python3
"""Reference verification — CoE Audit check 1, run against the real registry.

Responsibility
    Resolve every source in the canonical registry against public bibliographic
    authorities and report which entries are corroborated, which are
    unresolvable, and where the local metadata disagrees with the authority.

Why this exists
    A hallucinated or subtly wrong citation is the cheapest way for a claim to
    look supported while resting on nothing. The published CoE Audit benchmark
    found hallucinated-reference rates up to 21% across systems that all
    intended to be correct, so this is not a hypothetical failure mode.

    This check makes G3 stronger than a hand-rolled equivalent would be, because
    the authorities it queries are maintained by the scholarly infrastructure
    rather than by this project: Crossref for DOI-registered work, OpenAlex as a
    fallback for records Crossref does not hold.

Invariant
    The registry is **read-only** here, exactly as it is everywhere else in the
    bridge. Verification observes; it never writes back, never "corrects" a
    title, and never deletes a source it failed to resolve. An unresolved entry
    is a finding for a human, not a licence to mutate the canonical record.

Audit findings
    Implements the first of the four CoE Audit checks adopted in
    `docs/architecture/AETHRION_EXTERNAL_STANDARDS.md` §4.3. The other three —
    score verification, specification violation, method-code alignment — need
    artifacts this system does not yet produce.

Usage
    uv run python scripts/verify_references.py                # verify all
    uv run python scripts/verify_references.py --limit 10     # a sample
    uv run python scripts/verify_references.py --report out.json
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import unicodedata
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "airl_bridge.sqlite3"
UA = "AETHRION reference verification (+https://github.com/furkanhanilci/AETHRION)"
CROSSREF = "https://api.crossref.org/works"
OPENALEX = "https://api.openalex.org/works"
ARXIV = "https://export.arxiv.org/api/query"
TITLE_MATCH = 0.82          # below this, a resolved record is reported as a mismatch


@dataclass
class Result:
    airl_id: str
    title: str
    doi: str | None
    status: str             # RESOLVED · MISMATCH · UNRESOLVED · NO_IDENTIFIER
    authority: str | None
    similarity: float | None
    authority_title: str | None
    note: str = ""


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "").lower()
    return re.sub(r"[^a-z0-9 ]+", " ", text).strip()


def similarity(a: str, b: str) -> float:
    """Token-overlap ratio. Deliberately simple: this decides *reporting*, and a
    borderline case must be seen by a human rather than silently classified."""
    x, y = set(normalise(a).split()), set(normalise(b).split())
    if not x or not y:
        return 0.0
    return len(x & y) / max(len(x), len(y))


def by_doi(client: httpx.Client, doi: str) -> tuple[str, str] | None:
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip())
    try:
        response = client.get(f"{CROSSREF}/{doi}", timeout=20)
        if response.status_code == 200:
            titles = response.json()["message"].get("title") or [""]
            return "crossref", titles[0]
    except (httpx.HTTPError, KeyError, ValueError):
        pass
    try:
        response = client.get(f"{OPENALEX}/doi:{doi}", timeout=20)
        if response.status_code == 200:
            return "openalex", response.json().get("title") or ""
    except (httpx.HTTPError, ValueError):
        pass
    return None


def by_arxiv(client: httpx.Client, title: str) -> tuple[str, str] | None:
    """Preprints without a DOI are invisible to Crossref and often to OpenAlex."""
    try:
        response = client.get(ARXIV, params={"search_query": f'ti:"{title}"',
                                             "max_results": 3}, timeout=25)
        if response.status_code != 200:
            return None
        for candidate in re.findall(r"<entry>.*?<title>(.*?)</title>", response.text, re.S):
            candidate = " ".join(candidate.split())
            if similarity(title, candidate) >= TITLE_MATCH:
                return "arxiv", candidate
    except httpx.HTTPError:
        pass
    return None


def by_title(client: httpx.Client, title: str) -> tuple[str, str] | None:
    try:
        response = client.get(CROSSREF, params={"query.bibliographic": title, "rows": 3}, timeout=25)
        if response.status_code == 200:
            for item in response.json()["message"].get("items", []):
                candidate = (item.get("title") or [""])[0]
                if similarity(title, candidate) >= TITLE_MATCH:
                    return "crossref", candidate
    except (httpx.HTTPError, KeyError, ValueError):
        pass
    try:
        response = client.get(OPENALEX, params={"search": title, "per-page": 3}, timeout=25)
        if response.status_code == 200:
            for item in response.json().get("results", []):
                candidate = item.get("title") or ""
                if similarity(title, candidate) >= TITLE_MATCH:
                    return "openalex", candidate
    except (httpx.HTTPError, ValueError):
        pass
    return by_arxiv(client, title)


def verify_one(client: httpx.Client, row: sqlite3.Row) -> Result:
    title, doi = row["title"] or "", row["doi"]
    base = dict(airl_id=row["airl_id"], title=title, doi=doi)

    found = by_doi(client, doi) if doi else None
    if found is None and title:
        found = by_title(client, title)
    if found is None:
        if not doi and not title:
            return Result(**base, status="NO_IDENTIFIER", authority=None,
                          similarity=None, authority_title=None,
                          note="neither a DOI nor a title to resolve")
        return Result(**base, status="UNRESOLVED", authority=None, similarity=None,
                      authority_title=None,
                      note="no bibliographic authority holds a matching record; "
                           "for a DOI-less item this may mean unindexed rather than fabricated")

    authority, authority_title = found
    score = similarity(title, authority_title) if title else 0.0
    status = "RESOLVED" if score >= TITLE_MATCH else "MISMATCH"
    note = "" if status == "RESOLVED" else "resolved record's title differs from the local one"
    return Result(**base, status=status, authority=authority, similarity=round(score, 3),
                  authority_title=authority_title, note=note)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    if not DB.is_file():
        print(f"registry not found at {DB}", file=sys.stderr)
        return 1

    connection = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    query = "SELECT airl_id, title, doi FROM sources ORDER BY airl_id"
    if args.limit:
        query += f" LIMIT {args.limit}"
    rows = connection.execute(query).fetchall()
    connection.close()

    results: list[Result] = []
    with httpx.Client(headers={"User-Agent": UA}, follow_redirects=True) as client:
        for index, row in enumerate(rows, 1):
            result = verify_one(client, row)
            results.append(result)
            mark = {"RESOLVED": "ok  ", "MISMATCH": "diff", "UNRESOLVED": "MISS",
                    "NO_IDENTIFIER": "----"}[result.status]
            print(f"[{index:>3}/{len(rows)}] {mark} {result.title[:64]}")

    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    total = len(results)
    resolved = counts.get("RESOLVED", 0)

    print("\n" + "-" * 60)
    print(f"sources checked      {total}")
    for status in ("RESOLVED", "MISMATCH", "UNRESOLVED", "NO_IDENTIFIER"):
        if counts.get(status):
            print(f"{status.lower():<20} {counts[status]}")
    print(f"corroboration rate   {resolved / total:.1%}" if total else "no sources")
    print("\nThis measures whether the registry's records exist in public bibliographic")
    print("authorities. It does not measure whether a claim is supported by them.")

    if args.report:
        payload = {
            "check": "coe-audit/reference-verification",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "authorities": ["crossref", "openalex", "arxiv"],
            "title_match_threshold": TITLE_MATCH,
            "totals": counts,
            "corroboration_rate": round(resolved / total, 4) if total else None,
            "results": [asdict(r) for r in results],
        }
        args.report.write_text(json.dumps(payload, indent=2) + "\n")
        print(f"\nreport written to {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
