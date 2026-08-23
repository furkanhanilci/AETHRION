---
airl_id: AETHRION-IMPLEMENTATION-LOG
type: execution-log
status: active
owner: otonom
updated_at: "2026-08-23"
tags:
  - aethrion/execution
  - aethrion/contracts
  - aethrion/foundation
cssclasses:
  - aethrion-execution-log
---

# AETHRION — Implementation Log

Every material implementation step is recorded here. Each entry separates **what
was observed** (evidence) from **what was concluded** (interpretation), states
its **limits**, and names the **exact next step**. Before starting a new step,
the last entry, the cockpit and the relevant WP files are read again.

---

## Step 018 — Baselines v1.2.0 and v1.3.0: assimilation, and the failure modes a cohort adds

**Time:** 2026-08-23
**Scope:** two workstreams opened · WP-141–159 · ACC-052–120 · ADR-004–019 ·
58 upstream entries · a lineage register with its own checker · five figures ·
findings J1 and J2

### The premise, stated because it governs everything below

The intent was never to invent. It was to assemble: *copy implementations
selectively, copy ideas aggressively, copy architecture only after understanding
why it works, and rewrite everything into this project's domain model.* And with
one constraint that is not a preference — **do not hide the source; remove the
source's architectural identity.** Taking someone's code, changing it slightly,
concealing where it came from and claiming it as original is the thing this step
was built to make structurally impossible.

That is why the first artifact produced was not a design. It was a register.

### `provenance/upstreams.json` — 58 entries, and a checker that can fail

Every mechanism considered from another project has an entry: repository, paper,
licence, whether the licence was **read at the source**, assimilation type,
pinned commit, source files, local modules, work packages, and — required on
every entry — an **`authority_boundary`** saying what the mechanism may never
decide.

`scripts/check_upstream_lineage.py` enforces eleven rules and `--self-test`
injects a defect per rule, failing if any rule stays silent.

Three licences changed the *method* rather than the paperwork:

- **GPL-3.0** (MAS-Resilience) → no copy; reimplement from the published
  description.
- **CC-BY-NC** (WASP) → benchmark use only; it never enters product code.
- **MIT** (AgentSlimming) → legally copyable, and its core mechanism is **refused
  anyway** because `ADR-011` forbids reducing a cohort for cost. A permissive
  licence is permission, not a reason.

Fifty-six of the fifty-eight are `PROPOSED`. One is `REJECTED`. **One is
`ACCEPTED` and has running code** — Crossref, behind `scripts/monitor_sources.py`.
That ratio is the honest state of the assimilation programme and is printed by
the checker on every run.

### v1.2.0 — the scientific-intelligence workstream

Seven packages and twenty-nine scenarios, over six decision records: mechanism
assimilation (`ADR-004`), epistemic memory separation (`ADR-005`), the discovery
search graph (`ADR-006`), the frozen evaluator zone (`ADR-007`), the V0–V3
verification taxonomy (`ADR-008`) and publication as projection (`ADR-009`).

`ADR-008` is the one that reached back into the existing plan: the evidence
strategy's "E1 mechanical" had been covering two incompatible kinds of check, and
the rule *a mechanical check runs first and cannot be overridden by a model* is
correct for V0 and V1 and absurd at V2, where it says a model's judgement cannot
be overridden by a model.

### v1.3.0 — the reliability layer, and why it was needed

The plan to this point described a **pipeline**. It did not describe a **cohort**.
Nothing in it refused a single-agent downgrade of substantial work, caught a
confident wrong answer becoming consensus, stopped a budget optimiser cutting
assurance instead of verbosity, noticed an implementation quietly diverging from
a frozen method, or told a benchmark score that had seen the answers from one
that had not.

Twelve packages (WP-148–159), forty scenarios (ACC-081–120) and nine decision
records (`ADR-011`–`ADR-019`).

**The identifier collision, and how it was resolved.** The delta proposed
ADR-004–012; all nine were taken. Applying the delta's own rule — never
overwrite, the semantic name is binding — they became ADR-011–019, and reading
them properly revealed that two were not new decisions at all: `ADR-015`
*extends* `ADR-008`, and `ADR-019` *extends* `ADR-004`. Both are cross-linked in
both directions, and the remap is recorded in
`docs/review/2026-08-23_reliability_delta_id_remap.md`.

**The invariant that costs the most and is least negotiable.** Every cost
pressure a multi-agent system ever experiences argues for fewer agents.
`ADR-011` closes that door once: the cohort is an epistemic requirement, a cost
argument is not an answer to it, and what gets optimised is the conversation
instead. Independence is a five-dimension profile rather than a count — five
instances of one model on one context are one contribution, and they will agree.

### Two findings, and they are the same failure

- **J1** — `acceptance_v0.py` compared the whole projection manifest against the
  registry's source count. Finding I3 had deliberately moved two dashboards
  inside the manifest, so from that moment the check failed by exactly the number
  of dashboards, on a correct system. **The defect was in the check.**
- **J2** — the lineage checker's licence rule matched `licence.upper() ==
  "UNVERIFIED"` *exactly*, so `"UNVERIFIED — repository licence not confirmed on
  2026-08-23"`, strictly more informative, slipped past in silence. The rule was
  also wrong in principle: it forbade every assimilation type, when `ADR-004`
  says reimplementing a published mechanism creates no licence obligation and an
  unverified licence is a *reason* to reimplement rather than a reason to stop.

