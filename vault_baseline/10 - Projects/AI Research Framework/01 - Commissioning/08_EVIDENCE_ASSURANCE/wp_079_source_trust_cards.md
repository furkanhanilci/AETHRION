# WP-079 — SourceTrustCard ve Çalışma Kalitesi Değerlendirmesi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-079` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Methodologist |
| Bağımsız doğrulayıcı | Independent Domain/Statistician Reviewer |
| Hard dependencies | WP-005, WP-017, WP-063, WP-075, WP-076, WP-078 |
| İlgili gate | G3,G6,G10 |
| İlgili kontroller | CTL-EPI-02, CTL-LIT-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Kaynağın status, çalışma tasarımı, sample, measurement, bias, analysis, external validity ve reporting sınırları tek puan yerine gerekçeli trust kartında tutulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md), [WP-078 — Yapılandırılmış Evidence Extraction Hattı](../08_EVIDENCE_ASSURANCE/wp_078_evidence_extraction_pipeline.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-079-T01 | Kaynak türüne göre rubric/profile tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-079-T02 | Status/license/provenance otomatik alanlarını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-079-T03 | Method/bias/precision/applicability boyutlarını ayrı değerlendir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-079-T04 | Human/agent assessment ve disagreement semantiği yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-079-T05 | Expiry/new version/retraction impact kuralı ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-079-T06 | Calibration sample ve reviewer guide hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `SourceTrustCard engine`
- `Rubric profiles`
- `Calibration set`
- `Trust review UI contract`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- High prestige weak method not high trust
- Retraction override
- Reviewer calibration
- Missing data UNKNOWN not zero
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Trust tek authority score değildir
- [ ] Kart rule/evidence/rationale taşır
- [ ] Kaynak kalitesi claim entailment veya reproduction yerine geçmez
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

Rubric değişikliği eski kartı mutate etmez; re-assessment queue ve version üretir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
