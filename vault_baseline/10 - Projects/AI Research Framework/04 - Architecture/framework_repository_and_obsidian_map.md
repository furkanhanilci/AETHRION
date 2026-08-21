# AI Research Framework — Repository and Obsidian Map

Framework'ün bütün parçalarının nerede tutulduğunu gösterir.
**Repo kökü ile framework kökü aynıdır**; Bridge, framework içindeki
bileşenlerden yalnızca biridir.

## Kanonik kökler

| Alan | Konum | Rol |
|---|---|---|
| Framework deposu | `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK/` | Git repo kökü — kod, plan, skill, doküman, kanıt |
| Remote | `github.com/furkanhanilci/AI-Research-Framework` | private, `main` |
| Obsidian vault | `/home/otonom/Documents/Obsidian Vault/` | Kullanıcıya görünen proje bilgi alanı |
| SILBO model worktree | `/home/otonom/silbo-fix-005/` | Ayrı model/evaluation alanı; framework ile karıştırılmaz |

## Repository yapısı

```text
AI_RESEARCH_FRAMEWORK/            ← git repo kökü
├── src/
│   ├── airl_bridge/              Bridge bileşeni (Zotero → SQLite → Obsidian → MCP)
│   └── airl_framework/           Ortak contract çekirdeği
├── tests/                        Test paketi
├── skills/                       38 yürütme skill'i (Skill Registry)
├── planning/
│   └── commissioning/            WP-001–130, ACC-01–40 — KANONİK, hash mühürlü
├── docs/
│   ├── architecture/             Hedef mimari ve skill katmanı tasarımı
│   ├── review/                   Bağımsız review talimat ve raporları
│   ├── ARCHITECTURE_V0.md        Çalışan dikey dilimin mimarisi
│   └── OPERATIONS.md             İşletim rehberi
├── schemas/                      Ortak contract şemaları
├── delivery/                     Paket başına kanıt paketleri
├── deploy/                       systemd unit dosyaları
├── scripts/                      Acceptance ve smoke betikleri
├── vault_baseline/               Obsidian vault'un versiyonlanmış kopyası
├── data/                         SQLite ve projeksiyon yedekleri (git dışı)
└── .venv/                        Sanal ortam (git dışı)
```

## Plan bütünlüğü

`planning/commissioning/00_PROGRAM/SHA256SUMS.txt` 184 dosyayı mühürler.
Doğrulama, repo kökünden:

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

> Plan **tek kanonik kopyada** tutulur. Obsidian'daki `01 - Commissioning/`
> okuma/navigasyon aynasıdır; içerik değişecekse **önce kanonik dosya** değişir.

## Obsidian proje ağacı

```text
10 - Projects/AI Research Framework/
├── 00_navigation_and_execution_cockpit.md   yürütme durumu ve sonraki adım
├── 01 - Commissioning/                      plan aynası (İngilizce adlandırma)
├── 02 - Reviews/                            bağımsız review talimat ve sonuçları
├── 03 - Implementation/                     uygulama adımları
├── 04 - Architecture/                       mimari ve haritalar
├── 05 - Evidence/                           test, hash, acceptance kanıtı
├── 06 - Components/                         bileşen durumları
├── 07 - Skills/                             38 skill, yedi grupta
├── implementation_log.md                    adım günlüğü
└── ai_research_framework_current_status_and_roadmap.md
```

## Vault kök yapısı

| Alan | İçerik | Kim yazar |
|---|---|---|
| `00 - Home` | Giriş sayfası | insan |
| `01 - Inbox` | Sınıflandırılmamış geçici not | insan |
| `10 - Projects` | Proje ağaçları | insan |
| `20 - Source Notes` | İnsan sentezi | **yalnız insan** |
| `30 - Concepts` · `40 - Claims` · `50 - Decisions` · `60 - Runs` | Bilgi alanları | insan |
| `70 - Literature Sets` kökü | Kürasyonlu setler | insan |
| `70 - Literature Sets/Zotero Sources` | **Otomatik projeksiyon** | **Bridge — elle düzenlenmez** |
| `80 - Daily` | Günlük çalışma notu | insan |
| `90 - Archive` | Kapanmış/superseded | insan |
| `_Templates` | Not şablonları | insan |

## Adlandırma kuralları

- **Klasör ve dosya adları İngilizce.** Ürün kodu ön eki veya Türkçe ad kullanılmaz.
- Obsidian notları `lowercase_snake_case.md`.
- Her klasör indeksi `<alan>_index.md` (`reviews_index`, `skills_index`…).
  Sebep: `README` gibi yinelenen adlar Obsidian kısa-yol linklerinde belirsizlik yaratır.
- Skill dosyaları `lowercase-hyphen` (skill adıyla birebir).
- Ayna üreticisi bu kuralları yeniden üretmelidir.

> **Bilinen istisna:** `planning/commissioning/` altındaki WP ve ACC dosya adları
> hâlâ karışık Türkçe/İngilizce (`WP-002_kapsam_nfr_izlenebilirlik.md`).
> Obsidian aynası bunları İngilizceye çevirir. Kanonik tarafın da çevrilmesi
> ayrı bir adımdır ve hash mührünün yenilenmesini gerektirir.

## Sınır kuralı

Kod ve teknik teslimatlar repository'de kalır; kullanıcıya dönük proje durumu,
kararlar, review talimatları, kanıt ve yol haritası Obsidian proje ağacında
görünür tutulur. İkisi arasındaki kopya ilişkisi hash ile doğrulanır.
