# AIRL-OS Commissioning Programme

**Version:** 1.1
**Status:** Implementation and commissioning plan
**Purpose:** Bring the AIRL-OS target architecture into service through work
packages small enough to be assigned independently and closed with objective
evidence.

## 1. What this deliverable solves

This directory is not an architecture brochure. It is the execution system that
describes how architectural decisions become a working system. Each `WP-xxx`
file carries a single delivery responsibility; its dependencies, the work to be
done, the acceptance tests, the evidence package and the rollback behaviour all
live in that same file.

The programme is **developed and tested incrementally**, but it is not opened to
production with capabilities missing. Vertical slices may be built in sequence in
development and staging. Production cutover happens only with the target state
complete, all acceptance scenarios passed, two restore rehearsals performed, and
zero open critical findings.

## 2. Binding architectural decisions

- Temporal is the single process authority for the G0–G10 research lifecycle.
- LangGraph manages cognitive state **inside** a bounded agent task only.
- NATS JetStream carries post-commit integration events; it never holds gate state.
- Agents perform every external effect through the Tool Broker or the Execution
  Broker. An agent holds no credential directly.
- The Source Registry is the canonical owner of bibliographic identity,
  deduplication, status and trust.
- Zotero is a personal and team working surface: the personal library is a
  read-only seed, group libraries are a controlled collaboration view.
- `LiteratureSetManifest` is written to an immutable object store as a Source
  Registry snapshot; a Zotero collection is a human-readable mirror only.
- Obsidian is the canonical working surface for human synthesis; generated areas
  can never overwrite human areas.
- The Claim/Evidence Ledger is the canonical owner of the claim, evidence span,
  dependency, review, decision and supersession chain.
- Risk/assurance, execution, independence and claim assessment are **separate
  profiles**. They are never collapsed into a single combinatorial score.
- Producer, reviewer and reproducer separation is enforced by a machine-checkable
  `IndependenceProfile`.
- The D0–D4 data class alone does not select a sandbox. Data class, code trust,
  tool effect and network/credential scope together produce an `ExecutionProfile`.
- G10 is not a single workflow living for years; a Temporal Schedule launches
  short-lived `ImpactScan` runs.
- Platform Assurance cuts horizontally across every layer, validating the system
  itself through policy, workflow, broker, restore and golden-path tests.

## 3. Directory structure

| Path | Contents |
|---|---|
| `00_PROGRAM/` | Programme charter, target state, wave plan, RACI, DoR/DoD, evidence and change control |
| `01_GOVERNANCE/` | WP-001–010: governance and policy design |
| `02_CONTRACTS/` | WP-011–020: identity, schema, record and contract foundation |
| `03_FOUNDATION/` | WP-021–030: environment, repository, CI, data and platform backbone |
| `04_CONTROL_EVENT/` | WP-031–040: Temporal, G0–G10, event and replay |
| `05_MODEL_AGENT_TOOL/` | WP-041–050: gateway, admission, agent runtime and broker |
| `06_EXECUTION_SECURITY/` | WP-051–060: trust zones, compute, identity, policy and security |
| `07_LITERATURE_KNOWLEDGE/` | WP-061–074: Source Registry, Zotero, literature and Obsidian |
| `08_EVIDENCE_ASSURANCE/` | WP-075–090: evidence, claims, experiments, review and reproduction |
| `09_EXPERIENCE_OBSERVABILITY/` | WP-091–101: cockpit, decision UI, telemetry and FinOps |
| `10_INTEGRATION_CUTOVER/` | WP-102–121: vertical slices, commissioning and production cutover |
| `11_DAY2_OPERATIONS/` | WP-122–130: continuous operation and assurance |
| `12_ACCEPTANCE_SCENARIOS/` | ACC-01–ACC-40: Given/When/Then system acceptance scenarios |
| `13_TOOLING_INTEGRATION/` | WP-131–140: notification, communication, external records, evidence sealing and liveness |

## 4. Package status model

```text
BACKLOG → READY → IN_PROGRESS → TECH_COMPLETE → EVIDENCE_REVIEW
        → ACCEPTED → INTEGRATED → COMMISSIONED
                     ↘ REVISE / BLOCKED
```

- `READY`: Definition of Ready is complete; owner and dependencies are settled.
- `TECH_COMPLETE`: code and configuration are done but nothing is accepted yet.
- `EVIDENCE_REVIEW`: package tests and evidence manifest are under independent
  verification.
- `ACCEPTED`: package-level acceptance criteria have passed.
- `INTEGRATED`: contract tests against dependent systems have passed.
- `COMMISSIONED`: the related end-to-end acceptance scenarios have also passed.

A "done" declaration by an agent or an implementer can only mean
`TECH_COMPLETE`. The `ACCEPTED` decision belongs to the independent verifier
named in the package.

## 5. Effort codes

| Code | Initial estimate | Use |
|---|---:|---|
| XS | 0.5–2 person-days | A single schema, policy or small configuration |
| S | 2–5 person-days | A bounded delivery inside one service |
| M | 5–10 person-days | One service or one integration slice |
| L | 10–20 person-days | Multiple systems plus failure-path testing |

No package should default to larger than L. A package that comes out above L in
refinement is split. An estimate is not a calendar commitment; it becomes a date
through the capacity model in `00_PROGRAM/08_CAPACITY_AND_ESTIMATION.md`.

## 6. Order of work

1. Read the scope in `00_PROGRAM/01_TARGET_STATE_AND_INVARIANTS.md`.
2. Select the current wave from `00_PROGRAM/02_WAVE_AND_DEPENDENCY_MAP.md`.
3. Take a package whose dependencies are closed from
   `00_PROGRAM/03_PACKAGE_CATALOGUE.md`.
4. Run the DoR check in the package file and assign a named owner.
5. Make only the change within the package's scope.
6. Run the tests, produce the evidence manifest, and send it to independent
   verification.
7. Bind the accepted package to integration and acceptance scenarios.

## 7. Starting command

The first executable point of the programme is `WP-001 Commissioning Charter`.
No technology installation begins before WP-001 is accepted; otherwise
environment, security and team choices advance without a scope authority.

> **Known blocker.** Every package's Definition of Done requires a signed
> `EvidenceManifest` written to an immutable store — but the immutable store is
> WP-026, far downstream. As written, no package including WP-001 can reach
> `ACCEPTED`. Resolving this requires an interim evidence policy (proposed as
> **WP-000**) before the programme can start. See the audit report in
> `docs/review/`.
