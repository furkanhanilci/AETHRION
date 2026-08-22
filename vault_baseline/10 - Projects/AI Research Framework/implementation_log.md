---
airl_id: AI-RESEARCH-FRAMEWORK-IMPLEMENTATION-LOG
type: execution-log
status: active
owner: otonom
updated_at: "2026-08-22"
tags:
  - ai-framework/execution
  - ai-framework/contracts
  - ai-framework/foundation
---

# AI Research Framework — Implementation Log

Every material implementation step is recorded here. Each entry separates **what
was observed** (evidence) from **what was concluded** (interpretation), states
its **limits**, and names the **exact next step**. Before starting a new step,
the last entry, the cockpit and the relevant WP files are read again.

---

## Step 014 — The adoption matrix applied, and a second measurement

**Time:** 2026-08-22
**Scope:** component adoption taxonomy and matrix · G10 monitoring implemented ·
plan updated to adopt · ADR-003 · two reporting skills · fourth figure

### The principle this step settles

> **AIRL-OS should not invent its own parser, screening engine, policy language,
> sandbox, experiment tracker or scholarly identifier.** Its contribution is the
> layer above them: which evidence, having passed which gate, permits which claim
> to be accepted.

And the framing correction that came with it: **the point is not to shrink the
surface, it is to strengthen it.** A gate backed by a component its community
maintains and tests is stronger than the same gate backed by first-attempt code.

### Implemented: G10 monitoring, with a control that must fire

`scripts/monitor_sources.py` sweeps the registry against Crossref, which now
carries Retraction Watch data and exposes it as `update-to` / `updated-by`.

| Measure | Value |
|---|---:|
| Sources swept | **15** of 33 |
| **Invisible — no DOI** | **18** |
| Material signals | 0 |
| **Positive control** | **FIRED** |

**A clean report proves nothing unless the check can fire**, so every run
includes a known-retracted DOI and the script **exits non-zero if that control
stays silent**. This is the metascience plane's control-injection principle
applied at the smallest possible scale — the difference between "no retractions"
and "no detector".

And like the reference check before it, the measurement exposed its own
boundary: **18 of 33 sources carry no DOI and are invisible to the sweep.** A
clean report over a DOI-less registry would be a false reassurance, and the
report says so on its face.

Claim impact analysis is **not** implemented — nothing maps a retracted source to
dependent claims, because no Claim Ledger exists. G10's loop is opened, not
closed.

### The adoption taxonomy

"Reuse" was being used for six different things, which produces bad decisions —
importing a dependency where a pattern was needed, or reimplementing a pattern as
if it were a library. The register now types every entry:

`DEPENDENCY` · `ADAPTER` · `STANDARD` · `BENCHMARK` · `PATTERN` ·
`OPTIONAL BACKEND` · `REJECTED`

**A BENCHMARK can never become a gate.** That distinction is the reason the
taxonomy exists.

### What was adopted, and what it changes

| Component | Type | Changes |
|---|---|---|
| **Inspect AI** | DEPENDENCY | WP-043 stops being *build an evaluation engine* and becomes *encode behaviours as tasks and scorers*; WP-048 drives real harnesses through its agent bridge |
| **GROBID + Pub2TEI** | DEPENDENCY | One canonical TEI representation, so an `EvidenceSpan` addresses `tei_xpath` with a `representation_digest` — and a later parser produces v2 **without invalidating claims anchored to v1** |
| **Cedar** | DEPENDENCY | WP-049 integrates a policy engine with a formal semantics instead of writing conditionals; OPA is the recorded alternative behind a bake-off |
| **CaMeL** | PATTERN | WP-136 stops being *injection detection* and becomes *trusted control / untrusted data* |
| **OSF Registries** | DEPENDENCY | G2/G2b gains an external timestamped witness; required at R2 confirmatory and above |
| **Workflow Run RO-Crate** | STANDARD | Priority raised: adopt **before** the first slice, so the run format is never forked |
| **SEPIO + LinkML** | STANDARD | Promoted out of the deferred queue. Generates the contract surface from one model — which attacks the digest-format disagreement at its root |
| **Croissant 1.1 · SWHID ISO/IEC 18670** | STANDARD | Dataset records and software identity |
| **MLflow + OpenTelemetry** | DEPENDENCY | Observability — **never the scientific truth store** |
| **Object-lock WORM · lakeFS** | OPTIONAL BACKEND | WP-026 becomes *integrate and verify*, not *build* |
| **PaperBench** | PATTERN + BENCHMARK | Its three-container separation is the working demonstration of producer / reproducer / reviewer |
| **ResearchClawBench** | BENCHMARK | Makes the central claim testable — see below |
| Detector libraries as a boundary | **REJECTED** | A detector is defence in depth; the boundary is structural |

Ten work packages now carry an **Adopted component** section stating what they
stand on and what that changes.

### ADR-003 — trusted control, untrusted data, policy

Decided: control flow comes only from trusted intent; untrusted content may
supply values but can never create actions or expand permissions; policy is
evaluated by Cedar; **any policy-evaluation anomaly denies**. The CaMeL result is
recorded as **67–77 % of AgentDojo tasks under provable security depending on
paper version** — the discrepancy kept rather than rounded to the flattering
figure.

Measured against **someone else's** attack suite, deliberately: a system
evaluated only against attacks it imagined is measuring its imagination.

### Two skills: reporting and figures

- **`reporting-results`** — iron law: *no sentence that does not resolve to a
  claim, and no claim stated more broadly than its evidence*. Binds the EQUATOR
  guideline family to study type, and records that a guideline is a completeness
  standard, not a quality one.
- **`producing-figures`** — a figure is a claim in visual form. Semantic model
  before layout, archetype from structure rather than habit, exact-text
  allowlist, colour never the only channel, final-size measured, and: **a figure
  of a designed system states that it is designed.**

51 skills.

### The experiment this makes possible

ResearchClawBench holds model, tools, budget and task fixed and varies only the
governance layer. That is the paper worth writing — *does research governance
improve autonomous research integrity, and at what cost?* — and the honest
expectation is that governance costs runtime and may not raise the score.
**Both outcomes are publishable; only one is flattering.**

### Evidence

- `monitor_sources.py` → 15 swept, 0 material, **control fired**; report recorded
- `verify_references.py` → 27/33 corroborated
- 25/25 tests · 51/51 skills · plan semantics OK · documents consistent
- **4/4 figures**, 0 overflow · seal 207/207 · mirror drift 0

A checker bug was fixed along the way: `check_figures.py` measured XML-escaped
text, counting `&#x27;` as six characters and reporting an overflow that did not
exist. It now unescapes before measuring.

### Limits

- Every adoption in the matrix except the three Crossref-family checks is a
  **decision, not a component that runs**.
- The control layer this project owns is the least built part of the stack, and
  the fourth figure says so.
- No end-to-end run. No CoE Audit score beyond check 1. BVC-01 still staged.

### Next step

Activate BVC-01, sign WP-000's acceptance, then the first end-to-end slice —
built on adopted components from the start rather than retrofitted onto
first-attempt code.

---

## Step 013 — Building on mature components, and the first measurement

**Time:** 2026-08-22
**Scope:** component adoption register · reference verification implemented and
run against the real registry

### The framing that matters

The point of adopting an existing implementation here is **not** to reduce scope.
It is that a gate backed by something the scholarly community maintains and tests
is **stronger** than the same gate backed by code written here for the first
time. A citation check that queries Crossref is better than one that queries a
local heuristic — not cheaper.

### What was implemented

`scripts/verify_references.py` — CoE Audit check 1, resolving every source in the
canonical registry against **Crossref**, **OpenAlex** and **arXiv**.

This is the first thing in the repository that produces an **empirical number
about itself**, which was the sharpest gap in the last external review.

### The measurement, and what it actually taught

| Authorities | Corroborated | Rate |
|---|---:|---:|
| Crossref + OpenAlex | 25 / 33 | 75.8 % |
| **+ arXiv** | **27 / 33** | **81.8 %** |

The first run scored 75.8 %, and the instructive part was *why*: **every
unresolved entry was a DOI-less preprint**, which a DOI-registration authority
structurally cannot see. Adding one authority moved the rate six points.

