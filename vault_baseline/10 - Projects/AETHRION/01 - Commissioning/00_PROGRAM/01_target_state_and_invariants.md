---
title: "Target State, System Boundary and Invariants"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/01_target_state_and_invariants.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Target State, System Boundary and Invariants

## Target operating outcome

When AETHRION is in service, a research request travels from G0 to G10 in a
single correlation chain carrying its identity, budget, source set, protocol,
runs, claims, independent review, reproduction, human decision, publication
package and subsequent impact monitoring.

The point is not that each of these exists. It is that they are **linked**: any
claim can be traced, in one query, back through every step that produced it.

## Planes of responsibility

| Plane | What it owns | Example of canonical state |
|---|---|---|
| Experience | Human intent, visible decisions, working surface | Approval command, human annotation |
| Control | Lifecycle, gates, retry, timeout, compensation | Temporal event history |
| Event | Post-commit integration and replay | NATS stream/consumer offset |
| Cognition | Bounded agent task graph | LangGraph checkpoint and `AgentResult` |
| Execution | Isolated compute, queue, tool and workload lease | `ExecutionLease`, `SandboxAttestation` |
| Evidence & Operations | Source, artifact, claim, run, telemetry, cost, audit | Registries, immutable manifests |

Policy/model routing and identity/security cut horizontally across all planes.

> **Proposed addition.** A seventh plane — **Metascience & Calibration** — is
> proposed in `docs/architecture/AETHRION_IDEAL_STRUCTURE.md`. The six planes
> above govern *the research*; none of them measures *the lab's own capacity to
> produce correct results*. In a model-operated lab that measurement is not
> optional, because the correlated-error assumption underpinning independent
> review is otherwise untested.

## Canonical ownership

| Information | Canonical owner | View / derivative |
|---|---|---|
| Workflow and gate state | Temporal | Cockpit, NATS, dashboard |
| Project/task metadata | PostgreSQL Project Registry | Neo4j, dashboard |
| Bibliographic identity and status | Source Registry / PostgreSQL | Zotero, Obsidian |
| Human bibliographic notes | Zotero human fields | Source Registry ingest view |
| Claim/evidence | Claim Ledger / PostgreSQL | Neo4j, reports, Obsidian links |
| Code/policy/schema | Git | OCI image, deployed bundle |
| Dataset / large artifact | Object store + immutable manifest | MLflow and cache |
| Experiment/eval | MLflow + Run Registry | Grafana / reports |
| Human synthesis | Obsidian Markdown + Git history | Derived concept graph |
| Model admission | Capability Registry | Router cache |
| Cost | Cost Ledger | Dashboard / forecast |

## Lifecycle

| Gate | Primary frozen output | Example of what blocks passage |
|---|---|---|
| G0 Intake | `IntakeRecord` | No purpose, owner or initial class |
| G1 Charter | `ProjectCharter` and `ControlPlan` | No testable outcome or decision right |
| G2 Protocol | `ProtocolManifest` | An open material assumption or stop rule |
| G3 Literature | `LiteratureSetManifest` | Missing identity, inclusion basis or locator |
| G4 Baseline | `BaselineBundle` / `FalsificationPlan` | Leakage, or no counter-test |
| G5 Execute | `RunManifest` and artifacts | Policy, budget, identity or lineage failure |
| G6 Review | `ReviewBundle` / disposition | An open critical finding or independence problem |
| G7 Repro | `ReproductionReport` | Missing manifest or out-of-tolerance result |
| G8 Decision | `DecisionRecord` | Invalid owner, delegation or rationale |
| G9 Publish | `PublicationPackage` | Missing claim lineage or citation audit |
| G10 Monitor | `MonitoringPolicy` / `ImpactCase` | Silent supersession or unprocessed impact |

Risk changes only gate **depth**. Gate identity and the requirement to produce a
`GateRecord` never change.

