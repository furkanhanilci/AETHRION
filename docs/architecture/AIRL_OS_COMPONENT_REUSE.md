# AIRL-OS — Mature Components to Build On

| Field | Value |
|---|---|
| Document type | Architecture reference — component adoption register |
| Scope | Existing, maintained implementations that make a gate **stronger** than a hand-rolled equivalent |
| Sibling documents | `AIRL_OS_EXTERNAL_STANDARDS.md` (formats) · `AIRL_OS_RELATED_SYSTEMS.md` (systems) |
| Status | §2 is **implemented and measured**; §3 is adopted and unbuilt; §4 is under evaluation |
| Date | 2026-08-22 |

**In one paragraph.** `AIRL_OS_EXTERNAL_STANDARDS.md` records which *formats* this
project adopts instead of inventing. This document records which *running
implementations* it should build on, and the reason is not to reduce scope — it
is that a gate backed by an implementation the scholarly community maintains and
tests is **stronger** than the same gate backed by something written here for the
first time. A citation check that queries Crossref is better than one that
queries a local heuristic, not cheaper.

---

## 1. The selection rule

A component is adopted when it makes a control **more likely to catch what the
control exists to catch**:

1. **Maintained by people closer to the problem** — Crossref knows about DOIs;
   this project never will.
2. **Already tested against reality** — a validated implementation of a
   statistical forensic test has survived cases nobody here would have imagined.
3. **Failure is legible** — when it is wrong, that is visible and attributable,
   rather than buried in bespoke code.
4. **Adoption does not import authority** — the component supplies a signal; what
   AIRL-OS *does* with the signal stays an AIRL-OS decision.

Rule 4 is why this register is separate from the gate policy. Crossref decides
whether a record exists. It does not decide whether a package is accepted.

---

## 2. Implemented — reference verification

| | |
|---|---|
| Component | **Crossref** · **OpenAlex** · **arXiv** APIs |
| Where | `scripts/verify_references.py` |
| Gate | G3 literature freeze · G9 publication conformance |
| Implements | CoE Audit check 1 (`AIRL_OS_EXTERNAL_STANDARDS.md` §4.3) |

### The first measurement this project has produced

Run against the **33 real sources** in the canonical registry:

| Authorities | Corroborated | Unresolved | Rate |
|---|---:|---:|---:|
| Crossref + OpenAlex | 25 / 33 | 8 | **75.8 %** |
| **+ arXiv** | **27 / 33** | 6 | **81.8 %** |

**Adding one authority moved the rate six points**, and the reason is the useful
part: every unresolved entry was a **DOI-less preprint**, which a
DOI-registration authority structurally cannot see. The first run did not reveal
bad sources; it revealed an inadequate check. That is what the measurement was
for.

The remaining 6 unresolved entries are **3 distinct titles**, each appearing 2–3
times — which independently corroborates the duplicate-detection dashboard the
bridge already produces.

> **What this number is not.** It measures whether records *exist* in public
> bibliographic authorities. It says nothing about whether a claim is supported
> by them, and an unresolved DOI-less item means *unindexed*, not *fabricated*.
> The published CoE Audit benchmark measured hallucinated references in
> **generated** bibliographies; this registry is human-curated, so the numbers
> are not comparable and must never be presented as if they were.

The registry is opened **read-only**. Verification observes; it never writes back
a "corrected" title and never removes a source it could not resolve.

---

## 3. Adopted, not yet built

| Capability | Component | Why it is stronger than building it here |
|---|---|---|
| **Evidence attestation** — the real WP-000 target | **`sigstore-python`** + the OpenSSF **`model-signing`** library | Keyless OIDC identity and a Rekor inclusion proof, which the current local-key interim profile explicitly lacks. This is the named upgrade path out of `airl-interim-v0.1` |
| **Statistical forensics** at G6-0 | **`statcheck`** (Python port of Nuijten's R package) · **`grim`** · **`pysprite`** | These tests have subtle edge cases — scale granularity, rounding, integer constraints. A fresh implementation would reproduce known bugs the published ones already fixed |
| **Screening at G3** | **ASReview** — active-learning screening, published in *Nature Machine Intelligence* | Pairs directly with the SAFE stopping rule already adopted; a hand-rolled screener would have neither the model nor the stopping evidence |
| **Run provenance** at G5/G7 | **`ro-crate-py`** with the Workflow Run Crate profile | Machine-actionable, engine-independent, re-execution aware, and mapped to W3C PROV — none of which a bespoke run manifest would be |
| **Agreement and calibration** in the metascience plane | **`krippendorff`** · `statsmodels` (Fleiss κ) · `scikit-learn` (Brier) | Standard estimators with known behaviour on missing data and small samples |
| **Claim publication** | **`nanopub-py`** | Publishes a claim as a FAIR nanopublication — assertion, provenance and publication info — which is the shape `ClaimVersion` already has |
| **Literature retrieval** at G3 | **PaperQA2** | A far more mature retrieval and evidence-gathering subsystem than this project will build. AIRL-OS's contribution is how retrieval binds to provenance and claim scope, not the retrieval itself |

---

## 4. Under evaluation

| Area | Note |
|---|---|
| Untrusted-content boundary (ACC-44, WP-136) | Guard libraries exist for prompt-injection screening; none has been evaluated here, and adopting one before evaluating it would contradict §1 rule 2 |
| Preregistration registries | An external, timestamped registry would strengthen G2b beyond a local hash. Not yet assessed |
| Retraction monitoring at G10 | Crossref carries retraction data; the ingest path is not designed |

---

## 5. What this changes about the plan

Nothing is deleted. Several packages become **thinner and stronger at the same
time**: their job stops being *implement this capability* and becomes *integrate
this component under our contract, and verify it behaves*. That integration work
is real, and the verification of it is the part AIRL-OS actually contributes.

| Package | Was | Becomes |
|---|---|---|
| WP-000 | build attestation | integrate `sigstore-python`, keep the interim profile as the fallback |
| WP-068-class screening | build a screener | integrate ASReview, own the stopping-rule evidence |
| WP-080 citation entailment | build reference checking | **done for the reference half**; the entailment half remains |
| WP-082 run registry | design a run record | emit Workflow Run Crate |
| WP-093-class metascience | implement estimators | use standard ones, own the calibration set |

---

## 6. Sources

- Crossref API · OpenAlex — <https://github.com/J535D165/pyalex> · arXiv API
- `sigstore-python` — <https://github.com/sigstore/sigstore-python> · `model-signing` — <https://github.com/sigstore/model-transparency>
- statcheck (Python) — <https://github.com/hplisiecki/statcheck_python> · `grim` — <https://pypi.org/project/grim/> · `pysprite` — <https://github.com/QuentinAndre/pysprite>
- ASReview — <https://github.com/asreview/asreview> · *Nature Machine Intelligence* — <https://www.nature.com/articles/s42256-020-00287-7>
- `ro-crate-py` — <https://github.com/ResearchObject/ro-crate-py> · `nanopub-py` — <https://github.com/fair-workflows/nanopub>
- `krippendorff` — <https://pypi.org/project/krippendorff/> · PaperQA2 — <https://github.com/Future-House/paper-qa>
