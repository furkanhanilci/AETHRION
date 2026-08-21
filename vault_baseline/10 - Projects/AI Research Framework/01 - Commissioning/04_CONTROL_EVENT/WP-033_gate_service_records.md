# WP-033 — Gate Service ve GateRecord Değerlendirmesi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-033` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Control Plane Lead |
| Bağımsız doğrulayıcı | Assurance Lead |
| Hard dependencies | WP-008, WP-016, WP-018, WP-032 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-GOV-01, CTL-EPI-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Gate artifact, policy, review, budget ve blocker girdilerini deterministik değerlendirip Temporal history'ye PASS/REVISE/REJECT/BLOCKED/DISAGREEMENT sonucu yazan servis oluşur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-033-T01 | Gate evaluation input adapter'larını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-033-T02 | Hard/soft check ve verdict precedence uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-033-T03 | Aynı oturumda kapanan gate'ler için ayrı kayıt üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-033-T04 | Gate explanation ve failed check listesi oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-033-T05 | Reopen/supersession ve evidence snapshot bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Gate Service`
- `GateRecord persistence`
- `Verdict rule tests`
- `Gate explanation format`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Her gate hard-fail fixture
- Risk depth ayrı kayıt testi
- Policy/budget UNKNOWN fail-closed
- Stale input snapshot reject
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Gate sonucu Temporal event history'ye yazılmadan geçerli değildir
- [ ] Kritik blocker verdict'i PASS olamaz
- [ ] Aynı input/policy aynı verdict'i üretir
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

Hatalı gate evaluation superseding record ile düzeltilir; workflow son güvenli state'e pause edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