**The measurement did not find bad sources. It found an inadequate check.** That
is what measuring is for, and it is the first time this project has been
corrected by evidence rather than by review.

A second finding fell out of it: the 6 remaining unresolved entries are only **3
distinct titles**, each appearing 2–3 times — independent corroboration of the
duplicate-detection dashboard the bridge already produces.

### What the number is not

It measures whether records **exist** in public bibliographic authorities. It
says nothing about whether a claim is supported by them, and an unresolved
DOI-less item means *unindexed*, not *fabricated*. The published CoE Audit
benchmark measured hallucinated references in **generated** bibliographies; this
registry is human-curated, so the numbers are **not comparable** and are recorded
as not comparable.

The registry is opened read-only. Verification observes; it never writes back a
corrected title and never removes a source it failed to resolve.

### The adoption register

`AIRL_OS_COMPONENT_REUSE.md` records which running implementations each control
should be built on, with a selection rule whose fourth clause is the important
one: **adoption supplies a signal, never authority.** Crossref decides whether a
record exists; it does not decide whether a package is accepted.

Adopted and not yet built: **`sigstore-python`** and OpenSSF **`model-signing`**
(the named upgrade path out of the `airl-interim-v0.1` local-key profile),
**statcheck / grim / pysprite** for G6-0, **ASReview** for screening,
**`ro-crate-py`** with the Workflow Run Crate profile for run provenance,
**`krippendorff`** and standard estimators for the metascience plane,
**`nanopub-py`** for claim publication, and **PaperQA2** for retrieval at G3.

Nothing in the plan is deleted. Several packages become thinner and stronger at
once: their job stops being *implement this capability* and becomes *integrate
this component under our contract, and verify it behaves* — and verifying it is
the part AIRL-OS actually contributes.

### Evidence

- `verify_references.py` → **27/33, 81.8 %**, report at
  `delivery/measurements/reference_verification.json`
- 25/25 tests · skills 49/49 · plan semantics OK · documents consistent
- Figures 3/3, 0 overflow · seal 207/207 · mirror drift 0

### Limits

- One of four CoE Audit checks is implemented. The other three need artifacts
  this system does not produce.
- The check needs network, so it is **not** part of BVC-01 and stays manual,
  like the Bridge-dependent checks.
- Every component in §3 of the register is adopted on paper and built nowhere.
- This step added capability and a measurement. It did not produce an end-to-end
  run, which remains the gap.

### Next step

Unchanged in shape, better supported: activate BVC-01, sign WP-000's acceptance,
then the first end-to-end slice — which now has a real check waiting for it at
G3, and three more to implement.

---

## Step 012 — External positioning, and a guard against the drift that keeps recurring

**Time:** 2026-08-22
**Scope:** independent review response — document drift made mechanically
impossible · Science One positioning · CoE Audit adopted · terminology · licence

### The review, and what it found that mattered

An external reviewer assessed the repository from scratch, using no prior
context. The verdict: **strong research-system architecture, small genuine
working slice, very large implementation gap** — which matches this log. Two
findings were worth more than the verdict.

### Finding 1 — the drift is recurring, so the fix is not a fix

Two documents disagreed with reality:

- `planning/commissioning/README.md` said **46** acceptance scenarios while 51
  existed. The cause is instructive: an earlier edit corrected the *range* to
  `ACC-01 – ACC-51`, which broke the exact-match string the *count* edit depended
  on. The count silently stayed behind.
- `ADR-001`'s summary still said the record "leaves the decision field blank"
  after the decision had been taken and its status set to `ACCEPTED`.

Both violate `DOCUMENT_STANDARD.md` §3 rule 2 — *counts are derived, not
remembered* — which this repository wrote and then broke twice.

**So the rule now has a check.** `scripts/check_doc_consistency.py` derives the
truth from the repository and compares it against every count a document states,
and it fails a decision record whose status says `ACCEPTED` while its body still
describes the decision as open. It found both defects on its first run, and a
deliberately injected drift confirmed it fails when it should.

### Finding 2 — Chain-of-Evidence is not ours

Google Research published **Science One / ScientistOne** in mid-2026 around
exactly the principle this architecture is built on: every claim traceable to its
evidence source. Its **CoE Audit** measured four integrity checks across **75
papers and five systems**, finding hallucinated-reference rates up to **21 %**,
score verification passing in as few as **42 %** of papers, and method–code
alignment between **20 % and 80 %** — while reporting **0/337** hallucinated
references for itself.

That is external evidence for the claim this repository has only asserted:
**retrofitted verification does not work.** They demonstrated it; AIRL-OS argued
it.

`AIRL_OS_RELATED_SYSTEMS.md` now states the overlap plainly, names where those
systems are ahead without qualification — end-to-end runs, measurement, an
empirical outcome, a far more mature literature subsystem — and positions AIRL-OS
by **scope** rather than by novelty: Science One asks whether an autonomous system
can produce verifiable papers; AIRL-OS asks under what governance a claim may be
believed at all.

### CoE Audit adopted as the external benchmark

The four checks — reference verification, score verification, specification
violation, method–code alignment — are adopted verbatim into G6-0 and G9. They
are concrete, published, and measure exactly what this framework claims to
enforce.

**Adopting a benchmark means agreeing to be measured by it.** AIRL-OS has no
score on any of the four, because it has produced nothing to audit. The first
end-to-end slice goes through CoE Audit, and the result is recorded whatever it
says.

### Terminology — the distinction that was about to be blurred

The reviewer flagged that an outside reader seeing *"R2 independently verified"*
would assume two people. ADR-001 §6.2 now separates three terms and binds R1/R2
to the honest one:

| Term | Permitted for |
|---|---|
| **Independent verification** — a different human or institution | R3 only, and only when named |
| **Internally separated verification** — same operator, separated context, environment, model family, time | R1 and R2 |
| **Cross-model corroboration** | a component of internal separation, never a substitute |

### Licence positioning

The README now answers the fair question rather than leaving it implicit: the
architecture is meant to be read and reused; the implementation is one person's
research infrastructure. **If this ever becomes something a community builds on,
the licence has to change first** — a proprietary framework cannot credibly ask
for the interoperability it preaches.

### Evidence

- `check_doc_consistency.py` → documents agree with the repository and with
  themselves; drift injection correctly fails
- 25/25 tests · plan semantics OK · seal 207/207 · skills 49/49 · figures 3/3
- Mirror drift 0 (208 plan, 68 skill/doc/figure)

### Limits

- The reviewer's central point stands and is not addressed by this step: **the
  gap is specification → executable mechanism → empirical evidence**, and nothing
  here closes it. This step improved honesty and added a guard; it added no
  capability.
- No CoE Audit score exists. No end-to-end run exists.
- BVC-01 is still staged, not active.

### Next step

Unchanged: activate BVC-01, sign WP-000's acceptance, then WP-001 — and after
that, **stop specifying**. The next thing worth building is one end-to-end
vertical slice thin enough to finish, run through CoE Audit.

---

## Step 011 — The first working version: decisions taken, evidence actually issued

**Time:** 2026-08-22
**Scope:** ADR-001 and ADR-002 decided · BVC-01 implemented · WP-000 executed

### What changed in kind, not degree

Every previous step produced specification. This one produced **a verifiable
artifact and a decided acceptance path** — the first time the framework applied
its own rules to itself. The third piece, automated verification, is written but
blocked on a credential and is recorded as blocked rather than as done.

### ADR-001 decided — C2 is no longer open

**Model A + C adopted, Model B available when an external verifier can be named:**

| Class | Acceptance | Conditions |
|---|---|---|
| **R1** | solo permitted | mechanical checks pass; the profile records which dimensions held |
| **R2** | solo permitted | cross-family review · clean-room reproduction · declared temporal separation · manifest states human identity and economic interest were **not** independent |
| **R3** | **`BLOCKED`** | only an externally named human verifier lifts it |

The reasoning is that five of seven independence dimensions survive a one-person
operation and can be enforced mechanically, while the two that do not — human
identity and economic interest — are precisely the two that matter most at R3.
So R3 is blocked rather than approximated. **Packages now have an acceptance
path, and the laboratory does not claim independence it does not have.**

