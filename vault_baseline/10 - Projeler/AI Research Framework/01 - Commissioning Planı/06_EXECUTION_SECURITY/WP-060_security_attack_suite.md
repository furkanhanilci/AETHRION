# WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-060` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Red Team Lead |
| Bağımsız doğrulayıcı | Safety Owner / Commissioning Board |
| Hard dependencies | WP-049, WP-050, WP-051, WP-052, WP-053, WP-054, WP-055, WP-056, WP-057, WP-058, WP-059 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-SEC-01..05, CTL-OBS-02 |
| İlgili ACC senaryoları | ACC-05, ACC-06, ACC-09, ACC-15, ACC-16, ACC-17, ACC-18, ACC-25, ACC-32, ACC-37 |

## Amaç ve beklenen sonuç

Prompt injection, tool misuse, secret exfiltration, memory poisoning, sandbox escape, supply chain, data poisoning, reviewer manipulation, cost denial ve audit tampering saldırıları otomatik/manuel suite olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-051 — Dört Trust Zone ve Ağ Segmentasyonu](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP ve Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-059 — Supply-Chain Admission, Sigstore ve SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-060-T01 | Threat-control map'ten attack case'leri türet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-060-T02 | Canary secret, malicious PDF/repo/tool fixtures hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-060-T03 | Tool confused-deputy/target scope testleri yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-060-T04 | Sandbox/kernel/network/cost/audit saldırıları ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-060-T05 | Expected deny/contain/detect/respond evidence tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-060-T06 | Regression schedule ve finding pipeline bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Agentic attack suite`
- `Malicious fixture corpus`
- `Red-team report template`
- `Security regression schedule`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-05/06/09/15/16/17/18/25/32/37 saldırı yolları
- Audit tamper/hash verification
- Memory poisoning human-zone overwrite
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical attack'ların tamamı deny/contain ve audit üretir
- [ ] Açık critical finding=0
- [ ] False positive correction kontrolü zayıflatmadan yapılır
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

Failed suite deployment/cutover'ı bloklar; correction yalnız validated finding ile, sonra tam etkilenen regression tekrar çalışır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
