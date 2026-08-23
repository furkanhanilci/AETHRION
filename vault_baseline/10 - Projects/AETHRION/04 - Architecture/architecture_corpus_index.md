---
title: "Architecture"
cssclasses:
  - aethrion-reference
type: reference
category: architecture
summary: "Three kinds of document live here and confusing them is the main way this repository gets overestimated: a reference describes what was decided, a decision record fixes something and names who decided it, and a proposal argues for something nobody has agreed to yet."
source: "docs/architecture/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `docs/architecture/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Architecture

| Field | Value |
|---|---|
| Document type | Index — the architecture corpus, and what kind of document each one is |
| Scope | Target design, decision records and positioning |
| Sibling documents | `../README.md` · `../DOCUMENT_STANDARD.md` · `../branding.md` (naming: AETHRION, and where `AIRL` is kept on purpose) |
| Status | Index |
| Date | 2026-08-23 |

**In one paragraph.** Three kinds of document live here and confusing them is the
main way this repository gets overestimated: a **reference** describes what was
decided, a **decision record** fixes something and names who decided it, and a
**proposal** argues for something nobody has agreed to yet. Every file below is
labelled, and the labels are load-bearing.

| Document | Kind | Answers |
|---|---|---|
| `AETHRION_ARCHITECTURE.md` | reference | What is this system? The diagrammed entry point |
| `AETHRION_ROLES.md` | reference | The fourteen durable functions, what each may never do, and why role ≠ person |
| `FOUNDATION.md` | reference | The contract and platform substrate |
| `AETHRION_ROLE_MODEL_ASSIGNMENT.md` | decision record | Which actor class executes each gate; effort and reviewer quota per assurance class |
| `AETHRION_EXTERNAL_STANDARDS.md` | decision record | Which formats are adopted rather than invented |
| `AETHRION_COMPONENT_REUSE.md` | decision record | Which running implementation each control stands on, and under which adoption type |
| `ADR-001_solo_operator_independence.md` | **accepted decision** | What independence means with one operator: R1 solo · R2 declared-partial · **R3 blocked** |
| `ADR-002_bootstrap_verification_control.md` | **accepted decision** | BVC-01, a temporary verification control with an expiry — written, **not active** |
| `ADR-003_trusted_control_and_policy.md` | **accepted decision** | Untrusted content is data; a formally-analysable policy engine evaluates; any anomaly denies |
| `ADR-004_mechanism_assimilation.md` | **accepted decision** | A mechanism may be taken from another project; an architecture may not. Pin, licence, characterisation, authority boundary |
| `ADR-005_epistemic_memory_separation.md` | **accepted decision** | Six memories, not one. Only the evidence store may support a claim |
| `ADR-006_discovery_search_graph.md` | **accepted decision** | Discovery is a typed candidate graph, and a search score is never a confidence |
| `ADR-007_frozen_evaluator_and_verified_values.md` | **accepted decision** | The producer cannot influence the evaluator; every published number is a `VerifiedValue` |
| `ADR-008_verification_taxonomy.md` | **accepted decision** | V0–V3. "Mechanical" means V0 and V1; a semantic verifier must be qualified before it counts |
| `ADR-009_publication_as_projection.md` | **accepted decision** | The document is generated from the claim graph; a factual sentence with no claim fails the build |
| `ADR-010_policy_backend.md` | **accepted decision** | The `PolicyDecision` interface is commissioned; the engine is deferred to a bake-off that has not run |
| `ADR-011_multi_agent_execution_invariant.md` | **accepted decision** | Substantial scientific execution stays multi-agent; optimisation targets the conversation, never the cohort |
| `ADR-012_dual_disciplines.md` | **accepted decision** | Engineering and scientific disciplines stay separate and composable — a passing test is not a confirmed hypothesis |
| `ADR-013_blackboard_and_sparse_communication.md` | **accepted decision** | Inter-agent exchange is typed, sparse and delta-only, and the blackboard is deletable |
| `ADR-014_canonical_authority_and_split_brain.md` | **accepted decision** | One canonical owner per kind of state; every projection rebuilds losslessly |
| `ADR-015_adaptive_assurance_routing.md` | **accepted decision** | Assurance is routed by consequence and uncertainty, and a verifier may abstain. **Extends ADR-008** |
| `ADR-016_human_preliminary_judgment.md` | **accepted decision** | The human judges before the machine recommends, and correcting costs no more than approving |
| `ADR-017_benchmark_isolation.md` | **accepted decision** | A benchmark run is firewalled, and contamination is a label rather than a silent uplift |
| `ADR-018_specification_to_code_conformance.md` | **accepted decision** | The frozen specification and the running code must still agree; major drift changes scientific status |
| `ADR-019_supply_chain_and_upstream_standard.md` | **accepted decision** | Standard tooling establishes provenance, and adapted source enters through the same gate. **Extends ADR-004** |
| `AETHRION_IDEAL_STRUCTURE.md` | **proposal** | What should be added: roles, review mechanisms, the metascience plane |
| `AETHRION_SKILL_LAYER.md` | proposal + decision | How agents work. **§14 is decided**; §§2–13 record the analysis it overruled |
| `AETHRION_RELATED_SYSTEMS.md` | positioning + register | How this compares to other research systems — including where they are ahead — and which mechanism was taken from each |
| `../../provenance/README.md` | **generated register** | Every assimilated mechanism, its upstream, its licence, and what it may never decide |

## Reading order

1. `AETHRION_ARCHITECTURE.md` — the whole system, with §10 stating how much exists
2. `AETHRION_ROLES.md` — who is accountable
3. `AETHRION_COMPONENT_REUSE.md` — what is built here versus adopted
4. The nineteen ADRs — the decisions currently in force, in three groups.
   **ADR-001 to ADR-003** fix independence, bootstrap verification and the trust
   boundary. **ADR-004 to ADR-010** fix the epistemic layer — how a mechanism is
   taken, what is remembered where, what a search score may never become, where a
   number comes from, what "verify" means, what a document may assert, and which
   engine decides policy. **ADR-011 to ADR-019** fix the reliability layer — that
   the cohort is not a cost lever, that two disciplines stay separate, how agents
   talk, who owns which truth, how assurance is routed, when the human judges,
   how a benchmark is run, whether the code still matches the method, and how the
   supply chain is established
5. `AETHRION_IDEAL_STRUCTURE.md` — only after the above, because it is a proposal

**If you read only two:** ADR-008 and ADR-011. The first says what this project
means by *machines verify*; the second says what it means by *agents produce* —
and why the most obvious cost saving in a multi-agent system is the one it
refuses.

**If you read only one:** ADR-008. It is the record that says what this project
means by its own thesis sentence, and the distinction it draws — between a check
that is certain and a check that has an error rate — is the one that everything
else in the assurance layer rests on.

## What none of these establish

No document here is evidence that anything runs. For that, read
[`../STATUS.md`](../05 - Evidence/current_status.md), which is generated by running the checks.
