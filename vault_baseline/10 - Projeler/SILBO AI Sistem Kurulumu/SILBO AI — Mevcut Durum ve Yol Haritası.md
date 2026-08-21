---
airl_id: SILBO-PROJECT-SYSTEM-ROLLOUT
type: project
status: active
owner: otonom
created_at: "2026-08-21"
updated_at: "2026-08-21T16:34:38+03:00"
current_phase: fix-005a-preimplementation-challenge
canonical_status_scope: operational-tracker
tags:
  - silbo/project
  - silbo/architecture
  - silbo/status
  - silbo/roadmap
---

# SILBO AI — Mevcut Durum ve Yol Haritası

> [!important] Yaşayan proje kaydı
> Bu belge her maddi uygulama, test, review, kabul, rollback veya kapsam değişikliğinden sonra güncellenir. Bir iş yalnız niyet veya agent beyanıyla tamamlanmış sayılmaz; komut çıktısı, artifact ve gerekiyorsa bağımsız review ile desteklenir.

## 1. Yönetici özeti

SILBO çalışması iki ayrı fakat ilişkili düzlemde ilerlemektedir:

1. **Mevcut SILBO ürün reposu:** Eğitim, değerlendirme, verifier güvenilirliği ve yayın kalitesinde kanıt üretimi için daha önce geliştirilmiş gerçek kod tabanı. Bu repo şu anda `SILBO-FIX-004` bağımsız review aşamasındadır.
2. **AIRL-OS devreye alma programı:** 130 iş paketi ve 40 uçtan uca kabul senaryosuyla tam araştırma işletim sistemini tarif eden commissioning planı. Bu planın tamamı henüz kurulmamıştır.

Bunlara ek olarak, kullanılabilir bir ilk dikey dilim olarak **yerel literatür V0 sistemi** kurulmuştur:

```text
Zotero Local API (salt-okunur)
        -> AIRL Bridge API
        -> SQLite kanonik V0 kayıt defteri
        -> Obsidian Literatür Setleri görünümü
        -> Hermes salt-okunur MCP araçları
```

### Güncel durum özeti

| Alan | Durum | Kanıt / sınır |
|---|---|---|
| Yerel literatür V0 | ÇALIŞIYOR | 33 kaynak, 3 sınıf, Obsidian projeksiyonu |
| Bridge API | AKTİF | `127.0.0.1:8765`, Zotero write kapalı |
| Otomatik senkron | AKTİF | systemd user timer, 30 dakika |
| Hermes MCP | AKTİF | 5 salt-okunur araç |
| Obsidian bilgi mimarisi | V0 HAZIR | İnsan ve otomatik alanlar ayrıldı |
| SILBO-FIX-004 uygulaması | IMPLEMENTED | Immutable `T=85625d7...`, `H=ddad3ab...` |
| SILBO-FIX-004 bağımsız review | APPROVED | Sealed Fable review `efb87f2`; exact T/H doğrulandı |
| SILBO-FIX-004 idari quorum | PASS / ACCEPTED | Review `933f17f` ile governed soyda; exact quorum PASS |
| SILBO-FIX-004 state uzlaştırması | PASS | Ledger/queue/state commit `b96b989`; preflight PASS |
| SILBO-FIX-005a | IN_PROGRESS / LOCAL | Aktivasyon `d86f5be`; production öncesi A1–A4 challenge |
| Genel framework GitHub yayını | AKTİF / PRIVATE | `furkanhanilci/AI-Research-Framework`, `main=038f0ce` |
| SILBO model reposu | AYRI / DOKUNULMADI | Genel framework remote'u olarak kullanılmıyor |
| Tam AIRL-OS commissioning | BAŞLAMADI / PLAN | WP seviyesinde bağımsız kabul yok |
| Production cutover | YETKİLİ DEĞİL | 40 ACC, restore tatbikatları ve kritik bulgu kapanışları gerekli |

## 2. Bu belgede kullanılan durumlar

| Durum | Anlamı |
|---|---|
| `PLAN` | Tasarım veya iş paketi dokümante edilmiş, uygulama kanıtı yok |
| `IN_PROGRESS` | Yetkili ve sınırlandırılmış çalışma aktif |
| `TECH_COMPLETE` | Kod/konfigürasyon hazır; bağımsız kabul tamamlanmamış |
| `PARTIAL` | Hedefin yalnız açıkça belirtilen alt kümesi çalışıyor |
| `ACCEPTED` | Paket ölçütleri bağımsız kanıtla kabul edilmiş |
| `COMMISSIONED` | İlgili uçtan uca kabul senaryoları da geçmiş |
| `BLOCKED` | Devam için dış karar, yetki veya kapanmamış zorunlu önkoşul var |

