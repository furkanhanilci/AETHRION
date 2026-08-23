---
title: "ADR-019 — The Supply Chain Uses Standard Tooling, and Adapted Source Is Part of It"
aliases:
  - "ADR-019"
cssclasses:
  - aethrion-decision-record
type: decision-record
category: architecture
status: ACCEPTED
summary: "ADR-004 fixed how a mechanism is taken from another project: a pinned commit, a licence read at the source, a characterisation suite, a stated authority boundary."
source: "docs/architecture/ADR-019_supply_chain_and_upstream_standard.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
  - aethrion/adr
---

> [!info] Generated view
> This note is generated from `docs/architecture/ADR-019_supply_chain_and_upstream_standard.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# ADR-019 — The Supply Chain Uses Standard Tooling, and Adapted Source Is Part of It

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Which tools establish provenance and vulnerability posture, and how adapted upstream code enters that same regime |
| Sibling documents | **Extends `ADR-004`** (mechanism assimilation) · `AETHRION_EXTERNAL_STANDARDS.md` §4.5 · WP-159 · WP-059 · ACC-120 |
| Status | **ACCEPTED — 2026-08-23.** Toolchain decided; none of it is wired up |
| Date | 2026-08-23 |

**In one paragraph.** `ADR-004` fixed how a mechanism is taken from another project: a pinned commit, a
licence read at the source, a characterisation suite, a stated authority
boundary. What it left implicit is the machinery — which tools establish that
posture, and how adapted source joins the same supply chain as installed
dependencies. Adapted code is the awkward case: it has no package-manager entry,
no version and no upgrade path, so every ordinary supply-chain control looks
straight past it.

---

## 1. The decision

> **Provenance and vulnerability posture are established with maintained standard
> tooling, not with anything written here**, and **adapted upstream source is
> admitted through the same gate as an installed dependency.** No mechanism is
> reimplemented that SPDX, REUSE, OSV-Scanner, OpenSSF Scorecard, SLSA or
> Sigstore already covers.

> This record **extends `ADR-004`** and does not restate it. What a mechanism
> may never decide, and what a direct adaptation obliges, are there.

---

## 2. The toolchain, and what each answers

| Tool / standard | The question it answers |
|---|---|
| **SPDX** + **REUSE** | What licence governs this file, machine-readably |
| **OSV-Scanner** | Does any dependency in the lockfile or image have a known vulnerability |
| **OpenSSF Scorecard** | What is the security posture of a project before depending on it |
| **SLSA provenance** | What built this artifact, from which source, on what |
| **Sigstore / Cosign** | Is this artifact signed, and by an identity that can be checked |

All five are `DEPENDENCY` under the adoption taxonomy. This project's contribution
is which control they feed, not a better implementation of any of them.

---

## 3. Adapted source is the case the tooling misses

An installed dependency has a name, a version and an ecosystem watching it. A
file copied from another project and refactored has none of those, and is
therefore invisible to every scanner in the table above.

`ADR-004`'s register is what makes it visible, and this record binds it to
admission and to release:

- Admission requires the full `ADR-004` set — permissive licence read at the
  source, pinned commit, file list, SPDX header, `NOTICE` entry, characterisation
  suite — and a file arriving without them fails CI **before merge** (ACC-074,
  ACC-120).
- **Drift is monitored, never merged.** When upstream moves past a pin, the
  divergence is reported and a review item opens; the characterisation suite
  reruns and the pin moves through a recorded decision (ACC-073).
- **Unknown or incompatible licence means no copy.** The mechanism is specified
  and reimplemented instead, with a `MechanismSpec` and a clean lineage.

The register today holds 36 entries, all `PROPOSED`, all with `pinned_commit`
null — no code has been taken, and the checker begins demanding a pin the moment
any does.

---

## 4. What a release dossier carries

Signed artifacts with verifiable provenance; an SBOM and its scan result; the
Scorecard posture of what is depended on; the upstream register with every
adapted file accounted for; and the licence position stated per file rather than
per repository.

**A repository-level licence is not a per-file licence**, which is not pedantry —
it is the concrete reason the K-Dense domain-skill catalogue is `DEFER` in the
register rather than imported: MIT at the repository, and a per-skill `license`
field that is not uniform.

---

## 5. Consequences

**Accepted:** five more tools in the build, each with its own failure modes and
false positives, and a CI that takes longer.

**Accepted:** OSV and Scorecard will produce findings on dependencies with no
available fix. Those become recorded, owned, expiring residual risks — not
silence.

**Gained:** adapted source stops being a blind spot. It is the category most
likely to carry an unnoticed defect, because nothing else in the toolchain is
looking at it.

**Rejected:** a bespoke provenance or scanning implementation. It would be worse,
unmaintained, and would fail the register's own selection rule — maintained by
people closer to the problem.

---

## 6. Decision

**Accepted, 2026-08-23.** The toolchain is what WP-159 integrates and WP-059
admits against. **None of it is wired up.** `check_upstream_lineage.py` runs and
enforces `ADR-004`'s register rules; SPDX headers, REUSE conformance, OSV,
Scorecard, SLSA and Sigstore verification are all specified and absent.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-012`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
