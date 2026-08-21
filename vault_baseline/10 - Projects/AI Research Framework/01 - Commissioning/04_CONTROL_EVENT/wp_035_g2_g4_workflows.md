# WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-035` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Scientific Workflow Lead |
| Bağımsız doğrulayıcı | Methodologist / Evidence Lead / Falsification Lead |
| Hard dependencies | WP-008, WP-013, WP-017, WP-019, WP-032, WP-033, WP-034 |
| İlgili gate | G2,G3,G4 |
| İlgili kontroller | CTL-EPI-02, CTL-LIT-01, CTL-CST-01 |
| İlgili ACC senaryoları | ACC-01, ACC-39 |

## Amaç ve beklenen sonuç

Yöntem, literatür seti, baseline, falsification, stop rule ve compute açma kararı sürümlü artifact ve gate'lerle dondurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-034 — G0 Intake ve G1 Charter Workflow'ları](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-035-T01 | Protocol author/review/amend workflow'u yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-035-T02 | LiteratureCampaign child/task contract bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-035-T03 | LiteratureSetManifest freeze activity'sini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-035-T04 | Baseline/FalsificationPlan validation kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-035-T05 | Leakage/contamination ve budget readiness checks ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-035-T06 | G2–G4 revise/reopen transition'larını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `G2–G4 workflows`
- `Protocol amendment flow`
- `Literature freeze integration`
- `Compute-open decision`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Material protocol change version testi
- Literature set değişimi yeni synthesis gerektirir
- Baseline post-result mutation deny
- Leakage risk hard fail
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] G4 geçmeden pahalı execution açılmaz
- [ ] Protokol ve baseline frozen hash taşır
- [ ] Yeni kaynak eski manifesti sessizce değiştirmez
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

G2/G3/G4 revise durumunda yeni artifact version açılır; önceki frozen set/run ilişkileri korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
