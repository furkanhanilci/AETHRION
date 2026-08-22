---
name: curating-zotero
version: 1.0.0
description: Use when reading from or writing to Zotero, when a sync conflict occurs, or when agent-managed collections must be updated
gates: [G3, G9, G10]
roles: [Evidence Lead, Source Ingester, Evidence Linker]
assurance_classes: [R1, R2, R3]
non_waivable: true
data_class_ceiling: D1
emits: [SyncReceipt, ReconciliationTask]
mechanical_checks: [conditional_write_used, human_fields_untouched, idempotency_key_present]
---

# Curating Zotero

## Core principle

Zotero is a **working surface**, not the authority. Canonical source identity
lives in the Source Registry.

## Iron law

> **AGENTS NEVER WRITE TO HUMAN FIELDS.**
>
> `notes`, `user_tags`, `highlight_coords` — under no circumstances.

## Two libraries

| | Personal | Project group |
|---|---|---|
| Agent access | **read-only** | writes to the managed namespace |
| Managed namespace | — | `10_*`, `Project/*`, `80_*`, `90_*` |
| Human fields | untouched | untouched |
| Write path | none | Tool Broker → `PATCH` + `If-Match` |

## Data-class ceiling

> **The project group library is cloud-hosted. Nothing above `D1` may be
> written to it.** Unpublished experimental context (`D2`) does not go into a
> group library.

This is easy to violate by accident: a note explaining *why* a source matters
can contain unpublished findings.

## Conflict — 412

```
PATCH ... If-Match: <version>
  → 200  success, emit SyncReceipt
  → 412  ►► DO NOT BLINDLY RETRY ◄◄
          Queue a ReconciliationTask.
          The human edit is preserved.
```

**No blind retry on timeout either** — query state using the idempotency key,
then decide. A blind retry after a timeout is how duplicate writes happen.

## Every write

- Managed-namespace check
- Idempotency key
- `SyncReceipt`: item, field set, prior and new version, timestamp, actor
- **There are no silent writes**

## Human moves

When a human moves a source from `10_Agent_Candidates` to `Project/Methods`,
that is **a decision** and is recorded at ingest. The agent does not undo it,
and does not move it back on the next sync.

## Red flags

- A write without `If-Match`
- An automatic retry after a 412
- A write with no `SyncReceipt`
- D2+ content present in the group library
- An agent-initiated move reversing a human decision
