# WP-029 — MLflow Deney ve Eval Tracking Temeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-029` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Experiment Platform Lead |
| Bağımsız doğrulayıcı | Reproducibility Engineer / Security |
| Hard dependencies | WP-021, WP-025, WP-026 |
| İlgili gate | G4–G7 |
| İlgili kontroller | CTL-DAT-01, CTL-OBS-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Deney, eval, metric ve artifact referansları data-class uyumlu, access-controlled ve immutable run kimliğiyle izlenir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-029-T01 | Tracking server/backend/artifact store kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-029-T02 | Project/run RBAC ve data-class separation uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-029-T03 | Run tag standardı ve correlation ID ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-029-T04 | Artifact'ı kopyalamak yerine canonical ref kullan | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-029-T05 | Metric schema ve lifecycle tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-029-T06 | Backup/restore ve export testi kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `MLflow deployment`
- `Run naming/tag policy`
- `Access controls`
- `Tracking SDK wrapper`
- `Restore procedure`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Unauthorized project read negative testi
- Run→artifact/source correlation query
- Backup restore ve metric integrity testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] MLflow canonical artifact bytes sahibi olmaz
- [ ] Her run Project/Workflow/Run ID ile bağlıdır
- [ ] D3/D4 prompt/data telemetry'si policy dışına çıkmaz
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

Tracking servisi kaybında run execution artifactleri kaybolmaz; queued metadata idempotent ingest edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
