---
title: "Evidence and Acceptance Strategy"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/06_evidence_and_acceptance_strategy.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Evidence and Acceptance Strategy

## Evidence manifest

Every package produces an `EvidenceManifest` carrying at minimum:

```yaml
package_id: WP-xxx
target_revision: sha256-or-git-commit
environment_manifest: artifact-ref
policy_bundle: git-digest
schema_bundle: git-digest
test_results: []
security_results: []
contract_results: []
rollback_result: artifact-ref
review_records: []
open_findings: []
owner_decision: decision-id
created_at: timestamp
signature: sigstore-ref
external_timestamp: ots-ref        # WP-139 — independent time anchor
```

The `external_timestamp` field matters more than it appears. Every other field
in this manifest is verifiable only by someone who already trusts this system.
An external time anchor is the one piece of evidence that survives that
assumption being dropped.

## Evidence layers

| Layer | Question | Example |
|---|---|---|
| E0 Structural | Does the file, schema or reference exist? | JSON Schema validation, hash verification |
| E1 Mechanical | Is the behaviour correct under a deterministic test? | Unit, integration, policy tests |
| E2 Security | Is the forbidden path actually blocked? | Negative route, egress, permission tests |
| E3 Independent review | Did an actor outside the producer examine the semantics? | Blind `ReviewRecord` |
| E4 Reproduction | Does the same package run again in a clean environment? | `ReproductionReport` |
| E5 Operations | Are failure, restore and observability correct? | Chaos / DR / SLO evidence |

Which layers are required varies with package risk, but on critical packages the
applicable layers among E0–E5 cannot be waived.

**Cheap layers run first.** E1 mechanical checks cost seconds; E3 independent
review costs a reviewer's attention. Running them in the wrong order wastes the
expensive resource on problems the cheap one would have caught.

### E1 is two things, and baseline v1.2.0 separated them

The layer above reads "mechanical" as one category. For evidence *about the
repository* — does this file exist, does this digest match, does this policy test
pass — that is right. For evidence *about research*, the word was covering two
incompatible kinds of check, and `ADR-008` splits them:

| Class | What it is | Failure semantics |
|---|---|---|
| **V0** | Deterministic — digest, schema, signature, reference resolution | **Non-waivable.** Same input, same answer, always |
| **V1** | Computational or statistical — score recomputation, statistical test, tolerance | **Non-waivable**, given pinned software and configuration |
| **V2** | Model-mediated semantic — citation entailment, claim scope, method–code alignment | A **finding** with a measured error rate, routed to review. Requires a current qualification |
| **V3** | Human scientific judgement | Authority, not throughput |

The reason this matters to the evidence strategy rather than only to the
architecture: the rule *a mechanical check runs first and cannot be overridden by
a model* is correct for V0 and V1, and absurd at V2, where it says a model's
judgement cannot be overridden by a model. **A verification result carries its
class**, assigned by the verifier service from the procedure that actually ran —
never by the caller.

### A control that has never refused is not evidence

Every critical detector carries a **known-positive that must fail** and a
**known-negative that must pass**, in the same run that produces its clean
result. A suite in which a planted control stays silent fails, regardless of what
it reports.

This is not a new principle here — `scripts/monitor_sources.py` has always exited
non-zero when its planted retracted DOI went undetected. Baseline v1.2.0
generalises it to every verifier, and `check_upstream_lineage.py --self-test` is
the pattern applied to a checker's own rule set.
## E6 — External benchmark qualification

E0–E5 are all evidence this project produces about itself. Every one of them can
be complete, signed, witnessed and internally consistent while the system is
worse than a much simpler one at the thing it exists to do. That is not a
hypothetical failure of self-assessment; it is the normal one. **E6 is the layer
where the measurement is not ours.**

A V1 release dossier covers five axes. They are separate because a system can be
strong on one and unusable on another, and an average across them hides exactly
that.

| Axis | Question it answers | Instruments |
|---|---|---|
| **Scientific capability** | Can it do the research task at all? | ResearchClawBench, ScienceAgentBench, and domain-fit benchmarks chosen for the actual field |
| **Verifiability and reproduction** | Does the evidence hold when someone else checks it? | Chain-of-evidence audit tasks, PaperBench- and JudgeEval-style reproduction and grading sets |
| **Multi-agent reliability** | Does the cohort fail in the ways cohorts fail? | The MAST failure taxonomy, Who&When attribution data, and the internal faulty-agent suite (WP-152) |
| **Security** | Does the boundary hold under adversarial input? | Agent Security Bench, WASP, and the internal capability-gate injection suite (WP-155, ACC-117) |
| **Engineering maintenance** | Does it stay correct as its dependencies move? | CodeSyncBench- and AgentIssue-style regression sets, where a comparable harness is feasible |

The fifth axis is the one most often left out, and leaving it out is what makes a
system that benchmarked well eighteen months ago quietly stop working.

### Three rules that constrain how E6 may be used

**A benchmark's licence governs its use, and redistribution is the usual trap.**
Several of the instruments above are non-commercial, share-alike, or licensed
only for evaluation. The register in `provenance/upstreams.json` records the
licence for each, and the assimilation type for a benchmark is `BENCHMARK`
precisely so that it cannot be confused with a dependency that ships.

