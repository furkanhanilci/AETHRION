# WP-038 — Human Update, Cancellation ve Compensation Semantiği

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-038` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Control Plane Lead |
| Bağımsız doğrulayıcı | Governance Lead / Tool Platform Lead |
| Hard dependencies | WP-004, WP-013, WP-016, WP-032, WP-033 |
| İlgili gate | G1,G8,G9 |
| İlgili kontroller | CTL-GOV-03, CTL-OPS-01 |
| İlgili ACC senaryoları | ACC-25, ACC-26, ACC-35 |

## Amaç ve beklenen sonuç

İnsan kararları doğrulanmış Temporal Update ile, iptal ve dış yan etkiler ise açık compensation planıyla güvenli biçimde işlenir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/wp_033_gate_service_records.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-038-T01 | Decision Update authentication/idempotency yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-038-T02 | Evidence snapshot ve actor context doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-038-T03 | Cancel scope ve child/activity propagation tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-038-T04 | Lease revoke/sandbox stop/tool compensation adımlarını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-038-T05 | Immutable artifact INVALIDATED davranışını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-038-T06 | Timeout/escalation timer'larını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Human Update API`
- `Cancellation contract`
- `Compensation registry`
- `Decision authentication tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Duplicate approval tek karar
- Forged/expired actor deny
- Mid-tool timeout compensation
- Cancel sonrası artifact retention
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Signal serbest payload ile gate geçiremez
- [ ] Cancel canonical evidence'i silmez
- [ ] Compensation başarısızlığı reconciliation/incident açar
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

Update deployment rollback'unda workflow version uyumu korunur; hatalı insan kararı revoke+supersede edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
