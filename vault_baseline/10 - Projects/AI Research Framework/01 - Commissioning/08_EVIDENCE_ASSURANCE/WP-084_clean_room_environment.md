# WP-084 — Clean-Room Reproduction Ortamı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-084` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Reproducibility Lead |
| Bağımsız doğrulayıcı | Security / Independent SRE |
| Hard dependencies | WP-007, WP-014, WP-019, WP-026, WP-027, WP-052, WP-053, WP-054, WP-055, WP-059, WP-082 |
| İlgili gate | G7 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-03, CTL-SEC-04 |
| İlgili ACC senaryoları | ACC-19, ACC-20 |

## Amaç ve beklenen sonuç

Reproducer; producer workspace, credential, cache ve ara trace'lerinden ayrılmış, frozen manifestten kurulan temiz ortamda koşum yapar.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-059 — Supply-Chain Admission, Sigstore ve SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-084-T01 | Dedicated repro queue/node/namespace ve identity kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-084-T02 | Frozen package resolver ve image/data/code fetch doğrulaması yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-084-T03 | Producer cache/workspace/credential erişimini engelle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-084-T04 | Seed/hardware tolerance ve environment capture uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-084-T05 | Network/offline policy ve output capture bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-084-T06 | Environment destruction/forensic retention yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Clean-room platform`
- `Reproducer profile`
- `Environment resolver`
- `Isolation attestation`
- `Repro runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Producer credential/cache access deny
- Manifest-only environment build
- Different hardware tolerance
- Tampered artifact hash fail
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Reproducer producer ara çıktısını görmez
- [ ] Her input frozen digest'ten çözülür
- [ ] Clean-room attestation report'a bağlanır
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

Repro cell şüphede contain edilir; yeni temiz cell ve bağımsız credential ile run tekrar planlanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
