# Visual Completion — HEAD Delta Assessment

| Field | Value |
|---|---|
| Document type | Evidence — a dated assessment, frozen once written |
| Package | `AETHRION_VISUAL_ARCHITECTURE_COMPLETION`, 206 files, seal verified 206/206 |
| Package baseline | `5928ddd591cd1476cf6e142567489e1323f6328e` |
| Repository HEAD at assessment | `5928ddd` — **identical** |
| Date | 2026-08-23 |

**In one paragraph.** Phase 0 of the package's execution order requires pinning
HEAD and dispositioning every semantic assertion before a single candidate is
copied. HEAD and the package baseline are the same commit, so no assertion is
stale *by drift*. Several are stale for a different reason: the package was
written against a repository whose v1.3.1 work it could see, and three of its
findings had already been closed by that work. Those are dispositioned
`SUPERSEDED` with the evidence, not silently dropped.

## The package's own validators

`sha256sum -c PACKAGE_SHA256SUMS.txt` → **206/206 OK.**

`scripts/validate_package.py` and `scripts/validate_visuals.py` both require the
Graphviz `dot` binary, which is not installed here. They are recorded as **not
run**, with the reason, rather than reported as passing — the package's own
instruction 03 says the renderer must exit non-zero on layout failure, and a
renderer that is absent cannot do that.

The package's committed `VALIDATION_REPORT.txt` carries one finding of its own:
`FIG20.dot: long label line (55)`. It is a defect in a reference candidate, not
in this repository.

## Disposition of the fourteen-figure remediation matrix

Each verified by reading the **rendered SVG**, not the generator.

| Figure | Package verdict | Disposition | Evidence |
|---|---|---|---|
| `aethrion_stack.svg` | FAIL — Cedar named as selected | **CONFIRMED_AND_FIXED** | `("Cedar policy", DEP, False)` in the execution row; ADR-010 is ACCEPTED and says the bake-off has not run |
| `aethrion_trust.svg` | FAIL — Cedar as the decision point | **CONFIRMED_AND_FIXED** | Named in the policy box, the taxonomy sentence and the honest-limit note |
| `aethrion_evidence_chain.svg` | FAIL — count contradicts the generator | **CONFIRMED_AND_FIXED** | Caption said "nine of the ten links"; the chain marks two `working`, so eight are hollow |
| `aethrion_authority.svg` | FAIL — "seven stores" | **CONFIRMED_AND_FIXED** | The sentence said "seven plausible answers" and then listed **eight** components |
| `aethrion_topology.svg` | FAIL — vault wholesale disposable | **CONFIRMED_AND_FIXED** | Said the mirror "overwrites, so the failure mode of editing the vault is losing that edit" — finding **I10** had already made it refuse `generated: false` pages |
| `aethrion_discovery.svg` | FAIL/RESTRUCTURE — false linear chain | **CONFIRMED_AND_FIXED** | Four states drawn in a row with arrows, while `ADR-006` §2 draws a branch |
| `aethrion_verification.svg` | REVISE — "warning is fatal" ambiguous | **CONFIRMED_AND_FIXED** | Said "any warning is a failure; there is no advisory tier" while every green run reports `1 warning` from a library |
| `aethrion_lifecycle.svg` | REVISE — blanket "no model in G5" | **SUPERSEDED** | Split into `G5·D` / `G5·E` at baseline v1.3.1. `NO MODEL` survives only on the `G7a` row, where it is correct |
| `aethrion_waves.svg` | KEEP | **ALREADY_FIXED_EQUIVALENTLY** | Derived from the wave registry at v1.3.1; `check_figure_semantics.py` compares the rendered total to the package count |
| `aethrion_memory.svg` | KEEP — tighten wording | **NOT_APPLICABLE_WITH_EVIDENCE** | The suggested phrase "only Evidence is directly admissible" is absent because the figure already carries the constraint on its axes; adding the sentence would restate the diagram |
| `aethrion_assurance.svg` | KEEP/REFINE | **CONFIRMED_AND_FIXED** | The qualification turned out to have a defect behind it: the V0 row says *"same input, same answer, always"* and lists **reference resolution** among its examples — a check that asks a service whose answer changes the day a paper is retracted. It is repeatable for a pinned snapshot, not timeless. Also: the heading counted four questions beside a list of five |
| `aethrion_roles.svg` | REVISE — enforcement status | **CONFIRMED_AND_FIXED** | The card did not claim it; the closing paragraph did — *"the constraint is now enforced instead of argued about"*, while the engine that would admit or refuse a binding is WP-013 and is not built. Found by reading the rendered figure, not the card |
| `aethrion_reporting.svg` | REVISE — sequence connectors | **CONFIRMED_AND_FIXED** | Not a layout preference. The 3×3 grid carried arrows *within* each row and none between them, so the only thing telling a reader that stage 2 leads to stage 3 was the numbering — the audit's exact words, and exactly right |
| `aethrion_collaboration.svg` | KEEP/PROJECT | **STILL_VALID, deferred** | The publication projection is a real suggestion and is deferred with the reason: this repository has no publication venue and no rendering toolchain, so a 89 mm projection would be an artifact nothing consumes |

**Ten confirmed and fixed. One superseded. Two already equivalent or
inapplicable. One deferred with a reason.** Three of the four originally deferred
turned out to have real defects behind them, and all three were found by
*rendering the figure and looking at it* rather than by reading the generator. Nothing was accepted on the package's
authority; each was reproduced first.

## Two defects the package did not name

| Defect | How it was found |
|---|---|
| The **router Mermaid** in `README.md` said `SCIENTIFIC · 28` against a registry of **31** | Found while placing the disciplines figure beside it. A count inside a diagram label — the exact shape `check_doc_consistency.py` exists for, and the shape it kept missing because no rule named the pattern |
| `check_figures.py` printed the canvas **width** for every violation, including vertical ones | A figure whose content ran off the bottom reported an x-span comfortably inside a width it was not failing, sending the reader to widen a canvas that was already wide enough |

## What Phase 11 cannot be

The execution order requires an independent adversarial reviewer for each final
figure. `ADR-001` decides what is available to a solo operator: R1 solo, R2 under
a declared partial profile, **R3 `BLOCKED`**. There is no second person, so the
adversarial pass is **not run** and is recorded as such. Substituting a second
pass by the producing actor would be the kind of self-review this repository
exists to make impossible.
