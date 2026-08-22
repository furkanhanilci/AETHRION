---
title: "Figure Inventory and Design Specification"
cssclasses:
  - aethrion-reference
type: reference
category: architecture
status: WORKING
summary: "Figures here are generated artifacts, not drawings: the corpus is the source, the generator is version-controlled, and the SVG is reproducible from a clean checkout."
source: "docs/figures/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `docs/figures/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Figure Inventory and Design Specification

| Field | Value |
|---|---|
| Document type | Convention — figure inventory and design specification |
| Scope | The nine generated figures, their design system and their guarantees |
| Sibling documents | `../DOCUMENT_STANDARD.md` · `../architecture/AETHRION_ARCHITECTURE.md` · `../../skills/scientific-figures/SKILL.md` |
| Status | `WORKING` — figures are generated and mechanically checked |
| Date | 2026-08-22 |

**In one paragraph.** Figures here are generated artifacts, not drawings: the corpus is the source, the generator is version-controlled, and the SVG is reproducible from a clean checkout. There are nine of them rather than one per document, because a figure earns its place only by carrying a mechanism prose carries badly. Every string is measured against the box it sits in, and a figure that cannot be laid out honestly fails the build.

Figures here are **generated artifacts**, like the Obsidian mirrors and the
package catalogue. The canonical source is the architecture corpus; the
generator is version-controlled; the SVG is reproducible from a clean checkout.

```bash
python3 scripts/make_figures.py           # regenerate, then verify containment
python3 scripts/make_figures.py --check   # fail on drift
python3 scripts/check_figures.py          # verify containment alone
```

**Editing an SVG by hand is a defect.** Change the generator.

### The layout guarantee, and why it exists

The first figure set shipped with labels that overflowed their boxes. The check
in place at the time compared text against the **canvas**, so a string that
spilled out of a node but stayed on the page passed. That is a textbook case of
verifying the wrong invariant.

Two mechanisms now make it impossible:

1. **`figure_kit` measures text.** It carries the Helvetica advance-width table
   (units per 1000 em) and a 3 % safety margin, so `text_width` is a real
   measurement rather than a character count. `Canvas.cell` fits every string
   against the box's **inner** width: it wraps first, then shrinks toward the
   16-unit floor, and **raises** if the text still will not fit. A figure that
   cannot be laid out honestly fails the build instead of shipping clipped.
   The floor does not bend: three of the nine figures below were re-laid out
   during authoring because the kit refused a 15-unit label.
2. **`check_figures.py` re-measures the rendered SVG.** It parses the output,
   finds the tightest box enclosing each text anchor, and reports any string
   that escapes it. It deliberately does **not** trust the generator, so one bug
   cannot hide behind the same assumption twice.

`make_figures.py` runs both, so regeneration and verification cannot drift apart.

---

## 1. Why there are nine figures and not thirty

The temptation with a corpus this size is to put a diagram on every document.
That would produce exactly the failure mode a scientific-figure discipline warns
against: generic five-box flowcharts that pass the *"could this figure be used
for an unrelated project by changing the labels?"* test — which is the test a
figure must **fail** to be worth keeping.

So the inventory is deliberately short. A figure exists here only when it
carries a **mechanism** that prose carries badly:

| | Figure | Mechanism it carries | Prose alternative |
|---|---|---|---|
| 1 | `aethrion_lifecycle.svg` | Eleven gates × three actor classes, and the cells where no model is admitted | A table that hides the pattern |
| 2 | `aethrion_roles.svg` | Authority tiers, and constraint resolution replacing headcount | A list that reads as an org chart |
| 3 | `aethrion_evidence_chain.svg` | The chain, plus how much of it exists | A status table nobody cross-reads |
| 4 | `aethrion_stack.svg` | What is built here versus what is adopted, with the obligation each adoption type creates | A register nobody reads end to end |
| 5 | `aethrion_reporting.svg` | That formatting is downstream, and that no tool in the pipeline decides | A procedure list, which hides the authority question |
| 6 | `aethrion_waves.svg` | 141 packages in dependency order, against the one that has produced anything | A wave table that reads as progress |
| 7 | `aethrion_trust.svg` | Where an injected instruction stops, and on whose authority | A policy paragraph that never names the attack |
| 8 | `aethrion_verification.svg` | What each check proves *and* what it cannot see | A green dashboard, which is the failure mode |
| 9 | `aethrion_topology.svg` | Direction on every edge between repository, vault and the outside world | A prose claim that the mirror is one-way |

Figures 6–9 were added after the ADRs, the adoption matrix and the reporting
subsystem landed. Their absence was itself a defect: the corpus had grown four
structures that only prose described, and prose describes none of them well.

Everything else in the corpus uses inline Mermaid, which is editable in place,
renders in both GitHub and Obsidian, and does not need a build step. The rule:

> **SVG when precision and publication reproduction matter. Mermaid when the
> diagram belongs to the text it sits in.**

---

## 2. Design specification

Applied identically to all nine figures.

### Communication objective

Each figure states one five-second message, declared at the top of its
generator module. If a reader takes away only that sentence, the figure worked.

| Figure | Five-second message |
|---|---|
| 1 | Every gate resolves in the same order — mechanical first and unwaivable, then model production, then human authority — and three gates admit no model at all |
| 2 | Fourteen functions ordered by authority; a role is a function, so legality is decided by separation constraints, not headcount |
| 3 | A claim is admissible only if it resolves back to a source span and forward to a signed attestation — and one link of ten is implemented |
| 4 | Almost every layer is someone else's component; what this project owns is the control layer, and it is the least built part |
| 5 | A document is produced evidence-first and rendered last, and publication remains a human decision |
| 6 | 141 packages run in eleven waves behind one bootstrap package, and today exactly one of them has produced anything |
| 7 | A paper is data, never an instruction; the plane that can act never reads the plane a stranger can write |
| 8 | Ten checks keep the corpus honest about its own state; none of them can tell you whether the research is any good |
| 9 | The repository is the only place anything is authored; the vault is a one-way mirror; the outside world is read-only |

