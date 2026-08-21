# WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-062` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Source Resolver Lead |
| Bağımsız doğrulayıcı | Knowledge Curator / Citation Auditor |
| Hard dependencies | WP-017, WP-050, WP-058, WP-061 |
| İlgili gate | G3,G10 |
| İlgili kontroller | CTL-LIT-01 |
| İlgili ACC senaryoları | ACC-03, ACC-28 |

## Amaç ve beklenen sonuç

DOI, PMID, arXiv, ISBN, URL, title/author/year ve file hash sinyalleri açıklanabilir confidence ile tek SourceRecord'a çözülür; belirsiz çakışmalar insana gider.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-062-T01 | Identifier normalization/resolver zinciri yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-062-T02 | Crossref ve provider lookup'u broker üzerinden bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-062-T03 | Exact/fuzzy candidate generation ve match feature'larını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-062-T04 | Auto-merge güvenli eşiklerini küçük kurallarla uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-062-T05 | ConflictCase/curator queue ve split/merge lineage yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-062-T06 | Duplicate metrics ve known-item test seti kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Source Resolver service`
- `Match rules/features`
- `Conflict queue`
- `Known-item/dedup test corpus`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Aynı DOI duplicate önleme
- Aynı başlık farklı eser ayrımı
- Çelişen title/year manual case
- Cross-library Zotero duplicate mapping
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Belirsiz match sessiz auto-merge olmaz
- [ ] Merge bütün external binding ve eski referansları korur
- [ ] Duplicate tespiti Zotero kütüphane sınırına bağlı değildir
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

Yanlış merge split operation ile düzeltilir; affected manifests/claims için ImpactCase açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
