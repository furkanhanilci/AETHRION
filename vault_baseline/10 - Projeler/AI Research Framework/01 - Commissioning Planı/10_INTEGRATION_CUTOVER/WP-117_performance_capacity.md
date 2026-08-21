# WP-117 — Performans, Kapasite ve Yük Commissioning

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-117` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Capacity Engineering Lead |
| Bağımsız doğrulayıcı | SRE / FinOps / Assurance |
| Hard dependencies | WP-053, WP-096, WP-098, WP-100, WP-101, WP-115 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-CST-01, CTL-OBS-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Approved workload envelope altında intake/gate, event, model, broker, registry, experiment, review ve impact queue'ları SLO, quota ve cost sınırlarını karşılar.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-098 — Grafana ve Altı Operasyon Grafiği](../09_EXPERIENCE_OBSERVABILITY/WP-098_grafana_six_graphs.md), [WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md), [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-115 — Tam Sistem Regression ve Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-117-T01 | Workload mix/concurrency/data size/fan-out envelope tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-117-T02 | Service/queue/end-to-end load tests yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-117-T03 | DB/NATS/Temporal/model/tool/sandbox bottleneck ölç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-117-T04 | Autoscale/connection pool/cache/backpressure tune et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-117-T05 | Assurance queue ve human SLA kapasitesini modelle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-117-T06 | Cost curve/headroom/capacity plan üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Load test suite/results`
- `Capacity model`
- `Bottleneck/tuning report`
- `Cost/headroom forecast`
- `Capacity sign-off`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Nominal/peak/burst/soak
- Backpressure not data loss
- Review queue reserve
- Budget fan-out caps
- Large manifest/event reference
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] SLO approved envelope'da karşılanır
- [ ] En az %20 headroom veya named scale trigger vardır
- [ ] Backpressure unsafe bypass üretmez
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

Capacity fail olursa üretim kapsamı değil tarih/altyapı boyutu düzeltilir; RC READY durumu geri çekilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
