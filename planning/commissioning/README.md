# AIRL-OS Devreye Alma Programı

- **Sürüm:** 1.0
- **Tarih:** 13 Ağustos 2026
- **Durum:** Uygulama ve commissioning planı
**Amaç:** AIRL-OS hedef mimarisini, bağımsız atanabilen ve nesnel kanıtla kapatılabilen küçük iş paketleri halinde devreye almak.

## 1. Bu teslim neyi çözer?

Bu klasör bir mimari tanıtım dokümanı değildir. Mimari kararların çalışan sisteme nasıl dönüştürüleceğini tarif eden yürütme sistemidir. Her `WP-xxx` dosyası tek bir teslim sorumluluğu taşır; bağımlılıkları, uygulanacak işler, kabul testleri, kanıt paketi ve geri dönüş davranışı aynı dosyada bulunur.

Program artımlı olarak **geliştirilir ve test edilir**, ancak eksik yeteneklerle üretime açılmaz. Development ve staging ortamlarında dikey dilimler sırayla kurulabilir. Production cutover yalnız hedef durumun tamamı, kırk kabul senaryosu, iki restore tatbikatı ve sıfır açık kritik bulgu ile yapılır.

## 2. Korunan hedef mimari

Plan aşağıdaki bağlayıcı kararları uygular:

- Temporal, G0–G10 araştırma yaşam döngüsünün tek süreç otoritesidir.
- LangGraph yalnız sınırlandırılmış agent görevi içindeki bilişsel state'i yönetir.
- NATS JetStream canonical commit sonrası entegrasyon olaylarını taşır; gate state'i tutmaz.
- Agent bütün dış etkileri Tool Broker veya Execution Broker üzerinden gerçekleştirir.
- Source Registry bibliyografik kimlik, dedup, durum ve trust bilgisinin canonical sahibidir.
- Zotero kişisel ve ekip çalışma yüzeyidir; kişisel kütüphane salt okunur seed kaynağı, grup kütüphaneleri kontrollü ortak çalışma görünümüdür.
- LiteratureSetManifest, Source Registry snapshot'ı olarak immutable object store'a yazılır; Zotero koleksiyonu yalnız insan-okunur aynadır.
- Obsidian insan sentezinin canonical çalışma yüzeyidir; generated alanlar insan alanlarını ezemez.
- Claim/Evidence Ledger claim, evidence span, bağımlılık, review, karar ve supersession zincirinin canonical sahibidir.
- Risk/assurance, execution, independence ve claim assessment ayrı profillerdir; tek kombinatorik skora dönüştürülmez.
- Producer, reviewer ve reproducer ayrılığı machine-checkable bir IndependenceProfile ile zorlanır.
- D0–D4 veri sınıfı tek başına sandbox seçmez; veri, kod güveni, tool etkisi ve ağ/credential kapsamı birlikte ExecutionProfile üretir.
- G10 yıllarca yaşayan tek workflow değildir; Temporal Schedule kısa ömürlü ImpactScan çalıştırır.
- Platform Assurance bütün katmanları yatay keser; policy, workflow, broker, restore ve golden-path testleriyle sistemin kendisini doğrular.

## 3. Klasör yapısı

