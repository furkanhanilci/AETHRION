# WP-115 — Tam Sistem Regression ve Commissioning Dossier

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-115` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Assurance Lead |
| Bağımsız doğrulayıcı | Commissioning Board |
| Hard dependencies | WP-110, WP-111, WP-112, WP-113, WP-114 |
| İlgili gate | Commissioning |
| İlgili kontroller | Tüm kontroller |
| İlgili ACC senaryoları | ACC-01..ACC-40 |

## Amaç ve beklenen sonuç

Aynı release candidate üzerinde kırk senaryo, contract/replay/attack/restore/capacity kanıtı tek imzalı Commissioning Dossier'da birleştirilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-110 — Araştırma ve Literatür Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_110_research_acceptance.md), [WP-111 — Reliability, Event ve FinOps Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_111_reliability_finops_acceptance.md), [WP-112 — Security ve Privacy Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_112_security_privacy_acceptance.md), [WP-113 — Evidence, Reproduction ve Publication Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_113_evidence_repro_acceptance.md), [WP-114 — Operations, DR ve Restore Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-115-T01 | RC digest ve tüm bundle versions freeze et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-115-T02 | ACC-01–40 sonuçlarını aynı RC için doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-115-T03 | Contract/replay/security/repro/DR/cost/trace evidence manifestlerini birleştir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-115-T04 | Open finding/risk/exception/expiry taraması yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-115-T05 | KPI/SLO/capacity ve owner readiness scorecard üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-115-T06 | Independent board review ve BLOCKED/READY verdict yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Commissioning Dossier`
- `RC evidence manifest`
- `Finding/risk register snapshot`
- `Readiness scorecard`
- `Board verdict`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Same RC/bundle consistency
- Evidence link/hash/signature verify
- Open critical query=0
- Expired exception/profile scan
- All scenarios complete
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] 40/40 PASS
- [ ] Open critical=0
- [ ] Required high=0 veya açık izinli residual risk
- [ ] Dossier bağımsız doğrulanmış ve imzalı
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

READY verilmezse RC promote edilmez; correction yeni RC digest üretir ve etkilenen+baseline regression tekrar koşar.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
