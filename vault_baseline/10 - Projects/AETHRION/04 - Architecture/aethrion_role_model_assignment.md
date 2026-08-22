> [!info] Generated view
> This note is generated from `docs/architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# AETHRION — Role → Model Assignment Decision

| Field | Value |
|---|---|
| Document type | Architecture decision (ADR candidate) |
| Scope | Who executes each role: human / model / deterministic code |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · `AETHRION_IDEAL_STRUCTURE.md` (Section D) · `AETHRION_SKILL_LAYER.md` · `AETHRION_EXTERNAL_STANDARDS.md` |
| Date | 2026-08-22 |
| Status | **Proposal — human approval required before implementation** |

**In one paragraph.** This decision record assigns every role and every gate to an actor class — human, model, or deterministic code — and binds reviewer count and effort to the assurance class. It opens with a constraint rather than a preference: hosted models have no pinnable snapshot, so an R3 claim requires a local open-weight model or G7a reproduction is structurally impossible. The model catalogue in §2 is a dated snapshot that belongs in the WP-042 Capability Registry, not in an architecture document.

---

## 0. First: a finding that breaks the architecture

> *`AIRL-OS-Architecture.md` is a **historical name**: the v1.0 document this one was derived from, which no longer exists under that filename. Current project identity: **AETHRION**; the current architecture reference is [`AETHRION_ARCHITECTURE.md`](AETHRION_ARCHITECTURE.md). See [`../branding.md`](../branding.md).*

`AIRL-OS-Architecture.md` carries fields of this shape:

```yaml
model_profile: "Claude-Sonnet-5-Qualified-20260801"
model_snapshot: "Claude Sonnet 5 20260801"
```

**Those identifiers do not exist.** Current-generation Claude models have no
date-suffixed full identifier — the alias *is* the identity:

| Model | Identity | Date-suffixed full identity |
|---|---|---|
| Claude Fable 5 | `claude-fable-5` | **none** |
| Claude Opus 5 | `claude-opus-5` | **none** |
| Claude Opus 4.8 | `claude-opus-4-8` | **none** |
| Claude Sonnet 5 | `claude-sonnet-5` | **none** |
| Claude Haiku 4.5 | `claude-haiku-4-5` | `claude-haiku-4-5-20251001` |

> **Consequence:** for hosted Claude models, **date-based snapshot pinning is not
> possible.** The `ExperimentRun.model_snapshot` field cannot be filled for
> current-generation models.

And that breaks **Invariant 4** directly:

> *"A G7 clean-room run reproduces the result within the tolerance defined by the
> frozen manifest."*

If the frozen manifest cannot point at a model snapshot, then G7a (deterministic
reproduction) is **structurally impossible** with a hosted model. This is not a
preference; it is a constraint.

### What can be done — a three-layer substitute

| Layer | What is pinned | What it guarantees |
|---|---|---|
| **1. Capability fingerprint** | `GET /v1/models/{id}` → `max_input_tokens`, `max_tokens`, the `capabilities` tree; hashed and written into the manifest | That the model *surface* has not changed — **not that behaviour is unchanged** |
| **2. Full I/O logging** | The request body, the response, `response.model` and `usage` (via Langfuse) | What was asked and what was answered is auditable — **but not reproducible** |
| **3. Local open-weight model** | The **SHA-256** of the GGUF file plus the execution parameters — signed with `sigstore/model-transparency` / OpenSSF Model Signing | **Real determinism.** The weights are yours, and the hash is attested rather than asserted. |

> **Decision:** No run producing an `R3` claim may use a hosted model. **Layer 3
> is mandatory.** For R1/R2, layers 1+2 suffice, and the `model_snapshot` field
> must be renamed `capability_fingerprint` so it stops promising something it
> cannot deliver.

The 2× RTX A5000 (48 GB total VRAM) already available is therefore not an
optional convenience — it is **a precondition for R3**.

---

## 1. An honest definition of independence

The `Model Lineage` dimension of the `IndependenceMatrix` currently reads
*"different provider / base model / snapshot / fine-tune"*.

**The critical distinction — these tiers are not equal:**

| Distinction | Real independence value |
|---|---|
| Different tier within the same family (Sonnet 5 ↔ Opus 5) | **Low.** Shared training lineage, shared RLHF conventions, correlated errors |
| Different provider family (Anthropic ↔ OpenAI ↔ Google) | **Medium.** Still an overlapping web corpus, but a different training pipeline |
| Model judgement ↔ **mechanical verification** | **High.** The only genuinely independent axis |

> **Rule:** at `R2` and `R3` the reviewer **must** come from a different provider
> family. Opus 5 reviewing Sonnet 5 is **not** independent review; it is recorded
> as a `self_check`.

Even that rule is provisional. What is permanent is the **pairwise error
correlation measured by `measuring-agreement`** — a rule based on family names is
a proxy for the measurement, and it should be retired once the measurement exists.

---

## 2. Model pool

> **Layering, 2026-08-22.** The table below is a **dated snapshot, not
> architecture.** Prices, context windows and introductory discounts decay in
> months; the policy they serve does not. Three layers, kept apart:
>
> | Layer | Contains | Changes |
> |---|---|---|
> | **Architecture / ADR** | R1 → one qualified reviewer · R2 → different provider family · R3 → reproducibility-qualified local model | rarely, by decision |
> | **Capability Registry** (WP-042) | provider, model id, price, context, qualification status | continuously |
> | **Model Profile Snapshot** | `effective_from`, `effective_until`, evaluation digest | per qualification run |
>
> When WP-042 exists, this section becomes a pointer to it and the numbers below
> are deleted rather than maintained in two places.

Prices are per 1M tokens (input / output).

| Tier | Model | Price | Context | Why this one |
|---|---|---|---|---|
| **local** | Open-weight GGUF (local) | hardware | — | **Mandatory for R3.** The only real determinism |
| **bulk** | `claude-haiku-4-5` | $1 / $5 | 200K | High-volume screening, span extraction, calibration sets |
| **producer** | `claude-sonnet-5` | $3 / $15 | 1M | The main production tier; close to Opus on coding and agentic work |
| **producer+** | `claude-opus-5` | $5 / $25 | 1M | Hard agentic work, multi-file refactors |
| **adversarial** | `claude-fable-5` | $10 / $50 | 1M | Most capable; counter-argument and final review |
| **reviewer** | **non-Anthropic** | — | — | **Required for independence** |
| **arbiter** | A third family | — | — | Sees both sides and differs from both |

**Already available here:** Claude (this session) and Codex (used previously) —
so at least two provider families exist. Plus 48 GB VRAM for the local tier.

### Pricing notes

- Sonnet 5 carries an **introductory price of $2/$10 until 2026-08-31** — the best
  price/performance ratio available today sits here.
- **The Batch API gives a 50% discount** — calibration sets and multi-analyst runs
  are latency-insensitive; run them in batch.
- **Prompt caching** saves roughly 90%: the frozen prefix of a `ReviewPacket` is
  cache-friendly. The minimum cacheable prefix on Opus 5 is **512 tokens**
  (1024 on Opus 4.8).

### Two operational constraints

1. **Fable 5 requires 30-day retention; it cannot be used under ZDR.** If you
   need zero retention for D3/D4 data, Fable 5 is out of scope.
2. **Fable 5 and Opus 5 safety classifiers can refuse a request**
   (`stop_reason: "refusal"`, category `"cyber"` / `"bio"` and similar). If you do
   security or life-sciences research this is **an operational reality**, not an
   edge case: handle it with `fallbacks: "default"`, and **always check
   `stop_reason` before reading `content[0]`.**

---

## 3. Role → actor table

**Notation:** 👤 human · 🤖 model · ⚙️ deterministic code · ⬜ deferred

### 3.1 Durable functions

> **Role is a function, not a person.** Every row below is bound through a
> `RoleBinding` with explicit `must_be_independent_from` / `can_combine_with` /
> `cannot_combine_with` constraints. One person may hold several of these roles
> legally; independence is a property of the *separation constraints*, never of
> the headcount. See `AETHRION_ARCHITECTURE.md` §6.1 and WP-013.

| Role | Actor | Model | Note |
|---|---|---|---|
| Project Decision Owner | 👤 | — | **Never a model.** Signs G8/G9 |
| Safety / Data Owner | 👤 | — | The data-class decision stays human |
| **Research Integrity Officer** | 👤 + ⚙️ | mechanical triggers | statcheck/GRIM open cases automatically; the judgement is human |
| Scientific Owner | 👤 + 🤖 draft | `claude-opus-5` | The human writes the decision question |
| **Statistical Methods Owner** | 👤 + 🤖 | `claude-opus-5` @ `high` | The human locks the analysis plan |
| Evidence Lead | 👤 + 🤖 | `claude-sonnet-5` | The freeze decision is human |
| Engineering Owner | 🤖 + 👤 approval | `claude-opus-5` @ `xhigh` | Code production |
| Assurance Lead | 👤 + ⚙️ | — | Reviewer assignment; **not a model** |
| **Research Software Engineer** | 🤖 + 👤 approval | `claude-sonnet-5` | RO-Crate, Nix, badges |
| **Data Steward** | 🤖 + 👤 approval | `claude-sonnet-5` | Croissant, DOI |
| **Scientific Editor** | ⚙️ + 🤖 | `claude-sonnet-5` | Scope conformance is **mechanical** |
| **Red Team Lead** | 🤖 + 👤 | `claude-fable-5` @ `xhigh` | Pre-mortem, control injection |
| **Knowledge Steward** | ⚙️ + 🤖 | `claude-haiku-4-5` | Contradiction sweeps |
| **Metascience Lead** | 👤 + ⚙️ | — | Measures; **does not block** |

### 3.2 Gate → actor

| Gate | ⚙️ Mechanical | 🤖 Model | 👤 Human |
|---|---|---|---|
| **G0** Intake | duplicate search (embedding + Neo4j) | `haiku-4-5` triage | greenlight (5 min) |
| **G1** Charter | **the `RiskProfile → AssuranceClass` policy engine** | `opus-5` draft | **the decision question + approval** |
| **G2** Protocol | template completeness, placeholder sweep | `opus-5` draft · `fable-5` pre-mortem · **different-family** Stage-1 review | Scientific + Statistical Methods Owner **sign** |
| **G2b** Analysis Plan | — | `opus-5` @ `high` | **the Statistical Methods Owner locks it** |
| **G3** Literature | GROBID, DOI resolution, dedup, hashing | `sonnet-5` query plan · `haiku-4-5` screening | Evidence Lead **freezes** |
| **G4** Baseline | the baseline run | `opus-5` plan · `fable-5` pre-mortem | budget approval |
| **G5** Execute | **the experiment itself** | *(none, unless the model is the subject of the experiment)* | — |
| **G6-0** Mechanical | **statcheck, GRIM, GRIMMER, entailment, hashes** | — | — |
| **G6-1** Blind | `ReviewPacketBuilder` (**a program**) | **N reviewers, non-Anthropic** | — |
| **G6-2** Adversarial | the ACH matrix | `fable-5` @ `xhigh` | — |
| **G6-3** Disagreement | verdict comparison | Delphi rounds (same pool) | an arbiter **only if it fails to converge** |
| **G7a** Reproduction | **deterministic; NO model** | — | — |
| **G7b** Replication | distribution test | — | the RSE assigns the badge |
| **G8** Decision | package completeness | **produces a recommendation, never a decision** | **HUMAN ONLY, under quota** |
| **G9** Publish | **scope conformance**, RO-Crate, hashes | `sonnet-5` draft | Decision Owner + Editor |
| **G10** Monitor | Crossref / Retraction Watch / CVE | `haiku-4-5` triage | decides on a material signal |

### 3.3 Three invariants

1. **No agentic methodological discretion during a frozen G5 execution.** The
   subject of an experiment may itself be a model — a frozen model under test, a
   preregistered inference pipeline, an RL policy. What is forbidden is a
   research agent changing a threshold, metric, stopping point or sample mid-run
   because the result looks wrong. The model may be the instrument; it may not
   be the methodologist. This is the cleanest layer of the laboratory — protect it.
2. **The same at G7a**, more strictly: it runs the frozen manifest and reports
   what happened. It reproduces or it does not.
3. **At G8 a model produces only a recommendation.** This is already
   non-waivable ✅

---

## 4. Effort → assurance class mapping

The effort ladder (`low` → `max`) binds directly to the R classes:

| Assurance | Producer effort | Reviewer effort | Adversarial | Reviewer quota |
|---|---|---|---|---|
| **R1** | `medium` | `high` | — | 1 |
| **R2** | `high` | `high` | `xhigh` | 2, **different family** |
| **R3** | `xhigh` | `xhigh` | `max` | 3, **different family** + local reproduction |

**Note:** `low` and `medium` are stronger on current models than the names
suggest. `medium` really is sufficient for R1 — that is where your cost leverage
sits.

**Adaptive thinking:** on Opus 5 it is **on by default**. Omitting the `thinking`
field does not disable thinking. And `max_tokens` bounds thinking **and** the
answer together — a prompt arriving with a small `max_tokens` can now be cut off
mid-way.

> ⚠️ **Do not disable thinking.** `thinking: {type: "disabled"}` on Opus 5
> produces two silent failure modes: a tool call can be emitted **as plain text**
> (the call never executes and never errors), and `<thinking>` tags can leak into
> the response. To reduce cost, lower `effort` — do not disable thinking.

---

## 5. Independence quota — an enforceable rule

```yaml
independence_quota:
  R1: {reviewers: 1, family_rule: "any"}
  R2: {reviewers: 2, family_rule: "producer_family_excluded"}
  R3: {reviewers: 3, family_rule: "producer_family_excluded",
       extra: "reproduction on local open-weight"}

