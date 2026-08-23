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

## Rules once populated

1. A schema version is **registered**, never redefined. Changing a published
   version is forbidden; publish a new version instead.
2. Major-version changes are breaking. Producer and consumer compatibility is
   checked in CI, not by convention.
3. Every schema carries at least one **negative test** — an instance that must
   fail validation.
4. A contract with no production consumer is dead code. Bind it or delete it.
