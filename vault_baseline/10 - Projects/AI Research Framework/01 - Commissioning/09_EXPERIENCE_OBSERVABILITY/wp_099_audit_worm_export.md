# WP-099 — WORM Audit Ledger ve Bağımsız Export

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-099` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Internal Audit Platform Lead |
| Bağımsız doğrulayıcı | Independent Auditor / Security |
| Hard dependencies | WP-011, WP-015, WP-016, WP-025, WP-026, WP-028, WP-049, WP-055, WP-056, WP-059, WP-075, WP-082, WP-096 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-GOV-01, CTL-OPS-03 |
| İlgili ACC senaryoları | ACC-40 |

## Amaç ve beklenen sonuç

Policy, identity, model, tool, workflow, source, claim, artifact, cost ve human decision olayları hash-zincirli/WORM kayıtta tutulur ve proje bazında doğrulanabilir export edilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-059 — Supply-Chain Admission, Sigstore ve SLSA Policy](../06_EXECUTION_SECURITY/wp_059_supply_chain_admission.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-099-T01 | Audit event canonicalization ve sequence/hash chain yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-099-T02 | WORM store/retention/access separation kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-099-T03 | Sensitive field encryption/redaction ve audit-of-audit ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-099-T04 | Project/time/actor/control export API yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-099-T05 | Signature/manifest/verifier CLI oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-099-T06 | Tamper/gap detection ve incident trigger ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Audit Ledger`
- `Hash-chain service`
- `Audit export/verify tooling`
- `Retention/access policy`
- `Integrity dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Record tamper detection
- Missing sequence gap
- Unauthorized delete/modify deny
- Full project export chain verify
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Audit administrator kayıtları değiştiremez
- [ ] Export complete policy/model/tool/cost/artifact/decision zinciri taşır
- [ ] Retention legal hold'a uyar
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

Bozuk replica sağlam WORM copy'den restore edilir; hash gap critical incident ve cutover blocker olur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