J1 compared the wrong two numbers and reported a defect that was in the check. J2
matched the wrong string and reported clean because nothing it could see was
wrong. The register's own `--self-test` missed J2 because its injection wrote the
bare word the rule matched: **a control tested only with the input it was written
for is a control tested against itself.**

### The correction that mattered most

Work opened as a **v2.0.0** baseline. It is not v2 — it is an improvement inside
V1 — and every reference was reverted to v1.2.0 across the plan README, the
progress ledger, the index generator, the acceptance index, WP-115 and the root
README.

But the rule in `AGENTS.md` §7.4 is *a correction keeps the finish line where it
is; an addition moves it*, and both baselines are **additions**. That is recorded
as such rather than softened. `10_go_live_checklist.md` gained entry conditions,
and the plan is larger than it was.

### Evidence at the close of this step

```text
packages              141 → 159   (plus WP-000)
scenarios              51 → 120
decision records        3 → 19
figures                 9 → 14
tests                  46 → 60
upstream entries        0 → 58
plan seal             631 files
bundle                16/16
```

### Limits

Every capability added across both baselines is `SPECIFIED`. `src/` is a Zotero
bridge with thirteen modules; there is no cohort record, no blackboard, no
topology compiler, no communication governor, and no baseline harness to measure
any of it against. The delta's execution order assumes a runtime from step 5
onward, and that half is deferred with the reason written down rather than
quietly skipped.

---

## Step 021 — Closing the bridge findings: eleven of twelve

**Time:** 2026-08-23
**Scope:** H1 · H2 · H3 · H4 · M1 · M6 · M7 · M8 · M9 · L2 · L4 closed ·
H5 remains, and cannot be closed from inside the repository

### What these findings had in common

Reading them as a list of twelve unrelated defects misses the pattern. Almost
all of them were one property seen from different angles: **the system did
things it could not report on.**

- A fetch capped at 100 records reported the run `SUCCEEDED`.
- A source deleted upstream lived on in the registry and the vault forever.
- A projection that failed left the registry advanced and nothing said so.
- A read-only boundary — *the framework's strongest security claim* — was
  asserted by a hard-coded constant, so the three artifacts that appeared to
  verify it were testing `False is False`.

Each of those is silent in exactly the situation where you would want it to
speak. So the fixes are less about new capability than about making the system
able to say what it did.

### The order was in the register, and it mattered

H1 said, in the "why it is still open" column, *fix M9 first*. Not a preference:
pagination without it turns a masked truncation into **active data loss**.

The chain is: a complete walk authorises the deletion reconciliation → a
reconciliation run against a partial library withdraws every source the fetch
did not reach → and the 100-record cap was the only thing preventing a partial
walk from looking complete. Fix pagination alone and you have built a machine
for deleting three quarters of a library.

`fetch_top_items` therefore returns `(items, **complete**)`, and
`reconcile_deletions` runs only when `complete` is true. That coupling is now
`test_a_partial_walk_does_not_reconcile_deletions` rather than a warning in a
docstring.

### Deletion is a tombstone

`withdrawn_at`, not `DELETE FROM`. A registry is the system of record for source
identity, and an identity that silently vanishes cannot afterwards be told apart
from one that never existed — which is precisely the question an audit asks
about a citation that no longer resolves. A source that comes back keeps its
`airl_id`, because minting a new one would break every reference made while it
was withdrawn.

### One vulnerability was two

M1 read as "the mutating endpoints are unauthenticated". It is two distinct
problems needing two distinct controls:

- **CSRF** — a browser page can issue a preflight-free `POST /v1/sync` whose side
  effect runs even though the response is unreadable. Fixed by requiring
  `X-AIRL-Token`: a custom header is not on the CORS safelist, so the preflight
  the attacker cannot satisfy is forced.
- **DNS rebinding** — after the page loads, `attacker.example` resolves to
  `127.0.0.1` and the browser treats `GET /v1/sources` as same-origin. A token on
  the *writes* does nothing about that, so every request is checked against
  `allowed_hosts`.

An unset `AIRL_API_TOKEN` returns 503 rather than opening the endpoints. Failing
open on missing configuration is how a mandatory control becomes optional in
practice while staying mandatory on paper.

### A defect introduced while fixing one

The dry run added for M7 parsed the projection manifest itself and read the wrong
key — `files` where the format writes `generated_files` — so it reported **zero
deletions forever**. A planner that cannot see what a real run would delete is
worse than no planner, because it is reassuring.

The test caught it, and the parse is now shared with `_remove_stale` rather than
duplicated. That is the same one-owner rule that closed **K3** in the previous
baseline, applied two hundred lines further down: two representations of one
fact, disagreeing.

### The read-only boundary, finally evidenced

`zotero_write_enabled` is still a constant. It is simply no longer the evidence
for anything. The evidence is a transport that raises on any method other than
`GET`, driven through the whole ingest — **and a test that proves the transport
can raise.** Without that second test, the first passes just as happily against a
transport that checks nothing.

### H5 is the one left, and it is not a code problem

The CI workflow now covers the whole automatable bundle including every
self-test. It has never run. Activating it means `gh auth refresh -h github.com
-s workflow` and copying the file into `.github/workflows/` — an operator action
this session cannot perform.

Which means the eleven closures above are proven by a suite somebody has to
remember to run. That is the weaker half of the same claim, and it is worth
naming rather than rounding up.

### Evidence

```text
tests                 131 passed   (93 → 131)
bundle                19/19
plan seal             632/632
open findings         12 → 1
```

### Limits

