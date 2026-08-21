# WP-028 — NATS JetStream ve Transactional Outbox Temeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-028` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Event Platform Lead |
| Bağımsız doğrulayıcı | SRE / Data Platform Lead |
| Hard dependencies | WP-015, WP-021, WP-025 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-OPS-01, CTL-OBS-01 |
| İlgili ACC senaryoları | ACC-12, ACC-34 |

## Amaç ve beklenen sonuç

At-least-once olay omurgası, canonical DB commit ile publish niyetini aynı transaction'a alan outbox ve idempotent relay ile kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-028-T01 | JetStream cluster/stream/retention kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-028-T02 | Subject ACL ve workload identity bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-028-T03 | PostgreSQL outbox schema ve relay yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-028-T04 | Consumer durable/ack/DLQ standardını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-028-T05 | Replay/read-model mode kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-028-T06 | Schema registry validation ve telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `NATS cluster`
- `Outbox relay`
- `Consumer SDK`
- `DLQ/replay runbook`
- `Event dashboards`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Duplicate delivery tek business effect
- Commit sonrası relay crash recovery
- Poison event DLQ ve corrected replay
- NATS kaybında canonical state korunur
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] ACK yalnız business commit sonrası verilir
- [ ] Gate state NATS consumer tarafından doğrudan değişmez
- [ ] Outbox lag SLO ve alarmı vardır
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

Relay/consumer rollback'te offset ve outbox korunur; replay dry-run ile doğrulanmadan side effect açılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
