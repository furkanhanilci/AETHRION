# WP-120 — Production Cutover ve Go-Live Kararı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-120` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Executive Sponsor / Program Lead |
| Bağımsız doğrulayıcı | Commissioning Board / Internal Audit |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118, WP-119 |
| İlgili gate | Cutover |
| İlgili kontroller | Tüm kontroller |
| İlgili ACC senaryoları | ACC-01..ACC-40 |

## Amaç ve beklenen sonuç

İmzalı commissioning dossier ve rehearsal'a dayanarak change freeze, migration/promotion, smoke/integrity test, traffic enablement ve resmi Go-Live DecisionRecord yürütülür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-115 — Tam Sistem Regression ve Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-116 — Resilience, Chaos ve Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md), [WP-117 — Performans, Kapasite ve Yük Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md), [WP-118 — Operasyonel Hazırlık, On-Call ve Runbook Simulation](../10_INTEGRATION_CUTOVER/wp_118_operational_readiness.md), [WP-119 — Kontrollü Pilot ve Cutover Rehearsal](../10_INTEGRATION_CUTOVER/wp_119_pilot_cutover_rehearsal.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-120-T01 | Final RC/policy/schema/model/tool/infra digest freeze et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-120-T02 | Pre-cutover backup/restore point ve owner check yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-120-T03 | IaC/GitOps deployment ve migration adımlarını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-120-T04 | Service/contract/security/integrity smoke tests çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-120-T05 | Traffic/user access ve monitoring'i kontrollü aç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-120-T06 | Go/no-go/abort kararını kanıtla kaydet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-120-T07 | Post-cutover audit snapshot al | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Cutover execution log`
- `Go-Live DecisionRecord`
- `Production release manifest`
- `Smoke/integrity results`
- `Audit snapshot`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Preflight checklist
- Deployment/migration
- Security/identity/route smoke
- Workflow/source/claim/artifact integrity
- Abort/rollback readiness
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Commissioning Dossier READY
- [ ] 40/40 PASS ve open critical=0
- [ ] Tüm production digests imzalı/pinned
- [ ] Named executives/SRE/Safety go-live kararı
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

Abort eşiğinde trafik kapatılır, GitOps/DB planına göre son doğrulanmış baseline'a dönülür; immutable yeni kayıtlar silinmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