Every closure is a closure **against the check named beside it**, not in general.
H4 closed the binding — the bridge and the contract core now mint one digest —
and did **not** close `SchemaRegistry` being an in-process dictionary that
validates nothing; `src/airl_framework/README.md` says so where a reader will
find it. And the largest untested claim in the repository is untouched: **no
skill has a behaviour baseline**, and the runtime for one does not exist.

---

## Step 020 — Baseline v1.3.1: the plan made executable

**Time:** 2026-08-23
**Scope:** an external integration-consistency audit, adjudicated finding by
finding · the canonical programme model · four dependency directions reversed ·
four new controls · findings K1–K4

### What the audit was for

The two previous baselines added architecture. This one adds none. An external
package attacked the **seam** between the architecture and the machinery that
enforces it — which is exactly where the defects from those two expansions had
collected, because adding a workstream touches the plan and nothing forces it to
touch the generators, validators and figures that describe the plan.

Its own README refuses "could not reproduce" as a disposition unless the current
file, generator, registry and test evidence are cited. Every finding was
therefore verified **computationally**, not by reading, and the results are in
[`review/2026-08-23_integration_remediation_dispositions.md`](02%20-%20Reviews/integration_remediation_dispositions.md).

### The defect the whole baseline turns on

**A dependency graph can be perfectly acyclic and impossible to execute.**

Two packages required before go-live depended on packages that exist only after
it: WP-152 needed the Day-2 postmortem rhythm to define a failure taxonomy that
rhythm should consume, and WP-155 needed recurring recalibration for an initial
qualification it must have before anything runs. Neither is a cycle. The plan had
no valid starting order, and every check in a 16/16 bundle passed.

The plan validator *did* carry a phase rule. It read `Related packages` from the
**scenario document** while the violating edge lived in a **matrix column**, and
it only examined scenario→package edges while both real deadlocks are
package→package. A rule pointed at the compliant source.

### One relation, two owners, disagreeing 98 times

That column turned out to be the deeper problem. The WP↔ACC binding was written
in the scenario documents *and* in the matrix, and the two disagreed on **98 of
120 scenarios** — including eleven `PRE_GO_LIVE` scenarios the column bound to
Day-2 packages. It is the repository's own finding **M5**, open since the first
audit, and it is the mechanism behind the audit's headline P0.

The column was **deleted**, not synchronised. A cache with a drift check is still
two representations of one fact, and `ADR-014`'s answer to that is not a better
check.

### The aggregate that meant 118 and said 2

`WP-115`'s card, line 15: *"every scenario whose `Acceptance phase` is
`PRE_GO_LIVE`; the set is derived, never enumerated here, because an enumeration
drifts the moment a scenario is added."*

185 lines below, inside the generated block an independent verifier actually
works from: `ACC-01` and `ACC-40`. The prose was right, the machinery was wrong,
and the machinery was the surface being trusted.

Fixing it made **nine** cycles reachable. The audit predicted one.

### A deterministic generator reproducing a false claim

`aethrion_waves.svg` rendered *"141 work-package documents"* against a registry
of 160, for two baselines. `aethrion_topology.svg` said *"221 planning files,
byte-identical to baseline v1.0.5"* three baselines and 410 files later. Both
passed the containment check, which measures text boxes, and both passed the
drift check — which compares a figure to the generator that drew it, and the
generator was the thing that was wrong.

Wave membership was hard-coded in **two** places, both ending at `WP-140`, while
the wave map document listed W-S and W-R in prose. `expand_packages.wave_of`
returned the string `"unassigned"` for nineteen packages, and a string is not an
error.

### What was built

One canonical model — `00_PROGRAM/programme_metadata.json` plus
`scheduling_phase`, `wave_id` and `scenario_selector` columns — and four controls,
each carrying a self-test that reproduces the defect it was written for:

| Control | Rules | Its own mutations |
|---|---|---|
| `check_programme_graph.py` | 7 over package, scenario and milestone nodes | 6 |
| `check_figure_semantics.py` | 4 derived claims, read from the rendered SVG | 4 |
| `check_document_hygiene.py` | 5 distinct error codes | 3 + a clean specimen |
| dynamic-fact family in `check_stale_claims.py` | 4 facts over 12 live surfaces | positive and negative |

### The lesson from building them, which is the useful part

**Four of the seven programme-graph rules were defective when first written**,
and the self-test found all four before any of them ran on the corpus: two could
not fire at all, one crashed before its own diagnostic printed, and one —
`V-SCEN-002` — was *disabled by the very mutation it was meant to catch*.

That last one deserves its own sentence. The rule iterated over packages that
**had** a selector. Deleting `WP-115`'s selector therefore deleted the check
along with it, silently restoring the two-scenario enumeration. **A check
anchored on the thing it checks can be switched off by deleting that thing.** It
now iterates over the aggregators *declared* in the metadata.

And the figure checker's first bijection rule invented a naming convention —
`fig_X.py → aethrion_X.svg` — then enforced it, reporting two findings against a
repository with no defect (`fig_evidence.py` writes
`aethrion_evidence_chain.svg`). **A checker that invents a rule and enforces it
is worse than none, because its findings look like the real ones.**

### Where this repair departs from the package

Two places, both recorded as decisions rather than omissions:

- the scenario column was **deleted** rather than kept alongside a selector, per
  `ADR-014`;
- **WP-119 was left selector-free.** It is the cutover *rehearsal*, and a
  rehearsal that must first pass the entire commissioning suite is not a
  rehearsal — it is the suite.

