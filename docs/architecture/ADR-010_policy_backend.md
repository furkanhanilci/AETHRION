# ADR-010 — Policy Backend: the Interface Is Commissioned, the Engine Is Not Yet Chosen

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Resolving a contradiction between ADR-003 and WP-056 about which policy engine is being built |
| Sibling documents | `ADR-003_trusted_control_and_policy.md` · `AETHRION_COMPONENT_REUSE.md` §6 · WP-016 · WP-056 · ACC-24 |
| Status | **ACCEPTED — 2026-08-23.** The contradiction is resolved by deferring the engine, not by picking one |
| Date | 2026-08-23 |

**In one paragraph.** Two documents in this repository named different policy
engines. ADR-003 said Cedar, with OPA/Rego recorded as the alternative and the
choice "fixed only after a bake-off". WP-056 was titled *OPA Policy Platform*
and listed `OPA platform` as a mandatory deliverable. Neither is built, so
nothing was broken — but the plan had quietly made a decision the architecture
said was open, which means either document could have been used to justify
either engine. This record resolves it in the only direction the evidence
supports: the **interface** is what gets commissioned, and the engine is chosen
by a recorded bake-off that has not happened.

---

## 1. The decision

> **`PolicyDecision` is the commissioned contract; the engine behind it is a
> deployment choice.** No document may name a winner until the bake-off recorded
> here has run and produced evidence. WP-056 delivers the policy decision point,
> its bundle distribution, its fail-closed semantics and its explainability
> surface — **against the interface**, with one backend commissioned and the
> other retained as the recorded alternative.

---

## 2. What the contradiction actually was

| Document | What it said | Status |
|---|---|---|
| `ADR-003` §3 | Cedar is the policy decision point; OPA/Rego stays the recorded alternative; the choice is fixed after a bake-off | Architecture |
| `AETHRION_COMPONENT_REUSE.md` §6 | OPA/Rego — **OPTIONAL BACKEND** — "the general-purpose alternative, kept as the fallback in a recorded bake-off" | Architecture |
| `WP-056` | *OPA Policy Platform and Bundle Distribution*; deliverable `OPA platform` | Plan |

The architecture deferred; the plan had decided; and the two decided
differently. The defect is not that one is wrong — it is that a reader could
have cited whichever supported what they were about to do, which is what an
unresolved contradiction is for.

---

## 3. Why the answer is "the interface", not "pick one now"

A bake-off with no evidence is a preference. Neither engine has been run against
this system's actual policy set, because **no policy set is authored** — ADR-003
says so, and `AGENTS.md` §4.4 repeats it. Choosing now would be choosing on
reputation.

The properties this architecture needs from a policy engine are also not the ones
either project's marketing leads with:

| Requirement | Why it decides the choice |
|---|---|
| **Fail closed on evaluation error** | An engine that returns "no decision" on an internal error, and a caller that reads that as permission, is the failure mode. This must be provable, not configured |
| **Explainability of a denial** | A denial nobody can explain is a denial that gets overridden. ADR-003 §3.1 already requires the wrapper to preserve the reason |
| **Trusted/untrusted labelling in the model** | The control–data boundary has to be expressible *in the policy*, not enforced beside it |
| **Signed, versioned bundle distribution** | ACC-24 requires a policy rollback to be a recorded, verifiable event |
| **Decision latency at enforcement points** | Every tool call passes through it |

Those are measurable. The bake-off is the measurement, and it is qualification
evidence — not a gate.

---

## 4. Consequences for the documents

- **ADR-003 stands.** Its architectural decision — untrusted content is data,
  control flow comes from trusted intent, evaluation anomalies fail closed — is
  independent of the engine and is unaffected.
- **WP-056 becomes backend-neutral** in title, purpose and deliverables. It
  delivers the policy decision point and bundle distribution against the
  interface; the backend is named in its configuration, not in its identity.
- **`AETHRION_COMPONENT_REUSE.md`** records both engines as OPTIONAL BACKEND
  behind one interface, with the bake-off as the deciding evidence.
- **The filename `WP-056_opa_policy_platform.md` is retained.** Renaming it would
  break cross-references and re-seal the plan for no gain, and a filename is not
  a decision. This is the same rule that keeps `airl_*` where it is technical —
  see `docs/branding.md`. The document's title and contents are what a reader
  binds to.

---

## 5. What would settle it

The bake-off, run against a real policy set once one exists, reporting:

1. Fail-closed behaviour under injected evaluation errors, per request class.
2. Denial explainability — can the reason be rendered to a human without reading
   the policy source?
3. Whether the trusted/untrusted label is expressible natively in the model.
4. Signed bundle distribution and rollback against ACC-24.
5. Decision latency at the enforcement points, at realistic policy size.
6. Operational cost: authoring, testing and reviewing policies at this scale.

The result is a `VerificationResult` and a qualification record, and it is
recorded whichever way it lands — including the outcome where the difference does
not matter and the choice falls to operational familiarity.

---

## 6. Consequences

**Accepted:** an interface with one implementation is speculative generality
until the second exists. It is accepted here because the second one already
exists in the documents, and the cost of the abstraction is smaller than the cost
of two records disagreeing.

**Accepted:** the choice stays open longer, and someone will want to decide it
sooner. The reason not to is that deciding it now would produce exactly the
document this record is repairing.

**Gained:** one answer to "which policy engine is AETHRION building?" — *the
interface; the engine is measured, and the measurement has not run.*

---

## 7. Decision

**Accepted, 2026-08-23.** The contradiction is closed by making the interface the
commissioned deliverable and the engine an open, recorded choice. **The bake-off
has not run**, no policy set is authored, and no policy engine is deployed.

Reopened when: the first policy set exists, at which point the bake-off is
runnable and this record is superseded by one that names an engine and shows the
evidence.
