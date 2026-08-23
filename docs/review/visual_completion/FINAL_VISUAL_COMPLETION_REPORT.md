# Final Visual Completion Report

| Field | Value |
|---|---|
| Document type | Evidence — dated, frozen once written |
| Package | `AETHRION_VISUAL_ARCHITECTURE_COMPLETION` · seal 206/206 verified |
| Package baseline | `5928ddd` — identical to HEAD at start |
| Figures before → after | **14 → 17** |
| Date | 2026-08-23 |

**In one paragraph.** Seven figures were teaching something the repository had
decided against — two named a policy engine the accepted ADR declines to select,
one understated how much of the evidence chain is built, one carried a count that
did not match its own list, one described a data-loss behaviour the code had been
changed to prevent, one drew a branch as a sequence, and one claimed a strictness
the bundle does not have. Each was repaired at its generator, the prose and
Mermaid that taught the same thing were repaired with it, and three semantic
checks were added so the class cannot recur silently.

## Old → new mapping

| Figure | Change | Was |
|---|---|---|
| `aethrion_stack.svg` | backend-neutral | `Cedar policy` in the execution row |
| `aethrion_trust.svg` | backend-neutral | `Cedar` as the decision point, in three places |
| `aethrion_evidence_chain.svg` | count **derived** | "nine of the ten links" against a chain marking two as working |
| `aethrion_authority.svg` | count → invariant | "seven plausible answers", followed by eight components |
| `aethrion_topology.svg` | matches the code | "the mirror overwrites, so the failure mode of editing the vault is losing that edit" |
| `aethrion_discovery.svg` | row → **branch** | `DRAFT → DEBUG → IMPROVE → FUSE` as a mandatory sequence |
| `aethrion_verification.svg` | scope qualified | "any warning is a failure; there is no advisory tier" |
| **`aethrion_disciplines.svg`** | **new** | `ADR-012` had no figure |
| **`aethrion_decision.svg`** | **new** | `ADR-016` had no figure |
| **`aethrion_reproduction.svg`** | **new** | `WP-157`'s zones had no figure |

Nothing was removed. `waves`, `memory`, `assurance`, `roles`, `reporting`,
`collaboration` and `lifecycle` were verified and kept, four of them with
package suggestions deferred and the reasons recorded in
[`00_head_delta_assessment.md`](00_head_delta_assessment.md).

## Prose and Mermaid repaired alongside

The package's binding rule: *a figure remediation is incomplete if the same
document still contains an inline Mermaid or caption that teaches the old
semantics.*

| Surface | Repair |
|---|---|
| `README.md` Figure 9 caption | said the vault is never edited back; now names the `generated: false` protection |
| `README.md` Figure 2 caption | carried the hollow count; the count now lives only in the figure, derived |
| `README.md` Figure 10 caption | now leads with the branch, not only the boundary |
| `README.md` router Mermaid | `SCIENTIFIC · 28` against a registry of **31** |
| `README.md` gate table | `G5` was one row; now `G5·D` and `G5·E` |
| `README.md` §3 | gained the G10 supersession flow — the judgement the lifecycle diagram's dashed edge skips |
| `AETHRION_ARCHITECTURE.md` lifecycle Mermaid | `G5 … no model in the loop` → two nodes, with the orphaned `style G5` rule repaired |
| `AETHRION_ARCHITECTURE.md` Figure 1 caption | described the pre-split figure |
| `docs/figures/README.md` | three new rows; the topology and discovery rows rewritten; the "cannot disagree because generated" guarantee replaced |

## The guarantee sentence that had to change

`docs/figures/README.md` said Figure 6's counts were *"derived from the plan
directory at generation time, so the figure cannot disagree with the plan."*

The counts were genuinely derived — through a wave table that ended at `WP-140`,
so nineteen packages fell outside every range and were counted by nothing.
**Derived is not the same as true.** A generator that asks the wrong question
reproduces the wrong answer perfectly. The guarantee is now two independent
paths meeting at an assertion, which is a claim that can fail.

