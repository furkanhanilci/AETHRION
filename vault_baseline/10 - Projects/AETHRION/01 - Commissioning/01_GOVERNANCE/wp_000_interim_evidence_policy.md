---
title: "WP-000 — Interim Evidence Policy and Attestation Bootstrap"
aliases:
  - "WP-000"
  - "WP-000 — Interim Evidence Policy and Attestation Bootstrap"
type: work-package
category: commissioning
status: TECH_COMPLETE
summary: "Every Definition of Done requires a signed EvidenceManifest held in an immutable store."
source: "planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/wb
  - aethrion/effort/s
  - aethrion/gate/program
  - aethrion/state/tech-complete
---

# WP-000 — Interim Evidence Policy and Attestation Bootstrap

## Package card

| Field | Value |
|---|---|
| Work package | `WP-000` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **S** — small — one owner, one review cycle |
| Accountable owner | Project Decision Owner |
| Independent verifier | Assurance Lead |
| Hard dependencies | — **none, and none is permitted.** A bootstrap package that depends on a downstream package reproduces the deadlock it exists to break |
| Related gates | Program (applies to every gate's evidence requirement) |
| Related controls | CTL-GOV-01, CTL-EPI-01 |
| Related acceptance scenarios | ACC-06 |
| Status at baseline | `TECH_COMPLETE` — tooling implemented, specimen issued and verified; acceptance awaits the verifier arrangement in ADR-001 |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_000_interim_evidence_policy.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_000_interim_evidence_policy.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every Definition of Done requires a signed `EvidenceManifest` held in an
immutable store. That store is delivered by **WP-026**, which sits several
dependency levels downstream of WP-001. As written, **no package can be
`ACCEPTED` — including the first one — so the programme cannot start.** This is
audit finding **C1**.

This package resolves the deadlock by **delegating immutability to existing
public infrastructure instead of building it first**. On completion, a work
package can produce evidence that a verifier can check, that no participant can
retroactively alter, and that requires no trusted third party of the programme's
own.


## Analysis

### What this package actually decides

Not "how do we store evidence". The decision is **whose word makes a manifest
believable**, and WP-000 answers it by refusing to be the answer: immutability is
delegated to infrastructure the programme does not control, so that a verifier
never has to trust the party that produced the evidence.

That is why the package can precede WP-001. It buys nothing except the right to
start, and it is the only package in the programme whose value is entirely
negative — it removes an impossibility.

### Why the deadlock is structural rather than an oversight

The Definition of Done requires a signed manifest in an immutable store; the
immutable store is WP-026; WP-026 sits ten dependency levels below WP-001. Every
package therefore fails its own acceptance criteria, including the one that
authorises the programme. Nothing in the plan is wrong in isolation — the DoD is
correct, WP-026 is correctly placed, and the dependency edges are real. The
deadlock is a property of the graph, which is exactly the class of defect a
reviewer reading packages one at a time cannot see.

### The failure mode this package must not become

An interim policy that outlives its trigger. The whole risk here is that
`airl-interim-v0.1` quietly becomes permanent because it works well enough:
a local Ed25519 key, a local clock, and one operator holding the repository, the
key, the generator and the anchor. That configuration is **tamper-evident, not
externally witnessed**, and the distance between those two phrases is the entire
security claim.

Two controls exist against that drift and both are deliverables of this package,
not aspirations: the manifest carries its own `limitations` list so it cannot be
read as more than it is, and the retirement procedure names WP-026 and WP-139 as
the packages that end it.

### Current implementation state

The tooling is implemented and runs (`scripts/evidence_manifest.py`); a specimen
manifest for this package exists at `delivery/WP-000/evidence.dsse.json`, has
nine subjects, verifies, and rejects both tamper paths. The package is
`TECH_COMPLETE` and **not `ACCEPTED`** — issuance is not acceptance, and the
verifier arrangement it needs is decided by ADR-001, not by this package.

## Out of scope

- The permanent content-addressed WORM store (**WP-026**), which supersedes this
  policy's storage arrangement without invalidating anything issued under it
- The Claim/Evidence Ledger (**WP-075**)
- **The independence question.** This package makes evidence *tamper-evident*;
  it does **not** decide who may act as an independent verifier in a small
  organisation. That is finding **C2** and remains open. Adopting the attestation
  standards below does not close it, and this package must not be read as if it did.

## Execution record — 2026-08-22

The interim profile is implemented in `scripts/evidence_manifest.py`, and a
specimen manifest for this package exists at `delivery/WP-000/`:

```
signature           OK
subject digest      OK   README.md
subject digest      OK   planning/commissioning/00_PROGRAM/SHA256SUMS.txt
subject digest      OK   planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md
time anchor         OK   (interim/local)
payload altered     rejected, as required
```

Both tamper paths are exercised by `tests/test_evidence_manifest.py`: altering a
covered file fails the digest check, and forging the signature fails the envelope
check. Verification exits `1` in both cases.

> **What is implemented is narrower than the target, and the manifest says so.**
> The in-toto Statement and the DSSE envelope are as specified; the signature is
> a **local Ed25519 key** rather than Sigstore keyless, and the attestation is
> **not submitted to a transparency log** — keyless signing needs an interactive
> OIDC flow this environment does not have. The manifest records
> `attestation_profile: airl-interim-v0.1` and carries its own `limitations`
> list, so no reader can mistake it for the full profile. Moving to Sigstore and
> Rekor is the remaining work in this package.

## Interim evidence format

The `EvidenceManifest` is expressed as an **in-toto Statement (ITE-6)**, wrapped
in a **DSSE** envelope, signed through **Sigstore** with a short-lived
OIDC-bound certificate, and recorded in the **Rekor** transparency log.

> **Rekor is a tamper-evident transparency record for signed metadata — not an
> artifact store.** It holds the attestation and its inclusion proof; the
> artifacts, the Sigstore bundle, the certificate chain and the verification
> material still need durable storage. **WP-026 is not cancelled by this
> package**; it is deferred behind it.

**Timestamping is owned here, temporarily.** This package implements its own
minimal external time anchor so that it depends on nothing. **WP-139** later
assumes permanent ownership of timestamping, and this package's implementation
is retired into it — the direction of the dependency is WP-139 → WP-000, never
the reverse.

```
subject:       [{name: <artifact>, digest: {sha256: <hex>}}]
predicateType: https://airl-os.local/EvidenceManifest/v0.1
predicate:
  work_package:     WP-nnn
  gate:             <gate id>
  target_revision:  <git sha / image digest>
  tests:            [{name, result, revision}]
  environment:      {os, runtime, dependency digests}
  schema_versions:  {...}
  policy_versions:  {...}
  verifier:         {identity, decision, timestamp}
  findings_open:    [{id, severity, owner, expiry}]
  residual_risk:    <text>
```

Rationale for adopting rather than inventing is recorded in
`docs/architecture/AETHRION_EXTERNAL_STANDARDS.md` §3.

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

**None.** This package depends on nothing and can start at `t0`. Only two packages in the programme have this property.

### Full prerequisite closure

**Empty.** Nothing has to happen before this package.

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | WB — Bootstrap |
| Dependency depth | level **1** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | Project Decision Owner |
| Independent verifier | Assurance Lead |
| Gates touched | `Program` |
| Controls | `CTL-GOV-01` · `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- A named owner and a verifier **independent of the producer** are assigned, under
  the interim independence arrangement recorded in this package.
- The signing identity provider and the transparency log endpoint are reachable.
- The `predicateType` URI and the predicate schema are fixed and versioned.
- The migration path into WP-026 is written down before the first manifest is issued.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

**No upstream inputs.** Everything this package needs, it produces.

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `S`** — small — one owner, one review cycle.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Project Decision Owner** carries the acceptance decision; **Assurance Lead** must verify independently of whoever implements.
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
| WP-000-T01 | Fix the `EvidenceManifest` predicate schema and its versioning rule | Implementation owner | Schema file + version record |
| WP-000-T02 | Implement manifest generation, DSSE signing and log submission | Implementation owner | Script + a signed specimen manifest |
| WP-000-T03 | Implement verification: signature, inclusion proof, digest match | Implementation owner | Verification run over the specimen |
| WP-000-T04 | Implement the **interim** external time anchor here — no dependency on WP-139 — and record the anchor reference | Implementation owner | Anchor receipt |
| WP-000-T05 | Write the interim independence and verifier arrangement, with its expiry | Project Decision Owner | Signed policy record |
| WP-000-T06 | Write the WP-026 migration and retirement procedure for this policy | Implementation owner | Migration note |

## Mandatory deliverables

- `Interim Evidence Policy` — a signed governance record with an explicit expiry
- The interim timestamping implementation, owned by this package
- `EvidenceManifest` predicate schema, versioned
- Generation, signing and verification tooling
- One end-to-end specimen manifest, signed, logged, anchored and verified
- The WP-026 migration and retirement procedure
- A signed `EvidenceManifest` **for this package itself** — issued under the
  policy it defines, which is the bootstrap step

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-000_interim_evidence_policy.tests.md`](wp_000_interim_evidence_policy.tests.md).

