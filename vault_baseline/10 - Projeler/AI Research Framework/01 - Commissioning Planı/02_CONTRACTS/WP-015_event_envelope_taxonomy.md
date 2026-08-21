# WP-015 — Event Envelope, Subject ve Schema Taxonomy

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-015` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Event Platform Lead |
| Bağımsız doğrulayıcı | Control Plane Lead / Security |
| Hard dependencies | WP-011, WP-012, WP-014 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-OPS-01, CTL-OBS-01 |
| İlgili ACC senaryoları | ACC-12, ACC-34 |

## Amaç ve beklenen sonuç

Canonical commit sonrası yayımlanan olayların kimliği, causation, actor, data class, payload reference, version ve retention sözleşmesi tamamlanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/WP-011_kimlik_korelasyon_standardi.md), [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-015-T01 | EventEnvelope alanlarını sabitle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-015-T02 | workflow/artifact/evidence/security/cost/telemetry subject taxonomy kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-015-T03 | Payload gövdesi vs encrypted reference kuralını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-015-T04 | At-least-once/idempotent consumer beklentisini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-015-T05 | Schema evolution ve replay_mode semantiğini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `EventEnvelope schema`
- `Event Catalog seed`
- `Subject/retention table`
- `Consumer contract`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Duplicate event fixture
- D3 payload gövdeye yazma negatif testi
- Major schema replay compatibility testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her olay event/causation/correlation/idempotency taşır
- [ ] NATS olayı gate state'i tek başına değiştiremez
- [ ] PII/D3/D4 payload event gövdesine girmez
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

Uyumsuz event DLQ'ya alınır; producer/consumer eski subject'te tutulur ve adapter ile migration yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
