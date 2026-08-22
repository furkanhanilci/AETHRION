---
title: "Wave and Dependency Map"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
source: "planning/commissioning/00_PROGRAM/02_wave_and_dependency_map.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# Wave and Dependency Map

## Principle

A wave is not a production phase. Waves describe the order in which things can
be built in parallel on development and staging. **Production opens in a single
integrated cutover.**

The distinction matters: a wave completing does not mean anything is live. It
means a defined set of integration evidence exists.

## Waves

| Wave | Objective | Package range | Exit evidence |
|---|---|---|---|
| **WB — Bootstrap** | Make acceptance possible at all: interim evidence attestation | **WP-000** | One signed, logged, verified specimen `EvidenceManifest` |
| W0 — Programme lock | Fix scope, ownership, risk and the acceptance system | WP-001–010 | Signed operating model and policy drafts |
| W1 — Contract spine | Fix identity, schema and canonical ownership | WP-011–020 | Contract compatibility and schema registry pass |
| W2 — Platform backbone | Environment, GitOps, data, event and artifact foundations | WP-021–031, WP-051, WP-055–059 | Foundation health, identity and policy smoke tests |
| W3 — Control and runtime | Run the workflow, agent, model, broker and sandbox | WP-032–060 | Replay, route, tool and sandbox tests |
| W4 — Knowledge and evidence | Literature, Source Registry, Claim Ledger, experiment and review path | WP-061–090 | Source→claim→run→review lineage pass |
| W5 — Human and visibility | Cockpit, decision queue, graphs, telemetry and FinOps | WP-091–101 | Human decision and end-to-end correlation pass |
| W6 — Vertical integration | Integrate the G0–G10 and engineering flows | WP-102–115 | Vertical slices and 51 acceptance tests |
| W7 — Commissioning | Security, resilience, DR, capacity, audit and pilot | WP-116–119 | Commissioning dossier; zero critical findings |
| W8 — Cutover | Rehearsal, production opening and hypercare | WP-120–121 | Go-live `DecisionRecord` and stabilisation |
| W9 — Day-2 | Continuous assurance and operation | WP-122–130 | Periodic control-effectiveness records |
| **W-T — Tooling** | **Notification, communication, external records, evidence sealing, liveness** | **WP-131–140** | **Broker policy tests; channel ceiling enforcement; timestamp verification by a third party** |

The tooling wave is deliberately not numbered in sequence. Several of its
packages — evidence timestamping (WP-139) and service liveness (WP-140) — are
useful from W0 onward and do not need to wait for the platform backbone.

## Critical path

```text
WP-001
  → WP-005/WP-006/WP-007
  → WP-011/WP-012
  → WP-020
  → WP-021/WP-025/WP-026/WP-028/WP-031/WP-051/WP-056/WP-058
  → WP-032/WP-035/WP-047/WP-049/WP-062/WP-077
  → WP-102..WP-106
  → WP-115
  → WP-116..WP-119
  → WP-120
```

## Safe parallelisation clusters

- In W0, WP-003, WP-005, WP-006 and WP-007 can proceed in parallel once WP-001
  locks scope.
- In W1, once the identifier standard is ready, the event, artifact, source,
  claim and decision schemas can be produced by separate teams in parallel;
  WP-020 unifies them.
- In W2, Postgres, object store, NATS, MLflow and derived indexes can be built in
  parallel by separate platform owners.
- In W3, the control plane, model/agent and execution/security tracks proceed in
  parallel through their contracts.
- In W4, literature and evidence teams can work in parallel once the
  `SourceRecord`/`SourceRepresentation` interface is fixed.
- In W5, work can start against mock contracts without waiting for backend
  completion; commissioning happens against real services.

## Work that must not be parallelised

- Producing two independent versions of the same canonical schema.
- Writing OPA rules and UI explanations under different interpretations before
  policy semantics are fixed.
- Routing reviewers before the review independence contract is closed.
- Enabling Zotero write-back on production-like data before the source
  identity/dedup rule is closed.
- Declaring clean-room reproduction before immutable artifacts and `RunManifest`
  exist.
- Running a cutover rehearsal without restore evidence.

## Dependency change rule

When a package discovers a new hard dependency, the catalogue is updated, the
affected `READY` packages are re-evaluated, and a programme event is emitted.
A dependency is never skipped under schedule pressure; only an explicit temporary
control with an expiry date permits a staging experiment.
