---
title: "AETHRION — operating manual for an agent"
aliases:
  - "AGENTS"
  - "AGENTS.md"
  - "Operating Manual"
cssclasses:
  - aethrion-index
type: index
category: project
source: "AGENTS.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/project
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `AGENTS.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# AETHRION — operating manual for an agent

> **Read this file completely before touching anything.** It is written for any
> AI coding agent or new human maintainer arriving with no prior context, and it
> is the only document that assumes you have read nothing else. Every path and
> command in it is checked by `scripts/check_agent_guide.py`, which runs in the
> verification bundle — if something here is wrong, that check fails.

---

## 1. What this is

**AETHRION — Agentic Intelligence Research Layer.** An evidence-centred research
system. Its thesis, and the sentence the whole design follows from:

> **agents produce · machines verify · humans decide** — and the three are kept
> structurally separate.

The failure it is built against is not incompetence but **plausibility**: fluent,
well-cited, confident model output that is wrong, and that no amount of further
model capability detects from the inside. So model output is a *hypothesis* that
must survive mechanical verification, independent review and a human decision
before it becomes a claim.

**`AIRL` is not the product name.** It is the abbreviation of the descriptor and
survives only as a technical term. See §7.5 — do not "finish the rename".

### The three things in this repository

| | What | State |
|---|---|---|
| 1 | A target architecture | Designed; largely unbuilt |
| 2 | A sealed commissioning plan — **this is V1** | 160 packages, 120 scenarios, sealed |
| 3 | One vertical slice that runs | Zotero → SQLite → Obsidian + read-only MCP |

**The distance between (1) and (3) is large, and every document states it rather
than implying it.** If a document ever suggests the system works end to end,
that document is the defect.

---

## 2. Do this first, every session

```bash
cd /home/otonom/Desktop/FH/AETHRION
uv run python scripts/write_status.py    # runs the 20-check bundle, rewrites docs/STATUS.md
python3 scripts/ready_queue.py           # rewrites docs/READY.md
git log --oneline -5
```

`write_status.py` must print **20/20**. If it does not, fix that before doing
anything else — a session that starts on a red bundle cannot tell its own
breakage from the breakage it inherited.

Then read, in order:

| # | File | Answers |
|---|---|---|
| 1 | `docs/STATUS.md` | What is true right now. **Generated** |
| 2 | `docs/READY.md` | What can be started today. **Generated** |
| 3 | `vault_baseline/10 - Projects/AETHRION/03 - Implementation/session_handover_2026-08-22.md` | Where the last session stopped |
| 4 | `docs/EXECUTING_A_WORK_PACKAGE.md` | The loop for running a work package |

Do **not** start by reading the architecture corpus. It is 41,000 lines. Almost
everything a session needs is generated and re-derived; reading a document to
learn a number a script prints is how a session starts with a stale fact.

---

## 3. Repository map

| Path | What | Generated? |
|---|---|---|
| `src/airl_bridge/` | The working slice: Zotero client, SQLite registry, FastAPI, Obsidian projection, MCP server | no |
| `src/airl_framework/` | Shared contract core. **Zero production consumers** — finding H4 | no |
| `tests/` | 35 tests | no |
| `scripts/` | Verification, generation and execution tooling — 48 scripts | no |
| `planning/commissioning/` | The V1 plan: WP-000–159, ACC-01–120. **632 files, hash-sealed** | indexes only |
| `docs/architecture/` | Target design, three ADRs, positioning | no |
| `docs/figures/` | 14 SVG figures | **yes** — from `scripts/fig_*.py` |
| `docs/STATUS.md`, `docs/READY.md` | Live state | **yes** |
| `docs/review/` | Dated, frozen audit reports | no — and never updated |
| `delivery/` | Evidence packages, signing keys, measurements, the progress ledger | partly |
| `deploy/` | systemd units, the staged CI workflow | no |
| `skills/` | 52 Agent Skills — 11 vendored from `obra/superpowers`, 41 native | no |
| `schemas/` | Shared contract schemas | no |
| `provenance/` | Which mechanism came from which project, its licence, and what it may never decide | `provenance/README.md` **yes** — generated from `provenance/upstreams.json` |
| `vault_baseline/` | Versioned snapshot of the Obsidian vault — linted by `check_vault.py` | **mostly** |
| `docs/assets/branding/` | The canonical logo | no |

---

## 4. The architecture, in enough detail to work without the corpus

### 4.1 The evidence chain

```
Source → SourceRepresentation → EvidenceSpan → ClaimVersion → ExperimentRun
       → Review → Reproduction → DecisionRecord → Publication → Monitoring

