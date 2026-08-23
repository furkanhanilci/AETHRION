# ADR-017 — A Benchmark Run Is Firewalled, and Contamination Is a Label

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | How an external benchmark is run so that its score means something, and what is reported when it does not |
| Sibling documents | `AETHRION_COMPONENT_REUSE.md` §4 · `ADR-007` (frozen evaluator) · WP-158 · WP-043 · ACC-118 |
| Status | **ACCEPTED — 2026-08-23.** Policy decided; no benchmark has been run |
| Date | 2026-08-23 |

**In one paragraph.** This architecture leans on external benchmarks — they are the door external
truth comes through, and the register names a dozen. A benchmark score is only
worth having if the system could not have seen the answers, and for an agent with
web retrieval that is not a safe assumption: recent work shows deep-research
agents reaching public benchmark metadata, questions and answers through ordinary
search and inflating measured performance. This record firewalls the run and
makes contamination a reported label rather than a silent uplift.

---

## 1. The decision

> **A benchmark run freezes its dataset manifest, its network mode, its allowed
> domains and its evaluator isolation before it starts, and every retrieval is
> audited.** Where benchmark material appears in the search log, the run is
> labelled `CONTAMINATED` or `REVIEW_REQUIRED` and **its score is never reported
> as a clean score.**

---

## 2. Search-time contamination is the new part

Training-data contamination is well known and partly addressable by using recent
benchmarks. Search-time contamination is not: the agent retrieves the answer
during the run, from a leaderboard, a paper, a GitHub issue or a discussion
thread. Nothing about the model is contaminated. The measurement is.

The firewall is therefore about the run, not the model:

| Frozen before the run | Why |
|---|---|
| Dataset manifest digest | So the task set cannot drift between runs |
| Network mode and allowed domains | So retrieval scope is a decision, not an accident |
| Known benchmark identifiers | So the scanner knows what it is looking for |
| Evaluator isolation mode | So the grader is unreachable — `ADR-007` |
| Contamination policy | So the response to a hit is decided before there is a hit |

---

## 3. What the agent may never reach

Gold answers, private rubrics, hidden test splits, the grader prompt and the
evaluator source. This is `ADR-007`'s producer/evaluator boundary applied to
evaluation itself, and the reason it needs restating is that benchmark harnesses
routinely put the answer key one directory above the working tree.

**Contamination is reported, not corrected.** A contaminated run is not quietly
rerun until it comes back clean — that is the same selective-reporting failure
the architecture refuses everywhere else. The label travels with the score into
the release dossier.

---

## 4. The baseline that makes the efficiency claim meaningful

`ADR-011` keeps the cohort and `ADR-013` prunes its conversation, and the
resulting claim — *this is cheaper without being worse* — needs something to be
cheaper **than**.

**The baseline is the naive fully connected cohort**, not a single agent.
Comparing an optimised multi-agent system to one agent measures the cost of
having a cohort at all, which is a decision already taken on epistemic grounds
and not up for re-litigation on cost. Comparing it to an unpruned cohort measures
the optimisation, which is the thing actually being claimed.

Both arms run under the same firewall, the same dataset manifest and the same
budget, and the comparison is reported as a frontier — quality against cost —
rather than as a single number.

---

## 5. Consequences

**Accepted:** benchmark runs get slower and more constrained, and some benchmarks
will be unrunnable under a strict network mode. An unrunnable benchmark is
recorded as unrun.

**Accepted:** the scanner will produce false positives — a legitimate paper that
happens to discuss the benchmark. `REVIEW_REQUIRED` exists so that a human sorts
those rather than the pipeline guessing.

**Gained:** a reported score carries the conditions it was produced under, which
is the difference between a measurement and a number.

**Rejected:** running benchmarks with open retrieval and trusting the score. It
is what most reported agent numbers currently are, and it is why this record
exists.

---

## 6. Decision

**Accepted, 2026-08-23.** The firewall is what WP-158 delivers. **No benchmark in
the adoption register has been run** — not CoE Audit, not ResearchClawBench, not
AgentDojo, not any of the reproduction suites — so there is no score for this
policy to have protected yet.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-010`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
