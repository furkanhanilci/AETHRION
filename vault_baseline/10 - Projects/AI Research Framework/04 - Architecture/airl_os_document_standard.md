> [!info] Generated view
> This note is generated from `docs/DOCUMENT_STANDARD.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Document Standard

| Field | Value |
|---|---|
| Document type | Convention — how documents in this repository are written |
| Applies to | `README.md`, everything under `docs/`, `skills/README.md`, `planning/commissioning/**` |
| Status | **In force.** New documents conform; existing ones are brought into line when touched |
| Date | 2026-08-22 |

**In one paragraph.** Every document here states what it is, what it covers, and
how far it is from being true, before it says anything else. That last part is
the unusual one and the reason this standard exists: a corpus this large, about a
system this unbuilt, decays into something that reads as a description of
software that runs. The conventions below exist to keep description and
aspiration visibly separate.

---

## 1. Required structure

### 1.1 Front-matter table

Every document opens with a title and a field table:

```markdown
# Title

| Field | Value |
|---|---|
| Document type | reference · decision record · plan · convention · report |
| Scope | one line: what this covers, and what it does not |
| Sibling documents | the two or three a reader should know exist |
| Status | see §2 |
| Date | ISO date of last substantive change |
```

### 1.2 One-paragraph summary

Immediately after the table, **In one paragraph.** — the whole document
compressed. A reader who stops there should not be misled about anything.

### 1.3 Numbered sections

Top-level sections are numbered. Cross-references cite the number
(`AIRL_OS_ARCHITECTURE.md §6.1`) rather than a heading title, because titles
change and numbers survive the change or fail loudly.

### 1.4 Closing pointer table

Reference documents end with a table mapping *questions* to *files* — not a list
of links. A reader arrives with a question, not with a wish to browse.

---

## 2. Status vocabulary

Status is a controlled term, never prose. These are the only permitted values:

| Term | Means | May be claimed when |
|---|---|---|
| `WORKING` | Runs, verified locally | A command reproduces it from a clean checkout |
| `TECH_COMPLETE` | Built, not independently verified | Code exists and its own tests pass |
| `ACCEPTED` | An independent verifier accepted an evidence package | Never yet, in this repository |
| `SPECIFIED` | Written down in enough detail to build | A work package or schema exists |
| `PROPOSAL` | Argued for, awaiting a decision | — |
| `DESIGNED` | Described in the architecture, not scheduled | — |

A document that uses "done", "complete" or "ready" without one of these terms
behind it is out of conformance.

---

## 3. The honesty rules

These are what the standard is actually for.

1. **Distance is stated, never implied.** Any document describing a designed
   system says, in its own text, that it is designed. Diagrams carry the same
   obligation — a figure of an unbuilt system that does not mark it as unbuilt
   is the visual form of overclaiming.
2. **Counts are derived, not remembered.** Any number that can drift — packages,
   scenarios, skills, sealed files — is checked against the repository when the
   document is touched. Stale counts are the most common defect found in review.
3. **Tense matters.** A decision record describes the state at the time of the
   decision, in the past tense, and states the present state separately. A
   document rewritten to match the present stops being a record.
4. **Evidence is not edited.** Audits and verification reports are frozen at
   their date. Current state goes in a new dated document.
5. **A limitation section is mandatory** in any document describing a component.
   "Limits and open points" is not optional politeness; it is the part reviewers
   read first.

---

## 4. Formatting conventions

| Element | Convention |
|---|---|
| Emphasis | **Bold** for the load-bearing clause of a paragraph, at most one per paragraph |
| Callouts | `>` blockquote opening with a bold label — **Decision**, **Warning**, **Status**, **Open question** |
| Tables | For any comparison of three or more things across two or more attributes |
| Code blocks | Language-tagged. YAML for contracts, bash for commands, text for trees |
| Diagrams | Inline Mermaid when the diagram belongs to the text; a generated SVG under `docs/figures/` when precision or publication reproduction matters — see `docs/figures/README.md` |
| Line length | Wrapped near 80 columns, so diffs stay reviewable line by line |
| Terminology | One name per concept across the corpus. `EvidenceManifest`, never "evidence file" |

---

## 5. What is mechanically checked

Conventions that are not enforced decay. These are:

| Rule | Enforced by |
|---|---|
| Plan documents unchanged without a recorded re-seal | `sha256sum -c 00_PROGRAM/SHA256SUMS.txt` |
| Generated vault notes match their canonical source | `mirror_plan.py --check`, `mirror_vault.py --check` |
| Skill frontmatter and provenance | `scripts/validate_skills.py` |
| Figures match their generators, and text fits its box | `scripts/make_figures.py --check`, `scripts/check_figures.py` |

Everything else in this standard is currently enforced by review only, which is
an honest limitation rather than a plan.

---

## 6. Where to go next

| Question | File |
|---|---|
| What is this system? | `docs/architecture/AIRL_OS_ARCHITECTURE.md` |
| Who is accountable for what? | `docs/architecture/AIRL_OS_ROLES.md` |
| What is adopted rather than invented? | `docs/architecture/AIRL_OS_EXTERNAL_STANDARDS.md` |
| How are figures produced? | `docs/figures/README.md` |
| What is actually built? | `docs/review/2026-08-22_remediation_verification.md` |
