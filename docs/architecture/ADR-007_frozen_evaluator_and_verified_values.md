# ADR-007 — Frozen Evaluators and Verified Values

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Where a published number comes from, and who is structurally unable to influence it |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · ADR-003 · ADR-006 · WP-082 · WP-083 · WP-084 · ACC-53 · ACC-54 · ACC-55 · ACC-77 |
| Status | **ACCEPTED — 2026-08-23.** Boundary decided; nothing is built |
| Date | 2026-08-23 |

**In one paragraph.** A system that optimises a metric will optimise whatever is
easiest to move, and the easiest thing to move is usually the metric. Not through
malice — an agent that can edit the evaluation script, read the held-out set or
report its own score has been handed three cheaper paths to a good number than
doing the research. This record puts the evaluator on the other side of a
security boundary from the thing being evaluated, and gives every published
number a typed identity that traces back to an immutable evaluator output.

---

## 1. The decision

> **The producer cannot influence the evaluator.** Official evaluator code, the
> metric definition and any hidden material live in a zone the candidate has no
> read or write path into. Evaluation emits a `RawEvaluatorArtifact` — immutable,
> digest-addressed, stored **before any agent interprets it**. Every published
> number is a `VerifiedValue` bound to one of those artifacts. **No number
> reaches a publication without that binding.**

---

## 2. The boundary

```
  PRODUCER ZONE                     ║        EVALUATOR ZONE
  ─────────────                     ║        ──────────────
  candidate code        editable    ║  official evaluator code    frozen
  candidate config      editable    ║  metric definition          frozen
  permitted train data  read        ║  hidden validation material  no producer path
  protocol, plan        read-only   ║  answer keys                 no producer path
                                    ║  signing identity            separate
        │                           ║
        └── signed candidate commit ═╬══► execution ──► RawEvaluatorArtifact
                                    ║                          │
                                    ║                    VerifiedValue
```

The producer may not: write evaluator source; read hidden material; override the
metric; write a `VerifiedValue` through any API; reach the evaluator's
credentials or environment; or traverse a path into the private zone.

**A boundary breach invalidates the run.** It does not lower the score. A
candidate that reached the evaluator zone has produced a result of unknown
provenance, and scoring it low would record it as a bad result rather than as no
result — ACC-54.

### The isolation is per candidate, not per campaign

Each candidate executes in its own workspace with its own commit lineage, under a
`MutationPolicy` naming editable, read-only and forbidden paths. Two candidates
running in parallel cannot see each other's working tree. This is what makes a
diff attributable and a parallel population safe.

---

## 3. Raw first, interpretation second

The evaluator's output is stored immutably **before** any agent summarises it.

This ordering is the whole mechanism. The alternative — an agent reads the
output, writes a summary, and the summary is what persists — means the record of
what happened is a paraphrase produced by an interested party. Every downstream
check then verifies the paraphrase.

So: raw bytes, digest, environment digest, evaluator code digest, dataset
snapshot reference. Interpretation happens afterwards and separately, and
changing an interpretation never changes the artifact it interprets (ADR-005 §3).

---

## 4. `VerifiedValue` — why a number needs an identity

A number in a paper is normally a string that someone typed. Here it is a record:

| Field | Why |
|---|---|
| `run_ref`, `evaluator_artifact_ref` | the number traces to bytes an evaluator produced |
| `metric_definition_ref` | 0.87 of *what*, computed *how* |
| `aggregation`, `seed_set` | a mean over which runs, at which seeds |
| `uncertainty`, `confidence_interval` | what the number does not pin down |
| `scope_qualification` | the dataset, baseline and protocol it holds under |

Two consequences follow, and both are tested.

**A number the registry does not carry cannot be published.** A writer stage that
emits 89.1% where the registry holds 87.3% fails the build regardless of how good
the surrounding prose is — ACC-53. A declared rounding of a registered value
passes and records its display transform, so the check discriminates rather than
blocking all formatting.

**A value cannot be rebound.** Reusing a trusted value identifier against a
different raw output is refused; a legitimate recomputation creates a successor
rather than editing one, and assertions referencing the original still resolve to
the original — ACC-77.

---

## 5. Why promotion is mechanical

A candidate moves DRAFT → SMOKE → VERIFY → FULL against criteria derived from the
frozen `EvaluationContract` and `AnalysisPlanManifest`. Where the criterion is
computable, the decision is computed. A model may recommend; it may not promote
past a threshold that refused.

`ExperimentPromotionRecord` records the tier transition, the criteria snapshot,
the values that decided it and whether the decision was `MECHANICAL_POLICY` or
`HUMAN`. Under a CONFIRMATORY study mode the rule is non-waivable — ACC-60.

This is the general rule of the architecture applied to one gate: **a mechanical
check, where one exists, runs first and cannot be overridden by a model.**

---

## 6. What this does not protect against

Stated plainly, because a boundary that is described as complete is worse than
one whose limits are known:

- **A wrong metric.** The evaluator is frozen, not correct. Optimising a bad
  metric perfectly is still optimising a bad metric, and only review catches it.
- **Contaminated training data.** If the held-out set leaked into the corpus
  before freezing, isolation preserves the leak — ACC-37 is the separate control.
- **A supply-chain compromise of the evaluator itself.** Handled by WP-027 and
  WP-059, not here.
- **Overfitting through repeated legitimate evaluation.** Nothing in this record
  bounds how many times a hidden set may be queried; that is a budget and
  protocol question.

---

## 7. Consequences

**Accepted:** experiments become more expensive to run. Two zones, two
identities, a workspace per candidate and an immutable artifact per evaluation
is real infrastructure.

**Accepted:** a researcher cannot glance at the hidden set to debug an
implausible score. That is the intended cost.

**Gained:** every published number has a traversable path to bytes, and the path
is checkable by a machine.

**Gained:** the CoE-style score-verification audit becomes possible at all —
recomputing a reported value against a raw evaluator output requires the raw
output to exist.

---

## 8. Decision

**Accepted, 2026-08-23.** The boundary is the contract WP-083 and WP-084 deliver
and WP-082 records. **Nothing is built** — there is no evaluator zone, no
candidate workspace, no run registry and no value registry. The isolation pattern
behind it is recorded in `provenance/upstreams.json` under ADR-004 as a pattern
taken, not code adopted.