- A manifest whose payload is altered after signing **fails** verification
- A manifest whose subject digest does not match the artefact **fails**
- A manifest absent from the transparency log **fails**, even with a valid signature
- Verification succeeds offline against a stored inclusion proof
- The independent verifier can complete verification **without** the producer's tooling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-000_interim_evidence_policy.acceptance.md`](wp_000_interim_evidence_policy.acceptance.md), together with what this package still cannot establish.

- [ ] An `EvidenceManifest` can be issued, signed, logged, anchored and verified end to end.
- [ ] A tampered manifest is rejected by the verification path.
- [ ] The programme's first packages can reach `ACCEPTED` **without** WP-026.
- [ ] The policy carries an explicit expiry and a named retirement package.
- [ ] The package depends on **no** downstream package, and its timestamping runs without WP-139.
- [ ] The C2 independence question is **restated as still open** in the policy text, not silently absorbed.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.



## Acceptance evidence package

- Test results captured on the same target revision/digest
- The specimen `EvidenceManifest` with its log entry and anchor references
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- **A policy that never expires becomes the permanent architecture.** The expiry
  date and the retirement package are part of the deliverable, not commentary.
- Public log submission publishes **hashes and metadata**. Manifest predicates
  must therefore stay at data class **D0/D1**; no D2+ content may enter a
  predicate. This is a non-waivable constraint of using a public log.
- Reachability of an external log is an availability dependency. An offline
  fallback — locally signed, anchored later — must be defined, and a manifest
  awaiting anchoring is **not** yet acceptance evidence.
- Adopting an attestation standard **does not** create independence. Using it to
  imply C2 is resolved would be exactly the overstatement the audit warned about.
- A "package complete" statement is **not** acceptance. Without a verifier
  decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

Manifests already issued and logged are **never** withdrawn; a superseding
manifest is issued and the earlier entry remains as the historical record. If
the interim policy is retired early, packages accepted under it retain their
acceptance and their manifests migrate into WP-026 by reference.

## Handoff into downstream packages

On acceptance, every package in the programme gains a usable acceptance path.
WP-026 consumes this package's manifests by reference and does not re-issue them;
WP-075 links claims to them; **WP-139 takes over timestamping from this package
and retires the interim implementation.**

This package is the **bootstrap phase**. WP-001 remains the first *normal*
commissioning package: no technology installation begins before WP-001 is
accepted, and WP-001 cannot be accepted before this package exists.
