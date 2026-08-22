> [!info] Generated view
> This note is generated from `skills/blind-reviewing/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: blind-reviewing
version: 1.0.0
description: Use when assigned as a blind reviewer, when assessing a frozen review packet, or when producing a ReviewVerdict
gates: [G6]
roles: [Blind Reviewer]
assurance_classes: [R1, R2, R3]
requires_skills: [independence-discipline]
emits: [ReviewVerdict]
mechanical_checks: [packet_only_access, no_producer_trace_accessed]
---

# Blind Reviewing

## Core principle

You see only the **frozen packet**. You do not know how the producer reasoned —
and you must not.

## Access boundary

Do not search for, request, or infer anything outside the packet. If you need
information the packet lacks, **ask the Assurance Lead**, never the producer.
Contacting the producer converts a blind review into a conversation.

## Assessment axes

| Axis | Question |
|---|---|
| Method | Can this protocol answer this question? |
| Evidence sufficiency | Is there enough for the claim? |
| **Evidence diagnosticity** | Does the evidence **eliminate** rival explanations, or is it compatible with all of them? |
| Scope | Does the claim assert more than the data permits? |
| Reproducibility | Do the manifests actually make reproduction possible? |
| Severity | Would the falsification test have caught the claim if it were false? |

## Diagnosticity — the most important question

> Evidence compatible with **every** rival hypothesis is **worthless** — it
> discriminates nothing.

Volume of evidence is not strength of evidence. Count the discriminating items,
not the total. Ten citations that are all consistent with both the claim and its
negation carry less weight than one that rules the negation out.

## Verdict

`ACCEPT` — unconditional
`CONDITIONAL_PASS` — with **numbered, individually actionable** conditions
`REJECT` — on grounds of method, evidence or integrity; **not "I disliked the
result"**

A vague condition cannot be satisfied. Each condition describes one action.

## Anti-bias rules

- **Order effects:** where several claims are reviewed, **randomise the order**
- **Self-recognition:** the packet is anonymous; do not infer authorship from
  writing style, and do not act on the inference if you form one
- **Length bias:** a long report is not a good report
- **Conformity:** you do not see other reviewers' verdicts, by design

## Red flags

- You needed information outside the packet and did not request it properly
- Your verdict's rationale concerns the direction of the result
- You gave every claim the same verdict
- You scored evidence volume rather than diagnosticity
