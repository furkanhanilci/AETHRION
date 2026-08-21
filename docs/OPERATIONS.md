# İşletim Rehberi

## Günlük durum kontrolü

```bash
curl -fsS http://127.0.0.1:8765/ready
systemctl --user is-active airl-bridge.service airl-bridge-sync.timer
systemctl --user list-timers airl-bridge-sync.timer --no-pager
```

## Elle senkron

```bash
curl -fsS -X POST 'http://127.0.0.1:8765/v1/sync?limit=100'
```

Bu işlem Zotero'ya yazmaz. SQLite kayıt defterini günceller ve yalnız
`70 - Literature Sets/Zotero Sources` dalını yeniden üretir.

## Hermes doğrulama

```bash
hermes mcp test airl_bridge
cd /home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK/airl_bridge_api
.venv/bin/python scripts/mcp_smoke.py
```

Hermes yapılandırmasındaki `tools.include` listesi beş araç içermelidir.
`prompts` ve `resources` kapalı kalmalıdır.

## Loglar

```bash
journalctl --user -u airl-bridge.service -n 100 --no-pager
journalctl --user -u airl-bridge-sync.service -n 100 --no-pager
```

Zotero kapalıyken zamanlanmış görev başarısız olabilir; sonraki zamanlayıcı
çalışması tekrar dener. Bridge veritabanı ve son başarılı Obsidian görünümü
korunur.

## Yerleşim geçişi yedeği

Eski `80_Generated` ağacı ve eski `AIRL Ana Sayfa.md`, aşağıdaki geri alınabilir
yerel yedekte tutulur:

```text
data/projection-backups/vault-layout-before-silbo-main-20260821/
```

Yedek doğrulanmadan veya açık insan onayı olmadan silinmemelidir.

## Güvenli yeniden kurulum sırası

1. `uv sync --extra dev`
2. `.env` içindeki vault yolunu doğrula.
3. `deploy/airl-bridge.service` birimini kullanıcı systemd alanına kopyala.
4. Bridge servisini etkinleştir ve `/ready` yanıtını doğrula.
5. Vault baseline dosyalarını kopyala.
6. Bir kez elle senkron çalıştır.
7. Hermes MCP sunucusunu ekle ve beş araçlık izin listesini uygula.
8. Senkron timer'ını etkinleştir.
9. `scripts/acceptance_v0.py` ve test paketini çalıştır.
