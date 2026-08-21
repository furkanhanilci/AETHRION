# WP-092 — Project Workspace ve G0–G10 Gate Timeline

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-092` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Experience Lead |
| Bağımsız doğrulayıcı | Research Operations / Assurance |
| Hard dependencies | WP-008, WP-032, WP-033, WP-034, WP-035, WP-036, WP-037, WP-091 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-GOV-01, CTL-OPS-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Her proje; current gate, frozen versions, blockers, budget, owner, residual risk, reopen history ve sonraki eylemi açıklayan çalışma yüzeyine kavuşur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-034 — G0 Intake ve G1 Charter Workflow'ları](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-036 — G5 Execute–G9 Publish Workflow'ları](../04_CONTROL_EVENT/wp_036_g5_g9_workflows.md), [WP-037 — G10 Temporal Schedule ve Kısa ImpactScan](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-091 — Lab Cockpit Bilgi Mimarisi ve Uygulama Kabuğu](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-092-T01 | Project overview/charter/control profile views yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-092-T02 | G0–G10 timeline ve GateRecord diff göster | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-092-T03 | Artifact/manifest/review/repro/decision panels bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-092-T04 | BLOCKED/REVISE/DISAGREEMENT explanation tasarla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-092-T05 | Reopen/supersession/history karşılaştırması ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-092-T06 | Authorized command/update formlarını Temporal API'ye bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Project Workspace`
- `Gate Timeline`
- `Artifact/evidence panels`
- `Command/update forms`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- G7 fail controlled return visualization
- Risk depth and separate GateRecord
- Unauthorized transition deny
- Projection lag/current canonical query
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Kullanıcı neden bloklandığını rule/evidence ile görür
- [ ] UI'dan serbest state mutation yoktur
- [ ] Eski version ve decision history erişilebilirdir
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

Frontend rollback state kaybettirmez; hatalı command API server-side policy ile reddedilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
