# Measurements

Empirical results produced by this repository about itself. Each is a real run
against real data, recorded whatever it said.

| Measurement | File | Result |
|---|---|---|
| Reference verification — CoE Audit check 1 | `reference_verification.json` | **81.8 %** corroborated (27/33 sources) |

Reproduce:

```bash
uv run python scripts/verify_references.py --report delivery/measurements/reference_verification.json
```

> These are measurements of the **registry**, not of generated research. AIRL-OS
> has produced no research artifacts, so it has no score on the other three CoE
> Audit checks. Presenting the number above as comparable to a
> hallucinated-reference rate measured on generated bibliographies would be a
> category error — see `docs/architecture/AIRL_OS_COMPONENT_REUSE.md` §2.
