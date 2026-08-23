# ADR-014 — One Canonical Authority Per Kind of State

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Which store owns which truth, and what happens when a projection disagrees with it |
| Sibling documents | `AETHRION_ARCHITECTURE.md` §4 · `ADR-005` · WP-159 · WP-030 · ACC-119 · ACC-012 · ACC-034 |
| Status | **ACCEPTED — 2026-08-23.** Authority matrix decided; only one of its stores exists |
| Date | 2026-08-23 |

**In one paragraph.** A system with a workflow engine, a relational store, an object store, an event
bus, a graph projection, a vector index and two human workspaces has seven
plausible answers to "where does this live?". Split brain does not usually arrive
as a dramatic failure — it arrives as a projection that is subtly ahead of the
store it projects, read by something that trusts it. This record assigns exactly
one authority per kind of state and makes everything else rebuildable.

---

## 1. The decision

> **Each kind of state has exactly one canonical owner, and everything else is a
> rebuildable projection.** An event payload never becomes truth. A derived index
> is never read as authority. **Dropping every projection and rebuilding it must
> lose nothing** — and that is a test, not an aspiration.

---

## 2. The matrix

| State | Canonical owner | Everything else |
|---|---|---|
| Gate and lifecycle position | **Temporal** | An event announcing a transition is a notification |
| Scientific domain records | **PostgreSQL** | Neo4j, pgvector and OpenSearch project it |
| Artifact bytes and digests | **Immutable object store** | Any local copy is a cache |
| Human decisions | **Signed `DecisionRecord`** | A message about a decision is not one |
| Cognitive scratch state | **LangGraph, bounded to one task** | It cannot transition a gate |
| Experiment telemetry | **MLflow** | Operational only — never a scientific result |
| Literature working surface | **Zotero**, human-owned regions respected | The Source Registry owns bibliographic identity |
| Human synthesis surface | **Obsidian**, human-owned regions respected | Generated regions are projections and say so |

The line that does the most work: **MLflow answers what the system did;
`EvidenceManifest` plus the run registry answer what may be believed.**

---

## 3. The write path

A canonical transaction and its outbox record commit **atomically**. The
publisher reads the outbox afterwards. A consumer never promotes a payload to
truth — it validates identity and version and re-reads canonical state.

This ordering is the whole mechanism, and getting it backwards is the standard
way a distributed system acquires two truths: publish first, commit second, and
a crash between them leaves an event describing something that never happened.

---

## 4. The tests, because this is a class of bug that hides

Split brain is invisible in a healthy system and obvious only in a post-mortem.
It is therefore specified as an injection suite rather than as a property:

- kill the publisher after the database commit;
- deliver the same event twice;
- deliver events out of order;
- return a LangGraph result after its task was cancelled;
- delete a Neo4j projection and rebuild it — ACC-119;
- restart a service and replay a Temporal workflow;
- attempt two concurrent gate transitions on one project.

Every one must end with canonical state correct and the projection agreeing with
it, or with an explicit, recorded failure. **A silent divergence is the failure.**

---

## 5. Correlation, or none of the above is diagnosable

One correlation chain spans project, gate, task, agent, model, tool, artifact,
run and claim identifiers, carried on OpenTelemetry spans. Without it, a
divergence between two stores is a fact nobody can trace to a cause.

Secrets and full sensitive prompts are excluded or redacted by data class — a
trace is an operational artifact and is read by more people than the data it
describes.

---

## 6. Consequences

**Accepted:** the outbox is real infrastructure and a real latency cost on every
canonical write.

**Accepted:** "rebuild the projection" has to be a routine, tested operation
rather than an emergency procedure, or it will not work on the day it matters.

**Gained:** a projection can be deleted without consequence, which makes graph
and index changes cheap rather than frightening.

**Rejected:** dual-write to store and index. It is faster, it is simpler, and it
produces two truths whose disagreement nobody notices until a claim rests on the
wrong one.

---

## 7. Decision

**Accepted, 2026-08-23.** The matrix is what WP-159 verifies and WP-030 projects
from. **Only one store in the table exists** — SQLite behind the Zotero bridge.
Temporal, PostgreSQL, the object store, NATS, Neo4j and MLflow are all
unimplemented, and the split-brain suite has never run.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-007`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
