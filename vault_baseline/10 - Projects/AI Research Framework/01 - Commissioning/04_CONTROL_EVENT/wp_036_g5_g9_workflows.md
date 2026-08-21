# WP-036 — G5 Execute–G9 Publish Workflow'ları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-036` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Workflow Engineering Lead |
| Bağımsız doğrulayıcı | Assurance Lead / Decision Owner |
| Hard dependencies | WP-004, WP-007, WP-008, WP-019, WP-032, WP-033, WP-035 |
| İlgili gate | G5–G9 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-01, CTL-EPI-03 |
| İlgili ACC senaryoları | ACC-08, ACC-19, ACC-20, ACC-30 |

## Amaç ve beklenen sonuç

Execution, claim freeze, blind review, reproduction, human decision ve publication gate'leri canonical artifact/decision zinciriyle çalışır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-036-T01 | G5 RunBatch dispatch/checkpoint/stop flow yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-036-T02 | G6 frozen review package ve disposition bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-036-T03 | G7 reproduction request/result/reopen akışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-036-T04 | G8 evidence-delta human decision update'ını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-036-T05 | G9 citation/provenance/security release checklist bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-036-T06 | Cancellation/compensation ve supersession ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `G5–G9 workflows`
- `Review/repro integration contracts`
- `Decision update flow`
- `Publication transition`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Execution partial fail recovery
- Unresolved critical review BLOCKED
- G7 tolerance fail→CHALLENGED
- Invalid approval/publication lineage negative tests
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Producer kendi acceptance'ını veremez
- [ ] G9 claim lineage incomplete ise fail
- [ ] G7 fail controlled return üretir, history silmez
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

Release öncesi hata workflow'u son güvenli gate'te pause eder; external draft side effects compensate edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