### Evidence

```text
bundle                19/19   (three new checks added)
plan seal             632/632 (one file added: programme_metadata.json)
plan semantics        160 packages · 120 scenarios · 0 warnings
programme graph       0 phase inversions · 0 cycles · aggregates = registry query
figure semantics      4 claims match · 4 mutations caught
document hygiene      748 governed documents · 0 structural defects
tests                 93 passed
vault                 well-formed
attestation           signature OK · 9 subject digests OK
```

### Limits

The plan is now executable. **That is a statement about the plan, not about the
system it describes.** Nothing is `ACCEPTED`, nothing is `INTEGRATED`, nothing is
`MEASURED`, and no skill has a behaviour baseline. Every performance figure in
the plan remains a target awaiting a calibration run that has never been made.

Two scope-matrix rows were deliberately **not** closed, though similarly-named
packages now exist: agreement/error-correlation measurement, and programme-level
control-injection rates. WP-155 qualifies a verifier and WP-126 recalibrates one;
neither measures correlation *between* reviewers, which is the number deciding
whether two agreeing verdicts are one observation or two.

---

## Step 019 — Baseline v1.3.0 completion: the extension pass, and a checklist made mechanical

**Time:** 2026-08-23
**Scope:** 26 pre-v1.2.0 scenarios extended in place · delta documents 28, 29,
32, 35 and 38 applied · the final-audit wording list implemented as eight
regression rules with a self-test · findings J3 and J4

### What was left after Step 018

Step 018 landed the reliability layer as new material: twelve work packages,
forty scenarios, nine decision records, two figures, twenty-two upstream entries.
What it did not do is reconcile that layer with the plan that already existed.
`ACC_001_080_EXISTING_IMPACT_MATRIX.md` flags fifty-five scenarios
`REVIEW/EXTEND`, with the instruction *"avoid duplicate semantics"*, and five
delta documents had been read but not applied.

### The extension pass — 26 scenarios, not 55

Twenty-nine of the fifty-five are ACC-052–080, authored at v1.2.0 and already
carrying the layer the matrix asks for. Extending them would have produced the
duplication the instruction forbids. **Twenty-six predate v1.2.0**, and each was
extended in place: two or three additional invariants, one additional test step,
and a short section naming the failure that scenario would otherwise pass while
leaving unexamined.

Every added block says, in the scenario itself, that it is an extension and that
the reliability layer's own scenarios are ACC-081–120 — so a reader arriving at
ACC-05 from an old reference finds the new obligation without finding a second
copy of ACC-117.

**One correction fell out of reading them.** ACC-08 described its counter-test as
run by "the mechanical verifier" — precisely the wording the delta asks a final
audit to search for. It is a deterministic re-execution against a frozen target,
so it now names the **V1 computational verifier** it actually is. Worth recording
because the regression rule written the same day does *not* fire on it: the
wording was found by reading, and that is the limit of the rule.

### Five delta documents, applied where they belong

| Document | Applied to |
|---|---|
| 28 — external benchmark release qualification | `00_PROGRAM/06` as **E6**: five axes, three constraint rules (licence, no merge into product code, every result pinned to model and snapshot) |
| 29 — metascience and Pareto release gates | `00_PROGRAM/06` as **"Release quality is a frontier, not a verdict"**: a fixed, public measurement set |
| 32 — baseline freeze and release dossier | `00_PROGRAM/09`: fifteen inventory elements, and the five-word maturity vocabulary `SPECIFIED` → `CODED` → `TESTED` → `ACCEPTED` → `EXTERNAL_BENCHMARKED` → `MEASURED` |
| 35 — definition of done / final audit | `00_PROGRAM/05`: ten `DONE` conditions, plus the wording audit — see below |
| 38 — hard acceptance targets | `00_PROGRAM/10` and `06`: hard zeros as conditions, performance figures as **targets to be frozen after calibration** |

Two of those deserve their own sentence. **Useful challenge rate** is the ratio
that stops the coordination measures from being gamed: cutting every message
between agents drives redundant message rate to zero and drives useful challenge
rate to zero with it, and only the second number reveals that the cohort has been
silenced rather than optimised. And the performance targets are recorded
everywhere as targets — they are reported results from other systems doing other
work, and importing them as thresholds would be the same error as importing a
benchmark score.

### The finding that changed the shape of the work — J3

Document 35 ends with eight wordings a final audit should grep for: a
single-agent default, a fully-connected topology as the target, a mechanical
check doing semantic work, a timeout that approves, an event as authority, a
projection as canonical, a published number with no binding, the engineering
skills as tooling.

**Every one of those eight phrases already appears in this repository, every time
inside a sentence that forbids it.** A hand grep returns a wall of correct prose.
The auditor stops reading it, and the one affirmative use is somewhere in the
middle. A checklist item that produces a hundred false positives is a checklist
item that gets ticked without being read.

So it is implemented instead: a third rule family in `check_stale_claims.py`,
with two guards at different scopes — a paragraph-level prohibition marker, and a
local negation check on the thirty characters before the match — and every rule
carrying **a specimen that must trip it and a specimen that must not.**

### The finding that justified the design — J4

The self-test reported **two of the eight rules silent on their own positive
specimen**, before either had touched the corpus. The fully-connected rule read
left-to-right only, and English does not. The timeout rule was suppressed by a
paragraph guard containing the bare word `not`, so *"if the reviewer does **not**
respond the gate auto-approves"* read as a refusal.

