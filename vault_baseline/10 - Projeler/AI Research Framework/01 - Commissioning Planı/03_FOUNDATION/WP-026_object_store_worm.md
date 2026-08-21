# WP-026 — Content-Addressed Object Store ve WORM

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-026` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Data Platform Lead |
| Bağımsız doğrulayıcı | Archivist / Security |
| Hard dependencies | WP-021, WP-014 |
| İlgili gate | G3–G10 |
| İlgili kontroller | CTL-DAT-03, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-23, ACC-27 |

## Amaç ve beklenen sonuç

PDF, dataset, artifact, evidence ve publication bytes content hash, object lock, encryption, retention ve legal-hold ile immutable saklanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-026-T01 | Bucket/namespace ve data-class ayrımını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-026-T02 | Content-addressed key ve multipart hash doğrulaması uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-026-T03 | Object lock/WORM ve retention policy aç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-026-T04 | Encryption key ve access logging bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-026-T05 | Quarantine, canonical ve publication alanlarını ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-026-T06 | Replication/restore ve bit-rot scan kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Object storage IaC`
- `Object address service`
- `Retention matrix`
- `Integrity scan job`
- `Restore procedure`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Aynı key overwrite deny
- Corrupt byte hash detection
- Cross-region restore ve legal-hold testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Canonical object overwrite edilemez
- [ ] Her object ArtifactRecord ve hash'e bağlıdır
- [ ] Retention delete policy owner/approval olmadan çalışmaz
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

Bozuk replica sağlam hash'ten onarılır; restore yeni physical object üretir ve canonical reference doğrulanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
