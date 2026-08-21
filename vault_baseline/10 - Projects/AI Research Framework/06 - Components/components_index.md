# Components Index

Framework bileşenleri ve gerçek durumları. Bir bileşenin planlanmış olması
kurulduğu anlamına gelmez.

## Bileşen durumu

| Bileşen | Durum | Kayıt |
|---|---|---|
| **Bridge** (Zotero → SQLite → Obsidian → MCP) | ✅ **ÇALIŞIYOR** | [[10 - Projects/AI Research Framework/06 - Components/Bridge/bridge_component_status\|Bridge Component Status]] |
| Contract çekirdeği (`airl_framework`) | ⚠️ `TECH_COMPLETE` — üretim tüketicisi yok | — |
| Skill Registry | 📐 tasarlandı, test edilmedi | [[skills_index]] |
| Temporal / Gate Service | ⬜ kurulmadı | — |
| NATS / Outbox | ⬜ kurulmadı | — |
| Source Registry (PostgreSQL) | ⬜ kurulmadı (SQLite V0 var) | — |
| Claim / Evidence Ledger | ⬜ kurulmadı | — |
| Tool Broker / Execution Broker | ⬜ kurulmadı | — |
| **Notification Broker** | 📐 **önerildi** | Skill Layer, Bölüm 4-G |
| Model Gateway / Capability Registry | ⬜ kurulmadı | — |
| Metascience düzlemi | 📐 önerildi | İdeal Yapı, Bölüm C |

**Gösterim:** ✅ çalışıyor · ⚠️ kısmi · 📐 tasarlandı · ⬜ kurulmadı

## Sınır

Bridge, framework'ün **ilk dikey dilimidir**, kökü değil. Bridge'in çalışması
130 iş paketinin kurulduğu anlamına gelmez.