## New checks, and the defects they were made to catch

Acceptance criterion 17 requires the semantic checks to fail on a planted
stale-backend / stale-status / stale-relationship fixture. Three rules were
added to `check_figure_semantics.py`, and all four historical defects are
planted in its self-test:

| Rule | Catches |
|---|---|
| `check_policy_backend_neutrality` | any figure naming a policy engine while `ADR-010` declines to select one |
| `check_evidence_chain_is_self_consistent` | a hollow count that no longer matches the figure's own `working` labels |
| `check_mirror_description_matches_the_code` | a figure describing mirror behaviour the code refuses |

Plus three derived-count rules in `check_doc_consistency.py` for the per-family
skill counts, because the drift that produced `SCIENTIFIC · 28` was a number
inside a diagram label — the shape this checker exists for and the shape it kept
missing.

**One of the new rules had the defect it was written to catch.** The policy guard
searched the raw ADR for a contiguous phrase; the binding sentence is
`**The bake-off\nhas not run**`, wrapped and bolded, so the search found nothing
and the rule concluded the ADR permitted naming an engine. It now normalises
whitespace and keys on the ADR's own binding sentence. That is the fourth time
in four passes a first-draft control has carried the defect it was built to find,
and the fourth time a planted mutation found it before the corpus did.

## Commands run, with their real output

```text
sha256sum -c PACKAGE_SHA256SUMS.txt          206/206 OK
uv run python scripts/write_status.py        20/20 checks pass
uv run pytest                                149 passed
python3 scripts/check_figures.py             17 figures checked, 0 overflow(s)
python3 scripts/check_figure_semantics.py    4 derived claims · no contradictions
python3 scripts/check_figure_semantics.py --self-test
                                             4 registry mutations and 4 planted
                                             figure defects · 0 produced no finding
python3 scripts/check_document_hygiene.py    748 documents · 0 structural defects
python3 scripts/check_doc_consistency.py     documents agree with the repository
```

## Final-size classification

Every figure in this corpus is **architecture / reference-only**. None is a
publication projection and none is claimed to be one.

The package asks for 180 mm and 89 mm previews. They are **not produced**, and
the reason is not effort: this repository has no rendering toolchain installed
and no publication venue, so a 89 mm PNG would be an artifact nothing consumes
and no one has inspected. `delivery/specimen/README.md` already records that
nothing here has ever been rendered. Producing a preview and calling it
final-size QA would be the kind of evidence-shaped output the corpus exists to
refuse.

What *is* enforced at generation time is stricter than a preview: `figure_kit`
raises rather than shrinking any string below a 16-unit legibility floor, and it
refused two labels during this pass. Both were shortened, which is the order
instruction 03 requires.

## Unresolved limitations

- **Phase 11 did not run.** The execution order requires an independent
  adversarial reviewer per figure. `ADR-001` puts that out of reach for a solo
  operator — R3 is `BLOCKED`, declared rather than waived. Every figure here was
  inspected by the actor that produced it, and a second self-review is not a
  substitute.
- **The package's own validators did not run.** Both need Graphviz `dot`, which
  is not installed. Recorded as unavailable, not as passing.
- **No publication projection exists**, per the classification above.
- **The review lifecycle has no named states** anywhere in the corpus. `FLOW05`
  pointed at this and was vetoed rather than allowed to invent them. It is a gap
  for WP-088/WP-089, not something a figure should decide.
- **Four package suggestions are deferred with reasons**, not silently dropped:
  the assurance determinism wording, the roles enforcement note, the reporting
  connectors, and the collaboration publication projection.

## What this report does not claim

The corpus is not "complete". Seventeen figures carry seventeen mechanisms, three
mechanical rules now compare a figure's claims to the decisions it describes, and
the cross-representation contradictions the audit named are closed. A figure can
still draw the wrong arrow, explain a mechanism badly, or be beautiful and
useless — and nothing here would notice.
