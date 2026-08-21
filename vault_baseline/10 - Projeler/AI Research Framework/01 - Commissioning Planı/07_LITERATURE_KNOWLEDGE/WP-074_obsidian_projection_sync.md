# WP-074 — Obsidian Projection, Link Integrity ve Knowledge Write-Back

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-074` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Platform Lead |
| Bağımsız doğrulayıcı | Knowledge Curator / Data Platform Lead |
| Hard dependencies | WP-028, WP-030, WP-061, WP-072, WP-073 |
| İlgili gate | G8,G9,G10 |
| İlgili kontroller | CTL-OPS-03, CTL-EPI-01 |
| İlgili ACC senaryoları | ACC-21, ACC-22, ACC-31 |

## Amaç ve beklenen sonuç

Source/claim/run/decision değişiklikleri yalnız generated zone'ları günceller; insan synthesis linkleri kontrol edilir ve concept graph derived projection olarak yeniden kurulabilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Arşiv](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-073 — Obsidian Vault, Human/Generated Zones ve Şablonlar](../07_LITERATURE_KNOWLEDGE/WP-073_obsidian_vault_modeli.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-074-T01 | Event-driven generated block renderer yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-074-T02 | AIRL ID link resolver/backlink index kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-074-T03 | Human edit detection ve three-way zone merge uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-074-T04 | Broken/orphan link report ve curator queue ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-074-T05 | Concept/entity edge extraction'ı derived graph'a bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-074-T06 | Full vault projection rebuild procedure yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Obsidian projection service`
- `Link checker`
- `Human-preservation diff`
- `Concept graph projection`
- `Rebuild runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Human edit while generated refresh
- Broken source/claim link
- Full projection rebuild
- Superseded claim banner update
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Renderer insan zone'una yazamaz
- [ ] Broken material link G9'u bloklayabilir
- [ ] Derived graph kaybı vault/canonical kayıt kaybı değildir
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

Projection yeni branch'te rebuild ve diff review sonrası merge edilir; conflict curator queue'ya gider.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
