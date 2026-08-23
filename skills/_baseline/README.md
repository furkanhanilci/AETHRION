# Skill Behaviour Baseline

| Field | Value |
|---|---|
| Document type | Reference — what a skill baseline is here, and what it is not |
| Scope | `routing.json`, and the harness that reads it |
| Status | `WORKING` for the routing layer; the execution layer is **specified and unrun** |
| Date | 2026-08-23 |

**In one paragraph.** For as long as this repository has existed, its own status
page has carried the line *"skills conform to a format; none has a behaviour
baseline"* — the largest untested claim in the corpus. This directory closes the
half of that claim which can be closed without a model runtime, and states
plainly which half cannot.

## The two layers, and why they are separated

**A skill can fail in two different places**, and only one of them needs a model
to observe:

| Layer | The question | Needs a runtime? |
|---|---|---|
| **Routing** | Given a situation, can the right skill be *reached at all* — and is it distinguishable from the one it is most likely to be confused with? | **No** |
| **Execution** | Once loaded, does the skill change what the agent does? | **Yes** |

The routing layer is not a lesser version of the execution layer. It is a
different failure, and it is the one that was actually broken: **seventeen of
fifty-two skills were reachable by no chain of references from the router.** A
skill nobody can be routed to never loads, so its execution behaviour is not
merely unmeasured — it is irrelevant.

Among the seventeen was `dispatching-parallel-analysts`, which `ADR-012` names as
one half of a pair that must never be substituted for the other. Its engineering
counterpart, `dispatching-parallel-agents`, sat in the router table. A task
needing independent analyses would therefore route to the skill that decomposes
work with one right answer — **precisely the substitution the decision record
forbids**, arrived at not by a bad judgement but by the correct one being
unreachable.

## What `routing.json` holds

- **`reachability`** — the exemption list and its justification. A skill is
  reachable if the router names it, or if a reachable skill names it.
- **`content_invariants`** — per skill, a phrase its own text must contain and,
  where the risk is conflation, one it must not. A skill that has drifted out of
  its own core rule still parses, still loads, and no longer says the thing it
  exists to say.
- **`non_synonym_pairs`** — the four pairs from `ADR-012` §2, each with the
  substitution that must remain impossible.
- **`execution_fixtures`** — task descriptions with the skill each must resolve
  to, and the discipline markers the output must carry. **These have never been
  run.**

## The execution layer is reported as unrun, never as passing

`scripts/check_skill_baseline.py` prints the execution fixture count and the
reason it did not run, and exits on the routing layer alone. It does not skip
quietly and it does not report a green line for work that did not happen.

> The repository's own rule, from `28_CLAUDE_MASTER_IMPLEMENTATION_INSTRUCTION.md`:
> *a check that is unavailable must be reported as unavailable, never marked
> PASS.* A behaviour baseline that reported PASS because it had nothing to run
> would be a more damaging artifact than no baseline at all — it would convert an
> honest gap into a false assurance, which is the exact failure this whole system
> is built against.

## What closing the routing layer does not establish

It does not establish that any skill works. It establishes that every skill can
be reached, that each still contains its own core rule, and that the four
confusable pairs remain distinguishable. Loading the right procedure is a
precondition for following it, not evidence of having followed it.