The first corpus scan then produced four false positives: `Expiry | WP-024
acceptance` in a decision-record table, the heading `Timeout escalation path with
no approval branch` in nine work packages, and two scenarios naming a derived
store and the canonical records in one breath. All four are now tests.

**A regression checker shipped without a self-test would have printed the same
reassuring line as one that worked, and this repository would have recorded eight
controls where it had six.** It is J2's sentence one layer up — *a control tested
only with the input it was written for is a control tested against itself* — with
one addition: for this rule family the negative specimen is mandatory too,
because a checker that flags every correct paragraph gets switched off, and a
switched-off checker and an absent one are the same thing.

### Also completed

- `README.md` §4 gained the **collaboration plane**, with both new figures, the
  degradation floor, and the authority section — the planes diagram had six
  planes and the architecture had seven.
- `schemas/README.md` gained the seventeen v1.3.0 contracts, each owned by a work
  package and each labelled `SPECIFIED`, with the three properties that cut
  across them: never a substitute for canonical state, evidence about a run
  rather than authority over it, and immutable where immutability is the point.
- `09_change_and_configuration_control.md` said **"the current baseline is
  v1.1.0"** two baselines after it stopped being true. Corrected, with v1.2.0 and
  v1.3.0 both recorded as **additions that moved the finish line** — because a
  baseline that moves the finish line while calling itself a refinement is the
  most expensive undocumented change a plan can carry.

### Evidence

```text
bundle                16/16
plan seal             631/631 OK   (29 files changed, no file added or removed)
plan semantics        160 work packages · 120 acceptance scenarios · 0 warnings
tests                 70 passed
stale claims          6 literal · 2 derived · 8 architectural regression rules
regression self-test  0 silent on positive · 0 firing on negative
vault                 929 pages · 0 broken links · 0 uncontrolled tags
attestation           signature OK · 9 subject digests OK
```

### Limits

The seal proves twenty-nine plan files changed and none was added — it does not
prove the extensions are the right extensions. The eight regression rules are
narrower than the concept they implement, and the gap is stated in the checker
itself rather than implied: an author who asserts a regression inside a paragraph
that happens to refuse something else escapes the rule. And every capability
touched in this step remains `SPECIFIED`. Nothing in workstream 15 runs.

### Next

The five delta documents applied here were the last unapplied ones. What remains
is not delta application but the standing gap: **no work package is `ACCEPTED`,
and no skill has a behaviour baseline.** Those are the two claims this repository
most wants to be able to make and currently cannot.

---

## Step 017 — Structural completeness: every folder explains itself

**Time:** 2026-08-22
**Scope:** folder-level documentation · fourteen generated workstream indexes ·
document-kind taxonomy · a stray artifact removed

### The audit

A structural scan asked one question of every directory a reader can arrive at:
**does it explain itself?** Fourteen commissioning workstreams holding 141
package documents and 51 scenarios had no index at all — the plan could only be
navigated by knowing package numbers in advance. `docs/`, `scripts/`, `tests/`,
`deploy/`, `src/*` and four `delivery/` subdirectories were the same.

A directory of 141 files with no way in is not organised; it is sorted.

### Fourteen indexes, generated

`scripts/make_plan_indexes.py` writes each workstream README **from the packages
in it** — title, hard dependencies, status, and whether the package stands on an
adopted component. A hand-maintained index of 141 packages drifts within a week,
so this one is derived and `--check` fails the build if it is edited.

The seal moved **207 → 221**, and the inventory, mirrors and status page followed.

### Ten folder READMEs, written to be read cold

`docs/` (a reading order for someone arriving with no context) · `docs/architecture/`
· `docs/review/` · `scripts/` · `tests/` · `deploy/` · `src/airl_bridge/` ·
`src/airl_framework/` · `delivery/specimen/` · `delivery/_keys/` ·
`delivery/WP-000/` · `skills/_vendor/` · `.claude/`.

Two conventions made them worth having:

- **Each states what it does not contain.** `tests/README.md` lists what is
  untested — the read-only boundary, agent behaviour, everything designed and
  unbuilt — and that list is the more useful half.
- **Each names its own limit at the point of the claim.**
  `src/airl_framework/README.md` opens by saying nothing imports it and that its
  digest format contradicts the bridge's, because a component reference that
  buries finding H4 in a footnote is advertising.

### The taxonomy that was missing

`DOCUMENT_STANDARD.md` now names four document kinds — **reference · decision
record · proposal · evidence** — plus generated documents as a fifth. Confusing
them is the main way this repository gets overestimated: *"nobody has agreed to
this"* is the whole content of a proposal label, and `AETHRION_IDEAL_STRUCTURE.md`
had been read as description more than once.

It also adds **folder-level documentation** and **writing for a reader who
arrives cold** as standard sections: expand acronyms per document, name files
rather than "the above", give reference tables a *question* column, and **put the
limitation next to the claim** so a reader who stops early is not misled.

### A stray artifact

`delivery/WP-TEST/` — a pytest fixture's output — had been **committed into the
evidence directory**, where a reader would reasonably take it for a real package.
Removed, git-ignored, and the fixture now cleans up after itself.

### Evidence

- 10/10 status checks · seal **221/221** · plan semantics OK
- workstream indexes: 15 directories, 0 drift · stale claims 0 · counts agree
- 25/25 tests · 52/52 skills · 5/5 figures, 0 overflow · mirror drift 0
- **every directory now carries a README**; every vault index is linked from the cockpit

