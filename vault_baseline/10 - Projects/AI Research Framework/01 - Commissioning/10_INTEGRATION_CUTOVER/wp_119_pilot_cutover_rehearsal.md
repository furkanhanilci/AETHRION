# WP-119 — Kontrollü Pilot ve Cutover Rehearsal

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-119` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Program Lead |
| Bağımsız doğrulayıcı | Commissioning Board / Independent Observer |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118 |
| İlgili gate | Commissioning |
| İlgili kontroller | Tüm kontroller |
| İlgili ACC senaryoları | ACC-01..ACC-40 |

## Amaç ve beklenen sonuç

Production dışı fakat production-equivalent ortamda düşük riskli gerçekçi pilot ve baştan sona cutover/abort/rollback rehearsal aynı prosedürle tamamlanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-115 — Tam Sistem Regression ve Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-116 — Resilience, Chaos ve Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md), [WP-117 — Performans, Kapasite ve Yük Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md), [WP-118 — Operasyonel Hazırlık, On-Call ve Runbook Simulation](../10_INTEGRATION_CUTOVER/wp_118_operational_readiness.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-119-T01 | Pilot seçim kriteri ve data minimization yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-119-T02 | Production-equivalent RC/config/data volume ile G0–G10 pilot çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-119-T03 | Operasyon/karar/assurance SLA ve human usability ölç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-119-T04 | Cutover runbook, freeze, migration, smoke, abort ve rollback adımlarını prova et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-119-T05 | Pilot feedback'i correction package'e çevir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-119-T06 | Final rehearsal report ve go/no-go recommendation üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Pilot dossier`
- `Cutover rehearsal log`
- `Usability/ops findings`
- `Rollback proof`
- `Go/no-go recommendation`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Full pilot G0–G10
- Abort threshold trigger
- Rollback to prior baseline
- On-call/human decision timing
- Audit export
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Pilot bütün invariant'ları karşılar
- [ ] Rehearsal rollback kanıtı vardır
- [ ] Açık critical/high pilot finding yok
- [ ] Gerçek cutover prosedürü timeboxed ve owner'lıdır
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

Pilot production yan etkisi üretmez; rehearsal state environment teardown/archive ile kapatılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
