import unittest

from airl_framework.contracts import ArtifactManifest, EventEnvelope, Identity, SchemaRegistry


class ContractTests(unittest.TestCase):
    def test_identity_correlation_is_stable_and_rejects_unknown_fields(self):
        first = Identity(project_id="PROJECT-001", run_id="RUN-001")
        second = Identity(run_id="RUN-001", project_id="PROJECT-001")
        self.assertEqual(first.correlation_key(), second.correlation_key())
        with self.assertRaises(ValueError):
            Identity(project_id="project-lowercase")

    def test_artifact_manifest_requires_digest_and_supports_supersession(self):
        manifest = ArtifactManifest(
            artifact_id="ARTIFACT-001", media_type="application/json", sha256="a" * 64,
            size_bytes=3, producer="SERVICE-001", source_revision="git:abc",
            validity="SUPERSEDED", parents=("ARTIFACT-000",),
        )
        self.assertEqual(manifest.as_dict()["validity"], "SUPERSEDED")
        with self.assertRaises(ValueError):
            ArtifactManifest(artifact_id="ARTIFACT-002", media_type="text/plain", sha256="bad", size_bytes=0, producer="SERVICE-001", source_revision="x")

    def test_event_requires_payload_reference_and_carries_correlation(self):
        subject = Identity(project_id="PROJECT-001", task_id="TASK-001")
        event = EventEnvelope(event_id="EVENT-001", event_type="task.created", schema_version="1.0.0", actor_id="ACTOR-001", subject=subject, payload_ref="artifact://ARTIFACT-001")
        self.assertEqual(event.as_dict()["correlation_id"], subject.correlation_key())

    def test_schema_registry_rejects_redefinition_and_breaking_major(self):
        registry = SchemaRegistry()
        registry.register("task", "1.0.0", {"type": "object"})
        registry.register("task", "1.1.0", {"type": "object", "additionalProperties": False})
        self.assertTrue(registry.compatible("task", "1.0.0", "1.1.0"))
        with self.assertRaises(ValueError):
            registry.register("task", "1.0.0", {"type": "string"})
        with self.assertRaises(KeyError):
            registry.compatible("task", "1.0.0", "2.0.0")


if __name__ == "__main__":
    unittest.main()
