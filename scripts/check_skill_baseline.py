#!/usr/bin/env python3
"""Measure the half of skill behaviour that can be measured without a runtime.

The claim this exists to narrow
    ``docs/STATUS.md`` has carried the line *"skills conform to a format; none
    has a behaviour baseline"* since the registry existed. It is the largest
    untested claim in the repository and it was true.

    It was also **two claims wearing one sentence.** A skill can fail in two
    different places, and only one of them needs a model to observe:

      routing    can the right skill be REACHED at all, and is it
                 distinguishable from the one it is most confused with?
      execution  once loaded, does it change what the agent does?

    Only the second needs a runtime. The first was simply never checked — and it
    was broken: **seventeen of fifty-two skills were reachable by no chain of
    references from the router.** A skill nobody can route to never loads, so
    its execution behaviour is not unmeasured, it is irrelevant.

    One of the seventeen was ``dispatching-parallel-analysts``, which ``ADR-012``
    names as half of a pair that must never be substituted. Its engineering
    counterpart sat in the router table. A task needing independent analyses
    routed to the skill that decomposes work with one right answer — the exact
    substitution the decision record forbids, reached not by bad judgement but by
    the correct option being unreachable.

Three rules, all deterministic
    R1  reachability — every skill reachable from the router, transitively
    R2  content invariants — each skill still contains its own core rule
    R3  non-synonym separation — the four ADR-012 pairs remain distinguishable

The execution layer is reported, not run
    ``--self-test`` proves each rule can fire. The execution fixtures are printed
    with the reason they did not run and are **never** counted as passing. A
    behaviour baseline that reported PASS for work that did not happen would
    convert an honest gap into a false assurance, which is the failure this whole
    system is built against.

Exit codes
    0 — the routing layer holds.  1 — it does not.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
FIXTURES = SKILLS / "_baseline" / "routing.json"

SKILL_REF = re.compile(r"`([a-z][a-z0-9-]+)`")


def registry() -> set[str]:
    return {d.name for d in SKILLS.iterdir()
            if d.is_dir() and (d / "SKILL.md").exists()}


def skill_text(name: str) -> str:
    """Everything the skill says, not only its card.

    A router entry can legitimately live in a companion file — `brainstorming`
    keeps half its procedure in `visual-companion.md`. Reading only SKILL.md
    would report those references as absent.
    """
    return "\n".join(p.read_text(encoding="utf-8", errors="replace")
                     for p in sorted((SKILLS / name).rglob("*.md")))


def references(names: set[str]) -> dict[str, set[str]]:
    return {n: {r for r in SKILL_REF.findall(skill_text(n)) if r in names} - {n}
            for n in names}


def reachable_from(root: str, edges: dict[str, set[str]]) -> set[str]:
    seen, stack = {root}, [root]
    while stack:
        for nxt in edges.get(stack.pop(), ()):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def domain_of(name: str) -> str:
    found = re.search(r'airl\.domain:\s*"([^"]+)"',
                      (SKILLS / name / "SKILL.md").read_text(encoding="utf-8"))
    return found.group(1) if found else "?"


# ------------------------------------------------------------------- rules
def audit(names: set[str] | None = None,
          edges: dict[str, set[str]] | None = None,
          fixtures: dict | None = None) -> list[str]:
    fixtures = fixtures if fixtures is not None else json.loads(
        FIXTURES.read_text(encoding="utf-8"))
    names = names if names is not None else registry()
    edges = edges if edges is not None else references(names)
    problems: list[str] = []

    # R1 — reachability
    spec = fixtures["reachability"]
    root = spec["root"]
    exempt = set(spec.get("exempt", {}))
    found = reachable_from(root, edges)
    for name in sorted(names - found - exempt):
        problems.append(
            f"R1 {name} is in the registry and no chain of references from "
            f"{root} reaches it — it can never be routed to, so whatever it "
            f"says is unreachable rather than untested")

    # R2 — content invariants
    for name, rule in sorted(fixtures["content_invariants"].items()):
        if name not in names:
            problems.append(f"R2 the baseline names {name}, which is not a skill")
            continue
        text = skill_text(name)
        for phrase in rule["must_contain"]:
            if phrase.lower() not in text.lower():
                problems.append(
                    f"R2 {name} no longer contains {phrase!r} — {rule['why']}")
        for phrase in rule.get("must_not_contain", []):
            if phrase.lower() in text.lower():
                problems.append(
                    f"R2 {name} contains {phrase!r}, which it must not — "
                    f"{rule['why']}")

    # R3 — the four pairs stay apart
    for pair in fixtures["non_synonym_pairs"]:
        eng = pair["engineering"]
        for sci in pair["scientific"]:
            for name in (eng, sci):
                if name not in names:
                    problems.append(
                        f"R3 the pair names {name}, which is not a skill")
            if eng not in names or sci not in names:
                continue
            if domain_of(eng) == domain_of(sci):
                problems.append(
                    f"R3 {eng} and {sci} are both '{domain_of(eng)}' — the pair "
                    f"exists because they are different disciplines, and a "
                    f"router that sees one family cannot choose between them")
            if sci not in found:
                problems.append(
                    f"R3 {sci} is unreachable while its counterpart {eng} is "
                    f"routable — a task needing {sci} lands on {eng}, which is "
                    f"the substitution ADR-012 forbids. "
                    f"{pair['substitution_fails_because']}")
    return problems


# --------------------------------------------------------------- self-test
def self_test() -> int:
    """Each rule must be observed refusing the defect it was written for."""
    names = registry()
    edges = references(names)
    base = json.loads(FIXTURES.read_text(encoding="utf-8"))

    def orphan(_n, e, _f):
        """Cut every reference to a skill: R1 must notice it went dark."""
        target = "verification-before-completion"
        return _n, {k: (v - {target}) for k, v in e.items()}, _f

    def drift(_n, e, f):
        """A skill that no longer contains its own rule."""
        clone = json.loads(json.dumps(f))
        clone["content_invariants"]["test-driven-development"]["must_contain"] = [
            "a phrase this skill has never contained"]
        return _n, e, clone

    def collapse(_n, e, f):
        """A pair whose halves land in one family, so a router cannot separate them."""
        clone = json.loads(json.dumps(f))
        clone["non_synonym_pairs"] = [{
            "engineering": "test-driven-development",
            "scientific": ["systematic-debugging"],   # both engineering
            "substitution_fails_because": "injected",
        }]
        return _n, e, clone

    mutations = [
        ("R1", "a skill nothing references any more", orphan),
        ("R2", "a skill that has drifted out of its own core rule", drift),
        ("R3", "a confusable pair collapsed into one family", collapse),
    ]
    silent = []
    for rule, description, mutate in mutations:
        n, e, f = mutate(names, edges, base)
        if not any(p.startswith(rule) for p in audit(n, e, f)):
            silent.append((rule, description))
    print(f"{len(mutations)} mutations injected · {len(silent)} rule(s) stayed silent")
    for rule, description in silent:
        print(f"  ✗ {rule} did not fire on {description}")
    return 1 if silent else 0


def main() -> int:
    if "--self-test" in sys.argv[1:]:
        return self_test()

    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    names = registry()
    problems = audit(names, fixtures=fixtures)
    execution = fixtures["execution_fixtures"]

    print(f"{len(names)} skills · "
          f"{len(reachable_from(fixtures['reachability']['root'], references(names)))} "
          f"reachable from {fixtures['reachability']['root']} · "
          f"{len(fixtures['content_invariants'])} content invariants · "
          f"{len(fixtures['non_synonym_pairs'])} non-synonym pairs")
    for problem in problems:
        print(f"  ✗ {problem}")

    # Reported, never counted. The execution layer is the half that needs a
    # runtime, and saying so on every run is the whole point.
    print(f"\nexecution layer: {len(execution['fixtures'])} fixtures, "
          f"status {execution['status']}")
    print(f"  not run — {execution['blocked_by']}")
    print(f"  pass criterion, for when a runtime exists: {execution['pass_criterion']}")

    if problems:
        print(f"\n{len(problems)} routing baseline violation(s)")
        return 1
    print("\nthe routing baseline holds: every skill is reachable, each still "
          "contains its own core rule, and the four confusable pairs remain in "
          "different families with both halves routable. That is a precondition "
          "for following a procedure, not evidence of having followed one")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
