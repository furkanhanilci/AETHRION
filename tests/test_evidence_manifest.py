"""Tests for the WP-000 interim evidence attestation tooling.

The point of an `EvidenceManifest` is that changing what it covers breaks
verification. These tests exercise exactly that, because a tamper-evidence claim
that is never tested is a claim, not a control.
"""
from __future__ import annotations

import base64
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "scripts" / "evidence_manifest.py"


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TOOL), *args],
                          cwd=ROOT, capture_output=True, text=True)


@pytest.fixture(scope="module")
def specimen(tmp_path_factory) -> Path:
    covered = ROOT / "delivery" / "README.md"
    result = run("issue", "--package", "WP-TEST", "--gate", "Program",
                 "--subject", str(covered.relative_to(ROOT)))
    assert result.returncode == 0, result.stderr
    manifest = ROOT / "delivery" / "WP-TEST" / "evidence.dsse.json"
    yield manifest
    # The fixture writes into the delivery tree; leaving it behind would put a
    # test artifact in the evidence directory, where a reader would reasonably
    # take it for a real package.
    shutil.rmtree(manifest.parent, ignore_errors=True)


def test_issued_manifest_verifies(specimen: Path) -> None:
    result = run("verify", "--manifest", str(specimen.relative_to(ROOT)))
    assert result.returncode == 0
    assert "signature           OK" in result.stdout


def test_tamper_demo_rejects_an_altered_payload(specimen: Path) -> None:
    result = run("verify", "--manifest", str(specimen.relative_to(ROOT)), "--tamper-demo")
    assert result.returncode == 0
    assert "rejected, as required" in result.stdout


def test_altered_subject_fails_verification(specimen: Path) -> None:
    covered = ROOT / "delivery" / "README.md"
    original = covered.read_bytes()
    try:
        covered.write_bytes(original + b"\n<!-- tampered -->\n")
        result = run("verify", "--manifest", str(specimen.relative_to(ROOT)))
        assert result.returncode == 1
        assert "subject digest      FAIL" in result.stdout
    finally:
        covered.write_bytes(original)


def test_broken_signature_fails_verification(specimen: Path) -> None:
    envelope = json.loads(specimen.read_text())
    original = specimen.read_text()
    try:
        forged = base64.b64encode(b"\x00" * 64).decode()
        envelope["signatures"][0]["sig"] = forged
        specimen.write_text(json.dumps(envelope))
        result = run("verify", "--manifest", str(specimen.relative_to(ROOT)))
        assert result.returncode == 1
        assert "signature           FAIL" in result.stdout
    finally:
        specimen.write_text(original)


def test_manifest_declares_its_own_limitations(specimen: Path) -> None:
    envelope = json.loads(specimen.read_text())
    statement = json.loads(base64.b64decode(envelope["payload"]))
    limitations = statement["predicate"]["limitations"]
    assert any("transparency log" in item for item in limitations)
    assert statement["predicate"]["attestation_profile"] == "airl-interim-v0.1"
    assert statement["predicate"]["verifier"]["decision"] == "PENDING"
