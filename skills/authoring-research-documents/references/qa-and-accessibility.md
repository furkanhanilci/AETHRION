# QA and Accessibility

Four QA passes, in this order. **Style polish never precedes scientific
checking** — a well-edited false sentence is harder to catch than a clumsy one.

## 1. Scientific QA

| Question | Fails when |
|---|---|
| Does every statement match its source artifact? | prose asserts more than the run recorded |
| Is every category correct? | an interpretation is written as an observation |
| Is scope preserved? | a condition present in the result is absent in the sentence |
| Is anything unsupported? | a sentence resolves to no claim |
| Are negative results present? | a null result in protocol scope is missing |

## 2. Statistical QA

Numbers in prose are checked against the artifacts that produced them: test
statistics recomputed, means checked for consistency with the reported sample
size and scale, uncertainty labelled with what it is — SD, SEM, 95 % CI, IQR —
and never mixed within one table or figure.

Validated implementations do this: **statcheck**, **grim**, **pysprite**. They
carry applicability conditions, and a check run outside its conditions produces a
wrong answer, not a weak one — see `AIRL_OS_IDEAL_STRUCTURE.md` B7.1.

> **A forensic flag is a flag.** It opens triage, never an accusation.

## 3. Reporting-guideline QA

Only the applicable guideline, at its recorded version. `none_applicable` is a
result, not a gap.

## 4. Language and style QA

| Tool | Authority |
|---|---|
| **Vale** | Deterministic lexical and structural rules — terminology, acronyms, placeholders, banned promotional language, heading conventions. Error severity only where detection is reliable |
| **LanguageTool** | Grammar and spelling, **local or licensed instance**; the public free endpoint's own documentation says not to send automated traffic |

> **A suggestion may never silently change technical meaning.** Every
> suggestion touching a number, unit, qualifier, hedge or technical term is
> reviewed individually. "The grammar checker changed it" is not a defence.

Subjective prose preferences are not hard errors. *"This discussion lacks
insight"* is a review comment, not a lint rule.

## 5. Accessibility

Separate contracts per output, and each claims only what was tested.

**HTML** — WCAG 2.2 where applicable: text alternatives, semantic headings,
real table structure, contrast, keyboard behaviour for interactive material.

**Figures** — alt text where the format supports it · a caption that carries the
message · **never colour as the only channel** · legible at final physical size.

**Tables** — semantic headers in HTML · logical structure · no table-as-layout.

**PDF** — when PDF/A or PDF/UA is requested, choose a renderer profile intended
to produce it and **validate the rendered artifact with veraPDF**, not the
renderer's configuration. Record the profile and the result.

> **Do not claim "accessible".** Record what was mechanically tested and what
> still needs human review. veraPDF passing proves machine-verifiable rules held;
> it does not prove a person can use the document.

## 6. Rendered-artifact QA

The source passing is not the artifact passing. Inspect the actual output:
references rendered · figures present and legible at size · tables not
overflowing · cross references resolved rather than showing `??` · limits
respected · no placeholder survived.

## 7. What may not be called "mechanically verified"

A regex that finds no `TODO` proves no `TODO` was found. It does not prove the
document is complete, correct, supported or publishable.
