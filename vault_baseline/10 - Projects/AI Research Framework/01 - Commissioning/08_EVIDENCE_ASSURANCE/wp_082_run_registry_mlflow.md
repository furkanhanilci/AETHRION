# WP-082 — Run Registry ve MLflow Lineage Entegrasyonu

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-082` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Experiment Platform Lead |
| Bağımsız doğrulayıcı | Reproducibility Engineer |
| Hard dependencies | WP-014, WP-019, WP-025, WP-026, WP-029, WP-032, WP-081 |
| İlgili gate | G4,G5 |
| İlgili kontroller | CTL-DAT-01, CTL-CST-01 |
| İlgili ACC senaryoları | ACC-39 |

## Amaç ve beklenen sonuç

Run kabulü; protocol, literature set, dataset, code, environment, prompt, model, seed, budget ve execution attestation tamamlanmadan başlamaz; MLflow yalnız tracking görünümü olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-029 — MLflow Deney ve Eval Tracking Temeli](../03_FOUNDATION/wp_029_mlflow_foundation.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-081 — Protocol, Analysis, Baseline ve Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-082-T01 | Run Registry state/API kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-082-T02 | Pre-run manifest completeness/admission checks yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-082-T03 | Temporal/Execution/MLflow correlation bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-082-T04 | Metric/artifact/result ingestion ve hash validation ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-082-T05 | Failed/cancelled/negative run lifecycle tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-082-T06 | Run comparison/query ve outbox events ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Run Registry`
- `Preflight validator`
- `MLflow integration`
- `Run lineage queries`
- `Run lifecycle dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Missing dataset/image/model deny
- Run ID correlation end-to-end
- Failed run artifact retained
- MLflow outage queued ingest
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Eksik metadata ile run başlamaz
- [ ] MLflow canonical workflow/artifact state sahibi değildir
- [ ] Negatif sonuç first-class run durumudur
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

Tracking failure execution evidence'i kaybetmez; idempotent backfill yapılır, invalid run publish edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
