# Visual Completion — Selection Records

| Field | Value |
|---|---|
| Document type | Evidence — dated selection records, frozen once written |
| Protocol | `instructions/02_CLAUDE_COMPARATIVE_SELECTION_PROTOCOL.md` |
| Rule applied | *Do not choose this package's candidate merely because the package provided it. The package is a strong alternative, not authority.* |
| Date | 2026-08-23 |

**In one paragraph.** The protocol requires three concepts compared per
materially changed figure: the current repository version, the package
candidate, and a genuinely different alternative. Below, the concept adopted for
each is recorded with what was rejected and why. In every case the *defect* came
from the package and the *design* did not — which is the outcome the protocol is
built to produce, and worth stating plainly rather than presenting each as an
independent discovery.

## The renderer decision, made once

Instruction 09 asks for three renderer paths to be evaluated. **Path A —
`figure_kit`** is adopted for every figure, and the package's Graphviz is
rejected as a repository renderer.

The reasoning is not preference. `figure_kit` measures every string against the
box it sits in and **raises** rather than shrinking text below a 16-unit
legibility floor — which is instruction 03's zero-tolerance rule enforced at
generation time rather than checked afterwards. It caught two labels during this
pass and refused to draw them; both were shortened, which is what the policy
requires. Graphviz would have laid them out at whatever size fit.

The package's DOT candidates were read as *concepts*. None was imported.

---

## FIG-D · `aethrion_discovery.svg` — the state panel

| Concept | Verdict |
|---|---|
| **Current repository figure** | **Vetoed.** Four states in a row with arrows between them: `DRAFT → DEBUG → IMPROVE → FUSE`. `ADR-006` §2 draws a *branch*. Hard veto: stale architecture, misleading causality |
| **Package FIG12 + FIG13** | Rejected as a pair. It splits candidate fidelity from evaluator authority across two figures, and the repository figure already carries the authority boundary as its strongest element. Splitting would have weakened the surviving half |
| **Adopted — the ADR's own topology** | One question — *did the parent execute?* — selecting `DEBUG` or `IMPROVE` as alternatives, with `FailedApproach` on the exhaustion edge and `FUSE` fed by two branches |

**Semantic change:** a reader can no longer come away believing a candidate
passes through every state in order, or that debugging precedes improving.
**What it cost:** the `FailedApproach` label lost its `never HYPOTHESIS`
qualifier to the panel note. Instruction 03's order was followed — shorten
before shrinking.

---

## FIG-A · `aethrion_authority.svg` — the opening claim

| Concept | Verdict |
|---|---|
| **Current repository figure** | **Vetoed** on the count. "Seven plausible answers", followed by a list of eight components |
| **Package FIG21** | Concept accepted, wording not. Its framing — state-kind ownership rather than a count — is correct and is what was adopted |
| **Adopted** | The sentence now asks the question and refuses to answer it with a number: the invariant is one owner per *kind* of state, and the component count is an implementation detail that changes |

**Why the count was worse than wrong:** a reader who memorises "seven stores"
has memorised the thing that will be false next quarter, instead of the rule that
will still be true.

---

## FIG-N · Three figures that did not exist

The package's `05_NEW_VISUALS_RATIONALE.md` proposes ten additions. Three were
adopted; the rest were **rejected against the package's own test** — *do not add
a figure if it merely repeats prose without improving comprehension* — because
the corpus already carries their mechanism (collaboration, discovery, assurance,
memory, authority, waves).

| Adopted | Closes | Why prose was failing |
|---|---|---|
| `aethrion_disciplines.svg` | `ADR-012` | Its content is a **distinction**, and a distinction in prose reads as a glossary. Four ways of being wrong were being read as four synonyms |
| `aethrion_decision.svg` | `ADR-016` | Its content is an **ordering**, which prose is worst at making binding. "The human decides" was already true and said nothing about *when they were told what* |
| `aethrion_reproduction.svg` | `WP-157` | Its content is a set of **quiet paths**. A boundary diagram shows the routes an attacker must cross; the leaks that matter never cross one |

Each was checked against a live consumer before being drawn.
`aethrion_disciplines.svg` reads its pairs from `skills/_baseline/routing.json`,
so the figure and `check_skill_baseline.py` R3 cannot drift apart — the figure is
a projection of the fixture, not a second copy of it.

---

## FIG-F · The eight flow companions

The package ships eight inline Mermaid flows. **Five were vetoed and one was
adopted**, and the reason is the same for all of them: a flow that names an
object the architecture does not have is not a projection of the architecture,
it is a proposal wearing a diagram's clothes.

Each object name was checked against the corpus before the flow was considered.

| Flow | Objects it names | Present? | Disposition |
|---|---|---|---|
| `FLOW08` monitoring / supersession | `ClaimVersion`, `ImpactScan`, `SupersessionRecord` | all present | **ADOPTED**, adapted into `README.md` §3 |
| `FLOW01` request → project | `ResearchIntent` | **absent** | Vetoed — invented semantics |
| `FLOW03` cohort expansion | `CohortExpansionRequest` | **absent** | Vetoed — invented semantics |
| `FLOW05` review / rebuttal FSM | `REBUTTAL_OPEN`, `ARBITRATION_REQUIRED` | **absent** | Vetoed — the *concept* exists as `DisagreementCase` under WP-089, the named states do not |
| `FLOW02` gate authority | — | duplicate | Vetoed — `README.md` already carries the three-stage gate resolution |
| `FLOW04` candidate → value | — | duplicate | Vetoed — `aethrion_discovery.svg` carries the boundary this flattens |
| `FLOW06` tool intent | — | duplicate | Vetoed — `aethrion_trust.svg` carries the attack path to where it stops |
| `FLOW07` publication build | — | duplicate | Vetoed — `aethrion_reporting.svg` carries the authority question this omits |

**`FLOW05` is the interesting veto.** Its state machine is well-formed and the
mechanism it describes is real — this repository has `arbitrating-disagreement`,
a `DisagreementCase` object and a WP that owns it. What it does not have is a
review lifecycle with those five state names. Importing the diagram would have
created a schema by drawing it, and a later reader would have found a state
machine in the README with no contract behind it and reasonably assumed one
existed.

The gap it points at is real and is recorded rather than closed: **the review
lifecycle has no named states anywhere in the corpus.** That is a finding for
WP-088/WP-089 to answer, not something a figure should decide.

## Hard vetoes recorded, so the protocol is visibly binding

| Candidate | Veto |
|---|---|
| Keeping `Cedar` because two figures already said it | Wrong backend status. `ADR-010` is ACCEPTED and defers the engine |
| Keeping the discovery row because it laid out neatly | Stale architecture, misleading causality |
| Keeping "any warning is a failure" because it reads strongly | Status overclaim — every green run reports a library warning |
| A 5-card decision lane at the width that produced the best rhythm | Text overflow. Cards narrowed rather than text shrunk |

---

## What no record here can establish

Every figure above was inspected by the actor that produced it. `ADR-001` puts
R3 independent review out of reach for a solo operator, so **Phase 11 did not
run** — and a second self-review is not a substitute for it. These records say
what was compared and why one concept was chosen. They do not say that an
independent reviewer failed to find a defect, because none looked.
