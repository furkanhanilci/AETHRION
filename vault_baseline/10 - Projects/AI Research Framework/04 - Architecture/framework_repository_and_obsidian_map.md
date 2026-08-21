# AI Research Framework — Repository and Obsidian Map

Bu not, framework’ün bütün parçalarının nerede tutulduğunu gösterir. `airl_bridge_api`
framework’ün tamamı değildir; Bridge, framework içindeki ilk çalışan dikey
altyapı bileşenidir.

## Canonical project roots

| Alan | Konum | Rol |
|---|---|---|
| Commissioning plan | `../AIRL_OS_DEVREYE_ALMA_PLANI/` | WP-001–WP-130 ve ACC-01–ACC-40 hedef sistemi |
| Application repository | `../../` | Kod, test, deployment, schemas, delivery ve vault baseline |
| Obsidian vault | `/home/otonom/Documents/Obsidian Vault/` | Kullanıcıya görünen proje bilgi alanı |
| Bridge component | `../../` | Zotero/SQLite/API/Obsidian projection ilk çalışan slice |
| SILBO model worktree | `/home/otonom/silbo-fix-005/` | Ayrı model/evaluation alanı; framework ile karıştırılmaz |

## Obsidian project tree

- `00_navigation_and_execution_cockpit.md` — yürütme durumu ve sonraki adım
- `01 - Commissioning/` — plan, WP ve ACC dokümantasyonunun İngilizce aynası
- `02 - Reviews/` — bağımsız review promptları ve review sonuçları
- `03 - Implementation/` — gerçek uygulama adımları ve karar kayıtları
- `04 - Architecture/` — repository, veri akışı ve mimari haritalar
- `05 - Evidence/` — test, acceptance, hash ve kanıt paketleri
- `06 - Components/Bridge/` — Bridge’in kendi durum ve sınır kayıtları
- `implementation_log.md` — geriye dönük ve ileriye dönük adım günlüğü
- `ai_research_framework_current_status_and_roadmap.md` — yaşayan durum özeti

## Sınır kuralı

Framework’e ait genel belgeler `airl_bridge_api/docs` altında kaybolmamalıdır.
Kod ve teknik teslimatlar repository’de kalır; kullanıcıya dönük proje durumu,
kararlar, review talimatları, kanıt ve yol haritası bu Obsidian proje ağacında
görünür tutulur.
