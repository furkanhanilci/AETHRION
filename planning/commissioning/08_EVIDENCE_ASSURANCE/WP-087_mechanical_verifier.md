# WP-087 — Mekanik Verification Engine

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-087` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Verification Engineering Lead |
| Bağımsız doğrulayıcı | Independent Test Engineer |
| Hard dependencies | WP-020, WP-024, WP-026, WP-027, WP-075, WP-076, WP-080, WP-081, WP-082, WP-086 |
| İlgili gate | G2–G9 |
| İlgili kontroller | CTL-EPI-01, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-08, ACC-17, ACC-23, ACC-30 |

## Amaç ve beklenen sonuç

Schema, hash, test, policy, manifest, signature, locator, lineage ve report-claim linkleri LLM beyanından bağımsız deterministik kayıtlarla doğrulanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-024 — CI Temeli ve Deterministik Kalite Kapıları](../03_FOUNDATION/WP-024_ci_kalite_kapilari.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-080 — Claim–Citation Entailment, Scope ve Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline ve Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-086 — Frozen ve Kör Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-087-T01 | Validator plugin interface ve registry kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-087-T02 | Schema/hash/signature/SBOM/policy validators ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-087-T03 | Test/CI/run/manifest/locator/lineage validators bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-087-T04 | Finding structural validation ve target revision check yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-087-T05 | VerificationRecord/evidence map üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-087-T06 | Validator version/calibration/regression kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Verification Engine`
- `Validator catalog`
- `VerificationRecord service`
- `Regression fixtures`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Tamper hash/signature fail
- Missing lineage/locator fail
- Finding wrong file/symbol invalid
- Same target deterministic results
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Self-declaration verification sayılmaz
- [ ] Validator input/output/version ve artifact hash taşır
- [ ] Critical mechanical fail reviewer çoğunluğuyla geçilemez
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur; non-waivable blocker bulunmamaktadır.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.
- [ ] Rollback/compensation davranışı denenmiş ve audit edilmiştir.
- [ ] İlgili dashboard, alert, audit query veya integrity query çalışma kanıtı üretmiştir.

## Kabul kanıtı paketi

- Aynı target revision/digest üzerinde alınmış test sonuçları
- Environment, schema, policy ve dependency sürümlerini içeren EvidenceManifest
- Bağımsız verifier ReviewRecord veya VerificationRecord'u
- Rollback/compensation denemesi ve sonuç referansı
- Açık finding, residual risk ve owner/expiry listesi

## Riskler ve kontrol noktaları

- Contract veya canonical sahiplik belirsizse implementasyon durur ve Architecture Board'a eskale edilir.
- Identity, data route, artifact integrity, bağımsızlık veya kritik evidence problemi waiver ile geçirilemez.
- Geçici manuel kontrol gerekiyorsa owner, scope, expiry, compensating control ve kaldırma paketi kaydedilir.
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Hatalı validator release revoke edilir; etkilenen VerificationRecord'lar re-run/impact alır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
