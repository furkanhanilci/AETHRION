# WP-070 — İnsan + Agent Çift Yönlü Literatür Keşfi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-070` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Lead |
| Bağımsız doğrulayıcı | Independent Literature Reviewer |
| Hard dependencies | WP-007, WP-045, WP-047, WP-062, WP-065, WP-066, WP-069 |
| İlgili gate | G3 |
| İlgili kontroller | CTL-EPI-02, CTL-GOV-02 |
| İlgili ACC senaryoları | ACC-01, ACC-02 |

## Amaç ve beklenen sonuç

İnsan seed'leri agent genişletmesiyle, agent adayları insan seçim/karşı-kanıt aramasıyla birleşir; coverage ve provenance iki yönlü görünür olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-065 — Kişisel Zotero Seed Ingest Hattı](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-066 — Agent Candidate ve Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md), [WP-069 — SearchProtocol ve LiteratureCampaign Orkestrasyonu](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-070-T01 | Human seed branch ve agent discovery branch'ini ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-070-T02 | Keyword/citation/snowball/semantic scout bundle'larını çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-070-T03 | Farklı model/strateji sonuçlarını resolver'da birleştir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-070-T04 | Counter-evidence ve minority-source branch ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-070-T05 | Candidate ranking'i karar değil triage olarak uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-070-T06 | Human inclusion feedback'i sonraki query iteration'a bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Dual-loop discovery workflow`
- `Discovery provenance`
- `Candidate/coverage matrix`
- `Counter-evidence log`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Human seed→agent snowball
- Agent candidate→human inclusion
- Minority/counter source retained
- One branch outage partial state
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Agent popülerlik sırası inclusion kararı değildir
- [ ] İki tarafın kaynakları aynı resolver/dedup'tan geçer
- [ ] Arama boşluğu ve anlaşmazlık görünür kalır
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

Hatalı scout profile/bundle devre dışı bırakılır; ürettiği adaylar INVALIDATED değil source provenance ile düşük trust/disposition alır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