> **Proposed refinements.** Three additions are proposed in
> `docs/architecture/AETHRION_IDEAL_STRUCTURE.md`: a **G2b Analysis Plan** locked
> separately from the protocol; an **in-principle acceptance** at G2 so that G8
> cannot reject on the direction of the result; and splitting **G7 into G7a
> (deterministic reproduction) and G7b (distributional replication)**, which are
> different operations with different tolerances.

## Trust boundaries

- **Zone 0:** Humans and governance; MFA, named decisions, audit export.
- **Zone 1:** Control plane; Temporal, gate service, registries, policy decisions.
- **Zone 2:** Execution fabric; sandbox, broker, workload identity, egress proxy.
- **Zone 3:** Untrusted content; external documents, web, repositories and tool
  output under quarantine.

Zone transitions cannot occur without explicit identity, policy, schema and
audit.

## Invariants restated, 2026-08-22

Two invariants were reworded because their original form was either too strong or
too weak to enforce:

| Was | Is | Why |
|---|---|---|
| "No model at G5 and G7a" | **No agentic methodological discretion during a frozen execution** | The subject of an experiment may itself be a model. What is forbidden is an agent moving a threshold mid-run because the result looks wrong |
| "Independent verification required" | **Independent verification at R3; internally separated verification at R1/R2, declared as such** | With one operator the first form was unsatisfiable, so it blocked everything. See ADR-001 |

A third is added by ADR-003:

> **Untrusted content is data.** Control flow comes only from trusted intent;
> retrieved text may supply values but can never create actions or expand
> permissions. A detector is defence in depth, never the boundary.

And one from the role model:

> **A role is a function, not a person.** Independence is expressed as separation
> constraints on a `RoleBinding`, never as headcount.

## Invariants added by baseline v1.2.0

The invariants above constrain how the system **acts**. These constrain what may
be **believed** about what it produced, and they were added because the earlier
baseline could have been completed in full without any of them being exercised
once. Each names the scenario that tests it, so the invariant and its evidence
cannot drift apart.

> **No prose without a claim.** A factual publication assertion with no
> `ClaimVersion` behind it does not enter a package — ACC-52.

> **No number without a `VerifiedValue`**, and no `VerifiedValue` without an
> immutable evaluator output beneath it — ACC-53, ACC-77.

> **No evaluator controlled by its producer.** The producer has no read or write
> path to the evaluator source, the hidden material or the official metric. A
> boundary breach **invalidates the run** rather than lowering its score —
> ACC-54, ACC-55.

> **No confirmatory result without a plan frozen before it.** The claim ceiling
> lowers by record and never rises on the same data — ACC-56.

> **No reproduction in the producer's environment** — ACC-65.

> **No qualifying verdict from an unqualified verifier**, and "mechanical" means
> V0 and V1 only. A model-mediated result recorded as V0 is refused — ACC-61,
> ACC-62.

> **No failed experiment without a recorded outcome**, and an implementation,
> data, infrastructure or policy failure **never** refutes a hypothesis —
> ACC-63, ACC-64.

> **No hypothesis or principle mutated in place.** A change is a successor
> version naming its parent and its evolution operator — ACC-57.

> **No human intervention without an audit record**, and no timeout, learned
> preference, attention score or inbound message creates an approval — ACC-68,
> ACC-69.

> **No adapted mechanism without lineage** — a pinned commit, a licence read at
> the source, a characterisation suite written before the code moves, and a
> statement of what the mechanism may never decide — ACC-73, ACC-74.

> **Nothing the search graph computes is epistemic.** A selection score, a
> normalised rank or a tournament position allocates compute and can never be
> written into a claim, a value or a gate. `STOPPED_BY_BUDGET` satisfies no gate.

> **Only the evidence store may support a claim.** Search experience, procedural
> memory and principle memory may not, and a memory query that names no store is
> refused rather than silently widened — ACC-79.

