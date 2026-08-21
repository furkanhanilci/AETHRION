# WP-055 — SPIFFE/SPIRE Workload Identity ve Vault

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-055` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Identity Platform Lead |
| Bağımsız doğrulayıcı | Security / Internal Audit |
| Hard dependencies | WP-004, WP-016, WP-021, WP-025, WP-031, WP-049, WP-051, WP-052 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-SEC-03, CTL-GOV-01 |
| İlgili ACC senaryoları | ACC-25, ACC-26 |

## Amaç ve beklenen sonuç

Human, service, worker ve sandbox aktörleri uzun ömürlü paylaşılan secret yerine attested identity ve kısa ömürlü purpose-bound credential kullanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/WP-004_insan_karar_sla_delegasyon.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-051 — Dört Trust Zone ve Ağ Segmentasyonu](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-055-T01 | SPIRE server/agent trust domain kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-055-T02 | Service/workload registration selectors yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-055-T03 | Vault auth method, secret engine ve lease policy kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-055-T04 | Human OIDC/MFA/RBAC ve decision actor binding'i bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-055-T05 | Credential injection/rotation/revoke telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-055-T06 | Break-glass two-person workflow'u kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `SPIRE/Vault deployments`
- `Identity registry mapping`
- `Lease policies`
- `Break-glass procedure`
- `Identity audit dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Wrong workload selector deny
- Expired lease access deny
- Task cancel lease revoke
- Forged approval identity deny
- Break-glass audit
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Shared static production credential yoktur
- [ ] Lease task/purpose/target scope taşır
- [ ] Human decision verified MFA context'e bağlıdır
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

Compromised identity/lease revoke edilir; affected workload pause ve incident/impact scan açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
