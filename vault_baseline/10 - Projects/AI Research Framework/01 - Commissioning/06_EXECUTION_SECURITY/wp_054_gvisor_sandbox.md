# WP-054 — gVisor Sandbox ve Execution Cell Lifecycle

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-054` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Execution Security Lead |
| Bağımsız doğrulayıcı | Red Team / SRE |
| Hard dependencies | WP-006, WP-014, WP-027, WP-049, WP-052, WP-053 |
| İlgili gate | G5,Engineering |
| İlgili kontroller | CTL-SEC-04, CTL-SEC-05 |
| İlgili ACC senaryoları | ACC-15, ACC-17 |

## Amaç ve beklenen sonuç

Her autonomous code execution resolve→allocate→attest→execute→capture→destroy aşamalarında digest-pinned, no-privilege, scoped mount ve forensic evidence üreten geçici hücrede çalışır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-054-T01 | RuntimeClass/gVisor ve seccomp/capability baseline kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-054-T02 | Ephemeral workspace/mount/path policy uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-054-T03 | OCI signature/SBOM attestation gate bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-054-T04 | CPU/memory/time/process limits ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-054-T05 | Artifact capture/hash/upload ve teardown yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-054-T06 | Forensic snapshot ve escape detection kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Sandbox profiles`
- `Execution Cell controller`
- `SandboxAttestation`
- `Capture/destroy workflow`
- `Red-team tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Host mount/privilege/syscall escape deny
- Unsigned/mutable image deny
- Resource bomb termination
- Artifact capture then destroy
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Agent host kernel/credential/network'e doğrudan erişemez
- [ ] Cell expiry sonunda credential ve compute yok edilir
- [ ] Artifact hash/attestation workflow'a döner
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

Şüpheli cell contain/stop edilir, forensic snapshot karantinaya alınır; node drain/reimage runbook'u çalışır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