**A control that has never been observed to refuse is not a control.** Every
critical detector in this set carries a known-positive that must fail and a
known-negative that must pass, and a suite in which a planted control stays
silent fails — regardless of what its clean result says.

## Invariants added by baseline v1.3.0

The v1.2.0 set constrains what may be **believed**. These constrain **how the
work is carried out** — and each exists because an efficiency argument would
otherwise be free to trade it away.

> **Substantial scientific execution stays multi-agent.** At least two
> epistemically independent cognitive contributions before synthesis, where
> independence is a five-dimension profile and not a count. Optimisation targets
> the communication graph, the context and the assurance route — **never the
> cohort** — ACC-081, `ADR-011`.

> **Peer output is embargoed until initial positions are sealed.** Anchoring is
> an effect, not a preference, and the seal is what makes independent agreement
> distinguishable from deference afterwards — ACC-082.

> **A majority cannot close a material challenge.** Convergence requires it
> answered, explicitly accepted as a limitation, or escalated — ACC-090.

> **The blackboard is deletable.** Inter-agent exchange is typed, delta-only and
> never canonical: deleting it must lose no scientific record, and no entry may
> be promoted to evidence or to a claim — ACC-085, `ADR-013`.

> **Budget degrades verbosity, never the cohort and never assurance.** A task
> that cannot afford its required assurance is `BLOCKED`, not completed more
> cheaply — ACC-099, ACC-101.

> **A verifier may abstain, and abstention escalates.** It satisfies no
> requirement, is not a failure, and its rate is a qualification metric. A route
> is never lowered by queue length or budget — ACC-108, ACC-109, `ADR-015`.

> **The human judges before the machine recommends.** The recommendation is
> unreachable through **every** interface until the preliminary assessment is
> sealed, and correcting never costs more effort than approving — ACC-110,
> ACC-112, `ADR-016`.

> **The frozen specification and the running code must still agree.** An
> unapproved major deviation cannot carry a confirmatory package forward —
> ACC-104, `ADR-018`.

> **Every contributing model invocation carries an execution fingerprint**, and a
> hosted black-box model does not yield an `EXACT` reproduction claim — ACC-115,
> ACC-116.

> **A benchmark score carries the conditions it was produced under.** A run that
> could have reached the answers is labelled, never reported clean, and never
> silently rerun for a cleaner one — ACC-118, `ADR-017`.

> **One canonical owner per kind of state.** Events, blackboard entries and
> derived projections cannot masquerade as canonical scientific state, and every
> projection rebuilds losslessly — ACC-119, `ADR-014`.

> **`UNKNOWN` is a legitimate failure classification.** A taxonomy that forces
> every failure into a named cause produces a register of misattributions —
> ACC-094.

**Two disciplines stay separate and composable.** A passing test is not a
confirmed hypothesis; a preregistered analysis is not correct code — `ADR-012`.

## Success invariants

1. Every material claim links, in a single query, to its source representation,
   evidence span, run, review and decision.
2. The same external side effect happens exactly once across retry and replay.
3. A reviewer can work from a frozen package without seeing the producer's trace.
4. A G7 clean-room run reproduces the defined tolerance from the frozen manifest,
   or marks the claim `CHALLENGED`.
5. No agent can write to a personal Zotero record; human fields are never
   silently overwritten.
6. Derived graphs and indexes can be rebuilt from canonical records from scratch.
7. A model snapshot change produces requalification and an explicit task impact
   assessment.
8. D3/D4 routes and T4/T5 actions fail closed.
9. At a hard budget limit no new expensive work opens; the workflow pauses without
   losing state.
10. Production cutover happens only when every commissioning evidence item is
    signed.

> **Structural constraint on invariant 4.** Current-generation hosted models do
> not carry date-suffixed snapshot identifiers, so a frozen manifest cannot pin
> one. Deterministic reproduction therefore requires local open-weight models
> with a weight-file hash. What can be pinned for hosted models is a **capability
> fingerprint** plus full input/output logging. See
> `docs/architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md`.
