# WP-114 — Operations, DR ve Restore Kabul Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-114` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Independent DR Witness / Internal Audit |
| Hard dependencies | WP-025, WP-026, WP-028, WP-030, WP-031, WP-052, WP-099, WP-101, WP-109 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-OPS-02, CTL-OPS-03 |
| İlgili ACC senaryoları | ACC-21, ACC-27, ACC-28, ACC-40 |

## Amaç ve beklenen sonuç

Regional/control-plane kaybı, registry/object/event/graph/Zotero restore ve audit integrity en az iki bağımsız tatbikatla RPO/RTO hedeflerini karşılar.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-109 — Kırk Acceptance Senaryosu Registry ve Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-114-T01 | DR-1 component restore ve DR-2 regional/management-plane restore planla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-114-T02 | Postgres PITR, object, NATS, Temporal, registry, audit ve projections restore et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-114-T03 | Zotero full resync ve graph/vault rebuild yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-114-T04 | Workflow/run/claim/source/artifact integrity query'lerini çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-114-T05 | On-call/incident/communication ve decision timeline'ı ölç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-114-T06 | DR dossier, gaps ve sign-off üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Two DR drill reports`
- `Restore manifests`
- `Integrity query results`
- `RPO/RTO scorecard`
- `DR sign-off`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-21,27,28,40
- Temporal open workflow continuity
- Object/audit hash integrity
- Projection rebuild
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] İki restore drill PASS
- [ ] Workflow state RPO=0 ve approved RTO
- [ ] Canonical/derived integrity queries PASS
- [ ] Açık critical DR gap yok
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

DR failure cutover'ı bloklar; restore environment karantinada kalır ve production baseline değiştirilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
