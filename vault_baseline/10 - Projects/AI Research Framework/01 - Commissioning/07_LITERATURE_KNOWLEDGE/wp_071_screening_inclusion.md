# WP-071 — Screening, Inclusion/Exclusion ve Coverage

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-071` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Lead |
| Bağımsız doğrulayıcı | Methodologist / Blind Literature Reviewer |
| Hard dependencies | WP-007, WP-017, WP-061, WP-062, WP-069, WP-070 |
| İlgili gate | G3 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Title/abstract ve full-text screening; reason-coded inclusion/exclusion, disagreement, sampling ve risk bazlı bağımsız review ile frozen sete hazır hale gelir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-069 — SearchProtocol ve LiteratureCampaign Orkestrasyonu](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md), [WP-070 — İnsan + Agent Çift Yönlü Literatür Keşfi](../07_LITERATURE_KNOWLEDGE/wp_070_dual_directional_literature.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-071-T01 | Screening criteria/rubric ve reason code'ları tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-071-T02 | Title/abstract ve full-text queue'larını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-071-T03 | Human/agent blind assignments ve conflict-of-interest kontrolü ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-071-T04 | R1/R2/R3 dual-review/sampling derinliği uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-071-T05 | DisagreementCase ve arbiter escalation bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-071-T06 | PRISMA-benzeri flow/coverage/unknown raporu üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Screening service`
- `Decision queue`
- `Reason taxonomy`
- `Coverage/flow report`
- `Screening calibration set`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Include/exclude boundary calibration
- Conflicting reviewers case
- Missing full text state
- R3 independence requirement
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her exclusion gerekçe ve actor taşır
- [ ] Material disagreement gizlenmez
- [ ] Unavailable source INCLUDED diye otomatik sayılmaz
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

Kriter değişimi amendment ve affected-decision rescreen kuyruğu açar; eski decisions korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