Bu dokümandaki `V0 HAZIR` veya `ÇALIŞIYOR` ifadeleri, 130 paketlik programın `ACCEPTED` ya da `COMMISSIONED` olduğu anlamına gelmez.

## 3. Kaynak otoriteleri ve çalışma dizinleri

### 3.1 Tam devreye alma planı

```text
/home/otonom/Desktop/FH/AIRL_OS_DEVREYE_ALMA_PLANI_v1.0/
  AIRL_OS_DEVREYE_ALMA_PLANI/
```

Bu alan hedef mimariyi, WP-001–WP-130 paketlerini ve ACC-01–ACC-40 kabul senaryolarını tanımlar.

### 3.2 Yerel literatür V0 uygulaması

```text
/home/otonom/Desktop/FH/AIRL_OS_DEVREYE_ALMA_PLANI_v1.0/
  airl_bridge_api/
```

Yerel Git başlangıç commit'i:

```text
15d57af Establish SILBO local literature bridge V0
```

### 3.3 Mevcut SILBO ürün reposu

Kabul edilmiş FIX-004 worktree'si:

```text
/home/otonom/silbo-fix-004
branch: codex/fix-004
current local HEAD: b96b989
implementation target/T: 85625d7a30fd9d77c9179ccff94d08b27ac0b1fd
handoff/H: ddad3abb49e53043e668a597432b9848ad43fb6a
review import: 933f17f3fe7b6b25b60e4ec293db0e6ad4b9acf5
closeout: 5737757
state reconciliation: b96b989
```

Aktif, actor-owned FIX-005a worktree'si:

```text
/home/otonom/silbo-fix-005a
branch: codex/fix-005a
governed base: b96b9894378000451966ab2fba3132d29ac80b64
activation commit: d86f5be
```

Shared `/home/otonom/silbo-ai` çalışma alanında toplu stage, cleanup veya uygulama yapılmaz.
SILBO model kodu ve remote'ları genel AI framework yayınından ayrı tutulur.

### 3.4 Genel AI framework GitHub reposu

```text
account: furkanhanilci
repository: AI-Research-Framework
visibility: private
default branch: main
remote: https://github.com/furkanhanilci/AI-Research-Framework.git
first published commit: 5efd305d52aca1557576e3208668ee9e474344da
current published framework commit: 038f0ce278af716b59ec78f6fc0b271b0f263e8b
```

İlk push öncesinde izlenen dosyalar kontrol edildi: `.env`, sanal ortam,
SQLite/WAL verileri, pytest cache ve projeksiyon yedekleri ignore kapsamında.
İzlenen dosyalarda yaygın credential/token imzası bulunmadı; 16/16 test geçti.

## 4. Kurulan yerel literatür V0

### 4.1 Zotero bağlantısı

- Zotero Local API yerel makinede etkinleştirildi.
- Bağlantı `http://127.0.0.1:23119/api` üzerinden çalışıyor.
- Kişisel kütüphane yalnız okunuyor.
- Bridge içinde Zotero API anahtarı, create, update, merge veya delete işlemi bulunmuyor.
- Kayıtların Zotero içindeki insan alanları değiştirilmedi.

### 4.2 Bridge API

- FastAPI servisi yalnız loopback üzerinde çalışıyor.
- SQLite WAL tabanlı V0 kayıt defteri kuruldu.
- Kaynaklar kararlı AIRL kimliği ve Zotero item key ile eşleniyor.
- Tekrar senkron aynı kaynağı çoğaltmıyor.
- Sağlık, readiness, listeleme, arama, kategori ve olası kopya endpoint'leri var.
- OpenAPI arayüzü yerel olarak erişilebilir.

### 4.3 Obsidian yerleşimi

Ana çalışma yüzeyi:

- [[00 - Ana Sayfa/SILBO AI Main Page|SILBO AI Main Page]]

İnsan tarafından yönetilen alanlar:

```text
01 - Gelen Kutusu
10 - Projeler
20 - Kaynak Notları
30 - Kavramlar
40 - İddialar
50 - Kararlar
60 - Çalıştırmalar
70 - Literatür Setleri kökü
90 - Arşiv
_Şablonlar
```

Otomatik Zotero görünümü:

```text
70 - Literatür Setleri/
  Zotero Kaynakları/
    00 - Kontrol Panosu/
    01 - Dergi Makaleleri/            25 kaynak
    02 - Konferans Bildirileri/         2 kaynak
    03 - Raporlar ve Ön Baskılar/       6 kaynak
```

