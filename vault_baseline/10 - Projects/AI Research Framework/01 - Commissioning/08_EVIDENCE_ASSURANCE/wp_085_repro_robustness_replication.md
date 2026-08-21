# WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-085` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Reproducibility Lead |
| Bağımsız doğrulayıcı | Assurance Lead / Statistician |
| Hard dependencies | WP-005, WP-007, WP-019, WP-077, WP-081, WP-082, WP-083, WP-084 |
| İlgili gate | G7 |
| İlgili kontroller | CTL-EPI-03 |
| İlgili ACC senaryoları | ACC-19, ACC-20 |

## Amaç ve beklenen sonuç

Dört doğrulama türü ayrı protokol, tolerance, independence ve certificate ile yürütülür; risk sınıfı gerekli minimum kombinasyonu belirler.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-081 — Protocol, Analysis, Baseline ve Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-083 — ExperimentBatch ve Staged Execution](../08_EVIDENCE_ASSURANCE/wp_083_experiment_batch.md), [WP-084 — Clean-Room Reproduction Ortamı](../08_EVIDENCE_ASSURANCE/wp_084_clean_room_environment.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-085-T01 | Verification type selector ve policy yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-085-T02 | Same code/env repeatability job kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-085-T03 | Independent environment reproducibility job kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-085-T04 | Seed/parameter/data-slice robustness matrix uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-085-T05 | Independent data/method replication request lifecycle yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-085-T06 | Tolerance/pre-registration/root-cause/disposition ve certificate üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Verification pipeline`
- `Type-specific protocols`
- `Robustness matrix`
- `Reproduction certificates`
- `Failure taxonomy`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Repeatability pass/repro fail
- Robustness edge slice fail
- Replication unavailable state
- Tolerance predeclared enforcement
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Türler birbirinin yerine geçmez
- [ ] R3 minimum clean-room ve gerekli robustness olmadan pass olmaz
- [ ] Fail claim'i CHALLENGED ve root-cause queue yapar
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

Failed certificate silinmez; corrected manifest yeni verification run ve certificate version üretir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
