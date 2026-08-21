# WP-104 — Dikey Dilim 3 — Baseline → Run → Claim/Evidence

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-104` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Scientific Engineering Lead |
| Bağımsız doğrulayıcı | Methodologist / Evidence Auditor |
| Hard dependencies | WP-035, WP-054, WP-075, WP-076, WP-077, WP-078, WP-079, WP-080, WP-081, WP-082, WP-083, WP-095, WP-096, WP-097, WP-100 |
| İlgili gate | G4,G5 |
| İlgili kontroller | CTL-DAT-01, CTL-EPI-01, CTL-CST-01 |
| İlgili ACC senaryoları | ACC-08, ACC-09, ACC-23, ACC-32, ACC-39 |

## Amaç ve beklenen sonuç

Frozen protocol/literature/baseline'dan staged run çalışır; sonuç artifact, evidence span ve claim dependency/assessment zincirine dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-078 — Yapılandırılmış Evidence Extraction Hattı](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard ve Çalışma Kalitesi Değerlendirmesi](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md), [WP-080 — Claim–Citation Entailment, Scope ve Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline ve Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-083 — ExperimentBatch ve Staged Execution](../08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.md), [WP-095 — Claim/Evidence Explorer ve Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-097 — Langfuse Model/Agent Trace ve Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/WP-097_langfuse_llm_trace.md), [WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-104-T01 | Baseline/falsification ve preflight manifest oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-104-T02 | Staged experiment/smoke/full run çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-104-T03 | Model/tool/sandbox/artifact/cost correlation doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-104-T04 | Evidence extraction/anchor/trust/citation audit yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-104-T05 | Claim/dependency/state ve negative result path'ini oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-104-T06 | Cockpit/graph/audit'te lineage sorgula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Run/claim vertical dossier`
- `Run manifests/artifacts`
- `Claim/Evidence records`
- `Cost/trace/audit evidence`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Missing manifest run deny
- Budget hard stop
- Artifact overwrite deny
- Contradictory evidence state
- Negative result retained
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Run complete frozen lineage taşır
- [ ] Material claim locator ve source status'a bağlıdır
- [ ] Self-declaration mekanik evidence yerine geçmez
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

Run/claim synthetic projectte invalidate edilir; canonical evidence retained ve correction yeni version olarak yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