Dosya adları makale başlığından üretilir. Aynı başlığa sahip farklı Zotero öğelerinde çakışmayı önlemek için `— Zotero ITEMKEY` eki kullanılır.

Kontrol görünümleri:

- [[70 - Literatür Setleri/Zotero Kaynakları/00 - Kontrol Panosu/Kaynak Kataloğu|Kaynak Kataloğu]]
- [[70 - Literatür Setleri/Zotero Kaynakları/00 - Kontrol Panosu/Olası Kopyalar|Olası Kopyalar]]

### 4.4 Hermes MCP

Hermes yalnız aşağıdaki araçları görür:

1. `bridge_status`
2. `search_sources`
3. `get_source`
4. `list_categories`
5. `list_possible_duplicates`

Hermes tarafında açık `tools.include` listesi bulunur; MCP prompt ve resource yetenekleri kapalıdır. Senkron, yazma, silme veya Zotero mutation aracı sunulmaz.

### 4.5 Otomasyon ve işletim

- `airl-bridge.service` aktif.
- `airl-bridge-sync.timer` aktif ve bekleme durumunda.
- Timer 30 dakikada bir yerel `/v1/sync` çağrısı yapar.
- Zotero kapalıysa çalışma hata kaydı üretir; sonraki timer yeniden dener.
- Son başarılı Obsidian görünümü ve SQLite kayıtları korunur.

### 4.6 Test ve kabul kanıtı

Son doğrulanan sonuçlar:

```text
Python testleri: 16/16 PASS
V0 acceptance: accepted
Kaynak sayısı: 33
Kategori sayısı: 3
Zotero write enabled: false
```

Bir bağımlılık forward-reference uyarısı görülmüştür; test hatası değildir ve uygulama kabulünü etkilememiştir. Yine de bağımlılık güncellemesinde yeniden kontrol edilmelidir.

## 5. Yerel V0 sırasında tamamlanan adımlar

### Adım 1 — Mevcut kurulum keşfi

- Hermes, Zotero, Obsidian ve dosya yolları incelendi.
- Hermes sürümü, model ayarı, MCP durumu ve gateway durumu kaydedildi.
- Zotero Local API erişim gereksinimi belirlendi.

### Adım 2 — Zotero Local API aktivasyonu

- Zotero ayarı yedeklenerek Local API etkinleştirildi.
- Zotero güvenli biçimde yeniden başlatıldı.
- Kişisel kütüphane endpoint'i doğrulandı.

### Adım 3 — Bridge API kurulumu

- Servis projesi, veritabanı, normalize edici, projeksiyon ve CLI yazıldı.
- Yerel systemd servisi kuruldu.
- İlk 33 kaynak içeri alındı.

### Adım 4 — Kaynak adlandırma ve sınıflandırma

- ID tabanlı Obsidian dosyaları makale başlığı tabanlı adlara geçirildi.
- Dergi makalesi, konferans bildirisi ve rapor/ön baskı sınıfları oluşturuldu.
- Aynı başlıklı kayıtlar için çakışmasız adlandırma eklendi.
- Olası kopyalar otomatik birleştirilmeden raporlandı.

### Adım 5 — Obsidian bilgi mimarisi

- İnsan sentezi ve otomatik projeksiyon sınırları tanımlandı.
- Proje, kaynak notu, kavram, iddia, karar, çalıştırma, literatür seti ve günlük not şablonları oluşturuldu.
- Ana sayfa `SILBO AI Main Page` olarak genelleştirildi.
- Zotero kaynakları kullanıcının kararıyla `70 - Literatür Setleri/Zotero Kaynakları` altına taşındı.

### Adım 6 — Hermes MCP bağlantısı

- Salt-okunur MCP adapteri oluşturuldu.
- Hermes beş aracı keşfetti.
- Gerçek durum ve LiDAR kaynak araması MCP üzerinden başarıyla çağrıldı.

### Adım 7 — Periyodik senkron

- 30 dakikalık systemd timer kuruldu.
- İlk oneshot çalışma `Result=success` ve exit code `0` ile tamamlandı.

### Adım 8 — Sürümleme ve işletim belgeleri

- V0 mimari belgesi ve işletim rehberi yazıldı.
- Uçtan uca kabul betiği eklendi.
- Proje için yerel Git deposu ve başlangıç commit'i oluşturuldu.
- Eski `80_Generated` ağacı ve `AIRL Ana Sayfa.md` silinmeden geri alınabilir yedeğe taşındı.

### Adım 9 — Tam SILBO durumuna geçiş kontrolü

