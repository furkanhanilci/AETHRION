> [!info] Generated view
> This note is generated from `docs/figures/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Figure Inventory and Design Specification

Figures here are **generated artifacts**, like the Obsidian mirrors and the
package catalogue. The canonical source is the architecture corpus; the
generator is version-controlled; the SVG is reproducible from a clean checkout.

```bash
python3 scripts/make_figures.py           # regenerate
python3 scripts/make_figures.py --check   # fail on drift
```

**Editing an SVG by hand is a defect.** Change the generator.

---

## 1. Why there are three figures and not thirty

The temptation with a corpus this size is to put a diagram on every document.
That would produce exactly the failure mode a scientific-figure discipline warns
against: generic five-box flowcharts that pass the *"could this figure be used
for an unrelated project by changing the labels?"* test — which is the test a
figure must **fail** to be worth keeping.

So the inventory is deliberately short. A figure exists here only when it
carries a **mechanism** that prose carries badly:

| | Figure | Mechanism it carries | Prose alternative |
|---|---|---|---|
| 1 | `airl_os_lifecycle.svg` | Eleven gates × three actor classes, and the cells where no model is admitted | A table that hides the pattern |
| 2 | `airl_os_roles.svg` | Authority tiers, and constraint resolution replacing headcount | A list that reads as an org chart |
| 3 | `airl_os_evidence_chain.svg` | The chain, plus how much of it exists | A status table nobody cross-reads |

Everything else in the corpus uses inline Mermaid, which is editable in place,
renders in both GitHub and Obsidian, and does not need a build step. The rule:

> **SVG when precision and publication reproduction matter. Mermaid when the
> diagram belongs to the text it sits in.**

---

## 2. Design specification

Applied identically to all three figures.

### Communication objective

Each figure states one five-second message, declared at the top of its
generator module. If a reader takes away only that sentence, the figure worked.

| Figure | Five-second message |
|---|---|
| 1 | Every gate resolves in the same order — mechanical first and unwaivable, then model production, then human authority — and three gates admit no model at all |
| 2 | Fourteen functions ordered by authority; a role is a function, so legality is decided by separation constraints, not headcount |
| 3 | A claim is admissible only if it resolves back to a source span and forward to a signed attestation — and one link of ten is implemented |

### Archetype selection

None of the three is a left-to-right pipeline, because none of the underlying
structures is one.

- **Figure 1** is a **matrix**: gates on the vertical axis (time), actor class on
  the horizontal (authority). The interesting question at each gate is not "what
  comes next" but "who may act".
- **Figure 2** is an **authority ladder** plus a worked constraint resolution.
  Deliberately not an org chart — an org chart implies people, which is the
  misreading the figure exists to prevent.
- **Figure 3** is a **serpentine chain with a status channel**, plus an attached
  attestation sub-chain.

### Visual encoding

| Channel | Meaning | Notes |
|---|---|---|
| Position (column / tier) | Actor class · authority tier | The primary channel; survives greyscale |
| Colour | Kind of object — mechanical, model, human, artifact, revision | **Never** encodes status |
| Stroke pattern | Build status: solid = implemented, dashed = designed | Redundant with an explicit text label |
| Hatch fill | "No model admitted" | Redundant with the words in the cell |
| Stroke weight | Emphasis on a single decisive cell (G8 `DECIDES`) | Used once per figure at most |

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

### Output

SVG only, and deliberately: SVG is the vector master, renders natively in GitHub
and Obsidian, keeps text selectable and editable, and needs no rasteriser in the
toolchain. For a submission requiring PDF or high-DPI PNG:

```bash
rsvg-convert -f pdf -o lifecycle.pdf docs/figures/airl_os_lifecycle.svg
rsvg-convert -f png -d 600 -p 600 -o lifecycle.png docs/figures/airl_os_lifecycle.svg
```

Neither `librsvg` nor `cairosvg` is a project dependency; adding one to render a
figure is not worth a runtime dependency in a research bridge.

### Explicitly excluded

3-D effects · gradients · drop shadows · icon sets · rainbow palettes ·
decorative backgrounds · rounded "card" aesthetics · any element that does not
carry information.

---

## 3. Honesty constraint

All three figures mark what does not exist. Figure 1 carries a status line,
Figure 2 names the open C2 decision, and Figure 3 draws nine of its ten links
hollow.

This is not modesty — it is the same rule the rest of the repository runs on: a
diagram that shows a designed system without marking it as designed is the
visual form of claiming an implementation that is not there.
