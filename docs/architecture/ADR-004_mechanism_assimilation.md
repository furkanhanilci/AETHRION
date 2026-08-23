# ADR-004 — Mechanism Assimilation and Upstream Lineage

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | How a mechanism from another project enters this architecture, and what that costs |
| Sibling documents | `AETHRION_COMPONENT_REUSE.md` (what is adopted) · `AETHRION_RELATED_SYSTEMS.md` (from whom) · `../../provenance/README.md` (the register) · **`ADR-019`, which extends this record with the supply-chain toolchain** · WP-141 · ACC-73 · ACC-74 |
| Status | **ACCEPTED — 2026-08-23.** Register and checker exist; no mechanism has been adapted yet |
| Date | 2026-08-23 |

**In one paragraph.** Most of what a research system needs has been solved
somewhere before — a candidate search tree, a budget governor, an artifact
lineage graph, a review state machine. Writing each of them here for the first
time produces a worse version of a thing that already exists. But importing
another project's mechanism imports its architecture unless something stops it,
and importing its architecture is how a system becomes a collection of other
people's systems. This record fixes the terms: mechanisms are taken, product
identities are not, and taking one is an auditable act with a pin, a licence read
at the source, a characterisation suite and a stated authority boundary.

---

## 1. The decision

> **A mechanism may be taken. An architecture may not.** Every assimilated
> mechanism is recorded in `provenance/upstreams.json` with its upstream, its
> licence, what was deliberately *not* taken, and **what the mechanism may never
> decide**. Code is copied only under a permissive licence, from a pinned commit,
> behind a characterisation suite written first. Where any of those is missing,
> the mechanism is specified and reimplemented instead.

---

## 2. What "not an architecture" means concretely

The rule is easy to agree with and easy to violate, so it is stated as an
observable property of the repository rather than as an intention:

**No external project appears as a runtime module, a directory, a backend, a
class name or a configuration key.** There is no `src/third_party/`, no
capability interface whose implementations are named after other systems, and no
document describing an external system as part of the running architecture.

What arrives instead is a mechanism expressed in this system's own vocabulary. A
candidate node becomes a `SearchNode` bound to an `ArtifactRecord`; a scalar
score becomes a `VerifiedValue` bound to a `RawEvaluatorArtifact`; a budget
counter becomes a `ResearchBudgetContract` whose exhaustion is a
`CampaignStopRecord` that satisfies no gate.

That last substitution is the point. Upstream, a stopped search is a loop that
ended. Here it has to be a record that explicitly is not an acceptance, because
this system's failure mode is a plausible result being read as a verified one.

### Where upstream identity does live

In `NOTICE`, in `provenance/upstreams.json`, in SPDX headers on any adapted
file, and in `AETHRION_RELATED_SYSTEMS.md`. Engineering lineage stays visible and
attributable. It is simply not part of what the system *is*.

---

## 3. The three decisions, and what each obliges

| Decision | When | Obligation |
|---|---|---|
| **DIRECT_ADAPT** | Permissive licence · small dependency closure · behaviour isolable and testable · low architectural contamination | Pinned commit · named file list · characterisation suite **written before the code moves** · SPDX and `NOTICE` · behaviour-equivalence tests |
| **ADAPTIVE_REIMPLEMENT** | The idea is strong but the code brings its storage, orchestration or authority model with it | A written mechanism specification — inputs, outputs, states, invariants, failure conditions, forbidden behaviour — before any implementation |
| **DEPENDENCY** | Mature infrastructure whose reimplementation would be worse and less safe | Version pinning, upgrade path, failure semantics |

A permissive licence makes copying **legal**. It does not make copying
**correct**, and the register contains several entries that are permissively
licensed and still reimplemented — because a native contract mattered more than
saving the implementation time.

### The rule that runs in both directions

`check_upstream_lineage.py` refuses a `DIRECT_ADAPT` entry that reaches
`ADAPTING` without a pin, a file list, a characterisation suite and a permissive
licence. It **also** refuses an `ADAPTIVE_REIMPLEMENT` entry that names source
files: if files were copied, the decision was direct adaptation, and calling it a
reimplementation is how a licence obligation goes unrecorded.

---

## 4. Why the characterisation suite comes first

A characterisation suite written *after* adaptation tests what the local code
does. Written *before*, it tests what the upstream code did — which is the only
thing that makes the two comparable.

This matters twice. It matters when the local version is written, because
divergence then becomes a visible decision rather than an accident. And it
matters years later, when upstream fixes a bug in code that was copied here: the
suite is what answers *does that fix apply to us?* Without it, the honest answer
is that nobody can tell.

---

## 5. Why every entry states what the mechanism may never decide

Every other supply-chain control in this programme asks whether a component is
what it claims to be. This one asks a different question, and it is the question
specific to a research system: **has this mechanism quietly acquired authority?**

The failure is not hypothetical, and the register records real instances of it
being refused:

- A search selection score is a compute allocation. Written into a claim
  assessment, it becomes a confidence nobody measured.
- A retrieval sufficiency assessment is a model's opinion that it has read
  enough. Treated as a stopping rule, it lets a confirmatory campaign stop when
  the evidence became favourable.
- An artifact-need broadcast is a coordination signal. Given the power to start
  work, it becomes an autonomous research loop with no gate in it.
- An `auto_proceed_on_timeout` flag is a convenience. At a mandatory human gate
  it is the end of human authority, which is why the capability is absent here
  rather than defaulted to false.

So `authority_boundary` is a required field, and an entry without one fails the
checker.

---

## 6. Consequences

**Accepted:** adaptation is slower than copying. A pin, a licence read, a suite
and a specification are real work before any behaviour exists.

**Accepted:** the register will contain entries that are never used. Recording a
decision not to take something is the cheaper half of not re-examining it every
six months, which is why `DEFER` and `REJECT` are first-class states with stated
reasons.

**Gained:** upstream drift becomes detectable rather than invisible — ACC-73.

**Gained:** the licence position is a file, not a memory — ACC-74.

**Gained:** "AETHRION adapted this" is a checkable statement. The checker's
`--self-test` injects a defect per rule and fails if any rule stays silent, so a
clean run means the rules can fire, not merely that nobody looked.

---

## 7. What this record does not decide

It does not decide **which** mechanisms are worth taking; that is
`AETHRION_COMPONENT_REUSE.md` and the register. It does not license copying under
any licence a scanner has not read. And it does not make an adapted mechanism
correct — a characterisation suite proves the local version behaves like the
upstream one, which is a different claim from the upstream one being right.

---

## 7.1 What this record leaves open, and where it is decided

This record fixes the **rules** for taking a mechanism. It names no tools, and it
does not say how adapted source joins the same supply chain as an installed
dependency — which matters, because adapted source has no package-manager entry
and is invisible to every ordinary scanner.

[`ADR-019`](ADR-019_supply_chain_and_upstream_standard.md) decides both: SPDX and
REUSE for licence, OSV-Scanner and OpenSSF Scorecard for posture, SLSA and
Sigstore for provenance, and admission of adapted files through the same gate as
a dependency. The rules below are unchanged; that record is the machinery.

---

## 8. Decision

**Accepted, 2026-08-23.** The register and its checker exist and are in the
verification bundle. **No entry has reached `ADAPTING`** — every decision is
currently on paper, `pinned_commit` is `null` throughout, and the rules that
demand a pin begin to bite at the moment the first line of code moves.

Reopened if: a licence position turns out to have been read wrongly; an
upstream's terms change in a way that affects an adapted file; or the register
grows large enough that per-entry review stops happening, which would make it a
list rather than a control.