- `/home/otonom/START_HERE_SILBO_CODEX.md` dosyasının 862 satırı eksiksiz okundu.
- Aktif `silbo-fix-004` worktree'si, target/handoff ve Git geçmişi doğrulandı.
- `verify_protocol_consistency.py`: PASS.
- Codex implementer attestation: PASS.
- FIX-004 için geçerli review dosyası bulunmadığı doğrulandı.

### Adım 10 — FIX-004 bağımsız review ve doğrulama

- Claude Code/Fable reviewer kurulu ve erişilebilir bulundu.
- Exact target worktree'sinin temiz ve detached olduğu doğrulandı.
- `fable/review-silbo-fix-004-r1` dalı oluşturuldu.
- Ayrı report ve mutation worktree'leri oluşturuldu.
- Fable review commit'i `efb87f2bab065fc658a0053cedb6357d995d34e1` olarak tamamlandı.
- Commit'in parent'ı exact handoff `H=ddad3abb...`; değiştirdiği tek dosya review kaydıdır.
- Author ve committer kimliği `SILBO Fable <silbo-fable@users.noreply.local>` olarak doğrulandı.
- Machine header exact `T/H/manifest`, `INDEPENDENCE: SEALED` ve `VERDICT: APPROVED` içeriyor.
- Reviewer 29/29 artifact hash, 144/144 evaluation, 52/52 runtime, 10/10 iki yönlü verifier kontrolleri, 15/15 mutation ve 104/104 rescore sonucunu bağımsız yeniden üretti.

### Adım 11 — Yaşayan durum kaydı Obsidian'a eklendi

- Bu kapsamlı durum/yol haritası kaydı `10 - Projeler/SILBO AI Sistem Kurulumu` altında oluşturuldu.
- `10 - Projeler/Projeler.md` içine kalıcı wiki bağlantısı eklendi.
- Git baseline ve gerçek Obsidian kopyalarının SHA-256 değeri aynı bulundu: `571edd4cbc4167a14202ea234ab9e536a50b1b4adf0dcac9dc36113da26896fd`.
- Belge, her maddi adım sonrasında yeni kanıt ve exact sonraki eylemle güncellenecek.

### Adım 12 — FIX-004 review entegrasyonu ve quorum

- Fable review-only commit'i governed `codex/fix-004` soyuna cherry-pick edildi: `933f17f3fe7b6b25b60e4ec293db0e6ad4b9acf5`.
- Cherry-pick edilen review dosyası ile özgün reviewer dosyasının SHA-256 değeri aynı doğrulandı: `c43b4b2ab50d1aad19a4bd73482ae46df756c53559759a457f8dcb0e6958cba6`.
- Yeni commit'in parent'ı exact handoff `ddad3abb49e53043e668a597432b9848ad43fb6a`; tek değişiklik Fable review kaydıdır.
- Exact quorum komutu `implementer=codex`, exact `T/H`, handoff manifesti ve Fable review kaydıyla çalıştırıldı.
- Quorum çıktısı: `status: PASS`, `errors: []`, reviewer kümesi: `["fable"]`.
- FIX-004 exact target/handoff üçlüsü bu kanıtla `ACCEPTED` durumundadır; yeni target veya handoff bu onayı geçersiz kılar.

### Adım 13 — FIX-004 state/queue uzlaştırması

- Final closeout ve ham quorum kaydı yerel commit `5737757` içinde tutuldu.
- `FABLE_ERROR_LEDGER.md` üzerinde E-F16 ve E-F20 exact target/quorum kanıtıyla `CLOSED` olarak işlendi.
- `FIX_QUEUE.md`, `PROJECT_STATE.md`, `state.json` ve reinterpretation kayıtları güncellendi.
- Wrapper invocation false-negative riski engelleyici olmayan `AIR-013 CANDIDATE` olarak kaydedildi; FIX-004 yeniden açılmadı.
- Protokol tutarlılığı ve Codex coordinator attestation `PASS` verdi.
- Tam preflight `PASS`; tek waiver daha önce tanımlı `G6 → SILBO-FIX-006`.
- Uzlaştırma yerel commit'i: `b96b989`.
- Kuyruk bağımlılığına göre sıradaki tek bounded iş `SILBO-FIX-005a`; `SILBO-FIX-005` bunun kabulünden önce başlatılamaz.
- Kullanıcının GitHub hedefi bekleniyor; tüm commit'ler yerel, remote write yapılmadı.

### Adım 14 — Genel framework GitHub kurulumu

