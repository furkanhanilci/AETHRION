"""The execution loop must refuse the transitions the plan forbids.

These are the guarantees that make `delivery/progress.json` a ledger rather than
a file anyone can type into. Each test names the rule it defends.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "delivery" / "progress.json"


@pytest.fixture
def ledger_restored():
    backup = LEDGER.read_bytes()
    yield
    LEDGER.write_bytes(backup)
    subprocess.run([sys.executable, "scripts/ready_queue.py"], cwd=ROOT, check=True,
                   capture_output=True)


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "scripts/progress.py", *args],
                          cwd=ROOT, capture_output=True, text=True)


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
