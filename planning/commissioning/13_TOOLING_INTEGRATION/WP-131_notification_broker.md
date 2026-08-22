# WP-131 — Notification Broker Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-131` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Security Lead |
| Independent verifier | Safety & Governance Owner |
| Hard dependencies | WP-049 (Tool Registry/Broker), WP-016 (PolicyDecision schemas) |
| Related gates | Platform |
| Related controls | CTL-SEC-04, CTL-DAT-02 |
| Related acceptance scenarios | ACC-41, ACC-42 |
| Related skill | `notifying-humans` |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A **subclass of the Tool Broker** is built so that agents can reach humans. The
agent produces a notification **intent**; only the broker performs the send.

> **Invariant:** An agent never sends a message directly. Every send passes
> through the chain identity → policy → data class → DLP → idempotency →
> transmission → `NotificationReceipt`.

Notification is a `T3` side-effect class (it mutates an external system) and
therefore requires an **explicit egress exception** against the default-deny
network policy of the `ExecutionProfile`.

The reason for the indirection is not ceremony. A message that has left the
system cannot be recalled. Every check that matters must therefore happen
*before* transmission, at a single point that can be audited — which is exactly
what a broker is.

## Out of scope

- Per-channel connector implementation (WP-132)
- Inbound message handling (WP-136)
- Decision authorisation (WP-135)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-049 (Tool Registry/Broker), WP-016 (PolicyDecision schemas)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-131-T01 | Define the broker interface and the `NotificationIntent` schema | Schema file + contract test |
| WP-131-T02 | Build the policy check chain (identity, `TaskContract`, data class) | A negative test for every step of the chain |
| WP-131-T03 | Idempotency key generation and duplicate-send prevention | A second call with the same key performs no send |
| WP-131-T04 | Emit `NotificationReceipt` and `ToolReceipt` | A record for every send; a send without a record is impossible |
| WP-131-T05 | Rate limiting and quiet-hours policy | Over threshold the send is deferred, never dropped |
| WP-131-T06 | Place a transport abstraction (Apprise or equivalent) behind the interface | Changing channel does not change the broker contract |

## Mandatory deliverables

- The `NotificationBroker` service interface and implementation
- The `NotificationIntent` and `NotificationReceipt` schemas
- The policy chain and the idempotency ledger
- The egress allowlist definition
- An updated runbook and the service ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- **An agent cannot send directly:** a send attempted outside the broker is rejected
- **Idempotency:** two calls with the same key → one send, two receipts sharing one `sent_id`
- **Timeout behaviour:** no blind retry when no response arrives; the state is queried instead
- **Rate limit:** over threshold the message queues rather than being silently dropped
- Negative tests for unauthorised, missing, duplicate and partial-failure inputs

## Acceptance criteria

- [ ] No send originating outside the broker can succeed (static **and** runtime checks)
- [ ] Every send produces exactly one `NotificationReceipt`; there is no send without a receipt
- [ ] N calls with the same idempotency key → exactly 1 send
- [ ] Automatic re-sends after a timeout number **zero**
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- When the broker is down, notifications are **not silently lost**; they queue and the queue depth is monitored
- Extending the egress allowlist requires Safety/Data Owner approval
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The broker is disabled; pending notifications stay in the queue and are sent in
order on re-enable. A notification that has already been sent cannot be recalled
— which is precisely why the pre-send checks are non-waivable.

## Handoff into downstream packages

WP-132 builds the channel registry, WP-133 the outbound flows, WP-134 escalation
and WP-135 decision routing on top of this broker. None of them starts without it.
