---
title: "Tests"
cssclasses:
  - aethrion-index
type: index
category: implementation
status: WORKING
summary: "172 tests cover the components that exist: the bridge's database, projection, API and MCP boundary, the shared contract core, and the evidence attestation tooling."
source: "tests/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/execution
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `tests/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Tests

| Field | Value |
|---|---|
| Document type | Index — what is tested, and what is deliberately not |
| Scope | The 172 tests that run today |
| Sibling documents | `../scripts/README.md` · `../docs/OPERATIONS.md` |
| Status | `WORKING` — 172 passing; coverage is narrow and honestly so |
| Date | 2026-08-23 |

**In one paragraph.** 172 tests cover the components that exist: the
bridge's database, projection, API and MCP boundary, the shared contract core,
and the evidence attestation tooling. They do not cover the target architecture,
because it is not built, and they do not cover agent behaviour, because no
behaviour-testing runtime exists. A green suite here means the implemented slice
behaves; it does not mean the framework works.

| File | Covers | Notable property |
|---|---|---|
| `test_database.py` | canonical registry, idempotent upsert, stable identity | re-running a sync must not duplicate a source, and an `unchanged` record is not written — the counter and the disk must agree |
| `test_obsidian.py` | projection writing, manifest-owned deletion, path containment | the projector deletes only files it recorded creating, records everything it writes, and refuses to run on a manifest it cannot read |
| `test_api.py` | the `GET` half of the FastAPI surface | **no defensive path is covered here** — see below |
| `test_mcp_server.py` | the MCP tool set | asserts **exactly five** read-only tools |
| `test_contracts.py` | identity, manifest, event envelope, schema registry | rejects malformed digests and duplicate schema registration |
| `test_skill_baseline.py` | that the right skill can be **reached**, and that the unmeasured half says so | "skills conform to a format; none has a behaviour baseline" was two claims wearing one sentence. Seventeen of 52 were reachable by no chain of references at all — including one half of a pair `ADR-012` says must never be substituted, while the other half sat in the router table. The last two tests here check that the execution corpus is reported as **unrun** rather than passing |
| `test_service_divergence.py` | what a sync reports when half of it works | there is no transaction spanning SQLite and a directory of Markdown files, so the two halves cannot be made atomic. What can be made true is that a caller is never handed a result that looks like both succeeded — plus the negative control that a healthy sync records no divergence |
| `test_mirrors.py` | the Obsidian mirrors | a mirror writes what changed and **preserves the inode** of everything else — a running editor watches inodes, and a tree that is deleted and recreated breaks every watch it holds | It also refuses to write over a page whose frontmatter says `generated: false`, because a projection may replace its own pages and nobody else's.
| `test_evidence_manifest.py` | issuing and verifying attestations | **the tamper cases are the point**: an altered payload, an altered covered file and a forged signature each fail |
| `test_zotero.py` | source identity, **the read-only boundary**, and pagination | the boundary is the framework's strongest security claim and was asserted by a hard-coded constant, so the artifacts verifying it tested `False is False`. A transport now **raises** on any non-`GET` through the whole ingest — and a test proves that transport can raise, because a control nobody has watched refuse is not evidence |
| `test_progress_cli.py` | the execution loop's refusals | the ledger is a ledger, not a file anyone can type into: an unmet dependency, an unverified manifest and an R3 acceptance are each refused, and the refusal names the document that forbids it |
| `test_stale_claim_checker.py` | the checker that catches stale prose | it plants the two defects an external review found in a corpus whose status page reported none — a checker narrower than the sentence it prints is the failure this test stops recurring |
| `test_upstream_lineage.py` | the assimilation register and its checker | **every rule must be demonstrable in both directions**: the committed register passes, and each ADR-004 obligation — pin, characterisation suite, no source files on a reimplementation, a stated authority boundary — can be made to fail on demand |
| `test_architectural_regressions.py` | the eight wordings that contradict a decision record | the hard half is **suppression**, not detection: every one of those phrases already appears here inside a sentence that forbids it, so each rule carries a specimen that must trip it *and* a specimen that must not, and the two guards are pinned to the false positives that produced them |
| `test_programme_graph.py` | that the plan can actually be executed | a dependency graph can be perfectly acyclic and still impossible to start; these hold the four historical defects as fixtures — a pre-go-live package needing Day-2 work, the benchmark firewall depending on the regression that aggregates it, an aggregate selector deleted along with the check that guarded it, and a WP↔ACC binding with two owners |
| `test_acquisition_binding.py` | that an adoption decision reaches the package that has to execute it | the registers decided what to adopt, copy and reimplement, and nothing joined those decisions to the work: AIDE was a registered `DIRECT_ADAPT` source for WP-144's candidate state machine and WP-144 never named it, while WP-041 was titled after a component no register knew. Both directions are held shut here, together with the two ways the fix rots — an obligation quietly treated as met, and a package reaching `READY` with one still open |
| `test_figure_and_hygiene_checks.py` | that a figure's claims match the repository, and that governed documents are well-formed | **a deterministic generator reproduces a false claim exactly as faithfully as a true one** — one figure said "141 work-package documents" against a registry of 160, another said "221 planning files" against a seal of 631, and both regenerated byte-identically for two baselines |

## What is not tested

- **Agent behaviour.** No skill has a baseline test; the runtime for one does not
  exist. **This is the largest untested claim in the repository** — and since the
  bridge findings closed, it is also the only structural gap left in this list.
- **The live Zotero API's actual pagination semantics.** `test_zotero.py` drives
  a `MockTransport` shaped like the documented behaviour. That proves the client
  handles what the documentation describes; it does not prove Zotero does it.
- **Everything designed and unbuilt** — Temporal, the ledgers, the brokers, the
  gates.

```bash
uv run pytest          # all 172
uv run pytest -k mcp   # one area
```
