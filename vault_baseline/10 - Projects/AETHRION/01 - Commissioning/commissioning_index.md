---
title: "AETHRION Commissioning Programme"
cssclasses:
  - aethrion-index
type: index
category: commissioning
source: "planning/commissioning/README.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/index
---

# AETHRION Commissioning Programme

**Version:** 1.4
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
| Work packages | **159** (WP-001 – WP-159) |
| Work package documents in total | **160** |
| Test procedure documents | **160** — one per package, `*.tests.md` |
| Acceptance criteria documents | **160** — one per package, `*.acceptance.md` |
| Acceptance scenarios | **120** (ACC-01 – ACC-120) |
| Programme documents | 12 |
| Markdown files under this tree | 630 |
| Files covered by the hash seal | 632 (630 Markdown + 1 CSV) |

> ### What V1 is
>
> **V1 is this plan.** Its scope is the sealed baseline below — WP-000–159 and
> ACC-01–120, exactly the files the seal covers and nothing else. Its completion
> criterion is already written and mechanical:
> [`00_PROGRAM/10_go_live_checklist.md`](00_PROGRAM/10_go_live_checklist.md) —
> every `PRE_GO_LIVE` scenario passing on **one** release candidate, zero open
> critical findings, and a signed go-live `DecisionRecord`. V1 is finished when
> those conditions hold, and not before.
>
> **V2 is everything proposed after the freeze.** "Should we add this too?" and
> "let's do that differently" are V2 questions by definition, and they have a
> home outside the seal:
> [`docs/V2_CANDIDATES.md`](../04 - Architecture/aethrion_v2_candidates.md).
>
> The distinction that governs which is which: **a correction keeps the finish
> line where it is; an addition moves it.**
>
> ### v1.2.0 moved it, once, on purpose
>
> Baseline v1.2.0 added a workstream and twenty-nine scenarios. By the rule
> above that is an addition, not a correction, and it is recorded as one: the
> finish line moved, the minor version was bumped rather than the patch version,
> and this paragraph exists so that nobody later reads the change as
> housekeeping.
>
> **Why it was taken inside V1 rather than parked.** The register exists to stop
> a plan absorbing every good idea, and it has done that job — six entries after
> a full brand migration, all of them cosmetic renames. But the earlier baseline
> had a gap that parking would have preserved rather than deferred. It tested
> the *platform* thoroughly: isolation, replay, budget stops, supply chain,
> notification ceilings. It did not test the *epistemic path*. Nothing in
> ACC-01–51 refused a publication sentence with no claim behind it, a reported
> number with no verified value under it, a producer editing the evaluator that
> scores it, a compile error recorded as a refuted hypothesis, or a reproduction
> run in the environment that produced the result.
>
> Those are the failures this architecture exists to prevent. The plan could
> have been completed in full, every scenario passing, without one of them being
> caught. That is a defect in what the baseline verifies, and a baseline whose
> completion would not demonstrate the thing it was built for is not finishable
> in any sense worth having.
>
> **And it was the cheapest possible moment.** Nothing is `ACCEPTED`; one
> package is `READY`; no work has been done against the old finish line. The
> same change made after a year of execution would have reopened a plan with
> completed work measured against it.
>
> The rule is unchanged and still binding for the next proposal. Moving the
> finish line is a thing that happens with a version bump, a tag and a stated
> reason — not twice, and not quietly.

> **Commissioning baseline v1.3.3 — 2026-08-24.** A refinement baseline, and
> the classification is the first thing it had to settle. `AGENTS.md` §7.4: a
> correction keeps the finish line where it is, an addition moves it. **No
> package, no scenario and no capability is added.** WP-148 already had to
> deliver a collaboration plane; naming the contract it is delivered behind is
> *how*, not *what*, and every product idea that would have expanded scope —
> a desktop cockpit, voice collaboration, mobile control, a draft delegation
> protocol as canonical attribution — went to `docs/V2_CANDIDATES.md` instead.
>
> What it settles: most of what the collaboration plane needs is not scientific
> work. Identities, rooms, message transport, presence and runtime attachment are
> adopted behind a `CollaborationBackend` contract with **Buzz** as the first
> candidate; agent harnesses are adopted behind an `AgentRuntime` contract with
> **Hermes** preferred and not exclusive; and `ADR-020` fixes what neither may
> ever decide **before** any code moves, which is the only point at which fixing
> it is cheap.
>
> Nine packages change in the sealed tree — WP-046, WP-047, WP-048, WP-148,
> WP-149, WP-150, WP-153, WP-154 and WP-159 — gaining the boundary, the
> compile-time refusals, the fifteen-behaviour backend characterisation, the
> backend-loss proof and the guard that a `DONE` message is not a package state.
> Nineteen new test cases and twenty-one acceptance criteria are negative: the
> integration is proven by what it refuses, not by two agents exchanging a
> message.
>
> **The licence was not read, and the register said so.** The change
> specification proposed direct adaptation of an orchestration manifest and
> reported the upstream as Apache-2.0. No licence can be read at the source from
> a session with no network, and `check_upstream_lineage.py` R7 refuses a direct
> adaptation under an unverified one — so `ASM-060` is registered as a `PATTERN`,
> the mode that moves no files. The checker refusing a proposal from outside the
> repository is the control working, not an obstacle to route around.
>
> Also closed here, and found on the way: `obra/superpowers` — eleven skills
> vendored verbatim, the largest thing in this repository taken from someone
> else — was recorded only in `NOTICE` and in no register at all. It is now
> `ASM-066` under a new `VENDORED` mode, because verbatim inclusion is neither
> adaptation nor reimplementation and calling it either misstates the obligation.

