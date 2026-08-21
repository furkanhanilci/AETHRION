# WP-122 — Service Health, SLO ve Error-Budget Ritmi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-122` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Service Owners / Internal Audit |
| Hard dependencies | WP-101, WP-121 |
| İlgili gate | Day-2 |
| İlgili kontroller | CTL-OBS-01, CTL-OPS-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Günlük/haftalık service health, SLO, dependency, capacity, alert quality ve error-budget review kalıcı işletim ritmine dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilizasyon.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-122-T01 | Daily health ve weekly SLO review agenda kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-122-T02 | Error-budget breach release freeze uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-122-T03 | Ownership/runbook freshness kontrol et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-122-T04 | Dependency risk ve toil backlog takip et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-122-T05 | Monthly availability/correctness/freshness report üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Ops cadence calendar`
- `SLO review template`
- `Error-budget decisions`
- `Toil backlog`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Synthetic alert review
- Error-budget release block
- Orphan owner/runbook scan
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical SLO breach named action/owner taşır
- [ ] Error budget görmezden gelinmez
- [ ] Vanity uptime correctness'in yerini almaz
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

Ritim aksarsa governance escalation; kontrol kalıcı kapatılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
