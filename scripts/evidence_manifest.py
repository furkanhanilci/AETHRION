#!/usr/bin/env python3
"""Issue and verify `EvidenceManifest` attestations — the WP-000 interim profile.

Responsibility
    Make a work package's evidence **tamper-evident** without waiting for the
    permanent content-addressed store (WP-026). A manifest is expressed as an
    in-toto Statement, wrapped in a DSSE envelope, signed, and anchored in time.

Invariant
    Verification fails when anything the manifest covers changes: the payload,
    a subject digest, or the signature. The tamper case is not a comment in a
    document — it is exercised by ``--tamper-demo`` and by the test suite.

What this is, precisely
    This is the **interim profile** defined by WP-000, and it is deliberately
    narrower than the target:

    ==============  ==========================  ============================
    Layer           Target (WP-000 §"format")   Implemented here
    ==============  ==========================  ============================
    Statement       in-toto Statement (ITE-6)   in-toto Statement ✅
    Envelope        DSSE                        DSSE ✅
    Signature       Sigstore, keyless OIDC      **local Ed25519 key**
    Transparency    Rekor inclusion proof       **not submitted**
    Time anchor     WP-139 (OpenTimestamps)     **WP-000's own interim anchor**
    ==============  ==========================  ============================

    Keyless signing needs an interactive OIDC flow and a network path this
    environment does not have. Claiming a Rekor entry that does not exist would
    be exactly the overstatement this repository is built to prevent, so the
    manifest records its own profile in ``attestation_profile`` and verification
    reports what is *not* covered.

Audit findings
    Addresses the storage half of **C1**. Does **not** address **C2**: this tool
    produces evidence, and evidence is not acceptance. Who may verify is decided
    in ADR-001, not here.

Usage
    python3 scripts/evidence_manifest.py issue  --package WP-000 --gate Program \\
        --subject README.md --subject planning/commissioning/00_PROGRAM/SHA256SUMS.txt
    python3 scripts/evidence_manifest.py verify --manifest delivery/WP-000/evidence.dsse.json
    python3 scripts/evidence_manifest.py verify --manifest ... --tamper-demo
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey)

ROOT = Path(__file__).resolve().parent.parent
KEY_DIR = ROOT / "delivery" / "_keys"
PREDICATE_TYPE = "https://airl-os.local/EvidenceManifest/v0.1"
PAYLOAD_TYPE = "application/vnd.in-toto+json"
PROFILE = "airl-interim-v0.1"


# ---- digests ---------------------------------------------------------------
def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical(obj) -> bytes:
    """Deterministic JSON: the signature must not depend on key ordering."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


# ---- DSSE ------------------------------------------------------------------
def pae(payload_type: str, payload: bytes) -> bytes:
    """DSSE Pre-Authentication Encoding — binds the type to the payload."""
    return b"DSSEv1 %d %s %d %s" % (
        len(payload_type), payload_type.encode(), len(payload), payload)