> **v1.3.2** was a repair baseline, and the
> rule that decides it is `AGENTS.md` §7.4: a correction keeps the finish line
> where it is, an addition moves it. **No package, no scenario and no capability
> is added.** Every acquisition decision this baseline projects into a package
> was already taken — in `AETHRION_COMPONENT_REUSE.md`, in `ADR-004` or in the
> package that owns the integration. What was missing was the **binding**.
>
> The plan decided what to adopt, what to copy and refactor under a licence, and
> what to reimplement from a specification. Those decisions lived in the
> architecture corpus; the work lived in a package document; nothing joined
> them. So `WP-144` specified a candidate state machine over seven tasks while
> AIDE sat in the register as its `DIRECT_ADAPT` source, unnamed by the package —
> an implementer reading only the package would have rewritten a mechanism the
> architecture had already decided to take. `WP-153` specified a nine-dimensional
> budget ledger without naming BATS. And the reverse defect was worse: `WP-041`
> is titled *LiteLLM Model Gateway Foundation* and no register knew LiteLLM
> existed, so the component had no version policy, no failure semantics and no
> statement of what it may never decide.
>
> What this baseline changes in the sealed tree:
>
> - Every package card gains **Implementation acquisition and assimilation**, a
>   generated block naming each bound source, its mode, what is taken, what
>   AETHRION still owns, what the source may never decide, and the obligation the
>   mode creates that nobody has met yet. `BUILD_NATIVE` is stated rather than
>   left to silence, because silence cannot distinguish a package with no
>   upstream from a package whose upstream nobody recorded.
> - Every package card's **Definition of Ready** gains the acquisition
>   precondition, and `00_PROGRAM/05` states why it gates `READY` rather than
>   `TECH_COMPLETE`.
>
> Outside the seal: `provenance/components.json` makes the runtime-component
> decisions machine-readable for the first time, `scripts/expand_acquisition.py`
> projects both registers into the packages, and
> `scripts/check_wp_implementation_sources.py` checks the binding in both
> directions with a `--self-test` per rule. `scripts/ready_queue.py` now holds a
> package out of *Ready now* while an obligation is open.
>
> **No entry moved to `ADAPTING` and no code was copied.** Every obligation is
> reported as open, which is the honest state: no commit is pinned, no
> characterisation suite exists, and no `MS-*` mechanism specification has been
> written anywhere in this repository.

> **v1.3.1** was a repair baseline: no package,
> no scenario and no capability added. It closes the integration defects that
> made v1.3.0's plan unexecutable — two pre-go-live packages depending on Day-2
> packages, two cutover aggregators binding two scenarios where they meant 118,
> and a WP↔ACC relation with two owners disagreeing on 98 of 120 scenarios — and
> it adds the four controls that would have caught each of them. The canonical
> programme model now lives in
> [`00_PROGRAM/programme_metadata.json`](00_PROGRAM/programme_metadata.json) and
> the phase, wave and selector columns of the dependency matrix.
>
> **v1.3.0** was the baseline the
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

> **v1.0.3 removes a false assurance claim.** Three programme documents said the
> `EvidenceManifest` is recorded in a public transparency log. It is not: WP-000
> runs the `airl-interim-v0.1` profile, which signs with a local key and
> explicitly does not submit to a log — WP-000 §5 always said so, and the
> summaries above it did not. The same three files still called finding **C2**
> an open decision after `ADR-001` decided it. Naming only; no requirement,
> identifier, dependency, acceptance phase or scenario changed. Found by a
> stale-claim checker that had to be widened first, because the old one was a
> list of literals and could not see either defect.

