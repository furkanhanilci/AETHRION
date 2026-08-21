# WP-107 — Engineering Dikey Dilim — Spec → Worktree → Signed Release

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-107` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Engineering Lead |
| Bağımsız doğrulayıcı | Independent Technical Reviewer / Reproducer |
| Hard dependencies | WP-023, WP-024, WP-027, WP-032, WP-045, WP-047, WP-048, WP-049, WP-054, WP-059, WP-082, WP-086, WP-087, WP-089, WP-090, WP-096 |
| İlgili gate | Engineering,G5–G9 |
| İlgili kontroller | CTL-GOV-02, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-06, ACC-17, ACC-23 |

## Amaç ve beklenen sonuç

Bir standart ve bir kritik kod değişikliği spec, reality check, isolated worktree, deterministic verify, blind review, reproducer, architecture gate ve signed package akışından geçer.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-023 — Git, Worktree ve Protected Path Politikası](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md), [WP-024 — CI Temeli ve Deterministik Kalite Kapıları](../03_FOUNDATION/WP-024_ci_kalite_kapilari.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-048 — Codex, OpenCode ve Direct Worker Adapter'ları](../05_MODEL_AGENT_TOOL/WP-048_codex_opencode_adapters.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-059 — Supply-Chain Admission, Sigstore ve SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-086 — Frozen ve Kör Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate ve Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-107-T01 | B/C risk fixtures ve technical spec oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-107-T02 | Plan reality check/protected path/worktree aç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-107-T03 | Agent implementasyonu ve CI verification çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-107-T04 | Frozen diff blind/cross-family review et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-107-T05 | HIGH/BLOCKER reproducer ve correction loop uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-107-T06 | Re-freeze/re-review, signed build ve human merge decision yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Engineering vertical dossier`
- `Frozen review packets`
- `Validated findings`
- `Signed OCI/release`
- `Merge DecisionRecord`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Protected path deny
- Worker self-approval deny
- Validated finding correction
- Unsigned release deny
- Migration rollback dry-run
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Aynı target commit bütün evidence'ta korunur
- [ ] Yalnız validated finding correction'a girer
- [ ] Critical değişiklik farklı-aile/insan review ve merge kararı taşır
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

Failed release branch/worktree karantinaya alınır; signed prior artifact production pointer'ı değişmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