### Limits

- This step made the repository legible. It added **no capability**, and the
  things it explains more clearly are still mostly unbuilt.
- Folder READMEs are hand-maintained except the fourteen generated ones; they
  will need the same discipline the rest of the corpus gets.

### Next step

Unchanged, and now easier to hand to someone else: activate BVC-01, accept
WP-000, run the authoring bake-off in Docker.

---

## Step 016 — A full pass over every folder, and drift made mechanically visible

**Time:** 2026-08-22
**Scope:** corpus-wide staleness audit · five stale programme documents · every
vault index · a generated status page · ten skills bound to their components

### The audit, done mechanically rather than by eye

A scan for statements the repository had outgrown found **66 stale phrases in 24
files**. The important part was the classification: roughly half were
**legitimate history** — implementation log entries, the frozen audit, dated
ledger rows — and editing those to match the present is exactly what
`DOCUMENT_STANDARD.md` §3 rules 3 and 4 forbid.

So the fix was not a find-and-replace. `scripts/check_stale_claims.py` now
separates the two:

| Exempt | Why |
|---|---|
| implementation log · frozen audit · frozen verification reports | they record a moment |
| a sentence in the past tense | *"at the time, all 38 skills were non-conformant"* is history |
| a dated ledger row | `\| 2026-08-22 \| Step 003 — 38 skills written \|` is a record |

**477 documents scanned, 8 historical records exempt, 0 stale claims.** A checker
that could not tell those apart would push a maintainer toward the forbidden edit.

### Five programme documents nobody had touched

`00_how_to_use_this_plan` · `01_target_state_and_invariants` ·
`04_role_and_responsibility_matrix` · `07_programme_risk_register` ·
`09_change_and_configuration_control` had not moved since the English rewrite,
and every decision since had passed them by. They now carry:

- the **three-check** plan verification — seal, semantics, declared counts — and
  the rule that re-sealing to silence a failing check is the seal's one
  prohibited use
- the **restated invariants**: no agentic methodological discretion; internally
  separated verification at R1/R2; untrusted content is data; **role is a
  function, not a person**
- the audit findings' **current status**, and four new risks this baseline
  itself creates — chief among them **adoption without verification**, since ten
  packages now stand on external components

### A status page that cannot drift

Dated verification reports are evidence and are now **frozen with a forward
pointer**. Live status moved to `docs/STATUS.md`, **generated** by
`scripts/write_status.py` running the bundle: every line is the last line of a
command that was just run.

Building it exposed three faults in itself, which is the argument for generating
it at all:

| Fault | Fix |
|---|---|
| pytest's final line is a documentation URL | select the summary by content, not position |
| `-q` suppresses the summary when stdout is not a terminal | drop the flag |
| the recorded line carried an elapsed time, so `--check` could **never** pass | strip the duration — a check that cannot pass is worse than none |

It also immediately caught a broken seal and two stale count patterns that the
manual pass had missed.

### Every vault index brought current

`architecture_index` gained the eight documents and three ADRs written since it
was last touched; `evidence_index` gained the measurements; `components_index`
now distinguishes the six things that actually run from the ones that do not;
`bridge_component_status` carries the checks that now run against it; the
repository map, the cockpit and the roadmap were corrected.

Two skill groups both sorted under **H**; reporting moved to **I**.

### Ten skills bound to what they stand on

`curating-zotero` · `searching-literature` · `screening-sources` ·
`extracting-evidence` · `anchoring-spans` · `calibrating-confidence` ·
`measuring-agreement` · `investigating-integrity-concerns` ·
`monitoring-external-feeds` · `building-review-packets` each declare
`airl.adopted_components` and carry the authority boundary in the body.

### Evidence

- `check_stale_claims.py` → **0** · `check_doc_consistency.py` → agree
- `write_status.py --check` → matches, **twice in a row**
- 25/25 tests · 52/52 skills · plan semantics OK · seal 207/207
- 5/5 figures, 0 overflow · mirror drift 0 (208 plan · 76 skill/doc/figure)

### Limits

- This step corrected **descriptions**, not capability. Nothing new runs.
- The exemption list is narrow by design and will need extending as more dated
  records accumulate; a wrong exemption hides real drift.
- Everything the previous steps could not do remains undone: no end-to-end run,
  no rendered document, no behaviour-tested skill, no accepted package.

### Next step

Unchanged: activate BVC-01, accept WP-000, run the authoring bake-off in Docker.

---

## Step 015 — Document production: a conductor, twelve reference modules, and two checkers

**Time:** 2026-08-22
**Scope:** `authoring-research-documents` skill · external systems register with
authority boundaries · specimen report · two mechanical checkers · fifth figure

### The design question, answered before writing anything

> Should `authoring-research-documents` be one large skill?

**No.** The router is **131 lines** and loads one of twelve reference modules
when its phase is reached. The handbook lives beside the skill, not inside it,
which is what progressive disclosure in the Agent Skills format is for. The main
skill is the conductor; `reporting-results`, `producing-figures`, the evidence
skills, the Zotero skills and the review skills are the orchestra.

### The principle the pipeline encodes

```
evidence → claims → structure → prose → figures → QA → render
```

Stages 0–2 finish **before a renderer is chosen**. A document whose first
decision was its template has already skipped the only stage that could have
stopped it.

And the boundary that everything else hangs from: **`quarto render` exiting zero
means the document rendered.** It says nothing about whether the document is
true, complete, venue-compliant or publishable.

