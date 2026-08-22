# AETHRION Commissioning Programme

**Version:** 1.1
**Status:** Implementation and commissioning plan
**Purpose:** Bring the AETHRION target architecture into service through work
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

## 3. Inventory

| Item | Count |
|---|---:|
| Bootstrap package | **1** (WP-000) — precedes the programme, depends on nothing |
| Work packages | **140** (WP-001 – WP-140) |
| Work package documents in total | **141** |
| Acceptance scenarios | **51** (ACC-01 – ACC-51) |
| Programme documents | 12 |
| Markdown files under this tree | 220 |
| Files covered by the hash seal | 221 (220 Markdown + 1 CSV) |

> **Commissioning baseline v1.0.2 — 2026-08-22.** This is the baseline the
> programme will actually be commissioned against. Everything after this point
> is a **recorded change**: edit the canonical file, regenerate the seal
> deliberately, and record the change in the implementation log. Improvements
> are expected to arrive *while running*, not before starting.
>
> **v1.0.1 corrected three semantic defects that the hash seal could not see** —
> acceptance identifiers colliding with the numbers the tooling packages already
> referenced, a go-live requirement that depended on Day-2 packages scheduled
> after go-live, and stale ranges left behind when the scenario count changed.
> The seal proves files did not change; it says nothing about whether they agree
> with each other. `scripts/validate_commissioning_plan.py` now checks that, and
> **both checks must pass** before the plan is considered valid.
>
> **v1.0.2 carries the project's current name.** 29 files changed: the product
> is AETHRION rather than AIRL-OS, and ten architecture documents moved to
> filenames that say so. No requirement, identifier, dependency, acceptance
> phase or scenario was touched — `git diff v1.0.1..v1.0.2 -- planning/` is
> naming only. The seal was regenerated deliberately as part of this recorded
> change, which is the one sanctioned reason to regenerate it; re-sealing to
> silence a failing check remains prohibited. Both the seal and
> `validate_commissioning_plan.py` pass on the new baseline.

Verify the seal from the repository root:

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

Every entry must report `OK`. The seal is regenerated deliberately, as part of a
recorded change — never as a routine step to silence a failing check.

## 3.1 How to navigate

Every workstream directory carries a **generated** README listing its packages,
their dependencies, their status and whether they stand on an adopted component.
Regenerate with `python3 scripts/make_plan_indexes.py`; the build checks them
with `--check`.

### Programme documents, and the question each answers

| Document | Answers |
|---|---|
| [`00_how_to_use_this_plan.md`](00_PROGRAM/00_how_to_use_this_plan.md) | How is this plan executed and verified? |
| [`01_target_state_and_invariants.md`](00_PROGRAM/01_target_state_and_invariants.md) | What is being built, and what must never break? |
| [`02_wave_and_dependency_map.md`](00_PROGRAM/02_wave_and_dependency_map.md) | In what order, and after what? |
| [`03_package_catalogue.md`](00_PROGRAM/03_package_catalogue.md) | What is every package, in one place? |
| [`04_role_and_responsibility_matrix.md`](00_PROGRAM/04_role_and_responsibility_matrix.md) | Who is accountable, and which roles may combine? |
| [`05_definition_of_ready_and_done.md`](00_PROGRAM/05_definition_of_ready_and_done.md) | When may a package start, and when is it accepted? |
| [`06_evidence_and_acceptance_strategy.md`](00_PROGRAM/06_evidence_and_acceptance_strategy.md) | What counts as evidence? |
| [`07_programme_risk_register.md`](00_PROGRAM/07_programme_risk_register.md) | What is likely to go wrong, and what already has? |
| [`08_capacity_and_estimation.md`](00_PROGRAM/08_capacity_and_estimation.md) | Is there capacity to do this? |
| [`09_change_and_configuration_control.md`](00_PROGRAM/09_change_and_configuration_control.md) | How does the plan itself change without drifting? |
| [`10_go_live_checklist.md`](00_PROGRAM/10_go_live_checklist.md) | What must be true before cutover? |
| [`11_scope_coverage_matrix.md`](00_PROGRAM/11_scope_coverage_matrix.md) | Is anything in scope not covered by a package? |
| [`12_ACCEPTANCE_SCENARIOS/acceptance_scenarios_index.md`](12_ACCEPTANCE_SCENARIOS/acceptance_scenarios_index.md) | All 51 scenarios, by severity and phase |

## 4. Directory structure

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
| `12_ACCEPTANCE_SCENARIOS/` | ACC-01–ACC-51: Given/When/Then system acceptance scenarios, including ACC-41–46 skill governance |
| `13_TOOLING_INTEGRATION/` | WP-131–140: notification, communication, external records, evidence sealing and liveness |

## 5. Package status model

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

## 6. Effort codes

| Code | Initial estimate | Use |
|---|---:|---|
| XS | 0.5–2 person-days | A single schema, policy or small configuration |
| S | 2–5 person-days | A bounded delivery inside one service |
| M | 5–10 person-days | One service or one integration slice |
| L | 10–20 person-days | Multiple systems plus failure-path testing |

No package should default to larger than L. A package that comes out above L in
refinement is split. An estimate is not a calendar commitment; it becomes a date
through the capacity model in `00_PROGRAM/08_capacity_and_estimation.md`.

## 7. Order of work

1. Read the scope in `00_PROGRAM/01_target_state_and_invariants.md`.
2. Select the current wave from `00_PROGRAM/02_wave_and_dependency_map.md`.
3. Take a package whose dependencies are closed from
   `00_PROGRAM/03_package_catalogue.md`.
4. Run the DoR check in the package file and assign a named owner.
5. Make only the change within the package's scope.
6. Run the tests, produce the evidence manifest, and send it to independent
   verification.
7. Bind the accepted package to integration and acceptance scenarios.

## 8. Starting command

The programme starts in two steps, and the order is not negotiable:

```
BOOTSTRAP PHASE
  WP-000  Interim Evidence Policy and Attestation Bootstrap
          depends on nothing · makes acceptance possible at all
        ↓
PROGRAMME START
  WP-001  Commissioning Charter and Programme Authority
          the first normal commissioning package
        ↓
  WP-002 ...
```

**WP-000 is the bootstrap package; WP-001 remains the first normal commissioning
package.** No technology installation begins before WP-001 is accepted;
otherwise environment, security and team choices advance without a scope
authority. And WP-001 cannot be accepted before WP-000 exists, because until
then no package can produce acceptable evidence at all.

> **Known blocker — half resolved.** Every package's Definition of Done requires
> a signed `EvidenceManifest` written to an immutable store — but the immutable
> store is WP-026, far downstream. As written, no package including WP-001 could
> reach `ACCEPTED`.
>
> [**WP-000 — Interim Evidence Policy and Attestation Bootstrap**](01_GOVERNANCE/WP-000_interim_evidence_policy.md)
> now closes the storage half: the manifest is issued as a signed in-toto
> attestation recorded in a public transparency log and anchored in time, so
> immutability is delegated rather than deferred. The rationale is in
> `docs/architecture/AETHRION_EXTERNAL_STANDARDS.md` §3.
>
> The other half — finding **C2**, who may act as an independent verifier in a
> one-person operation — is **still open** and is a decision, not code. See the
> audit report in `docs/review/`.
