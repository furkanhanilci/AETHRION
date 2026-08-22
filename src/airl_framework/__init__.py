"""Shared AETHRION contracts — the first foundation slice.

Exposes the canonical contract surface: :class:`Identity`,
:class:`ArtifactManifest`, :class:`EventEnvelope` and :class:`SchemaRegistry`.

⚠️ This package currently has **no production consumer** (audit finding **H4**).
See :mod:`airl_framework.contracts` for what that means and what binding it
would require.
"""

from .contracts import (
    ArtifactManifest,
    EventEnvelope,
    Identity,
    SchemaRegistry,
)

__all__ = ["ArtifactManifest", "EventEnvelope", "Identity", "SchemaRegistry"]