> **v1.0.4 names the baseline as V1 and gives V2 a home.** The plan already
> defined its own completion — `10_go_live_checklist.md` has said since v1.0
> exactly which conditions must hold — but nothing called that "V1", and the
> change-control document told readers to run `git diff v1.0.1..v1.0.3` when no
> such tags existed. Both are fixed: the baselines are tagged in git, the scope
> and completion criterion are stated in one place, and additions now go to
> `docs/V2_CANDIDATES.md` outside the seal. Two paragraphs of text; no
> requirement, identifier, dependency, acceptance phase or scenario changed.

> **v1.0.5 separates progress from the plan, so the programme can actually be
> run.** Every package's `Current status` field is now `Status at baseline`, and
> execution state moved to `delivery/progress.json` **outside the seal**. Until
> this change, starting work on WP-001 would have broken the seal — the
> specification's integrity proof would have been invalidated by progress against
> that specification, and the only way to keep it green would have been to
> re-seal on every status change, which change control prohibits. 141 field
> labels, 14 regenerated indexes; no requirement, dependency, identifier,
> acceptance phase or scenario changed. `docs/READY.md` now answers *what can be
> started today* — one package, WP-001.

> **v1.2.0 opens the scientific-intelligence workstream — the first change that
> moves the finish line.** Every baseline before it was a correction: naming,
> a false assurance claim, a mislabelled field, a status column in the wrong
> file. This one adds capability, and it says so in the minor version rather
> than arriving as a v1.1.1 nobody would look at twice.
>
> What it adds: `14_SCIENTIFIC_INTELLIGENCE` with **WP-141–147**, and
> **ACC-52–80**. The packages cover study mode and idea framing, hypothesis and
> principle evolution, the discovery search graph, how that search is allocated
> and stopped, the six epistemic memories, and specialist cognition that
> recommends without deciding. The scenarios cover the epistemic failures V1
> could not catch.
>
> What it does **not** do: renumber anything. Every V1 identifier means what it
> meant, every V1 dependency still resolves, and no acceptance phase changed.
> WP-141–147 append; ACC-52–80 append. The `v1.1.0` tag and its seal are intact,
> so the previous baseline can still be verified exactly as it stood.
>
> One structural rule came with it. The seven new packages describe mechanisms
> that other projects solved first, and **WP-141 makes taking one an auditable
> act**: a pinned commit, a named file list, a characterisation suite written
> before the code moves, a licence read at the source, and a statement of what
> the mechanism may never decide. The register is `provenance/upstreams.json`
> and `scripts/check_upstream_lineage.py` refuses an entry that skips any of it.

> **v1.3.0 adds the reliability layer, and moves the finish line a second time.**
> The rule in §3 says moving it should not happen twice without a reason as
> specific as the first. Here is the reason: v1.2.0 gave the plan an epistemic
> path and left the *execution* of that path unmodelled. It assumed a cohort of
> agents without saying what made one legitimate, assumed they would talk without
> bounding the cost, assumed a failure could be attributed, and assumed a human
> reading a recommendation was judging rather than ratifying.
>
> What it adds: `15_RELIABILITY_EFFICIENCY` with **WP-148–159**, and
> **ACC-081–120**. The cohort invariant and what independence means; typed
> delta-only exchange over a compiled sparse topology; a governor with a quality
> guard that rolls back; memory masking by epistemic status; a failure taxonomy
> in which `UNKNOWN` is legitimate; a budget that degrades verbosity and never
> assurance; specification-to-code conformance; assurance routed by consequence
> with abstention; the human judging before the machine recommends; model
> execution fingerprints; a benchmark firewall; and cross-plane integrity.
>
> Nine decision records — **ADR-011 to ADR-019** — fix the decisions behind them.
> Two of the nine *extend* an existing record rather than adding one: ADR-015
> extends ADR-008's verification taxonomy with routing and abstention, and
> ADR-019 extends ADR-004's assimilation rules with the supply-chain toolchain.
>
> What it does **not** do: renumber anything. WP-148–159 append, ACC-081–120
> append, and the nine decision records took the next free numbers rather than
> the ones their source package proposed — recorded in
> [`docs/review/2026-08-23_reliability_delta_id_remap.md`](../../docs/review/2026-08-23_reliability_delta_id_remap.md).
>
> **The direction it explicitly refuses.** Every cost pressure on a multi-agent
> system argues for fewer agents. This baseline holds the cohort fixed and
> optimises the conversation instead — `ADR-011` — and that refusal is the single
> most load-bearing decision in it.

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
| [`12_ACCEPTANCE_SCENARIOS/acceptance_scenarios_index.md`](12_ACCEPTANCE_SCENARIOS/acceptance_scenarios_index.md) | Every scenario, by severity and phase |

