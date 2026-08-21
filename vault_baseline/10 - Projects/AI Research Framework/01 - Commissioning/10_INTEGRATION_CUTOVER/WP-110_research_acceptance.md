# WP-110 — Araştırma ve Literatür Kabul Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-110` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Research Director |
| Bağımsız doğrulayıcı | Citation Auditor / Assurance |
| Hard dependencies | WP-103, WP-104, WP-105, WP-106, WP-108, WP-109 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-EPI-01, CTL-LIT-01, CTL-GOV-02 |
| İlgili ACC senaryoları | ACC-01..ACC-08 |

## Amaç ve beklenen sonuç

Human seed, agent write-back, duplicate, retraction, injection, self-approval, order bias ve counter-test senaryoları tam kanıtla kapanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-103 — Dikey Dilim 2 — İki Yönlü Literatür ve Set Freeze](../10_INTEGRATION_CUTOVER/WP-103_dikey_dilim_literatur.md), [WP-104 — Dikey Dilim 3 — Baseline → Run → Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_dikey_dilim_run_claim.md), [WP-105 — Dikey Dilim 4 — Blind Review → Arbitration → Clean-Room](../10_INTEGRATION_CUTOVER/WP-105_dikey_dilim_review_repro.md), [WP-106 — Dikey Dilim 5 — Human Decision → Publish → Monitor](../10_INTEGRATION_CUTOVER/WP-106_dikey_dilim_decision_publish_monitor.md), [WP-108 — Retraction, Drift ve Supersession Dikey Dilimi](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_dikey_dilim.md), [WP-109 — Kırk Acceptance Senaryosu Registry ve Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-110-T01 | ACC-01–ACC-08 fixture'larını resetle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-110-T02 | Aynı release candidate üzerinde paralel olmayan kontrollü koşum yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-110-T03 | Expected Registry/Zotero/Ledger/Gate/Audit sonuçlarını doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-110-T04 | Critical finding triage/reproducer/correction çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-110-T05 | Research acceptance dossier ve owner sign-off üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ACC-01–08 results`
- `Research acceptance dossier`
- `Finding/disposition records`
- `Owner sign-off`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-01..ACC-08
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Sekiz senaryo PASS
- [ ] Açık critical/high research finding yok
- [ ] Manifest, claim, reviewer ve source integrity sorguları tamam
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

Failure cutover'ı bloklar; fixture state temizlenir, correction sonrası yalnız etkilenen değil regression seti tekrar çalışır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
