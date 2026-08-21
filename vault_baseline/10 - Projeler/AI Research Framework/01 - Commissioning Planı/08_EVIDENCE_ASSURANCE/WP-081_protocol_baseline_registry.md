# WP-081 — Protocol, Analysis, Baseline ve Falsification Registry

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-081` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Method Office Lead |
| Bağımsız doğrulayıcı | Statistician / Falsification Lead |
| Hard dependencies | WP-008, WP-014, WP-019, WP-025, WP-026, WP-035, WP-075 |
| İlgili gate | G2,G4,G5 |
| İlgili kontroller | CTL-EPI-02, CTL-DAT-01 |
| İlgili ACC senaryoları | ACC-39 |

## Amaç ve beklenen sonuç

ProtocolManifest, AnalysisPlan, BaselineBundle ve FalsificationPlan freeze/amendment, owner, hash ve gate referansıyla canonical registry'de tutulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-019 — Run, Environment ve Reproduction Şemaları](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-081-T01 | Registry data model/API ve outbox events kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-081-T02 | Variables/outcomes/controls/sample/stop rule validation yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-081-T03 | Baseline/null/counter-test/leakage fields zorunlu kıl | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-081-T04 | Freeze/signature ve amendment/supersession lifecycle uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-081-T05 | Run/claim linkage ve post-hoc change detector ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-081-T06 | Review/approval workflow API bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Method Registry`
- `Protocol validators`
- `Amendment workflow`
- `Post-hoc change detector`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Missing stop rule fail
- Post-result baseline edit deny
- Protocol amendment preserves old run
- Leakage detector fixture
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Frozen protocol hash'siz G5 run açılmaz
- [ ] Post-hoc değişiklik görünür amendment'tır
- [ ] Negative result ve stop rule korunur
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

Yanlış protocol version INVALIDATED olur; bağlı run/claim impact alır ve eski artifact kalır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