### Archetype selection

None of the nine is a generic left-to-right pipeline, because none of the
underlying structures is one.

- **Figure 1** is a **matrix**: gates on the vertical axis (time), actor class on
  the horizontal (authority). The interesting question at each gate is not "what
  comes next" but "who may act".
- **Figure 2** is an **authority ladder** plus a worked constraint resolution.
  Deliberately not an org chart — an org chart implies people, which is the
  misreading the figure exists to prevent.
- **Figure 3** is a **serpentine chain with a status channel**, plus an attached
  attestation sub-chain.
- **Figure 4** is a **layered stack with an ownership channel**, so "who is
  responsible for this layer" is answered by position, not by a legend.
- **Figure 5** is a **staged pipeline with an authority annotation** on the one
  stage that is not mechanical.
- **Figure 6** is a **dependency ladder with a progress channel** — explicitly
  not a Gantt chart, because the plan has no dates and drawing time it does not
  have would be an invention. Its package counts are **derived from the plan
  directory at generation time**, so the figure cannot disagree with the plan.
- **Figure 7** is a **two-lane separation diagram with one attack path** drawn to
  the point where it is cut. Two clean lanes with no adversary in them would
  flatter the design; the cut is the content.
- **Figure 8** is a **claim/evidence pairing with an explicit blind-spot
  column**. The blind spots are why it exists.
- **Figure 9** is a **source-of-truth topology with direction on every edge**.
  Direction is the content: a two-way sync would create a second place to be
  wrong in.

### Visual encoding

| Channel | Meaning | Notes |
|---|---|---|
| Position (column / tier / lane) | Actor class · authority tier · trust plane | The primary channel; survives greyscale |
| Colour | Kind of object — mechanical, model, human, artifact, revision | **Never** encodes status |
| Stroke pattern | Build status: solid = implemented, dashed = designed | Redundant with an explicit text label |
| Hatch fill | "No model admitted" | Redundant with the words in the cell |
| Stroke weight | Emphasis on a single decisive cell (G8 `DECIDES`, the `DENIED` step) | Used once per figure at most |
| Bar length | Package count, Figure 6 only | Labelled numerically beside every bar |

**Colour is never the only channel.** Every distinction is also carried by
position, pattern or text, so the figures survive colour-vision deficiency and
greyscale reproduction.

### Palette

Okabe–Ito, chosen for colour-vision safety:

| Hex | Role in these figures |
|---|---|
| `#009E73` | mechanical check |
| `#0072B2` | model production |
| `#D55E00` | human authority |
| `#E69F00` | frozen artifact |
| `#CC79A7` | revision / feedback path |
| `#1A1A1A` / `#6B6B6B` / `#C8C8C8` | ink, muted text, rules |

Background is pure `#FFFFFF`. Fills are the hue blended toward white so that
black body text keeps its contrast.

### Typography and final size

Canvas width is capped at **1200 user units**. Set to a 180 mm double-column
figure, one unit ≈ 0.425 pt, so the **minimum 16-unit text ≈ 6.8 pt**; at 190 mm
it clears 7 pt. Since the output is vector, reproduction at any size is exact —
but do not set these figures below 180 mm.

`scripts/make_figures.py` carries the minimum-font constant so the constraint is
recorded next to the code that must respect it.

### Exact-text control

Every visible string is taken from the architecture corpus. The generators
contain no invented module names, no invented metrics, and no invented
relationships. A figure that says something the corpus does not say is a defect,
not a design choice — which is also why the figures show *status* rather than
implying completeness.

Figure 6 goes one step further and **derives** its numbers by counting work
packages on disk. Derivation is preferable to transcription wherever the source
is machine-readable: a transcribed number is a claim that can go stale, and this
corpus already ships a scanner whose job is finding those.

### Output

SVG only, and deliberately: SVG is the vector master, renders natively in GitHub
and Obsidian, keeps text selectable and editable, and needs no rasteriser in the
toolchain. For a submission requiring PDF or high-DPI PNG:

```bash
rsvg-convert -f pdf -o lifecycle.pdf docs/figures/aethrion_lifecycle.svg
rsvg-convert -f png -d 600 -p 600 -o lifecycle.png docs/figures/aethrion_lifecycle.svg
```

Neither `librsvg` nor `cairosvg` is a project dependency; adding one to render a
figure is not worth a runtime dependency in a research bridge.

### Explicitly excluded

3-D effects · gradients · drop shadows · icon sets · rainbow palettes ·
decorative backgrounds · rounded "card" aesthetics · any element that does not
carry information.

---

## 3. Honesty constraint

Every figure marks what does not exist. Figure 1 carries a status line, Figure 2
names the resolved-but-partial independence decision, Figure 3 draws nine of its
ten links hollow, Figure 4 marks the control layer as the least built, Figure 6
labels exactly one wave as started, Figure 7 states that no policy set is
authored and no adversarial benchmark has been run, Figure 8 spends its closing
paragraph on what the bundle cannot see, and Figure 9 reports 27 of 33
references verified rather than a pass.

This is not modesty — it is the same rule the rest of the repository runs on: a
diagram that shows a designed system without marking it as designed is the
visual form of claiming an implementation that is not there.
