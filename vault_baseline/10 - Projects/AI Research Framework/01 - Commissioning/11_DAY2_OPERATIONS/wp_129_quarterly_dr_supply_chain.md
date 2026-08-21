# WP-129 — Quarterly DR, Supply-Chain ve Audit Tatbikatı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-129` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead / Supply Chain Security |
| Bağımsız doğrulayıcı | Independent Audit Witness |
| Hard dependencies | WP-027, WP-059, WP-099, WP-114, WP-121 |
| İlgili gate | Day-2 |
| İlgili kontroller | CTL-OPS-02, CTL-OPS-03, CTL-SEC-05 |
| İlgili ACC senaryoları | ACC-17, ACC-27, ACC-40 |

## Amaç ve beklenen sonuç

Üç aylık restore, workflow replay, signature/revoke, audit export ve dependency/patch tatbikatları üretim baseline'ının sürdürülebilirliğini kanıtlar.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-059 — Supply-Chain Admission, Sigstore ve SLSA Policy](../06_EXECUTION_SECURITY/wp_059_supply_chain_admission.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-114 — Operations, DR ve Restore Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-129-T01 | Rotating component/regional restore drill seç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-129-T02 | Open workflow replay/worker version test et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-129-T03 | Image/tool/policy signature/revoke exercise yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-129-T04 | Full project audit export/hash verify çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-129-T05 | Patch/CVE/backup/retention/owner gaps review et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-129-T06 | Drill findings ve next-quarter plan kapat | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Quarterly drill dossier`
- `Restore/replay evidence`
- `Supply-chain/audit results`
- `Improvement backlog`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- PITR/object/Temporal/NATS restore rotation
- Revoked artifact deny
- Audit chain verify
- Owner/runbook execution
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] RPO/RTO ve integrity hedefleri karşılanır
- [ ] Açık critical drill finding cutover değil production risk escalation üretir
- [ ] Evidence bağımsız witness taşır
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

Tatbikat unexpected riskte durdurulur; production blast radius guard ve incident process uygulanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
