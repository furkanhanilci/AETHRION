---
name: writing-protocols
description: "Use when authoring a ProtocolManifest, when freezing method at G2, or when a material method change requires a new protocol version"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:writing-plans"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G2"
  airl.roles: "Scientific Owner,Statistical Methods Owner,Red Team Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "writing-analysis-plans"
  airl.emits: "ProtocolManifest,InPrincipleAcceptance"
  airl.mechanical_checks: "no_placeholders,required_sections_present,falsification_plan_nonempty"
---

# Writing Protocols

## Core principle

A protocol is a contract written before the result is known. It leaves the
implementer no interpretive latitude on anything that could change the outcome.

## Required sections

`hypotheses` · `variables` · `dataset` · `baseline` · `success_metrics` ·
`falsification_plan` · `stop_rules` · `exclusion_rules` · `uncertainty` ·
`material_changes`

A missing section is `GATE_FAIL`, checked mechanically. This is not a style
review.

## Placeholder ban

Forbidden: `TBD`, `handle edge cases`, `similar to the above`, `tune as needed`,
`an appropriate threshold`, `standard method`, `etc.`

Every value is written in full: the threshold number, the repetition count, the
tolerance, the version string. A placeholder in a frozen protocol is an
un-frozen decision.

## Exclusion rules — the highest-risk section

`exclusion_rules` is where a protocol most easily becomes result-shaping. Each
rule carries a **rationale** and a **pre-specified threshold**.

> An exclusion rule may not be added or altered after results are seen. If it
> changes, a new `ProtocolManifest` version is issued and the affected analysis
> is labelled `exploratory`.

State also what happens to excluded records: they are reported in the flow
counts, never silently dropped.

## Falsification and severity

For each hypothesis: *"If this claim were false, what observation would show
it?"* Then the harder question: *"Would this test actually catch it?"*

Severity is assessed and signed by the Statistical Methods Owner. **A test that
lacks the power to detect the error produces no evidence when it passes.** A
protocol full of weak tests is more dangerous than one with few strong tests,
because it looks thorough.

## Pre-mortem (R2, R3)

Before G4, the Red Team runs: *"A year has passed and this project failed
completely. Why?"* Moving from future tense to past tense breaks defensive
reasoning. The resulting items are added to `falsification_plan`.

## Self-review checklist

The protocol reviews **itself** before consuming human attention:

- [ ] Every requirement maps to a section
- [ ] No placeholders anywhere
- [ ] Variable names and types are consistent across sections
- [ ] Stop rules and success metrics do not contradict each other
- [ ] Exclusion rules are pre-specified and justified
- [ ] Falsification tests were assessed for power, not just presence

Failing this consumes no reviewer time — it is returned first.

## Red flags

- `success_metrics` present but `falsification_plan` absent
- A threshold expressed as "as appropriate" or "reasonable"
- Protocol and analysis plan in the same file
- Every falsification test is one the method would obviously pass
