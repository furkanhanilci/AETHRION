# WP-057 — Default-Deny Egress Proxy, DLP ve Allowlist

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-057` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Network Security Lead |
| Bağımsız doğrulayıcı | Red Team / Privacy Owner |
| Hard dependencies | WP-006, WP-021, WP-049, WP-051, WP-055, WP-056 |
| İlgili gate | G3,G5,Platform |
| İlgili kontroller | CTL-SEC-02, CTL-OBS-02 |
| İlgili ACC senaryoları | ACC-16, ACC-18, ACC-32 |

## Amaç ve beklenen sonuç

Execution ve service dış trafiği domain/IP/method/purpose/data-class allowlist, secret/PII detector ve tam audit üzerinden geçer.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-051 — Dört Trust Zone ve Ağ Segmentasyonu](../06_EXECUTION_SECURITY/wp_051_trust_zone_network.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-057-T01 | Explicit proxy/DNS policy ve TLS strategy kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-057-T02 | Tool/provider domain registry ve purpose allowlist bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-057-T03 | Request/response size/MIME/method constraints ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-057-T04 | Secret/PII/D3-D4 DLP detector uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-057-T05 | Canary secret ve anomalous volume alert kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-057-T06 | Emergency deny/revoke ve exception akışını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Egress proxy`
- `Allowlist registry`
- `DLP pipeline`
- `Egress audit/alerts`
- `Exception runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Unknown domain deny
- Secret canary exfil deny
- D3 public endpoint deny
- DNS bypass/raw IP deny
- Approved connector pass
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Direct internet route yoktur
- [ ] DLP deny lease revoke ve incident üretebilir
- [ ] Sensitive body loglarda maskelenir
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

False-positive allowlist değişikliği süreli exception ile; proxy arızasında fail-closed veya policy tanımlı local-only route.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
