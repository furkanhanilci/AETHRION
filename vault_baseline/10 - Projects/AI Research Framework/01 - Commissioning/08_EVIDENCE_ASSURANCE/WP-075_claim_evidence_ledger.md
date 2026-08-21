# WP-075 — Canonical Claim/Evidence Ledger Servisi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-075` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Platform Lead |
| Bağımsız doğrulayıcı | Data Architect / Assurance Lead |
| Hard dependencies | WP-018, WP-020, WP-025, WP-026, WP-028, WP-030, WP-055, WP-056, WP-061 |
| İlgili gate | G5–G10 |
| İlgili kontroller | CTL-EPI-01 |
| İlgili ACC senaryoları | ACC-04, ACC-08, ACC-30, ACC-31 |

## Amaç ve beklenen sonuç

Claim, evidence span, dependency, assessment, review link, decision ve supersession kayıtları immutable-versioned canonical ledger'da saklanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-075-T01 | Claim/Evidence/Dependency/Assessment tablolarını migrate et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-075-T02 | Version/create/challenge/supersede API'lerini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-075-T03 | Optimistic locking, actor, policy ve outbox event bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-075-T04 | Field/data-class RBAC ve access log uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-075-T05 | Lineage/impact query API'lerini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-075-T06 | Backup, integrity ve WORM audit export'unu kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Claim Ledger service`
- `Migrations/API`
- `State transition engine`
- `Lineage queries`
- `Service runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Immutable version/supersession
- Unauthorized claim verify deny
- Claim→source/run/review/decision query
- Concurrent challenge
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Claim metni düzeltmesi yeni version üretir
- [ ] VERIFIED kalıcı/geri alınamaz durum değildir
- [ ] Material claim bağı eksikse publication'da görünemez
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

Hatalı transition superseding event ile düzeltilir; geçmiş decision/reference değişmeden kalır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
