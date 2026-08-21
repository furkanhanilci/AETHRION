# WP-048 — Codex, OpenCode ve Direct Worker Adapter'ları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-048` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Agent Runtime Lead |
| Bağımsız doğrulayıcı | Security / Eval Office |
| Hard dependencies | WP-023, WP-027, WP-046, WP-047 |
| İlgili gate | G5,Engineering |
| İlgili kontroller | CTL-SEC-03, CTL-SEC-04 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Farklı agent runtime'ları aynı TaskContract, isolation, tool, result, audit ve cancellation contract'ını sağlayan değiştirilebilir adapter'lara dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-023 — Git, Worktree ve Protected Path Politikası](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-048-T01 | Adapter interface ve lifecycle yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-048-T02 | Codex non-interactive/task adapter uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-048-T03 | OpenCode headless/server adapter uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-048-T04 | Direct/local queue worker adapter uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-048-T05 | Worktree/sandbox/tool credentials bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-048-T06 | Structured result, trace, cancel ve failure normalization ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Runtime adapter SDK`
- `Codex adapter`
- `OpenCode adapter`
- `Direct worker adapter`
- `Conformance report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Aynı canonical task üç adapter'da schema uyumlu
- Cancel/timeout normalization
- Permission/path negative test
- Runtime session kaybı recovery
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Runtime session AIRL workflow state'i değildir
- [ ] Adapter raw provider secret almaz
- [ ] Sonuç canonical AgentResult/artifact contract'ına uyar
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

Adapter tekil olarak disable edilebilir; görev eligible başka adapter'a yeni execution lease ile dispatch edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
