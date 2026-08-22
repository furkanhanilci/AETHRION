> [!info] Generated view
> This note is generated from `docs/architecture/ADR-001_solo_operator_independence.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# ADR-001 — Solo-Operator Independence Model

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | What "independent verification" means when the laboratory has one operator |
| Sibling documents | `AETHRION_ROLES.md` §5 · `AETHRION_ARCHITECTURE.md` §6.1 · WP-007 · WP-000 |
| Status | **ACCEPTED — 2026-08-22.** The recommendation in §4 is the decision |
| Date | 2026-08-22 |

**In one paragraph.** Every Definition of Done requires an independent verifier,
and the role model forbids the producer from verifying its own work. With one
human operator those two rules meet head-on, and the result was that **no work
package could be accepted at all** — audit finding **C2**. This record resolves
that without weakening either rule: it sets out three models, states what each
costs, and **adopts Model A + C** (§6) — solo acceptance at R1, solo acceptance
at R2 only under a declared *partial* independence profile, and **R3 blocked**
unless an external human verifier is named. What it deliberately does not do is
manufacture independence the operation does not have.

---

## 1. The deadlock, precisely

```
WP-000 acceptance requires    → a verifier independent of the producer
role model requires           → producer ≠ Assurance Lead ≠ final verifier
the operation has             → one human
                              ⇓
                        no package reaches ACCEPTED
                              ⇓
              the commissioning programme cannot start
