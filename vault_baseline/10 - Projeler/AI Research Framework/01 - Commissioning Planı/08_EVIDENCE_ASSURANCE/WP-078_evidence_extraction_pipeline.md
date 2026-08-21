# WP-078 — Yapılandırılmış Evidence Extraction Hattı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-078` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Lead |
| Bağımsız doğrulayıcı | Independent Evidence Auditor |
| Hard dependencies | WP-045, WP-047, WP-058, WP-063, WP-068, WP-075, WP-076 |
| İlgili gate | G3,G5,G6 |
| İlgili kontroller | CTL-SEC-01, CTL-EPI-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Karantinadan geçen kaynaklar read-only extractor ile study design, population, intervention, outcome, estimate, limitation ve counter-evidence adaylarına ayrılır; ikinci geçişle doğrulanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-068 — Zotero Annotation → EvidenceCandidate Hattı](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-078-T01 | Domain-neutral extraction schema ve profile extensions tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-078-T02 | Chunk/section/table-aware extraction graph yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-078-T03 | Her alanı EvidenceCandidate+locator+quote hash ile üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-078-T04 | Deterministic parser/validator ve missing-field checks ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-078-T05 | Independent second-pass sampling/risk review bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-078-T06 | Correction/version ve quality telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Extraction pipeline`
- `Extraction schemas`
- `Evidence candidate store`
- `Second-pass review queue`
- `Quality dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Known paper field extraction
- Table/figure locator
- Prompt injection cannot tool call
- Contradictory/limitation extraction
- Second-pass disagreement
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Extractor claim'i VERIFIED yapamaz
- [ ] Her material alan source span taşır
- [ ] Missing/uncertain alan uydurulmaz, UNKNOWN kalır
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

Hatalı extraction INVALIDATED/new version olur; source representation ve human note değişmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
