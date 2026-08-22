# Writing — By Document Type

## 1. Claim strength is a vocabulary, not a style choice

The verb carries the epistemic claim. Choosing it loosely is how a measurement
becomes a law.

| Evidence | Permitted verbs |
|---|---|
| One measurement, one condition | *was observed* · *measured* · *in this configuration* |
| Repeated measurement, same setup | *shows* · *reproduces* |
| Correlation | *is associated with* · *co-occurs with* — **never** *causes* |
| Controlled comparison | *indicates* · *supports* |
| Preregistered confirmatory test | *demonstrates* — and only within the tested scope |
| Contrary result | *fails to support* · *is inconsistent with* |

**Novelty words require evidence or removal:** *novel · first · unique ·
state-of-the-art · superior · robust · comprehensive*. Each is a claim about the
literature, and a claim about the literature needs the literature.

## 2. Scientific writing

- **Uncertainty is preserved**, not smoothed. If a result holds under one
  condition, the condition travels with the sentence.
- **Precision follows the data.** Reporting six decimals from a
  three-significant-figure instrument is fabrication with extra steps.
- **Acronyms** are defined on first meaningful use unless the venue says otherwise.
- **Notation is exact** — variables, units, sub/superscripts, dimensional
  consistency. Equations are never invented to look rigorous.
- **Tense and voice follow venue and domain convention.** There is no universal rule.

### Generic-LLM prose to remove

Throat-clearing openings · "in today's rapidly evolving…" · repeated summary
sentences · exaggerated transitions · unsupported adjectives · marketing
language · manufactured certainty · a conclusion that restates the abstract.

Where detection is lexical and reliable, it becomes a Vale rule. Where it is a
judgement, it stays a review comment.

## 3. Technical and industrial R&D writing

**Do not force academic sections onto an engineering report.** Two working
topologies:

```
Executive summary → context → requirements → current state → method →
implementation → V&V → results → risks → open issues → recommendations →
decision requests → appendices
```

```
Problem → evidence → alternatives → trade-offs → recommendation →
implementation plan → risks
```

Every statement under **requirements, verification, results and deviations**
resolves to a source artifact: a requirement id, a test result, a design record,
an issue, a measurement, an `ExperimentRun`.

> **A deviation is not a limitation.** Rewording one as the other is the
> characteristic integrity failure of V&V reporting.

## 4. Thesis writing

A thesis is **not a journal article scaled to a hundred pages**. Method is
explained pedagogically, dead ends have a place, and the argument accumulates
across chapters.

Institutional regulations outrank every generic reference, including ISO 7144.
Support front matter, abstracts, acknowledgements, contents, lists of figures and
tables, nomenclature, abbreviations, declarations, appendices.

## 5. Literature synthesis

**A review is not a list of summaries.** Default to synthesis structures:
thematic · methodological · chronological · theoretical · evidence-strength ·
contradiction-and-gap · taxonomy.

Every synthesis statement resolves to the **set** of sources supporting it, and
disagreement between sources is reported as disagreement — not averaged into a
consensus that no source holds.

Systematic reviews additionally bind to the PRISMA contract already adopted.

## 6. Proposals

> **Planned work is never written in the past tense.**

Separate, visibly: what has been done · what is proposed · what is contingent.
A proposal that reads as though its results already exist is the single most
damaging error in this archetype, and it happens by tense alone.

## 7. Executive briefs

Compression must not remove the condition a result depends on. If the finding
holds only under one configuration, the brief says so in the same sentence —
brevity is not a licence to widen scope.
