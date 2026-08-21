# WP-064 — Zotero Kütüphane, Koleksiyon ve Yetki Modeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-064` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Lead |
| Bağımsız doğrulayıcı | Security / Governance |
| Hard dependencies | WP-004, WP-012, WP-017, WP-049, WP-050, WP-061 |
| İlgili gate | G3,G10 |
| İlgili kontroller | CTL-LIT-03, CTL-SEC-03 |
| İlgili ACC senaryoları | ACC-01, ACC-02 |

## Amaç ve beklenen sonuç

Kişisel Zotero salt-okunur seed yüzeyi, AIRL grup kütüphaneleri trust/üyelik sınırına göre ortak çalışma yüzeyi ve agent-managed koleksiyonlar olarak kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/wp_050_tool_connectors.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-064-T01 | Kişisel library read-only credential ve erişim sınırını doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-064-T02 | Grup library açma kriteri: üyelik/gizlilik/lisans/retention/ownership tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-064-T03 | Project collection şablonunu oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-064-T04 | 00_Human_Seeds/10_Agent_Candidates/20_Screening/30_Included/40_Used/50_Excluded/80_Updates/90_Frozen_View kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-064-T05 | Agent vs human authority ve R3 intake/curated ayrımını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-064-T06 | Organization owner/admin continuity planı yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Zotero topology`
- `Collection template`
- `Credential/permission matrix`
- `Library lifecycle SOP`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Personal write negative test
- Wrong group/collection target deny
- R3 intake→curated promotion
- Owner continuity tabletop
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Proje başına grup varsayılan değildir; trust sınırı belirler
- [ ] Agent kişisel library'ye yazamaz
- [ ] Collection namespace tek başına güvenlik kontrolü sayılmaz
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

Yanlış grup/permission release revoke edilir; write connector kapatılıp SyncReceipt audit edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
