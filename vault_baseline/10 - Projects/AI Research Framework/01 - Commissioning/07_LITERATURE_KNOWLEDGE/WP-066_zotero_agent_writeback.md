# WP-066 — Agent Candidate ve Used-Source Write-Back

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-066` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Platform Lead |
| Bağımsız doğrulayıcı | Knowledge Curator / Security |
| Hard dependencies | WP-012, WP-017, WP-049, WP-050, WP-061, WP-062, WP-064 |
| İlgili gate | G3,G5 |
| İlgili kontroller | CTL-LIT-03, CTL-OPS-01 |
| İlgili ACC senaryoları | ACC-02, ACC-03, ACC-35 |

## Amaç ve beklenen sonuç

Agent'ın bulduğu adaylar ile gerçekten claim/run tarafından kullanılan kaynaklar yalnız izinli grup koleksiyonlarına threshold, conditional write ve SyncReceipt ile yazılır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-064 — Zotero Kütüphane, Koleksiyon ve Yetki Modeli](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_kutuphane_yetki.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-066-T01 | Candidate/Used write eligibility kuralını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-066-T02 | SourceRecord→Zotero item field mapping yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-066-T03 | Agent-owned item/field marker'larını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-066-T04 | Read–merge–If-Unmodified-Since-Version PATCH akışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-066-T05 | Collection membership tam liste semantiğini güvenli yönet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-066-T06 | Attachment/license ve note policy'sini uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-066-T07 | SyncReceipt/outbox event üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Zotero write-back service`
- `Field mapping`
- `Eligibility policy`
- `SyncReceipt ledger`
- `Connector tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Candidate write idempotency
- Used source priority write
- 412 conflict reconcile
- Human-curated item direct patch deny
- Wrong collection deny
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Sırf bulundu diye bütün kaynaklar write-back olmaz
- [ ] HUMAN_CURATED kayda agent yalnız UpdateProposal üretir
- [ ] Her write item version ve policy decision taşır
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

Uncertain/timeout write tekrar edilmeden remote read ile reconcile edilir; connector feature flag ile durdurulur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