### ADR-002 decided — BVC-01 written, staged, **not yet active**

`deploy/bvc-01-verify.yml` defines a push-triggered run of pytest, the skill
registry contract, the plan semantics validator, the plan seal and the figure
checks.

It sits in `deploy/` rather than `.github/workflows/` because the token
available here lacks GitHub's `workflow` scope and the push is refused. That is
a credential boundary, not a design choice — but it means **the control is not
running**, and saying otherwise would have been the exact overstatement this
step is otherwise about avoiding. Activation is one command plus one commit,
recorded in ADR-002 §6.

It is **not** WP-024 and does not pretend to be: schema validation, policy
bundles, security scanning, provenance attestation and integration testing belong
to that package, which hard-depends on three unbuilt ones. BVC-01 carries an
owner, an expiry (WP-024 acceptance or 2027-02-22) and a named retirement
package, and its final step **prints what it does not cover** rather than hiding
it. **It does not close H5.**

### WP-000 executed — the first real evidence

`scripts/evidence_manifest.py` issues and verifies `EvidenceManifest`
attestations: an in-toto Statement, a DSSE envelope, an Ed25519 signature, and
WP-000's **own** interim time anchor — not WP-139's, deliberately.

```
signature           OK
subject digest      OK   README.md
subject digest      OK   planning/commissioning/00_PROGRAM/SHA256SUMS.txt
subject digest      OK   planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md
time anchor         OK   (interim/local)
payload altered     rejected, as required
```

Five tests exercise the claim rather than asserting it: a good manifest verifies,
an altered payload is rejected, **an altered covered file fails the digest
check**, a forged signature fails the envelope check, and the manifest declares
its own limitations. Verification exits `1` in every failure case.

**The implemented profile is narrower than the target, and the manifest says so
on its face.** `attestation_profile: airl-interim-v0.1`: local Ed25519 key
instead of Sigstore keyless, and **no transparency-log submission** — keyless
signing needs an interactive OIDC flow this environment does not have. Claiming
a Rekor entry that does not exist would have been precisely the overstatement
this repository exists to prevent, so every manifest carries a `limitations`
list and verification prints what is not covered.

An operational property fell out of building it: **a manifest is issued last.**
It covers digests, so changing a covered file afterwards fails verification —
which is the control working. This was observed during this step, when a README
edit after issuance broke the specimen; it is now documented in
`delivery/README.md`.

### Evidence

- `pytest` → **25 passed** (20 + 5 attestation tests)
- BVC-01 → written, **not active**; the checks still run only when someone remembers
- Plan seal **207/207** · plan semantics **OK, 0 defects**
- Skills 49/49 · figures 3/3, 0 overflow
- WP-000 attestation verifies; both tamper paths rejected
- Mirror drift **0** (208 plan, 67 skill/doc/figure)

### Limits

- **WP-000 is `TECH_COMPLETE`, not `ACCEPTED`.** Issuance is not acceptance; the
  manifest records `verifier.decision: PENDING`. Under ADR-001 an R1 acceptance
  is now permitted, and that signature is the Project Decision Owner's to give.
- The transparency log and keyless identity remain unimplemented. That is the
  remaining work in WP-000, not a detail.
- The interim anchor binds to the issuer's clock and a commit hash. It is weaker
  than a timestamp authority and says so in every manifest.
- 51 acceptance scenarios still have never been run. No skill has a behaviour
  baseline. The Bridge is still the only working vertical slice.

### Next step

WP-001. The programme now has what it never had: a defined acceptance path
(ADR-001), a working evidence mechanism (WP-000), and verification that runs
without being remembered (BVC-01).

---

## Step 010 — Commissioning baseline v1.0.1: the defects the seal could not see

**Time:** 2026-08-22
**Scope:** pre-commissioning readiness review response — semantic plan defects,
a plan validator, two decision records, and licensing

### The finding behind this step

A pre-commissioning readiness review gave **architecture freeze: GO**, and
**commissioning baseline v1.0 as-is: NO-GO**. The reason was not weak design. It
was that three defects survived the freeze which the hash seal is structurally
incapable of detecting, because **every file involved was byte-identical to its
sealed state**. The seal proves files did not change. It says nothing about
whether they agree with each other.

### Defect 1 — acceptance identifiers collided (Critical)

`13_TOOLING_INTEGRATION` packages already referenced ACC-41 – ACC-45. Those
scenarios had never been written, so the references dangled. Baseline v1.0 then
added six **skill** scenarios at exactly those numbers, and the dangling
references silently resolved to the wrong subject: **WP-136 inbound content
quarantine now claimed to be tested by "Skill Ignored Under Pressure".**

Corrected by renumbering the skill scenarios to **ACC-46 – ACC-51** and writing
the five scenarios the tooling packages had been referencing all along:
notification data-class ceiling · broker outage · escalation and dead-man's
switch · inbound content is not an instruction · irreversible external
submission. **51 scenarios.**

### Defect 2 — go-live required post-go-live work (Critical)

```
WP-120 cutover  requires  all acceptance scenarios PASS
                          ⇓ includes ACC-36, ACC-38, ACC-27, ACC-29, ACC-07, ACC-37
                          ⇓ which referenced WP-124 / WP-126 / WP-127 / WP-129
                          ⇓ which hard-depend on WP-121 programme closure
                          ⇓ which happens after WP-120
```

A cycle: **to go live you had to finish work that only exists after going live.**

