# WP-018 — Claim, Evidence, Review ve Decision Şemaları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-018` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Platform Lead |
| Bağımsız doğrulayıcı | Assurance Lead / Methodologist |
| Hard dependencies | WP-011, WP-012, WP-014, WP-016, WP-017 |
| İlgili gate | G5–G10 |
| İlgili kontroller | CTL-EPI-01, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-08, ACC-30 |

## Amaç ve beklenen sonuç

Claim sürümü, evidence span, bağımlılık, assessment, review verdict, disagreement ve human decision semantiği yayınlanabilir contract olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-018-T01 | ClaimRecord tip/status/validity koşullarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-018-T02 | EvidenceSpan hash+structural locator+fingerprint çıpasını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-018-T03 | ClaimDependency supports/contradicts/derived-from ilişkilerini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-018-T04 | ReviewRecord/Verdict/Finding/Disposition şemalarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-018-T05 | DisagreementCase/DecisionRecord/supersession alanlarını tamamla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Evidence contract bundle`
- `Claim state machine`
- `Review/disagreement schemas`
- `Decision schema fixtures`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Immutable claim version testi
- RELOCATED/AMBIGUOUS/NEEDS_REANCHOR durum testi
- Unresolved critical verdict gate fixture
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Evidence eski representation erişilebiliyorsa ORPHANED olmaz
- [ ] Claim düzeltmesi yeni version üretir
- [ ] Review ve decision frozen input snapshot taşır
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

Schema hatasında record quarantine edilir; canonical geçmiş overwrite edilmeden migration adapter uygulanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
