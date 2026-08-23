---
title: "Architecture Scope → Work Package Coverage Matrix"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/11_scope_coverage_matrix.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Architecture Scope → Work Package Coverage Matrix

This matrix is the fast audit for one question: **"has any component or
governance area been left out of the plan?"** Detailed dependencies live in
`03_package_catalogue.md` and `package_dependency_matrix.csv`.

Read a row as: *primary packages build the capability; integration/acceptance
packages prove it works in context.* A row with a primary package but no
acceptance column is a capability nobody will ever be asked to demonstrate.

| Target architecture area | Primary work packages | Integration / acceptance |
|---|---|---|
| Programme, scope, NFR, ADR | WP-001–002, WP-010 | WP-115, WP-120 |
| Roles, RACI, human decision | WP-003–004 | WP-102, WP-106, ACC-25–26 |
| Risk and assurance | WP-005, WP-008 | WP-102, WP-105 |
| ExecutionProfile: data / code / effect / network | WP-006 | WP-112, ACC-15–18 |
| Independence matrix | WP-007 | WP-105, ACC-06–08, ACC-38 |
| Control and exception | WP-009, WP-016, WP-056 | WP-112, WP-123 |
| Identity and correlation | WP-011 | WP-096, ACC-40 |
| Canonical field authority | WP-012 | WP-103, ACC-03/22/28 |
| Task / role / agent contracts | WP-013, WP-047 | WP-102, WP-107 |
| Artifact and dataset immutability | WP-014, WP-026 | WP-104, ACC-23 |
| Event / outbox / NATS | WP-015, WP-028, WP-039 | WP-111, ACC-12/34 |
| Source and literature schemas | WP-017 | WP-061–072 |
| Claim / review / decision schemas | WP-018 | WP-075–090 |
| Run / environment / reproduction schemas | WP-019 | WP-081–085 |
| Schema registry and SDK | WP-020 | Every service contract test |
| Dev / staging / prod and network | WP-021, WP-051 | WP-112/114/119 |
| Repository / worktree / CI | WP-022–024 | WP-107 |
| PostgreSQL / object store / MLflow | WP-025–026, WP-029 | WP-104/114 |
| Derived graph / vector / search | WP-030 | WP-095, ACC-21 |
| Temporal and G0–G10 | WP-031–040 | WP-102–106, ACC-13–14 |
| LiteLLM / capability / admission | WP-041–045 | WP-124, ACC-10/11/36/37 |
| LangGraph and runtime adapter | WP-046–048 | WP-107 |
| Tool Broker and connectors | WP-049–050 | ACC-05/12/35 |
| Kubernetes / Kueue / gVisor | WP-052–054 | WP-116/117, ACC-15/33 |
| SPIFFE / Vault / OPA / egress | WP-055–057 | WP-112, ACC-16/18/25/26/32 |
| Content quarantine | WP-058 | ACC-05 |
| Sigstore / SLSA / supply chain | WP-027, WP-059 | ACC-17 |
| Agentic red team | WP-060 | WP-112/123 |
| Source Registry / resolver / status | WP-061–063 | WP-103/108, ACC-03/04 |
| Zotero library / seed / write / sync | WP-064–068 | WP-103/125, ACC-01/02/03/28 |
| Two-way literature flow and screening | WP-069–071 | WP-103, ACC-01–03 |
| Immutable `LiteratureSetManifest` | WP-072 | WP-103/106, ACC-01/30 |
| Obsidian human and generated zones | WP-073–074 | WP-113/125, ACC-22 |
| Claim / Evidence Ledger | WP-075–080 | WP-104–106, ACC-04/08/30 |
| Protocol / run / experiment | WP-081–083 | WP-104, ACC-09/33/39 |
| Clean-room and the four verification types | WP-084–085 | WP-105/113, ACC-19/20 |
| Blind review / verifier / arbitration | WP-086–089 | WP-105/126, ACC-06/07/08/38 |
| Publication and RO-Crate | WP-090 | WP-106, ACC-30/31/40 |
| Cockpit / decision / literature / claim UI | WP-091–095 | Vertical slices and pilot |
| OpenTelemetry / Langfuse / Grafana | WP-096–098 | WP-116/121/122 |
| WORM audit | WP-099 | ACC-40 |
| Cost and FinOps | WP-100 | WP-111/127, ACC-09/29 |
| Service SLO and runbooks | WP-101 | WP-118/122 |
| Vertical integration | WP-102–108 | WP-109–115 |
| The fifty-one acceptance scenarios | WP-109–114, `12_ACCEPTANCE_SCENARIOS/` | WP-115 |
| Chaos / capacity / operational readiness | WP-116–118 | WP-119–120 |
| Pilot / cutover / hypercare | WP-119–121 | Production |
| Continuous assurance and operations | WP-122–130 | Day-2 control evidence |
| **Notification and human reachability** | **WP-131–135** | **ACC-25, ACC-26, ACC-41–43** |
| **Inbound content and external feeds** | **WP-136–137** | **ACC-04, ACC-05, ACC-31, ACC-36, ACC-44** |
| **External records and evidence sealing** | **WP-138–139** | **ACC-23, ACC-30, ACC-40, ACC-45** |
| **Service liveness** | **WP-140** | **ACC-43** |
| **Upstream assimilation and lineage** | **WP-141**, WP-059 | **ACC-73, ACC-74** |
| **Study mode, bottleneck and idea framing** | **WP-142**, WP-005, WP-034 | **ACC-56** |
| **Hypothesis and principle evolution** | **WP-143**, WP-018 | **ACC-57** |
| **Discovery search graph and candidate lifecycle** | **WP-144**, WP-082 | **ACC-58, ACC-64** |
| **Search allocation, fusion and stopping** | **WP-145**, WP-083, WP-100 | **ACC-09, ACC-59** |
| **Epistemic memory taxonomy and retention** | **WP-146**, WP-026, WP-125 | **ACC-70, ACC-79** |
| **Specialist cognition without authority** | **WP-147**, WP-007, WP-086 | **ACC-06, ACC-72** |
| **Frozen evaluator and verified values** | **WP-082–084** | **ACC-53, ACC-54, ACC-55, ACC-60, ACC-77** |
| **Verification taxonomy and verifier qualification** | **WP-087**, WP-044, WP-126 | **ACC-61, ACC-62, ACC-76** |
| **Standalone reproduction and claim consistency** | **WP-085** | **ACC-65, ACC-66, ACC-67** |
| **Publication compiler and assertion binding** | **WP-090**, WP-080 | **ACC-52, ACC-76** |
| **Human intervention audit and attention priority** | **WP-004**, WP-038, WP-093 | **ACC-68, ACC-69** |

