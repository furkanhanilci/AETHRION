"""The execution loop must refuse the transitions the plan forbids.

These are the guarantees that make `delivery/progress.json` a ledger rather than
a file anyone can type into. Each test names the rule it defends.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PRODUCTION_LEDGER = ROOT / "delivery" / "progress.json"

# Every test in this file runs against a **copy**. It did not: `start WP-011` was
# run against the production ledger, and a run that did not reach its restore
# left WP-011 `IN_PROGRESS` for good — after which this suite failed on every
# subsequent run and `docs/READY.md` was wrong about the whole programme. A test
# that can corrupt the state it is testing is not isolated, whatever it asserts.
LEDGER: Path


@pytest.fixture(autouse=True)
def isolated_ledger(tmp_path, monkeypatch):
    global LEDGER
    copy = tmp_path / "progress.json"
    copy.write_bytes(PRODUCTION_LEDGER.read_bytes())
    monkeypatch.setenv("AIRL_PROGRESS_LEDGER", str(copy))
    LEDGER = copy
    yield copy
    assert PRODUCTION_LEDGER.read_bytes() == ORIGINAL_LEDGER, (
        "a test mutated the production ledger")
    assert PRODUCTION_READY.read_bytes() == ORIGINAL_READY, (
        "a test rewrote docs/READY.md — the generated queue must follow its ledger")


ORIGINAL_LEDGER = PRODUCTION_LEDGER.read_bytes()
PRODUCTION_READY = ROOT / "docs" / "READY.md"
ORIGINAL_READY = PRODUCTION_READY.read_bytes()


@pytest.fixture
def ledger_restored():
    """Retained for the tests that name it; isolation is now automatic."""
    yield


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "scripts/progress.py", *args],
                          cwd=ROOT, capture_output=True, text=True,
                          env={**os.environ, "AIRL_PROGRESS_LEDGER": str(LEDGER)})


def set_state(pid: str, state: str) -> None:
    data = json.loads(LEDGER.read_text())
    data["packages"][pid]["state"] = state
    LEDGER.write_text(json.dumps(data, indent=2) + "\n")


def test_t0_state_is_one_ready_one_in_flight_none_accepted() -> None:
    data = json.loads(LEDGER.read_text())["packages"]
    assert data["WP-000"]["state"] == "TECH_COMPLETE"
    assert data["WP-001"]["state"] == "NOT_STARTED"
    assert not [p for p, v in data.items() if v["state"] == "ACCEPTED"]


def test_cannot_start_a_package_with_unaccepted_dependencies() -> None:
    result = run("start", "WP-011")           # depends on WP-010, NOT_STARTED
    assert result.returncode == 2
    assert "Definition of Ready" in result.stderr


def test_cannot_reach_tech_complete_without_verifying_evidence(ledger_restored) -> None:
    assert run("start", "WP-001").returncode == 0
    result = run("tech-complete", "WP-001")
    assert result.returncode == 2
    assert "evidence manifest" in result.stderr


def test_cannot_accept_before_tech_complete(ledger_restored) -> None:
    assert run("start", "WP-001").returncode == 0
    result = run("accept", "WP-001", "--verifier", "Someone", "--assurance", "R1")
    assert result.returncode == 2
    assert "issuance is not acceptance" in result.stderr


def test_r3_acceptance_is_blocked_by_adr_001(ledger_restored) -> None:
    set_state("WP-001", "TECH_COMPLETE")
    result = run("accept", "WP-001", "--verifier", "Someone", "--assurance", "R3")
    assert result.returncode == 2
    assert "ADR-001" in result.stderr


def test_producer_may_not_verify_its_own_work(ledger_restored) -> None:
    set_state("WP-001", "TECH_COMPLETE")
    result = run("accept", "WP-001", "--verifier", "Executive Sponsor", "--assurance", "R1")
    assert result.returncode == 2
    assert "may not verify its own work" in result.stderr


def test_r2_acceptance_records_the_partial_independence_declaration(ledger_restored) -> None:
    set_state("WP-001", "TECH_COMPLETE")
    assert run("accept", "WP-001", "--verifier", "Internal Audit",
               "--assurance", "R2").returncode == 0
    entry = json.loads(LEDGER.read_text())["packages"]["WP-001"]
    assert entry["state"] == "ACCEPTED"
    assert "DECLARED PARTIAL" in entry["note"]
