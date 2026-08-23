---
title: "Programme Risk Register and Treatment Rules"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/07_programme_risk_register.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Programme Risk Register and Treatment Rules

| ID | Risk | Early signal | Preventive control | Owner | Cutover impact |
|---|---|---|---|---|---|
| PR-01 | Platform scope grows uncontrolled | Packages keep exceeding L | Contract-first, scope lock, retirement criteria | Chief Architect | High |
| PR-02 | Policy becomes combinatorial | Large cross-tables, unexplainable decisions | Separate profiles, precedence and hard-promotion rules | Governance Lead | Critical |
| PR-03 | Canonical ownership blurs | Zotero/Registry/Obsidian values diverge | Field authority and reconciliation | Knowledge Lead | Critical |
| PR-04 | Verification backlog grows | G6/G7 waiting and bypass requests | Risk-based depth, C0 mechanical checks, capacity reserve | Assurance Lead | Critical |
| PR-05 | Reviewer independence exists only on paper | Same trace, credential or model family | Machine-checkable `IndependenceProfile` | Assurance Lead | Critical |
| PR-06 | Agent tool authority expands too far | Direct credential or connector use | Broker-only, purpose-bound identity | Safety Owner | Critical |
| PR-07 | Dual authority over event/state | A NATS consumer changes gate state | Temporal-only transitions, outbox contract | Control Plane Lead | Critical |
| PR-08 | Artifact overwrite / lineage loss | Different bytes at the same URI | Content addressing, object lock | Data Platform Lead | Critical |
| PR-09 | Cost runaway | Fan-out, retry, token growth | Hard budget, queue quota, minimum bundle | FinOps Lead | High |
| PR-10 | Vendor lock-in | Provider fields leak into role contracts | Adapter conformance and canonical contracts | Model Platform Lead | High |
| PR-11 | Human rubber-stamping | Very fast or generic approvals | Evidence-delta UI, rationale rubric, sampling | Governance Lead | High |
| PR-12 | False rigor | Many artifacts, weak entailment | Outcome audit, anti-metrics, citation audit | Research Director | Critical |
| PR-13 | Restore exists only on paper | Backups present, no rehearsal | Two restore drills + integrity queries | SRE Lead | Critical |
| PR-14 | Source licences violated | PDFs proliferate uncontrolled | Licence policy, hash-only fallback, access log | Knowledge / Safety | Critical |
| PR-15 | Eval contamination | Golden set appears in prompts or traces | Separate credential/store, canary, invalidate/re-eval | Eval Office | Critical |

## Risks identified by the audit

| ID | Risk | Why it is not covered above | Owner |
|---|---|---|---|
| **PR-16** | **Independence is assumed, never measured** | PR-05 addresses paper independence; it does not address correlated errors between genuinely different models | Metascience Lead |
| **PR-17** | **Confidence scores carry no measurement basis** | A specific, mechanical instance of PR-12 that the register treats only in the abstract | Metascience Lead |
| **PR-18** | **The lab's own error rate is unknown** | No control mechanism measures whether the pipeline produces correct results at all | Metascience Lead |
| **PR-19** | **Publication bias survives the gate structure** | G2 freezes the protocol, but G8 can still reject on the direction of the result | Research Director |
| **PR-20** | **Periodic work fails silently** | Neither PR-13 nor SLO alerting covers a job that stops without erroring | SRE Lead |
| **PR-21** | **Scope does not fit the organisation** | The programme assumes dozens of role-holders and a separate assurance pool | Executive Sponsor |

## Status of the audit findings, 2026-08-22

| Finding | Then | Now |
|---|---|---|
| **C1** evidence bootstrap | Critical — nothing could be accepted | **Storage half addressed.** WP-000 written and its tooling implemented; a specimen manifest verifies and both tamper paths are rejected. **No manifest has been accepted** |
| **C2** independent verification | Critical — R3 permanently blocked | **Decided** in ADR-001: R1 solo · R2 solo under a declared partial-independence profile · **R3 `BLOCKED`** without an external verifier |
| **H5** no CI | Open | **Partly.** BVC-01 is decided and written (`deploy/bvc-01-verify.yml`) but **not active** — activation needs a workflow-scoped token. H5 itself stays open: it is the absence of the WP-024 platform |
| **H1** ingest capped at 100 | Open | Open. **Fix M9 first**, or pagination turns a masked truncation into active data loss |
| **H2 · H3 · H4** | Open | Open |