def load_or_create_key() -> Ed25519PrivateKey:
    KEY_DIR.mkdir(parents=True, exist_ok=True)
    private_path, public_path = KEY_DIR / "airl-interim.ed25519", KEY_DIR / "airl-interim.pub"
    if private_path.exists():
        return serialization.load_pem_private_key(private_path.read_bytes(), password=None)
    key = Ed25519PrivateKey.generate()
    private_path.write_bytes(key.private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()))
    private_path.chmod(0o600)
    public_path.write_bytes(key.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    print(f"generated interim signing key at {private_path.relative_to(ROOT)}")
    return key


# ---- interim time anchor ---------------------------------------------------
def interim_anchor(envelope_digest: str) -> dict:
    """WP-000 owns its own anchor; WP-139 takes ownership later.

    The anchor binds the envelope digest to two things the issuer does not
    control: the wall clock, and the repository's own commit history. It is
    weaker than an external timestamp authority and says so.
    """
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        head = "unavailable"
    return {
        "anchor_type": "interim/local",
        "owned_by": "WP-000",
        "successor": "WP-139 assumes ownership of timestamping",
        "issued_at": datetime.now(timezone.utc).isoformat(),
        "repository_head": head,
        "envelope_sha256": envelope_digest,
        "limitation": "no external timestamp authority; strength is bounded by the issuer's clock "
                      "and by the commit this anchor names",
    }


# ---- issue -----------------------------------------------------------------
def issue(args: argparse.Namespace) -> int:
    subjects = []
    for rel in args.subject:
        path = (ROOT / rel).resolve()
        if not path.is_file():
            print(f"subject not found: {rel}", file=sys.stderr)
            return 1
        subjects.append({"name": rel, "digest": {"sha256": sha256_file(path)}})

    statement = {
        "_type": "https://in-toto.io/Statement/v1",
        "subject": subjects,
        "predicateType": PREDICATE_TYPE,
        "predicate": {
            "attestation_profile": PROFILE,
            "work_package": args.package,
            "gate": args.gate,
            "target_revision": interim_anchor("")["repository_head"],
            "checks": args.check,
            "verifier": {"identity": args.verifier, "decision": "PENDING",
                         "note": "issuance is not acceptance; see ADR-001"},
            "findings_open": [],
            "limitations": [
                "signed with a local Ed25519 key, not Sigstore keyless",
                "not submitted to a transparency log",
                "time anchor is WP-000's interim anchor, not WP-139",
            ],
        },
    }
    payload = canonical(statement)
    key = load_or_create_key()
    signature = key.sign(pae(PAYLOAD_TYPE, payload))
    envelope = {
        "payloadType": PAYLOAD_TYPE,
        "payload": base64.b64encode(payload).decode(),
        "signatures": [{"keyid": hashlib.sha256(
            key.public_key().public_bytes(
                serialization.Encoding.Raw, serialization.PublicFormat.Raw)).hexdigest()[:16],
            "sig": base64.b64encode(signature).decode()}],
    }
    out_dir = ROOT / "delivery" / args.package
    out_dir.mkdir(parents=True, exist_ok=True)
    envelope_path = out_dir / "evidence.dsse.json"
    envelope_path.write_text(json.dumps(envelope, indent=2) + "\n")
    anchor = interim_anchor(hashlib.sha256(canonical(envelope)).hexdigest())
    (out_dir / "evidence.anchor.json").write_text(json.dumps(anchor, indent=2) + "\n")

    print(f"issued  {envelope_path.relative_to(ROOT)}")
    print(f"anchor  {(out_dir / 'evidence.anchor.json').relative_to(ROOT)}")
    print(f"subjects: {len(subjects)} · profile: {PROFILE}")
    return 0


# ---- verify ----------------------------------------------------------------
def _verify_envelope(envelope: dict, public_key: Ed25519PublicKey) -> tuple[bool, dict | None]:
    try:
        payload = base64.b64decode(envelope["payload"])
        signature = base64.b64decode(envelope["signatures"][0]["sig"])
        public_key.verify(signature, pae(envelope["payloadType"], payload))
        return True, json.loads(payload)
    except (InvalidSignature, KeyError, ValueError):
        return False, None


def verify(args: argparse.Namespace) -> int:
    envelope_path = (ROOT / args.manifest).resolve()
    envelope = json.loads(envelope_path.read_text())
    public_key = serialization.load_pem_public_key((KEY_DIR / "airl-interim.pub").read_bytes())

    ok, statement = _verify_envelope(envelope, public_key)
    print(f"signature           {'OK' if ok else 'FAIL'}")
    if not ok:
        return 1

    all_match = True
    for subject in statement["subject"]:
        path = ROOT / subject["name"]
        actual = sha256_file(path) if path.is_file() else None
        match = actual == subject["digest"]["sha256"]
        all_match &= match
        print(f"subject digest      {'OK  ' if match else 'FAIL'} {subject['name']}")

    anchor_path = envelope_path.parent / "evidence.anchor.json"
    anchor_ok = False
    if anchor_path.is_file():
        anchor = json.loads(anchor_path.read_text())
        anchor_ok = anchor["envelope_sha256"] == hashlib.sha256(canonical(envelope)).hexdigest()
        print(f"time anchor         {'OK' if anchor_ok else 'FAIL'}  ({anchor['anchor_type']})")

    print(f"profile             {statement['predicate']['attestation_profile']}")
    print("not covered         transparency log · keyless identity · external timestamp authority")

    if args.tamper_demo:
        print("\n-- tamper demonstration --")
        tampered = json.loads(json.dumps(envelope))
        payload = json.loads(base64.b64decode(tampered["payload"]))
        payload["predicate"]["findings_open"] = []
        payload["predicate"]["work_package"] = "WP-999"
        tampered["payload"] = base64.b64encode(canonical(payload)).decode()
        ok_t, _ = _verify_envelope(tampered, public_key)
        print(f"payload altered     {'FAIL — VERIFICATION BROKEN' if ok_t else 'rejected, as required'}")
        if ok_t:
            return 1

    return 0 if (all_match and anchor_ok) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_issue = sub.add_parser("issue")
    p_issue.add_argument("--package", required=True)
    p_issue.add_argument("--gate", default="Program")
    p_issue.add_argument("--subject", action="append", required=True)
    p_issue.add_argument("--check", action="append", default=[])
    p_issue.add_argument("--verifier", default="unassigned — see ADR-001")
    p_issue.set_defaults(func=issue)

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("--manifest", required=True)
    p_verify.add_argument("--tamper-demo", action="store_true")
    p_verify.set_defaults(func=verify)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
