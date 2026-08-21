# WP-016 — PolicyDecision, Control ve Exception Şemaları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-016` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Policy Platform Lead |
| Bağımsız doğrulayıcı | Internal Audit |
| Hard dependencies | WP-006, WP-009, WP-011 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-GOV-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Her authorization/route/gate kararının girdisi, bundle sürümü, rule ID'si, açıklaması ve exception bağlantısı denetlenebilir kayda dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-009 — Control Kataloğu, Exception ve Non-Waivable Blocker'lar](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-016-T01 | PolicyDecision allow/deny/obligations alanlarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-016-T02 | ControlRecord owner/evidence/frequency alanlarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-016-T03 | ExceptionRecord scope/approver/expiry şemasını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-016-T04 | Policy explanation ve input hash formatını sabitle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-016-T05 | Re-evaluation trigger'larını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `PolicyDecision schema`
- `ControlRecord schema`
- `ExceptionRecord schema`
- `Example decision fixtures`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Missing bundle/rule ID negatif testi
- Expired exception validation
- Input hash determinism testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Karar açıklanabilir rule ID ve bundle digest taşır
- [ ] Exception kapsam dışı kullanılamaz
- [ ] UNKNOWN policy sonucu allow'a dönüşmez
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

Policy record düzeltilmez; yeni superseding decision yazılır ve etkilenen task'lar re-evaluate edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
