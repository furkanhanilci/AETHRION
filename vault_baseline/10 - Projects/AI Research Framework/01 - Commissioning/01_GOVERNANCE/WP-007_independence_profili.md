# WP-007 — IndependenceProfile ve Separation-of-Duties Politikası

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-007` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Lead |
| Bağımsız doğrulayıcı | Internal Audit / Safety Owner |
| Hard dependencies | WP-003, WP-005 |
| İlgili gate | G6,G7,G8 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-06, ACC-38 |

## Amaç ve beklenen sonuç

Producer, reviewer ve reproducer ayrılığı insan, model ailesi, context, credential, environment, veri yolu ve ekonomik çıkar boyutlarında denetlenebilir olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-003 — Rol Kataloğu ve RACI Baseline](../01_GOVERNANCE/WP-003_rol_katalogu_raci.md), [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-007-T01 | Yedi bağımsızlık boyutunu tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-007-T02 | R1/R2/R3 minimum setlerini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-007-T03 | Non-compensable boyut ve blocker kurallarını belirle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-007-T04 | Frozen package/context contamination kontrollerini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-007-T05 | Assignment-time ve gate-time yeniden değerlendirmeyi tasarla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `IndependenceProfile rubric`
- `Eligibility matrix`
- `Conflict-of-interest declaration`
- `Violation response`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Planner self-review negatif testi
- Aynı model ailesi/context contamination testi
- Reviewer unavailable fail-closed testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Tek ortalama independence skoru yoktur
- [ ] R3 insan ayrımı sağlanamazsa BLOCKED olur
- [ ] Reviewer yalnız frozen paket ve izinli context görür
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

İhlal edilen review/repro kayıtları INVALIDATED olur; yeni bağımsız assignment açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
