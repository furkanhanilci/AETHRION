# WP-019 — Run, Environment ve Reproduction Şemaları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-019` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Experiment Platform Lead |
| Bağımsız doğrulayıcı | Reproducibility Engineer |
| Hard dependencies | WP-011, WP-014, WP-018 |
| İlgili gate | G4–G7 |
| İlgili kontroller | CTL-DAT-01, CTL-EPI-03 |
| İlgili ACC senaryoları | ACC-19, ACC-20 |

## Amaç ve beklenen sonuç

Deney ve doğrulama koşuları dataset, code, environment, prompt, model snapshot, seed, metric ve tolerance ile tam manifestlenir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/WP-011_kimlik_korelasyon_standardi.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-019-T01 | RunManifest input/output ve lineage alanlarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-019-T02 | Protocol/Baseline/AnalysisPlan referanslarını zorunlu kıl | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-019-T03 | EnvironmentManifest hardware/driver/image/SBOM alanlarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-019-T04 | Repeatability/Reproducibility/Robustness/Replication türlerini ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-019-T05 | ReproductionReport tolerance ve root-cause şemasını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Run schema bundle`
- `EnvironmentManifest`
- `ReproductionReport`
- `Tolerance policy examples`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Eksik seed/model/image hash negatif testi
- Aynı manifest determinism fixture
- Repro türü yanlış etiketleme testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Run bütün frozen input sürümlerini taşır
- [ ] Reproduction sonucu pass/fail ve tolerance gerekçesi taşır
- [ ] Replication reproduction yerine geçmez ve tersi
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

Eksik manifestli run INVALID/EXPLORATORY kalır; publication veya critical claim'e promote edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
