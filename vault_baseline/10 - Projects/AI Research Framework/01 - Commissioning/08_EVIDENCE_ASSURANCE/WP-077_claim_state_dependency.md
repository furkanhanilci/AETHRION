# WP-077 — Claim State, Dependency ve Assessment Motoru

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-077` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Platform Lead |
| Bağımsız doğrulayıcı | Methodologist / Assurance Lead |
| Hard dependencies | WP-005, WP-018, WP-075, WP-076 |
| İlgili gate | G5–G10 |
| İlgili kontroller | CTL-EPI-01, CTL-EPI-03 |
| İlgili ACC senaryoları | ACC-08, ACC-19, ACC-20 |

## Amaç ve beklenen sonuç

Empirical/methodological/interpretive claim'ler; evidence, validity, conflict, reproduction ve dependency blocker'larıyla PROVISIONAL/SUPPORTED/CONTESTED/CHALLENGED/REPLICATED gibi durumlara geçer.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-077-T01 | Claim type ve lifecycle transition kurallarını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-077-T02 | supports/contradicts/derived-from dependency graph validation yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-077-T03 | Assessment vektörünü provenance/method/directness/consistency/repro/scope/uncertainty boyutlarıyla kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-077-T04 | Non-compensable blocker precedence uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-077-T05 | Dependency status propagation ve impact queue ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-077-T06 | Human/assurance disposition API'sini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Claim state engine`
- `Dependency validator`
- `Assessment rubric`
- `Impact propagation worker`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Broken provenance BLOCKED
- Strong source weak method telafi etmez
- Contradictory evidence CONTESTED
- Repro pass state promotion
- Upstream supersession propagation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Yedi boyut tek confidence yüzdesine ortalanmaz
- [ ] Critical blocker yüksek kaynak kalitesiyle telafi olmaz
- [ ] State değişimi rule/evidence refs taşır
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

Yanlış assessment yeni version/disposition ile düzeltilir; publication impact scan otomatik açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
