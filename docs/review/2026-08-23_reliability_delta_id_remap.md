# Reliability Completion Delta — Identifier Remap

| Field | Value |
|---|---|
| Document type | Review — dated, frozen. Never updated |
| Scope | Every identifier the reliability completion delta proposed, and the identifier it received here |
| Sibling documents | `2026-08-23_reliability_delta_audit.md` (the audit that found the collisions) |
| Status | Frozen — the remapping is applied; this record is why |
| Date | 2026-08-23 |

**In one paragraph.** The delta was written against an assumed repository and
proposes identifiers that partly collide with ones already in use. Its own rule
is that a taken identifier is never overwritten and the semantic name is the
binding thing. This record applies that rule: nine architecture decision records
move, twelve work packages and forty scenarios do not, and two of the moved
records turn out to extend an existing decision rather than to be new ones.

---

## 1. Architecture decision records — all nine remapped

Baseline v1.2.0 accepted `ADR-004`–`ADR-010` earlier on the same day. The delta's
`ADR-004`–`ADR-012` therefore land at `ADR-011`–`ADR-019`, in the delta's own
order.

| Delta proposed | Semantic name — the binding identity | Assigned here |
|---|---|---|
| `ADR-004` | Multi-agent scientific execution invariant | **`ADR-011`** |
| `ADR-005` | Dual scientific and software-engineering disciplines | **`ADR-012`** |
| `ADR-006` | Scientific blackboard and sparse typed communication | **`ADR-013`** |
| `ADR-007` | Canonical authority and split-brain prevention | **`ADR-014`** |
| `ADR-008` | Adaptive assurance and qualified semantic verification | **`ADR-015`** |
| `ADR-009` | Human preliminary judgment before AI recommendation | **`ADR-016`** |
| `ADR-010` | Benchmark isolation and contamination policy | **`ADR-017`** |
| `ADR-011` | Specification-to-code conformance | **`ADR-018`** |
| `ADR-012` | Supply chain and upstream assimilation standard | **`ADR-019`** |

### 1.1 Two of these are extensions, not new decisions

The collision was numeric. Two of the nine also overlap **semantically** with a
decision this repository already took, and recording them as independent records
would leave two documents deciding the same question.

| Delta record | Overlaps | Resolution |
|---|---|---|
| Adaptive assurance and qualified semantic verification | **`ADR-008`** — the V0–V3 verification taxonomy, which already requires a `VerifierQualificationRecord` before a V2 verdict can satisfy anything | `ADR-015` **extends** `ADR-008`. The taxonomy stands; what is added is *routing* — which class runs when, cascade on uncertainty, and `ABSTAIN` as a valid verdict rather than a failure |
| Supply chain and upstream assimilation standard | **`ADR-004`** — mechanism assimilation, which already requires a pinned commit, a licence read at the source, a characterisation suite and a stated authority boundary | `ADR-019` **extends** `ADR-004`. The assimilation rules stand; what is added is the *toolchain* — SPDX/REUSE, OSV-Scanner, OpenSSF Scorecard, SLSA provenance, Sigstore — and the drift-monitoring policy that binds them to release |

Each extending record names what it extends in its header and does not restate
it. A reader arriving at `ADR-015` is sent to `ADR-008` for the taxonomy; a
reader arriving at `ADR-008` is told where the routing lives.

---

## 2. Work packages — no collision, no remap

The delta proposes `WP-148`–`WP-159`. The first package stopped at `WP-147`, so
all twelve are free and all twelve keep their proposed numbers.

| Delta | Semantic name | Assigned |
|---|---|---|
| `WP-148` | Multi-Agent Collaboration Plane and Cohort Integrity | **`WP-148`** |
| `WP-149` | Sparse Communication Topology and Scientific Blackboard | **`WP-149`** |
| `WP-150` | Communication Governor, Edge Utility and Context Projection | **`WP-150`** |
| `WP-151` | Memory Masking and Proactive Intervention | **`WP-151`** |
| `WP-152` | Failure Taxonomy, Attribution and Resilience Controls | **`WP-152`** |
| `WP-153` | Research Budget, Token Ledger and Efficiency Control | **`WP-153`** |
| `WP-154` | Engineering Discipline and Specification Conformance | **`WP-154`** |
| `WP-155` | Adaptive Assurance, Verifier Qualification and Escalation | **`WP-155`** |
| `WP-156` | Human Oversight Debiasing and Attention Governance | **`WP-156`** |
| `WP-157` | Reproduction Determinism and Model Execution Fingerprint | **`WP-157`** |
| `WP-158` | Benchmark Firewall and External Evaluation Qualification | **`WP-158`** |
| `WP-159` | Supply Chain, Upstream Drift and Cross-Plane Integrity | **`WP-159`** |

They live in a new workstream, **`15_RELIABILITY_EFFICIENCY`**.

---

## 3. Acceptance scenarios — no collision, no remap

`ACC-081`–`ACC-120` are free; the first package stopped at `ACC-80`. All forty
keep their proposed numbers, and the highest scenario becomes `ACC-120`.

---

## 4. Programme risks — remapped

The delta numbers its risk dossiers `R01`–`R30`. The programme risk register
already uses `PR-01`–`PR-28`, and `R01` in a repository that has `PR-01` is an
invitation to conflate them.

The thirty dossiers are therefore folded into the existing register as
**`PR-29`–`PR-58`**, in the delta's order, each keeping its delta identifier in a
provenance column so the dossier it came from stays findable.

---

## 5. The rule this record applies

From the delta's own handoff:

> *Repository bu ID'leri daha önce kullanmışsa **asla overwrite etme**; sonraki
> boş ID'leri ata ve `delta-id-remap.md` üret. **Semantic adlar binding source of
> truth'tur.***

Which is the right rule, and worth stating why: an identifier is a promise that
two documents talking about `ADR-008` mean the same decision. Reusing one to
match a package's expectations would break every cross-reference already written
against it, silently, in a corpus whose whole discipline is that references
resolve.

**Nothing in the previous baselines was renumbered, rewritten or re-sealed to
accommodate this delta.**
