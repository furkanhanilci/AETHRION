# WP-159 — Supply Chain, Upstream Drift and Cross-Plane Integrity

## Package card

| Field | Value |
|---|---|
| Work package | `WP-159` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Chief Architect / SRE Lead |
| Hard dependencies | WP-024, WP-027, WP-059, WP-141 |
| Related gates | Platform,G5,G9 |
| Related controls | CTL-SUP-01, CTL-OPS-01 |
| Related acceptance scenarios | ACC-119, ACC-120 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-159_supply_chain_and_cross_plane_integrity.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-159_supply_chain_and_cross_plane_integrity.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Provenance and vulnerability posture come from maintained standard tooling, adapted upstream source is admitted through the same gate as a dependency, and no projection can become a second truth.


## Analysis

### What this package actually decides

Two things that share a failure mode: which tooling establishes supply-chain
posture, and which store owns which truth.

Both are cases of something being trusted that nobody verified — an unscanned
dependency, or a projection read as authority.

### The toolchain, integrated rather than rebuilt

| Tool | The question it answers |
|---|---|
| **SPDX** + **REUSE** | What licence governs this file, machine-readably |
| **OSV-Scanner** | Does any dependency have a known vulnerability |
| **OpenSSF Scorecard** | What is the posture of a project before depending on it |
| **SLSA provenance** | What built this artifact, from which source |
| **Sigstore / Cosign** | Is this signed by a checkable identity |

All five are `DEPENDENCY`. Reimplementing any of them would fail the register's
own selection rule — maintained by people closer to the problem — and would be
worse.

### Adapted source is the blind spot

An installed dependency has a name, a version and an ecosystem watching it. A
file copied from another project and refactored has none of those, and every
scanner above looks straight past it.

`ADR-004`'s register is what makes it visible; this package binds it to admission
and release. A file arriving without a pin, a licence read at the source, a file
list, an SPDX header and a characterisation suite **fails CI before merge** —
ACC-120. Drift is monitored and never auto-merged.

### Cross-plane integrity, and why it is here

`ADR-014` assigns one canonical owner per kind of state. This package tests it,
because split brain is invisible in a healthy system and obvious only in a
post-mortem:

- kill the publisher after the database commit;
- deliver an event twice, and out of order;
- return a cancelled task's result;
- **drop a projection and rebuild it** — ACC-119;
- replay a workflow after a restart;
- attempt two concurrent gate transitions.

Every one ends with canonical state correct and the projection agreeing, or with
an explicit recorded failure. **A silent divergence is the failure.**

### Correlation, or none of it is diagnosable

One correlation chain — project, gate, task, agent, model, tool, artifact, run,
claim — carried on OpenTelemetry spans, with secrets and sensitive prompts
excluded or redacted by data class.

Without it a divergence between two stores is a fact nobody can trace to a
cause, which turns every integrity test into a bug report with no next step.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md) | `CI pipelines` · `Verification summary schema adapter` · `Test ownership registry` · `Flake policy` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md) | `Admission policies` · `Trust root management` · `CVE/exception workflow` · `Revocation/impact runbook` |
| [WP-141 — Upstream Assimilation, Lineage and Characterisation Governance](../14_SCIENTIFIC_INTELLIGENCE/WP-141_upstream_assimilation_governance.md) | `AssimilationCandidate schema` · `UpstreamLineage register` · `check_upstream_lineage.py` · `SPDX/REUSE policy` |

### Full prerequisite closure