- GitHub web/device akışıyla `furkanhanilci` hesabı doğrulandı.
- Yanlış kapsamı çağrıştıran boş `SILBO-AI` repo adı, veri yüklenmeden önce `AI-Research-Framework` olarak değiştirildi.
- Repo private oluşturuldu; kullanıcı hesabının yetkisi `ADMIN` olarak doğrulandı.
- Repo açıklamasından SILBO ifadesi kaldırıldı ve genel araştırma framework kapsamı yazıldı.
- `airl_bridge_api` deposu yalnız yeni framework repo'suna `origin` olarak bağlandı.
- Temiz `main` dalı `5efd305` commit'iyle ilk kez push edildi ve uzak commit değeri API üzerinden doğrulandı.
- Mevcut SILBO ürün reposunun `Mgh0x/Silbo-AI` remote'u değiştirilmedi ve oraya push yapılmadı.
- Tam commissioning planının 184 Markdown, 1 CSV ve 1 TXT dosyası `planning/commissioning/` altında genel framework repo'suna alınmak üzere hazırlandı.
- Commissioning planı, genel README ve güncel living-status kaydı commit `038f0ce278af716b59ec78f6fc0b271b0f263e8b` ile `main` dalına yayınlandı.
- GitHub API üzerinden remote `main` değerinin exact `038f0ce...` olduğu doğrulandı.

### Adım 15 — SILBO-FIX-005a yerel aktivasyonu

- Kabul edilmiş FIX-004 state commit'i `b96b989` temiz başlangıç olarak doğrulandı.
- `/home/otonom/silbo-fix-005a` actor-owned worktree'si ve `codex/fix-005a` dalı oluşturuldu.
- Production editinden önce scope, risk, rollback, CPU-only resource boundary, human-only remote sınırı ve immutable `T/H` teslim modeli task kaydına eklendi.
- Aktif state ve queue yalnız bu tek implementation döngüsünü gösterecek şekilde güncellendi.
- Implementer attestation, protocol consistency ve preflight `PASS`; yalnız mevcut `G6 → SILBO-FIX-006` waiver'ı var.
- Aktivasyon yerel commit'i: `d86f5be`.
- SILBO worktree'sinden herhangi bir remote'a push yapılmadı.

## 6. SILBO ürün reposunun güncel yönetilen durumu

### Kabul edilmiş geçmiş

| İş | Durum |
|---|---|
| SILBO-SYS-003 | Exact Fable quorum ile kabul edildi |
| SILBO-FIX-002 | Kabul edildi |
| SILBO-FIX-003 | Exact target/handoff, sealed Fable review ve quorum ile kabul edildi |

### Kabul edilen döngü: SILBO-FIX-004

```text
BASE = 410ef3f83b230ef14564b3a1e5375031af906113
T    = 85625d7a30fd9d77c9179ccff94d08b27ac0b1fd
H    = ddad3abb49e53043e668a597432b9848ad43fb6a
```

Uygulama ve bağımsız review kanıtına göre:

- Evaluation: 144/144 PASS
- Runtime: 52/52 PASS
- Do-nothing: 10/10 reddedildi
- Reference: 10/10 kabul edildi
- Mutation: 15/15 yakalandı
- Archived rescore: 104/104 uyumlu
- E-F16/E-F20: executable-CLOSED

Fable bu sonuçları bağımsız olarak yeniden üretmiş ve exact `T/H/manifest` üçlüsü için sealed `APPROVED` vermiştir. Review-only commit governed lineage'a baytları değiştirilmeden alınmış ve exact quorum doğrulaması `PASS` vermiştir. Dolayısıyla FIX-004 bu immutable üçlü için kabul edilmiştir.

Review sırasında bir adet engelleyici olmayan `MINOR` bulgu kaydedildi: `executes()` predicate'i `sh -c ...` gibi wrapper invocation biçimlerini tanımıyor. Arşivde bu biçimi kullanan kayıt bulunmadığı ve standart yol `run_python` olduğu için FIX-004 kabulünü engellemedi; ADR-008 reopen koşuluyla uyumlu bir `CANDIDATE` olarak ele alınacaktır.

### Sıradaki döngü: SILBO-FIX-005a

FIX-005a; repair path, sonuç sınıflandırması ve runtime'ın iç doğrulama çıktısının model bağlamına sızmasını önleyen context-isolation sınırını mutation-proven testlerle koruyacaktır. Bu paket CPU-local instrument çalışmasıdır; repair deneyini, model inference'ını veya GPU training'i içermez.

### Bilinen açık guard

`G6`, SILBO-FIX-006 kapsamındaki 9/21 çözümlenmemiş provenance fact nedeniyle kırmızıdır. Son preflight bunu açık waiver olarak gösterdi ve başka unwaived guard failure bulunmadı.

