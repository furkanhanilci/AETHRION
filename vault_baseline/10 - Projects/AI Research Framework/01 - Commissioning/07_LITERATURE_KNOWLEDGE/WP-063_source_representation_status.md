# WP-063 — Source Representation, Lisans ve Durum İzleme

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-063` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Lead |
| Bağımsız doğrulayıcı | Archivist / Safety / Citation Auditor |
| Hard dependencies | WP-014, WP-017, WP-026, WP-037, WP-050, WP-058, WP-061, WP-062 |
| İlgili gate | G3,G10 |
| İlgili kontroller | CTL-LIT-02, CTL-DAT-03 |
| İlgili ACC senaryoları | ACC-04 |

## Amaç ve beklenen sonuç

PDF, HTML, preprint, dataset documentation ve correction/retraction temsilcileri hash, format, lisans, parser ve availability ile sürümlenir; durum değişimi ImpactScan tetikler.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-037 — G10 Temporal Schedule ve Kısa ImpactScan](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-063-T01 | Representation ingest/hash/license/access metadata yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-063-T02 | Format-specific structural locator map'ini üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-063-T03 | Version/correction/preprint→published ilişkilerini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-063-T04 | Crossref/Crossmark/retraction/status feed adapter'larını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-063-T05 | Periodic status Schedule ve event üretimini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-063-T06 | Unavailable old representation ve retention davranışını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Representation ingest service`
- `License/status policy`
- `Status monitor`
- `Format locator metadata`
- `Retention mapping`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Yeni PDF eski bytes'ı değiştirmez
- Retraction event ImpactCase
- License deny hash-only fallback
- Old representation availability/reanchor testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Eski immutable representation erişilebiliyorsa evidence orphan olmaz
- [ ] Status değişimi eski manifesti mutate etmez
- [ ] Lisans izin vermiyorsa bytes değil kimlik/hash saklanır
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

Hatalı status yeni status event'iyle supersede edilir; retraction etkisi manuel silinmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