| Yol | İçerik |
|---|---|
| `00_PROGRAM/` | Program charter'ı, hedef durum, dalga planı, RACI, DoR/DoD, kanıt ve değişiklik yönetimi |
| `01_GOVERNANCE/` | WP-001–010: yönetişim ve politika tasarımı |
| `02_CONTRACTS/` | WP-011–020: kimlik, schema, kayıt ve contract temeli |
| `03_FOUNDATION/` | WP-021–030: ortam, repository, CI, veri ve platform omurgası |
| `04_CONTROL_EVENT/` | WP-031–040: Temporal, G0–G10, event ve replay |
| `05_MODEL_AGENT_TOOL/` | WP-041–050: gateway, admission, agent runtime ve broker |
| `06_EXECUTION_SECURITY/` | WP-051–060: trust zone, compute, identity, policy ve güvenlik |
| `07_LITERATURE_KNOWLEDGE/` | WP-061–074: Source Registry, Zotero, literatür ve Obsidian |
| `08_EVIDENCE_ASSURANCE/` | WP-075–090: evidence, claim, deney, review ve reproduction |
| `09_EXPERIENCE_OBSERVABILITY/` | WP-091–101: cockpit, karar UI, telemetry ve FinOps |
| `10_INTEGRATION_CUTOVER/` | WP-102–121: dikey dilimler, commissioning ve production cutover |
| `11_DAY2_OPERATIONS/` | WP-122–130: sürekli işletim ve güvence |
| `12_ACCEPTANCE_SCENARIOS/` | ACC-01–ACC-40: Given/When/Then sistem kabul senaryoları |

## 4. Paket durum modeli

```text
BACKLOG → READY → IN_PROGRESS → TECH_COMPLETE → EVIDENCE_REVIEW
        → ACCEPTED → INTEGRATED → COMMISSIONED
                     ↘ REVISE / BLOCKED
```

- `READY`: Definition of Ready eksiksizdir; owner ve bağımlılıklar nettir.
- `TECH_COMPLETE`: Kod/konfigürasyon tamamdır fakat henüz kabul edilmiş sayılmaz.
- `EVIDENCE_REVIEW`: Paket testleri ve kanıt manifesti bağımsız doğrulamadadır.
- `ACCEPTED`: Paket seviyesindeki kabul ölçütleri geçmiştir.
- `INTEGRATED`: Bağımlı sistemlerle contract testleri geçmiştir.
- `COMMISSIONED`: İlgili uçtan uca kabul senaryoları da geçmiştir.

Bir agent'ın veya implementer'ın “tamamlandı” beyanı yalnız `TECH_COMPLETE` olabilir. `ACCEPTED` kararı pakette tanımlı bağımsız doğrulayıcıya aittir.

## 5. Efor kodu

| Kod | İlk tahmin | Kullanım |
|---|---:|---|
| XS | 0,5–2 kişi-gün | Tek schema, policy veya küçük yapılandırma |
| S | 2–5 kişi-gün | Tek servis içi sınırlı teslim |
| M | 5–10 kişi-gün | Bir servis veya entegrasyon dilimi |
| L | 10–20 kişi-gün | Birden çok sistem ve failure-path testi |

Hiçbir paket varsayılan olarak L'den büyük olmamalıdır. Refinement sonunda L üstü çıkan paket bölünür. Tahmin takvim taahhüdü değildir; `00_PROGRAM/08_KAPASITE_VE_TAHMIN.md` içindeki kapasite modeliyle tarihe çevrilir.

## 6. Çalışmaya başlama sırası

1. `00_PROGRAM/01_HEDEF_DURUM_VE_INVARIANTLAR.md` ile kapsamı okuyun.
2. `00_PROGRAM/02_DALGA_VE_BAGIMLILIK_HARITASI.md` üzerinden geçerli dalgayı seçin.
3. `00_PROGRAM/03_PAKET_KATALOGU.md` içinden bağımlılıkları kapanmış paketi alın.
4. Paket dosyasındaki DoR kontrolünü yapın ve named owner atayın.
5. Yalnız paket kapsamındaki değişikliği gerçekleştirin.
6. Testleri çalıştırın, evidence manifesti üretin ve bağımsız doğrulamaya gönderin.
7. Kabul edilen paketi entegrasyon ve kabul senaryolarına bağlayın.

## 7. Başlangıç komutu

Programın ilk icra noktası `WP-001 Commissioning Charter`dır. WP-001 kabul edilmeden teknoloji kurulumuna başlanmaz; aksi durumda ortam, güvenlik ve takım seçimleri kapsam otoritesi olmadan ilerler.
