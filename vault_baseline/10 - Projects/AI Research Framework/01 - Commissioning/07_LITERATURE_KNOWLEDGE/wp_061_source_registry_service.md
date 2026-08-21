# WP-061 — Canonical Source Registry Servisi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-061` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Platform Lead |
| Bağımsız doğrulayıcı | Data Architect / Citation Auditor |
| Hard dependencies | WP-012, WP-017, WP-020, WP-025, WP-026, WP-028, WP-055, WP-056 |
| İlgili gate | G3,G10 |
| İlgili kontroller | CTL-LIT-01, CTL-OPS-01 |
| İlgili ACC senaryoları | ACC-03, ACC-28 |

## Amaç ve beklenen sonuç

Bibliyografik kimlik, representation, trust, status, project membership ve Zotero binding kayıtlarının canonical PostgreSQL servisi kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-061-T01 | SourceRecord/Representation/Trust/Binding tablolarını migrate et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-061-T02 | Create/read/version/merge/tombstone API'lerini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-061-T03 | Optimistic concurrency ve outbox event üretimini bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-061-T04 | Field authority ve data-class RBAC uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-061-T05 | Search/filter/history ve bulk ingest API ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-061-T06 | Backup, SLO ve audit query'lerini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Source Registry service`
- `Database migrations`
- `API/OpenAPI`
- `Outbox events`
- `Service runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Concurrent update 409/merge case
- Unauthorized field write
- Source history traversal
- DB fail/retry idempotency
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Source Registry canonical identity/status sahibidir
- [ ] Hiçbir Zotero key/DOI tek başına primary key olmaz
- [ ] Her mutation version ve actor taşır
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

Hatalı migration expand-contract ile düzeltilir; yanlış merge split/supersession event üretir, kayıt silinmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
