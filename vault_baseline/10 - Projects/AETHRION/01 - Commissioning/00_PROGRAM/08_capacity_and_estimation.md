---
title: "Capacity and Estimation Model"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/08_capacity_and_estimation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Capacity and Estimation Model

## Why there is no fixed calendar

The target system varies widely with team size, existing infrastructure, managed
service preferences, data classes and institutional controls. Files therefore
carry an effort class; the calendar is computed after WP-001 against real
capacity.

## Three-point estimation

Each package receives the following at refinement:

- `O`: optimistic person-days, assuming contracts and infrastructure are ready.
- `M`: expected person-days.
- `P`: pessimistic person-days, allowing for migration, security or integration
  surprises.
- PERT: `(O + 4M + P) / 6`.

## Capacity pools

| Pool | Example roles | Capacity to protect |
|---|---|---|
| Architecture/Contracts | Chief Architect, schema owner | Contract and ADR review |
| Platform/SRE | Platform, DB, network, SRE | Foundation, HA, DR |
| Security/Governance | Security, safety, IAM, privacy | Policy, threat testing, approval |
| Research/Knowledge | Method, evidence, librarian | Literature and claim semantics |
| Assurance/Eval | Reviewer, verifier, reproducer | **Independent acceptance; never consumed by the feature team** |
| Product/Experience | UI, CLI, UX, accessibility | Cockpit and decision surfaces |
| **Metascience** | Calibration, agreement, controls | **Measurement; never consumed by delivery pressure** |

The two protected pools are protected for the same reason: both produce
information that delivery pressure would otherwise trade away, and both produce
it slowly.

## WIP limits

- One owner carries at most two `IN_PROGRESS` packages at a time.
- At least 25% of assurance capacity is reserved for correction and
  re-verification.
- For critical-path packages, an integration window is reserved in the dependent
  team's calendar in advance.
- Control and evidence contracts are never delayed for UI or reporting during the
  foundation wave.
- No new feature package opens in the final two commissioning cycles before
  cutover.

## The human decision bottleneck

In a model-operated lab, model capacity is elastic and human decision capacity is
not. A model can produce more decision requests per day than any person can
consider properly.

> Human decision capacity is therefore modelled as a **hard quota**, not a
> throughput target. When the quota is exhausted the queue waits. There is no
> express-review mode, because an express review is not a review.

Measured alongside it: decision-time distribution, which evidence sections were
opened, the G10 reversal rate, and the rate of acceptance despite an adversarial
rejection. A rising reversal rate is the earliest observable signal of
rubber-stamping.

## Converting to a calendar

1. Estimate all `READY` packages with three-point estimation.
2. Compute real weekly capacity per role pool, net of holidays, on-call and BAU.
3. Extract the critical path from the hard-dependency graph.
4. Model review and reproduction delay as a **separate queue** — it does not
   share capacity with implementation.
5. Reserve at least 20% for integration and correction.
6. Validate the production date against the WP-115 acceptance burn-down and the
   WP-119 rehearsal result.

Schedule pressure cannot be used to defer target capabilities. If something has
to move, the production date moves, not the scope.

## What baseline v1.2.0 added to the estimate

Seven packages, effort mix **0 S · 2 M · 5 L** —
against a programme mix of 9 S · 51 M · 88 L.
Five of the seven are **L**, which is the honest signal: this is not a trim of
supporting work, and estimating it as one is how the production date moves later
without anyone deciding that it should.

Three properties of this wave affect capacity in ways the effort class alone does
not carry:

- **WP-141 gates the rest.** Assimilation governance after assimilation is
  documentation rather than control, so it cannot be parallelised behind the
  packages that depend on the mechanisms it governs.
- **Half of every test table in this wave is a refusal case.** A refusal case
  needs a working system *and* a way to make it fail, which costs more fixture
  work than a happy-path case and is routinely estimated as if it did not.
- **The Assurance and Metascience pools carry more of it than the effort class
  suggests** — verifier qualification, control injection and error-correlation
  measurement are the pools the WIP limits above already protect from delivery
  pressure, and this wave increases the demand on both.

## What baseline v1.3.0 added to the estimate

Twelve packages, effort mix **0 S · 2 M · 10 L**. Ten of the
twelve are **L**, which is a heavier wave than the one before it and is not an
estimation artefact — most of these packages deliver a control *and* the
injection suite that proves it fires.

Three properties that change capacity beyond what the effort class carries:

- **WP-148 gates the wave.** A communication optimiser built before the cohort it
  optimises has no quality guard to anchor against, and a budget controller built
  before the ledger has nothing to degrade.
- **Two runnable arms, not one.** Every efficiency claim here is measured against
  a naive fully-connected baseline that must also be built, run and maintained.
  The baseline is not a fixture — it is a second execution path.
- **Most cases are injections.** A refusal case needs a working system *and* a
  way to make it fail; a split-brain case needs a way to kill a publisher
  mid-commit. That is materially more fixture work than a happy-path case and is
  routinely estimated as if it were not.

The pools this lands on are the two the WIP limits already protect from delivery
pressure: **Assurance/Eval** and **Metascience**. Between v1.2.0 and v1.3.0 the
demand on both roughly doubled while neither gained capacity, which is a
scheduling fact rather than a risk to be mitigated later.
