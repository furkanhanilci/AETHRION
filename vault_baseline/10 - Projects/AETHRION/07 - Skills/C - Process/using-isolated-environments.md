> [!info] Generated view
> This note is generated from `skills/using-isolated-environments/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: using-isolated-environments
description: "Use before starting any producing, reviewing or reproducing work that touches files, state or compute"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:using-git-worktrees"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G5,G6,G7"
  airl.roles: "Engineering Owner,Research Software Engineer,Reproducer"
  airl.assurance_classes: "R1,R2,R3"
  airl.emits: "EnvironmentManifest,BaselineVerificationRecord"
  airl.mechanical_checks: "clean_baseline_verified,environment_digest_pinned"
---

# Using Isolated Environments

## Core principle

A non-isolated workspace invalidates the independence claim. And: **never fight
the harness** — if isolation mechanisms already exist, use them rather than
building a parallel set.

## Procedure

**Step 0 — Detect existing isolation.** If you are already in an isolated
workspace, do not create another. If unsure, ask; do not assume. Nested
isolation produces phantom state that nobody cleans up.

**Step 1 — Create the workspace.** Prefer native tooling; fall back to manual.
Before creating, verify the target directory is ignored by version control.

**Step 2 — Install dependencies.** Versions pinned; digest recorded.

**Step 3 — VERIFY A CLEAN BASELINE.**

> Run the existing verification suite. **If it is not fully green, do not
> proceed.**
>
> Reason: work done on a dirty baseline makes it impossible to attribute a later
> failure. You lose the ability to say whether you broke it.

## Isolation dimensions

These map one-to-one onto the Independence Matrix:

| Dimension | Control |
|---|---|
| Directory | Separate workspace |
| Cache | Cleared — no shared build artifacts |
| Identity | Separate workload identity |
| Network | Default BLOCK |
| Data path | Sources **re-fetched**, never taken from the producer's cache |
| Node / namespace | Separate (R2, R3) |

## Additional rule for reproduction

At G7 the reproducer may use **none** of the producer's intermediate outputs —
only the frozen manifest and **primary sources**. Re-using a cached extraction
means reproducing the producer's extraction bug along with the result.

## Cleanup

The workspace is removed when work ends. **Evidence is not removed**: manifests,
hashes and logs remain in the immutable store.

## Rationalization table

| Justification | Ruling |
|---|---|
| "It was clean already" | Show the command output. **Assumption is not verification.** |
| "Re-fetching the sources is slow" | Then reproduction is slow. That is its cost. |
| "The cache is shared but it is only read" | A shared read reproduces shared errors. |
| "Same machine, different directory is enough" | For R1 sometimes. For R2/R3, no. |

## Red flags

- Work started with no baseline verification output
- Reviewer and producer in the same workspace
- Dependency versions unpinned
- Reproduction used the producer's cached data
