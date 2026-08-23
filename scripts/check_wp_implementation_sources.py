#!/usr/bin/env python3
"""Check that every acquisition decision is bound to the package that executes it.

Responsibility
    `check_upstream_lineage.py` asks whether a register entry is well-formed.
    This asks the question that follows it and that nothing asked before: **is
    the decision visible where the work happens, and does the work agree with
    it.**

    Four failure classes, none of which a seal, a link checker or the lineage
    checker can see:

    1. **A decision nobody executing the work can see.** AIDE was a registered
       `DIRECT_ADAPT` source for WP-144's candidate state machine and the words
       "AIDE" appeared nowhere in WP-144. An implementer working from the package
       would have written the mechanism from scratch — correctly, under this
       plan's own rules, and for no reason.
    2. **A component the plan names and no register knows.** WP-041 is titled
       *LiteLLM Model Gateway Foundation*; LiteLLM had no register entry, so it
       had no authority boundary, no version policy and no statement of what it
       may never decide. The reverse of (1) and the more dangerous direction:
       adoption without an obligation.
    3. **A package that contradicts its own register.** The register says
       *integrate an object-lock implementation*; a task list that says *build a
       WORM store* has silently reversed a decision that was taken elsewhere.
    4. **An obligation treated as met because nobody printed it.** Every entry in
       both registers is `PROPOSED`. A package that presents a `DIRECT_ADAPT`
       source without a pin, a file list and a characterisation suite is
       inviting exactly the copy ADR-004 refuses.

Why every rule can be made to fail
        python3 scripts/check_wp_implementation_sources.py --self-test

    injects a deliberate defect per rule and fails if any rule stays silent. A
    checker that has never been observed to fail reports "no findings" and "no
    detector" in identical words — the discipline `check_upstream_lineage.py`
    and `monitor_sources.py` already apply.

Exit codes
    0 — every binding holds.  1 — at least one defect.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import acquisition_model as model                                 # noqa: E402

ROOT = model.ROOT
COMPONENTS = model.COMPONENTS
INDEX = ROOT / "provenance" / "COMPONENTS.md"
REUSE = ROOT / "docs" / "architecture" / "AETHRION_COMPONENT_REUSE.md"
STATE_OPEN = ("<!-- generated:register-state — produced by "
              "scripts/check_wp_implementation_sources.py; do not edit inside "
              "this block -->")
STATE_CLOSE = "<!-- /generated:register-state -->"
cell = model.cell

REQUIRED = ("id", "name", "adoption", "status", "work_packages", "owned_contract",
            "not_owned", "authority_boundary", "not_used", "version_policy",
            "failure_semantics", "selection", "conformance", "source")
CMP_ID = re.compile(r"^CMP-\d{3}$")
WP_ID = re.compile(r"^WP-\d{3}$")
GENERATED = re.compile(r"<!--\s*generated:.*?<!--\s*/generated:[a-z-]+\s*-->", re.S)

# A term short enough or common enough to appear by accident is not evidence
# that a package names a component. These are excluded from the prose scan
# rather than from the register: the entry stays, only the text search skips it.
UNSEARCHABLE = {"ERA", "OPA", "MAST", "BATS", "AIDE", "CSL", "SEPIO", "E2B"}

# Words that turn "adopt this" into "build this". Matched only inside the task
# and deliverable sections, where a contradiction is an instruction rather than
# a description.
# The contradiction has a precise shape, and getting it wrong in either
# direction makes the rule useless. "Build the Neo4j claim/source/run/review
# graph **projection**" is correct — AETHRION builds the projection, not the
# database — so the component name alone is not the signal. What is a
# contradiction is the component standing as the thing being built: either the
# head noun of the phrase, or followed by a word that names the component class
# the register just said not to write.
SYSTEM_NOUN = (r"engine|store|platform|server|runtime|database|gateway|tracker|"
               r"sandbox|broker|scheduler|parser|language|implementation")
BUILD_TEMPLATE = (r"\b(?:build|implement|develop|write)\s+"
                  r"(?:a|an|the|our own|its own|one)?\s*"
                  r"{term}\b\s*(?:$|[,.;)]|\band\b|(?:" + SYSTEM_NOUN + r")\b)")
TASK_SECTIONS = ("## Implementation tasks", "## Mandatory deliverables")




def render(components: dict) -> str:
    """The component register as a page — generated, never edited by hand."""
    entries = components["entries"]
    order = ["DEPENDENCY", "ADAPTER", "OPTIONAL_BACKEND", "STANDARD", "PATTERN"]
    by_type: dict[str, list[dict]] = {}
    for entry in entries:
        by_type.setdefault(entry["adoption"], []).append(entry)

    unresolved = sum(len(model._unresolved(e, e["adoption"])) for e in entries)
    bound = len({w for e in entries for w in e["work_packages"]})

    out = [
        "# Component Adoption Register",
        "",
        "| Field | Value |",
        "|---|---|",
        "| Document type | Index — **generated** from `provenance/components.json` |",
        "| Scope | Every external component this system runs on, what AETHRION still owns, and what the component may never decide |",
        "| Sibling documents | `upstreams.json` / [`README.md`](README.md) (mechanisms assimilated into this repository's own code) · "
        "`../docs/architecture/AETHRION_COMPONENT_REUSE.md` (why each is adopted) |",
        "| Status | Regenerated by `scripts/check_wp_implementation_sources.py --write`; **never edited by hand** |",
        f"| Entries | **{len(entries)}** |",
        f"| Bound to | **{bound}** work packages |",
        f"| Open obligations | **{unresolved}** |",
        f"| Register retrieved | {components['retrieval_date']} |",
        "",
        "**In one paragraph.** This register answers *which running implementation "
        "does this control stand on*, and its sibling answers *which mechanisms are "
        "implemented here having been solved somewhere else first*. The distinction "
        "is not pedantic: a `DEPENDENCY` is installed and called and the work happens "
        "inside it, while an assimilated mechanism runs as this system's own code and "
        "leaves no runtime trace of where it came from. The two create different "
        "obligations, which is why they are two registers. Every entry below was "
        "already decided in `AETHRION_COMPONENT_REUSE.md`, an ADR or the package that "
        "owns the integration; what is new is that the decision is now machine-readable "
        "and joined to the package that has to execute it.",
        "",
        "> **A null obligation field is not an oversight.** It is an unresolved "
        "acquisition decision, it is printed in the package that carries it, and "
        "`scripts/ready_queue.py` will not call that package `READY` until it is "
        "answered. Every entry is `PROPOSED` except the two that actually run.",
        "",
        "---",
        "",
        "## Adoption types",
        "",
        "| Type | Meaning | Obligation before implementation |",
        "|---|---|---|",
    ]
    obligation = {
        "DEPENDENCY": "version or image-digest policy · failure semantics",
        "ADAPTER": "version or image-digest policy · failure semantics",
        "OPTIONAL_BACKEND": "a recorded qualification, and the backend actually chosen",
        "STANDARD": "a conformance suite against the published specification",
        "PATTERN": "attribution, and honesty about divergence",
    }
    for name in order:
        if name in components["adoption_types"]:
            out.append(f"| **{name}** | {components['adoption_types'][name]} | "
                       f"{obligation.get(name, '—')} |")
    out.append("")

    for name in order:
        group = by_type.get(name)
        if not group:
            continue
        out += ["---", "", f"## {name} ({len(group)})", "",
                "| ID | Component | Packages | Status | AETHRION owns | May never decide |",
                "|---|---|---|---|---|---|"]
        for entry in group:
            packages = " · ".join(f"`{w}`" for w in entry["work_packages"]) or "—"
            out.append(f"| `{entry['id']}` | {entry['name']} | {packages} | "
                       f"`{entry['status']}` | {cell(entry['owned_contract'], 220)} | "
                       f"{cell(entry['authority_boundary'], 260)} |")
        out.append("")

    out += ["---", "", "## What this register is not", "",
            "It is not an installation list — nothing here is installed, and the two "
            "entries marked `INTEGRATED` are the Zotero and Obsidian adapters that "
            "already run. It is not a recommendation: an `OPTIONAL_BACKEND` row names "
            "a candidate and a way of deciding, never a choice. And it is not "
            "evidence of adoption — `status` is the honest field.", "",
            "## Watched third-party names", "",
            "A name on this list must resolve to a register entry. The list is a rule "
            "set rather than an understanding of what a vendor name looks like, which "
            "is why its size is printed on every run: a name nobody added is a name "
            "nobody checks.", "",
            "  ".join(f"`{n}`" for n in components.get("third_party_watchlist", [])),
            ""]
    return "\n".join(out)


def register_state(components: dict, upstreams: dict) -> str:
    """The two registers, counted rather than remembered."""
    def tally(entries: list[dict], key: str) -> str:
        counts: dict[str, int] = {}
        for entry in entries:
            counts[entry[key]] = counts.get(entry[key], 0) + 1
        return " · ".join(f"{k} {v}" for k, v in sorted(counts.items()))

    ups, cmps = upstreams["entries"], components["entries"]
    bound = len({w for e in ups + cmps for w in e["work_packages"]})
    open_obligations = (
        sum(len(model._unresolved(e, e["assimilation"])) for e in ups)
        + sum(len(model._unresolved(e, e["adoption"])) for e in cmps))
    adapting = sum(1 for e in ups if e["status"] in {"ADAPTING", "ACCEPTED"}
                   and e["assimilation"] == "DIRECT_ADAPT")
    running = sum(1 for e in cmps if e["status"] == "INTEGRATED")

    return "\n".join([
        "| Register | Entries | By type |",
        "|---|---:|---|",
        f"| `provenance/upstreams.json` — mechanisms assimilated | **{len(ups)}** | "
        f"{tally(ups, 'assimilation')} |",
        f"| `provenance/components.json` — components adopted | **{len(cmps)}** | "
        f"{tally(cmps, 'adoption')} |",
        "",
        f"Together they are bound to **{bound} of 160** work packages and carry "
        f"**{open_obligations}** open obligations.",
        "",
        f"**{adapting} entries have reached `ADAPTING`**, and "
        f"**{running} components are `INTEGRATED`** — the Zotero and Obsidian "
        f"adapters, which are the part of this system that actually runs. Every "
        f"other row is a decision on paper: `pinned_commit` is `null` throughout, "
        f"no `MS-*` mechanism specification has been written, and the rules that "
        f"demand a pin, a file list and a characterisation suite begin to bite at "
        f"the moment the first line of code moves.",
    ])


def splice_state(text: str, body: str) -> str:
    block = "\n".join([STATE_OPEN, "", body, "", STATE_CLOSE])
    pattern = re.compile(re.escape(STATE_OPEN) + r".*?" + re.escape(STATE_CLOSE), re.S)
    if not pattern.search(text):
        raise KeyError("register-state block missing from AETHRION_COMPONENT_REUSE.md")
    return pattern.sub(lambda _: block, text)


def load_components() -> dict:
    return json.loads(COMPONENTS.read_text(encoding="utf-8"))


def prose(text: str) -> str:
    """The hand-authored part of a package document — generated blocks removed.

    A generated block quotes the register, so scanning it would let the block
    satisfy the rule that checks the block. Only hand-authored prose counts.
    """
    return GENERATED.sub(" ", text)


def sections(text: str) -> str:
    """Only the parts of a document that instruct rather than describe."""
    out = []
    for heading in TASK_SECTIONS:
        start = text.find(heading)
        if start == -1:
            continue
        end = text.find("\n## ", start + len(heading))
        out.append(text[start:end if end != -1 else len(text)])
    return "\n".join(out)


def search_term(name: str) -> str | None:
    head = re.split(r"\s+[—·]\s+|\s+/\s+", name)[0].strip()
    head = re.sub(r"\s*\([^)]*\)\s*$", "", head).strip()
    if len(head) < 4 or head in UNSEARCHABLE:
        return None
    return head


def consumer_mentions(texts: dict[str, str]) -> int:
    """Packages that name a component they do not own.

    Printed rather than failed. A consumer naming MLflow is using it, and the
    authority boundary belongs once — in the package that adopted it.
    """
    total = 0
    for _, name, bound in model.registered_names():
        term = search_term(name)
        if not term:
            continue
        pattern = re.compile(rf"\b{re.escape(term)}\b")
        total += sum(1 for pid, text in texts.items()
                     if pid not in bound and pattern.search(prose(text)))
    return total


def audit(components: dict, upstreams: dict, documents: dict[str, Path],
          texts: dict[str, str]) -> list[str]:
    """Every rule in one place, so `--self-test` can aim at each by name."""
    problems: list[str] = []
    bindings = [(e["id"], e["name"], set(e.get("work_packages", [])), e["assimilation"])
                for e in upstreams["entries"]]
    bindings += [(e["id"], e["name"], set(e.get("work_packages", [])), e["adoption"])
                 for e in components["entries"]]
    types = set(components["adoption_types"])
    statuses = set(components["statuses"])
    seen: set[str] = set()

    for entry in components["entries"]:
        eid = entry.get("id", "<no id>")

        # B1 — shape, identity and vocabulary
        for field in REQUIRED:
            if field not in entry:
                problems.append(f"{eid}: required field {field!r} is missing")
        if not CMP_ID.match(str(entry.get("id", ""))):
            problems.append(f"{eid}: identifier is not CMP-nnn")
        if eid in seen:
            problems.append(f"{eid}: duplicate identifier")
        seen.add(eid)
        if entry.get("adoption") not in types:
            problems.append(f"{eid}: adoption {entry.get('adoption')!r} is not one "
                            f"of the declared types")
        if entry.get("status") not in statuses:
            problems.append(f"{eid}: status {entry.get('status')!r} is not one of "
                            f"the declared statuses")

        adoption, status = entry.get("adoption"), entry.get("status")

        # B2 — an adopted component must say what it may never decide, and what
        # AETHRION keeps when it is replaced. Adoption without an authority
        # boundary is the failure this register exists to prevent.
        if status != "REJECTED":
            if not (entry.get("authority_boundary") or "").strip():
                problems.append(f"{eid}: no authority boundary stated")
            if not (entry.get("owned_contract") or "").strip():
                problems.append(f"{eid}: does not say what AETHRION owns — a "
                                f"component with no contract behind it is an "
                                f"architecture, not an adoption")

        # B3 — references into the plan must resolve
        for ref in entry.get("work_packages", []):
            if not WP_ID.match(str(ref)):
                problems.append(f"{eid}: {ref!r} is not a work-package identifier")
            elif ref not in documents:
                problems.append(f"{eid}: references {ref}, which is not in the plan")

        # B4 — a component that is running must have a version policy and a
        # failure semantics. `pip install X` is not an adoption decision.
        if adoption in {"DEPENDENCY", "ADAPTER"} and status in {"QUALIFIED", "INTEGRATED"}:
            if not entry.get("version_policy"):
                problems.append(f"{eid}: {adoption} at status {status} with no "
                                f"version or image-digest policy")
            if not entry.get("failure_semantics"):
                problems.append(f"{eid}: {adoption} at status {status} with no "
                                f"failure semantics")

        # B5 — an optional backend may not be chosen implicitly
        if adoption == "OPTIONAL_BACKEND" and status != "PROPOSED" and not entry.get("selection"):
            problems.append(f"{eid}: OPTIONAL_BACKEND at status {status} with no "
                            f"recorded qualification — a backend chosen without "
                            f"one was chosen by whoever wrote it down first")

        # B6 — a standard is implemented as specified, and that is testable
        if adoption == "STANDARD" and status in {"QUALIFIED", "INTEGRATED"} \
                and not entry.get("conformance"):
            problems.append(f"{eid}: STANDARD at status {status} with no "
                            f"conformance suite")

    # B7 — every registered decision is visible in the package that executes it
    for eid, name, bound, _ in bindings:
        for pid in sorted(bound):
            if pid not in documents:
                continue
            if eid not in texts[pid]:
                problems.append(f"{pid}: bound to {eid} ({name.split(' — ')[0]}) in "
                                f"the register, and the package document does not "
                                f"carry it — run scripts/expand_acquisition.py")

    # B8 — a decision with no execution site. An entry bound to no package was
    # decided and handed to nobody, which is the state every entry in this
    # register was in before the acquisition block existed.
    #
    # Note what this rule is *not*. A component is bound to the package that
    # owns its adoption, and it is legitimately *named* by the packages that go
    # on to call it: MLflow is owned by WP-029 and WP-082 and mentioned in
    # fifteen more. Failing those mentions would conflate ownership with use and
    # would push the same authority boundary into fifteen documents, where the
    # fifteenth copy is the one that goes stale. Unbound mentions are counted
    # and printed instead — see `consumer_mentions`.
    for eid, name, bound, decision in bindings:
        # A rejection and a deferral are decisions *not* to take something. They
        # correctly have no execution site, and requiring one would force a
        # package to be named for work nobody is going to do.
        if decision in {"DEFER", "REJECT", "REJECTED", "DEFERRED"}:
            continue
        if not bound:
            problems.append(f"{eid}: {name.split(' — ')[0]} is decided and bound to "
                            f"no work package — a decision with no execution site "
                            f"reaches nobody who has to act on it")

    # B8b — the mirror image, and the one that actually bit: a third-party name
    # this plan is known to use, with no register entry at all. LiteLLM was
    # named in nine package documents and in WP-041's title while no register
    # knew it existed, so it had no authority boundary, no version policy and no
    # statement of what it may never decide.
    #
    # This is a rule set, not a semantic understanding of what a vendor name
    # looks like. The watchlist is the honest form of that limit, and its size
    # is printed on every run so the gap stays visible rather than reading as
    # coverage.
    # A watched name is covered when any register entry names it. Matching on
    # the entry's leading word would miss "Croissant 1.1", "NATS JetStream" and
    # "Neo4j · pgvector · OpenSearch" — three entries that exist and would have
    # been reported as missing, which is a checker failing a correct register.
    # Match against the product name only — the part before the em dash — and
    # case-sensitively. Searching the whole descriptive name reported "Temporal"
    # as registered because ASM-037's description contains the phrase
    # "spatial-temporal message graph": a coverage rule satisfied by an unrelated
    # entry is worse than no rule, because it reports the gap as closed.
    registered = [name.split(" — ")[0] for _, name, _, _ in bindings]
    for watched in components.get("third_party_watchlist", []):
        needle = re.compile(rf"\b{re.escape(watched)}\b")
        if any(needle.search(head) for head in registered):
            continue
        named_in = sorted(pid for pid, text in texts.items()
                          if re.search(rf"\b{re.escape(watched)}\b", prose(text)))
        if named_in:
            problems.append(f"{watched!r} is named in {len(named_in)} package "
                            f"document(s) ({', '.join(named_in[:4])}"
                            f"{' …' if len(named_in) > 4 else ''}) and appears in "
                            f"neither register — adoption without an obligation")

    # B9 — a package may not contradict the decision the register recorded.
    # "Integrate an object-lock implementation" and "build a WORM store" cannot
    # both be true, and the register is the one that was reviewed.
    for entry in components["entries"]:
        if entry["adoption"] not in {"DEPENDENCY", "ADAPTER", "OPTIONAL_BACKEND"}:
            continue
        term = search_term(entry["name"])
        if not term:
            continue
        rule = re.compile(BUILD_TEMPLATE.replace("{term}", re.escape(term)),
                          re.I | re.M)
        for pid in entry.get("work_packages", []):
            if pid not in texts:
                continue
            if rule.search(sections(prose(texts[pid]))):
                problems.append(f"{pid}: its tasks say build {term!r} while "
                                f"{entry['id']} records it as {entry['adoption']} — "
                                f"one of the two is wrong and the register is the "
                                f"one that was reviewed")

    # B10 — an upstream adopted in both registers must say so. PaperQA2 is a
    # runtime ADAPTER and three of its mechanisms are reimplemented natively;
    # both are true, and an implementer who sees only one asks the wrong
    # question — "am I using this or rewriting it?"
    upstream_heads = {}
    for entry in upstreams["entries"]:
        head = re.split(r"\s+—\s+", entry["name"])[0].strip()
        upstream_heads.setdefault(head, []).append(entry)
    for entry in components["entries"]:
        head = re.split(r"\s+—\s+", entry["name"])[0].strip()
        if head not in upstream_heads:
            continue
        others = ", ".join(e["id"] for e in upstream_heads[head])
        if not entry.get("notes") or not any(e["id"] in (entry.get("notes") or "")
                                             for e in upstream_heads[head]):
            problems.append(f"{entry['id']}: {head} is adopted here as "
                            f"{entry['adoption']} and also assimilated as a "
                            f"mechanism ({others}); the entry does not disclose "
                            f"the second decision")

    return problems


def self_test(components: dict, upstreams: dict, documents: dict[str, Path],
              texts: dict[str, str]) -> int:
    def mutate(fn):
        c, u, t = copy.deepcopy(components), copy.deepcopy(upstreams), dict(texts)
        fn(c, u, t)
        return c, u, t

    def first(entries, adoption):
        return next(e for e in entries if e["adoption"] == adoption)

    def qualify(entries, adoption, **clear):
        e = first(entries, adoption)
        e["status"] = "INTEGRATED"
        e.update(clear)

    injections = [
        ("B1 missing required field", lambda c, u, t: c["entries"][0].pop("not_used")),
        ("B2 no authority boundary",
         lambda c, u, t: c["entries"][0].update(authority_boundary="  ")),
        ("B3 reference to a package that does not exist",
         lambda c, u, t: c["entries"][0].update(work_packages=["WP-999"])),
        ("B4 running dependency with no version policy",
         lambda c, u, t: qualify(c["entries"], "DEPENDENCY", version_policy=None,
                                 failure_semantics=None)),
        ("B5 optional backend chosen with no qualification",
         lambda c, u, t: qualify(c["entries"], "OPTIONAL_BACKEND", selection=None)),
        ("B6 standard implemented with no conformance suite",
         lambda c, u, t: qualify(c["entries"], "STANDARD", conformance=None)),
        ("B7 registered decision absent from its package",
         lambda c, u, t: t.update({c["entries"][0]["work_packages"][0]: "nothing here"})),
        ("B8 decided component bound to no package",
         lambda c, u, t: c["entries"][0].update(work_packages=[])),
        ("B8b watched third-party name in neither register",
         lambda c, u, t: c["third_party_watchlist"].append("Temporal") or
                         [e.update(name="redacted") for e in c["entries"]
                          if "Temporal" in e["name"]]),
        ("B9 package tasks contradict the register",
         lambda c, u, t: (c["entries"].append(
             dict(c["entries"][0], id="CMP-900", name="Kafka",
                  adoption="DEPENDENCY", work_packages=["WP-028"], notes=None)),
             t.update({"WP-028": t["WP-028"] +
                       "\n## Implementation tasks\n\n| T01 | Build a Kafka "
                       "broker | owner | ref |\n"}))),
        ("B10 dual adoption not disclosed",
         lambda c, u, t: next(e for e in c["entries"]
                              if e["name"].startswith("PaperQA2")).update(notes=None)),
    ]

    silent = []
    for label, injection in injections:
        c, u, t = mutate(injection)
        before = set(audit(components, upstreams, documents, texts))
        after = set(audit(c, u, documents, t))
        if not (after - before):
            silent.append(label)

    if audit(components, upstreams, documents, texts):
        print("  self-test: the unmutated registers do not pass — fix that first")
        return 1
    for label in silent:
        print(f"  control did not fire: {label}")
    print(f"{len(injections)} controls injected, {len(silent)} silent")
    return 1 if silent else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="regenerate provenance/COMPONENTS.md from the register")
    parser.add_argument("--self-test", action="store_true",
                        help="inject a defect per rule and fail if any rule stays silent")
    args = parser.parse_args()

    components = load_components()
    upstreams = json.loads(model.UPSTREAMS.read_text(encoding="utf-8"))
    documents = model.packages()
    texts = {pid: path.read_text(encoding="utf-8") for pid, path in documents.items()}

    if args.self_test:
        return self_test(components, upstreams, documents, texts)

    problems = audit(components, upstreams, documents, texts)
    index = render(components)
    reuse = REUSE.read_text(encoding="utf-8")
    reuse_updated = splice_state(reuse, register_state(components, upstreams))
    if args.write:
        INDEX.write_text(index, encoding="utf-8")
        REUSE.write_text(reuse_updated, encoding="utf-8")
    else:
        if not INDEX.is_file() or INDEX.read_text(encoding="utf-8") != index:
            problems.append("provenance/COMPONENTS.md has drifted from the register "
                            "(run --write; do not edit it by hand)")
        if reuse != reuse_updated:
            problems.append("AETHRION_COMPONENT_REUSE.md's register state has drifted "
                            "(run --write; do not edit inside the block)")

    for problem in problems:
        print(f"  {problem}")

    bound = len({p for _, _, ps in model.registered_names() for p in ps})
    unresolved = model.unresolved_packages()
    mentions = consumer_mentions(texts)
    watchlist = len(components.get("third_party_watchlist", []))
    print(f"{len(components['entries'])} component entries and "
          f"{len(upstreams['entries'])} upstream entries bound to {bound} of "
          f"{len(documents)} packages, {len(unresolved)} packages with an "
          f"unresolved acquisition obligation, {mentions} downstream mentions of "
          f"an owned component (not a defect), {watchlist} watched third-party "
          f"names, {len(problems)} binding problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
