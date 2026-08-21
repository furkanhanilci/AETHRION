from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Any, Mapping


_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]{2,127}$")
_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


def _required(value: str, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()


def _identity(value: str, field: str) -> str:
    value = _required(value, field)
    if not _ID_RE.fullmatch(value):
        raise ValueError(f"{field} must be an uppercase stable identifier")
    return value


class Identity:
    """Stable correlation identity carried across every framework plane."""

    FIELDS = (
        "project_id", "workflow_id", "gate_id", "task_id", "actor_id",
        "source_id", "representation_id", "claim_id", "evidence_id",
        "run_id", "artifact_id", "review_id", "decision_id", "cost_id",
    )

    def __init__(self, **values: str | None):
        unknown = set(values) - set(self.FIELDS)
        if unknown:
            raise ValueError(f"unknown identity fields: {sorted(unknown)}")
        self.values = {
            field: (_identity(value, field) if value is not None else None)
            for field, value in values.items()
        }

    def as_dict(self) -> dict[str, str]:
        return {key: value for key, value in self.values.items() if value is not None}

    def correlation_key(self) -> str:
        payload = json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode()).hexdigest()


class ArtifactManifest:
    """Immutable bytes manifest with explicit lineage and validity."""

    def __init__(
        self,
        *,
        artifact_id: str,
        media_type: str,
        sha256: str,
        size_bytes: int,
        producer: str,
        source_revision: str,
        validity: str = "VALID",
        parents: tuple[str, ...] = (),
    ):
        self.artifact_id = _identity(artifact_id, "artifact_id")
        self.media_type = _required(media_type, "media_type")
        if not _HASH_RE.fullmatch(sha256):
            raise ValueError("sha256 must be a lowercase SHA-256 digest")
        if not isinstance(size_bytes, int) or size_bytes < 0:
            raise ValueError("size_bytes must be a non-negative integer")
        self.sha256 = sha256
        self.size_bytes = size_bytes
        self.producer = _identity(producer, "producer")
        self.source_revision = _required(source_revision, "source_revision")
        if validity not in {"VALID", "SUPERSEDED", "REVOKED", "QUARANTINED"}:
            raise ValueError("invalid artifact validity")
        self.validity = validity
        self.parents = tuple(_identity(parent, "parent") for parent in parents)

    def as_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "media_type": self.media_type,
            "sha256": self.sha256,
            "size_bytes": self.size_bytes,
            "producer": self.producer,
            "source_revision": self.source_revision,
            "validity": self.validity,
            "parents": list(self.parents),
        }


class EventEnvelope:
    """Versioned event contract; payload is referenced, not silently embedded."""

    def __init__(
        self,
        *,
        event_id: str,
        event_type: str,
        schema_version: str,
        actor_id: str,
        subject: Identity,
        payload_ref: str,
        causation_id: str | None = None,
        correlation_id: str | None = None,
        data_class: str = "INTERNAL",
    ):
        self.event_id = _identity(event_id, "event_id")
        self.event_type = _required(event_type, "event_type")
        self.schema_version = _required(schema_version, "schema_version")
        self.actor_id = _identity(actor_id, "actor_id")
        self.subject = subject
        self.payload_ref = _required(payload_ref, "payload_ref")
        self.causation_id = causation_id
        self.correlation_id = correlation_id or subject.correlation_key()
        if data_class not in {"PUBLIC", "INTERNAL", "CONFIDENTIAL", "RESTRICTED"}:
            raise ValueError("invalid data_class")
        self.data_class = data_class
        self.occurred_at = datetime.now(timezone.utc).isoformat()

    def as_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "schema_version": self.schema_version,
            "actor_id": self.actor_id,
            "subject": self.subject.as_dict(),
            "payload_ref": self.payload_ref,
            "causation_id": self.causation_id,
            "correlation_id": self.correlation_id,
            "data_class": self.data_class,
            "occurred_at": self.occurred_at,
        }


class SchemaRegistry:
    """Small in-process registry enforcing explicit version compatibility."""

    def __init__(self):
        self._schemas: dict[str, dict[str, Any]] = {}

    def register(self, name: str, version: str, schema: Mapping[str, Any]) -> None:
        name, version = _required(name, "name"), _required(version, "version")
        key = f"{name}:{version}"
        if key in self._schemas and self._schemas[key] != dict(schema):
            raise ValueError(f"schema redefinition is forbidden: {key}")
        self._schemas[key] = dict(schema)

    def get(self, name: str, version: str) -> dict[str, Any]:
        key = f"{_required(name, 'name')}:{_required(version, 'version')}"
        try:
            return dict(self._schemas[key])
        except KeyError as exc:
            raise KeyError(f"schema is not registered: {key}") from exc

    def compatible(self, name: str, producer_version: str, consumer_version: str) -> bool:
        if producer_version == consumer_version:
            self.get(name, producer_version)
            return True
        # Major-version changes are breaking; minor/patch upgrades are compatible
        # only when both versions have been explicitly registered.
        p_major = producer_version.split(".", 1)[0]
        c_major = consumer_version.split(".", 1)[0]
        self.get(name, producer_version)
        self.get(name, consumer_version)
        return p_major == c_major
