# WP-009 — Control Kataloğu, Exception ve Non-Waivable Blocker'lar

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-009` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız doğrulayıcı | Internal Audit |
| Hard dependencies | WP-005, WP-006, WP-007, WP-008 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-GOV-03 |
| İlgili ACC senaryoları | ACC-24, ACC-26 |

## Amaç ve beklenen sonuç

Her kontrol owner, enforcement point, evidence, test frekansı ve exception yaşam döngüsüyle registry nesnesine dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/WP-006_execution_profili.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-009-T01 | Governance/epistemic/data/literature/security/ops/observability/cost/model kontrollerini kimliklendir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-009-T02 | Control→policy→test→evidence mapping kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-009-T03 | Exception request/approval/expiry/auto-revoke semantiğini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-009-T04 | Non-waivable blocker listesini policy'ye bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-009-T05 | Control effectiveness review frekansını ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Control Catalog`
- `ExceptionPolicy`
- `NonWaivableBlocker registry`
- `Control-test mapping`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Expired exception auto-revoke testi
- Non-waivable exception negatif testi
- Kontrolün evidence üretmemesi fail testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her kontrolün zorlayıcı noktası ve kanıtı vardır
- [ ] Exception süreli ve scope-bound'dur
- [ ] Kritik blocker için exception yolu yoktur
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

Hatalı policy bundle rollback edilir; exception etkisi bulunan kararlar yeniden değerlendirilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
