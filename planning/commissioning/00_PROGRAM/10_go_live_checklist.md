# Go-Live Checklist

## Mandatory entry conditions

- [ ] WP-001–119 `COMMISSIONED` in their respective states.
- [ ] **WP-141–147 `COMMISSIONED`.** The scientific-intelligence packages are
      pre-go-live, not Day-2. They are what the ACC-52–80 scenarios exercise, and
      a cutover with those scenarios unpassed would open production on a system
      whose epistemic controls have never refused anything.
- [ ] **WP-148–159 `COMMISSIONED`.** The reliability packages are pre-go-live for
      the same reason: they are what ACC-081–120 exercise, and a cohort whose
      collaboration controls have never been injected with a faulty agent has not
      been shown to have any.
- [ ] Every `PRE_GO_LIVE` acceptance scenario PASSes on the same release candidate.
- [ ] Every `DAY2_CONTINUOUS` scenario is **armed and scheduled**, not passed — a Day-2
      rhythm cannot be a precondition of the go-live that precedes it.
- [ ] Open critical findings = 0.
- [ ] Open high findings = 0, or a time-boxed, **waivable** residual risk
      accepted by the Commissioning Board.
- [ ] Two independent restore rehearsals completed; RPO 0 for workflow state and
      the restore RTO target met.
- [ ] Temporal replay and open-workflow versioning tests passed.
- [ ] NATS duplicate/replay/DLQ and transactional outbox tests passed.
- [ ] Sandbox escape, default-deny egress, secret exfiltration and D3/D4 route
      negative tests passed.
- [ ] Source Registry ↔ Zotero full resync produced no duplicates or overwrites.
- [ ] Critical claim lineage and `LiteratureSetManifest` completeness at 100%.
- [ ] Critical workflow clean-room reproduction within the defined tolerance.
- [ ] Model admission, fallback, no-eligible-route and revoke/impact tests passed.
- [ ] Budget 80% and hard-stop behaviour tested.
- [ ] Audit export verified the policy, model, tool, source, claim, run, cost and
      decision chain.
- [ ] On-call, incident commander, break-glass and escalation lists current.
- [ ] Capacity/load test results meet the approved workload envelope.
- [ ] Runbooks applied in staging and signed by their owner.
- [ ] Cutover rehearsal successful using the same procedure.
- [ ] Rollback/abort thresholds and decision owners are explicit.

## Additional conditions from the audit

- [ ] **Interim evidence policy in place** — packages can actually reach
      `ACCEPTED` (WP-000).
- [ ] **Independence measured, not assumed** — pairwise error correlation
      measured for the reviewer pool (WP-043 initial qualification / `measuring-agreement`;
      WP-126 owns the recurring recalibration in Day-2).
- [ ] **Confidence scores calibrated** or displayed as `UNCALIBRATED`.
- [ ] **Control injection running** — the lab's false positive and false negative
      rates are known numbers.
- [ ] **Notification and escalation path tested** — a human is actually reached
      when something fails.
- [ ] **Periodic job liveness monitored** — silent stoppage is detected within
      hours (WP-140).
- [ ] **Evidence externally time-anchored** — manifests verifiable without
      trusting this repository (WP-139).
- [ ] **R3 model policy settled** — deterministic reproduction is achievable for
      every R3 claim.
- [ ] **Human attention quota defined** and its telemetry running.

## Additional conditions from baseline v1.2.0

Each of these is a control that this baseline added because the earlier one could
have been completed in full without it ever being exercised.

- [ ] **No prose without a claim, no number without a `VerifiedValue`** — the
      publication compiler has refused a planted claimless sentence and a planted
      ungrounded figure, and has **passed** the declared-rounding and
      editorial-text controls (ACC-52, ACC-53).
- [ ] **The evaluator boundary has been attacked and held** — a candidate could
      reach neither the evaluator source nor the hidden material by any route in
      the supported threat model, and every attempt is in the audit trail
      (ACC-54, ACC-55).
- [ ] **A confirmatory claim has been refused** on a plan sealed after its first
      outcome, and the claim ceiling has been shown to lower by record and never
      to rise (ACC-56).
- [ ] **An implementation failure has been shown not to refute a hypothesis** —
      compile, data and valid-null cases classified differently on the same run
      (ACC-64).
- [ ] **A reproduction has run with no agent present**, from a declared package,
      in an environment with no lineage to the producer's (ACC-65, ACC-66).
- [ ] **Every V2 verifier in the required path carries a current qualification**
      for its task type at its threshold, and an unqualified one produces
      `INCONCLUSIVE` rather than a verdict (ACC-61).
- [ ] **Every critical detector has fired on a planted control** in the same run
      that reported its clean result. A silent detector fails this line.
- [ ] **Upstream lineage is complete** — every adapted file registered, licences
      read at the source, and `check_upstream_lineage.py --self-test` reporting
      zero silent controls (ACC-73, ACC-74).

## Additional conditions from baseline v1.3.0

The reliability layer's own hard-zero conditions. Each is a count that must be
zero on the release candidate, not a control that must exist.

- [ ] **Single-agent downgrades of substantial work: 0.** A cohort that was
      silently reduced is a cohort that was never there — ACC-081.
- [ ] **Unresolved material challenges silently dropped: 0.** Convergence closed
      over an unanswered objection is the failure the cohort was convened to
      prevent — ACC-090.
- [ ] **Blockers or non-waivable safety messages suppressed by any optimiser: 0**
      — ACC-088.
- [ ] **Assurance routes lowered by budget or queue pressure: 0** — ACC-108.
- [ ] **Unapproved `SCIENTIFIC_MAJOR` deviations carried into a confirmatory
      package: 0** — ACC-104.
- [ ] **Model invocations contributing to a published result without a complete
      execution fingerprint: 0** — ACC-115.
- [ ] **Benchmark scores reported clean from a run that reached benchmark
      material: 0** — ACC-118.
- [ ] **Silent divergences in the split-brain injection suite: 0**, and every
      derived projection rebuilt losslessly — ACC-119.
- [ ] **A `HumanPreliminaryAssessment` exists for every G8 decision**, sealed
      before its recommendation was reachable through any interface — ACC-110.
- [ ] **Coordination overhead measured against the runnable naive
      fully-connected baseline**, with the quality delta inside the declared
      tolerance and the frontier published — ACC-086.

> **The performance figures are targets, not constants.** A communication
> reduction goal against the fully-connected baseline, and a quality-loss ceiling,
> are release targets to be frozen **after** calibration with confidence
> intervals — not numbers carried over from a paper about a different system.

## Cutover decision

The go-live meeting is not a presentation sign-off. The test, open risk, restore,
capacity, security and assurance evidence inside the Commissioning Dossier is
reviewed. The decision record carries:

- the release candidate digest;
- the policy, schema, model and tool bundle versions;
- the acceptance scenarios passed and their evidence references;
- residual risks with owners and expiry dates;
- the cutover window and the abort authority;
- the rollback point and its verification queries;
- the hypercare duration and its exit criteria.

If any non-waivable blocker is discovered during the meeting the outcome is
`BLOCKED`. There is no conditional production opening.
