# WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-121` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead / Program Lead |
| Bağımsız doğrulayıcı | Executive Sponsor / Assurance |
| Hard dependencies | WP-120 |
| İlgili gate | Cutover,Day-2 |
| İlgili kontroller | Tüm kontroller |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Go-live sonrası yoğun gözlem, hızlı incident/reconciliation, SLO/cost/quality ölçümü ve exit kriterleriyle sistem normal Day-2 işletimine devredilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-120 — Production Cutover ve Go-Live Kararı](../10_INTEGRATION_CUTOVER/wp_120_production_cutover.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-121-T01 | Hypercare command center/rota ve decision cadence kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-121-T02 | Critical journeys/synthetic tests/queues/cost/security/evidence dashboards izle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-121-T03 | Incident/finding/change freeze ve rollback yetkisini işlet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-121-T04 | User support/feedback/knowledge capture yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-121-T05 | SLO/error budget/quality KPI baseline'ı doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-121-T06 | Exit review ve Day-2 owner handoff imzala | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Hypercare log`
- `Incident/finding summary`
- `Production KPI baseline`
- `Day-2 handoff`
- `Program closure report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Synthetic G0→decision journey
- Zotero sync/impact/queue health
- Budget/invoice sample
- Audit export sample
- On-call response
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Hypercare exit boyunca critical incident=0 açık
- [ ] SLO ve evidence integrity hedefleri karşılanır
- [ ] Day-2 owners/runbooks/ritimler aktiftir
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

Critical instability'de cutover rollback yetkisi kullanılır; partial feature bypass ile devam edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
