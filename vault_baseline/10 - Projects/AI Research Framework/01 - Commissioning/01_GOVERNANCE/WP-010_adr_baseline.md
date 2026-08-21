# WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-010` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Chief Architect |
| Bağımsız doğrulayıcı | Architecture Board |
| Hard dependencies | WP-002, WP-005, WP-006, WP-007, WP-008, WP-009 |
| İlgili gate | Program,Platform |
| İlgili kontroller | CTL-GOV-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Temporal/LangGraph/NATS, Source Registry/Zotero/Obsidian, canonical kayıt, trust zone ve cutover kararları yeniden açma tetikleyicileriyle ADR baseline'ına alınır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/WP-002_kapsam_nfr_izlenebilirlik.md), [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/WP-006_execution_profili.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-009 — Control Kataloğu, Exception ve Non-Waivable Blocker'lar](../01_GOVERNANCE/WP-009_control_exception_katalogu.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-010-T01 | Bağlayıcı kararları ADR'lara ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-010-T02 | Alternatifleri, trade-off ve neden reddedildiğini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-010-T03 | Decisionsın re-open trigger'larını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-010-T04 | Canonical owner ve trust boundary etkilerini ilişkilendir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-010-T05 | ADR→WP→control mapping kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Signed ADR bundle`
- `Rejected alternatives register`
- `Reopen trigger register`
- `Architecture baseline digest`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Birbiriyle çelişen ADR taraması
- Her material package için ADR link kontrolü
- Reopen trigger tabletop testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Canonical sahiplik ve motor sınırlarında çelişki yoktur
- [ ] Her bağlayıcı karar accountable approver taşır
- [ ] Baseline digest release manifest'e girebilir
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

Yeni baseline kabul edilmezse son imzalı ADR bundle geçerli kalır; uygulama paketleri READY olmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
