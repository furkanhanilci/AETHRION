# Venue Requirements and Reporting Guidelines

**Three different things, routinely conflated:**

| | Answers | Example |
|---|---|---|
| **Venue formatting requirements** | How must it look and how long may it be? | page limit, template, anonymisation |
| **Reporting guideline** | What must be reported for this study type? | PRISMA, CONSORT, TRIPOD+AI |
| **Scientific methodology** | Was the work sound? | neither of the above |

> **"PRISMA-compliant" does not mean the review is sound.** A reporting guideline
> is a *completeness* standard. Treating it as a quality standard is a category
> error that this file exists to prevent.

## Venue resolution

Every target gets a `VenueProfile`, and **nothing in it comes from memory**:

```yaml
VenueProfile:
  venue:
  article_type:
  source_url:
  retrieved_at:
  source_digest_or_version:
  template_source:
  template_digest:
  mandatory: [page_limit, abstract_limit, anonymisation, reference_style, ...]
  recommended: [...]
  venue_tooling: [...]     # e.g. template selectors, reference checkers, PDF checkers
  status: VERIFIED | UNVERIFIED_CURRENT_REQUIREMENT
```

**`UNVERIFIED_CURRENT_REQUIREMENT` blocks any compliance claim.** It does not
block drafting.

There is no single "IEEE style" or "Elsevier style" — requirements are per
journal and per article type, and they change. Where a venue publishes checking
tools, they are invoked rather than approximated.

## Guideline resolution

```
domain and study type
        ↓
does a guideline exist for this?
   ├── no  → none_applicable          ← a legitimate result
   └── yes → guideline · version · applicability rationale · checklist
```

**Scope caution.** The EQUATOR family is primarily health research. Importing
CONSORT into a robotics experiment because it sounds rigorous is a
misapplication, not diligence.

| Study type | Guideline |
|---|---|
| Systematic review | PRISMA 2020 · PRISMA-S · PRISMA-LSR |
| Randomised trial · protocol | CONSORT · SPIRIT |
| Observational | STROBE |
| Prediction model including ML | TRIPOD+AI |
| AI in medical imaging | CLAIM |
| Early clinical evaluation of AI decision support | DECIDE-AI |
| Diagnostic accuracy | STARD |
| Animal research | ARRIVE |
| Qualitative | COREQ · SRQR |
| Quality improvement | SQUIRE |
| Economic evaluation | CHEERS |

## AI/ML venue checklists

Some venues require their own checklist — reproducibility, transparency, ethics,
societal impact. It is loaded, versioned and applied **for that venue only**:

```
if target_venue has a required checklist:
        load current version · map applicable items
else:
        do not require it
```

A venue checklist is a **venue requirement**, never a universal AIRL scientific
standard, and copying one into the framework as though it were would repeat the
category error at the top of this file.

## Structural references

**ANSI/NISO Z39.18** for scientific and technical reports and **ISO 7144** for
theses are structural references. Both are old; institutional, customer and
accessibility requirements override them.
