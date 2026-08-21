# WP-102 — Dikey Dilim 1 — Intake → Protocol Freeze

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-102` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Research Workflow Lead |
| Bağımsız doğrulayıcı | Assurance / Project Decision Owner |
| Hard dependencies | WP-034, WP-035, WP-056, WP-091, WP-092, WP-093, WP-100, WP-101 |
| İlgili gate | G0,G1,G2 |
| İlgili kontroller | CTL-GOV-01, CTL-GOV-03 |
| İlgili ACC senaryoları | ACC-06, ACC-25, ACC-26 |

## Amaç ve beklenen sonuç

Gerçekçi bir R1 ve bir R3 proje, G0–G2 boyunca risk/control plan, charter, protocol, human decision ve audit zinciriyle ilerler.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-034 — G0 Intake ve G1 Charter Workflow'ları](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-091 — Lab Cockpit Bilgi Mimarisi ve Uygulama Kabuğu](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md), [WP-092 — Project Workspace ve G0–G10 Gate Timeline](../09_EXPERIENCE_OBSERVABILITY/WP-092_project_gate_timeline.md), [WP-093 — Human Decision Queue ve Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md), [WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md), [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-102-T01 | R1/R3 synthetic project fixtures hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-102-T02 | Cockpit'ten Intake başlat | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-102-T03 | Risk/Execution/Independence policy kararlarını doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-102-T04 | Charter/SLA/delegation ve protocol freeze'i çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-102-T05 | Budget reservation/audit/telemetry zincirini kontrol et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-102-T06 | Revise/block/reopen path'lerini test et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Vertical slice dossier`
- `R1/R3 project histories`
- `Trace/audit/decision evidence`
- `Integration findings`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Happy path R1/R3
- Unknown risk BLOCKED
- Expired delegation
- Protocol material amendment
- Budget unavailable
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] G0–G2 bütün canonical kayıtları bağlıdır
- [ ] R3 daha derin assurance alır ama aynı gate'leri kullanır
- [ ] Açık critical integration finding yoktur
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

Dilim başarısızsa production benzeri proje kapatılır; synthetic artifacts retained, correction package açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
