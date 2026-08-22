---
title: "Definition of Ready and Definition of Done"
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/05_definition_of_ready_and_done.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Definition of Ready and Definition of Done

## Definition of Ready — all packages

A package becomes `READY` only when all of the following hold:

- The package purpose and its single delivery boundary are clear.
- Out-of-scope items are written down.
- An Accountable Owner, an implementer and an independent verifier are assigned.
- Hard dependencies are `ACCEPTED`, or in an explicitly permitted mock-contract
  state.
- Affected canonical owners and interfaces are identified.
- DataClass, ToolEffect, CodeTrust and network/credential scope are classified.
- Required environments and test fixtures are accessible.
- Acceptance criteria are **measurable** and the owner of the test command or
  scenario is identified.
- Migration, rollback or compensation behaviour is defined.
- A three-point effort estimate and a capacity owner exist.
- Open blockers and assumptions are visible.

> **On measurability.** The generic criteria in the current package template
> ("all mandatory tests have passed") are not measurable in the sense meant here.
> A package is genuinely `READY` when its criteria name a number, a threshold or
> a command. Refinement is where that specificity is added; without it the
> package cannot be closed objectively.

## Technical completion

`TECH_COMPLETE` states only that the implementation is ready:

- Code, policy, schema and IaC are ready for review.
- Unit and package-level integration tests have run.
- Required migration and rollback dry runs have been performed.
- Telemetry, correlation and audit signals are in place.
- Documentation and runbook changes are committed.
- A draft evidence manifest exists.

## Definition of Done — package acceptance

- All acceptance criteria passed **on the same target revision**.
- Test results are bound to artifact hashes and an environment manifest.
- The verifier performed verification **independently of the producer**.
- Security, data and policy negative tests passed.
- Contract compatibility and downstream consumer tests are green.
- No open critical or high findings; accepted medium/low risks carry a named
  owner and an expiry.
- Rollback or compensation behaviour was exercised at least once.
- Working evidence exists via an observability dashboard, alert or audit query.
- The evidence manifest is signed and written to an immutable store.
- The package status is `ACCEPTED`; once the dependent vertical slice passes it
  is recorded as `INTEGRATED`.

> **Bootstrap constraint.** The last item requires an immutable store, delivered
> by WP-026, which itself sits several dependency levels downstream of WP-001.
> As written, no package can satisfy this — including the first one. An interim
> evidence policy defining a temporary, externally time-anchored evidence store
> is a precondition for the programme starting at all. Written as
> [**WP-000**](../01_GOVERNANCE/wp_000_interim_evidence_policy.md); the
> timestamping mechanism it needs is **WP-139**.
>
> WP-000 resolves the **storage** half of the deadlock by expressing the
> `EvidenceManifest` as a signed in-toto attestation with an external time
> anchor, rather than by building an immutable store first. The profile in force
> is `airl-interim-v0.1`: a local signing key and a local anchor, **not** a
> transparency log and **not** keyless — WP-139 supplies those. The **other**
> half, finding **C2**, is decided by
> [`ADR-001`](../../04 - Architecture/adr_001_solo_operator_independence.md):
> R1 solo, R2 declared partial, R3 `BLOCKED`.

## Definition of Commissioned

An `ACCEPTED` package is still not production-ready. To become `COMMISSIONED`,
every acceptance scenario that uses the package must pass **on the same release
candidate**. A `SKIPPED` scenario on a critical package does not count as a pass.

## Evidence that is not accepted

- An agent's or implementer's free-text declaration of success.
- Test outputs from different revisions mixed together.
- A screenshot with no hash or environment information.
- An independence claim from a reviewer who saw the producer's trace.
- A test passing against a mock presented as a real integration test.
- A happy-path demonstration only.
- A confidence number with no measurement behind it.
