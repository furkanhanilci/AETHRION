# WP-127 — FinOps, Kapasite ve Portfolio Review Ritmi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-127` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | FinOps Lead / Research Director |
| Bağımsız doğrulayıcı | Internal Audit / Assurance |
| Hard dependencies | WP-100, WP-117, WP-121 |
| İlgili gate | G0,G4,G8,Day-2 |
| İlgili kontroller | CTL-CST-01, CTL-CST-02 |
| İlgili ACC senaryoları | ACC-09, ACC-29 |

## Amaç ve beklenen sonuç

Aylık invoice reconciliation, forecast, quality-adjusted cost/outcome, queue capacity, model mix ve stop/pivot portföy kararları kalıcı hale gelir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-117 — Performans, Kapasite ve Yük Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-127-T01 | Invoice/provider/compute/storage reconciliation çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-127-T02 | Project/outcome budget variance ve forecast üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-127-T03 | Model/agent fan-out ve verification EVI analiz et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-127-T04 | Capacity/headroom/queue wait planını güncelle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-127-T05 | Low-value/high-cost project stop/pivot kararını kaydet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-127-T06 | Annual cost policy benchmark/reopen tetikle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Monthly FinOps report`
- `Invoice cases`
- `Portfolio decision records`
- `Capacity forecast`
- `Optimization backlog`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Invoice variance sample
- Hard budget event audit
- Cost allocation completeness
- Quality-adjusted route comparison
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Maliyet yalnız token fiyatıyla optimize edilmez
- [ ] Assurance insan maliyeti görünürdür
- [ ] Bütçe override named decision/expiry taşır
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

Yanlış allocation reconciliation adjustment ile; geçmiş fatura/ledger event'i silinmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
