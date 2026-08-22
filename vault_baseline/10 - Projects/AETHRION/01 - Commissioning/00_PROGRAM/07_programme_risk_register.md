---
title: "Programme Risk Register and Treatment Rules"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/07_programme_risk_register.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Programme Risk Register and Treatment Rules

| ID | Risk | Early signal | Preventive control | Owner | Cutover impact |
|---|---|---|---|---|---|
| PR-01 | Platform scope grows uncontrolled | Packages keep exceeding L | Contract-first, scope lock, retirement criteria | Chief Architect | High |
| PR-02 | Policy becomes combinatorial | Large cross-tables, unexplainable decisions | Separate profiles, precedence and hard-promotion rules | Governance Lead | Critical |
| PR-03 | Canonical ownership blurs | Zotero/Registry/Obsidian values diverge | Field authority and reconciliation | Knowledge Lead | Critical |
| PR-04 | Verification backlog grows | G6/G7 waiting and bypass requests | Risk-based depth, C0 mechanical checks, capacity reserve | Assurance Lead | Critical |
| PR-05 | Reviewer independence exists only on paper | Same trace, credential or model family | Machine-checkable `IndependenceProfile` | Assurance Lead | Critical |
| PR-06 | Agent tool authority expands too far | Direct credential or connector use | Broker-only, purpose-bound identity | Safety Owner | Critical |
| PR-07 | Dual authority over event/state | A NATS consumer changes gate state | Temporal-only transitions, outbox contract | Control Plane Lead | Critical |
| PR-08 | Artifact overwrite / lineage loss | Different bytes at the same URI | Content addressing, object lock | Data Platform Lead | Critical |
| PR-09 | Cost runaway | Fan-out, retry, token growth | Hard budget, queue quota, minimum bundle | FinOps Lead | High |
| PR-10 | Vendor lock-in | Provider fields leak into role contracts | Adapter conformance and canonical contracts | Model Platform Lead | High |
| PR-11 | Human rubber-stamping | Very fast or generic approvals | Evidence-delta UI, rationale rubric, sampling | Governance Lead | High |
| PR-12 | False rigor | Many artifacts, weak entailment | Outcome audit, anti-metrics, citation audit | Research Director | Critical |
| PR-13 | Restore exists only on paper | Backups present, no rehearsal | Two restore drills + integrity queries | SRE Lead | Critical |
| PR-14 | Source licences violated | PDFs proliferate uncontrolled | Licence policy, hash-only fallback, access log | Knowledge / Safety | Critical |
| PR-15 | Eval contamination | Golden set appears in prompts or traces | Separate credential/store, canary, invalidate/re-eval | Eval Office | Critical |

## Risks identified by the audit

| ID | Risk | Why it is not covered above | Owner |
|---|---|---|---|
| **PR-16** | **Independence is assumed, never measured** | PR-05 addresses paper independence; it does not address correlated errors between genuinely different models | Metascience Lead |
| **PR-17** | **Confidence scores carry no measurement basis** | A specific, mechanical instance of PR-12 that the register treats only in the abstract | Metascience Lead |
| **PR-18** | **The lab's own error rate is unknown** | No control mechanism measures whether the pipeline produces correct results at all | Metascience Lead |
| **PR-19** | **Publication bias survives the gate structure** | G2 freezes the protocol, but G8 can still reject on the direction of the result | Research Director |
| **PR-20** | **Periodic work fails silently** | Neither PR-13 nor SLO alerting covers a job that stops without erroring | SRE Lead |
| **PR-21** | **Scope does not fit the organisation** | The programme assumes dozens of role-holders and a separate assurance pool | Executive Sponsor |

## Status of the audit findings, 2026-08-22

| Finding | Then | Now |
|---|---|---|
| **C1** evidence bootstrap | Critical — nothing could be accepted | **Storage half addressed.** WP-000 written and its tooling implemented; a specimen manifest verifies and both tamper paths are rejected. **No manifest has been accepted** |
| **C2** independent verification | Critical — R3 permanently blocked | **Decided** in ADR-001: R1 solo · R2 solo under a declared partial-independence profile · **R3 `BLOCKED`** without an external verifier |
| **H5** no CI | Open | **Partly.** BVC-01 is decided and written (`deploy/bvc-01-verify.yml`) but **not active** — activation needs a workflow-scoped token. H5 itself stays open: it is the absence of the WP-024 platform |
| **H1** ingest capped at 100 | Open | Open. **Fix M9 first**, or pagination turns a masked truncation into active data loss |
| **H2 · H3 · H4** | Open | Open |

## New risks recorded by this baseline

| Risk | Why it is a risk |
|---|---|
| **Adoption without verification** | Ten packages now stand on external components. A component adopted and never verified is a dependency with the *appearance* of assurance |
| **Benchmark drift into gate** | A `BENCHMARK` measures the laboratory; if one ever becomes a pass condition, the laboratory starts optimising against its own scorer |
| **Specification outpacing execution** | 141 package documents, 51 scenarios, 52 skills — and one working vertical slice. This is the standing risk, and it is not decreasing |
| **Interim attestation mistaken for witnessed** | `airl-interim-v0.1` is tamper-evident, **not externally witnessed**: one operator holds the repository, the key, the generator and the clock |

## Scoring

Programme risks are tracked with impact and likelihood on a 1–5 scale. However,
**critical security, identity, evidence, reproduction and data blockers cannot be
lowered by a numeric total.** The numeric score exists for prioritisation; it is
not a waiver mechanism.

## Risk closure

A risk does not close on "mitigation applied". Closure requires a control
effectiveness test, an evidence reference, a residual-risk owner and a
re-evaluation date.

On cutover day every critical risk must be `CLOSED` or explicitly classified
`ACCEPTABLE` by policy. Non-waivable risks cannot be `ACCEPTABLE`.