candidate → frozen evaluator → RawEvaluatorArtifact → VerifiedValue → PublicationAssertion
```

Two properties matter more than the chain: it is **traversable in both
directions** (published sentence → source span; retracted source → every
dependent claim), and **the loop closes** — `VERIFIED` is explicitly not a
permanent state. **One of the ten links is implemented.**

The second line is where a *number* comes from, and it is not optional: no
number reaches a publication without a `VerifiedValue`, and no `VerifiedValue`
exists without an immutable evaluator output under it. The producer has no read
or write path into the evaluator zone. **None of that line is implemented** —
ADR-007.

### 4.2 The G0–G10 lifecycle

`G0` Intake · `G1` Charter · `G2` Protocol · `G2b` Analysis Plan · `G3`
Literature · `G4` Baseline + Falsification · `G5` Execute · `G6` Assurance ·
`G7a` Reproduction · `G7b` Replication · `G8` Human Decision · `G9` Publish ·
`G10` Monitor.

Each gate resolves in the same order: **mechanical check first and unwaivable →
model may produce → human holds authority**. No model at G5 or G7a; at G8 a model
may only recommend. **None of this is implemented** — there is no gate runtime.

### 4.3 The planes

Experience · Control (Temporal — the process authority) · Event (NATS — carries
events, never authority) · Cognition (LangGraph — bounded reasoning inside one
task, never across gates) · Execution (sandbox, tool broker, execution broker) ·
Evidence and Operations · Metascience (proposed). **None is built.**

### 4.4 The trust boundary — ADR-003

Trusted control plane holds the goal and every privilege. Untrusted data plane
holds everything an outsider can write: paper full text, tool output, web pages,
reviewer comments. **Content crosses; authority does not.** A retrieved sentence
may change what the agent knows, never what it may do. A formally-analysable
policy engine behind the `PolicyDecision` interface is the policy
decision point; default deny; an anomaly is a denial, not a warning. **No policy
set is authored and no adversarial benchmark has been run.**

### 4.5 Roles

Fourteen durable functions ordered by authority. **A role is a function, not a
person**: one operator may hold several, and legality is decided by separation
constraints on a `RoleBinding`, not by headcount. Independence under one operator
is decided by **ADR-001**: R1 solo · R2 solo under a *declared partial*
independence profile · **R3 `BLOCKED`**, declared rather than waived.

### 4.6 What is adopted rather than invented

Components carry an adoption type — `DEPENDENCY`, `ADAPTER`, `STANDARD`,
`BENCHMARK`, `PATTERN`, `OPTIONAL_BACKEND`, `DIRECT_ADAPT`,
`ADAPTIVE_REIMPLEMENT`, `DEFER`, `REJECTED` — each with a mandatory
`authority_boundary`. Adopted: Inspect AI, GROBID + Pub2TEI, PaperQA2, ASReview,
the CaMeL pattern, OSF Registries, Workflow Run RO-Crate, SEPIO + LinkML, CiTO,
Croissant, SWHID, MLflow + OpenTelemetry, sigstore, Crossref/OpenAlex/arXiv.
Register: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

**Do not write a PDF parser, a policy language, a sandbox or an experiment
tracker here.** The value is which evidence, through which control, licenses
which claim.

### 4.6.1 Substantial scientific work is multi-agent, and that is not a cost lever

`ADR-011`. At least two **epistemically independent** cognitive contributions
before synthesis — independence being a five-dimension profile (cognitive
function, evidence exposure, peer visibility, model profile, prompt perspective),
**not a count**. Several instances of one model on one context are one
contribution.

Optimisation targets the **conversation**: typed delta-only messages over a
compiled sparse topology, context projection, memory masking, adaptive assurance
routing. Never the cohort. Budget pressure degrades verbosity; a task that cannot
afford its required assurance is `BLOCKED`, not completed more cheaply.

If you are about to reduce a cohort to save tokens, that is the decision
`ADR-011` exists to refuse. **None of this is implemented** — WP-148–159 specify
it and there is no collaboration plane.

### 4.7 Taking a mechanism from another project

A **mechanism** may be taken; an **architecture** may not. No external project
appears here as a runtime module, directory, backend, class name or config key —
if you are about to create `src/third_party/<name>`, stop and read `ADR-004`.

The register is `provenance/upstreams.json`, checked by
`python3 scripts/check_upstream_lineage.py`. Before any code moves:

| Decision | What it requires |
|---|---|
| `DIRECT_ADAPT` | permissive licence **read at the source** · pinned commit · named file list · characterisation suite written **before** the code moves · SPDX and `NOTICE` |
| `ADAPTIVE_REIMPLEMENT` | a written mechanism specification first. **No source files** — an entry naming files is refused, because if files were copied the decision was direct adaptation |
| `DEPENDENCY` | version pin, upgrade path, failure semantics |

Every entry states **what the mechanism may never decide.** That field is
required, and the checker refuses an entry without one. Run
`--self-test` to confirm the rules still fire; a checker that has never been
seen to fail reports "no findings" and "no detector" identically.

**No entry has reached `ADAPTING`.** Everything in the register is a decision on
paper and `pinned_commit` is `null` throughout. There is no network access from
the sandboxed shell here, so pinning a commit is work for a session that has one
— do not invent a digest to satisfy the field.

---

## 5. What actually runs — read this before believing §4

| Component | State |
|---|---|
| Zotero → SQLite → Obsidian bridge, read-only MCP (5 tools) | **Working**, 35 tests |
| Evidence issuance/verification, signed, tamper-rejecting | **Working** — `TECH_COMPLETE`, not `ACCEPTED` |
| Plan seal, figure generators, mirrors, 20-check bundle | **Working** |
| Upstream lineage register and its checker, 11 firing controls | **Working** — the register is decisions, not adapted code |
| Reference verification (Crossref/OpenAlex/arXiv) | **Working** — 27 of 33 corroborated |
| Source monitoring (first slice of G10) | **Working** — positive control fires |
| 52 skills | Format-conformant; **none behaviour-tested** |
| Contract core | Prototype, **zero consumers**, digest format conflicts with the bridge |
| Temporal · LangGraph · NATS · brokers · ledgers · Model Gateway · G0–G10 runtime · policy set | **No code** |
| Discovery search graph · frozen evaluator zone · six memories · V0–V3 verifier engine · publication compiler | **No code** — specified at v1.2.0 by ADR-004–010 and WP-141–147 |
| Collaboration plane · sparse topology · communication governor · memory mask · failure taxonomy · budget ledger · spec conformance · assurance router · human preliminary flow · model fingerprint · benchmark firewall | **No code** — specified at v1.3.0 by ADR-011–019 and WP-148–159 |
| Notification channels (ntfy · Telegram · Discord/Slack · WhatsApp) | **Planned** — specified, nothing connected, nothing sends |
| CI (BVC-01) | **Staged, never run** — needs a workflow-scoped token |

Open findings: **H1** Zotero ingest capped at 100 records (fix M9 first, or
pagination turns a masked truncation into active data loss) · **H2** no deletion
reconciliation · **H3** the read-only boundary has no behavioural test · **H4**
the contract core has no consumers · **H5** no CI. **C1** and **C2** are closed
by WP-000 and ADR-001.

That is the high tier only. **`docs/FINDINGS.md` is the register** — all
twenty-four audit findings with their current state, plus the twelve raised by
the 2026-08-22 and 2026-08-23 inspections. Twelve are open. Do not infer a
finding's state from a module docstring; sixteen of them used to live nowhere else, and several had
been fixed with nothing saying so.

---

## 6. Current position

**t0.** 1 package ready (**WP-001**, which authorises the programme), 1
`TECH_COMPLETE` (**WP-000**), **0 accepted**, 140 not started. Nothing has run
end to end.

---

## 7. Rules that are not negotiable

### 7.1 Generated files are never hand-edited

`docs/STATUS.md` · `docs/READY.md` · `docs/figures/*.svg` · the 16 workstream
`README.md` files under `planning/commissioning/` · everything under
every page under `vault_baseline/10 - Projects/AETHRION/` whose frontmatter says
`generated: true` — the mirrors write those and refuse to touch any other.

Change the generator, regenerate, verify. Each generator has a `--check` mode and
the bundle runs them.

### 7.2 The plan is sealed

`planning/commissioning/` is 632 hash-sealed files. Verify:

```bash
(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt)
```

Changing a plan file is a **recorded change**: edit, regenerate the seal, bump the
baseline in `planning/commissioning/README.md`, tag it, record why. **Re-sealing
to silence a failing check is the one prohibited use of the seal.**

### 7.3 Progress is not the plan

Execution state is `delivery/progress.json`, **outside the seal**. Move packages
with `scripts/progress.py`; never hand-edit the ledger. Each package's
`Status at baseline` field is history and never changes again.

### 7.4 Additions are V2; corrections are V1

**A correction keeps the finish line where it is; an addition moves it.** V1 is
the whole sealed plan; it is complete when
`planning/commissioning/00_PROGRAM/10_go_live_checklist.md`'s entry conditions
hold. Anything else goes to `docs/V2_CANDIDATES.md`, never into `planning/`.

### 7.5 `AIRL` stays where it is technical

Retained deliberately: the `airl.*` skill-metadata namespace (required by
`scripts/validate_skills.py`), the `airl_id` schema field, `airl-bridge` and its
systemd units, `src/airl_bridge/`, `src/airl_framework/`, `AIRL_API_*` env vars,
`X-AIRL-Token`, the `airl-interim-v0.1` attestation profile and the
`https://airl-os.local/…` predicateType — **the last two are inside signed
evidence and renaming either invalidates a signature that verifies today.**
`docs/branding.md` lists every retention with its reason.

### 7.6 State distance from working software

`docs/DOCUMENT_STANDARD.md` defines the controlled vocabulary: `WORKING`,
`TECH_COMPLETE`, `ACCEPTED`, `SPECIFIED`, `PROPOSED`, `DESIGNED`, `DEPRECATED`.
**`TECH_COMPLETE` is not `ACCEPTED`** — only an independent verifier moves a
package. Never describe a plan as an implementation.

### 7.7 Do not invent architecture

Document something as part of AETHRION only when it is implemented, specified,
or in the approved plan. If it exists only as an idea, label it `PROPOSED`. If it
is not present at all, do not add it.

---

## 8. Common tasks

### Change a document
Edit it → `uv run python scripts/write_status.py` → mirror (§9) → commit.

### Change a figure
Edit `scripts/fig_*.py`, never the SVG → `python3 scripts/make_figures.py`.
`figure_kit` **raises** rather than shrinking text below a 16-unit legibility
floor; if it refuses, widen the box or shorten the label.

### Change the plan
Edit → re-seal (§7.2) → `python3 scripts/validate_commissioning_plan.py` →
`python3 scripts/check_doc_consistency.py` → bump the baseline → tag → record it.

### Run a work package
```bash
python3 scripts/ready_queue.py
python3 scripts/progress.py show WP-001
python3 scripts/progress.py start WP-001
# … do the work the package document specifies …
python3 scripts/evidence_manifest.py issue --package WP-001 --gate Program --subject <file> --check "<what was verified>"
python3 scripts/progress.py tech-complete WP-001
python3 scripts/progress.py accept WP-001 --verifier "<not the owner>" --assurance R1
```
`progress.py` refuses what the plan forbids and names the document that forbids
it. A refusal is not advice. Full runbook: `docs/EXECUTING_A_WORK_PACKAGE.md`.

### Add a skill
Agent Skills format plus the `airl.*` metadata contract; validate with
`python3 scripts/validate_skills.py`. Vendored skills under `skills/_vendor/`
keep upstream attribution and their pinned commit — do not rewrite them.

---

## 9. Before you finish anything

```bash
uv run python scripts/write_status.py                                    # must print 20/20
python3 scripts/mirror_vault.py "vault_baseline/10 - Projects/AETHRION"
python3 scripts/mirror_plan.py "vault_baseline/10 - Projects/AETHRION/01 - Commissioning"
python3 scripts/mirror_vault.py "/home/otonom/Documents/Obsidian Vault/10 - Projects/AETHRION"
python3 scripts/mirror_plan.py "/home/otonom/Documents/Obsidian Vault/10 - Projects/AETHRION/01 - Commissioning"
```

Reissue the WP-000 attestation if any of its subjects changed, then verify:

```bash
uv run python scripts/evidence_manifest.py verify --manifest delivery/WP-000/evidence.dsse.json --tamper-demo
```

---

## 10. Hazards — each of these has actually happened

| Hazard | What happens | Guard |
|---|---|---|
| `mirror_plan.py` once **replaced its target directory** | Pointed at a vault root instead of the commissioning subtree, it deleted the whole vault. It also broke a running Obsidian's file watcher, so the editor kept showing a stale index of files that no longer existed at those inodes | It now writes **differentially** — only what changed, removing only what the mirror no longer generates — and still refuses a target holding files it does not generate. Pass the subtree, never the root |
| Editing a generated file | Overwritten on the next run; `--check` fails | Change the generator |
| Editing a plan file without re-sealing | Seal check fails | §7.2 |
| Pushing a change to `.github/workflows/` or `deploy/*.yml` | Rejected — the token lacks `workflow` scope | Commit the rest; report the workflow change |
| Trusting a green bundle too far | The checks are internal consistency only | §11 |
| "Finishing" the AIRL rename | Breaks imports, a schema field, or a signature | §7.5 |
| Editing the Obsidian vault by hand | Lost on the next mirror | Edit the repository |
| Inventing a tag in the vault | It fragments one idea into two nodes no query can join | the vocabulary lives in `vault_baseline/_meta/taxonomy.md`; add tags to `scripts/vault_frontmatter.py`, never to a note |

---

## 11. What the verification bundle does **not** prove

All fifteen checks are **internal consistency**. They confirm this repository says
the same thing everywhere, that its plan is well-formed and that its evidence
verifies — and every one of those would still hold for a corpus describing a
system that does not work.

External truth enters through exactly two doors: reference verification against
Crossref, OpenAlex and arXiv, and the benchmarks named in the adoption matrix
(CoE Audit, ResearchClawBench, PaperBench, AgentDojo), **none of which has been
run**.

The stale-claim checker is a set of rules, not a semantic understanding; it
prints its rule counts so the gap stays visible. An external review once found
two stale claims in a corpus whose status page said there were none. Assume the
same is possible now.

---

## 12. Index — where to look for what

| Question | File |
|---|---|
| What is true right now? | `docs/STATUS.md` |
| What can I start today? | `docs/READY.md` |
| How do I run a work package? | `docs/EXECUTING_A_WORK_PACKAGE.md` |
| What is the whole system? | `docs/architecture/AETHRION_ARCHITECTURE.md` — **§10 first** |
| Who is accountable, and what may they never do? | `docs/architecture/AETHRION_ROLES.md` |
| What was decided, and by whom? | `docs/architecture/ADR-001_solo_operator_independence.md` · `ADR-002_bootstrap_verification_control.md` · `ADR-003_trusted_control_and_policy.md` |
| What is adopted rather than invented? | `docs/architecture/AETHRION_COMPONENT_REUSE.md` |
| How does this compare to Science One, PaperQA2? | `docs/architecture/AETHRION_RELATED_SYSTEMS.md` |
| How are documents written here? | `docs/DOCUMENT_STANDARD.md` |
| What is the project called, and where does `AIRL` stay? | `docs/branding.md` |
| What is deliberately not V1? | `docs/V2_CANDIDATES.md` |
| What is known to be wrong, and is it still? | `docs/FINDINGS.md` |
| How do agents work? | `skills/README.md`, `docs/architecture/AETHRION_SKILL_LAYER.md` |
| How do I run and verify the slice? | `docs/OPERATIONS.md` |
| What may a vault note be tagged? | `vault_baseline/_meta/taxonomy.md` (generated) |
| What does each script do? | `scripts/README.md` |
| The plan itself | `planning/commissioning/README.md` |
| Where did the last session stop? | `vault_baseline/10 - Projects/AETHRION/03 - Implementation/session_handover_2026-08-22.md` |
