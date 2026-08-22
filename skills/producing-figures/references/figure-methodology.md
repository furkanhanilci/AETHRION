# Figure Methodology — The Long Form

Loaded when a figure is non-trivial. `SKILL.md` carries the procedure; this
carries the parts that only matter once you are deep in one.

## 1. The precedence order

When guidance conflicts, resolve **downward**, never upward:

1. **Scientific truth in the supplied material**
2. Target venue requirements
3. Statistical and scientific correctness
4. Communication clarity
5. Accessibility
6. Figure-generation methodology
7. Aesthetics

Aesthetics is last on purpose. A beautiful figure that misstates a result is a
worse artifact than an ugly one that does not.

## 2. The workflow, and its document counterpart

```
SCIENTIFIC UNDERSTANDING → COMMUNICATION OBJECTIVE → FIGURE INVENTORY →
FIGURE ARCHETYPE → SEMANTIC STRUCTURE → VISUAL ENCODING → RENDERER SELECTION →
DESIGN SYSTEM → IMPLEMENTATION → SCIENTIFIC QA → VISUAL QA → PUBLICATION QA
```

The same shape governs documents, which is why the two skills compose:

```
UNDERSTANDING → DOCUMENT OBJECTIVE → AUDIENCE → EVIDENCE INVENTORY →
CLAIM INVENTORY → ARCHETYPE → OUTLINE → NARRATIVE → DRAFT →
FIGURE/TABLE/EQUATION INVENTORY → RESOLUTION → SCIENTIFIC QA → STATISTICAL QA →
LANGUAGE QA → VENUE QA → RENDER → ARTIFACT QA → REVIEW → PACKAGE
```

## 3. Archetypes — the grammar, so the default is a choice

**Architecture** modular · layered · hierarchical · distributed · hub-and-spoke ·
multi-agent · subsystem topology.
**Process** linear · staged · branching · converging · iterative · cyclic ·
feedback · conditional.
**Mechanism** cause-effect · physical · interaction · transformation sequence ·
state transition · temporal.
**Comparison** baseline vs proposed · before/after · condition · success/failure.
**Experimental** setup · apparatus · simulation configuration · measurement.
**Analytical** mathematical framework · optimisation · probabilistic model.
**Hierarchical** taxonomy · classification tree.
**Temporal** timeline · lifecycle · evolution.
**Spatial** topology · layout · map.
**Quantitative** bar · grouped bar · dot · line · scatter · bubble · box ·
violin · histogram · KDE · ECDF · heatmap · slope · forest · Bland–Altman ·
calibration · ROC/PR · confusion matrix · parallel coordinates · small multiples.

## 4. Quantitative reasoning before any chart type

Classify each variable — categorical · ordinal · continuous · discrete ·
temporal · spatial · binary · probabilistic. Name the comparison — magnitude ·
ranking · trend · distribution · variability · uncertainty · correlation ·
composition · change over time · calibration · error. Identify the sample
structure — single · repeated · independent · paired · grouped · time series ·
aggregate.

| Goal | Prefer | Avoid |
|---|---|---|
| Magnitude | dot plot · bar where a zero baseline is meaningful | bars for non-zero-baseline quantities |
| Trend | line · small multiples | dual axes |
| Distribution | box · violin · ECDF · histogram, with points where n is small | a bar of means when the distribution exists |
| Relationship | scatter, with transparency under overplotting | a regression line the analysis does not support |
| Model comparison | grouped bars · point estimates · small multiples | radar charts by default |

**Uncertainty is drawn only if it was measured**, and the figure says which
quantity it is — SD, SEM, 95 % CI, IQR — never mixing them in one panel.
**Never invent error bars, p-values, significance brackets or intervals.**

## 5. Panel structure

Do not reach for `subplots(1, 2)` reflexively. Panels follow the information
hierarchy: one panel when there is one message; asymmetric layouts when one
element dominates; small multiples when the comparison is across conditions.
Panel labels `(a)`, `(b)`, `(c)` placed consistently, not competing with titles.

## 6. Semantic model before layout

Nodes — components, concepts, states, processes, entities, inputs, outputs.
Edges — information flow, physical transfer, causality, dependency, control,
feedback, transformation, temporal progression. Groups — context, inputs,
method, environment, validation, outputs. Every node marked PRIMARY, SECONDARY
or TERTIARY, and **layout reflects that hierarchy**: giving everything equal
prominence tells the reader nothing.

**Every arrow means exactly one thing, and it is stated.** Orthogonal routing,
gentle curves for feedback, consistent arrowheads, line style varied only when
semantics differ. No arrows through modules, no diagonal clutter.

## 7. Colour and typography

Restrained, colourblind-conscious, roughly 3–5 functional colours — more only if
the content genuinely has more categories. Okabe–Ito is a safe default palette
but is not applied mechanically to every figure.

**Colour is never the only channel.** Pair it with shape, line style, hatch,
position, luminance or annotation, so the figure survives greyscale and
colour-vision deficiency.

Background pure white unless a deviation is justified. Typography
publication-oriented, matching venue requirements where they exist.

## 8. Final-size legibility

Design at the intended physical width and **compute** the smallest text size
there. A figure legible at 1600 px and unreadable in a journal column has failed.
For this repository the constant lives in `scripts/make_figures.py`; at 180 mm a
16-unit minimum lands near 6.8 pt.

## 9. Concept exploration and the originality test

Generate at least **three genuinely different** concepts — architecture-centric,
storytelling-centric, mechanism-centric — not three cosmetic variants of one.
Score on scientific correctness, interpretability, density, hierarchy,
publication suitability, accessibility and originality.

> **Could this exact figure be reused for an unrelated project by changing the
> labels?** If yes, its topology does not reflect this work. Redesign or delete.

## 10. Chartjunk

No 3-D bars, bevels, gradients, drop shadows, glossy effects, heavy backgrounds,
decorative icons, rainbow palettes, clipart or oversized legends. For explanatory
figures also avoid generic SmartArt, marketing-infographic styling, giant rounded
cards and dashboard aesthetics.

## 11. QA gates

**Scientific** — every statement traceable to the source; every arrow a real
relationship; nothing invented. **Statistical** — scales not misleading, axis
truncation justified, ordering meaningful, aggregation not hiding variability.
**Visual** — alignment, spacing, hierarchy, line weights, routing, density.
**Accessibility** — colourblind and greyscale interpretable, contrast, readable
text, non-colour encodings present. **Publication** — legible at final size,
vector master where appropriate, venue requirements met.

## 12. Provenance

A figure reporting computational results points back to the data, the code and
the `ExperimentRun` that produced them. A figure is a claim in visual form, and a
claim carries its provenance.

## 13. Methodology sources

Recorded as **patterns**, with no code or text copied and licences unverified
until they are: Paper Framework Figure Studio Pro (semantic graph contract,
visible-text allowlist, negative constraints), Scientific Figure Generator
(topology matching), Academic Figure Skills (staged separation of content,
architecture, specification and palette), ResearchFigureSkill (evidence locking,
five-second message), Academic Figure Generator (editable diagram generation),
PaperBanana (retrieval → content planning → style planning → rendering →
self-critique → refinement), DiagramRAG (structural rather than cosmetic
reference matching).

> **A visual reference may inform layout, topology and visual grammar. It may
> never supply a missing scientific fact.**
