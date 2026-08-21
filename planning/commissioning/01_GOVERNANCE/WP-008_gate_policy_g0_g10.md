# WP-008 — G0–G10 Gate ve Assurance Politikası

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-008` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Research Director |
| Bağımsız doğrulayıcı | Assurance Lead / Safety Owner |
| Hard dependencies | WP-004, WP-005, WP-007 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-GOV-01, CTL-EPI-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Her gate'in değişmez amacı, giriş/çıkış artifact'ı, hard blocker'ı, risk bazlı derinliği, reopen ve escalation davranışı tek policy baseline'ında kapanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/WP-004_insan_karar_sla_delegasyon.md), [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-008-T01 | G0–G10 giriş/çıkış ve GateRecord alanlarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-008-T02 | R1/R2/R3 assurance overlay'lerini bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-008-T03 | Gate'ler aynı oturumda kapanabilse de ayrı kayıt üretme kuralını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-008-T04 | Protocol/literature/run/review/repro reopen kurallarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-008-T05 | Non-waivable blocker ve residual-risk kabul sınırını eşle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-008-T06 | G10 supersession/impact davranışını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Gate Policy v1`
- `Gate artifact matrix`
- `Reopen/return transition table`
- `Gate owner matrix`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Happy path state walkthrough
- Her gate için en az bir hard-fail testi
- Risk derinliği ve ayrı GateRecord testi
- G7 fail→CHALLENGED geri dönüş testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] On bir gate'in tümünde owner, artifact, acceptance ve blocker vardır
- [ ] Risk gate'i kaldırmaz
- [ ] Kritik blocker insan override ile geçilemez
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

Yeni gate policy açık workflow'lara doğrudan uygulanmaz; impact scan ve versioned transition ile promote edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
