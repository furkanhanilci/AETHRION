# ADR-013 — The Blackboard Is a Projection, and the Topology Is Sparse by Default

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | How agents exchange information, what that exchange is allowed to be, and why the default graph is not fully connected |
| Sibling documents | `ADR-011` · `ADR-014` · `ADR-005` (epistemic memory) · WP-149 · WP-150 · ACC-083 – ACC-088 |
| Status | **ACCEPTED — 2026-08-23.** Protocol decided; nothing is built |
| Date | 2026-08-23 |

**In one paragraph.** Keeping a cohort (`ADR-011`) means paying for its conversation, and a naive
cohort talks to itself quadratically: every agent to every agent, every round,
carrying full reasoning transcripts. Published work on communication pruning
reports large token reductions with small quality loss, and the useful reading of
that is not "use fewer agents" but "most of what they say to each other is
redundant." This record makes the exchange typed, sparse and delta-only, and
keeps it firmly outside the evidence path.

---

## 1. The decision

> **Inter-agent exchange is typed, sparse and delta-only, and it is never
> canonical state.** A `BlackboardEntry` carries a message type, artifact
> pointers and a change — not a transcript. The communication graph is compiled
> per task and is fully connected only in an explicit benchmark or control mode.
> **No blackboard entry may be promoted to evidence or to a claim.**

---

## 2. The blackboard is a projection

A shared workspace is genuinely useful for coordination: it lets an agent see
what has already been tried without asking. It is also the most tempting place in
the architecture to accidentally store truth, because it is where the interesting
sentences appear.

So the rule is structural rather than advisory: **delete the blackboard and no
canonical science is lost.** Everything that mattered is an `ArtifactRecord`, an
`EvidenceSpan`, a `ClaimVersion` or a `FindingRecord`; the entry pointed at it.

Three consequences follow:

- A `BlackboardEntry` is **not evidence** — ACC-085.
- There is **no path** from an entry to a `ClaimVersion`. Promotion goes through
  the evidence core like everything else.
- A `REFUTED` or `SUPERSEDED` entry is excluded from ordinary reasoning context
  by the memory mask, while staying visible to a failure-history query — the two
  are different questions and `ADR-005` already separates the stores that answer
  them.

---

## 3. Typed messages, and why free text was the problem

Ten types: `PROPOSAL`, `CHALLENGE`, `EVIDENCE`, `REQUEST`, `CORRECTION`,
`DISAGREEMENT`, `CONSENSUS_CANDIDATE`, `ABSTAIN`, `STATUS`, `BLOCKER`.

The type is what makes the exchange checkable. A `CHALLENGE` can be tracked to
resolution; a paragraph of prose containing an objection cannot, and the
objection is lost the moment someone summarises the thread. `ADR-011`'s
convergence rule — no unresolved material challenge — is only enforceable because
challenges are a type rather than a tone.

**Delta-only:** a message carries what changed, the evidence it points at and the
action it asks for. Large content goes to the artifact store and the message
carries a digest. This is not compression for its own sake — a transcript passed
between agents is also a channel for one agent's error to become another's
premise, which is `ADR-005` §6's concern arriving through a different door.

---

## 4. Sparse by default, with the baseline kept honest

The Task Compiler derives an initial topology from the task class, the scientific
phase, the roles, the evidence dependencies, the independence requirements and
the budget. Edges carry a policy: allowed message types, token ceiling, evidence
scope, visibility, security class.

Pruning happens on three axes, and none of them is the cohort:

| Axis | What is removed |
|---|---|
| **Spatial** | An edge between two roles that has never carried anything useful |
| **Temporal** | The assumption that every edge is used every round |
| **Semantic** | A viewpoint already expressed, restated |

**A quality guard, not a token target.** An optimisation is accepted only if the
quality delta stays within tolerance *and* coordination cost falls meaningfully.
A regression rolls the topology back — ACC-086, ACC-087. Measuring against a
single agent would flatter the result; the baseline is the **naive fully
connected cohort**, which is the thing actually being improved on.

**Two things a governor may never silence:** a `BLOCKER`, and any non-waivable
safety message. A low-utility edge carrying a blocker is still carrying a
blocker — ACC-088.

---

## 5. Consequences

**Accepted:** a compiled topology is a thing that can be compiled *wrongly*, and
a wrongly pruned edge is an agent that never hears something it needed.
ACC-086's quality guard is the detection mechanism, and it is a statistical one —
it will not catch a single unlucky omission.

**Accepted:** typed messages are more work to produce than prose, and models are
better at prose.

**Gained:** the coordination overhead ratio becomes a measurable number rather
than an intuition, which is what makes `ADR-011`'s cost argument answerable with
evidence instead of preference.

**Rejected:** a chat transcript as the collaboration record. It is the cheapest
option and it is unqueryable, unsummarisable without loss, and impossible to
audit for a dropped objection.

---

## 6. Decision

**Accepted, 2026-08-23.** The protocol is what WP-149 and WP-150 deliver.
**Nothing is built** — no blackboard, no topology compiler, no governor, and no
baseline harness to measure any of it against.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-006`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
