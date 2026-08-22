---
title: "Independence Discipline"
aliases:
  - "independence-discipline"
type: skill
category: skill
status: WORKING
source: "skills/independence-discipline/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/shared
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/independence-discipline/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: independence-discipline
description: "Use when dispatching any agent, assigning a reviewer or reproducer, or when an agent requests help from another agent"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.gates: "G5,G6,G7"
  airl.roles: "all"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "IndependenceRecord"
  airl.mechanical_checks: "no_producer_spawned_agents,reviewer_assigned_by_assurance_only"
---

# Independence Discipline

## Iron law

> **A PRODUCER MAY NOT SUMMON ITS OWN VERIFIER OR ITS OWN HELPER.**
>
> Not a helper, not a reviewer, not a "second opinion". None of them.

## Why this dimension is non-compensable in every class

If it is violated, **the measurement of the other seven dimensions becomes
meaningless.** A helper summoned by the producer is effectively a co-author but
does not appear in the independence record, so the matrix returns a `PASS` that
describes a state of affairs that does not exist.

## Who assigns whom

| Work | Assigned by |
|---|---|
| Producer task | Task Compiler |
| Reviewer | Assurance Lead |
| Reproducer | Assurance Lead |
| Arbiter | Assurance Lead (sees both sides) |
| Helper agent | **Nobody — helpers do not exist** |

## The eight dimensions

| Dimension | R1 | R2 | R3 | Non-compensable in |
|---|---|---|---|---|
| **Delegation Boundary** | PASS | PASS | PASS | **R1, R2, R3** |
| Context Isolation | PASS | PASS | PASS | R2, R3 |
| Human Identity | PARTIAL | PASS | PASS | R3 |
| Incentive & Reporting | PASS | PASS | PASS | R3 |
| Model Lineage (**measured**) | PARTIAL | PASS | PASS | — |
| Credentials | PARTIAL | PASS | PASS | — |
| Runtime Environment | PARTIAL | PASS | PASS | — |
| Data & Retrieval Path | PARTIAL | PASS | PASS | — |

## Model lineage is a measurement, not a declaration

Two tiers of the same model family are **not** independent — shared training
lineage produces correlated errors. In R2 and R3 the reviewer must come from a
different **provider family**, and even that is provisional: the binding
constraint is the measured pairwise error correlation. See `measuring-agreement`.

Reviewing Sonnet-tier work with Opus-tier from the same provider is recorded as
`self_check`, not as independent review.

## Rationalization table

| Justification | Ruling |
|---|---|
| "It is only a formatting helper" | A helper is a helper. **Forbidden.** |
| "I checked my own work — that is good practice" | Self-checking is good; it is **not independent review**. Record it as `self_check`. |
| "I used a different model, so it is independent" | Different model, same caller. **Delegation violation.** |
| "The reviewer was unavailable" | The queue waits. There is no auto-approve. |
| "This is R1, the rules are looser" | This dimension is non-compensable **in R1 too**. |
| "The helper only read files, it did not write anything" | Reading shapes the output. Still a violation. |
| "I am the only person here" | Then human identity is `PARTIAL` and R3 work is blocked. That is the correct outcome, not a reason to bypass. |

## Red flags

- A second agent invocation descending from the producer in the correlation chain
- Reviewer and producer sharing a workload identity
- A review packet built by the producer
- An independence record marked `PASS` with no measurement behind the lineage claim
