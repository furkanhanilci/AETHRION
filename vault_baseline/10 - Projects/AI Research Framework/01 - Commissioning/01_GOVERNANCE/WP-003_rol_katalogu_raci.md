# WP-003 — Rol Kataloğu ve RACI Baseline

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-003` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Governance Lead |
| Bağımsız doğrulayıcı | Internal Audit |
| Hard dependencies | WP-001, WP-002 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-GOV-01, CTL-GOV-02 |
| İlgili ACC senaryoları | ACC-06, ACC-38 |

## Amaç ve beklenen sonuç

İnsan, service ve model aktörlerinin rol, karar hakkı, yasak eylem, gerekli artifact ve escalation sınırları tek katalogda sabitlenir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-001 — Commissioning Charter ve Program Yetkisi](../01_GOVERNANCE/WP-001_commissioning_charter.md), [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/WP-002_kapsam_nfr_izlenebilirlik.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-003-T01 | 36 çekirdek rolü kalıcı fonksiyon ve görev hücresine eşle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-003-T02 | Her rol için mandate, input/output ve forbidden action yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-003-T03 | G0–G10 ile platform release kararlarının RACI'sini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-003-T04 | Küçük ekip rol birleştirme kurallarını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-003-T05 | RoleContract versioning ve atama yaşam döngüsünü tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Role Catalog`
- `RACI matrix`
- `Role-combination policy`
- `Role assignment workflow`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Eksik accountable karar taraması
- Aynı artifact self-approval negatif testi
- Küçük ekip R1/R3 tabletop testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her material kararın tek A rolü vardır
- [ ] Producer tek başına review/repro/accept yapamaz
- [ ] Rol birleştirme independence policy'yi ihlal etmez
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

Çakışan atamalar iptal edilir; son imzalı rol baseline'ına dönülür.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
