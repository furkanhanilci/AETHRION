# Framework Audit Evidence — 2026-08-22

Bağımsız denetim sırasında **taze koşumla** toplanan kanıt. Her satır
tekrar üretilebilir bir komuta bağlıdır.

İlgili rapor:
[[10 - Projects/AI Research Framework/02 - Reviews/claude_framework_audit_report|Claude Framework Audit Report]]

## E1 — Mekanik doğrulama

| Komut | Exit | Sonuç |
|---|---:|---|
| `.venv/bin/python -m pytest -q` | 0 | **20 passed**, 1 uyarı (pydantic forward-ref) |
| `sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt` | 0 | **184/184 OK**, 0 FAILED |
| `diff -rq vault_baseline "$VAULT"` | — | içerik farkı yok (yalnız `.obsidian/` config) |

## E5 — Operasyon

| Kontrol | Sonuç |
|---|---|
| `systemctl --user is-active airl-bridge.service` | `active` |
| `systemctl --user is-active airl-bridge-sync.timer` | `active` |
| `GET /health` | `{"status":"ok","version":"0.1.0","zotero_write_enabled":false}` |
| `GET /ready` | `{"status":"ready","zotero":"reachable","source_count":33}` |
| SQLite | 33 kaynak · 25 sync run · son 8 run `SUCCEEDED` |
| Kaynak dağılımı | journalArticle 25 · report 6 · conferencePaper 2 |

## Git durumu

| Alan | Değer |
|---|---|
| HEAD | `6c849bd` |
| origin/main | `6c849bd` — 0 ahead / 0 behind |
| Çalışma ağacı | temiz (denetim anında) |
| Takipli dosya | 434 |
| Remote | `github.com/furkanhanilci/AI-Research-Framework` (private) |

## Plan bütünlük analizi (script ile)

| Ölçüm | Sonuç |
|---|---|
| WP dosyası ↔ CSV eşleşmesi | 130/130, eksik yok, fazla yok |
| Bağımlılık grafiği | **döngü yok**, ileri bağımlılık **0** |
| Plan içi markdown link | 1011 link, **0 kırık** (her üç kopyada) |
| WP şablon oranı (≥120/130 dosyada aynen tekrar) | **%59,2** |
| ACC şablon oranı (≥36/40) | **%48,8** |
| WP başına özgün satır | ~25 |
| WP ↔ ACC çapraz referans | CSV ile ACC dokümanları **39/40 vakada farklı** |
| ACC referansı olmayan WP | **62/130** |
| ACC alanı placeholder olan WP | **39/130** |
| Farklı `owner` rolü | **73** |
| Farklı `verifier` rolü | **114** |
| Efor dağılımı | L: 83 · M: 42 · S: 5 |

## Obsidian bütünlüğü

| Ölçüm | Denetim öncesi | Sonrası |
|---|---|---|
| Not sayısı | 246 | 246 + 38 skill + 8 indeks |
| Wikilink | 103, 0 kırık | yeniden doğrulandı |
| Şablon yolu config | ❌ `_Şablonlar` (bozuk) | ✅ `_Templates` |
| Günlük not klasörü | ❌ yok, kök kirliliği | ✅ `80 - Daily` |
| Dataview | ❌ kurulu değil → sorgular ölü | ✅ core-search sözdizimine çevrildi |
| Yinelenen not adı | `README` ×2, `readme` ×2 | ✅ 0 |

## Doğrulanamayan alanlar

| Alan | Neden |
|---|---|
| SILBO FIX-004/005a/005 kabul zinciri | Ayrı repository, kapsam dışı |
| Hermes `tools.include` beş-araç kısıtı | Config repo dışında |
| GitHub branch protection kuralları | Salt-okunur sınır |
| `acceptance_v0.py` çalıştırma | Canlı servise yazıyor + kişisel veriye bağımlı |
| Zotero gerçek toplam kayıt sayısı | Zotero doğrudan sorgulanmadı |
