---
title: "Producing Figures"
aliases:
  - "producing-figures"
type: skill
category: skill
status: WORKING
source: "skills/producing-figures/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/producing-figures/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: producing-figures
description: "Use when a figure, diagram, chart or graphical abstract is about to be made for a report, paper or architecture document; when choosing between a plot, a diagram and an illustration; or when a figure must be checked before publication"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G6,G9"
  airl.roles: "Scientific Editor,Scientific Owner,Research Software Engineer"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "false"
  airl.requires_skills: "scope-discipline,evidence-before-claim"
  airl.emits: "Figure,FigureSpecification"
  airl.mechanical_checks: "text_fits_its_box,every_visible_string_traceable_to_source,status_marked_on_designed_systems"
---

# Producing Figures

## Core principle

> **A figure is a claim in visual form.** Everything `evidence-before-claim` and
> `scope-discipline` require of a sentence, this skill requires of a picture.

Do not start by drawing. Do not start by picking colours. Do not start by
choosing matplotlib, SVG or Mermaid.

## Procedure

### 1. State the five-second message

Complete this sentence before anything else:

> *"A informed reader should understand within five seconds that ______."*

Everything in the figure serves that sentence. Anything that does not is
questioned and usually removed.

### 2. Decide whether a figure is warranted at all

A figure earns its place only by carrying a **mechanism that prose carries
badly**. Apply the originality test:

> *"Could this exact figure be used for an unrelated project by changing the
> labels?"* If yes, it is decoration — either redesign it so its topology
> reflects this work, or delete it and keep the prose.

### 3. Build the semantic model before the layout

List nodes, edges and groups, and mark each PRIMARY / SECONDARY / TERTIARY.
Classify the relationships — sequential, causal, hierarchical, comparative,
feedback — because **topology must follow the structure of the work**, not a
default left-to-right pipeline.

### 4. Choose the archetype from the structure, not from habit

| The work is… | The figure is… |
|---|---|
| Actors acting at stages | a matrix, not a pipeline |
| A chain with status | a chain with an explicit status channel |
| A hierarchy of authority | tiers, not an org chart |
| Exact numbers | a plot, with the chart type chosen from the comparison |
| Both structure and numbers | coordinated figures, not one crowded hybrid |

### 5. Choose the renderer from the content

| Content | Renderer |
|---|---|
| Exact numerical data, axes | matplotlib — deterministic, reproducible |
| Architecture precision, editable labels | **SVG, generated from code** |
| A diagram belonging to the text it sits in | inline Mermaid |
| Conceptual illustration | vector illustration |

**Never ask an image model to reproduce exact numbers** when deterministic
plotting is available.

### 6. Fix the exact-text allowlist

Write down every visible string **before** rendering, and take each from the
source material. Do not improvise terminology while drawing.

### 7. Encode, then check the encoding

- Colour is information. Restrained, colourblind-conscious palette.
- **Colour is never the only channel** — pair it with position, pattern, shape
  or text so the figure survives greyscale and colour-vision deficiency.
- Status is never encoded by colour alone.
- Every arrow means one thing, and that meaning is stated.

### 8. Design for the final size, and measure it

A figure that is legible at 1600 px and unreadable in a journal column has
failed. Compute the smallest text size at the intended physical width and check
it against the venue's floor.

## Iron rules

1. **Never invent a value, module, relationship, label or citation** to make a
   figure look complete. Missing information is omitted or marked missing.
2. **A figure of a designed system states that it is designed.** A diagram of an
   unbuilt architecture that does not mark it as unbuilt is the visual form of
   claiming an implementation that does not exist.
3. **Text must fit its box** — verified by measurement, not by eye.
4. **Figures are generated, not hand-drawn**, wherever the figure will be
   maintained. The generator is the source; editing output is a defect.

## Going deeper

`references/figure-methodology.md` carries the long form: the precedence order,
the archetype grammar, quantitative reasoning before chart choice, panel
structure, the semantic model, colour and typography rules, final-size
computation, concept exploration, the QA gates and the methodology sources.

## Mechanical verification

```bash
python3 scripts/make_figures.py --check   # generators match, text fits its box
python3 scripts/check_figures.py          # independent containment re-measurement
```

`docs/figures/README.md` holds this project's figure inventory, design system
and palette.

## Rationalization table

| What gets said | Ruling |
|---|---|
| "The label is only slightly clipped" | **No.** Clipped text is wrong text. Shrink, wrap, or resize the box |
| "Colour alone is fine, nobody prints greyscale" | **No.** Colour-vision deficiency is not about printing |
| "A placeholder number keeps the layout balanced" | **Never.** An invented number in a figure is a fabricated result |
| "Every document should have a diagram" | **No.** A figure that carries no mechanism is decoration |
| "It's obvious this part isn't built yet" | **It is not obvious to a reader.** Mark it |
| "I'll fix the SVG by hand, it's faster" | **That is the defect.** Fix the generator |

## Red flags

- Choosing the renderer before understanding the content
- A left-to-right pipeline for something that is not a pipeline
- Three cosmetic variants presented as three design concepts
- A caption that asserts more than the figure shows
- Any string in the figure that appears nowhere in the source material
