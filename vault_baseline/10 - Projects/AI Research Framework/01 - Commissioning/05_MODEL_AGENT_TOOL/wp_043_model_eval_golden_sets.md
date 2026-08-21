# WP-043 — Rol Bazlı Model Eval ve Golden Set Yönetimi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-043` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Eval Office |
| Bağımsız doğrulayıcı | Independent Domain/Assurance Reviewer |
| Hard dependencies | WP-007, WP-014, WP-018, WP-019, WP-020, WP-029, WP-042 |
| İlgili gate | Platform,G6 |
| İlgili kontroller | CTL-MOD-01, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-07, ACC-37 |

## Amaç ve beklenen sonuç

Planner, scout, extractor, coder, reviewer ve arbiter rolleri için contamination-korumalı, versioned eval setleri ve ölçüm rubrikleri oluşur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-029 — MLflow Deney ve Eval Tracking Temeli](../03_FOUNDATION/wp_029_mlflow_foundation.md), [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-043-T01 | Role-specific capability/failure taxonomy çıkar | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-043-T02 | Golden, adversarial ve regression setlerini hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-043-T03 | Dataset split/access/canary/contamination kontrollerini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-043-T04 | Deterministic grader ve human rubric'leri kalibre et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-043-T05 | Validated precision, incremental finding, cost/triage/latency metriklerini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-043-T06 | Eval manifest ve release sürecini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Eval dataset manifests`
- `Role eval harness`
- `Grader/rubric bundle`
- `Contamination controls`
- `Eval scorecard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Known-answer/edge-case validation
- Inter-rater calibration
- Golden item access negative test
- Order/verbosity/self bias probes
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Eval seti production prompt/log yetkisinden ayrıdır
- [ ] Tek aggregate skor role eligibility'nin yerini almaz
- [ ] Contamination tespitinde set invalidate edilir
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

Contaminated bundle INVALIDATED olur; yeni version oluşturulur ve etkilenen profile'lar re-evaluate edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
