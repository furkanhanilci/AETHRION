# ADR-005 — Epistemic Memory Separation

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | What the system remembers, in how many places, and which of those may support a claim |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · WP-146 · WP-012 · ACC-70 · ACC-79 · ADR-007 |
| Status | **ACCEPTED — 2026-08-23.** Taxonomy decided; no store is built |
| Date | 2026-08-23 |

**In one paragraph.** The default design for an agent system is one long-term
memory: write everything the agent might later need into a vector store and
retrieve by similarity. That is the wrong shape here, and the reason has nothing
to do with retrieval quality. A raw evaluator output, a failed experiment, a
debugging lesson and a working scientific principle do not have the same
epistemic status — they differ in whether they may support a claim, whether they
may change, whether they may expire, and who may read them. A store that treats
them alike will eventually allow one to be used as another, and the specific
failure that ends in is a stale procedural note being cited as evidence.

---

## 1. The decision

> **There are six memories, not one.** Evidence · Finding · Search Experience ·
> Procedural · Principle · Human Intervention. Each has its own authority,
> mutability, retention and read policy. **Only the Evidence store may support a
> claim.** A retrieval request names the stores it is asking; a query across all
> of them by default is refused.

---

## 2. The six, and what distinguishes them

| Store | Immutable | Decays | May support a claim | Typical reader |
|---|:--:|:--:|---|---|
| **Evidence** | yes | never | **yes**, subject to admissibility | anyone with clearance |
| **Finding** | versioned | no | indirectly — a claim is drafted *from* a finding | reviewers, writers |
| **Search Experience** | append/version | yes, archivable | **no** | the search policy only |
| **Procedural** | versioned | yes, with revalidation | **no** | implementers |
| **Principle** | versioned | supersedable | **no** — a working belief is not a claim | ideation, review |
| **Human Intervention** | yes | never | as decision evidence only | audit, metascience |

### The two extremes define the design

**Evidence is immutable and content-addressed and never decays.** A source can be
retracted and its status changes; the bytes do not. That is not conservatism —
it is what makes G10 possible. A claim anchored to a retracted source must remain
traversable *after* the retraction, or the impact scan has nothing to walk.

**Procedural memory is the opposite.** "This library needs that flag" is true
about a version on a date, and it goes stale silently — no error, no signal, just
advice that quietly stopped applying. It is versioned, it expires, it is
revalidated, and it can never support a claim.

Putting these two in one store forces one of them into the wrong regime. Either
evidence becomes deletable, or procedural notes become permanent truth.

---

## 3. Why Finding is separate from Claim, and from Evidence

Three distinct things that a single "memory" collapses:

```
raw artifact ──► FindingRecord ──► ClaimVersion
 (what was      (what we think    (what the system
  observed)      it means)         asserts, after a gate)
```

Evidence is an observation. A finding is an interpretation of it — SUPPORTED,
REFUTED or INCONCLUSIVE, with scope and limitations. A claim is what survives
verification, review, reproduction and a human decision.

The load-bearing consequence: **revising an interpretation must not touch the
observation.** When review concludes a finding was wrong, the finding gains a
version and every raw digest is unchanged. ACC-78 tests exactly this, in both
directions — the revision succeeds, and a direct edit of the raw artifact is
refused.

---

## 4. Why Search Experience and Procedural memory exist at all

They are the two stores that make the system cheaper rather than more correct,
and that is why their authority is zero.

**Search Experience** answers *what has this campaign already tried?* — plan,
code artifact, metric, parent edges, mechanism tags, outcome. It is read by the
search policy to avoid re-walking dead ends. It is not read by a reviewer, and
that exclusion is a design requirement rather than a default (§6).

**Procedural memory** answers *how do we do this kind of thing?* Its
`FailedApproach` entries carry the distinction that gives them their value: a
method that could not be *applied* and a hypothesis that was *tested and not
supported* are different outcomes, and only the second is about the science. A
system that records both as "failed" will eventually report a compile error as a
refuted hypothesis — which ACC-64 exists to make impossible.

---

## 5. Why Principle uses a different status vocabulary

`PrincipleVersion` is PROPOSED, SUPPORTED, CHALLENGED or SUPERSEDED.
`ClaimVersion` is not. The vocabularies are deliberately disjoint so that no
reader — and no query — can confuse a working belief carrying a high posterior
with an accepted claim.

A principle is the thing underneath a hypothesis: the reason it looked worth
testing. It usually outlives several hypotheses, and when a result is surprising
the useful question is whether one hypothesis failed or whether something beneath
it is wrong. A model with only one layer cannot express that difference.

---

## 6. Memory is an independence question

Independence is normally treated as a question about *who* reviews. It is also a
question about *what the reviewer can read*.

A reviewer who can query the producer's search-experience memory inherits the
producer's dead ends and the producer's framing. The review is then anchored
rather than independent, and nothing in the record shows it — the reviewer is a
different actor, the profile says independent, and the contamination is invisible.

So a `MemoryQuery` carries the store, the task class, the assurance class and the
requesting role, and blind-review policy excludes the producer's search and
procedural memory by default. ACC-72 asserts this from the review side; ACC-79
asserts it from the retention side.

---

## 7. Where vector search fits

`pgvector`, OpenSearch and a graph projection are **derived read models** over
canonical stores. They make retrieval fast; they are not where anything lives,
and any of them can be dropped and rebuilt. ACC-71 requires exactly that rebuild
to be lossless.

Canonical epistemic state is PostgreSQL for structure and a content-addressed
object store for payloads. An embedding index that cannot be regenerated from
those two is a defect, not a store.

---

## 8. Consequences

**Accepted:** six contracts instead of one, and a retrieval API that is more
awkward to call because it makes the caller name what kind of thing it wants.
That awkwardness is the control.

**Accepted:** some knowledge does not fit cleanly, and forcing it into a store
decides its authority. Where the fit is genuinely unclear, the conservative
placement is Procedural — the store with no claim-supporting power.

**Gained:** "have we tried this before, and did it fail technically or
scientifically?" is answerable from records rather than from a chat log.

**Gained:** a retention job can be run at all. With one store it could never
safely delete anything, so nothing would ever be cleaned up and the store would
become an undifferentiated archive that is technically complete and practically
unusable.

**Rejected:** a single embedding store as canonical memory. Recorded here so the
question is not reopened as though it had never been asked.

---

## 9. Decision

**Accepted, 2026-08-23.** The taxonomy is decided and is the contract WP-146
delivers. **No store is implemented.** The Evidence store's first slice — the
`ArtifactRecord` DAG on immutable payloads — depends on WP-026, which does not
exist either.
