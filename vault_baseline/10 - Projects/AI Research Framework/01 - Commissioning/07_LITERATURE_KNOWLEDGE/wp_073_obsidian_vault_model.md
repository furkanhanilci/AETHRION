# WP-073 — Obsidian Vault, Human/Generated Zones ve Şablonlar

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-073` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Lead |
| Bağımsız doğrulayıcı | Knowledge Curator / Governance |
| Hard dependencies | WP-012, WP-017, WP-022, WP-061, WP-072 |
| İlgili gate | G3,G8,G10 |
| İlgili kontroller | CTL-OPS-03 |
| İlgili ACC senaryoları | ACC-22 |

## Amaç ve beklenen sonuç

Obsidian insan sentezi; project, source, concept, claim, decision ve result note'larında stable AIRL IDs, Git history ve korunmuş human/generated bloklarla çalışır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-022 — Repository Topolojisi ve Kod Sahipliği](../03_FOUNDATION/wp_022_repository_topology.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-073-T01 | Vault/dizin/tag/property standardı kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-073-T02 | Project/Source/Concept/Claim/Decision/Result templates yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-073-T03 | source_registry_id/claim_id/run_id link alanlarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-073-T04 | Human-authored ve generated fenced block semantics uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-073-T05 | Git branch/review/merge ve backup kuralını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-073-T06 | Better BibTeX key'i alias, canonical ID'yi AIRL ID yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Obsidian vault baseline`
- `Note templates`
- `Zone/merge policy`
- `Git workflow`
- `User guide`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Template/schema lint
- Generated refresh human edit preservation
- Alias/canonical ID link test
- Git restore
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Obsidian Source Registry veya Claim Ledger yerine geçmez
- [ ] İnsan serbest sentezi korunur
- [ ] Generated block provenance ve timestamp taşır
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

Bozuk generated block canonical kayıttan rebuild edilir; insan Git history'si restore edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
