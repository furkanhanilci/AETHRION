# WP-039 — Event Consumer, DLQ ve Güvenli Replay Çerçevesi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-039` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Event Platform Lead |
| Bağımsız doğrulayıcı | SRE / Security |
| Hard dependencies | WP-015, WP-020, WP-028, WP-032 |
| İlgili gate | Platform,G10 |
| İlgili kontroller | CTL-OPS-01 |
| İlgili ACC senaryoları | ACC-12, ACC-34 |

## Amaç ve beklenen sonuç

Tüm consumer'lar idempotency, canonical-commit-before-ACK, poison event DLQ, replay mode ve projection rebuild contract'ını ortak SDK ile uygular.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-039-T01 | Consumer middleware/unique key standardı yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-039-T02 | ACK transaction boundary uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-039-T03 | DLQ metadata, retry/backoff ve repair workflow kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-039-T04 | replay_mode=dry-run/read-model-rebuild davranışını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-039-T05 | Offset/lag/poison telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-039-T06 | Örnek consumer conformance suite yayınla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Consumer SDK`
- `DLQ service/runbook`
- `Replay controller`
- `Conformance tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Duplicate delivery test
- Side effect commit öncesi crash
- Poison event sonsuz loop önleme
- Replay external mutation deny
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Exactly-once business effect idempotency ile sağlanır
- [ ] DLQ kaydı owner ve correction taşır
- [ ] Replay production mutation'ı otomatik tekrar etmez
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

Consumer rollback offset kaybetmez; yeni sürüm shadow consumer ile doğrulanıp cutover edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
