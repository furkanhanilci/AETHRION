# Change and Configuration Control

## Baselines

The programme versions at least the following separately:

- Architecture decision bundle
- Role and policy contract bundle
- Event/schema bundle
- Infrastructure/IaC bundle
- Model capability/admission bundle
- Tool registry bundle
- Data/source/claim schema bundle
- Acceptance scenario bundle
- Production release candidate manifest
- **Skill bundle** — the execution discipline agents operate under

The skill bundle is versioned for the same reason as the policy bundle: it
changes agent behaviour, and a result produced under one version is not
comparable to one produced under another.

## Change classes

| Class | Example | Approval |
|---|---|---|
| Editorial | Clarification that does not change meaning | Package owner |
| Compatible | Backward-compatible optional field | Schema owner + contract test |
| Material | Gate, route, owner, retention or acceptance change | Architecture/Governance board |
| Critical | Trust zone, data boundary, canonical owner, blocker waiver | Decision Owner + Safety + Assurance |

## Change flow

```text
Change Request → Impact Scan → ADR/Schema Proposal → Independent Review
               → Decision → Implementation Packages → Regression/Replay
               → Baseline Promotion
```

An Impact Scan lists open workflows, frozen literature sets, claims, admission
profiles, runbooks and acceptance scenarios. A material change takes effect only
with a new baseline; prior decisions and artifacts remain unchanged.

## Configuration drift

- Production changes cannot be made outside GitOps; a break-glass change opens an
  incident and a reconciliation.
- A model alias change is not accepted as a pinned snapshot; requalification is
  required.
- Policy bundle rollback goes to a signed previous version and the decision log is
  preserved.
- Database migrations carry both a forward and a rollback/downgrade strategy; an
  irreversible migration is applied in two stages.
- External edits in Zotero and Obsidian do not automatically become truth in the
  canonical registries; ingest and reconciliation rules run.

## Plan file versioning

An accepted WP file is not modified retroactively. A new requirement adds a file
revision note and a change ID; the prior evidence manifest preserves which
revision it was accepted against.

> **Current applicability.** No package is currently `ACCEPTED`, so every plan
> file is still freely modifiable. This rule becomes binding from the first
> acceptance onward — which is also the point at which the plan stops being a
> draft.

## Plan integrity — three checks, not one

The seal is necessary and **not sufficient**. Baseline v1.0.1 exists because
three defects survived it while every file was byte-identical to its sealed
state: colliding acceptance identifiers, a go-live requirement that depended on
post-go-live packages, and stale ranges.

| Check | Proves | Cannot see |
|---|---|---|
| `sha256sum -c` | sealed files did not change | whether they agree with each other |
| `validate_commissioning_plan.py` | references resolve both ways · the DAG is acyclic · phases are valid · go-live is feasible | whether the plan is a *good* plan |
| `check_doc_consistency.py` | declared counts match reality · no decision record contradicts its own status | anything outside the declared numbers |

**A plan change is complete only when all three pass** and the change is recorded
in the implementation log. Re-sealing to silence a failing check is the one
prohibited use of the seal.

## Plan integrity

The canonical plan is sealed:

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

Every entry must report `OK`. A mismatch means a plan file changed without the
seal being regenerated. The seal is regenerated deliberately, as part of a
recorded change — never as a routine step to silence a failing check.

The Obsidian mirror is a **generated** reading copy. Plan content changes in the
canonical file first, then propagates. Editing the mirror directly creates a
divergence that the seal will not detect, because the seal does not cover the
mirror.