### Authority boundaries, made mandatory

Every component in the register carries an explicit `authority_boundary`:

```yaml
authority_boundary:
  external_tool_may: "render a document and resolve its internal references"
  external_tool_may_not: "decide whether a claim is supported, or whether a
    document may be published"
```

**A component that cannot be given one does not enter a gate.**
`scripts/check_reporting_registry.py` enforces that the register keeps its
adoption types, sources, retrieval dates, unverified claims and rejections —
including a check that *something* is marked `UNVERIFIED`, because a register
with no unverified claim is usually one that stopped checking.

### What was honestly refused

- **No authoring backend was chosen.** Quarto, Pandoc, Typst, LaTeX, MyST, Vale
  and LanguageTool are all **absent from this environment**. The bake-off is
  specified in full — specimen contents, attempted outputs, twenty recorded
  fields, weighting — and marked **NOT RUN**. Quarto appears everywhere as a
  *provisional* default. Docker is available, so it can be run in containers.
- **Nothing was rendered.** No PDF, no DOCX. Claiming either would have been the
  overstatement this repository exists to prevent.
- **MyST's "400+ journal templates"** is recorded as **UNVERIFIED** rather than
  repeated. So are the exact JATS, MECA and CRediT standard revisions.
- **DataCite 4.7** *was* verified: released 2026-03-03, and it adds `SWHID` as a
  related-identifier type — which connects to AIRL's existing SWHID adoption.

### What actually runs

`scripts/check_document.py` — placeholders, citation resolution, cross-reference
resolution — and a **specimen technical report** built from this repository's own
two measurements, with a real bibliography of three verified references.

The specimen immediately corrected the checker twice:

| Fault found by real use | Fix |
|---|---|
| `@fig-stack.` — sentence punctuation captured into the key | strip trailing punctuation |
| every unreferenced `#sec-` label flagged | only figures, tables and equations *must* be referenced; a section anchor exists for navigation |

Then a deliberate corruption confirmed it fires: a `TODO`, an orphan figure and a
citation resolving to nothing were all caught.

**A third bug surfaced in `figure_kit`:** requesting text below the 16-unit
legibility floor failed with a confusing message. It now says plainly that the
box should widen rather than the floor lower.

### The reporting family

| Skill | Owns |
|---|---|
| `authoring-research-documents` | the pipeline, the contract, the archetypes, the packaging ladder |
| `reporting-results` | what a result permits you to say |
| `producing-figures` | figures, with the long-form methodology in a reference module |

**52 skills.**

### Boundaries recorded, not assumed

- **Docling stays off the evidence path.** General report ingestion is Docling;
  scholarly evidence is GROBID/Pub2TEI. Converging them requires measurement.
- **Better BibTeX is a projection**, not identity. Zotero 8 has native citation
  keys — check before adding a second key authority.
- **LanguageTool's public free endpoint is not used** for automated traffic; its
  own documentation asks for that.
- **A reporting guideline is a completeness standard**, and the EQUATOR family is
  primarily health research. `none_applicable` is a legitimate result.
- **ORCID, ROR and CRediT never give an agent authorship authority.** An ORCID is
  never invented; an affiliation is never rewritten by fuzzy matching.

### Evidence

- 25/25 tests · 52/52 skills · plan semantics OK · documents consistent
- **5/5 figures**, 0 overflow · seal 207/207 · mirror drift 0
- specimen resolution checks pass · reporting register auditable

### Limits

- **No renderer, so no rendered artifact.** The pipeline's second half is written
  and unexercised.
- The bake-off has no result, so the authoring stack is undecided.
- The reference modules describe QA passes whose tools are not installed.
- Nothing here made the framework produce a research document; it made the
  discipline for doing so explicit and checkable.

### Next step

Run the bake-off in Docker — it is the one blocked decision that the environment
can actually unblock — then render the specimen and inspect the artifact rather
than the source.

---

## Step 014 — The adoption matrix applied, and a second measurement

**Time:** 2026-08-22
**Scope:** component adoption taxonomy and matrix · G10 monitoring implemented ·
plan updated to adopt · ADR-003 · two reporting skills · fourth figure

### The principle this step settles

> **AETHRION should not invent its own parser, screening engine, policy language,
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

`AETHRION_COMPONENT_REUSE.md` records which running implementations each control
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
the part AETHRION actually contributes.

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
**retrofitted verification does not work.** They demonstrated it; AETHRION argued
it.

`AETHRION_RELATED_SYSTEMS.md` now states the overlap plainly, names where those
systems are ahead without qualification — end-to-end runs, measurement, an
empirical outcome, a far more mature literature subsystem — and positions AETHRION
by **scope** rather than by novelty: Science One asks whether an autonomous system
can produce verifiable papers; AETHRION asks under what governance a claim may be
believed at all.

### CoE Audit adopted as the external benchmark

The four checks — reference verification, score verification, specification
violation, method–code alignment — are adopted verbatim into G6-0 and G9. They
are concrete, published, and measure exactly what this framework claims to
enforce.

**Adopting a benchmark means agreeing to be measured by it.** AETHRION has no
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

`NOTICE` added: AETHRION proprietary, all rights reserved; the eleven vendored
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
| `aethrion_lifecycle.svg` | eleven gates × three actor classes, and the cells admitting no model | a table hides the pattern |
| `aethrion_roles.svg` | authority tiers and constraint resolution replacing headcount | a list reads as an org chart |
| `aethrion_evidence_chain.svg` | the chain, plus how much of it exists | a status table is never cross-read |

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