hard_rules:
  - the producer profile and the final reviewer profile MUST NOT be identical
  - at R2/R3 the reviewer MUST NOT be from the producer's PROVIDER FAMILY
  - two profiles whose measured pairwise error correlation ρ exceeds the
    threshold do not both count toward the same quota   # output of measuring-agreement
  - a producer may summon no agent at all                # independence-discipline
  - the adversarial reviewer's metric is the quality of its REFUTATION
```

**Advisor tool warning:** Anthropic's advisor tool pairs an executor with an
advisor — but on Opus 5 the advisor result comes back **encrypted**
(`advisor_redacted_result`) and the client cannot read it. **In a laboratory that
audits everything, an unreadable advice channel is unacceptable.** Do not use the
advisor tool anywhere in the G6 review path.

---

## 6. Cost envelope — a rough estimate

For one R2 confirmatory project (200 candidate sources → 40 included, 12
scenarios, 3 reviewers):

| Stage | Model | Estimated tokens | Approximate cost |
|---|---|---|---|
| G3 screening | `haiku-4-5` batch | ~2M input | ~$1 |
| G3 span extraction | `haiku-4-5` | ~1M | ~$1 |
| G2 protocol + analysis plan | `opus-5` @ high | ~300K | ~$5 |
| G5 analysis (multi-analyst ×3) | `sonnet-5` | ~1.5M | ~$8 |
| G6 blind review ×2 | **non-Anthropic** | ~600K | provider-dependent |
| G6 adversarial | `fable-5` @ xhigh | ~200K | ~$12 |
| G9 text + scope | `sonnet-5` | ~200K | ~$3 |
| **Total (Anthropic side)** | | | **~$30** |

Prompt caching and batching roughly halve that figure. **The real cost is not the
models — it is human decision capacity.** The attention budget — five G8
decisions per week under `attention@1.0.0`, a policy value rather than an
architectural constant — is the actual bottleneck, and no amount of model spend
relieves it.

---

## 7. Implementation order

| # | Work | What it unblocks |
|---|---|---|
| 1 | Rename `model_snapshot` → `capability_fingerprint` and snapshot `GET /v1/models` | Invariant 4 |
| 2 | Write the R3 → local open-weight requirement into an ADR, signing the weights with OMS / `model-transparency` | G7a |
| 3 | Connect at least one **non-Anthropic** provider to the reviewer pool | R2/R3 independence |
| 4 | Check `stop_reason == "refusal"` and set `fallbacks: "default"` on every call | Production resilience |
| 5 | Put the effort → R class mapping into the policy engine | Gate depth |
| 6 | Wire the Batch API into calibration sets and multi-analyst runs | Metascience cost |
| 7 | Build the `measuring-agreement` calibration set | K1 — measured independence |

---

## 8. Explicitly deferred

| Role / component | Why |
|---|---|
| Advisor tool | Encrypted result — cannot be audited |
| Fable 5 (on D3/D4 work) | 30-day retention requirement, no ZDR |
| Managed Agents | Your orchestration is Temporal; two control planes is one too many |
| A separate `arbiter` provider family | Requires access to a third family; a human arbiter serves for now |

---

## 9. The limit of this decision

This assignment rests on **an unmeasured assumption**: that the error correlation
between different provider families is lower than between tiers within one family.

That is plausible, but **it is not proven.** It will be measured once the
`measuring-agreement` calibration set exists, and this table will be revised
against that measurement.

> If a laboratory runs without measuring its own independence assumption, the
> "independent verification" it produces is the repetition of an assumption.
