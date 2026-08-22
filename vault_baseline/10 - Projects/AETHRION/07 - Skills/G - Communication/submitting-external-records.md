---
title: "Submitting External Records"
aliases:
  - "submitting-external-records"
type: skill
category: skill
status: WORKING
source: "skills/submitting-external-records/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/submitting-external-records/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: submitting-external-records
description: "Use when a protocol or analysis plan must be externally timestamped, when artifacts need a persistent DOI, or when a publication package is being deposited"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G2,G9"
  airl.roles: "Data Steward,Research Software Engineer,Project Decision Owner"
  airl.assurance_classes: "R1,R2,R3"
  airl.emits: "ExternalRegistrationRecord,DOIRecord"
  airl.mechanical_checks: "human_approved_before_submission,data_class_ceiling_enforced,doi_recorded_in_manifest"
  airl.data_class_ceiling: "D1"
  airl.tool_effect: "T3"
---

# Submitting External Records

## Core principle

Your internal records verify themselves. **An external record is an independent
witness.**

The strongest form of preregistration discipline is one where the lock is
**outside your control and unalterable**.

## Iron law

> **EXTERNAL SUBMISSION IS IRREVERSIBLE — EACH ONE REQUIRES EXPLICIT HUMAN
> APPROVAL.**
>
> The agent prepares; the human submits.

## What goes where, and when

| Record | Target | Gate | Gain |
|---|---|---|---|
| Preregistration (protocol + analysis plan) | **OSF Registries** | **G2** | Timestamped, immutable record + persistent DOI |
| Code and environment | **Zenodo** / Software Heritage | G9 | Permanent archive + DOI |
| Dataset | Zenodo / domain repository | G9 | DOI + machine-readable dataset metadata |
| Publication package | Zenodo / institutional repository | G9 | RO-Crate + DOI |
| Author identity | **ORCID** | G9 | Persistent author identifier |
| Preprint | arXiv / bioRxiv | G9 | Visibility (**submission is not fully automatable**) |

> **Verification note:** OSF registrations are timestamped, immutable and
> DOI-bearing; the programmatic submission path must be verified before
> implementation. arXiv submission requires a human step and cannot be fully
> automated.

## Why external preregistration at G2

Your internal `AnalysisPlanManifest` hash lives in your own system. An external
record is evidence **to someone who does not trust your system** — which is the
only kind of evidence that matters to an outside reader. This is the external
anchor for in-principle acceptance.

For sensitive work, OSF supports **embargo**: the registration is timestamped
but remains private for a defined period. Timestamp and disclosure are separable.

## Before submitting

- [ ] Human approval received (**exact word**: `SUBMIT`)
- [ ] Data class ≤ D1
- [ ] DLP scan passed
- [ ] Licence and citation metadata complete (`CITATION.cff`, `CodeMeta`)
- [ ] Embargo decision made
- [ ] Irreversibility acknowledged

## Afterwards

The returned DOI is written **into the manifest and the `EvidenceManifest`**.
An unrecorded DOI sits outside the evidence chain and is therefore useless — it
proves something exists but nothing links to it.

## Rationalization table

| Justification | Ruling |
|---|---|
| "We can fix it later" | **An external record is irreversible.** A correction is a new version, not a deletion. |
| "Submit now, decide the embargo later" | The embargo is chosen at submission time. |
| "The internal hash is enough" | The internal hash requires trusting your system. |
| "It's just a draft" | A draft submitted externally is a submitted record. |

## Red flags

- An external submission triggered by an agent
- A DOI returned but not written to the manifest
- D2+ content in an external record