`docs/architecture/AETHRION_ROLES.md` — fourteen durable functions, each with its
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
them.** Sections 2–13 of `AETHRION_SKILL_LAYER.md` treated every Superpowers
skill as something to convert — §11 said literally *"`test-driven-development` →
add as `preregistration-discipline`"*. That reading was overruled in a new §14.

The evidence that it was wrong was in the repository: **all 12 engineering
skills were absent**, while AETHRION is itself built by agents. The laboratory had
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
   vendored: `using-aethrion` is the single router, and `writing-skills` is the
   AIRL adaptation covering both families.
3. **`scripts/validate_skills.py`** — a real mechanical check: format
   conformance, the AIRL metadata contract, and pinned upstream provenance.
4. **Bootstrap** — `.claude/skills → ../skills`, so the registry actually loads.
5. **`using-aethrion` became a router** across both families with the two
   classification axes (`research_mode` × `execution_path`).
6. **`docs/architecture/AETHRION_EXTERNAL_STANDARDS.md`** — an adoption register:
   what is adopted, what is deferred, and why, each with an integration point.
7. **`docs/architecture/AETHRION_ARCHITECTURE.md`** — the explanatory entry point
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

1. [[10 - Projects/AETHRION/02 - Reviews/claude_framework_audit_report|Claude Framework Audit Report]] —
   an evidence-based independent audit. 1,509 lines of Python, 20 tests, the live
   service, SQLite, Git, the vault and 186 plan files were examined.
2. [[10 - Projects/AETHRION/04 - Architecture/aethrion_ideal_structure|AETHRION Ideal Structure]] —
   the added roles, review mechanisms, the 7th plane (Metascience & Calibration),
   the role→model assignment architecture and the tool stack.
3. [[10 - Projects/AETHRION/04 - Architecture/aethrion_skill_layer|AETHRION Skill Layer]] —
   the integration of all 14 `obra/superpowers` skills into AETHRION.

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
[[10 - Projects/AETHRION/07 - Skills/skills_index|Skills Index]].

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
| Templates carried a `silbo/*` tag namespace (the project had been renamed) | ✅ `aethrion/*` (16 files) |
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

---

## 2026-08-22 — Brand migration: AETHRION, and commissioning baseline v1.0.2

### What changed

The project has an official identity: **AETHRION — Agentic Intelligence Research
Layer**. It was documented as *AIRL-OS* before today, and as the *AI Research
Framework* before that. Neither is a current name.

`AIRL` was **not** removed. It is the abbreviation of the descriptor, and it
stays wherever it names a technical thing rather than the product: the `airl.*`
skill-metadata namespace, the `airl_id` source-registry field, the `airl-bridge`
service and its two systemd units, `src/airl_bridge/` and `src/airl_framework/`,
the `AIRL_API_*` environment variables, the `X-AIRL-Token` header, the
`airl-interim-v0.1` attestation profile and the `https://airl-os.local/…`
`predicateType` inside the signed manifest. Each retention is listed with its
reason in `docs/branding.md`; none was left behind by accident.

### Scope

| Area | Change |
|---|---|
| Documentation | Brand prose migrated repository-wide; `docs/branding.md` added as the naming authority |
| Filenames | Eight `AIRL_OS_*.md` architecture documents → `AETHRION_*.md`; nine `airl_os_*.svg` figures → `aethrion_*.svg`; `skills/using-airl-os/` → `skills/using-aethrion/` |
| Figures | All nine regenerated from their generators; no SVG hand-edited |
| Logo | `docs/assets/branding/aethrion-logo.png`, committed byte-identical; one generated projection inside the vault |
| Obsidian | Project area renamed to `10 - Projects/AETHRION`; landing page rewritten; tags `ai-framework/*` → `aethrion/*`; every wikilink re-resolved |
| Plan | Re-sealed as **baseline v1.0.2** — naming only, no requirement or identifier touched |
| Repository | Directory and GitHub repository renamed to `AETHRION`; systemd units repointed |

### Why the seal was regenerated

`00_PROGRAM/09_change_and_configuration_control.md` permits exactly one reason to
re-seal: a deliberate, recorded change. This is that case. 29 plan files changed,
all of them naming, and the diff is verifiable — `git diff v1.0.1..v1.0.2 --
planning/` shows no requirement, dependency, acceptance phase, identifier or
scenario altered. Both the seal and `validate_commissioning_plan.py` pass on the
new baseline. Re-sealing to silence a failing check remains prohibited.

### What did not change

No architecture. No lifecycle definition. No plane definition. No implementation
status: WP-000 is still `TECH_COMPLETE` and not `ACCEPTED`, BVC-01 is still
staged and has never run, no skill has a behaviour baseline, and the distance
between the design and the software is exactly what it was this morning. A rename
is not progress, and this entry is not a progress entry.

### Limits and open points

- ⚠️ **The Python packages were not renamed.** `airl_bridge` and `airl_framework`
  are import paths; renaming them breaks the console script, the systemd units
  and every consumer at once. Listed as a follow-up, not performed.
- ⚠️ **The attestation profile and `predicateType` were not renamed.** Both are
  inside signed evidence; changing either invalidates a signature that currently
  verifies.
- The frozen audit of 2026-08-21 keeps its original name and now carries a
  historical-name banner. It is a record of a date, not current documentation.

### Next step

Unchanged by this entry: give the contract core at least one real production
consumer, and activate BVC-01 with a workflow-scoped token.