## 4. How a package is documented

Every work package is **three documents**, side by side in its workstream directory:

| File | Answers | Read by |
|---|---|---|
| `WP-nnn_slug.md` | What is this, what does it depend on, what does its acceptance release? | Refinement and planning |
| `WP-nnn_slug.tests.md` | How is it tested — environment, data, coverage items, cases, execution log, incident and completion reports? | The implementer and the tester |
| `WP-nnn_slug.acceptance.md` | What must hold for `ACCEPTED`, and what does it still not establish? | The **independent verifier** |

The split is not filing. `00_PROGRAM/06` requires a reviewer to work from a **frozen packet** without seeing the producer's trace, and a criteria section living inside the producer's working card is not that packet. The companions are structured on the information items of **ISO/IEC/IEEE 29119-3:2021** — the common elements of §5.2, the dynamic test process items of §8, and the completion report of §7.4 — adopted for document structure only; the evidence layers E0–E5 and the gate model remain this programme's own.

Each companion carries generated blocks — test strategy, environment requirements, data requirements, coverage items, the Definition of Ready/Done/Commissioned checklists and the non-waivable list — derived from `package_dependency_matrix.csv` by `scripts/make_package_companions.py`. What sits outside those blocks is authored, and is never overwritten.

## 5. Directory structure

| Path | Contents |
|---|---|
| [`00_PROGRAM/`](00_PROGRAM/README.md) | Programme charter, target state, wave plan, RACI, DoR/DoD, evidence and change control |
| [`01_GOVERNANCE/`](01_GOVERNANCE/README.md) | WP-001–010: governance and policy design |
| [`02_CONTRACTS/`](02_CONTRACTS/README.md) | WP-011–020: identity, schema, record and contract foundation |
| [`03_FOUNDATION/`](03_FOUNDATION/README.md) | WP-021–030: environment, repository, CI, data and platform backbone |
| [`04_CONTROL_EVENT/`](04_CONTROL_EVENT/README.md) | WP-031–040: Temporal, G0–G10, event and replay |
| [`05_MODEL_AGENT_TOOL/`](05_MODEL_AGENT_TOOL/README.md) | WP-041–050: gateway, admission, agent runtime and broker |
| [`06_EXECUTION_SECURITY/`](06_EXECUTION_SECURITY/README.md) | WP-051–060: trust zones, compute, identity, policy and security |
| [`07_LITERATURE_KNOWLEDGE/`](07_LITERATURE_KNOWLEDGE/README.md) | WP-061–074: Source Registry, Zotero, literature and Obsidian |
| [`08_EVIDENCE_ASSURANCE/`](08_EVIDENCE_ASSURANCE/README.md) | WP-075–090: evidence, claims, experiments, review and reproduction |
| [`09_EXPERIENCE_OBSERVABILITY/`](09_EXPERIENCE_OBSERVABILITY/README.md) | WP-091–101: cockpit, decision UI, telemetry and FinOps |
| [`10_INTEGRATION_CUTOVER/`](10_INTEGRATION_CUTOVER/README.md) | WP-102–121: vertical slices, commissioning and production cutover |
| [`11_DAY2_OPERATIONS/`](11_DAY2_OPERATIONS/README.md) | WP-122–130: continuous operation and assurance |
| [`12_ACCEPTANCE_SCENARIOS/`](12_ACCEPTANCE_SCENARIOS/README.md) | ACC-01–ACC-120: Given/When/Then system acceptance scenarios, including ACC-41–46 skill governance and ACC-47–51 |
| [`13_TOOLING_INTEGRATION/`](13_TOOLING_INTEGRATION/README.md) | WP-131–140: notification, communication, external records, evidence sealing and liveness |

## 6. Package status model

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
> [**WP-000 — Interim Evidence Policy and Attestation Bootstrap**](01_GOVERNANCE/wp_000_interim_evidence_policy.md)
> now closes the storage half: the manifest is issued as a signed in-toto
> attestation and anchored in time, so immutability is delegated rather than
> deferred. The profile in force is `airl-interim-v0.1`, which signs with a
> local key and is **not** submitted to a transparency log; the permanent
> profile that is, arrives with WP-139. The rationale is in
> `docs/architecture/AETHRION_EXTERNAL_STANDARDS.md` §3.
>
> The other half — finding **C2**, who may act as an independent verifier in a
> one-person operation — is **decided**, by
> [`ADR-001`](../04 - Architecture/adr_001_solo_operator_independence.md):
> R1 proceeds solo, R2 proceeds and is declared partial in the record, and R3 is
> `BLOCKED` rather than waived. A decision is not an implementation — R3 work
> still cannot be accepted here — but the question is no longer open.
