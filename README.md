# AI Research Framework

Kanıt-merkezli, denetlenebilir bir araştırma işletim sistemi (AIRL-OS).
Temel tezi: **ajan üretir, makine doğrular, insan karar verir** — ve bu üçü
yapısal olarak birbirine karışmaz.

Bu depo, hedef mimariyi, yürütme disiplinini ve şu ana kadar gerçekten
çalışan bileşenleri bir arada tutar. **Plan, uygulama kanıtı değildir**:
aşağıdaki tablo ikisini ayırır.

| Alan | Durum | Konum |
|---|---|---|
| Literatür köprüsü (Bridge) V0 | ✅ **Çalışıyor**, yerel olarak kabul edildi | `src/airl_bridge/` |
| Zotero → Obsidian projeksiyonu | ✅ Çalışıyor, Zotero sınırında salt-okunur | `src/airl_bridge/obsidian.py` |
| Hermes MCP erişimi | ✅ Çalışıyor, beş salt-okunur araç | `src/airl_bridge/mcp_server.py` |
| Ortak contract çekirdeği | ⚠️ `TECH_COMPLETE` — üretim tüketicisi yok | `src/airl_framework/` |
| Skill Registry (38 skill) | 📐 Yazıldı, **test edilmedi** | `skills/` |
| Obsidian bilgi mimarisi | ✅ V0 hazır | `vault_baseline/` |
| Hedef mimari ve skill katmanı | 📐 Tasarlandı, karar bekliyor | `docs/architecture/` |
| Tam devreye alma programı | ⬜ Planlandı, başlatılmadı | `planning/commissioning/` |

## Yapı

```text
src/          Bridge ve ortak contract çekirdeği
tests/        Test paketi
skills/       38 yürütme skill'i — ajanların NASIL çalışacağı
planning/     WP-001–130, ACC-01–40 (hash mühürlü kanonik plan)
docs/         Mimari, review ve işletim dokümanları
schemas/      Ortak contract şemaları
delivery/     Paket başına kanıt paketleri
deploy/       systemd unit dosyaları
scripts/      Acceptance ve smoke betikleri
vault_baseline/  Obsidian vault'un versiyonlanmış kopyası
```

## Nereden başlanır

| Soru | Belge |
|---|---|
| Şu an gerçekten ne var, ne yok? | [`docs/review/FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md`](docs/review/FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md) |
| Hedef mimariye **ne** eklenmeli? | [`docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md`](docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md) |
| Ajanlar **nasıl** çalışmalı? | [`docs/architecture/AIRL_OS_SKILL_LAYER.md`](docs/architecture/AIRL_OS_SKILL_LAYER.md) · [`skills/README.md`](skills/README.md) |
| Çalışan dikey dilimin mimarisi | [`docs/ARCHITECTURE_V0.md`](docs/ARCHITECTURE_V0.md) |
| Günlük işletim | [`docs/OPERATIONS.md`](docs/OPERATIONS.md) |
| Tam program planı | [`planning/commissioning/README.md`](planning/commissioning/README.md) |

## Çalışan dikey dilim: Literature Bridge V0

```text
Zotero Local API (salt-okunur)
        → SQLite kanonik kaynak kayıt defteri
        → Obsidian "70 - Literature Sets/Zotero Sources" projeksiyonu
        → Hermes MCP (beş salt-okunur araç)
```

Servis yalnız `127.0.0.1` üzerinde dinler. Zotero API anahtarı almaz ve
kodda hiçbir Zotero yazma işlemi bulunmaz.

### Kurulum

```bash
cd /home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK
uv sync --extra dev
```

`.env` yerel olarak şunlara ayarlıdır: Zotero Local API `http://127.0.0.1:23119/api`,
kişisel kütüphane `users/0`, vault `/home/otonom/Documents/Obsidian Vault`,
üretilen notlar `70 - Literature Sets/Zotero Sources`, API `http://127.0.0.1:8765`.

### Zotero Local API'yi aç

1. Zotero'yu başlat
2. **Ayarlar → Gelişmiş → Genel**
3. **Bu bilgisayardaki diğer uygulamaların Zotero ile iletişim kurmasına izin ver** seçeneğini aç
4. Port `23119` yerel kalsın; yönlendirme veya dışa açma yapma

```bash
uv run airl-bridge doctor
```

### Çalıştırma

```bash
uv run airl-bridge serve

systemctl --user status airl-bridge.service
systemctl --user status airl-bridge-sync.timer
journalctl --user -u airl-bridge.service -n 50
```

Kullanıcı timer'ı aynı yerel senkronizasyonu 30 dakikada bir çalıştırır.

Yerel adresler: [`/health`](http://127.0.0.1:8765/health) ·
[`/ready`](http://127.0.0.1:8765/ready) · [`/docs`](http://127.0.0.1:8765/docs)

### İlk senkronizasyon

```bash
curl -X POST 'http://127.0.0.1:8765/v1/sync?limit=100'
curl 'http://127.0.0.1:8765/v1/sources?limit=10'

# veya sunucu olmadan
uv run airl-bridge sync --limit 100
```

Tekrarlanan senkron aynı Zotero kütüphane/öğe anahtarı için idempotenttir.
Zotero kaynaklı dosyalar otomatik yönetilen `Zotero Sources` dalında tutulur ve
kanonik kayıt defterinden yeniden üretilir. İnsan sentezi `20 - Source Notes`,
kürasyonlu setler `70 - Literature Sets` kökünde kalır.

> ⚠️ **Bilinen sınır:** Ingest 100 kayıtta sabit tavanlıdır; sayfalama ve
> `since=` artımlı senkron yoktur. Kütüphane 100 kaynağı geçtiğinde senkron
> sessizce eksik çalışır. Ayrıntı: denetim raporu bulgu **H1**.

### Test

```bash
uv run pytest
uv run python scripts/mcp_smoke.py
uv run python scripts/acceptance_v0.py
```

## Hermes MCP erişimi

Hermes, `airl-bridge-mcp` sunucusunu stdio üzerinden başlatır ve yalnız beş
salt-okunur araç görür: durum, kaynak arama, kaynak ayrıntısı, kategori
sayıları, olası kopya raporu. Senkronizasyon, yazma, silme veya Zotero
mutasyon aracı sunulmaz. Hermes yapılandırmasında açık bir beş araçlık
`tools.include` listesi vardır; MCP prompt ve resource yetenekleri kapalıdır.

## Durum semantiği

`ÇALIŞIYOR` bir bileşenin yerel olarak doğrulandığını söyler.
`ACCEPTED` üreticiden bağımsız bir doğrulayıcının kanıt paketini kabul
ettiğini söyler. Şu an **hiçbir iş paketi `ACCEPTED` değildir**.
