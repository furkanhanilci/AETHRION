# Kanıt ve Kabul Stratejisi

## Evidence manifest

Her paket şu minimum alanları taşıyan bir `EvidenceManifest` üretir:

```yaml
package_id: WP-xxx
target_revision: sha256-or-git-commit
environment_manifest: artifact-ref
policy_bundle: git-digest
schema_bundle: git-digest
test_results: []
security_results: []
contract_results: []
rollback_result: artifact-ref
review_records: []
open_findings: []
owner_decision: decision-id
created_at: timestamp
signature: sigstore-ref
```

## Kanıt katmanları

| Katman | Soru | Örnek |
|---|---|---|
| E0 Yapısal | Dosya/schema/reference var mı? | JSON Schema validation, hash verify |
| E1 Mekanik | Davranış deterministik testte doğru mu? | Unit, integration, policy test |
| E2 Güvenlik | Yasak yol gerçekten engelleniyor mu? | Negative route, egress, permission test |
| E3 Bağımsız review | Üretici dışı aktör semantiği inceledi mi? | Blind ReviewRecord |
| E4 Reproduction | Aynı paket temiz ortamda tekrar çalışıyor mu? | ReproductionReport |
| E5 Operasyon | Failure, restore ve gözlemlenebilirlik doğru mu? | Chaos/DR/SLO evidence |

Paketin riskine göre gereken katman değişir; ancak critical paketlerde E0–E5'in ilgili olanları waiver edilemez.

## Finding yaşam döngüsü

```text
REPORTED → STRUCTURALLY_VALID → REPRODUCED → VALIDATED
         ↘ NOT_REPRODUCIBLE / DUPLICATE / OUT_OF_SCOPE
VALIDATED → FIXED → REVERIFIED → CLOSED
```

Correction yalnız `VALIDATED` bulgular için açılır. Kritik bulgunun “muhtemelen yanlış pozitif” diye kapatılması mümkün değildir; reproducer sonucu gerekir.

## Kabul seviyeleri

- Package Acceptance: Paket contract ve testleri.
- Integration Acceptance: İki veya daha fazla servis arasındaki gerçek interface.
- Vertical Slice Acceptance: G0–G10'un ilgili bölümündeki iş sonucu.
- System Commissioning: ACC-01–ACC-40, attack suite, DR ve capacity.
- Human Go-Live Decision: Kanıt özetini ve residual risk'i gören yetkili karar.

## İzlenebilirlik

Her requirement `REQ-*`, control `CTL-*`, work package `WP-*`, test `TST-*`, acceptance scenario `ACC-*`, finding `FND-*` ve decision `DEC-*` kimliğiyle bağlanır. Go-live dossier en az `REQ → WP → TST/ACC → Evidence → Decision` zincirini sorgulayabilmelidir.

