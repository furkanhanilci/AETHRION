# WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-002` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Chief Architect |
| Bağımsız doğrulayıcı | Assurance Lead |
| Hard dependencies | WP-001 |
| İlgili gate | Program |
| İlgili kontroller | CTL-GOV-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Fonksiyonel kapsam ve dayanıklılık, izlenebilirlik, izolasyon, idempotency, audit, privacy, cost ve accessibility NFR'ları test edilebilir gereksinimlere dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-001 — Commissioning Charter ve Program Yetkisi](../01_GOVERNANCE/wp_001_commissioning_charter.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-002-T01 | Fonksiyonel capability listesini REQ kimlikleriyle çıkar | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-002-T02 | Her NFR için hedef, ölçüm ve test owner'ı ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-002-T03 | Domain-specific profil gerektiren alanları ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-002-T04 | REQ→WP→TST/ACC izlenebilirlik şemasını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-002-T05 | Kapsam dışı ve future-request kurallarını kaydet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Requirement Registry`
- `NFR scorecard`
- `Traceability matrix seed`
- `Scope boundary record`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Her REQ için ölçülebilir acceptance varlık testi
- Kapsam dışı maddeler için owner review
- NFR çelişki ve uygulanabilirlik walkthrough
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Material gereksinimlerin %100'ü owner ve test taşır
- [ ] Belirsiz 'hızlı/güvenli/ölçeklenebilir' ifadesi kalmaz
- [ ] Domain profilleri generic core'dan ayrıdır
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

İzlenemeyen gereksinimler taslağa döner; downstream paket READY yapılamaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
