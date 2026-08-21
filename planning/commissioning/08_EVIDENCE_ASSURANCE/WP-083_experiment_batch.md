# WP-083 — ExperimentBatch ve Staged Execution

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-083` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Scientific Engineering Lead |
| Bağımsız doğrulayıcı | Methodologist / FinOps / SRE |
| Hard dependencies | WP-032, WP-035, WP-045, WP-053, WP-054, WP-082 |
| İlgili gate | G4,G5 |
| İlgili kontroller | CTL-CST-01, CTL-DAT-01 |
| İlgili ACC senaryoları | ACC-09, ACC-33, ACC-39 |

## Amaç ve beklenen sonuç

Deneyler smoke→baseline→small sweep→full run sırasıyla, başarı/stop/budget ölçütleri ve checkpoint'lerle kontrollü batch workflow'unda yürür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-083-T01 | ExperimentBatch workflow ve batch/item state yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-083-T02 | Staged compute promotion checks kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-083-T03 | Parameter/seed matrix ve fan-out caps uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-083-T04 | Checkpoint/preemption/resume ve partial result behavior ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-083-T05 | Budget reservation/release ve cost attribution bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-083-T06 | Stop/pivot/negative result decision'ı uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ExperimentBatch workflow`
- `Staging policy`
- `Parameter manifest`
- `Checkpoint/recovery logic`
- `Batch report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Smoke fail prevents full run
- Budget hard stop preserves state
- Kueue preemption resume
- Partial batch result semantics
- Negative result closure
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Pahalı compute G4 ve önceki stage pass olmadan açılmaz
- [ ] Batch bütün run manifestlerini korur
- [ ] Sonuca bakıp plan/metric değiştirilemez
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

Batch pause/cancel compute ve lease'i bırakır; completed run artifactleri korunur, resume yeni lease ile yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
