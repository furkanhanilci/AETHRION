# Go-Live Checklist

## Mandatory entry conditions

- [ ] WP-001–119 `COMMISSIONED` in their respective states.
- [ ] ACC-01–ACC-40 PASS on the same release candidate.
- [ ] Open critical findings = 0.
- [ ] Open high findings = 0, or a time-boxed, non-waivable residual risk
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
      measured for the reviewer pool (WP-132 / `measuring-agreement`).
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