## New risks recorded by this baseline

| Risk | Why it is a risk |
|---|---|
| **Adoption without verification** | Ten packages now stand on external components. A component adopted and never verified is a dependency with the *appearance* of assurance |
| **Benchmark drift into gate** | A `BENCHMARK` measures the laboratory; if one ever becomes a pass condition, the laboratory starts optimising against its own scorer |
| **Specification outpacing execution** | 160 package documents, 120 scenarios, 52 skills — and one working vertical slice. This is the standing risk, and baselines v1.2.0 and v1.3.0 **increased** it twice: nineteen packages and sixty-nine scenarios of specification were added against no new implementation |
| **Interim attestation mistaken for witnessed** | `airl-interim-v0.1` is tamper-evident, **not externally witnessed**: one operator holds the repository, the key, the generator and the clock |

### Recorded by baseline v1.2.0

Each is a risk the new capability creates. They are listed beside the capability
rather than after it, because a control that introduces a risk and does not name
it has moved the failure rather than removed it.

| Risk | Why it is a risk | Owner |
|---|---|---|
| **PR-22 · A search score becomes a confidence** | The discovery graph produces several numbers and none is epistemic. A selection score written into a claim assessment is a confidence nobody measured, and it would read exactly like one that was | Chief Architect |
| **PR-23 · A semantic verifier is trusted as a mechanical one** | V2 checks are machine-performed and not machine-proved. Reported without their class, they inherit the credibility of a hash comparison | Assurance Lead |
| **PR-24 · The evaluator boundary is asserted rather than attacked** | An isolation boundary that has never been red-teamed is a configuration, not a control. ACC-54 and ACC-55 exist because the boundary is the single highest-value target in the system | Execution Security Lead |
| **PR-25 · Over-pruning at SMOKE kills what only works at scale** | A fidelity funnel is a bet that cheap evaluation predicts expensive evaluation. Where it does not, the funnel systematically discards the ideas whose benefit appears only at full fidelity — and the record shows a tidy campaign | Research Director |
| **PR-26 · Adapted upstream code drifts silently** | A pinned mechanism whose upstream fixes a bug is a local copy carrying a known defect. Without drift monitoring nobody finds out, because there is no package manager to notice | Supply Chain Security Lead |
| **PR-27 · Six memories become six places to be wrong** | Typed stores make authority checkable and multiply the surfaces that can disagree. A finding that contradicts its own evidence is now expressible, and only the rebuild and retention tests catch it | Knowledge Lead |
| **PR-28 · The publication compiler is routed around** | A compiler that refuses is a compiler people will want to bypass under deadline. The refusal has to be non-waivable, or it becomes advisory the first time it is inconvenient | Provenance Curator |

### Recorded by baseline v1.3.0

Thirty risks arrive with the reliability layer. They are numbered in this
register's own sequence and keep their source identifier, so the dossier each
came from stays findable.

Two properties are worth reading across the table rather than row by row. **Most
of them are failures a multi-agent system adds** — a single-agent pipeline has no
sycophancy risk, no attribution ambiguity and no communication explosion. And
**several are created by this baseline's own mitigations**: adaptive assurance
introduces selective enforcement, memory masking introduces wrongly-excluded
context, and pruning introduces the silenced-message residual. A mitigation that
introduces no risk is usually one that changes nothing.

