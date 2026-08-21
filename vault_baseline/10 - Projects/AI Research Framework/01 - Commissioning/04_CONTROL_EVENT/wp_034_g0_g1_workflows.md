# WP-034 — G0 Intake ve G1 Charter Workflow'ları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-034` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Research Operations Lead |
| Bağımsız doğrulayıcı | Project Decision Owner / Safety |
| Hard dependencies | WP-004, WP-005, WP-006, WP-013, WP-032, WP-033 |
| İlgili gate | G0,G1 |
| İlgili kontroller | CTL-GOV-01, CTL-DAT-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Talep; owner, amaç, kapsam, kabul, risk, data/tool profili, bütçe ve ControlPlan ile yürütülebilir projeye dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/wp_033_gate_service_records.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-034-T01 | IntakeRecord oluşturma/validation activity'lerini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-034-T02 | Risk/Execution/Independence profile evaluation bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-034-T03 | ProjectCharter ve acceptance authoring akışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-034-T04 | Human decision update/SLA entegrasyonu yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-034-T05 | G0/G1 GateRecord ve revise loop uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `G0/G1 workflows`
- `Intake/Charter UI API contract`
- `ControlPlan generation`
- `Gate fixtures`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Owner olmayan intake reject
- UNKNOWN risk pause
- Expired human decision escalation
- Charter revise→new version testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] G1 geçmeden downstream compute/model görevi açılmaz
- [ ] Charter test edilebilir outcome ve non-goal taşır
- [ ] Profile kararları rule ID ve owner taşır
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

Reject edilen proje tombstone değil kapanış kaydı alır; yeniden başlatma yeni charter version üretir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