| **Multi-agent cohort integrity** | **WP-148**, WP-007, WP-047 | **ACC-081, ACC-082, ACC-089, ACC-090** |
| **Sparse topology and the scientific blackboard** | **WP-149**, WP-015 | **ACC-083, ACC-084, ACC-085, ACC-086** |
| **Communication governance and context projection** | **WP-150**, WP-096, WP-100 | **ACC-086, ACC-087, ACC-088** |
| **Memory masking and proactive intervention** | **WP-151**, WP-146 | **ACC-096, ACC-097, ACC-098** |
| **Failure taxonomy, attribution and resilience** | **WP-152**, WP-082, WP-128 | **ACC-091, ACC-092, ACC-094, ACC-095** |
| **Research budget, token ledger and efficiency** | **WP-153**, WP-100, WP-145 | **ACC-099, ACC-100, ACC-101, ACC-102** |
| **Engineering discipline and spec conformance** | **WP-154**, WP-107, WP-081 | **ACC-103, ACC-104** |
| **Adaptive assurance and escalation** | **WP-155**, WP-087, WP-126 | **ACC-107, ACC-108, ACC-109** |
| **Human oversight debiasing** | **WP-156**, WP-004, WP-093 | **ACC-110, ACC-111, ACC-112** |
| **Reproduction determinism and model fingerprint** | **WP-157**, WP-084, WP-085 | **ACC-113, ACC-114, ACC-115, ACC-116** |
| **Benchmark firewall and evaluation isolation** | **WP-158**, WP-043, WP-057 | **ACC-118** |
| **Supply chain, upstream drift and cross-plane integrity** | **WP-159**, WP-024, WP-059, WP-141 | **ACC-119, ACC-120** |
| **Prompt injection and the capability gate** | **WP-058**, WP-060, WP-136 | **ACC-005, ACC-044, ACC-117** |

## Areas identified by the audit as not yet covered

These have no primary package. They are listed here rather than omitted, because
an uncovered area that is *named* is a scheduling decision, while an uncovered
area that is unnamed is an accident.

| Area | Why it matters | Proposed home |
|---|---|---|
| Interim evidence policy | Without it, no package can ever reach `ACCEPTED` — the plan cannot start | **WP-000**, ahead of Wave 0 |
| Agreement and error-correlation measurement | Independence is asserted throughout but measured nowhere | Metascience plane, alongside WP-007 |
| Confidence calibration | Confidence numbers appear in contracts with no measurement basis | Metascience plane |
| Control injection (positive and negative) | The lab's own false-positive and false-negative rates are unknown | Metascience plane |
| Attention-budget telemetry | Human decision capacity is the binding constraint and is untracked | Alongside WP-004 / WP-091 |
| Skill bundle governance | The skills in the registry change agent behaviour and are not under configuration control | Alongside WP-047 |

### Closed by baseline v1.2.0

Three rows left this table when the scientific-intelligence workstream opened.
They are recorded here rather than deleted, because a row that quietly disappears
and a row that was addressed look identical afterwards.

| Area | Now covered by |
|---|---|
| Assimilation of external mechanisms — previously ad hoc, with no register and no licence position per file | **WP-141**, `provenance/upstreams.json`, ADR-004, ACC-73–74 |
| What the system remembers, and which store may support a claim — previously one undifferentiated notion of memory | **WP-146**, ADR-005, ACC-70, ACC-79 |
| The meaning of "verify" where the verifier is a model — previously one word covering a hash comparison and a semantic judgement | **WP-087** revised, ADR-008, ACC-61–62, ACC-76 |

### Closed by baseline v1.3.0

| Area | Now covered by |
|---|---|
| How a cohort of agents collaborates — previously an unmodelled assumption that more agents was better | **WP-148–150**, ADR-011, ADR-013, ACC-081–090 |
| What happens when an agent is wrong, faulty or adversarial — previously handled only as an ordinary task failure | **WP-152**, ACC-091–095 |
| Whether the implementation still matches the frozen method — previously assumed, and checked by neither reviewer | **WP-154**, ADR-018, ACC-103–104 |
| Whether a benchmark score means anything — previously reported without the conditions it was produced under | **WP-158**, ADR-017, ACC-118 |
| Whether a human decision was a judgement or a ratification — previously unmeasurable | **WP-156**, ADR-016, ACC-110–112 |

## Completeness rule

When a new architecture area or binding invariant is added, the change is not
promoted to baseline until this matrix carries **a primary implementation
package, an integration package, and acceptance/operations evidence** for it.

A row that lists a primary package but leaves the acceptance column empty is an
incomplete entry, not a shorter one.
