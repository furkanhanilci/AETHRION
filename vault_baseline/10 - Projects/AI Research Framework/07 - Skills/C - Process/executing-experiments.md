> [!info] Generated view
> This note is generated from `skills/executing-experiments/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: executing-experiments
version: 1.0.0
description: Use when running experiment batches at G5, when jobs are being dispatched to compute, or when a run fails mid-batch
gates: [G4, G5]
roles: [Engineering Owner, Research Software Engineer]
assurance_classes: [R1, R2, R3]
requires_skills: [preregistration-discipline, using-isolated-environments, verification-before-completion]
emits: [ExperimentRun, ToolReceipt]
mechanical_checks: [manifest_hashes_pinned, budget_within_hard_limit, artifacts_scanned]
---

# Executing Experiments

## Core principle

Execution is the mechanical application of a frozen manifest. **No decisions are
made during execution.** If a decision is required, execution stops and returns
to G2.

## Preconditions — all mandatory

- [ ] `ProtocolManifest` locked
- [ ] `AnalysisPlanManifest` locked
- [ ] `LiteratureSetManifest` frozen
- [ ] Baseline run completed and reported
- [ ] Budget approved; soft and hard limits defined
- [ ] Model and tool qualification current

If any is missing, **G5 does not begin.** There is no partial start.

## Pinned per run

```
code_commit · container_digest · capability_fingerprint · policy_revision
protocol_hash · analysis_plan_hash · literature_set_hash · seed
```

These are written into `ExperimentRun`. **An unpinned run produces no evidence.**

> **Note on model identity:** current-generation hosted models carry no
> date-suffixed snapshot identifier. What is pinned is a **capability
> fingerprint** (the model's declared limits and capability tree, hashed), plus
> full input/output logging. Genuine determinism requires local open-weight
> models with a weight-file hash — this is why R3 runs are local.

## Procedure

1. Validate the `TaskContract`; compute the `ExecutionProfile`
2. Reserve compute against the budget
3. Signed image; read-only inputs mounted
4. Open the sandbox; **network defaults to BLOCK**
5. Run
6. Scan outputs (malware, secrets, DLP)
7. Produce manifest and hashes
8. Write to the immutable store
9. Revoke lease, workload identity and secrets

## Negative results

> **A negative result is an artifact, not an exception.** It is not deleted, not
> re-run in search of a different outcome, and not classified as a failed run.

A pipeline that quietly discards negative results manufactures a positive
literature out of nothing.

## Budget

Warning at the soft limit, **stop** at the hard limit. The workflow pauses
without losing state. There is no waiver for exceeding a hard limit.

## Failure inside a batch

If one run fails, **the batch is not re-run wholesale.** The failing run is
investigated separately (`investigating-anomalies`). A re-run receives a new
`run_id`; it never overwrites the original.

## Red flags

- The same `run_id` written twice
- `capability_fingerprint` empty
- Failed runs absent from the report
- A protocol parameter changed mid-execution
- The batch was re-run after seeing partial results
