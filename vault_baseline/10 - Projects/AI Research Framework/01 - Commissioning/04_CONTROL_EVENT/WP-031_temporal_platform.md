# WP-031 — Temporal Platform, Namespace ve HA

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-031` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Control Plane Lead |
| Bağımsız doğrulayıcı | SRE / Security |
| Hard dependencies | WP-021, WP-025, WP-026, WP-027, WP-028 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-OPS-02, CTL-SEC-03 |
| İlgili ACC senaryoları | ACC-13, ACC-14 |

## Amaç ve beklenen sonuç

Temporal; environment, data class, retention, worker identity ve failover sınırlarıyla durable workflow platformu olarak production-ready kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-031-T01 | Cluster/managed topology ve failure domain'i kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-031-T02 | Dev/staging/prod namespace ve retention ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-031-T03 | mTLS/workload identity/RBAC bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-031-T04 | Worker task queue ve versioning standardını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-031-T05 | Visibility/archive/large payload reference kuralını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-031-T06 | Backup/failover/SLO telemetry kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Temporal platform`
- `Namespace/queue catalog`
- `Worker identity policy`
- `HA/failover runbook`
- `SLO dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Worker/cluster failover testi
- Unauthorized queue poll negative testi
- Large payload object-ref testi
- Visibility/archive restore testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Workflow state worker kaybında korunur
- [ ] Büyük bytes event history'ye girmez
- [ ] Her worker yalnız izinli queue'yu poll eder
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

Control cluster failover runbook uygulanır; workflow history canonical olduğundan worker yeniden bağlanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
