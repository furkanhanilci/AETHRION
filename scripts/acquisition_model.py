#!/usr/bin/env python3
"""The acquisition model: which package takes what, from where, on what terms.

Responsibility
    Two registers answer two different questions, and neither of them is read by
    the person who has to act on it.

    `provenance/upstreams.json` records **mechanisms assimilated** into this
    repository's own code — ADR-004's subject. `provenance/components.json`
    records **components adopted at runtime** — what
    `AETHRION_COMPONENT_REUSE.md` decided. A DEPENDENCY is installed and called,
    and the work happens inside it; an assimilated mechanism runs as this
    system's own code and leaves no runtime trace of where it came from. The two
    obligations are different, which is why the registers are separate.

    This module joins both to the work package that has to execute the decision,
    and turns each entry into the only thing an implementer actually needs: a
    **mode**, what is taken, what AETHRION still owns, what the source may never
    decide, and **what is not yet resolved**.

Why an unresolved obligation is the load-bearing output
    Every entry in both registers is `PROPOSED`. No commit is pinned, no
    characterisation suite exists, and no `MS-*` mechanism specification has been
    written anywhere in this repository. A block that printed only "AIDE,
    DIRECT_ADAPT" would read as an instruction to go and copy a file, which is
    precisely what ADR-004 forbids until the pin, the file list and the
    characterisation exist.

    So the model computes obligations per mode and reports the ones that are
    still open. `BUILD_NATIVE` is emitted explicitly rather than by silence,
    because an implementer cannot otherwise tell a package with no upstream from
    a package whose upstream nobody recorded.

Invariant
    This module derives; it never decides. Every mode, boundary and exclusion it
    reports is transcribed from a register entry, and a register entry is
    transcribed from a decision already written in an ADR or an architecture
    document.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAMS = ROOT / "provenance" / "upstreams.json"
COMPONENTS = ROOT / "provenance" / "components.json"
PLAN = ROOT / "planning" / "commissioning"

# The mode an implementer acts on. `BUILD_NATIVE` is this repository's own and
# appears in neither register, because a register records what came from
# somewhere else and this one records that nothing did.
MODES = (
    "DEPENDENCY", "ADAPTER", "OPTIONAL_BACKEND", "STANDARD", "BENCHMARK",
    "PATTERN", "VENDORED", "DIRECT_ADAPT", "ADAPTIVE_REIMPLEMENT", "DEFER",
    "REJECT", "BUILD_NATIVE",
)

# What each mode requires before an implementer may write code under it, and the
# register field that answers it. The field names are identical in both
# registers on purpose: one obligation vocabulary, two subject matters.
OBLIGATIONS: dict[str, tuple[tuple[str, str], ...]] = {
    "DIRECT_ADAPT": (
        # The sequence is PROPOSED → pin → select files → characterise →
        # CHARACTERIZED → the package may be READY → ADAPTING. `CHARACTERIZED`
        # is a separate obligation from the three fields below it because the
        # fields can be filled without anyone having decided the adaptation is
        # still the right call once the pinned tree has actually been read —
        # which is exactly what ASM-007's own note says has to happen first.
        ("characterized", "the register entry moved to `CHARACTERIZED` — upstream "
                          "behaviour captured and the adaptation confirmed against "
                          "the pinned tree, not against the paper"),
        ("pinned_commit", "a pinned upstream commit — a branch name is not a pin"),
        ("source_files", "the exact list of files that will move"),
        ("characterization_suite", "a characterisation suite capturing upstream "
                                   "behaviour **before** any code moves"),
        ("licence_read", "a permissive licence read at the source"),
    ),
    "ADAPTIVE_REIMPLEMENT": (
        ("mechanisms", "mechanism identifiers naming what is being reimplemented"),
        ("mechanism_spec", "a written mechanism specification — inputs, outputs, "
                           "state, transitions, invariants, failure conditions "
                           "and forbidden behaviour — before implementation"),
    ),
    "DEPENDENCY": (
        ("version_policy", "a version or image-digest policy and an upgrade path"),
        ("failure_semantics", "what happens when it is unavailable, slow or wrong"),
    ),
    "ADAPTER": (
        ("version_policy", "a version or image-digest policy and an upgrade path"),
        ("failure_semantics", "what happens when it is unavailable, slow or wrong"),
    ),
    "OPTIONAL_BACKEND": (
        ("selection", "the qualification or bake-off that decides which backend, "
                      "recorded rather than chosen implicitly"),
        ("backend_chosen", "the backend itself — still unchosen, which is the "
                           "correct state until the qualification runs, and a "
                           "stop condition for anyone about to pick one"),
    ),
    "STANDARD": (
        ("conformance", "a conformance suite against the published specification"),
    ),
    "BENCHMARK": (),
    "PATTERN": (),
    # Verbatim inclusion moves a licence without refactoring anything, so the
    # obligations are provenance rather than behaviour: the tree must be
    # attributable, pinned and demonstrably unmodified.
    "VENDORED": (
        ("licence_read", "a licence read at the source and reproduced in full"),
        ("pinned_commit", "a pinned upstream commit — a branch name is not a pin"),
        ("source_files", "the exact list of vendored paths"),
    ),
    "DEFER": (),
    "REJECT": (),
    "BUILD_NATIVE": (),
}

PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "0BSD"}


def cell(text: str, limit: int = 320) -> str:
    """One markdown table cell: no pipes, no newlines, short enough to read.

    A register field is prose written to be read on its own. Dropped into a
    table it can carry a pipe, which silently splits the row, or run to three
    hundred words, which makes the table unreadable and the block ignored.
    """
    flat = re.sub(r"\s+", " ", (text or "").replace("|", "∣")).strip()
    if len(flat) > limit:
        flat = flat[:limit].rsplit(" ", 1)[0] + " …"
    return flat or "—"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def packages() -> dict[str, Path]:
    """Every package card in the plan, by identifier."""
    out = {}
    for path in sorted(PLAN.rglob("WP-*.md")):
        if not re.match(r"^WP-\d{3}_", path.name):
            continue
        if path.name.endswith((".tests.md", ".acceptance.md")):
            continue
        out[path.name[:6]] = path
    return out


def _unresolved(entry: dict, mode: str) -> list[str]:
    """The obligations this entry has not yet met, in the words of the rule."""
    open_items = []
    for field, description in OBLIGATIONS.get(mode, ()):
        if field == "characterized":
            if entry.get("status") not in {"CHARACTERIZED", "ADAPTING", "ACCEPTED"}:
                open_items.append(description)
            continue
        if field == "backend_chosen":
            # An optional backend that is still `PROPOSED` has a recorded way of
            # deciding and no decision. Both facts matter: the first stops the
            # question being reopened, the second stops an implementer picking
            # a backend because it was the one named first in a table.
            if entry.get("status") == "PROPOSED":
                open_items.append(description)
            continue
        if field == "licence_read":
            licence = (entry.get("licence") or "").strip()
            head = licence.split()[0].rstrip(",") if licence else ""
            if licence.upper().startswith("UNVERIFIED") or head not in PERMISSIVE:
                open_items.append(description)
            continue
        value = entry.get(field)
        if value in (None, "", [], {}):
            open_items.append(description)
    return open_items


def _taken(entry: dict, mode: str) -> str:
    """What actually crosses over, in the register's own terms."""
    if mode in {"DIRECT_ADAPT", "VENDORED"}:
        files = entry.get("source_files") or []
        if files:
            return " · ".join(f"`{f}`" for f in files)
        return "named source files — **not yet selected**"
    if mode == "ADAPTIVE_REIMPLEMENT":
        mechs = entry.get("mechanisms") or []
        return " · ".join(f"`{m}`" for m in mechs) if mechs else "mechanisms not yet identified"
    if mode == "BENCHMARK":
        return "a measurement of this system — nothing enters it"
    if mode == "PATTERN":
        # A pattern moves an idea. Falling through to the runtime-component
        # wording below made these rows read "the running implementation",
        # which is the one thing a pattern explicitly does not take.
        return "the idea only — no code and nothing called at runtime"
    if mode == "VENDORED":
        files = entry.get("source_files") or []
        return (f"{len(files)} paths, verbatim and never edited here"
                if files else "verbatim source — **paths not yet listed**")
    if mode in {"DEFER", "REJECT"}:
        return "nothing — recorded so it is not re-examined from scratch"
    owned = entry.get("not_owned")
    return owned or "the running implementation"


