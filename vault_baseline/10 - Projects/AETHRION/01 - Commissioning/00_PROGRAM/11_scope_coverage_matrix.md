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
| The forty-six acceptance scenarios | WP-109–114, `12_ACCEPTANCE_SCENARIOS/` | WP-115 |
| Chaos / capacity / operational readiness | WP-116–118 | WP-119–120 |
| Pilot / cutover / hypercare | WP-119–121 | Production |
| Continuous assurance and operations | WP-122–130 | Day-2 control evidence |
| **Notification and human reachability** | **WP-131–135** | **ACC-25, ACC-26, ACC-41–43** |
| **Inbound content and external feeds** | **WP-136–137** | **ACC-04, ACC-05, ACC-31, ACC-36, ACC-44** |
| **External records and evidence sealing** | **WP-138–139** | **ACC-23, ACC-30, ACC-40, ACC-45** |
| **Service liveness** | **WP-140** | **ACC-43** |

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
| Skill bundle governance | The the skill registry change agent behaviour and are not under configuration control | Alongside WP-047 |

## Completeness rule

When a new architecture area or binding invariant is added, the change is not
promoted to baseline until this matrix carries **a primary implementation
package, an integration package, and acceptance/operations evidence** for it.

A row that lists a primary package but leaves the acceptance column empty is an
incomplete entry, not a shorter one.
