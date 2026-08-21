# WP-059 — Supply-Chain Admission, Sigstore ve SLSA Policy

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-059` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Supply Chain Security Lead |
| Bağımsız doğrulayıcı | Independent Security Reviewer |
| Hard dependencies | WP-027, WP-052, WP-054, WP-056 |
| İlgili gate | G5,Platform |
| İlgili kontroller | CTL-SEC-05, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-17, ACC-26 |

## Amaç ve beklenen sonuç

Kubernetes ve tool/runtime dağıtımları yalnız digest-pinned, imzalı, SBOM/provenance'lı ve policy-compliant artifact kabul eder.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/wp_054_gvisor_sandbox.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-059-T01 | Admission controller ve trust roots kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-059-T02 | Cosign signature/provenance/SBOM policy yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-059-T03 | Allowed builder/source repo/dependency threshold tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-059-T04 | CVE exception/expiry workflow bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-059-T05 | Tool/MCP/plugin artifact signature check ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-059-T06 | Revoke ve running workload impact davranışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Admission policies`
- `Trust root management`
- `CVE/exception workflow`
- `Revocation/impact runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Unsigned image deny
- Mutable tag deny
- Untrusted builder provenance deny
- Expired CVE exception deny
- Revoked digest workload alert
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Production unsigned artifact çalıştırmaz
- [ ] Exception süreli ve owner'lıdır
- [ ] Revocation açık/çalışan workload impact'i üretir
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

Policy false positive'de önceki signed bundle rollback; artifact allowlist manuel kalıcı bypass yapılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
