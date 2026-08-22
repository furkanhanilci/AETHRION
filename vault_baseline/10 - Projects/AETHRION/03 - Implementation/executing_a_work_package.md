---
title: "Executing a Work Package"
type: reference
category: commissioning
status: WORKING
summary: "V1 is the whole commissioning plan, and it is executed one work package at a time."
source: "docs/EXECUTING_A_WORK_PACKAGE.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/commissioning
---

> [!info] Generated view
> This note is generated from `docs/EXECUTING_A_WORK_PACKAGE.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Executing a Work Package

| Field | Value |
|---|---|
| Document type | Runbook — the loop that moves one package from ready to accepted |
| Scope | V1 execution: the commissioning programme, one package at a time |
| Sibling documents | `READY.md` (what can be started) · `STATUS.md` (what the checks say) · `../planning/commissioning/00_PROGRAM/05_definition_of_ready_and_done.md` (the definitions this enforces) |
| Status | `WORKING` — every command below has been rehearsed end to end, including each refusal |
| Date | 2026-08-22 |

**In one paragraph.** V1 is the whole commissioning plan, and it is executed one work package at a time. This is the loop: pick from the ready queue, start it, do the work the package document specifies, issue an evidence manifest, mark it technically complete, and have someone who is not the producer accept it. Each transition runs through `scripts/progress.py`, which refuses the moves the plan forbids and names the document that forbids them. Nothing here advances the programme on its own — it makes advancing it possible without breaking the seal.

---

## 1. Before anything: what state is the programme in?

```bash
python3 scripts/ready_queue.py          # regenerate docs/READY.md
python3 scripts/progress.py show WP-001 # one package, its owner, its dependencies
```

`docs/READY.md` answers *what can I start today*. At t0 the answer is exactly one
package: **WP-001**, the commissioning charter. Everything else waits on
something unaccepted, and that is the plan working, not the plan stuck — WP-001
is the package that authorises the programme.

## 2. The loop

| Step | Command | What it refuses |
|---|---|---|
| **Pick** | read `docs/READY.md` | — |
| **Start** | `progress.py start WP-XXX` | A package whose hard dependencies are not `ACCEPTED` |
| **Do the work** | follow the package document's *Implementation tasks* table | — |
| **Produce evidence** | `evidence_manifest.py issue --package WP-XXX …` | — |
| **Technically complete** | `progress.py tech-complete WP-XXX` | Any package with no manifest, or a manifest that does not verify |
| **Accept** | `progress.py accept WP-XXX --verifier NAME --assurance R1\|R2` | Acceptance before `TECH_COMPLETE`; a verifier who is the accountable owner; anything at **R3** |

A refusal looks like this, and it is not advice:

```
refused: R3 work cannot be accepted by this organisation
  authority: ADR-001 §6 — R3 is BLOCKED by design, declared rather than waived
```

If a transition is refused, the answer is to satisfy the condition or to change
the decision that created it — in a decision record, not on the command line.

## 3. Where state lives, and why it is not in the plan

| Question | Answer lives in | Sealed |
|---|---|---|
| What is this package, and what must it produce? | the package document | **yes** |
| What was its status when the baseline froze? | the package document | **yes** |
| What is its status now? | `delivery/progress.json` | no |
| What can be started today? | `docs/READY.md`, generated | no |

The separation is load-bearing. If status lived inside the sealed file, starting
work on a package would invalidate the integrity proof of the plan the work was
against — progress would look like tampering, and keeping the seal green would
require re-sealing on every status change, which
`09_change_and_configuration_control.md` names as the one prohibited use of the
seal. `scripts/progress.py` writes the ledger and regenerates the queue; it never
touches `planning/`.

## 4. Acceptance under one operator

`ADR-001` decided what independence means here, and the CLI enforces it:

- **R1** — accepted solo. Normal path.
- **R2** — accepted solo **only** under a declared partial independence profile.
  The tool writes that declaration into the ledger entry so the limitation
  travels with the claim rather than being remembered.
- **R3** — **refused**. Not waived, not escalated: blocked, and the refusal cites
  the record that blocked it. R3 work is work this organisation cannot accept
  alone, and pretending otherwise is the failure the whole system exists to
  prevent.

## 5. What still has to be done by hand

Honest list, because a runbook that implies more automation than exists is worse
than no runbook:

- **The work itself.** Every package's *Implementation tasks* table is executed
  by a person or an agent; nothing here does it.
- **Assurance class.** R1/R2/R3 is decided per project at G1 through WP-005, not
  derived per package. It is passed in at acceptance and recorded.
- **Acceptance scenarios.** `ACC-01`–`ACC-51` are not tracked in the ledger yet;
  the `scenarios` key exists and is empty. Until scenarios are tracked,
  `COMMISSIONED` cannot be computed, only `ACCEPTED`.
- **Definition of Ready.** The CLI checks dependencies. It does not check that an
  owner is assigned, that an estimate is recorded or that fixtures are reachable
  — those are DoR items a human confirms.

## 6. First real move, whenever it is made

```bash
python3 scripts/progress.py start WP-001
# … execute the charter tasks …
python3 scripts/evidence_manifest.py issue --package WP-001 --gate Program \
    --subject <the charter artefacts> --check "<what was verified>"
python3 scripts/progress.py tech-complete WP-001
python3 scripts/progress.py accept WP-001 --verifier "<not the owner>" --assurance R1
python3 scripts/write_status.py
```

That sequence has been rehearsed against this repository, including every
refusal, and rolled back. The programme is at t0 by intent: one package ready,
one technically complete, nothing accepted.