### Yayın sistemi

İzole publication subsystem uygulanmış ve mutation testleri yapılmıştır; fakat henüz bağımsız Fable review ve ana hatta entegrasyon yoktur. Altı aday makaleden hiçbiri READY değildir.

## 7. Tam AIRL-OS programı karşılaştırma matrisi

| Program alanı | Mevcut gerçek durum | Kalan ana kapsam |
|---|---|---|
| `00_PROGRAM` | Plan dosyaları mevcut | Charter kabulü, owner, bütçe, gate ve kanıt registry işletimi |
| `01_GOVERNANCE` | SILBO repo içinde bazı rol/review kontrolleri var | WP-001–010 formal acceptance |
| `02_CONTRACTS` | V0 modelleri ve bazı repo contractları var | WP-011–020 schema registry ve authority contracts |
| `03_FOUNDATION` | Yerel Git/SQLite/systemd prototipi var | PostgreSQL HA, object store, NATS, OCI/CI, derived models |
| `04_CONTROL_EVENT` | Kurulu değil | Temporal, G0–G10, GateRecord, replay/DLQ |
| `05_MODEL_AGENT_TOOL` | Hermes MCP V0 var | LiteLLM, capability/model admission, LangGraph, Tool Broker |
| `06_EXECUTION_SECURITY` | SILBO'da bubblewrap kanıtı var | K8s, Kueue, gVisor, SPIFFE/Vault, OPA, egress/DLP |
| `07_LITERATURE_KNOWLEDGE` | Çalışan yerel V0 var | PostgreSQL registry, resolver, annotations, manifest freeze, write-back |
| `08_EVIDENCE_ASSURANCE` | SILBO kanıt protokolü kısmen güçlü | Claim Ledger, MLflow, clean-room repro, review/publish paketleri |
| `09_EXPERIENCE_OBSERVABILITY` | Obsidian ve yerel panolar var | Cockpit, telemetry, Langfuse, Grafana, cost ledger, SLO |
| `10_INTEGRATION_CUTOVER` | Yerel V0 acceptance var | WP-102–121 ve ACC-01–ACC-40 commissioning |
| `11_DAY2_OPERATIONS` | Timer/runbook V0 var | DR, incident, requalification, continuous assurance |

## 8. İleriye dönük yürütme planı

### Faz A — Mevcut SILBO closure kuyruğunu güvenli biçimde kapat

1. ~~FIX-004 Fable reviewünü tamamla.~~ `PASS`
2. ~~Review commit'ini exact identity ve machine header ile doğrula.~~ `PASS`
3. ~~Review bytesını değiştirmeden governed lineage'a al.~~ `PASS`
4. ~~Exact `T/H/manifest/review` quorum komutunu çalıştır.~~ `PASS`
5. ~~E-F16/E-F20 kapanışını state/queue kayıtlarında uzlaştır ve executable guardlarla sıradaki paketi doğrula.~~ `PASS`
6. Blocking finding varsa Codex için yeni `T2/H2` döngüsü oluştur; eski approvalı taşıma.
7. ~~Guardlarla sıradaki paketi doğrula.~~ `PASS — FIX-005a`
8. **FIX-005a için actor-owned yerel branch/worktree oluştur ve activation record'u üretim değişikliklerinden önce kaydet.** `NEXT`
9. Sırayla FIX-005a, FIX-005, FIX-006, FIX-006b, FIX-007, FIX-008 ve kalan FIX-009 ailesini ele al.
10. Instrument/security kuyruğu kapanmadan yeni pahalı ölçüm veya GPU training başlatma.

### Faz B — Formal commissioning başlangıcı

AIRL planı açık biçimde ilk resmi paketin `WP-001 Commissioning Charter` olduğunu söyler. Mevcut V0 geriye dönük olarak ACCEPTED ilan edilmeyecek; önce aşağıdakiler kurulacak:

1. Named accountable owner ve bağımsız verifier ataması.
2. Sistem sınırı, NFR, risk ve insan karar haklarının dondurulması.
3. Ortam, bütçe, veri sınıfı ve execution profile kararı.
4. Kanıt manifesti ve paket durum registry'si.
5. WP-001 bağımsız kabulü.

### Faz C — Contract ve foundation dalgası

1. WP-011–020: kimlik, canonical authority ve schema contracts.
2. WP-021–024: ortam, repository ve CI kalite kapıları.
3. WP-025–030: PostgreSQL, object store, NATS/outbox, MLflow ve derived read models.