**46 of 160 packages (29%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-059` |
| 27 | `WP-141` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **28** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Chief Architect / SRE Lead |
| Gates touched | `Platform` · `G5` · `G9` |
| Controls | `CTL-SUP-01` · `CTL-OPS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-119 — Destructive Projection Rebuild](../12_ACCEPTANCE_SCENARIOS/ACC-119_derived_projection_destructive_rebuild.md) | Critical | The rebuild is lossless. No injection produces a silent divergence: each ends with canonical state correct and the projection agreeing, or with an explicit recorded failure. |
| [ACC-120 — Missing Upstream Licence or Provenance](../12_ACCEPTANCE_SCENARIOS/ACC-120_missing_upstream_license_provenance.md) | High | The unregistered file fails admission before merge. The correctly registered one passes. OSV, Scorecard, SLSA provenance and signature verification run over the release, and a dependency with no available fix becomes an owned, expiring residual risk rather than silence. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-141 — Upstream Assimilation, Lineage and Characterisation Governance](../14_SCIENTIFIC_INTELLIGENCE/WP-141_upstream_assimilation_governance.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `CI pipelines` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Verification summary schema adapter` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Test ownership registry` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Flake policy` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `SPDX/REUSE and OSV admission checks` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Admission policies` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Trust root management` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `CVE/exception workflow` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Revocation/impact runbook` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Adapted-source admission control` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `AssimilationCandidate schema` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `UpstreamLineage register` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `check_upstream_lineage.py` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `SPDX/REUSE policy` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `Characterisation test convention` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `Upstream drift review workflow` | `WP-141` | `python3 scripts/progress.py show WP-141` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Supply Chain Security Lead** carries the acceptance decision; **Chief Architect / SRE Lead** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-159-T01 | Integrate SPDX and REUSE conformance into CI | Implementation owner | Commit / configuration / record reference |
| WP-159-T02 | Integrate OSV-Scanner over the lockfile and images | Implementation owner | Commit / configuration / record reference |
| WP-159-T03 | Integrate OpenSSF Scorecard for dependency admission | Implementation owner | Commit / configuration / record reference |
| WP-159-T04 | Produce SLSA provenance and verify Sigstore signatures at release | Implementation owner | Commit / configuration / record reference |
| WP-159-T05 | Bind the upstream lineage register to admission and drift review | Implementation owner | Commit / configuration / record reference |
| WP-159-T06 | Implement the outbox write path and its atomicity guarantee | Implementation owner | Commit / configuration / record reference |
| WP-159-T07 | Build the split-brain injection suite and the projection rebuild proof | Implementation owner | Commit / configuration / record reference |
| WP-159-T08 | Complete the OpenTelemetry correlation chain with data-class redaction | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SPDX/REUSE conformance`
- `OSV and Scorecard integration`
- `SLSA provenance and signature verification`
- `Split-brain injection suite`
- `Correlation chain with redaction`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-159_supply_chain_and_cross_plane_integrity.tests.md`](WP-159_supply_chain_and_cross_plane_integrity.tests.md).

- An adapted file without lineage or licence must fail admission before merge
- A correctly registered adapted file must pass — the check must discriminate
- Upstream drift must open a review item and must not auto-merge
- Each split-brain injection must end in correct canonical state or an explicit failure
- A dropped projection must rebuild losslessly from canonical stores
- A trace must carry the correlation chain and must not carry secrets
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-159_supply_chain_and_cross_plane_integrity.acceptance.md`](WP-159_supply_chain_and_cross_plane_integrity.acceptance.md), together with what this package still cannot establish.

- [ ] Provenance and vulnerability posture come from maintained tooling, not from code written here.
- [ ] Adapted upstream source passes through the same admission gate as an installed dependency.
- [ ] Every projection is rebuildable, and no injection produces a silent divergence.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.


## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- An efficiency measure that improves a cost number and quietly lowers assurance has moved the failure, not removed it. Every optimisation here is anchored to a quality guard and rolls back when it trips.
- A coordination defect is invisible in a healthy run and obvious only in a post-mortem. These packages are specified as injection suites for that reason, not as properties.
- Multi-agent cost pressure always argues for fewer agents. The cohort is fixed by ADR-011 and is not a lever any package here may pull.

## Rollback / compensation

Supply-chain findings are recorded rather than cleared: a dependency with no available fix becomes an owned, expiring residual risk, and a rebuilt projection is verified against canonical state rather than assumed correct.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
