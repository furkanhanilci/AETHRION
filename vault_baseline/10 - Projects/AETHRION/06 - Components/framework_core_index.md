---
title: "`airl_framework` — the shared contract core"
cssclasses:
  - aethrion-index
type: index
category: component
status: TECH_COMPLETE
summary: "This package defines the contracts every later service was supposed to bind to, and nothing binds to it."
source: "src/airl_framework/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/component
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `src/airl_framework/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# `airl_framework` — the shared contract core

| Field | Value |
|---|---|
| Document type | Component reference |
| Scope | Identity, artifact manifest, event envelope and schema registry |
| Sibling documents | `../../docs/architecture/FOUNDATION.md` · `../../schemas/README.md` |
| Status | `TECH_COMPLETE` — and that label is generous; see below |
| Date | 2026-08-22 |

**In one paragraph.** This package defines the contracts every later service was
supposed to bind to, and **nothing binds to it.** `airl_bridge` imports none of
it, the two disagree about how a digest is written, and `SchemaRegistry` is a
dictionary rather than a validator. It is recorded here as finding **H4** because
a contract with no consumer is not a foundation — it is a parallel universe that
happens to compile.

| Object | Defines |
|---|---|
| `Identity` | The correlation fields shared across every plane |
| `ArtifactManifest` | Content hash, lineage, retention, validity |
| `EventEnvelope` | Event id, causation, actor, data class, payload reference |
| `SchemaRegistry` | Registration and version resolution — **in-process, no JSON Schema validation** |

## The disagreement

| | Digest format |
|---|---|
| `ArtifactManifest` | bare 64-character hex |
| `airl_bridge` | `sha256:<hex>` |

Two representations of the same idea, in one repository, neither aware of the
other. **The next work here is not another contract**; it is giving one existing
contract a real consumer, which is what would have surfaced this immediately.

The planned direction is to generate the contract surface from a single
**LinkML** model rather than hand-writing it — see
`docs/architecture/AETHRION_COMPONENT_REUSE.md` §9.
