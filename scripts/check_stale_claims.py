#!/usr/bin/env python3
"""Find statements about the present that the repository has outgrown.

Responsibility
    ``check_doc_consistency.py`` checks *declared counts* against reality. This
    checks *prose*: a sentence that says "there is no CI" after a CI control was
    written, or "38 skills" in a document describing the current registry.

Invariant
    **Historical records are exempt, and that exemption is the point.** An
    implementation log entry, a frozen audit and a past step summary describe
    the state at their date; editing them to match today would destroy the record
    the repository keeps them for — `docs/DOCUMENT_STANDARD.md` §3 rules 3 and 4.
    So the exemption list is explicit and narrow rather than a blanket skip.

Audit findings
    Written after a corpus scan found 66 stale phrases, of which roughly half
    were legitimate history. A checker that cannot tell those apart would push a
    maintainer toward exactly the edit the standard forbids.

Three rule families, and the third is the newest
    *Literal* rules match a number somebody typed. *Derived contradiction* rules
    read the repository and look for prose disagreeing with it. **Architectural
    regression** rules — added at baseline v1.3.0 — look for a sentence that is
    not merely out of date but says the opposite of a decision record: a
    single-agent default, a fully-connected topology presented as the target, an
    event treated as authority, a projection treated as canonical, a timeout that
    approves something.

    These are the phrases `35_DEFINITION_OF_DONE_FINAL_AUDIT.md` asks a final
    audit to search for by hand. A hand search runs once, on the day someone
    remembers to run it. Every phrase on that list appears in this repository
    *inside a prohibition* — which is why each rule is paragraph-scoped and
    suppressed by a prohibition marker, and why every rule ships with both a
    specimen that must fire it and a specimen that must not.

Self-test
    ``--self-test`` runs both specimens through every regression rule and reports
    any rule that stayed silent on its positive or spoke on its negative. A
    checker that has never been observed to refuse reports "no findings" and
    "no detector" in identical words.

Exit codes
    0 — no stale present-tense claim.  1 — at least one.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files that record a moment and must never be edited to match the present.
HISTORICAL = (
    "implementation_log.md",
    "FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md",
    "claude_framework_audit_report.md",
    "session_handover_",              # its history section; the live fields are checked below
    "CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md",
    "_framework_audit_evidence.md",
    "remediation_verification",       # frozen dated verification reports

)
SKIP_DIRS = (".venv", "70 - Literature Sets", "skills/_vendor", "01 - Commissioning")

# A match inside one of these contexts is history, not a claim about the present.
# Reporting verbs matter as much as past tense here. A change record that says
# a document "said X — it is not" quotes the defect in order to deny it, and
# flagging that quotation would push a maintainer to delete the record of the
# correction, which is the edit DOCUMENT_STANDARD.md §3 rule 4 forbids.
PAST_TENSE = re.compile(
    r"\b(at the time|were|was|then held|previously|before this|used to|"
    r"had been|no longer|said|claimed|stated|corrected|it is not|"
    r"does not|did not)\b", re.I)
LEDGER_ROW = re.compile(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|")


def is_history(line: str) -> bool:
    """A dated ledger row, or a sentence written in the past tense."""
    return bool(LEDGER_ROW.match(line.strip()) or PAST_TENSE.search(line))


def _sealed() -> int:
    seal = ROOT / "planning" / "commissioning" / "00_PROGRAM" / "SHA256SUMS.txt"
    return len(seal.read_text(encoding="utf-8").strip().splitlines())


def _skills() -> int:
    return len([d for d in (ROOT / "skills").iterdir()
                if d.is_dir() and (d / "SKILL.md").exists()])


def _figures() -> int:
    return len(list((ROOT / "docs" / "figures").glob("*.svg")))


def _scenarios() -> int:
    return len(list((ROOT / "planning" / "commissioning" / "12_ACCEPTANCE_SCENARIOS")
                    .glob("ACC-*.md")))


# The corrections quote numbers, so they are derived rather than typed. A
# checker whose own advice has gone stale is worse than no checker: it tells a
# maintainer to write a wrong number with the authority of a passing build.
# This list said "the seal covers 207 files" while the seal covered 221.
CLAIMS: list[tuple[str, str]] = [
    (r"\bACC-01\s*[–-]\s*ACC-40\b", f"the scenario range ends at ACC-{_scenarios():02d}"),
    (r"\b(?:38|49|51) skills\b", f"the registry holds {_skills()} skills"),
    (r"\b46 scenarios\b", f"there are {_scenarios()} scenarios"),
    (r"\b(?:195|196|202|207)/(?:195|196|202|207)\b", f"the seal covers {_sealed()} files"),
    (r"[Tt]here is no CI\b", "BVC-01 is written and staged; say staged, not absent"),
    (r"\b(?:three|four|five|six|seven|eight) of them rather than one\b",
     f"there are {_figures()} figures"),
]

# ---------------------------------------------------------------------------
# Semantic checks. The three above this line match a literal that somebody
# thought to write down. These derive the truth from the repository and then
# look for prose that disagrees with it, which is the class of defect the
# literal list kept missing.
# ---------------------------------------------------------------------------

# Deliberately narrow. A decision record makes a question *decided*; it does not
# make the thing it decided *built*. "H5 remains open" is true — ADR-002 chose a
# control and the CI platform is still absent — so implementation-absence wording
# is left alone and only decision-shaped wording is flagged.
UNDECIDED = re.compile(
    r"\b(undecided|not yet decided|an open question|open decision|"
    r"is still open|remains an open question|no standard answers it)\b", re.I)


def resolved_findings() -> dict[str, str]:
    """Audit findings that an ACCEPTED decision record has closed."""
    out: dict[str, str] = {}
    for adr in sorted((ROOT / "docs" / "architecture").glob("ADR-*.md")):
        text = adr.read_text(encoding="utf-8")
        status = next((l for l in text.splitlines() if l.startswith("| Status")), "")
        if "ACCEPTED" not in status:
            continue
        for match in re.finditer(r"finding\s+\**([CHM]\d+)\**", text):
            out.setdefault(match.group(1), adr.name)
    return out


def contradictions() -> list[tuple[re.Pattern[str], str]]:
    """Claims the repository can currently disprove about itself."""
    rules: list[tuple[re.Pattern[str], str]] = []

    # The attestation profile states what it does not cover. A document may not
    # claim an assurance the issued manifest explicitly disclaims.
    policy = (ROOT / "planning" / "commissioning" / "01_GOVERNANCE"
              / "WP-000_interim_evidence_policy.md")
    if policy.exists() and "not submitted to a transparency log" in policy.read_text(
            encoding="utf-8"):
        rules.append((
            # Matches any phrasing that puts the manifest in a transparency
            # log. The first version of this rule required the word "recorded"
            # and missed "as a signed in-toto attestation in a public
            # transparency log" two files away.
            re.compile(r"in a public transparency log", re.I),
            "WP-000 runs the interim profile and is NOT in a transparency log",
        ))

    # The specimen states whether it has been rendered; nothing may say otherwise.
    specimen = ROOT / "delivery" / "specimen" / "README.md"
    if specimen.exists() and "never rendered" in specimen.read_text(encoding="utf-8"):
        rules.append((
            re.compile(r"\bspecimen\s+rendered\b", re.I),
            "delivery/specimen/README.md says never rendered — no toolchain installed",
        ))

    return rules


# ---------------------------------------------------------------------------
# Architectural regression rules — baseline v1.3.0.
#
# The list comes from `35_DEFINITION_OF_DONE_FINAL_AUDIT.md`, which asks a final
# audit to grep for wording the decision records have made wrong. Each phrase
# already appears in this repository, every time inside a sentence that forbids
# it, so a naive grep produces a wall of false positives and gets switched off.
#
# The discrimination is context, not cleverness: a paragraph that refuses a
# thing and a paragraph that asserts it use the same nouns and different verbs.
# So the rule matches the noun phrase and a PROHIBITION marker suppresses it.
# The failure mode this accepts is stated plainly: an author who asserts the
# regression *inside* a paragraph that also refuses something else escapes the
# rule. That is a narrower gap than not looking at all, and it is why the
# `specimen_clean` half of the self-test exists — it pins the suppression to
# behaviour rather than to intention.
# ---------------------------------------------------------------------------

# A bare "not" is useless as a prohibition marker and actively harmful: the
# first version of this guard contained one, and it suppressed the timeout rule
# on the sentence "if the reviewer does NOT respond the gate auto-approves" —
# an incidental negation reading as a refusal. The markers below are idioms that
# do the refusing, not words that happen to appear near it.
PROHIBITION = re.compile(
    r"\b(never|cannot|can't|may not|must not|is not|are not|no longer|"
    r"refus\w*|forbid\w*|prohibit\w*|reject\w*|denie\w*|deny|"
    r"instead of|rather than|is wrong|baseline|counter-?example|"
    r"anti-?pattern|stale|regression|hazard|refuted)\b", re.I)


# The paragraph guard is not enough on its own. "Timeout escalation path with
# NO approval branch" is a heading in a deliverable list — no surrounding
# sentence, no prohibition idiom, and a perfectly correct statement. So the
# thirty characters before the match are checked for a local negator too. Two
# guards at different scopes, because the false positives arrived at both.
LOCAL_NEGATION = re.compile(
    r"\b(no|never|without|zero|not|non|neither|nor|prevents?|excludes?)\b"
    r"[\s\-—,]*(?:\w+[\s\-]+){0,3}$", re.I)


class Regression:
    """One architectural-regression rule, carrying its own two specimens.

    `specimen_dirty` must be flagged and `specimen_clean` must not. Both are
    required: a rule with only a positive specimen can be satisfied by matching
    everything, and a rule with only a negative can be satisfied by matching
    nothing.
    """

    def __init__(self, name: str, pattern: str, correction: str,
                 specimen_dirty: str, specimen_clean: str) -> None:
        self.name = name
        self.pattern = re.compile(pattern, re.I)
        self.correction = correction
        self.specimen_dirty = specimen_dirty
        self.specimen_clean = specimen_clean

    def fires_on(self, block: str) -> bool:
        if PROHIBITION.search(block):
            return False
        for match in self.pattern.finditer(block):
            before = block[max(0, match.start() - 30):match.start()]
            if not LOCAL_NEGATION.search(before):
                return True
        return False


REGRESSIONS = [
    Regression(
        "single-agent default",
        r"\bsingle[- ]agent\b[^.\n]{0,60}\b(default|standard|normal|usual|"
        r"typical|suffices|is enough|is sufficient)\b"
        r"|\b(default|standard|normal|usual|typical)\b[^.\n]{0,60}"
        r"\bsingle[- ]agent\b",
        "ADR-011: substantial scientific execution requires an independent "
        "cohort; a single agent is not a default it can fall back to",
        "For a substantial analysis the default is single-agent execution, and "
        "a second reviewer is added when time allows.",
        "There is no silent single-agent downgrade: compilation refuses rather "
        "than dropping to one actor.",
    ),
    Regression(
        "fully-connected as the target topology",
        r"\bfully[- ]connected\b[^.\n]{0,60}\b(target|intended|desired|"
        r"production|design|architecture|topology we|is what we)\b"
        r"|\b(target|intended|desired|production)\b[^.\n]{0,60}"
        r"\bfully[- ]connected\b",
        "ADR-013: the fully-connected cohort is the measurement baseline. The "
        "target is the compiled sparse topology that beats it",
        "The target communication design is a fully-connected cohort so that "
        "every actor sees every message.",
        "Coordination overhead is measured against the fully-connected "
        "baseline, which is the control arm and not the target.",
    ),
    Regression(
        "mechanical verifier doing semantic work",
        r"\bmechanical\b[^.\n]{0,50}\b(entailment|semantic|claim scope|"
        r"citation support|method[–-]code|paraphrase|judgement|judgment)\b"
        r"|\b(entailment|semantic|claim scope|citation support)\b"
        r"[^.\n]{0,50}\bmechanical (check|verifier|verification)\b",
        "ADR-008: a model-mediated semantic check is V2 and produces a finding "
        "with a measured error rate, not a mechanical verdict",
        "A mechanical check confirms citation support before the claim is "
        "published.",
        "Citation entailment is V2 and is never described as a mechanical "
        "check; it produces a finding routed to review.",
    ),
    Regression(
        "a timeout that approves",
        r"\bauto[- ]?approv\w*\b"
        r"|\b(timeout|time[- ]out|no response|non[- ]response|silence|"
        r"the sla elaps\w+)\b[^.\n]{0,40}"
        r"\b(becomes?|is treated as|counts as|is deemed|implies|"
        r"results in|grants?|confers?|is taken as)\b[^.\n]{0,25}"
        r"\b(approv\w+|accept\w+|consent|sign[- ]?off)\b",
        "ADR-016 and skills/escalating-and-paging: a timeout escalates. It "
        "never becomes an approval, through any interface",
        "If the reviewer does not respond within 48 hours the gate "
        "auto-approves so the pipeline proceeds.",
        "A timeout never becomes an approval; the request escalates and the "
        "gate stays closed.",
    ),
    Regression(
        "an event treated as authority",
        r"\b(NATS |event bus |event )\w*\b[^.\n]{0,50}"
        r"\b(is the (authority|source of truth|canonical record)|"
        r"as the (authority|source of truth|canonical record)|"
        r"is authoritative|proves the state|confirms the transition)\b",
        "ADR-014: an event announces a transition. The canonical store is "
        "re-read; a payload is never promoted to truth",
        "The consumer trusts the event payload, which is the source of truth "
        "for the gate position.",
        "A NATS event alone is not evidence of canonical state; the consumer "
        "re-reads the store rather than trusting the payload.",
    ),
    Regression(
        "a projection treated as canonical",
        r"\b(Neo4j|pgvector|the vector (store|index)|OpenSearch|"
        r"the graph (store|projection)|the search index|MLflow)\b"
        r"\s+(is|as|remains|serves as|acts as|becomes|holds)\s+"
        r"(the\s+|our\s+)?(canonical|authoritative|source of truth|"
        r"system of record|truth\b)",
        "ADR-014: exactly one canonical owner per kind of state. Every index "
        "is a projection that can be destroyed and rebuilt losslessly",
        "Neo4j is the canonical store for the scientific record and the graph "
        "owns the relationships.",
        "Neo4j projects the relational record and is never canonical; drop it "
        "and rebuild it and nothing is lost.",
    ),
    Regression(
        "a published number without its binding",
        r"\b(publish\w*|report\w*|paper|manuscript)\b[^.\n]{0,60}"
        r"\b(without|independent of|regardless of)\b[^.\n]{0,40}"
        r"\b(ClaimVersion|VerifiedValue|evidence chain|EvidenceTag)\b",
        "ADR-009 and ACC-106: every published assertion binds a ClaimVersion "
        "and every number resolves to a VerifiedValue",
        "Summary figures may be published without a VerifiedValue when they "
        "are only illustrative.",
        "A number published without a VerifiedValue cannot reach the "
        "manuscript; the build refuses it however good the prose is.",
    ),
    Regression(
        "engineering skills demoted to tooling",
        r"\b(engineering (skills|discipline|family)|superpowers|"
        r"vendored eleven)\b[^.\n]{0,50}"
        r"\b(merely|only|just|nothing more than|simply)\b[^.\n]{0,40}"
        r"\b(bootstrap|tooling|scaffold\w*|convenience|helper\w*)\b",
        "ADR-012: the engineering family is where a large share of the "
        "science's failure modes live — evaluators, preprocessing, "
        "reproduction packages. It is a discipline, not tooling",
        "The engineering skills are merely bootstrap tooling for setting up a "
        "workspace.",
        "The engineering family is not merely bootstrap tooling: a broken "
        "evaluator is a scientific failure that arrives as a code defect.",
    ),
    # --- baseline v1.3.3 · ADR-020 ------------------------------------------
    # Adopting a collaboration substrate creates four new ways to write
    # something that is nearly true. Each of these sentences would pass a
    # reviewer who is not holding the boundary in mind, which is what makes them
    # worth a rule rather than a note.
    Regression(
        "a collaboration backend as the source of truth",
        r"\b(buzz|collaboration backend)\b[^.\n]{0,60}"
        r"\b(source of truth|canonical|system of record|holds the (claim|evidence|gate))\b"
        r"|\b(canonical|source of truth)\b[^.\n]{0,40}"
        r"\b(buzz|collaboration backend)\b",
        "ADR-020: the backend carries messages and holds no scientific state. "
        "Remove it and every claim, evidence span, verified value and decision "
        "must survive",
        "Buzz is the canonical store for collaboration state and the "
        "system of record for what each actor concluded.",
        "Buzz Relay is never the canonical store: a room is a projection, and "
        "deleting it loses no claim or evidence span.",
    ),
    Regression(
        "a runtime named as the architecture",
        r"\b(hermes|codex|claude code|buzz agent)\b[^.\n]{0,40}"
        r"\b(is|as) the\b[^.\n]{0,30}"
        r"\b(aethrion (agent )?runtime|agent runtime|orchestrator|"
        r"task compiler|architecture)\b",
        "ADR-020: a runtime is a qualified profile behind the AgentRuntime "
        "contract. Hermes is preferred and not exclusive, and a runtime is "
        "never a role",
        "Hermes is the AETHRION agent runtime and every actor is a Hermes "
        "agent.",
        "Hermes is one qualified runtime profile rather than the AETHRION "
        "agent runtime; Codex and Claude Code remain selectable.",
    ),
    Regression(
        "a backend approval treated as the human decision",
        r"\b(buzz|backend|workflow|chat)\b[^.\n]{0,40}\bapprov\w+\b"
        r"[^.\n]{0,40}\b(g8|g9|decisionrecord|human decision|"
        r"scientific decision)\b"
        r"|\b(g8|g9|decisionrecord)\b[^.\n]{0,40}"
        r"\b(buzz|backend|chat) approv\w+",
        "ADR-020: an approval is an interaction surface. The canonical decision "
        "is a signed DecisionRecord written through the Decision Service, and a "
        "backend cannot move G8 or G9",
        "A Buzz approval creates the G8 DecisionRecord once the operator "
        "clicks it.",
        "A Buzz approval is not a G8 DecisionRecord and cannot move the gate; "
        "the canonical decision is signed through the Decision Service.",
    ),
    Regression(
        "channel history offered as context",
        r"\b(channel|room|chat|conversation|transcript) history\b"
        r"[^.\n]{0,60}\b(context|contextprojection|projection|"
        r"what the agent sees)\b"
        r"|\b(context|contextprojection|projection|what the agent sees)\b"
        r"[^.\n]{0,60}\b(channel|room|chat|conversation|transcript) history\b",
        "ADR-020 §6: a ContextProjection is assembled from canonical state, "
        "admissible evidence, the compiled skill bundle and the peer deltas the "
        "round permits. A transcript is neither cost-bounded nor independent",
        "The agent's context is the room history plus the task, which keeps "
        "everyone aligned.",
        "Channel history is never the ContextProjection: appending a "
        "transcript would negate round zero and the budget at once.",
    ),
]


def self_test() -> int:
    """Every regression rule must be observed firing, and observed staying quiet."""
    silent, noisy = [], []
    for rule in REGRESSIONS:
        if not rule.fires_on(rule.specimen_dirty):
            silent.append(rule.name)
        if rule.fires_on(rule.specimen_clean):
            noisy.append(rule.name)
    print(f"{len(REGRESSIONS)} architectural regression rules · "
          f"{len(silent)} silent on their positive specimen · "
          f"{len(noisy)} firing on their negative specimen")
    for name in silent:
        print(f"  ✗ {name}: did not fire on the sentence written to trip it")
    for name in noisy:
        print(f"  ✗ {name}: fired on the sentence written to be legitimate")
    return 1 if silent or noisy else 0


# ---------------------------------------------------------------------------
# Dynamic facts — the fourth rule family, added at baseline v1.3.1.
#
# The three families above match *phrasings*. This one guards *values whose
# correct answer changes as the repository grows*, which is a different problem:
# nobody typed a wrong number, they typed a right one and the repository moved.
#
# Seven live surfaces said "141 packages" or "fifty-one scenarios" while the
# registries held 160 and 120, and every check in the bundle passed — because
# check_doc_consistency.py enforces a derived count only where a rule names the
# document AND the pattern, and none named these.
#
# Two deliberate restrictions, because the naive version of this rule is worse
# than nothing:
#
#   1. Only LIVE surfaces are scanned. A dated audit report saying "51 scenarios
#      existed at the time" is correct and must stay. That is the same exemption
#      the historical-record rule above makes, and for the same reason.
#   2. Only the facts listed here. Scanning every number in every document
#      produces a wall of findings about page counts, port numbers and years,
#      and a checker whose output is a wall is a checker nobody reads.
# ---------------------------------------------------------------------------

LIVE_SURFACES = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "docs/DOCUMENT_STANDARD.md",
    "docs/OPERATIONS.md",
    "docs/figures/README.md",
    "planning/commissioning/README.md",
    "planning/commissioning/00_PROGRAM/",
    "scripts/README.md",
    "tests/README.md",
    "schemas/README.md",
    "provenance/README.md",
)

NUMBER_WORDS = {
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "fifty-one": 51,
    "eighty": 80, "one hundred": 100,
}


def _packages() -> int:
    """Numbered packages — WP-001 upward, excluding the WP-000 bootstrap.

    Two different true answers exist here and confusing them is its own defect:
    the plan is 159 numbered packages *plus* a bootstrap package, and 160
    package documents. check_doc_consistency.py already draws that line, and
    this rule uses the same one so the two checkers cannot contradict."""
    matrix = (ROOT / "planning" / "commissioning" / "00_PROGRAM"
              / "package_dependency_matrix.csv")
    rows = matrix.read_text(encoding="utf-8").strip().splitlines()[1:]
    return sum(1 for r in rows if not r.startswith('"WP-000"'))


def _baseline() -> str:
    meta = (ROOT / "planning" / "commissioning" / "00_PROGRAM"
            / "programme_metadata.json").read_text(encoding="utf-8")
    return re.search(r'"version":\s*"(v[\d.]+)"', meta).group(1)


class DynamicFact:
    """A value the repository can compute, and the wordings that state it.

    `stale` is the set of values that were once correct. Matching those rather
    than "any number here" is what keeps the rule from firing on a sentence that
    contains a number for an unrelated reason.
    """

    def __init__(self, name, current, pattern, correction) -> None:
        self.name, self.current = name, current
        self.pattern, self.correction = re.compile(pattern, re.I), correction

    def findings(self, path: Path, text: str) -> list[str]:
        rel = str(path.relative_to(ROOT))
        if not any(rel.startswith(s) or rel == s for s in LIVE_SURFACES):
            return []
        out = []
        actual = self.current()
        for match in self.pattern.finditer(text):
            raw = next((g for g in match.groups() if g), None)
            if raw is None:
                continue
            claimed = NUMBER_WORDS.get(raw.lower(), None)
            if claimed is None:
                claimed = int(raw) if raw.isdigit() else raw
            if claimed == actual:
                continue
            line_no = text[:match.start()].count("\n") + 1
            if is_history(text.splitlines()[line_no - 1]):
                continue
            out.append(f"{rel}:{line_no}  {self.name} — says {claimed!r}, "
                       f"the repository holds {actual!r}. {self.correction}")
        return out


DYNAMIC_FACTS = [
    DynamicFact(
        "programme package count", _packages,
        r"\b(\d{2,4})\s+work packages are managed\b"
        r"|\ball (\d{2,4}) work packages\b"
        r"|\bindex of (\d{2,4}) packages\b"
        r"|\bplan is (\d{2,4}) packages\b"
        r"|\bacross (\d{2,4}) packages\b",
        "Numbered packages, excluding the WP-000 bootstrap — the convention "
        "check_doc_consistency.py already uses."),
    DynamicFact(
        "acceptance scenario count", _scenarios,
        r"\bAll (\d{2,4}|fifty-one|eighty) scenarios\b"
        r"|\bThe (fifty-one|\d{2,4}) (?:acceptance )?scenarios\b"
        r"|\b(\d{2,4}|fifty-one) scenarios, by\b",
        "Scenario totals belong to 12_ACCEPTANCE_SCENARIOS."),
    DynamicFact(
        "skill registry size", _skills,
        r"\bregistry holds (\d{2,3}) skills\b|\ball (\d{2,3}) skills\b",
        "Skill totals belong to skills/."),
    DynamicFact(
        "current commissioning baseline", _baseline,
        r"[Tt]he current baseline is \*?\*?(v\d+\.\d+\.\d+)"
        r"|\| Baseline \| `?(v\d+\.\d+\.\d+)"
        r"|\bcommissioning baseline (v\d+\.\d+\.\d+) —",
        "Only sentences asserting the CURRENT baseline are matched. "
        "\"Added by baseline v1.2.0\" states when something changed and is "
        "correct forever; matching that too would push a maintainer to rewrite "
        "history, which DOCUMENT_STANDARD.md \u00a73 forbids."),
]


def paragraphs(text: str):
    """Yield (first_line_number, paragraph). Claims wrap across lines."""
    line_no = 1
    for block in text.split("\n\n"):
        yield line_no, block
        line_no += block.count("\n") + 2


def is_historical(path: Path) -> bool:
    return any(marker in str(path) for marker in HISTORICAL)


def main(argv: list[str] | None = None) -> int:
    if "--self-test" in (argv if argv is not None else sys.argv[1:]):
        return self_test()

    findings: list[str] = []
    scanned = exempt = 0
    contradiction_rules = contradictions()
    closed = resolved_findings()

    for path in sorted(ROOT.rglob("*.md")):
        text_path = str(path)
        if any(skip in text_path for skip in SKIP_DIRS):
            continue
        if is_historical(path):
            exempt += 1
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern, correction in CLAIMS:
            for match in re.finditer(pattern, text):
                line_no = text[:match.start()].count("\n") + 1
                line = text.splitlines()[line_no - 1]
                if is_history(line):
                    continue
                findings.append(f"{path.relative_to(ROOT)}:{line_no}  "
                                f"{match.group(0)!r} — {correction}")

        for pattern, correction in contradiction_rules:
            for match in re.finditer(pattern, text):
                line_no = text[:match.start()].count("\n") + 1
                if is_history(text.splitlines()[line_no - 1]):
                    continue
                findings.append(f"{path.relative_to(ROOT)}:{line_no}  "
                                f"{match.group(0)!r} — {correction}")

        # A decision record closes a finding; prose may not still call it open.
        # The record itself is exempt, because it narrates the state it closed.
        for fact in DYNAMIC_FACTS:
            findings.extend(fact.findings(path, text))

        # Architectural regressions. Decision records are NOT exempt here —
        # unlike the undecided-finding rule below — because an ADR asserting a
        # regression is the worst place for one to live, not the safest.
        for line_no, raw_block in paragraphs(text):
            block = raw_block.replace("**", "").replace("*", "")
            if is_history(block):
                continue
            for rule in REGRESSIONS:
                if rule.fires_on(block):
                    findings.append(f"{path.relative_to(ROOT)}:{line_no}  "
                                    f"{rule.name} — {rule.correction}")

        if not path.name.startswith("ADR-"):
            for line_no, raw_block in paragraphs(text):
                # Bold and italics land in the middle of the phrases being
                # matched — "is **still open**" — so emphasis is stripped first.
                block = raw_block.replace("**", "").replace("*", "").replace("_", " ")
                if not UNDECIDED.search(block) or is_history(block):
                    continue
                for finding_id, adr in closed.items():
                    # The id must be introduced as an audit finding. "C2" also
                    # names a proposal item in AETHRION_IDEAL_STRUCTURE.md, and
                    # matching a bare token would flag an unrelated table.
                    if re.search(rf"finding\s+\**{finding_id}\b", block, re.I):
                        findings.append(
                            f"{path.relative_to(ROOT)}:{line_no}  "
                            f"calls {finding_id} undecided — decided by {adr}")

    print(f"{scanned} documents scanned · {exempt} historical records exempt · "
          f"{len(CLAIMS)} literal rules · {len(contradiction_rules)} derived "
          f"contradiction rules · {len(REGRESSIONS)} architectural regression "
          f"rules · {len(DYNAMIC_FACTS)} dynamic facts over "
          f"{len(LIVE_SURFACES)} live surfaces · "
          f"{len(closed)} closed finding(s) tracked")
    for finding in findings:
        print(f"  ✗ {finding}")
    if findings:
        print(f"\n{len(findings)} stale present-tense claim(s)")
        return 1
    print("\nno document contradicts the rules above — which is narrower than "
          "\"nothing is stale\", and the count of rules is printed so the gap "
          "stays visible")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
