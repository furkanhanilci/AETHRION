# WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-011` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Data Platform Lead |
| Bağımsız doğrulayıcı | Security Architect |
| Hard dependencies | WP-010 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-OBS-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Project, workflow, gate, task, actor, source, representation, claim, evidence, run, artifact, review, decision, cost ve event kimlikleri çakışmasız ve sorgulanabilir olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı](../01_GOVERNANCE/WP-010_adr_baseline.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-011-T01 | UUIDv7/opaque ID formatlarını ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-011-T02 | project→workflow→run→artifact→claim/cost korelasyon zincirini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-011-T03 | Actor human/model/service kimlik alanlarını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-011-T04 | External Zotero/DOI/ORCID gibi locator'ları alias olarak modelle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-011-T05 | ID üretme, tombstone ve merge kurallarını belirle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Identifier Standard`
- `Correlation envelope`
- `ID library contract`
- `Merge/tombstone rules`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Uniqueness/property test
- Cross-service correlation fixture
- Alias collision ve merge testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Canonical ID external key'e bağımlı değildir
- [ ] Her event/artifact actor ve correlation taşır
- [ ] Merge eski referansları kırmaz
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

Hatalı ID mapping tombstone+replacement event ile düzeltilir; geçmiş kayıt overwrite edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