```

The technical half of the evidence problem is solved: WP-000 makes evidence
tamper-evident without WP-026. **This half is not technical.** It is a question
about what the laboratory is willing to call independent, and answering it wrongly
in either direction is expensive:

- **Too permissive** — the laboratory produces "independently verified" claims
  that were verified by their own producer under a different label. Every
  downstream assurance statement becomes decorative, which is precisely the
  failure this system exists to prevent.
- **Too strict** — nothing is ever accepted, the programme never starts, and the
  architecture remains a document.

---

## 2. What independence is actually made of

The `IndependenceProfile` has never been about counting people. Its dimensions
are separable, and a single operator can satisfy several of them:

| Dimension | Satisfiable by one operator? | How |
|---|---|---|
| **Mechanical verification** | ✅ fully | The check does not care who wrote the code; it either passes or it does not |
| **Context isolation** | ✅ | Fresh context, packet built by a program, producer reasoning withheld |
| **Model family** | ✅ | Producer and reviewer drawn from different provider families |
| **Environment** | ✅ | Reproduction in a clean room the producer did not prepare |
| **Temporal separation** | ⚠️ partial | Review after a declared delay reduces, but does not remove, anchoring |
| **Economic interest** | ❌ | The operator benefits from their own work being accepted |
| **Human identity** | ❌ | There is one human |

**Five of seven dimensions survive a one-person operation.** The two that do not
are exactly the two that matter most at the highest assurance class — which is
why the recommendation below binds the answer to the class rather than giving one
answer for everything.

---

## 3. The three models

### Model A — Mechanical-first solo independence

The operator holds every human role. Independence is supplied by mechanical
verification, context isolation, cross-family model review, and clean-room
reproduction. The human signature attests that the mechanical evidence was
produced and reviewed, not that a second person agreed.

| | |
|---|---|
| **R1** | Sufficient |
| **R2** | Weak — a cross-family model review is not a second scientist |
| **R3** | Not permitted |
| **Cost** | None |
| **Risk** | The word "accepted" carries less than a reader will assume unless the record says so on its face |

### Model B — External human verifier

A named external party — a collaborator, a supervisor, an institution — performs
final verification for R2 and R3. The operator retains production and R1.

| | |
|---|---|
| **R1** | Solo, under Model A |
| **R2** | External verifier required |
| **R3** | External verifier required, plus local open-weight reproduction |
| **Cost** | A real human dependency, with real latency |
| **Risk** | The programme's throughput becomes a function of someone else's calendar |

### Model C — R3 deferred

Models A and B for R1/R2; **R3 is declared unreachable** in the current
organisation and every R3 project stays `BLOCKED` by design rather than by
accident.

| | |
|---|---|
| **Cost** | No R3 work at all |
| **Risk** | None to integrity; the risk is to ambition |

---

## 4. Recommendation

> **A + C, with B available when an external party can be named.**
>
> - **R1** — solo acceptance under Model A, with the operator's binding recorded
>   and the `IndependenceProfile` explicitly showing which dimensions were and
>   were not satisfied.
> - **R2** — solo acceptance permitted **only** with cross-family model review,
>   clean-room reproduction and a declared temporal separation; the record states
>   that human identity and economic interest were **not** independent.
> - **R3** — `BLOCKED` unless an external verifier is named. Not simulated, not
>   approximated, not waived.
>
> **And an unconditional rule:** an acceptance whose independence is partial says
> so in the `EvidenceManifest` itself. A reader must never have to infer it.

The reasoning is that the framework's value is its refusal to overstate. A
laboratory that manufactures independence it does not have has already lost the
only thing that distinguishes it from an assistant with good documentation.

---

## 5. What this decision binds

Once taken, this record must be reflected in:

| Where | Change |
|---|---|
| **WP-007** IndependenceProfile | The solo-operation policy becomes part of the profile definition |
| **WP-000** | Names who verifies the bootstrap manifest under the chosen model |
| **WP-013** `RoleBinding` | `can_combine_with` / `cannot_combine_with` encode the chosen model |
| `AETHRION_ROLES.md` §5 | The combination matrix stops being a reference and becomes binding |
| Plan seal | Regenerated deliberately, as a recorded change |

---

## 6. Decision

| Field | Value |
|---|---|
| Decision | **Model A + C adopted, with Model B available whenever an external verifier can be named** |
| Decided by | Project Decision Owner |
| Date | 2026-08-22 |
| Rationale | Five of the seven independence dimensions survive a one-person operation and can be enforced mechanically. The two that do not — human identity and economic interest — are exactly the two that matter most at R3, so R3 is blocked rather than approximated. Accepting R1 and R2 under a declared, partial independence profile lets the programme start without the laboratory claiming an independence it does not have |

### 6.1 What is now in force

| Assurance class | Acceptance | Mandatory conditions |
|---|---|---|
| **R1** | Solo acceptance permitted | Mechanical checks pass; the `IndependenceProfile` records which dimensions were satisfied |
| **R2** | Solo acceptance permitted | Cross-family model review · clean-room reproduction the producer did not prepare · declared temporal separation · the manifest states that human identity and economic interest were **not** independent |
| **R3** | **`BLOCKED`** | Only an externally named human verifier lifts it. Not simulated, not approximated, not waived |

**Unconditional:** an acceptance whose independence is partial declares that in
the `EvidenceManifest` itself. A reader must never have to infer it.

### 6.2 Terminology — the distinction this decision must not blur

Cross-family model review, fresh context, a clean-room environment and temporal
separation are **useful independence dimensions**. None of them is what science
means by *independent verification by an independent investigator*.

| Term | Means | May be used for |
|---|---|---|
| **Independent verification** | A different human or institution, with no stake in the outcome, reproduced or reviewed the work | R3 only, and only when that party is named |
| **Internally separated verification** | The same operator, with context, environment, model family and time deliberately separated | R1 and R2 |
| **Cross-model corroboration** | A different provider family reached the same conclusion | A *component* of internal separation, never a substitute for it |

**R1 and R2 acceptances say "internally separated verification".** They do not
say "independently verified", in the manifest, in a publication, or anywhere
else. A reader encountering "R2 independently verified" would reasonably assume
two people; that assumption would be false, and the framework's whole value rests
on not creating it.

> **What this unblocks, and what it does not.** Finding **C2** is now decided
> rather than open, so R1 and R2 packages have a defined acceptance path and the
> programme can start. It does not make a one-person laboratory independent, and
> every R3 project remains `BLOCKED` by this decision — deliberately.
