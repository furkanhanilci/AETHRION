---
title: "Shared Contract Schemas"
type: reference
category: architecture
source: "schemas/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `schemas/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Shared Contract Schemas

Machine-readable schemas for the canonical contracts that cross plane
boundaries.

## Intended contents

| Schema | Work package | What it defines |
|---|---|---|
| `identity.json` | WP-011 | Identity and correlation fields across every plane |
| `artifact-manifest.json` | WP-014 | Content hash, lineage, retention, validity |
| `event-envelope.json` | WP-015 | Event id, causation, actor, data class, payload reference |
| `policy-decision.json` | WP-016 | Authorization and routing decision records |
| `source-literature.json` | WP-017 | Source identity, representation, trust, set manifest |
| `claim-evidence.json` | WP-018 | Claim version, evidence span, review verdict, decision |
| `run-environment.json` | WP-019 | Run manifest, environment, reproduction tolerance |
| `notification.json` | WP-131 | Notification intent and receipt |
| `channel-registry.json` | WP-132 | Channel, data-class ceiling, egress hosts |

## Status

> ⚠️ **Currently empty.**
>
> The contract core in [`src/airl_framework/`](../src/airl_framework/) exists as
> in-process Python classes with no JSON Schema representation and no CI
> enforcement. It also has **no production consumer** — see finding **H4** in
> [`docs/review/`](../docs/review/).
>
> Until these schemas exist and are enforced in CI, WP-020 (Schema Registry and
> Contract SDK) cannot reach `TECH_COMPLETE`, let alone `ACCEPTED`.

## Rules once populated

1. A schema version is **registered**, never redefined. Changing a published
   version is forbidden; publish a new version instead.
2. Major-version changes are breaking. Producer and consumer compatibility is
   checked in CI, not by convention.
3. Every schema carries at least one **negative test** — an instance that must
   fail validation.
4. A contract with no production consumer is dead code. Bind it or delete it.
