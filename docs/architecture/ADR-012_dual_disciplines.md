# ADR-012 — Two Disciplines, Composable, Neither Collapsed Into the Other

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | The relationship between the software-engineering skill family and the scientific one, and why neither substitutes for the other |
| Sibling documents | `AETHRION_SKILL_LAYER.md` §14–§15 · `ADR-011` · WP-154 · WP-107 · ACC-103 · ACC-104 |
| Status | **ACCEPTED — 2026-08-23.** Separation decided; behaviour untested, as all 52 skills are |
| Date | 2026-08-23 |

**In one paragraph.** A research system that writes code needs two procedural disciplines, and they
are easy to conflate because their steps rhyme. Both plan before acting, both
have a moment of committing to a prediction, both end in review. They are not the
same, and the specific way they differ is that **a passing test says nothing
about whether a hypothesis is true, and a preregistered analysis says nothing
about whether the code is correct.** This record keeps them separate and
composable.

---

## 1. The decision

> **The engineering family and the scientific family are separate, composable
> families in one registry.** A task producing research code compiles both into
> one `TaskContract`. Neither is a renaming of the other, and no skill from one
> may be presented as satisfying an obligation of the other.

---

## 2. The four pairs that get conflated

| Engineering | Scientific | Why the substitution fails |
|---|---|---|
| `test-driven-development` | `preregistration-discipline` | A test fixes what the code must do; a preregistration fixes what a result will *mean*. Both commit before seeing an outcome, and that is where the resemblance stops. Passing tests on an analysis that was reshaped after seeing the data is a correct implementation of a compromised study |
| `requesting-code-review` | `requesting-review` · `adversarial-reviewing` | Code review asks *is this correct and maintainable*. Scientific review asks *does the evidence support the claim, and what would show it does not*. A reviewer who approves the diff has said nothing about the inference |
| `systematic-debugging` | `investigating-anomalies` | Debugging assumes the system is wrong and the expectation is right. Anomaly investigation cannot assume that — the surprising result may be the finding. Treating every anomaly as a bug is how a discovery gets fixed |
| `dispatching-parallel-agents` | `dispatching-parallel-analysts` | The first decomposes work that has one right answer. The second runs genuinely independent analyses **because** the answer is not known, and its output is a spread rather than a merge |

---

## 3. The double loop

```
SOFTWARE     design → plan → worktree → RED → implement → GREEN
                   → refactor → code review → verify → signed artifact
                                    │
                                    ▼  the artifact becomes eligible to run
SCIENCE      question → predict → freeze → experiment → observe
                   → assess → finding → claim
```

The junction is the only interesting part: a code artifact becomes **eligible to
produce scientific evidence** when the engineering loop has closed on it. Before
that it is a draft, and a result from a draft is a result from unknown code.

That is what WP-107's engineering vertical slice proves end to end, and what
`ADR-018` enforces afterwards — the frozen specification and the running code
have to still agree.

---

## 4. Why the engineering family is not absorbed

The first assimilation package made the scientific mechanisms very visible. The
predictable next step is to notice that eleven engineering skills look like
generic software practice and fold them into the scientific procedures that cite
them.

That would be wrong for a reason worth writing down: **most of what this system
will actually produce is code** — evaluators, preprocessing, simulation,
reproduction packages, analysis scripts. Every one of those is a place where an
ordinary software defect becomes a scientific error with a plausible number
attached. The engineering discipline is not supporting work around the science;
it is where a large fraction of the science's failure modes live.

The eleven remain vendored from `obra/superpowers` at a pinned commit, with
upstream attribution, and are not rewritten here.

---

## 5. Consequences

**Accepted:** two families is more registry surface, and the router has to
classify before it selects. `using-aethrion` already does that.

**Accepted:** a coding-science task loads more skills than either family alone,
which costs context. `ADR-013`'s context projection is the mitigation.

**Gained:** a reviewer can tell which discipline a finding belongs to, and route
it — `ADR-018`'s severity ladder depends on exactly that distinction.

**Rejected:** one merged procedure family. It reads simpler and it makes "the
tests pass" and "the result holds" the same sentence.

---

## 6. Decision

**Accepted, 2026-08-23.** Separation is preserved in the registry today —
engineering 11, scientific-research 31, shared 10 — and is enforced by
`validate_skills.py`. **No skill in either family has a behaviour baseline**;
WP-043 owns that and has not started.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-005`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