Corrected with an `Acceptance phase` field on every scenario. The initial
qualification is `PRE_GO_LIVE` and owned by a commissioning package; the
recurring rhythm stays in Day-2 and is named in the scenario's `Recurring
counterpart` field. Day-2 packages no longer claim a go-live scenario tests them.

### Defect 3 — stale ranges and a duplicated field

`ACC-01–ACC-40` survived in WP-115 and WP-120 while their acceptance criteria
demanded 46; the go-live checklist attributed independence measurement to
WP-132 (a channel registry); and it required *"a time-boxed, non-waivable
residual risk accepted"*, which is a contradiction in terms. WP-013 had gained a
duplicate `Related acceptance scenarios` row. All corrected.

### The real deliverable: `validate_commissioning_plan.py`

Fixing three defects is worth less than making the class of defect detectable, so
the plan now has a semantic validator alongside its seal. It checks identifier
existence, **bidirectional** WP↔ACC consistency, dependency-graph acyclicity,
acceptance-phase validity, **go-live feasibility**, stale ranges, index parity
and catalogue/matrix parity.

Its first run found the three known defects **plus 137 one-directional
references** nobody had noticed — packages claiming a scenario tested them while
the scenario listed different packages. Closed mechanically across 43 scenarios.

It also caught a mistake made *during* this step: closing the references
bidirectionally re-introduced the Day-2 cycle, because the Day-2 packages'
own claims pulled it back. The validator failed the build, and the fix was to
rename the relationship rather than delete it.

**From now on the plan is valid only when both pass:** `207/207` seal **and**
`plan semantics OK`.

### Two decisions written, neither taken

- **ADR-001 — Solo-Operator Independence.** The C2 deadlock, three models, and a
  recommendation: R1 solo; R2 solo only with cross-family review, clean-room
  reproduction and declared temporal separation, with partial independence stated
  in the manifest; **R3 `BLOCKED` unless an external verifier is named**. Five of
  the seven independence dimensions survive a one-person operation; human identity
  and economic interest do not. **The decision field is blank — a framework cannot
  grant itself independence.**
- **ADR-002 — Bootstrap Verification Control.** WP-024 hard-depends on three
  unbuilt packages, so CI cannot legitimately be "stood up" yet. `BVC-01` runs the
  automatable half of the bundle on push, as a temporary control with an owner, an
  expiry and WP-024 as its named retirement package. It explicitly does **not**
  close H5.

### Licensing

`NOTICE` added: AIRL-OS proprietary, all rights reserved; the eleven vendored
skills MIT with attribution and a pinned commit; conformance to public
specifications is not a licence claim.

### Evidence

- `validate_commissioning_plan.py` → **141 packages · 51 scenarios · 0 defects · 0 warnings**
- Plan seal regenerated → **207/207**
- `pytest` 20 passed · skills 49/49 · figures 3/3, 0 overflow
- Mirror drift **0** (208 plan, 67 skill/doc/figure)

### Limits

- **C2 is still open**, so nothing may be marked `ACCEPTED`. That is the finding
  working, not a blocker to route around.
- BVC-01 is written, not implemented. No CI runs today.
- 51 scenarios are written and **none has ever been run**.
- The validator checks the plan's internal consistency. It cannot check whether
  the plan is a good plan.

### Next step

Decide ADR-001. Then implement BVC-01, then execute WP-000 — issue one specimen
`EvidenceManifest`, sign it, log it, anchor it with **WP-000's own** interim
anchor, and demonstrate that a tampered copy fails verification.

---

## Step 009 — Figures that cannot overflow, and a document standard

**Time:** 2026-08-22
**Scope:** figure layout correctness · a written document standard applied to the
corpus entry points

### The defect

The figures shipped in Step 008 had labels that overflowed their boxes. The check
in place compared text against the **canvas**, so a string that spilled out of a
node but stayed on the page passed. **The wrong invariant was being verified** —
which is precisely the failure mode this framework is built to catch, appearing
in the framework's own tooling.

### The fix, in two independent layers

1. **`figure_kit` now measures text.** It carries the Helvetica advance-width
   table with a 3 % safety margin, so `text_width` is a measurement rather than a
   character count. `Canvas.cell` fits every string against the box's **inner**
   width: wrap first, then shrink toward the 16-unit floor, and **raise** if it
   still will not fit. A figure that cannot be laid out honestly now fails the
   build. It did fail, three times, during this step — each failure was a real
   overflow that would otherwise have shipped.
2. **`scripts/check_figures.py` re-measures the rendered SVG.** It finds the
   tightest box enclosing each text anchor and reports anything that escapes it.
   It deliberately does not trust the generator, so one bad assumption cannot
   hide behind itself twice. It caught both remaining overflows immediately.

`make_figures.py` runs generation and containment together, so they cannot drift
apart, and the check is now part of the verification bundle.

### Document standard

`docs/DOCUMENT_STANDARD.md` — required structure (front-matter table, a
one-paragraph summary, numbered sections, a closing question→file table), a
controlled **status vocabulary** (`WORKING`, `TECH_COMPLETE`, `ACCEPTED`,
`SPECIFIED`, `PROPOSAL`, `DESIGNED`), formatting conventions, and five honesty
rules:

- distance from working software is stated, never implied — diagrams included
- counts are re-derived when a document is touched, never remembered
- decision records stay in the past tense; documents rewritten to match the
  present stop being records
- evidence is never edited; current state goes in a new dated document
- a limitations section is mandatory in any document describing a component

Applied to every entry point: `README`, `OPERATIONS`, `ARCHITECTURE_V0`,
`FOUNDATION`, `skills/README`, `docs/figures/README`, all six architecture
documents and the verification report. **The frozen 2026-08-21 audit was left
untouched** under rule 4.

### Evidence

- `python3 scripts/check_figures.py` → **3 figures, 0 overflows**
- `make_figures.py --check` → 3 figures, 0 drift
- `uv run pytest` → 20 passed · `validate_skills.py` → 49 conform
- Plan seal **202/202** · mirror drift **0** (203 plan, 65 skill/doc/figure)

### Limits

- The containment check verifies *geometry*, not *design*. It cannot tell whether
  a figure communicates; it only guarantees nothing is clipped.
- The document standard is enforced by review except for the four mechanical
  checks listed in its §5. That is a limitation, not a plan.
- Nothing about the framework's capability changed. Again.

### Next step

Unchanged and now three steps overdue: **issue one signed specimen
`EvidenceManifest` under WP-000**, then CI — which now has seven checks waiting.

---

## Step 008 — The role layer, and figures that are generated rather than drawn

**Time:** 2026-08-22
**Scope:** role definitions and authority flows · three publication figures ·
a figure generator and its drift check

### Why figures, and why only three

The instruction was to add visualisations to every document. Applied literally
that produces exactly what a scientific-figure discipline forbids: a generic
box diagram on 141 work packages, each of which would pass the test a figure
must **fail** — *"could this be reused for an unrelated project by changing the
labels?"*

So the figure inventory was derived instead of assumed. A figure exists only
where it carries a **mechanism prose carries badly**, which produced three:

| Figure | Mechanism | Why prose fails |
|---|---|---|
| `airl_os_lifecycle.svg` | eleven gates × three actor classes, and the cells admitting no model | a table hides the pattern |
| `airl_os_roles.svg` | authority tiers and constraint resolution replacing headcount | a list reads as an org chart |
| `airl_os_evidence_chain.svg` | the chain, plus how much of it exists | a status table is never cross-read |

Everything else keeps inline Mermaid, which is editable in place and renders in
both GitHub and Obsidian without a build step.

### Figures are generated artifacts

`scripts/figure_kit.py` is a dependency-free SVG layer; `fig_lifecycle.py`,
`fig_roles.py` and `fig_evidence.py` are the three generators;
`scripts/make_figures.py --check` reports drift and is now the sixth item in the
verification bundle. **Hand-editing an SVG is a defect** — the same rule the
vault mirrors run under. No new runtime dependency was added: matplotlib and a
rasteriser would both have been heavier than the problem.

### Design constraints that were actually enforced

- **Colour never encodes status.** Status is stroke pattern plus an explicit
  label, so the figures survive greyscale and colour-vision deficiency. Position
  carries actor class, which is the primary channel.
- **Final-size legibility was measured, not assumed.** The first pass had 14-unit
  text — 6.0 pt at a 180 mm double column, below the floor most publishers
  accept. Raised to a 16-unit minimum (≈6.8 pt), then every string was
  re-measured for overflow; four real overflows were found and fixed.
- **Exact-text control.** Every visible string comes from the corpus. The
  generators invent no module names, metrics or relationships.
- **Honesty encoding.** Figure 1 carries a status line, Figure 2 names the open
  C2 decision, Figure 3 draws nine of its ten links hollow. A diagram of a
  designed system that does not mark it as designed is the visual form of
  claiming an implementation that is not there.

### The role layer

`docs/architecture/AIRL_OS_ROLES.md` — fourteen durable functions, each with its
mandate, what it decides, **what it may never do**, what it produces, when it
escalates, and which roles it may be combined with. Plus the authority-flow
diagram and a combination matrix.

The matrix is the useful part in a one-person operation: it shows that the
**Assurance Lead and the Metascience Lead cannot be the producer**, which is
precisely the corner where finding **C2** lives. The available resolutions —
supply the function mechanically, bring in an external party, or accept that the
assurance class stays unreachable — are named, and choosing between them is
still the open decision.

### Evidence

- `python3 scripts/make_figures.py --check` → **3 figures, 0 drift**
- `uv run pytest` → **20 passed** · `validate_skills.py` → **49 conform**
- Plan seal **202/202** · mirror drift **0** (203 plan, 64 skill/doc/figure)
- Figures mirrored into the vault with rewritten relative paths; vault and
  `vault_baseline` identical

### Limits

- **No role is bound in software.** `RoleBinding` is specified in WP-013 and
  built nowhere; the constraint engine does not exist.
- The figures describe a design. Nothing in them became more real by being drawn.
- SVG only. PDF/PNG export needs a rasteriser that is deliberately not a project
  dependency; the commands are documented in `docs/figures/README.md`.

### Next step

Unchanged, and now overdue: **issue one signed specimen `EvidenceManifest` under
WP-000**, then stand up CI — which now has six checks waiting.

---

## Step 007 — Commissioning baseline v1.0: drift closed, architecture sharpened, plan bound

**Time:** 2026-08-22
**Scope:** external review response — documentation drift, eight architectural
corrections, and the first binding of the skill layer into the sealed plan

### Why this step exists

An external review checked the state after Step 006 and raised eleven verifiable
claims. **All eleven were true**, and several were drift introduced by Step 006
itself — a document asserting a state that no longer existed, which is precisely
the failure this framework is built to catch. Two were structural.

### Structural corrections

**WP-000 carried a hidden downstream dependency.** Its card said
`Hard dependencies: none` while task T04 anchored timestamps through WP-139 — the
bootstrap package reproducing the deadlock shape it exists to break. WP-000 now
owns an interim time anchor outright; **WP-139 later assumes ownership**, and the
dependency direction is fixed as WP-139 → WP-000.

**Bootstrap ordering was contradictory.** The commissioning README still named
WP-001 as the first executable point. The plan now starts in two explicit steps:
`WB Bootstrap (WP-000) → W0 Programme lock (WP-001…)`. WP-001 remains the first
*normal* package; it simply cannot be accepted before WP-000 exists.

### Drift closed

- `SKILL_LAYER.md` §14 rewritten into before/after form — it described the
  pre-Step-006 state in the present tense.
- `skills/README.md`: the vendoring arithmetic was wrong. Three upstream skills,
  not two, are represented by AIRL adaptations
  (`using-superpowers`, `writing-skills`, `verification-before-completion`):
  **14 − 3 = 11 vendored verbatim**.
- Commissioning inventory: 140 WP / 194 md / 195 sealed → **141 WP documents /
  201 md / 202 sealed**, and 40 → **46** scenarios propagated through the go-live
  checklist, the cutover packages, the scope matrix and the wave map.
- **The audit is now frozen.** It carried 2026-08-21 counts alongside later
  remediation notes. A single recorded banner marks it immutable, and current
  state moved to `docs/review/2026-08-22_remediation_verification.md`. An audit
  edited to match the present is no longer evidence.

### Architectural corrections

| Correction | Why it matters |
|---|---|
| **In-principle acceptance is conditional**, routed on `research_mode` | Forcing Registered Report ceremony onto exploratory work teaches people to mislabel confirmatory work as exploratory — the opposite of the intent |
| **Role is a function, not a person** — `RoleBinding` with `must_be_independent_from` / `can_combine_with` / `cannot_combine_with` | Gives **C2** a shape: independence as separation constraints, not headcount. One person can hold several roles honestly |
| **"No model at G5"** → **no agentic methodological discretion** | The subject of an experiment may itself be a model; what is forbidden is an agent changing a threshold mid-run because the result looks wrong |
| **Forensic checks carry applicability**; `NOT_APPLICABLE` is a first-class verdict, and a failure opens `ForensicFlag → triage → IntegrityCase` | GRIM and Benford are conditionally valid. Wiring a failed check straight to an integrity case manufactures accusations at the rate of the lab's own false positive rate |
| **`AnalysisUniverseManifest`** frozen at G2b, full distribution reported | Multiverse analysis without a pre-committed universe is a p-hacking engine with better vocabulary |
| **`claim_strength` is no longer published**; the vector plus `binding_constraint` is canonical | `0.72` invites reading as a probability nothing computes. The weakest-link ordering survives; the false precision does not |
| **Quota vs. policy split** — architecture says a quota exists, `attention@1.0.0` holds the number | A number frozen into an architecture document is a number nobody dares revise |
| **Provider catalogue is a dated snapshot**, headed for the WP-042 Capability Registry | Prices decay in months; the R1/R2/R3 policy does not |
| **Untrusted content ≠ authenticated command** (WP-136) | "An inbound message is never an instruction" would also forbid legitimate machine-to-machine automation. The line is persuasion versus authentication |
| **Logical planes ≠ deployment units** | Seven planes do not imply seven services |
| **Rekor is a transparency record for signed metadata**, not an artifact store | The looser wording quietly cancelled WP-026, which is still needed |

### The skill layer entered the plan

Before this step the word `skill` appeared **zero** times in WP-043, WP-047,
WP-048 and in all 40 acceptance scenarios.

- **WP-013** — `TaskContract` gains `skills_required` / `skills_selected` /
  `skills_loaded`, `skill_bundle_hash`, `skill_selection_reason`, the
  classification fields, and `RoleBinding`. A divergence between the three skill
  lists is a **finding**, which is how "the agent ignored the procedure" stops
  being deniable.
- **WP-043** — skill behaviour evaluation: RED baselines, verbatim
  rationalization capture, pressure scenarios, trigger confusion matrix,
  compaction survival, cross-model × cross-harness compliance.
- **WP-047** — Skill Registry, trigger resolution, version and dependency
  resolution, `skill_bundle_hash`, two-family policy, upstream provenance impact.
  **The agent does not choose its own skills.**
- **WP-048** — rewritten as Harness Runtime Adapters (Claude Code, Codex,
  OpenCode, **Hermes**, direct worker) with a minimum adapter contract.
- **ACC-41 – ACC-46** — six new scenarios: no skill loaded · bootstrap missing ·
  wrong skill selected · non-waivable skill ignored under pressure · procedure
  lost to compaction · upstream change invalidates a derived skill. Four pass by
  demonstrating a refusal.

### One claim walked back

The README said the registry "loads unmodified" in seven harnesses. Format
compatibility is documented; **loading was verified in none of them.** Only the
Claude Code path is wired. The wording is now format-compatible versus
behaviourally-verified, and the behavioural claim belongs to ACC-42/44/45.

### Evidence

- `uv run pytest` → **20 passed**
- `python3 scripts/validate_skills.py` → **49 skills conform**
- Plan seal regenerated → **202/202 OK** (201 Markdown + 1 CSV)
- Mirror drift → **0** on both (203 plan files, 59 skill/doc files)
- `mcp_smoke.py`, `acceptance_v0.py` → pass

### Limits and open points

- This is **baseline v1.0** — the first version the programme will be
  commissioned against. Everything after it is a recorded change.
- **Nothing here was executed.** WP-000 has issued no manifest; ACC-41–46 have
  never run; no skill has a behaviour baseline; WP-013/043/047/048 are
  specification, not code.
- **C2 remains open.** It now has a form, not an answer.
- H1–H5 and the M-series are untouched. The Bridge is still the only working
  vertical slice.

### Next step

Stop specifying and start executing, in this order: **issue one signed specimen
`EvidenceManifest` under WP-000** — the only step that converts this design into
evidence — then **stand up CI**, which now has five checks waiting and closes
**H5**. Behaviour-testing `writing-skills` follows immediately after.

---

## Step 006 — Two skill families, an open format, and an adopted evidence standard

**Time:** 2026-08-22
**Scope:** the skill layer, the external standards register, the architecture
reference, and WP-000

### What was decided

**Research skills extend their engineering counterparts; they do not replace
them.** Sections 2–13 of `AIRL_OS_SKILL_LAYER.md` treated every Superpowers
skill as something to convert — §11 said literally *"`test-driven-development` →
add as `preregistration-discipline`"*. That reading was overruled in a new §14.

The evidence that it was wrong was in the repository: **all 12 engineering
skills were absent**, while AIRL-OS is itself built by agents. The laboratory had
written down how to conduct research and discarded how to build the laboratory.

### What was observed

- `skills/` held 38 skills and **zero** engineering skills.
- `.claude/` held no skill registration at all — the 38 skills **loaded nowhere**,
  including in the session editing them.
- All 38 used non-conformant frontmatter: `version`, `gates`, `roles`,
  `assurance_classes`, `emits`, `mechanical_checks`, `non_waivable`,
  `requires_skills`, `data_class_ceiling`, `tool_effect` at the top level, where
  the Agent Skills specification permits six fields and requires the rest under
  `metadata`.
- The word `skill` appears **zero** times in WP-043, WP-047 and WP-048, and zero
  times across all 40 acceptance scenarios. The skill layer was never connected
  to the sealed plan at all — not "partly", as had been assumed.

### What was done

1. **Format migration.** All 38 skills moved to the Agent Skills open format
   (`agentskills.io`), AIRL fields namespaced under `metadata` as `airl.*`.
2. **Engineering family vendored** from `obra/superpowers` @ `b36e0829`, MIT,
   with `airl.upstream_commit` pinned — 11 skills, including upstream's
   supporting material (`implementer-prompt.md`, task-brief scripts,
   `root-cause-tracing.md`, the `test-pressure-*.md` behaviour baselines).
   Upstream's `using-superpowers` and `writing-skills` were deliberately not
   vendored: `using-airl-os` is the single router, and `writing-skills` is the
   AIRL adaptation covering both families.
3. **`scripts/validate_skills.py`** — a real mechanical check: format
   conformance, the AIRL metadata contract, and pinned upstream provenance.
4. **Bootstrap** — `.claude/skills → ../skills`, so the registry actually loads.
5. **`using-airl-os` became a router** across both families with the two
   classification axes (`research_mode` × `execution_path`).
6. **`docs/architecture/AIRL_OS_EXTERNAL_STANDARDS.md`** — an adoption register:
   what is adopted, what is deferred, and why, each with an integration point.
7. **`docs/architecture/AIRL_OS_ARCHITECTURE.md`** — the explanatory entry point
   the corpus lacked: the principle, the evidence chain, the planes, G0–G10,
   the skill ecosystem, the attestation flow and the working V0 slice, with
   diagrams throughout.
8. **WP-000 written into the plan** — the interim evidence policy, expressed as
   an in-toto attestation signed through Sigstore and recorded in Rekor.

### Why WP-000 matters

Finding **C1** blocked the entire programme: acceptance requires a signed
manifest in an immutable store, and the store is WP-026, far downstream. The
deadlock existed only because the store was assumed to be ours to build.
Delegating immutability to a public transparency log removes the technical half
of the blocker without inventing a format.

### Evidence

- `python3 scripts/validate_skills.py` → **49 skills conform** (11 engineering ·
  28 scientific-research · 10 shared); one non-fatal warning on upstream's
  564-line `subagent-driven-development`, which is upstream's to fix.
- `uv run pytest` → **20 passed**.
- Plan seal regenerated after the WP-000 addition → **196/196 OK**.
- Mirror drift → **0** on both mirrors (197 plan files, 58 skill/doc files).
- `mcp_smoke.py` and `acceptance_v0.py` → pass.

### Limits and open points

- ⚠️ **No skill is behaviour-tested.** Format conformance is not behaviour. The
  `writing-skills` iron law — a failing baseline first — is satisfied by none of
  the 49. Upstream ships pressure tests for `systematic-debugging` only.
- ⚠️ **WP-000 resolves the storage half of C1 only.** Finding **C2** — who may
  act as an independent verifier in a one-person operation — is untouched, and no
  attestation standard resolves it.
- The skill layer is still **absent from the sealed plan**: WP-043/047/048 carry
  no skill acceptance criteria, and no acceptance scenario covers a missing or
  wrongly-selected skill.
- WP-000 is written, not executed: no manifest has been issued, signed or logged.
- Nothing about the framework's runtime capability changed. The Bridge remains
  the only working vertical slice.

### Next step

Behaviour-test the shared discipline skills against real work in this repository
— starting with `writing-skills` — and record the rationalisations observed
verbatim, replacing the anticipated tables. In parallel, stand up CI, which now
has a fifth check to run (`validate_skills.py`) and closes finding **H5**.

---

## Step 005 — File-by-file review of the whole repository

**Time:** 2026-08-22
**Scope:** every directory and every tracked file
**Status:** `DOCUMENTATION_COMPLETE` + two audit findings actually closed

### What was done

A file-by-file pass over the repository. Three kinds of change:

**1. Documentation added where there was none.** Every module in `src/`, every
file in `tests/` and both entry scripts now carry a module docstring that states
what the module is responsible for, which invariant it upholds, and **which audit
findings apply to it**. Previously not a single source file had one. The point is
that an agent loading `obsidian.py` should learn, from the file itself, that this
is the code that deletes files in the user's vault and why manifest-owned
deletion is the reason no human note has been lost.

**2. Two evidence-theatre findings closed with real fixes.**

| Finding | Before | After |
|---|---|---|
| **M2** `mcp_smoke.py` | Reported `isError` without checking it; no `assert`, no `raise`, no `sys.exit`. Exited 0 with the Bridge completely down. | Asserts the **exact** five-tool set, both call results and a non-empty response. **Verified: exits 1 with the Bridge stopped, 0 with it running.** |
| **M3** `acceptance_v0.py` | Failed unless the user's personal library contained a paper matching the hard-coded term "LiDAR". Also asserted `zotero_write_enabled is False` — a tautology against a constant. | Split into 11 data-independent structural checks plus an optional live search reading `AIRL_ACCEPTANCE_QUERY`. An empty result is `SKIPPED`, not `FAIL`. The tautological check was **removed**, and the script now reports what it does *not* prove. |

Removing the `zotero_write_enabled` assertion matters more than it looks: an
assertion that cannot fail is worse than no assertion, because it manufactures
the appearance of evidence. The read-only claim is now honestly labelled as
verified by reading the code, not by testing it (finding **H3** stays open).

**3. Stale content corrected.**

- `docs/architecture/FOUNDATION.md` was a one-line stub — one of the empty
  "deliverables" behind finding **C3**. It is now a real document: what the
  foundation layer is, what exists, and the three gaps that block it.
- The systemd unit descriptions still said "SILBO" (a leftover of finding
  **M10**). Fixed in `deploy/` and re-installed so the running units match.
- `planning/commissioning/README.md` pointed at four programme documents by
  their **pre-rename uppercase names** — four broken references. Fixed, and an
  explicit inventory table added (140 WPs, 40 ACCs, 194 Markdown files, 195
  sealed).
- Every ACC file claimed "A Critical scenario can never be waived" regardless of
  its own severity. Now severity-aware: 26 Critical, 12 High, 2 Medium, each with
  the rule that actually applies to it.
- A stray blank line under "Out of scope" in 129 generated WP files.

### Evidence

```
uv run pytest                                  20 passed
plan seal                                      195/195 OK
uv run python scripts/mcp_smoke.py             PASS (exit 0; exit 1 when Bridge stopped)
uv run python scripts/acceptance_v0.py         PASS (exit 0; 11 structural checks)
mirror_plan.py --check                         196 files, 0 drift
mirror_vault.py --check                        44 files, 0 drift
plan links                                     1021, 0 broken
doc links                                      63, 0 broken
vault wikilinks                                148, 0 broken
Turkish characters in tracked files            0
vault == vault_baseline                        identical
```

### Limits

- **Still no CI (finding H5).** Every check above runs by hand. Nothing prevents
  a commit that never ran them.
- **H3 remains open.** The read-only boundary needs a `MockTransport` behavioural
  test plus a static check; this step made the claim *honest*, not *proven*.
- C1, C2, H1, H2, H4 and the remaining M-series are untouched.
- No gate, contract semantic or work-package status changed.

### Next step

Unchanged: **settle the role → model assignment**, then rename
`model_snapshot` → `capability_fingerprint`, then stand up CI.

---

## Step 004 — Full English revision of the corpus

**Time:** 2026-08-22
**Scope:** the whole repository and the Obsidian project tree
**Status:** `DOCUMENTATION_COMPLETE`

### What was done

The entire corpus was rewritten in English and expanded — not translated
mechanically, but re-authored so that each document carries more explicit
reasoning than the version it replaces.

| Area | Result |
|---|---|
| `planning/commissioning/00_PROGRAM/` | 12 documents rewritten and renamed to English file names |
| `planning/commissioning/` WP files | **140** work packages regenerated in English, with English file names |
| `planning/commissioning/12_ACCEPTANCE_SCENARIOS/` | **40** scenarios plus the index rewritten |
| `03_package_catalogue.md` + `package_dependency_matrix.csv` | Regenerated mechanically from the WP data |
| `docs/review/` | The audit report and the review prompt rewritten; remediation status added |
| `docs/architecture/` | The three architecture documents rewritten |
| `skills/` | Already English; unchanged in this step |
| `src/`, `tests/` | User-facing strings, category folder names and MCP tool descriptions moved to English |
| Obsidian vault | Regenerated from canonical sources; human-authored notes rewritten |

### New in this step: the mirror generators

Two scripts were added, closing part of finding **M4**:

- `scripts/mirror_plan.py` — generates the Obsidian plan mirror from
  `planning/commissioning/`, rewriting file names and intra-plan links.
- `scripts/mirror_vault.py` — generates the skills and docs mirrors from
  `skills/` and `docs/`.

Both accept `--check`, which writes nothing and exits non-zero on drift. That is
the CI drift check the audit asked for; **it is not yet wired into CI**, because
there is still no CI (finding H5).

### Why it was done

A laboratory operated by multiple models cannot afford a corpus in two languages:
every document is an agent context, and mixed-language context degrades both
retrieval and instruction-following. The expansion matters as much as the
translation — the audit measured 59.2% template repetition in the WP files, and
the rewrite raises the density of package-specific content.

### Evidence

- `uv run pytest` → **20 passed** (fresh run, exit 0)
- `grep -rlP '[Turkish characters]'` across the repository → only the historical
  quotation inside audit finding L3, since rephrased → **0**
- `scripts/mirror_plan.py --check` → 196 generated files, **0 drift entries**
- `scripts/mirror_vault.py --check` → 44 generated files, **0 drift entries**
- Plan seal regenerated and re-verified after the rename

### Limits

- This step changed **documentation and user-facing strings**. It changed no
  gate, no contract semantics and no WP status.
- CI still does not exist, so none of these checks runs automatically.
- Findings C1, C2, H1–H5 and most of the M-series remain open.

### Next step

Unchanged from Step 003: **settle the role → model assignment.** Then rename
`model_snapshot` → `capability_fingerprint`, then stand up the CI foundation
(which closes H5 and automates the evidence production the rest of the plan
depends on).

---

## Step 003 — Independent audit and target-structure design

**Time:** 2026-08-22
**Scope:** the whole framework — plan, implementation, architecture, skill layer
**Status:** `DESIGN_PROPOSED / HUMAN_DECISION_PENDING`

### What was done

Three documents were produced:

1. [[10 - Projects/AI Research Framework/02 - Reviews/claude_framework_audit_report|Claude Framework Audit Report]] —
   an evidence-based independent audit. 1,509 lines of Python, 20 tests, the live
   service, SQLite, Git, the vault and 186 plan files were examined.
2. [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS Ideal Structure]] —
   the added roles, review mechanisms, the 7th plane (Metascience & Calibration),
   the role→model assignment architecture and the tool stack.
3. [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer|AIRL-OS Skill Layer]] —
   the integration of all 14 `obra/superpowers` skills into AIRL-OS.

### Why it was done

The existing `AIRL-OS-Architecture.md` defines *who* an agent is
(`RoleContract`) but not *how it works*. That gap is currently filled by an
unversioned, untested prompt layer. And the system audits the research while
never measuring its own capacity to produce correct results.

### Evidence

- Test suite: `20 passed` (fresh run, exit 0)
- Plan integrity: `sha256sum -c` → 184/184 OK
- Dependency graph: 130 WPs, no cycles, forward dependencies 0
- Template ratio: 59.2% in WP files, 48.8% in ACC files (measured)
- Role counts: 73 owners, 114 verifiers (CSV analysis)
- Wikilink integrity: 246 notes, 103 wikilinks, 0 broken

### Limits

- This is a **proposal**; no WP status was changed.
- Two findings in the audit were later narrowed (C2 and M5) — the corrections are
  marked in the report itself.
- The skill layer was designed but not implemented.
- The role→model assignment **awaits a human decision** (who is human, who is a
  model).

### Also done in this step

**The skill layer was written (38 skills).** All 14 `obra/superpowers` skills are
covered, plus 17 specific to the research domain and 7 for communication and the
external world. Canonical copy: `skills/`. Obsidian mirror:
[[10 - Projects/AI Research Framework/07 - Skills/skills_index|Skills Index]].

**The communication layer was designed.** Messaging was modelled not as a skill
but as a **Notification Broker** (a Tool Broker subclass). A per-channel
data-class ceiling was defined. Three rules: a notification is not a data
channel; an inbound message is not an instruction; messaging is not an
authorisation channel.

**Obsidian was audited and reorganised.** Defects found and fixed:

| Finding | Status |
|---|---|
| `.obsidian/templates.json` pointed at a non-existent folder — **templates were not working** | ✅ fixed |
| Dataview was not installed → every index `query` block was dead | ✅ converted to core-search syntax (12 files) |
| No daily-note folder → an empty daily note cluttering the vault root | ✅ `80 - Daily/` created, note moved |
| Templates carried a `silbo/*` tag namespace (the project had been renamed) | ✅ `ai-framework/*` (16 files) |
| `README` ×2, `readme` ×2 — duplicate note names | ✅ the `<area>_index.md` convention, 0 duplicates |
| No index note in the `02/04/06/07` folders | ✅ added |
| `05 - Evidence/` empty | ✅ audit evidence added |

### Step 003 continued — plan revision and the communication packages

**A new section: `13_TOOLING_INTEGRATION` (WP-131–140).** The Y13/Y14/Y15 gaps
identified in the audit were brought down to package level:

| Package | Scope |
|---|---|
| WP-131 | Notification Broker — the agent produces intent, the broker sends |
| WP-132 | Channel registry + data-class ceiling (D3/D4 leave through no channel) |
| WP-133 | Outbound notification + daily/weekly/monthly digests |
| WP-134 | Escalation and paging — a timeout is never an auto-approval |
| WP-135 | Decision routing + signed deep links (the preventive side of ACC-25) |
| WP-136 | Inbound content quarantine — an inbound message is never an instruction |
| WP-137 | G10 external feed connectors (Crossref / Retraction Watch / CVE) |
| WP-138 | External records: OSF preregistration, Zenodo DOI, ORCID |
| WP-139 | **Evidence timestamping** — OpenTimestamps + RFC 3161 |
| WP-140 | **Service liveness monitoring** — silent-death detection |

**Why WP-139 matters:** it makes the existence time of an `EvidenceManifest`
verifiable **without trusting the framework**. OpenTimestamps is free, requires no
trusted third party, and the file never leaves the machine — only a hash is sent.
That is the infrastructure-free solution to audit finding **C1** (the evidence
bootstrap deadlock).

**Why WP-140 matters:** audit findings **H1/H2** (silently partial sync, ghost
sources) belong to the "silent death" class — the job does not error, nothing
simply happens. A dead-man's switch makes that visible.

**The new packages carry measurable acceptance criteria.** In the existing 130
packages the criteria were 59% template and generic; in these 10, every criterion
is countable or testable.

### Limit

The content of the existing WP-001–130 was **not revised** in this step. Scope
reclassification (IN_SCOPE / DEFERRED) and the WP-000 Interim Evidence Policy
remain open.

### Next step

**Settle the role→model assignment.** For every role: human / model /
deterministic code / deferred. Without that decision the Independence Matrix
cannot be measured, the R classes cannot be applied, and the skills cannot enter
baseline testing.

Then: the baseline (RED) test for `writing-skills`, then pressure-testing the
five discipline skills in group B, then revising the WP files under
`planning/commissioning/` against this structure.

---

## Step 002 — Central project organisation and retrospective visibility correction

**Time:** 2026-08-21
**Scope:** all framework documentation, review, implementation, architecture,
evidence and component records
**Status:** `DOCUMENTATION_VISIBLE / REVIEW_READY`

### What changed

- General framework records were placed in the central Obsidian project tree
  rather than only under the Bridge application repository.
- Added `02 - Reviews/` for independent review prompts and results.
- Added `03 - Implementation/` for implementation indexes and step records.
- Added `04 - Architecture/` for repository and system maps.
- Added `05 - Evidence/` for test, acceptance, hash and review evidence.
- Added `06 - Components/Bridge/` so the Bridge is explicitly represented as one
  component rather than as the framework root.
- Added the complete review prompt and direct cockpit links.
- The complete commissioning mirror remains under `01 - Commissioning/`.

### Why

The previous layout made newly created general documents appear to belong to the
Bridge alone, and the actual Obsidian vault had not yet received the new project
folders. This separation makes the full project topology visible while keeping
code in the repository and user-facing project records in Obsidian.

### Evidence

- `04 - Architecture/framework_repository_and_obsidian_map.md`
- `02 - Reviews/claude_full_framework_review_prompt.md`
- `06 - Components/Bridge/bridge_component_status.md`
- `03 - Implementation/implementation_index.md`
- The cockpit section "Framework visibility map"

### Boundary

This is a documentation and navigation correction. It does not claim that the
work packages or acceptance scenarios are implemented. Implementation status
remains evidence-based and is tracked separately.

### Next

Use the central tree for every subsequent step: read the cockpit → the relevant
WP/ACC → implement in the correct repository component → test → record evidence
and the next step in this log → synchronise the Obsidian vault.

---

## Retroactive history — implementation steps completed before this log existed

This section records material steps completed before the Implementation Log was
created. The historical records are limited to what existing Git commits, test
output, systemd status and Obsidian hash comparisons can support; **intentions
without evidence are not shown as completed work.**

### Step 000-A — Existing installation discovery

- **What:** examined the Zotero Local API, Hermes MCP, the Obsidian vault, the
  Bridge working directory, the systemd unit and timer, and the existing file tree.
- **Why:** to avoid overwriting real paths and existing user data on an assumption.
- **Evidence:** the initial discovery and the subsequent Bridge V0 commit chain.
- **Limit:** discovery only; no production architecture is implied.
- **Next:** verify the read-only Zotero connection.

### Step 000-B — Zotero Local API and the read-only boundary

- **What:** enabled Zotero Local API loopback access; constrained the Bridge so
  that it performs no write, delete, merge or mutation of a Zotero human field.
- **Why:** to protect the user's bibliographic records from automated agent writes.
- **Evidence:** `zotero_write_enabled=false`; live acceptance output.
- **Limit:** ⚠️ **that evidence is weaker than it looks.** The field is a hard-coded
  constant, not a measured control — see audit finding **H3**. The boundary holds
  in the code as written, but nothing tests it.
- **Next:** the canonical local source registry and the Obsidian projection.

### Step 000-C — Literature Bridge V0

- **What:** built the FastAPI Bridge, the SQLite WAL registry, source identity
  and normalisation, the category and duplicate endpoints, and the Obsidian
  projection.
- **Why:** to run the first end-to-end vertical slice before moving to the large
  architecture.
- **Evidence:** commit `15d57af`; acceptance `33 sources / 3 categories`; the
  Bridge systemd service and timer active.
- **Limit:** SQLite V0; no PostgreSQL, no event bus, no Temporal, no production
  cutover. Ingest is capped at 100 records (finding **H1**).
- **Next:** separate the human and generated Obsidian areas.

### Step 000-D — Obsidian information architecture

- **What:** created the `00 - Home`, `10 - Projects`, `20 - Source Notes`,
  `30 - Concepts`, `40 - Claims`, `50 - Decisions`, `60 - Runs`,
  `70 - Literature Sets`, `90 - Archive` and `_Templates` structure; moved the
  Zotero projections under `70 - Literature Sets/Zotero Sources`.
- **Why:** so that human synthesis and automated projection files cannot
  overwrite one another.
- **Evidence:** commits `d3fc23a`, `2d64f02`; baseline/vault SHA-256 matches.
- **Limit:** this information architecture is not a full claim/evidence graph.
- **Next:** bring the plan Markdown into Obsidian and build the execution cockpit.

### Step 000-E — Commissioning plan import and cockpit

- **What:** imported the commissioning Markdown tree (130 WPs and 40 ACCs) into
  Obsidian; added the navigation/execution cockpit and the living status document.
- **Why:** so the plan is re-read at every step rather than living in chat memory.
- **Evidence:** 184 plan Markdown files in Obsidian; the cockpit's reading and
  step-closure rules.
- **Limit:** importing the plan does not mean the WPs have been built as services.
- **Next:** turn the plan into real foundation contract slices along the WP
  dependency order.

### Step 000-F — Naming and repository consolidation

- **What:** standardised the general root as `AI_RESEARCH_FRAMEWORK`; moved
  Obsidian folder and file names to a lowercase English standard; drove broken
  links to zero across 240 notes.
- **Why:** to separate the SILBO model name from the framework name and to prevent
  file and folder drift.
- **Evidence:** commit `d73b53e`; `notes=240, missing_links=0`; the generated
  dashboards `Source Catalog.md` and `Potential Duplicates.md`.
- **Limit:** Zotero article titles keep their original bibliographic form.
  ⚠️ The rename was **incomplete** — six documentation locations and the source
  category folder names kept their old values until Step 004 (finding **M10/L3**).
- **Next:** add the foundation and shared contract code.

### Step 000-G — SILBO readiness boundary

- **What:** produced capsule, mutation, byte-identical resume and drift-rejection
  evidence for FIX-005; inference was not started.
- **Why:** so the SILBO measurement line stays fail-closed while the framework
  advances.
- **Evidence:** SILBO target `b14b0b3`, evidence `3dd52e0`, handoff `ff696c7`.
- **Limit:** SILBO grants no inference authority without independent review.
  **This work lives in a separate repository and is outside the framework's
  evidence chain.**
- **Next:** implement the framework contract foundation slice; keep the SILBO
  review boundary separate.

---

## Step 001 — Foundation and contract core

**Time:** 2026-08-22
**Related plans:** WP-011, WP-014, WP-015, WP-020, ~~WP-022~~
**Status:** `TECH_COMPLETE / INDEPENDENT_REVIEW_PENDING`

### What was done

- Created the shared contract core under `src/airl_framework/contracts.py`:
  - `Identity`: validates project/workflow/task/source/claim/run/artifact/review
    identifiers in one format and derives a deterministic correlation key.
  - `ArtifactManifest`: requires SHA-256, size, producer, source revision, parent
    lineage and a `VALID/SUPERSEDED/REVOKED/QUARANTINED` state.
  - `EventEnvelope`: carries event type, schema version, actor, subject, payload
    reference, causation and correlation; it binds the payload by reference
    rather than silently embedding it.
  - `SchemaRegistry`: records the schema version, refuses redefinition and treats
    a major-version mismatch as a breaking change.
- Made the contract surface importable through `src/airl_framework/__init__.py`.
- Added `CODEOWNERS` and `dependency-rules.txt` boundary files.
- Tested both the accepting and the rejecting directions in
  `tests/test_contracts.py`.

### Correction (2026-08-22)

This step originally also claimed **WP-022 (repository topology)** as
`TECH_COMPLETE`. **That claim was wrong** and is retracted:

- The directories it created (`services/`, `workflows/`, `agents/`, `infra/`,
  `policy/`) were empty, and Git does not track empty directories — so they never
  existed in the remote repository at all.
- `CODEOWNERS` contained a single comment and enforced nothing;
  `dependency-rules.txt` was one unparseable line.

See audit finding **C3**. **WP-022 status: `NOT_STARTED`.** The two boundary
files now carry real content (Step 004), but without CI enforcement they are
still not a deliverable.

### Why it was done

The plan's target invariants require one correlation chain, immutable artifact
lineage, versioned events and canonical field authority. The existing bridge had
only the literature `SourceRecord` model; without this shared core, later claim,
run, review and decision services would each mint incompatible identities.

This step is not the production infrastructure. It establishes the shared
contract boundary that later services will bind to.

### Evidence

- `uv run pytest -q` → **20 passed**.
- The tests cover acceptance of valid identity/artifact/event/schema objects and
  rejection of lowercase identifiers, malformed digests, schema redefinition and
  a missing major version.

### Limits and open points

- ⚠️ **The contract core has zero production consumers** — nothing in
  `src/airl_bridge/` imports it, and its `content_hash` format already contradicts
  the format the bridge produces. See finding **H4**.
- `SchemaRegistry` is not yet a persistent registry service or a database; it is
  an in-process prototype that validates nothing against JSON Schema.
- The CODEOWNERS owners are placeholders; they must be settled by the WP-003 RACI
  and the WP-010 ADR decision.
- PostgreSQL, the object store, the event bus, the policy engine and Temporal have
  not been built.
- There is no independent verifier acceptance, so the step is `TECH_COMPLETE`,
  not `ACCEPTED`.

### Next step

Move the WP-011/014/015/020 contract surface into JSON Schema and
machine-readable manifest files, and give it **at least one real production
consumer** (route `SourceRecord.airl_id` generation through `Identity`). Then
bind the WP-013 project/task/role contract to the same registry.
