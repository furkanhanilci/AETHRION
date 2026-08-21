# WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-030` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Data Lead |
| Bağımsız doğrulayıcı | Data Platform Lead / Assurance |
| Hard dependencies | WP-012, WP-017, WP-018, WP-025, WP-026, WP-028 |
| İlgili gate | Platform,G10 |
| İlgili kontroller | CTL-OPS-03, CTL-OBS-01 |
| İlgili ACC senaryoları | ACC-21 |

## Amaç ve beklenen sonuç

Provenance graph, semantic retrieval ve full-text indexler canonical event/record'lardan sıfırdan yeniden kurulabilen read model olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-030-T01 | Projection schemas ve source event'leri tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-030-T02 | Neo4j claim/source/run/review graph projection'ı kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-030-T03 | pgvector embedding model/version metadata'sı ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-030-T04 | OpenSearch index/retention/data-class policy kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-030-T05 | Projection checkpoint ve lag telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-030-T06 | Full rebuild/swap procedure yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Projection services`
- `Graph/vector/search indexes`
- `Rebuild jobs`
- `Integrity/lag dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Canonical→projection count/hash reconciliation
- Graph corruption sonrası full rebuild
- Embedding model değişimi reindex testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Derived store hiçbir canonical write kabul etmez
- [ ] Projection silinip yeniden kurulabilir
- [ ] Data class ve deletion/legal-hold projection'a yansır
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

Bozuk index yeni namespace'te rebuild edilir; doğrulandıktan sonra alias atomik değiştirilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