**Benchmark source code is never merged into product code.** It lives behind the
firewall described in `ADR-017` and WP-158, and it is reachable from an
evaluation harness and from nowhere else. The reason is not licence hygiene —
that is a side benefit. It is that a benchmark inside the product is a training
signal inside the product, and a score produced afterwards means nothing.

**Every result is pinned to model, provider, snapshot, version and date.** A
benchmark number with no model snapshot beside it is not a result about this
system; it is a result about an unnamed configuration on an unnamed day. The
`ModelExecutionFingerprint` (WP-157) is what makes the pin something other than a
promise, and a score whose run reached benchmark material through retrieval is
labelled contaminated and **is not silently rerun for a cleaner one**
(ACC-118).

> **Current state.** No axis has been run. E6 is specified here so that the
> release dossier has a shape to fill, and so that the first person to run a
> benchmark does not have to invent the rules under time pressure — which is
> when the licence gets skipped and the snapshot goes unrecorded.

## Release quality is a frontier, not a verdict

An acceptance scenario answers pass or fail. That is the right shape for a
control and the wrong shape for an architecture decision, because every
optimisation this system makes trades along four axes at once: **quality, cost,
latency and human effort.** A change that improves one and silently damages
another has moved the problem, and a pass/fail gate cannot see it.

So each architectural optimisation is reported on the frontier, using a fixed
measurement set. The set is fixed so that two optimisations are comparable; it is
public so that a favourable subset cannot be selected after the fact.

| Group | Measures |
|---|---|
| **Volume** | Total model calls · input tokens · output tokens · inter-agent tokens |
| **Coordination** | Coordination overhead ratio (inter-agent tokens ÷ total) · redundant message rate · **useful challenge rate** · rounds to convergence |
| **Latency** | Wall-clock per task · time to first material challenge |
| **Reuse** | Tool-result reuse hit rate · context projection hit rate |
| **Human** | Human minutes per decision · per correction · per accepted claim |
| **Scientific** | Claim survival rate · reproduction success rate · verifier coverage · verifier abstention rate |
| **Unit economics** | Cost per `VerifiedValue` · cost per accepted claim |

Two of these deserve their own sentence. **Useful challenge rate** is the ratio
that stops the coordination measures from being gamed: cutting every message
between agents drives redundant message rate to zero and drives useful challenge
rate to zero with it, and only the second number reveals that the cohort has been
silenced rather than optimised. **Verifier abstention rate** is a health measure
rather than a failure measure — a verifier that never abstains is either
perfectly calibrated or not calibrated at all, and the second is far more common.

### The targets, and what kind of thing they are

Baseline v1.3.0 proposes, as **starting release targets**:

- optimised cohort communication and tokens **≥50% below the naive
  fully-connected baseline**;
- scientific quality drop **≤2%** against that same baseline;
- redundant inter-agent communication **<15%**;
- communication token share **<25–30%** of total;
- unresolved material challenges silently dropped: **0** — this one is not a
  target, it is a hard zero (ACC-090).

**These are targets to be frozen after calibration, with confidence intervals —
not constants derived from the literature.** They come from reported results on
other systems doing other work, and importing them as thresholds would be the
same error as importing a benchmark score: a number that is true somewhere,
asserted here. The first calibration run replaces every figure above with a
measured one and records the interval; until then they are a direction of travel
and are labelled as such wherever they appear.

The baseline for all of them is the **runnable naive fully-connected cohort**,
not a single agent. Comparing to a single agent measures the cost of having a
cohort at all — a question `ADR-011` settled on epistemic grounds, and one that a
cost measurement is not entitled to reopen (ACC-086, ACC-087).


## Finding lifecycle

```text
REPORTED → STRUCTURALLY_VALID → REPRODUCED → VALIDATED
         ↘ NOT_REPRODUCIBLE / DUPLICATE / OUT_OF_SCOPE
VALIDATED → FIXED → REVERIFIED → CLOSED
```

A correction is opened only for `VALIDATED` findings. A critical finding cannot
be closed as "probably a false positive" — a reproducer result is required.

Every finding must reach a terminal state. A finding that is neither closed nor
explicitly parked with an owner and an expiry has not been handled; it has been
forgotten. See the finding-ledger requirement in
`skills/arbitrating-disagreement`.

## Acceptance levels

- **Package Acceptance:** the package's own contracts and tests.
- **Integration Acceptance:** the real interface between two or more services.
- **Vertical Slice Acceptance:** the business outcome across the relevant portion
  of G0–G10.
- **System Commissioning:** ACC-01–ACC-120, the attack suite, DR and capacity.
- **Human Go-Live Decision:** an authorised decision taken by someone who has
  seen the evidence summary and the residual risk.

## Traceability

Every requirement is bound as `REQ-*`, every control as `CTL-*`, every work
package as `WP-*`, every test as `TST-*`, every acceptance scenario as `ACC-*`,
every finding as `FND-*` and every decision as `DEC-*`.

The go-live dossier must be able to answer the query
`REQ → WP → TST/ACC → Evidence → Decision` for any requirement.

> **Current state.** The WP↔ACC mapping exists in two places — the dependency
> matrix and the ACC documents — with different, undocumented semantics. Until
> one is designated authoritative and the other generated from it, the
> `COMMISSIONED` rule cannot be evaluated mechanically. See finding **M5** in the
> audit report.