def _owned(entry: dict, mode: str) -> str:
    """What stays AETHRION's when the source is taken, replaced or dropped."""
    if entry.get("owned_contract"):
        return entry["owned_contract"]
    if mode in {"PATTERN", "DEFER", "REJECT"}:
        return "everything — the implementation here is this repository's own"
    if mode in {"DIRECT_ADAPT", "ADAPTIVE_REIMPLEMENT"}:
        modules = entry.get("local_modules") or []
        if modules:
            return " · ".join(f"`{m}`" for m in modules)
        return ("the local module and contract surface this becomes — "
                "**named at refinement**")
    return "the contract this is held behind"


def rows_for(package: str) -> list[dict]:
    """Every acquisition decision bound to one package, register order preserved."""
    rows = []
    for entry in _load(UPSTREAMS)["entries"]:
        if package in entry.get("work_packages", []):
            mode = entry["assimilation"]
            rows.append({
                "id": entry["id"], "name": entry["name"], "mode": mode,
                "register": "provenance/upstreams.json", "status": entry["status"],
                "taken": _taken(entry, mode), "owned": _owned(entry, mode),
                "boundary": entry.get("authority_boundary") or "",
                "not_taken": entry.get("not_taken") or "",
                "unresolved": _unresolved(entry, mode),
                "licence": entry.get("licence"),
                "notes": entry.get("notes"),
            })
    for entry in _load(COMPONENTS)["entries"]:
        if package in entry.get("work_packages", []):
            mode = entry["adoption"]
            rows.append({
                "id": entry["id"], "name": entry["name"], "mode": mode,
                "register": "provenance/components.json", "status": entry["status"],
                "taken": _taken(entry, mode), "owned": _owned(entry, mode),
                "boundary": entry.get("authority_boundary") or "",
                "not_taken": entry.get("not_used") or "",
                "unresolved": _unresolved(entry, mode),
                "licence": None,
                "notes": entry.get("notes"),
            })
    return rows


def registered_names(with_mode: bool = False) -> list[tuple]:
    """(identifier, name, bound packages[, mode]) for every entry in both registers.

    Used to join a decision to the package that has to execute it, and to see
    which decisions reach nobody.
    """
    out = []
    for entry in _load(UPSTREAMS)["entries"]:
        row = (entry["id"], entry["name"], set(entry.get("work_packages", [])))
        out.append(row + (entry["assimilation"],) if with_mode else row)
    for entry in _load(COMPONENTS)["entries"]:
        row = (entry["id"], entry["name"], set(entry.get("work_packages", [])))
        out.append(row + (entry["adoption"],) if with_mode else row)
    return out


def unresolved_packages() -> dict[str, list[str]]:
    """Packages that cannot be `READY`, and the obligation that stops each."""
    out = {}
    for pid in packages():
        blockers = []
        for row in rows_for(pid):
            for item in row["unresolved"]:
                blockers.append(f"{row['id']} ({row['mode']}): {item}")
        if blockers:
            out[pid] = blockers
    return out
