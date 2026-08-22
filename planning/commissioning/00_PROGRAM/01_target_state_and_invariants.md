# Target State, System Boundary and Invariants

## Target operating outcome

When AIRL-OS is in service, a research request travels from G0 to G10 in a
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
> proposed in `docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md`. The six planes
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
> `docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md`: a **G2b Analysis Plan** locked
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
> `docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md`.
