---
title: "Shared Contract Schemas"
cssclasses:
  - aethrion-reference
type: reference
category: architecture
source: "schemas/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `schemas/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Shared Contract Schemas

Machine-readable schemas for the canonical contracts that cross plane
boundaries.

## Intended contents

| Schema | Work package | What it defines |
|---|---|---|
| `identity.json` | WP-011 | Identity and correlation fields across every plane |
| `artifact-manifest.json` | WP-014 | Content hash, lineage, retention, validity |
| `event-envelope.json` | WP-015 | Event id, causation, actor, data class, payload reference |
| `policy-decision.json` | WP-016 | Authorization and routing decision records |
| `source-literature.json` | WP-017 | Source identity, representation, trust, set manifest |
| `claim-evidence.json` | WP-018 | Claim version, evidence span, review verdict, decision |
| `run-environment.json` | WP-019 | Run manifest, environment, reproduction tolerance |
| `notification.json` | WP-131 | Notification intent and receipt |
| `channel-registry.json` | WP-132 | Channel, data-class ceiling, egress hosts |
| `study-mode.json` | WP-142 | Study mode, claim ceiling, external timestamp, supersession |
| `bottleneck-idea.json` | WP-142 | Bottleneck, idea card, falsification plan, prior-art collision |
| `hypothesis-principle.json` | WP-143 | Hypothesis, principle and assumption versions with evolution operators |
| `search-graph.json` | WP-144 | Search node, edge class, candidate workspace, mutation policy |
| `search-policy.json` | WP-145 | Selection policy, fusion proposal, stagnation, research budget contract |
| `evaluation-contract.json` | WP-013 · WP-081 | Frozen metric, direction, evaluator digest, hidden-test policy |
| `evaluator-value.json` | WP-082 | Raw evaluator artifact, verified value, prediction, failure assessment |
| `memory-taxonomy.json` | WP-146 | The six stores, their retention semantics and the memory query policy |
| `verification.json` | WP-087 | Verification result with its V0–V3 class, and verifier qualification |
| `reproduction.json` | WP-085 | Algorithm understanding, reproduction package and run, claim consistency |
| `publication-assertion.json` | WP-090 | Publication assertion, evidence tag (CiTO relations), text role |
| `human-intervention.json` | WP-004 · WP-093 | Intervention vocabulary with before/after refs; attention score, `authority=false` |
| `upstream-lineage.json` | WP-141 | Assimilation candidate and upstream lineage — **the one entry with a working implementation today**, as `provenance/upstreams.json` plus `scripts/check_upstream_lineage.py` |

### Added by baseline v1.3.0 — the reliability layer

The contracts above describe a research *pipeline*. These describe a **cohort**:
who is in it, what may cross between its members, what it costs, what it may not
be allowed to skip, and what makes a number it produced believable afterwards.
They are listed separately because the failure modes they carry did not exist
before there was more than one actor.