Bu fazda SQLite V0 verisi için kontrollü migration ve rollback planı hazırlanacak; doğrudan production veri taşıması yapılmayacak.

### Faz D — Control, agent ve güvenlik düzlemleri

1. Temporal tabanlı G0–G10 kontrol akışı.
2. Event/replay/DLQ davranışları.
3. LiteLLM ve Capability Registry.
4. LangGraph yalnız sınırlandırılmış bilişsel görevlerde.
5. Tool Broker ve Execution Broker.
6. Trust zone, sandbox, workload identity, OPA ve egress politikaları.

### Faz E — Literatür V0'ı formal platforma yükselt

1. SQLite kayıtlarını canonical PostgreSQL Source Registry'ye taşı.
2. DOI/kimlik çözümleme ve dedup/merge karar kayıtlarını ekle.
3. Seçilmiş koleksiyon/tag opt-in ve incremental `since` reader ekle.
4. Attachment, note ve annotation binding'lerini normalize et.
5. LiteratureSetManifest freeze ve immutable object store ekle.
6. Obsidian link integrity, human-preservation diff ve full rebuild kanıtlarını oluştur.
7. Zotero write-back ancak ayrı yetki, grup kütüphanesi ve audit politikasıyla değerlendirilsin.

### Faz F — Evidence, experience ve observability

1. Claim/Evidence Ledger.
2. Evidence locator ve citation entailment audit.
3. Run Registry ve MLflow.
4. Frozen review ve clean-room reproduction paketleri.
5. Cockpit, karar kuyruğu ve literature workbench.
6. OpenTelemetry, Langfuse, Grafana, cost ledger ve SLO.

### Faz G — Entegrasyon, commissioning ve production

1. WP-102–108 dikey dilimler.
2. WP-109–118 kabul registriesi, güvenlik, DR, performans ve operasyonel hazırlık.
3. ACC-01–ACC-40 senaryolarının aynı target üzerinde çalıştırılması.
4. En az iki restore tatbikatı.
5. Sıfır açık kritik bulgu.
6. Pilot cutover rehearsal.
7. İnsan onaylı production cutover ve hypercare.

## 9. Yetki ve insan kararı gerektiren sınırlar

Aşağıdaki işlemler kendiliğinden yapılmayacaktır:

- Yetkilendirilmiş `furkanhanilci/AI-Research-Framework` dışındaki bir repoya push veya merge.
- Production deploy veya dış ağdan API yayını.
- Zotero kayıtlarına yazma, silme veya otomatik merge.
- Büyük dependency/download veya bulut kaynağı açma.
- Uzun GPU training, model conversion veya quantization.
- Veri taşıma, geri döndürülemez migration veya artifact silme.
- İnsan karar hakkını etkileyen policy seçimi.

Her biri exact hedef, rollback, maliyet ve kabul kanıtı tanımlandıktan sonra ayrıca yürütülür.
Genel framework için izinli remote yalnız
`furkanhanilci/AI-Research-Framework` adresidir. SILBO model deposu ayrı iş akışı
ve ayrı yetki alanıdır; genel framework commit'leri oraya gönderilmez.

## 10. Başlıca riskler ve kontroller

| Risk | Kontrol |
|---|---|
| V0'ı tam sistem sanmak | Program matrisi ve açık status semantiği |
| İnsan Obsidian notlarının ezilmesi | Otomatik dal sınırı ve manifest-owned silme |
| Zotero verisinin değiştirilmesi | Salt-okunur adapter ve write tool yokluğu |
| Duplicate kaynakların yanlış birleşmesi | Yalnız raporlama, otomatik merge yok |
| Agent self-approval | Exact Fable review ve quorum |
| Bayat state dokümanı | Git SHA, executable guard ve artifact önceliği |
| Testin yanlış şeyi ölçmesi | İki yönlü test ve mutation zorunluluğu |
| Shared worktree hasarı | Actor-owned worktree ve dar Git işlemleri |
| Erken pahalı altyapı/training | Dependency ve resource gate |
| Production'a erken geçiş | 40 ACC, restore ve kritik bulgu şartı |

## 11. Geri alma ve yedek durumu

Eski Obsidian yerleşimi aşağıdaki yerel yedekte tutulur:

```text
/home/otonom/Desktop/FH/AIRL_OS_DEVREYE_ALMA_PLANI_v1.0/
  airl_bridge_api/data/projection-backups/
    vault-layout-before-silbo-main-20260821/
```

Bridge database dosyaları ve WAL dosyaları Git dışında tutulur. Unit dosyalarının kaynak kopyaları `airl_bridge_api/deploy/` altındadır. V0 kodu yerel Git commit'iyle geri alınabilir.