| Risk | Name | Threat | Mitigation | Owner | Source |
|---|---|---|---|---|---|
| **PR-29** | Architecture overengineering | A logical plane becomes a deployment unit before anything consumes it, and the operational failure surface grows without any assurance being added | Modular monolith first; a distribution decision needs a stated isolation, scaling or lifecycle reason, recorded | Chief Architect | `R01` |
| **PR-30** | Split brain across authorities | Temporal, the domain store, the event bus and a projection disagree about a gate or a claim — and the disagreement is invisible until a post-mortem | One canonical owner per kind of state; atomic outbox; idempotent consumers that re-read canonical state; injection suite rather than a property assertion | Chief Architect / SRE Lead | `R02` |
| **PR-31** | Communication explosion | Agents × rounds × full transcripts grows faster than the value it carries, and the cost lands on every task | Typed delta-only messages, artifact pointers, compiled sparse topology, measured edge utility — **pruning the conversation, never the cohort** | Chief Architect | `R03` |
| **PR-32** | Sycophancy and false consensus | Agents converge on a confident prior answer instead of deriving independently, and the record shows agreement rather than deference | Peer-output embargo before the first pass; sealed initial positions; convergence blocked by an unresolved material challenge | Assurance Lead | `R04` |
| **PR-33** | Faulty or malicious agent propagation | One bad output becomes another agent's premise and reaches synthesis | Challenger and Inspector functions, message provenance, qualification-aware propagation — and no agent able to bind authority anywhere | Red Team Lead / Assurance Lead | `R05` |
| **PR-34** | Failure attribution ambiguity | A run fails and the decisive step cannot be located, so work routes to the wrong discipline | Complete causal trace, a typed failure taxonomy, recorded attribution confidence — and **`UNKNOWN` as a legitimate terminal class** | Incident Commander | `R06` |
| **PR-35** | Long-horizon memory and context decay | A frozen constraint is buried, or a refuted intermediate conclusion keeps influencing later reasoning | Typed stores, context projection, memory masking by epistemic status, and selective proactive reminders | Knowledge Lead | `R07` |
| **PR-36** | Budget runaway | Search, debate, tool and experiment loops consume resources for little marginal value | A nine-dimension budget contract, a categorised token ledger, communication degradation before anything else, and reserved reproduction budget | FinOps Lead | `R08` |
| **PR-37** | Implementation drift | Under execution pressure the code quietly stops implementing the frozen method, and every downstream artifact stays internally consistent | Frozen specification digests compared against executed code, with a severity ladder that changes scientific status | Chief Architect | `R09` |
| **PR-38** | Claim, evidence and numeric lineage break | A published claim, citation or number cannot be traced or recomputed | Chain of evidence by construction; `VerifiedValue` for every number; publication assertions bound to claims | Evidence Platform Lead | `R10` |
| **PR-39** | Source status drift after a decision | Evidence is corrected or retracted after the decision that rested on it | Crossref and Retraction Watch feeds, an impact graph, and G10 material-delta traversal | Knowledge Monitoring Lead | `R11` |
| **PR-40** | Analysis flexibility, p-hacking and HARKing | Analysis choices are searched after the outcome is visible | G2b analysis-plan freeze with an external timestamp, deviation records, and a claim ceiling that lowers but never rises | Research Director | `R12` |
| **PR-41** | Evaluator gaming and leakage | The producer reads or modifies the hidden grader, metric or data | A private evaluator zone with its own identity, a signed evaluator digest, a path allowlist, and cheating fixtures that must be caught | Execution Security Lead | `R13` |
| **PR-42** | Verifier and judge overtrust | A semantic judge returns a false PASS and is treated as ground truth | Qualification with expiry, positive and negative controls, selective cascade, and `ABSTAIN` as a first-class verdict | Assurance Lead | `R14` |
| **PR-43** | Human automation bias | The decision owner ratifies the recommendation instead of evaluating the evidence | Preliminary assessment sealed before the recommendation is revealed; friction symmetry between approve and correct; `INSUFFICIENT_BASIS` | Project Decision Owner | `R15` |
| **PR-44** | False reproduction independence | The reproducer inherits the producer's environment, cache or credentials | Three zones with no shared secrets, cache or workspace; a package that runs with no agent context; lineage-based classification | Reproducibility Lead | `R16` |
| **PR-45** | Hosted model nondeterminism | The same request under the same settings yields materially different output | A model execution fingerprint including retry and fallback history; a five-level reproduction taxonomy in which a hosted black box does not yield `EXACT` | Reproducibility Lead | `R17` |
| **PR-46** | Prompt injection and tool misuse | External content becomes an instruction and induces an unsafe tool action | Quarantine, data-versus-instruction typing, tool intent through a capability gate, scoped credentials, and external attack regressions | Content Security Lead | `R18` |
| **PR-47** | Benchmark contamination | The agent retrieves a public benchmark answer during the run and the measured score inflates | A firewall frozen before the run, audited retrieval, hidden evaluator, and a contamination label that travels with the score | Eval Office | `R19` |
| **PR-48** | Dependency and upstream drift | A library changes, an agent uses a stale API from training memory, or an adapted mechanism diverges from its pin | OSV and Scorecard, pinned commits, characterisation drift checks, and review before any pin moves | Supply Chain Security Lead | `R20` |
| **PR-49** | Supply-chain artifact tampering | A build or dependency is modified without provenance | SLSA provenance, Sigstore signing and verification, an SBOM, and refusal of an unsigned artifact | Supply Chain Security Lead | `R21` |
| **PR-50** | Licence and provenance loss | External code is copied without a compatible licence or a traceable origin | SPDX and REUSE, `NOTICE`, the upstream register, and a direct-copy gate that fails admission before merge | Supply Chain Security Lead | `R22` |
| **PR-51** | Observability correlation loss | After an incident the agent, tool, artifact and claim lineage cannot be reconstructed | One correlation chain across planes on OpenTelemetry spans, with redaction by data class | AI Observability Lead | `R23` |
| **PR-52** | Publication drift | The renderer introduces prose or numbers that nothing supports | A compiler that refuses rather than writes; an assertion inventory; the model as renderer only | Provenance Curator | `R24` |
| **PR-53** | A derived store treated as truth | A vector or graph projection result is cited as canonical evidence | Read-model contracts carrying source references, and destructive rebuild tests that prove the projection owns nothing | Data Platform Lead | `R25` |
| **PR-54** | Skill and prompt behaviour drift | A skill exists, loads, and does not reliably change behaviour — or an update silently regresses it | Behaviour baselines before the skill, pressure tests, versioned qualification, and drift re-runs | Eval Office | `R26` |
| **PR-55** | Negative result and dead-end loss | Failed work disappears, and a later campaign repeats it or misclassifies why it failed | Mandatory negative result, failed approach, failure assessment and search experience records — retained, never pruned | Knowledge Lead | `R27` |
| **PR-56** | G10 alert fatigue | Every minor source or dependency change pages a human, and the pages stop being read | Material evidence-delta scoring with severity routing; a digest for everything below it | Knowledge Monitoring Lead | `R28` |
| **PR-57** | Independence bottleneck | A small team cannot satisfy R3 separation, and the honest outcome blocks the work | A machine-checkable independence profile, an honest `BLOCKED` rather than a quiet waiver, and an external reviewer path | Assurance Lead | `R29` |
| **PR-58** | Rigour and throughput collapse | Every task receives the full expensive verification, reproduction and human flow, and the laboratory stops | Adaptive assurance routed by consequence and uncertainty, risk profiles, selective escalation, and Pareto regression gates — **with multi-agent cognition preserved** | Research Director | `R30` |

> **A risk closes on a control that has been observed working, not on a
> mitigation that has been written.** None of these is closed. Every mitigation
> in the table is `SPECIFIED`, and the packages that would implement them have
> not started.

## Scoring

Programme risks are tracked with impact and likelihood on a 1–5 scale. However,
**critical security, identity, evidence, reproduction and data blockers cannot be
lowered by a numeric total.** The numeric score exists for prioritisation; it is
not a waiver mechanism.

## Risk closure

A risk does not close on "mitigation applied". Closure requires a control
effectiveness test, an evidence reference, a residual-risk owner and a
re-evaluation date.

On cutover day every critical risk must be `CLOSED` or explicitly classified
`ACCEPTABLE` by policy. Non-waivable risks cannot be `ACCEPTABLE`.