| Schema | Work package | What it defines |
|---|---|---|
| `agent-cohort.json` | WP-148 | `AgentCohortRecord` — the actors bound to a task, their roles, and the record that a cohort was convened rather than assumed |
| `cognitive-diversity.json` | WP-148 | `CognitiveDiversityProfile` — independence across five dimensions (cognitive function, evidence exposure, peer visibility, model profile, prompt perspective). **A count is not a profile**, and five instances of one model on one context is one contribution |
| `communication-edge.json` | WP-149 | `CommunicationEdgePolicy` — which actor may say what to which other actor, compiled per task rather than assumed complete |
| `blackboard-entry.json` | WP-150 | `BlackboardEntry` — a delta with a pointer and a digest. Deletable by construction: no canonical science lives here |
| `agent-message.json` | WP-150 | `TypedAgentMessage` — the ten message types. A `CHALLENGE` can be tracked to resolution; a paragraph cannot |
| `communication-utility.json` | WP-149 · WP-153 | `CommunicationUtilityRecord` — the measured value of an edge, and the record of what a degradation step actually removed |
| `context-projection.json` | WP-151 | `ContextProjectionRecord` — what was assembled into an invocation's context, and what was masked. A refuted conclusion must not return as current |
| `memory-intervention.json` | WP-151 | `MemoryInterventionRecord` — a masking, supersession or correction of a memory, with its authority and its reason |
| `research-budget.json` | WP-153 | `ResearchBudgetContract` — the exploration budget and the **reserved** verification, reproduction and assurance budget the exploration path cannot reach |
| `token-ledger.json` | WP-153 | `TokenLedgerEntry` — tokens classified by purpose, so that coordination overhead is a measurement rather than an estimate |
| `spec-conformance.json` | WP-154 | `SpecificationConformanceRecord` — the drift severity ladder `NONE` / `ENGINEERING_ONLY` / `SCIENTIFIC_MINOR` / `SCIENTIFIC_MAJOR` / `UNKNOWN`, and which frozen artefact the code diverged from |
| `human-preliminary.json` | WP-156 | `HumanPreliminaryAssessment` — sealed **before** any AI recommendation is reachable, plus `INSUFFICIENT_BASIS` as a first-class outcome |
| `decision-delta.json` | WP-156 | `DecisionDelta` — the distance between the preliminary assessment and the final decision, which is the only way anchoring becomes measurable |
| `model-fingerprint.json` | WP-157 | `ModelExecutionFingerprint` — provider, snapshot, API version, sampling parameters, and every retry and fallback. A silent failover mid-run is drift |
| `benchmark-policy.json` | WP-158 | `BenchmarkRunPolicy` — the frozen network mode, allowed domains and retrieval audit for a benchmark run |
| `contamination-finding.json` | WP-158 | `ContaminationFinding` — training-corpus and **search-time** contamination, and the label a contaminated score carries permanently |
| `efficiency-qualification-profile.json` | WP-149 · WP-153 | `EfficiencyQualificationProfile` — the sealed thresholds a coordination optimisation is judged against: quality ceiling, minimum reduction, statistical method, calibration and holdout digests with a no-overlap attestation, and a `frozen_at` after which a threshold change requires a new version. **The artifact exists so that "pre-declared tolerance" has a place to be declared**; without it the ceiling can be chosen once the release-candidate result is visible, which is not a ceiling |
| `upstream-assimilation.json` | WP-159 · WP-141 | `UpstreamAssimilationRecord` — the admission record for adapted code: lineage, licence, pin, characterisation suite and `authority_boundary` |

Three properties cut across the whole group, and each exists because of a
specific way this kind of record goes wrong:

- **A record here is never a substitute for canonical state.** A
  `BlackboardEntry` carries a pointer and a digest, and the content lives in the
  artifact store. Delete the blackboard and the science survives — `ADR-013`,
  ACC-085.
- **Every one of them is evidence about a run, not authority over it.** A cohort
  record does not approve a gate; a diversity profile does not license a claim; a
  fingerprint does not make a result reproducible. `ADR-014` keeps the authority
  where it was.
- **The immutable ones are immutable.** A `ModelExecutionFingerprint` or a
  `RawEvaluatorArtifact` that can be edited is not one. A legitimate
  recomputation creates a successor and leaves the original resolvable —
  ACC-023, ACC-077.

## Status

> ⚠️ **Currently empty**, with one exception: the upstream lineage register
> exists and is validated, but as `provenance/upstreams.json` against a
> hand-written checker rather than as a JSON Schema generated from one model.
> That is the same debt this directory records, arriving one file early.
>
> The contract core in [`src/airl_framework/`](../src/airl_framework/) exists as
> in-process Python classes with no JSON Schema representation and no CI
> enforcement. It also has **no production consumer** — see finding **H4** in
> [`docs/review/`](../docs/review/).
>
> Until these schemas exist and are enforced in CI, WP-020 (Schema Registry and
> Contract SDK) cannot reach `TECH_COMPLETE`, let alone `ACCEPTED`.
>
> The eighteen contracts added at v1.3.0 and v1.3.1 are `SPECIFIED` in the same sense as
> the rest of the table — named, owned by a work package, and unwritten. Listing
> them is worth doing anyway: the table is what a schema author is handed, and
> the alternative is re-deriving eighteen record shapes from twelve work
> packages under deadline. It is not, and must not be read as, a claim that any
> of them exists.

## Rules once populated

1. A schema version is **registered**, never redefined. Changing a published
   version is forbidden; publish a new version instead.
2. Major-version changes are breaking. Producer and consumer compatibility is
   checked in CI, not by convention.
3. Every schema carries at least one **negative test** — an instance that must
   fail validation.
4. A contract with no production consumer is dead code. Bind it or delete it.