## 12. Her adımdan sonra güncelleme protokolü

Her maddi adım tamamlandığında şu sıra uygulanır:

1. İlgili komut/test/artifact çıktısını doğrula.
2. Bu belgenin `updated_at` alanını değiştir.
3. Yönetici özeti ve güncel durum tablosunu revize et.
4. İlgili faz veya adım durumunu güncelle.
5. Yeni kanıt, commit, target, handoff veya review SHA'sını ekle.
6. Yeni risk, sınırlama veya rollback bilgisini yaz.
7. `Sonraki exact adım` bölümünü tek bir yürütülebilir eylem olarak güncelle.
8. Aşağıdaki değişiklik günlüğüne yeni satır ekle.
9. Obsidian kopyası ile Git baseline kopyasının aynı olduğunu doğrula.

Bir adım `PASS`, `PARTIAL`, `BLOCKED` veya `FAIL` olarak açıkça etiketlenir. Kısmi başarı, başarısız alt maddeleri gizlemez.

## 13. Değişiklik günlüğü

| Zaman | Adım | Durum | Kanıt / not |
|---|---|---|---|
| 2026-08-21 | Yerel literatür V0 kurulumu | PASS | 33 kaynak, Bridge, Obsidian, Hermes MCP |
| 2026-08-21 | Obsidian klasör ve adlandırma revizyonu | PASS | Zotero kaynakları Literatür Setleri altında |
| 2026-08-21 | Timer ve işletim baseline | PASS | İlk oneshot success, Git `15d57af` |
| 2026-08-21 15:54 +03 | SILBO continuity ve snapshot kontrolü | PASS | H `ddad3ab`, protocol ve attestation PASS |
| 2026-08-21 15:54 +03 | FIX-004 Fable review başlatıldı | IN_PROGRESS | Review branch ve iki izole worktree oluşturuldu |
| 2026-08-21 15:54 +03 | Yaşayan durum/yol haritası belgesi oluşturuldu | PASS | Obsidian `10 - Projeler` alanı |
| 2026-08-21 15:59 +03 | Obsidian yerleşimi ve byte doğrulaması | PASS | Baseline/vault SHA-256 `571edd4c...` |
| 2026-08-21 15:59 +03 | FIX-004 Fable review tamamlandı | APPROVED | Review `efb87f2`, sealed exact T/H, yalnız review dosyası |
| 2026-08-21 16:01 +03 | FIX-004 review governed soya alındı | PASS | Commit `933f17f`, review byte hash eşit |
| 2026-08-21 16:01 +03 | FIX-004 exact review quorum | ACCEPTED | `status: PASS`, `errors: []`, reviewer `fable` |
| 2026-08-21 16:16 +03 | FIX-004 closeout kaydı | PASS | Yerel commit `5737757`; ham quorum + final sonuç |
| 2026-08-21 16:16 +03 | Ledger/queue/state uzlaştırması | PASS | Yerel commit `b96b989`; preflight PASS |
| 2026-08-21 16:16 +03 | GitHub yayın sınırı | USER DECISION | Hesap/repo verilene kadar remote write yok |
| 2026-08-21 16:29 +03 | GitHub hesap doğrulaması | PASS | Aktif hesap `furkanhanilci` |
| 2026-08-21 16:29 +03 | Genel private repo oluşturma | PASS | `furkanhanilci/AI-Research-Framework` |
| 2026-08-21 16:29 +03 | İlk framework push | PASS | `main=5efd305`; 16/16 test, secret/ignore kontrolü |
| 2026-08-21 16:29 +03 | Commissioning plan import hazırlığı | PASS | `planning/commissioning/`, 186 dosya |
| 2026-08-21 16:32 +03 | Genel framework plan yayını | PASS | Private remote `main=038f0ce`; 188 dosyalık commit |
| 2026-08-21 16:34 +03 | FIX-005a yerel aktivasyonu | PASS | Worktree/branch, task/state, preflight; commit `d86f5be` |

## 14. Sonraki exact adım

**`d86f5be` tabanından ayrı disposable worktree oluştur; production editinden önce FIX-005a A1–A4 varsayımlarını mutation/probe ile sınayıp sonuçları `coordination/evidence/SILBO-FIX-005a-challenge.md` altında kaydet.**

Yalnız `furkanhanilci/AI-Research-Framework` genel framework remote'u olarak yetkilidir. FIX-005a kabul edilmeden FIX-005 repair ölçümü, yeni training veya tam AIRL altyapı implementasyonu başlatılmaz.
