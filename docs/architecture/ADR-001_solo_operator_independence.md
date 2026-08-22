# ADR-001 — Solo-Operator Independence Model

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | What "independent verification" means when the laboratory has one operator |
| Sibling documents | `AIRL_OS_ROLES.md` §5 · `AIRL_OS_ARCHITECTURE.md` §6.1 · WP-007 · WP-000 |
| Status | **PROPOSED — decision required before any package can reach `ACCEPTED`** |
| Date | 2026-08-22 |

**In one paragraph.** Every Definition of Done requires an independent verifier,
and the role model forbids the producer from verifying its own work. With one
human operator those two rules meet head-on, and the result is that **no work
package can be accepted at all** — audit finding **C2**. This record does not
resolve that by weakening either rule. It sets out three models, states what each
one costs, recommends one, and leaves the decision field blank, because a
framework cannot grant itself independence.

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
| `AIRL_OS_ROLES.md` §5 | The combination matrix stops being a reference and becomes binding |
| Plan seal | Regenerated deliberately, as a recorded change |

---

## 6. Decision

| Field | Value |
|---|---|
| Decision | *(not taken)* |
| Decided by | *(Project Decision Owner)* |
| Date | — |
| Rationale | — |

> **Until this table is filled in, no work package may be marked `ACCEPTED`** —
> including WP-000. Work may proceed to `TECH_COMPLETE`; it may not proceed past
> it. That is not a limitation to route around; it is the finding doing its job.
