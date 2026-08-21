# AI Research Framework — Bağımsız Denetim Raporu

| Alan | Değer |
|---|---|
| Rapor tarihi | 2026-08-21 |
| Reviewer | Claude Opus 5 (bağımsız, salt-okunur inceleme) |
| İnceleme kökü | `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK` |
| Yöntem | Kaynak kod okuması, test çalıştırma, canlı servis sorgusu, SQLite sorgusu, hash doğrulama, plan tutarlılık analizi (script) |
| Değiştirilen dosya | Yok (bu rapor hariç) |
| Commit / push | Yapılmadı |

> Bu rapor, `docs/review/CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md` içindeki talimatı
> **girdi** olarak kabul eder, **otorite** olarak değil. Promptun kendisi de
> Bölüm K'de denetlenmiştir ve gerçek dizin yapısıyla uyumsuz bulunmuştur.

---

## A. Yönetici özeti

### Kısa cevap

Elinizde **çok iyi yazılmış bir plan** ve **küçük ama düzgün çalışan bir dikey
dilim** var. Aradaki mesafe, dokümantasyonun ima ettiğinden çok daha büyük.

- Plan: 130 WP + 40 ACC, 186 dosya, ~88.000 kelime.
- Uygulama: **1.509 satır Python**, 20 test, 1 SQLite tablosu, 33 kayıt.
- Bağımsız kabul edilmiş (`ACCEPTED`) work package sayısı: **0**.
- Ve aşağıda göstereceğim üzere, **mevcut koşullarda 0 olmaya devam etmek zorunda** —
  bu bir çalışma hızı problemi değil, planın yapısal bir kusuru.

### Karar

**NOT PRODUCTION-READY.** Bu beklenen ve dokümanlarda da doğru şekilde
belirtilmiş bir durum. Asıl bulgu şu değil.

**Asıl bulgu: plan bugünkü haliyle *başlatılamaz*.** İlk paket olan WP-001 dahil
hiçbir paketin Definition of Done'ı, bu organizasyonda ve bu altyapıda
karşılanamaz. Detay: Bulgu **C1** ve **C2**.

### Durum dağılımı (kanıt bazlı)

| Durum | WP (130) | ACC (40) |
|---|---:|---:|
| `IMPLEMENTED` (bağımsız kanıtla kabul edilmiş) | **0** | **0** |
| `PARTIAL` (çalışan kod var, kabul kriteri karşılanmamış) | **9** | 0 |
| `CONTRADICTED` (beyan var, karşılığı yok / çelişiyor) | **2** | 0 |
| `DOCUMENTED_ONLY` (plan var, çalışan karşılık yok) | **119** | 40 |
| `MISSING` (plan dosyası eksik) | 0 | 0 |
| `BLOCKED` (doğrulanamadı) | 0 | 0 |

`PARTIAL` olan 9 paket: WP-011, WP-014, WP-015, WP-020, WP-061, WP-062, WP-065,
WP-073, WP-074.
`CONTRADICTED` olan 2 paket: **WP-022** (teslimatı repoda yok — Bulgu C3),
**WP-064** (yetki sınırlandırması yok, tüm kişisel kütüphane okunuyor).

### En kritik üç engel

1. **Kanıt zinciri bootstrap deadlock'u** (C1) — Her paketin DoD'si "imzalı
   EvidenceManifest immutable store'a yazılmış" şartı taşıyor; immutable store
   WP-026. WP-001 bile kendi kanıtını yazacağı yere sahip değil ve planda geçici
   kanıt istisnası tanımlı değil.
2. **Organizasyonel imkânsızlık** (C2) — Plan 73 farklı owner ve 114 farklı
   verifier rolü varsayıyor; gerçek organizasyon 1 kişi. "Verifier üreticiden
   bağımsız" şartı tanım gereği karşılanamaz.
3. **Kanıt teatrosu riski** (H3, M2, M3) — Şu anda "read-only kanıtı" olarak
   gösterilen üç artifact da aslında sabit bir `False` değerini test ediyor;
   "smoke test" hata durumunda bile exit 0 dönüyor; "acceptance" scripti
   kullanıcının kişisel kütüphanesindeki "LiDAR" kelimesine bağımlı.

### Şu an güvenle çalıştırılabilecek gerçek dikey dilim

`Zotero Local API (read-only) → SQLite registry → Obsidian projeksiyon → Hermes MCP (5 read-only tool)`

Bu dilim gerçekten çalışıyor, gerçekten idempotent ve gerçekten yerel. **33
kaynak, 3 kategori, 20/20 test PASS, servis ve timer aktif** — doğrulandı.
Sınırı: kütüphane 100 kaynağı geçtiği an sessizce eksik senkron etmeye başlar
(Bulgu H1).

---

## B. Repository ve environment snapshot

| Alan | Değer | Not |
|---|---|---|
| Framework kökü | `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK` | **Git deposu değil.** `.git`, `.codex`, `.agents` boş dizinler |
| Kanonik plan ağacı | `planning/commissioning/` (186 dosya) | **Versiyon kontrolü altında değil** |
| Uygulama reposu | `.` (repo koku) | Git repo, branch `main`, HEAD `6c849bd` |
| Remote | `https://github.com/furkanhanilci/AI-Research-Framework.git` | private, default `main` |
| Local vs remote | `0 ahead / 0 behind` — senkron | `origin/main = 6c849bd` |
| Çalışma ağacı | Temiz | `git status --short` boş |
| Takip edilen dosya | 434 | 211'i `vault_baseline/` |
| Python | 3.11, `.venv` mevcut | `uv` yönetimli |
| Test sonucu | **20 passed** | `.venv/bin/python -m pytest -q`, exit 0 |
| Bridge servisi | `active` | `/health` ve `/ready` 200 döndü |
| Sync timer | `active`, son çalışma 8 dk önce | 30 dk periyot |
| Kayıt sayısı | 33 kaynak, 25 sync run | Son 8 run: `SUCCEEDED`, 33 fetched / 33 unchanged |
| Plan hash doğrulaması | **184/184 OK** | `sha256sum -c SHA256SUMS.txt` |
| Vault | `/home/otonom/Documents/Obsidian Vault`, 246 not | baseline ile içerik olarak eşleşiyor |
| Wikilink bütünlüğü | 103 link, **0 kırık** | script ile doğrulandı |
| Plan içi markdown link | 1011 link, **0 kırık** (her üç kopyada da) | script ile doğrulandı |
| CI | **Yok** | `.github`, `Makefile`, `ruff`, `mypy`, `pre-commit` — hiçbiri yok |

---

## C. Gerçekten çalışan şeyler (hakkını teslim edelim)

Bunları küçümsemeyin; birçoğu bu ölçekte nadiren doğru yapılıyor:

1. **Idempotent upsert.** `content_hash` karşılaştırmasıyla insert/update/unchanged
   ayrımı doğru; `(library_type, library_id, key)` üzerinde UNIQUE constraint var.
   Test edilmiş: `tests/test_database.py:5`.
2. **Kararlı kimlik.** `airl_id`, Zotero item key binding'inin hash'i — başlık
   değişince kimlik değişmiyor. Test edilmiş: `tests/test_zotero.py:9`.
3. **Atomik dosya yazımı.** `mkstemp` + `fsync` + `os.replace` — kısmi yazılmış
   Markdown dosyası oluşmaz (`obsidian.py:253`).
4. **Manifest sahipli silme.** Projeksiyon yalnızca kendi manifestinde kayıtlı
   dosyaları siler; insan notu aynı klasörde olsa bile korunur. **Gerçek bir
   testi var**: `tests/test_obsidian.py:72`. Bu, veri kaybına karşı en önemli
   savunma ve doğru kurulmuş.
5. **Path traversal savunması.** Hem config seviyesinde (`config.py:58`) hem
   projeksiyon seviyesinde (`obsidian.py:42`, `:124`) vault dışına çıkış engelli.
6. **Loopback zorlaması.** `config.py:47` — `AIRL_API_HOST` loopback dışında bir
   değer alırsa servis başlamayı reddediyor. Bu iyi bir fail-closed default.
7. **XSS/enjeksiyon kaçışı.** Abstract ve başlık `html.escape`, YAML string'leri
   `json.dumps` ile kaçırılıyor; testi var (`tests/test_obsidian.py:5`).
8. **systemd sertleştirmesi.** `NoNewPrivileges`, `ProtectSystem=strict`,
   `ProtectHome=read-only` + dar `ReadWritePaths`. Bu seviyede hardening beklenmezdi.
9. **Plan bütünlüğü.** 130 paketin bağımlılık grafiği **döngüsüz**, hepsi
   topolojik sırada (ileri numaralı bağımlılık: 0), CSV ile dosya seti birebir
   örtüşüyor, 1011 iç link sağlam, 184 dosyanın hash'i tutuyor. Bu ciddi bir emek.
10. **Dürüst durum semantiği.** `ai_research_framework_current_status_and_roadmap.md`
    §2, `V0 HAZIR ≠ ACCEPTED` ayrımını açıkça yapıyor. Bu dokümanın kendisi
    "pazarlama özeti" değil. Bunu koruyun.

---

## D. Bulgular

Format: `ID | Severity | Başlık` → Kanıt → Etki → Öneri.

### C1 — CRITICAL — Kanıt zinciri bootstrap deadlock'u: hiçbir paket ACCEPTED olamaz

**Kanıt:**
- `00_PROGRAM/05_DEFINITION_OF_READY_DONE.md:41` — DoD: *"Evidence manifest
  imzalanmış ve immutable store'a yazılmıştır."*
- `01_GOVERNANCE/WP-001_commissioning_charter.md`, zorunlu teslimatlar:
  `- İmzalı EvidenceManifest` — bu satır **130/130** WP dosyasında var.
- `paket_bagimlilik_matrisi.csv` — immutable store = **WP-026**, bağımlılıkları
  `WP-021;WP-014` → `WP-020` → `WP-011` → `WP-010` → ... → `WP-001`.
- `00_PLANIN_KULLANIMI.md`, `06_KANIT_VE_KABUL_STRATEJISI.md`,
  `05_DEFINITION_OF_READY_DONE.md` içinde **bootstrap/geçici kanıt istisnası
  tanımlı değil** (grep: yalnız `TemporaryControlRecord` geçiyor, kanıt deposu
  için değil manuel kontrol için).

**Etki:** Bağımlılık grafiği döngüsüz olsa da **kanıt zinciri döngüsel**. WP-001'i
kabul etmek için imzalı bir evidence manifest'i immutable store'a yazmanız
gerekiyor; immutable store WP-026, o da 5 seviye aşağıda. Program teknik olarak
adım 1'de duruyor.

**Öneri:** WP-001'den önce bir **WP-000 Interim Evidence Policy** tanımlayın:
- Geçici kanıt deposu: `delivery/WP-xxx/` + `evidence-manifest.json`
  (dosya adı, sha256, üretici komut, target git SHA, timestamp).
- "İmza" yerine geçecek geçici mekanizma: git commit SHA + `git tag -s` veya en
  azından append-only bir `EVIDENCE_LEDGER.md`.
- Bu geçici mekanizmanın WP-026 tamamlandığında nasıl migrate edileceği ve
  expiry kriteri yazılı olsun (planın kendi `TemporaryControlRecord` formatı buna uyar).

---

### C2 — CRITICAL — Plan 73 owner + 114 verifier rolü varsayıyor; organizasyon 1 kişi

**Kanıt:**
- `paket_bagimlilik_matrisi.csv` analizi: **73 farklı `owner`**, **114 farklı
  `verifier`** değeri, 130 satırda.
- `05_DEFINITION_OF_READY_DONE.md:35` — *"Verifier üreticiden bağımsız doğrulama
  yapmıştır."*
- `05_DEFINITION_OF_READY_DONE.md:52` (Kabul edilmeyen kanıtlar) — *"Agent'ın veya
  implementer'ın serbest metin 'başarılı' beyanı"*, *"Reviewer'ın producer trace'ini
  görerek verdiği bağımsızlık iddiası"*.
- Gerçek durum: tüm vault notlarında `owner: otonom`; `CODEOWNERS` yalnız bir
  yorum satırı içeriyor, hiçbir sahip tanımlı değil.
- Efor dağılımı: **83 paket "L"**, 42 "M", 5 "S". Takvim yok
  (`08_KAPASITE_VE_TAHMIN.md`: *"sabit takvim yok"*).

**Etki:** 83 adet "L" efor paketini, ayrı bir assurance havuzuyla, bağımsız
verifier ile yürütmek kurumsal bir programın iş tanımı. Tek kişilik bir
organizasyonda bağımsızlık şartı **tanım gereği** karşılanamaz — SILBO tarafında
kullandığınız "sealed Fable review" yaklaşımı bunun tek gerçekçi ikamesi ve plan
bu ikameyi hiçbir yerde tanımlamıyor.

**Öneri:** İki seçenekten birini **açıkça** seçin ve planın 00_PROGRAM'ına yazın:
- **(a) Kapsamı küçültün:** 130 paketi, tek kişinin yürütebileceği ~20-25 paketlik
  bir "AIRL-OS Personal Edition"a indirin. Kalanları `DEFERRED` olarak işaretleyin.
- **(b) Bağımsızlık modelini yeniden tanımlayın:** SILBO'daki sealed-review +
  exact-quorum protokolünü framework'ün resmi verifier mekanizması yapın
  (WP-007'nin gerçek uygulaması bu olur). Farklı model ailesi + sealed context +
  exact T/H = "bağımsızlık" tanımını yazılı hale getirin.

Bu karar verilmeden yazılacak her satır kod, kabul edilemez kod olacak.

---

### C3 — CRITICAL — WP-022 "TECH_COMPLETE" beyan edildi; teslimatı repoda yok

**Kanıt:**
- `implementation_log.md:164-166` — *"WP-022 için ilk repository skeleton alanları
  eklendi: `schemas/`, `policy/`, `infra/`, `services/`, `workflows/`, `agents/`,
  `delivery/` ve `docs/architecture/`."*
- `ls -A`: `services/`, `workflows/`, `agents/`, `infra/`, `policy/`,
  `delivery/WP-011/`, `delivery/WP-014/`, `delivery/WP-015/`, `delivery/WP-020/`
  — **hepsi boş**.
- `git ls-files | grep -E '^(services|workflows|agents|infra|policy|delivery)/'`
  → **hiçbir çıktı yok**. Git boş dizin takip etmez.
- Dolayısıyla `github.com/furkanhanilci/AI-Research-Framework` reposunda bu
  dizinlerin **hiçbiri yok**.
- Yardımcı teslimatlar da içi boş:
  - `docs/architecture/FOUNDATION.md` → tek satır: `# Foundation repository skeleton`
  - `schemas/README.md` → tek satır: `# Shared contract schemas`
  - `dependency-rules.txt` → tek satır, ayrıştırılamaz düz metin:
    `src/airl_framework -> schemas, policy; src/airl_bridge -> services/knowledge; tests -> all owners`
  - `CODEOWNERS` → yalnız bir yorum satırı, sıfır kural. **Hiçbir şeyi zorlamıyor.**

**Etki:** Bu, planın kendi yasakladığı kanıt tipinin ta kendisi
(`05_DEFINITION_OF_READY_DONE.md:52`: *"Agent'ın serbest metin 'başarılı' beyanı"*).
Implementation log'a `TECH_COMPLETE` yazılmış bir iş, uzak repoda hiç yok.

**Öneri:** WP-022 durumunu `implementation_log.md`'de derhal `NOT_STARTED`'a
düşürün. Yeniden yaparken: her dizine `.gitkeep` + gerçek bir sınır dosyası
(örn. `policy/` içinde çalışan bir OPA/rego veya en az bir JSON şema),
`CODEOWNERS`'a gerçek kural, `dependency-rules.txt` yerine **CI'da zorlanan**
bir import-linter/`tach` konfigürasyonu.

---

### H1 — HIGH — Zotero ingest 100 kayıtta sabit tavanlı; sayfalama ve incremental sync yok

**Kanıt:**
- `src/airl_bridge/zotero.py:41` — `safe_limit = max(1, min(limit, 100))`
- `src/airl_bridge/main.py:126,136` — `Query(default=100, ge=1, le=100)`
- `src/airl_bridge/cli.py:68` — `choices=range(1, 101)`
- `deploy/airl-bridge-sync.service` — `POST /v1/sync?limit=100`
- `fetch_top_items` tek bir `GET /items/top` çağrısı yapıyor; `start` parametresi,
  `Total-Results` header okuması veya `since=` versiyon parametresi **yok**.

**Etki:** Kütüphane 100 kaynağı geçtiği an senkron **sessizce eksik** çalışmaya
başlar. Hata yok, uyarı yok; `sync_runs` tablosuna `SUCCEEDED` yazılır.
Dahası: `project_obsidian()` veritabanının tamamını projekte ettiği için, 100
tavanı yüzünden hiç girmemiş kaynaklar Obsidian'da da hiç görünmez. Şu anda 33
kaynakla gizli; büyüdüğünüz gün fark edilmesi çok zor bir veri eksikliği olur.

**Öneri (öncelik 1):**
- `fetch_top_items` içinde `start`/`limit` ile sayfalama döngüsü; `Total-Results`
  header'ını okuyup tam kapsamı doğrulayın.
- `sync_runs` tablosuna `library_version` (Zotero `Last-Modified-Version`) ekleyip
  sonraki çağrıda `?since=` kullanın (bu aynı zamanda WP-067'nin çekirdeği).
- `fetched < total` durumunda run'ı `PARTIAL` olarak işaretleyin, `SUCCEEDED` değil.

---

### H2 — HIGH — Zotero'da silinen kayıt registry'de ve Obsidian'da sonsuza kadar kalır

**Kanıt:**
- `src/airl_bridge/database.py` — `DELETE` veya tombstone içeren tek bir sorgu yok.
- `src/airl_bridge/service.py:41` — `project_obsidian()` DB'nin tamamını projekte eder.
- `obsidian.py:112` `_remove_stale()` yalnız "DB'de artık projeksiyona girmeyen"
  dosyaları siler; DB hiç küçülmediği için bu yol pratikte hiç tetiklenmez.
- Zotero `/deleted` endpoint'i hiç çağrılmıyor.

**Etki:** Kullanıcı Zotero'dan bir kaynağı sildiğinde veya kütüphaneden
çıkardığında, kaynak kanonik registry'de ve Obsidian'da kalır. Zamanla vault
"hayalet kaynak" biriktirir. Bu doğrudan planın 6 numaralı invariant'ını
("derived graph canonical kayıtlardan sıfırdan yeniden kurulabilir") ihlal eder:
canonical kayıt zaten yanlış.

**Öneri:** `since=` senkronuyla birlikte Zotero `/deleted?since=N` okuması ekleyin;
silinenleri **silmeyin**, `status = WITHDRAWN` + `withdrawn_at` ile tombstone
yapın (plan WP-011-T05 zaten bunu istiyor) ve projeksiyondan çıkarın.

---

### H3 — HIGH — `zotero_write_enabled` ölçülen bir kontrol değil, sabit; üç "kanıt" artifact'i bunu test ediyor

**Kanıt:**
- `src/airl_bridge/models.py:65` — `zotero_write_enabled: bool = False` (varsayılan)
- `src/airl_bridge/main.py:62-68` — `HealthResponse(...)` bu alanı **hiç set etmiyor**,
  yani her zaman varsayılan `False`.
- `src/airl_bridge/mcp_server.py:78` — `health.get("zotero_write_enabled", False)`
  — alan gelmese bile `False`.
- `src/airl_bridge/cli.py:34` — `"zotero_write_enabled": False` — düz sabit.
- Ve bunu "doğrulayan" üç artifact:
  - `tests/test_api.py:26` — `assert payload["zotero_write_enabled"] is False`
  - `scripts/acceptance_v0.py:41` — `require(health["zotero_write_enabled"] is False, ...)`
  - `scripts/acceptance_v0.py:77` — çıktıya yine sabit `False` yazıyor.

**Etki:** Bu bir totoloji. `False is False` test ediliyor. Kod yarın bir
`httpx.post` çağrısı kazansa bu üç kontrol de yeşil kalır. `README.md:31`,
`ARCHITECTURE_V0.md` ve status dokümanının en güçlü güvenlik iddiası —
"Zotero'ya yazılmıyor" — **sıfır test kapsamına sahip**.

**Öneri:**
- `HealthResponse.zotero_write_enabled` alanını kaldırın veya gerçekten
  hesaplanan bir değere bağlayın.
- Yerine **davranışsal bir test** yazın: `ZoteroClient`'a `MockTransport` verin ve
  `GET` dışında bir method geldiğinde `AssertionError` fırlatan handler ile tüm
  `sync` akışını çalıştırın. Bu, iddiayı gerçekten kanıtlar.
- Statik bir kontrol ekleyin (CI): `src/airl_bridge/zotero.py` içinde
  `post|put|patch|delete` regex'i eşleşirse build fail.

---

### H4 — HIGH — `airl_framework` contract çekirdeğinin sıfır üretim tüketicisi var; hâlâ mevcut sistemle çelişiyor

**Kanıt:**
- `grep -rn airl_framework` → yalnız `pyproject.toml:28`, `tests/test_contracts.py:3`
  ve iki vault notu. **`src/airl_bridge/` içinde tek bir import yok.**
- Bridge hiçbir `EventEnvelope` üretmiyor; sistemde event bus da yok.
- Çelişki: `contracts.py:11` → `_HASH_RE = ^[0-9a-f]{64}$` (çıplak digest).
  `zotero.py:104` → `content_hash = "sha256:" + hexdigest` (prefix'li).
  Yani mevcut kanonik kayıt, yeni yazılan `ArtifactManifest` sözleşmesini
  **daha doğduğu gün ihlal ediyor**.
- `SourceRecord.airl_id` hiçbir yerde `Identity` ile doğrulanmıyor.
- `SchemaRegistry` bir `dict` — kalıcı değil, JSON Schema kabul etmiyor
  (`Mapping[str, Any]` olarak saklayıp hiç valide etmiyor), CI tarafından
  zorlanmıyor. WP-020'nin beklenen sonucu *"CI tarafından zorlanır"* idi.

**Etki:** `implementation_log.md` Step 001, WP-011/014/015/020'yi
`TECH_COMPLETE` ilan ediyor. Gerçekte: 170 satırlık, hiçbir şeye bağlı olmayan,
mevcut veri modeliyle uyumsuz bir kütüphane. Testleri geçiyor ama
`05_DEFINITION_OF_READY_DONE.md:56`'nın yasakladığı şey bu:
*"Test geçiyor ama gereksinim yok"*.

**Öneri:** Yeni contract yazmadan önce **mevcut olanı bağlayın**:
1. `content_hash` formatını tek bir tanıma çekin (öneri: çıplak 64-hex + ayrı
   `hash_algo` alanı). Migration scripti + geri alma yolu yazın.
2. `SourceRecord.airl_id` üretimini `Identity` üzerinden geçirin — böylece
   contract'ın en az bir gerçek tüketicisi olur.
3. `SchemaRegistry`'yi `schemas/*.json` dosyalarından yükleyen ve `jsonschema` ile
   gerçekten valide eden bir yapıya çevirin; aksi halde WP-020 `MISSING`'dir.

---

### H5 — HIGH — CI yok; WP-024 ve WP-020'nin kabul kriteri yapısal olarak imkânsız

**Kanıt:** `.github/`, `.gitlab-ci.yml`, `Makefile`, `ruff.toml`, `mypy.ini`,
`.pre-commit-config.yaml` — **hiçbiri yok**. `pyproject.toml` içinde yalnız
`[tool.hatch...]` ve `[tool.pytest...]` var; lint/type/format konfigürasyonu yok.

**Etki:** Testler yalnız elle çalışıyor. `05_DEFINITION_OF_READY_DONE.md:24`
("Unit ve package-level integration testleri çalışmıştır") her paket için manuel
beyana dayanacak — yani C2/C3 problemi her pakette tekrar edecek. WP-020'nin
"producer/consumer compatibility CI tarafından zorlanır" hedefi zorlanacak bir
CI olmadığı için tanım gereği karşılanamaz.

**Öneri (öncelik 2, C1'den hemen sonra):** Tek bir GitHub Actions workflow'u:
`uv sync` → `ruff check` → `pytest -q` → H3'teki read-only statik kontrolü →
`sha256sum -c` plan bütünlük kontrolü. Bu tek dosya, üç ayrı bulguyu birden kapatır
ve kanıt üretimini otomatikleştirir.

---

### M1 — MEDIUM — Kimlik doğrulaması olmayan mutating endpoint'ler + Host header doğrulaması yok

**Kanıt:** `src/airl_bridge/main.py:124-138` — `POST /v1/ingest/zotero`,
`POST /v1/project/obsidian`, `POST /v1/sync`. Auth yok, token yok, CSRF koruması
yok. `create_app` içinde **hiçbir middleware yok** — ne `CORSMiddleware`,
ne `TrustedHostMiddleware`.

**Etki (loopback'e rağmen gerçek):**
- **CSRF:** Tarayıcıdaki herhangi bir sayfa, `fetch('http://127.0.0.1:8765/v1/sync?limit=100', {method:'POST', mode:'no-cors'})` ile
  preflight'sız "simple request" gönderebilir. Yanıtı okuyamaz ama **yan etki
  gerçekleşir**: senkron çalışır ve vault'un `Zotero Sources` dalı yeniden yazılır.
- **DNS rebinding:** `Host` header doğrulanmadığı için, saldırganın alan adını
  127.0.0.1'e rebind etmesi durumunda origin aynı sayılır ve `GET /v1/sources`
  ile **tüm literatür kayıt defteri okunabilir**.
- Makinedeki her yerel process de aynı yetkilere sahip.

**Öneri:** Düşük maliyetli, yüksek etkili:
- `TrustedHostMiddleware(allowed_hosts=["127.0.0.1", "localhost", "127.0.0.1:8765"])`
- Mutating endpoint'ler için `.env`'den okunan bir `AIRL_API_TOKEN` ve
  `X-AIRL-Token` header kontrolü (systemd sync unit'i de bu header'ı gönderir).
  Custom header, CSRF'i tek başına kapatır (preflight zorunlu hale gelir).

---

### M2 — MEDIUM — `mcp_smoke.py` hiçbir şeyi assert etmiyor; her koşulda exit 0

**Kanıt:** `scripts/mcp_smoke.py:25-31` — `status.isError` ve `search.isError`
değerleri **raporlanıyor**, kontrol edilmiyor. Fonksiyonda `assert`/`raise`/
`sys.exit` yok. Tool listesinin "tam 5 read-only tool" olduğu da doğrulanmıyor
(`README.md:127` ve `OPERATIONS.md` bunu iddia ediyor).

**Etki:** `README.md:117` ve `OPERATIONS.md` bu scripti doğrulama adımı olarak
gösteriyor. Bridge tamamen kapalı olsa bile script JSON basıp **0 ile çıkar**.
Bir insan çıktıyı okumazsa yeşil sanılır.

**Öneri:** `assert not status.isError`, `assert not search.isError`,
`assert sorted(t.name for t in tools.tools) == [beş isim]` ekleyin. Beş satır.

---

### M3 — MEDIUM — `acceptance_v0.py` kullanıcının kişisel verisine bağımlı; tekrar üretilemez

**Kanıt:** `scripts/acceptance_v0.py:39,49` —
`lidar_results = get("/v1/sources/search", q="LiDAR", limit=2)` ve
`require(bool(lidar_results), "Source search returned no LiDAR result")`.

**Etki:** Bu "acceptance" yalnız *bu* makinede, *bu* Zotero kütüphanesiyle geçer.
Kullanıcı LiDAR makalelerini silse acceptance kırmızıya döner. Planın kendi
kuralı (`06_KANIT_VE_KABUL_STRATEJISI` / `05_DoD`: aynı target revision üzerinde
tekrar üretilebilir kanıt) karşılanmıyor. Ayrıca canlı servise ihtiyaç duyduğu
için CI'da çalıştırılamaz.

**Öneri:** İki parçaya bölün: (a) veriden bağımsız yapısal acceptance
(manifest/registry sayı tutarlılığı, dashboard varlığı, kategori toplamı) — CI'da
sabit fixture ile çalışır; (b) canlı ortam smoke'u — arama sorgusunu `.env`'den
alsın, boş sonuç `SKIPPED` olsun, `FAIL` değil.

---

### M4 — MEDIUM — Plan 4 fiziksel kopyada yaşıyor; kanonik otorite çelişkili

**Kanıt:**
| # | Konum | Versiyon kontrolü | Bütünlük |
|---|---|---|---|
| 1 | `planning/commissioning/` | **Yok** (kök git repo değil) | `SHA256SUMS.txt` 184/184 OK |
| 2 | `planning/commissioning/` | Var (git) | Manifest yok |
| 3 | `vault_baseline/.../01 - Commissioning/` | Var (git) | Manifest yok, dosya adları farklı |
| 4 | `~/Documents/Obsidian Vault/.../01 - Commissioning/` | Yok | Manifest yok |

- Kopya 1 ve 2 **zaten ayrışmış**: `diff -rq` 12 dosyada fark buluyor
  (README'de `**Sürüm:**` satırları liste formatına çevrilmiş, bazı dosyalarda
  trailing newline farkı).
- Kopya 3/4, `SHA256SUMS.txt` ve `paket_bagimlilik_matrisi.csv` dosyalarını
  **içermiyor** — yani Obsidian aynası bütünlük açısından hiç doğrulanamaz.
- Kanonik otorite çelişkisi:
  - `00_navigation_and_execution_cockpit.md:8,24` → *"kanonik kopya: `planning/commissioning/`"*
  - `ai_research_framework_current_status_and_roadmap.md:77-84` → `planning/commissioning/` "hedef mimariyi tanımlar"
  - `CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md:59-73` → inceleme kökü olarak `planning/commissioning/`

**Etki:** Bu, tam olarak WP-012'nin ("Canonical Sahiplik ve Alan Bazlı Otorite
Matrisi") çözmesi gereken problem — ve plan bu problemi kendi üzerinde yaşıyor.
`09_DEGISIKLIK_VE_KONFIGURASYON_KONTROLU.md`'nin varlığına rağmen drift zaten başlamış.

**Öneri:**
1. Tek kanonik kopya seçin (öneri: `planning/commissioning/` —
   çünkü versiyon kontrolünde ve remote'ta).
2. `planning/commissioning/` kökünü ya silin ya da symlink yapın.
3. Obsidian aynasını **üretilen** hale getirin: `scripts/mirror_plan.py`
   (kanonik → vault, isim normalizasyonu + link yeniden yazımı) ve
   `scripts/check_plan_drift.py` (CI'da hash karşılaştırması).
4. `SHA256SUMS` dosyasını kanonik kopyanın yanında tutun ve CI'da doğrulayın.

---

### M5 — MEDIUM — WP↔ACC izlenebilirliği 39/40 vakada tutarsız

**Kanıt (script analizi):**
- CSV `scenarios` sütunundan çıkan WP↔ACC eşlemesi ile ACC dosyalarının
  *"İlgili paketler"* alanı **40 senaryodan 39'unda uyuşmuyor**.
  Örnek ACC-01: CSV → 12 paket (`WP-035, 050, 064, 065, 070, 072, 094, 103, 110, 115, 119, 120`),
  ACC dosyası → 5 paket (`WP-062, 065, 069, 072, 103`). İki liste birbirinin alt
  kümesi bile değil (`WP-062`, `WP-069` CSV'de yok).
- **62/130 WP**, hiçbir ACC dosyasında referans edilmiyor.
- **39/130 WP** kartında ACC alanı hâlâ placeholder:
  *"İlgili dikey dilim ve commissioning sırasında atanır"*.

**Etki:** `11_KAPSAM_KARSILIK_MATRISI` ve DoD'nin `COMMISSIONED` tanımı
("paketi kullanan ilgili ACC senaryolarının tamamı geçmeli") makineyle
hesaplanamıyor. Hangi ACC'nin hangi paketi kapattığı iki kaynağa göre farklı.

**Öneri:** İzlenebilirliği tek yönlü üretin: CSV'yi tek gerçek kaynak yapın,
ACC dosyalarındaki "İlgili paketler" alanını **CSV'den üretin**, ve CI'da
"her WP en az bir ACC'ye bağlı" + "iki yön tutarlı" kontrolünü çalıştırın.
39 placeholder'ı doldurun veya o paketleri açıkça `NO_ACC_REQUIRED` işaretleyin.

---

### M6 — MEDIUM — `sync` işleminde transaction sınırı ve compensation yok

**Kanıt:** `src/airl_bridge/service.py:45-48` —
```python
ingest = await self.ingest_zotero(limit=limit)   # DB commit edildi
projection = self.project_obsidian()              # burada patlarsa?
```
- `finish_sync()` yalnız `IngestResult` alanlarını kaydediyor (`service.py:35`);
  projeksiyon sonucu **hiçbir yere yazılmıyor**.
- `ProjectionError` → HTTP 422 (`main.py:56`), ama registry çoktan ilerlemiş.

**Etki:** Vault kilitli/dolu/erişilemez olduğunda registry ile Obsidian arasında
sessiz bir divergence oluşur ve bunun kaydı hiçbir yerde tutulmaz. Sonraki timer
`unchanged` göreceği için projeksiyonu **tekrar denemez bile** — hayır, denerdi
(projection her seferinde tam yeniden yazım), ama arada geçen sürede vault yanlış
durumda kalır ve bu durum audit edilebilir değildir.

**Öneri:** `sync_runs` tablosuna `projection_status`, `projected`,
`removed_stale`, `projection_error` sütunları ekleyin; `sync()`'i
`ingest → projection` sırasında projeksiyon hatasında run'ı `PARTIAL` yapacak
şekilde sarın. Bu WP-038'in (human updates & compensation) V0 karşılığıdır.

---

### M7 — MEDIUM — Projeksiyon, dry-run'sız ve hedef-doğrulamasız yıkıcı dosya işlemi

**Kanıt:** `obsidian.py:112-132` — manifestte kayıtlı her `.md` dosyası
koşulsuz `unlink()` ediliyor; `_remove_empty_parents` ile dizinler de siliniyor.
Config doğrulaması yalnız mutlak yol ve `..` engelliyor (`config.py:58`).
`AIRL_OBSIDIAN_GENERATED_DIR` `.env`'den geliyor ve `.env` **0644**.

**Etki:** `AIRL_OBSIDIAN_GENERATED_DIR` bir gün yanlışlıkla `20 - Source Notes`
gibi bir insan klasörüne işaret ederse: ilk run oraya üretir + manifest yazar,
ikinci run manifestteki dosyaları siler. Mevcut test (`test_obsidian.py:72`)
insan dosyasını koruyor — ama yalnız *manifeste girmemiş* dosyayı. Bir kez
projekte edilmiş bir yol geri dönülmez şekilde yönetime alınır.

**Öneri:**
- `--dry-run` bayrağı ve `POST /v1/project/obsidian?dry_run=true`.
- Hedef dizin boş değilse ve manifest yoksa → **reddet**, otomatik adopte etme.
- `projected == 0 && removed_stale > 0` durumunda (yani "her şeyi sil") ek onay
  iste; şu an bu durum sessizce tüm dalı temizler.

---

### M8 — MEDIUM — SQLite bağlantıları hiç kapatılmıyor

**Kanıt:** `database.py:60-67` `connect()` her çağrıda yeni bağlantı açıyor.
`with self.connect() as connection:` — Python `sqlite3`'te bu **transaction**
context manager'ıdır, bağlantıyı **kapatmaz**. `close()` çağrısı dosyada hiç yok.
`list_sources`, `get_source`, `search_sources`, `count_sources`,
`list_category_counts`, `start_sync`, `finish_sync`, `upsert_sources`,
`initialize` — dokuzu da aynı desende.

**Etki:** Her HTTP isteği bir bağlantı sızdırıyor; GC'ye kadar açık kalıyor.
33 kayıt ve 30 dakikalık timer ile fark edilmez; WAL dosyası ve fd sayısı
gerçek yükte sorun çıkarır.

**Öneri:** `contextlib.closing(...)` ile sarın veya `Database`'i bir
connection-per-request bağımlılığına çevirin. Beş satırlık düzeltme.

---

### M9 — MEDIUM — 10.000 satırlık sessiz kesme (silent truncation)

**Kanıt:** `service.py:42` `list_sources(limit=10_000)`,
`main.py:114` `duplicate_source_groups(database.list_sources(limit=10_000))`.

**Etki:** 10.000'i aşan kütüphanede projeksiyon kaynakların bir kısmını görmez,
sonra `_remove_stale` **görmediği kaynakların dosyalarını "bayat" sayıp siler**.
H1 (100 tavanı) bugün bunu maskeliyor; H1 düzeltilirse M9 aktif bir veri kaybı
yoluna dönüşür. **H1'i M9'dan önce düzeltmeyin.**

**Öneri:** `list_sources`'a sayfalayan bir iterator ekleyin (`iter_sources()`)
ve projeksiyonu onun üzerinden çalıştırın; limit varsayılanını kaldırın.

---

### M10 — MEDIUM — Dokümantasyon drift'i (yeniden adlandırma sonrası güncellenmemiş)

**Kanıt:**
| Dosya | İçerik | Gerçek |
|---|---|---|
| `docs/ARCHITECTURE_V0.md` | `00 - Plan Navigasyonu ve Yürütme Kokpiti.md` | `00_navigation_and_execution_cockpit.md` |
| `docs/ARCHITECTURE_V0.md` | `AI Research Framework — Current Status and Roadmap.md` | `ai_research_framework_current_status_and_roadmap.md` |
| `docs/ARCHITECTURE_V0.md` (invariant 4) | `70 - Literatür Setleri` | `70 - Literature Sets` |
| `..._current_status_and_roadmap.md:231` | "Python testleri: **16/16** PASS" | **20** (`implementation_log.md:183` doğru yazmış) |
| `deploy/airl-bridge-sync.service` | "SILBO Obsidian literature tree" | SILBO/framework ayrımı yapıldıktan sonra kalmış |
| `deploy/airl-bridge-sync.timer` | "SILBO Zotero to Obsidian synchronization" | aynı |

`implementation_log.md` Step 000-F bu yeniden adlandırmayı `PASS` olarak
kaydediyor, ama en az 6 yerde eski isimler kalmış.

**Not:** systemd unit'lerinin repo kopyası ile kurulu kopyası arasındaki tek fark
sondaki boş satırdır — **gerçek bir drift değil**, kontrol edildi.

**Öneri:** `scripts/check_docs.py` — dokümanlarda geçen vault yollarının gerçekten
var olduğunu doğrulayan bir kontrol; CI'da çalışsın. Test sayısını dokümana elle
yazmayı bırakın.

---

### M11 — MEDIUM — Kanonik plan ağacı versiyon kontrolü altında değil

**Kanıt:** Framework kökündeki `.git` **boş bir dizin**, git deposu değil
(`git status` → `fatal: not a git repository`). `planning/commissioning/`
(186 dosya, hash mühürlü) hiçbir repoda takip edilmiyor.

**Etki:** SHA256SUMS ile mühürlenmiş "kanonik" ağacın geçmişi yok, geri alınamaz,
yedeklenmiyor. Yanlışlıkla silinirse yalnızca `planning/commissioning/`
kopyasından (ki o zaten ayrışmış) kurtarılabilir.

**Öneri:** M4 ile birlikte çözün — tek kopya, git içinde, hash manifesti yanında.

---

### L1 — LOW — `.env` ve `.env.example` bayt-bayt aynı; example gerçek yolları içeriyor

`.env` ile `.env.example` identical (315 byte), izin `0644`.
`.env.example` git'te takip ediliyor ve kullanıcının gerçek ev dizini yollarını
(`/home/otonom/Documents/Obsidian Vault`) private repoya yayınlıyor. Şu an secret
yok ama `.env` secret için tasarlanmış dosya; ilk token eklendiğinde `chmod 600`
unutulacak.

**Öneri:** `.env.example`'ı gerçekten örnek yapın (`<VAULT_PATH>` placeholder'ları),
`.env`'i `chmod 600`.

---

### L2 — LOW — `airl_id` 64-bit kesilmiş hash; çakışma yönetimi yok

`zotero.py:83` — `sha256(binding)[:16]` (64 bit). `database.py:19` `airl_id`
PRIMARY KEY. Çakışma olursa `sqlite3.IntegrityError` ile senkron ortasında
patlar, kısmi commit kalır. Doğum günü sınırı ~4 milyar kayıt olduğu için pratik
risk düşük, ama plan (WP-011) çakışmasız kimlik ve merge/tombstone kuralı
istiyor — bu ikisi de yok.

---

### L3 — LOW — Kategori klasör adları İngilizce/Türkçe karışık

`catalog.py:10-23` — `01 - Journal Articles`, `02 - Conference Papers`,
`03 - Reports and Preprints` (İngilizce) vs `04 - Kitaplar`, `05 - Kitap Bölümleri`,
`06 - Tezler`, `07 - Web Kaynakları`, `08 - Veri Setleri`, `09 - Patentler`,
`90 - Diğer Belgeler`, `99 - Diğer Kaynaklar` (Türkçe). Aynı sözlükte.
`README.md:110` bunlara "Turkish publication-type folders" diyor, ama görünen
üçü İngilizce. `implementation_log.md` Step 000-F "lowercase İngilizce standardı"
uygulandığını `PASS` olarak kaydediyor.

Şu an yalnız ilk üç tür kullanımda (33 kaynak: journalArticle/report/conferencePaper)
olduğu için görünmüyor; ilk kitap eklendiğinde vault'ta karışık dil belirecek.

---

### L4 — LOW — Güvenlik ve hata yollarının test kapsamı sıfır

`tests/test_api.py` yalnız `GET` çağırıyor (`_get` helper'ı, satır 10).
Test edilmeyen yollar:
- Üç `POST` endpoint'inin hiçbiri
- `ZoteroUnavailable` → 503 handler (`main.py:52`)
- `ProjectionError` → 422 handler (`main.py:56`)
- `Settings.from_env` loopback reddi (`config.py:47`)
- `AIRL_OBSIDIAN_GENERATED_DIR` traversal reddi (`config.py:58`)
- `library_type` doğrulaması (`config.py:63`)

Yani **savunma mekanizmalarının tamamı test edilmemiş**. Bu, planın
`05_DoD`'sindeki "Security/data/policy negative testleri geçmiştir" şartıyla
doğrudan çelişiyor.

---

### L5 — LOW — Kök dizinde sahte `.git`, boş `.codex`, boş `.agents`

Bunlar araçları yanıltıyor (bu oturum "git repository: true" ile başladı, ama
kökte repo yok). Temizleyin veya gerçek repo yapın.

---

## E. Plan kalitesi denetimi (nicel)

Plan iyi. Ama "130 detaylı iş paketi" ifadesi olduğundan daha fazlasını ima ediyor.
Ölçtüm:

| Metrik | Değer |
|---|---|
| WP dosyası | 130, toplam 87.971 kelime, 9.653 boş olmayan satır |
| **130 dosyanın ≥120'sinde aynen tekrar eden satır** | **5.718 / 9.653 = %59,2** |
| Tam olarak tek bir WP'ye özgü satır | 3.318 = %34,4 → **WP başına ~25 özgün satır** |
| ACC dosyası | 40, 2.870 satır |
| 40 dosyanın ≥36'sında tekrar eden satır | 1.400 = **%48,8** |
| ACC başına özgün satır | ~32 |

**Yorum:** Her WP'nin `Test ve doğrulama planı`, `Kabul kriterleri`,
`Kabul kanıtı paketi`, `Riskler`, `Rollback`, `Handoff` bölümleri **birebir aynı
şablon**. "Uygulama görevleri" tablosunda 130 paketin tamamında `Tamamlanma kanıtı`
sütunu `Commit/konfigürasyon/kayıt referansı` yazıyor — yani **ölçülebilir bir
kabul kriteri değil**.

Bu şablonun bir değeri var (tutarlılık, unutulan boyut yok). Ama:
- `05_DoD` "Acceptance kriterleri **ölçülebilir**" diyor; şablon kriterler
  ölçülebilir değil ("Bütün zorunlu testler geçmiştir" gibi).
- Gerçek spesifikasyon içeriği **paket başına ~25 satır** — bu, uygulama için
  yetersiz. Örneğin WP-011'in tüm teknik içeriği 5 satırlık bir tablo
  (`UUIDv7/opaque ID formatlarını ata` vb.).

**Öneri:** Şablonu koruyun, ama uygulamaya alınan her paket için bir
`refinement` adımı zorunlu olsun: paket-özel, ölçülebilir kabul kriterleri
(sayı, eşik, komut) yazılmadan paket `READY` sayılmasın. Şablon kriterler
"minimum", refinement kriterleri "gerçek kapı" olsun.

**Planın güçlü yanları (nicel):** 130/130 dosya mevcut, CSV ile birebir örtüşüyor,
bağımlılık grafiği **döngüsüz ve topolojik sıralı** (ileri bağımlılık: 0),
1011 iç link **0 kırık**, 184 dosya hash doğrulaması **OK**. Bu düzey bütünlük
nadirdir.

---

## F. Contract ve veri akışı denetimi

| Sözleşme | Planlanan (WP) | Mevcut | Durum |
|---|---|---|---|
| Kimlik / korelasyon | WP-011 | `Identity` sınıfı (170 satır), üretimde kullanılmıyor | PARTIAL — H4 |
| Canonical field authority | WP-012 | Yok; planın kendisi 4 kopyada — M4 | DOCUMENTED_ONLY |
| Project/task/role | WP-013 | Yok | DOCUMENTED_ONLY |
| Artifact manifest | WP-014 | `ArtifactManifest` sınıfı; `content_hash` formatı çelişiyor | PARTIAL — H4 |
| Event envelope | WP-015 | `EventEnvelope` sınıfı; **hiç event üretilmiyor**, bus yok | PARTIAL — H4 |
| Policy/control/exception | WP-016 | Yok (`policy/` boş) | MISSING |
| Source/literature | WP-017 | `SourceRecord` (pydantic); representation/status/trust yok | PARTIAL |
| Claim/evidence/review/decision | WP-018 | Yok | DOCUMENTED_ONLY |
| Run/environment/repro | WP-019 | `sync_runs` tablosu (ingest sayaçları); manifest yok | PARTIAL (çok zayıf) |
| Schema registry + SDK | WP-020 | In-process `dict`; JSON Schema yok, valide etmiyor, CI yok | PARTIAL → pratikte MISSING |

**Producer/consumer uyumsuzlukları:**
1. `content_hash` formatı: `"sha256:<hex>"` (üretim) vs `^[0-9a-f]{64}$` (contract) — **aktif çelişki**.
2. `airl_id` üretimi contract doğrulamasından geçmiyor.
3. Obsidian frontmatter'ı (`obsidian.py:292-308`) ayrı bir *de facto* şema —
   `airl_id`, `type`, `status`, `source_category`, `content_hash`, `provenance` —
   hiçbir registry'de kayıtlı değil, sürümlenmiyor. Vault dosyaları bugün
   `schema_version` taşımıyor; ileride migration edilemez.
4. `.airl-projection-manifest.json` `schema_version: 1` taşıyor ama registry'de yok.
5. SQLite `schema_meta.schema_version = "1"` yazılıyor (`database.py:73`) ama
   **hiç okunmuyor** — migration mekanizması yok. `data/projection-backups/
   Sources-before-title-migration-20260821/` klasörü, bir migration'ın elle
   yapıldığını gösteriyor.

---

## G. Güvenlik ve güven sınırı denetimi

| Boyut | Hedef (plan) | Mevcut | Değerlendirme |
|---|---|---|---|
| Trust zones (Zone 0-3) | WP-051 | Yok; tek process, tek kullanıcı | DOCUMENTED_ONLY |
| Network egress | WP-057 | Bridge yalnız loopback (config.py:47) — **iyi** | V0 için yeterli |
| API authn/authz | WP-055/056 | **Yok** — M1 | Açık |
| CSRF / Host doğrulaması | — | **Yok** — M1 | Açık |
| Secret yönetimi | WP-055 | `.env` 0644, secret yok ama hazırlık zayıf — L1 | Zayıf |
| Sandbox | WP-054 | systemd hardening (gerçek ve iyi) | V0 için yeterli |
| Content quarantine / prompt injection | WP-058 | `html.escape` var (test edilmiş); PDF/abstract Hermes'e ham gidiyor | Kısmi |
| Policy enforcement | WP-056 | Yok (`policy/` boş) | Yok |
| Supply-chain admission | WP-059 | Yok; `uv.lock` var (iyi), imza/SBOM yok | Yok |
| Least privilege | — | Zotero read-only **iddia** ediliyor, test edilmiyor — H3 | Doğrulanmamış |
| Auditability | WP-099 | `sync_runs` tablosu (ingest sayaçları); event/audit log yok | Çok zayıf |
| Rollback | — | `data/projection-backups/` 3 yedek + git | V0 için makul |

**Prompt injection notu:** Hermes MCP `get_source`, Zotero abstract'ını
ham metin olarak modele veriyor (`mcp_server.py:98`). Kötü niyetli bir PDF'ten
gelen abstract, talimat enjekte edebilir. ACC-05 tam olarak bu senaryo ve
`DOCUMENTED_ONLY`. V0'da tool'lar read-only olduğu için blast radius düşük —
ama Hermes'in *diğer* tool'ları (dosya yazma vb.) varsa yükselir.
**Aksiyon:** MCP çıktısında dış içeriği açık bir sınırla işaretleyin
(`<untrusted-source-content>` gibi) — ucuz, etkili.

---

## H. Literatür / Zotero / Obsidian denetimi

**Akış doğrulandı:** `Zotero(23119) → Bridge(8765) → SQLite → Obsidian → Hermes MCP`.
Canlı: `/ready` → `{"status":"ready","zotero":"reachable","source_count":33}`.
DB: 33 kaynak (25 journalArticle, 6 report, 2 conferencePaper), 25 sync run,
son 8 run `SUCCEEDED` / 33 unchanged.

| Kontrol | Sonuç |
|---|---|
| Kaynak kimliği kararlı mı? | ✅ Evet, test edilmiş |
| İdempotent mi? | ✅ Evet, test edilmiş |
| Başlıkla adlandırma + çakışma eki | ✅ Evet, test edilmiş (`test_obsidian.py:41`) |
| İnsan notları korunuyor mu? | ✅ Evet, manifest-sahipli silme, test edilmiş |
| Zotero'ya yazma var mı? | ✅ Kodda yok (elle doğrulandı) — ❌ ama testle kanıtlanmıyor (H3) |
| Baseline ↔ gerçek vault senkron mu? | ✅ `diff -rq` → yalnız `.obsidian/` config ve boş `2026_08_21.md` farkı |
| Wikilink bütünlüğü | ✅ 103 link, 0 kırık |
| Plan aynası link bütünlüğü | ✅ 1011 link, 0 kırık |
| Duplicate raporlama, otomatik merge yok | ✅ Doğru (`catalog.py:36`, yalnız rapor) |
| Tam kapsam senkron | ❌ 100 tavanı — H1 |
| Silme/reconciliation | ❌ Yok — H2 |
| Annotation/attachment ingest | ❌ Yok (`zotero.py:14` atlanıyor) — WP-068 MISSING |
| Koleksiyon/tag opt-in yetki sınırı | ❌ Yok, `users/0` tamamı okunuyor — WP-064 CONTRADICTED |
| Literature set manifest freeze | ❌ Yok — WP-072 MISSING |
| Vault notlarında `schema_version` | ❌ Yok — migration edilemez |
| Duplicate not adı | ⚠️ `README.md` ×2, `readme.md` ×2 (Obsidian kısa-yol linkleri belirsizleşebilir) |

**Not:** `data/projection-backups/` içinde 3 geri alma yedeği var
(`Sources-before-title-migration`, `vault-layout-before-silbo-main`,
`vault-layout-before-ai-framework-consolidation`). Bunlar `.gitignore`'da —
yani **geri alma yedekleri versiyon kontrolünde değil ve yedeklenmiyor**.
`OPERATIONS.md` bunları resmi rollback noktası olarak gösteriyor. Riskli.

---

## I. Kanıt ve tekrar üretilebilirlik denetimi

Her "başarılı" iddiasını tekrar üretilebilirliğine göre ayırdım:

| İddia | Kanıt tipi | Tekrar üretilebilir? |
|---|---|---|
| "20/20 test PASS" | `pytest -q` | ✅ Evet — bu oturumda tekrar üretildi |
| "33 kaynak, 3 kategori" | canlı `/ready` + SQLite | ⚠️ Yalnız bu makinede, bu kütüphaneyle |
| "Bridge + timer aktif" | `systemctl --user is-active` | ✅ Evet — doğrulandı |
| "Plan bütünlüğü" | `sha256sum -c` 184/184 | ✅ Evet — tekrar üretildi |
| "Baseline = vault" | `diff -rq` | ✅ Evet — tekrar üretildi |
| "Zotero write kapalı" | sabit `False` | ❌ **Hayır — H3, kanıt değil** |
| "V0 acceptance: accepted" | `acceptance_v0.py` | ❌ **Hayır — M3, kişisel veriye bağımlı, canlı servis gerekli** |
| "MCP 5 read-only tool" | `mcp_smoke.py` | ❌ **Hayır — M2, hiçbir şey assert etmiyor** |
| "Step 001 TECH_COMPLETE (WP-011/014/015/020/022)" | implementation_log | ❌ **WP-022 için yanlış — C3** |
| SILBO FIX-004/005a `ACCEPTED` | ayrı repo, sealed review + quorum | 🔍 **Bu review'un kapsamı dışı** — ayrı repository, ayrı yetki alanı |

**Sonuç:** Şu anda "kanıt" olarak gösterilen 3 artifact'in 3'ü de gerçek bir şey
kanıtlamıyor. Bunlar kötü niyetle yazılmamış — ama planın kendi
`05_DoD:52` maddesinin ("Yalnız happy-path demo") tam örneği.

**Not — SILBO ayrımı:** Status dokümanı ve implementation log'daki SILBO FIX-004/
FIX-005a/FIX-005 kayıtları ayrı bir repository'ye (`/home/otonom/silbo-fix-00*`)
ait ve bu inceleme kapsamında **doğrulanmadı**. Bu ayrımın dokümanlarda açıkça
yapılmış olması iyi. Ancak dikkat: framework durum tablosunun (`§1 Güncel durum
özeti`) 20 satırının 8'i SILBO satırı ve hepsi `ACCEPTED`/`PASS`. Framework'e
yüzeysel bakan biri, framework'ün kabul edilmiş olduğu izlenimine kapılır.
**Öneri:** SILBO satırlarını ayrı bir tabloya taşıyın.

---

## J. Risk register

| # | Risk | Etki | Olasılık | Tespit kanıtı | Azaltım | Kapanış ölçütü |
|---|---|---|---|---|---|---|
| R1 | Program hiç başlayamaz (evidence deadlock) | Critical | **Kesin** | C1 | WP-000 Interim Evidence Policy | WP-001 geçici kanıtla `ACCEPTED` olabiliyor |
| R2 | Kapsam organizasyona sığmıyor | Critical | **Kesin** | C2 | Kapsam kesme veya sealed-review verifier modeli | 00_PROGRAM'da yazılı karar |
| R3 | Beyan ile gerçek arasında fark (WP-022) | High | Gerçekleşti | C3 | Durumu düşür, CI ile beyanı doğrula | `git ls-files` teslimatları gösteriyor |
| R4 | 100+ kaynakta sessiz veri eksikliği | High | Yüksek (zaman meselesi) | H1 | Sayfalama + `since=` | Test: 250 kayıtlık mock kütüphane tam senkron |
| R5 | Silinen kaynak hayalet olarak kalır | High | Yüksek | H2 | `/deleted` + tombstone | Test: silinen kaynak `WITHDRAWN`, projeksiyondan çıkıyor |
| R6 | Read-only iddiası bir gün sessizce bozulur | High | Orta | H3 | Davranışsal test + statik kontrol | MockTransport testi CI'da |
| R7 | Contract çekirdeği ölü kod olarak çürür | High | Yüksek | H4 | En az bir üretim tüketicisi | `airl_bridge` `Identity` kullanıyor |
| R8 | Manuel kanıt üretimi tekrarlanamaz | High | Kesin | H5 | GitHub Actions | Her push'ta yeşil pipeline |
| R9 | Yerel API kötüye kullanımı (CSRF/rebinding) | Medium | Düşük | M1 | TrustedHost + token | Test: token'sız POST 401 |
| R10 | Plan kopyaları ayrışır | Medium | Gerçekleşti | M4 | Tek kanonik + üretilen ayna + CI drift kontrolü | `check_plan_drift.py` yeşil |
| R11 | Projeksiyon yanlış klasörü yönetime alır | Medium | Düşük | M7 | dry-run + boş-dizin reddi | Test: dolu insan klasörü reddediliyor |
| R12 | 10k üstü kütüphanede aktif veri kaybı | Medium | Düşük (H1 sonrası artar) | M9 | Sayfalayan iterator | H1 ile birlikte kapanır |
| R13 | Rollback yedekleri versiyon kontrolsüz | Medium | Orta | H bölümü | Yedekleri hash'leyip manifest'e bağlayın | Yedek manifesti + doğrulama komutu |
| R14 | Dokümantasyon drift'i güveni aşındırır | Medium | Gerçekleşti | M10 | `check_docs.py` | CI'da yol doğrulaması |
| R15 | Prompt injection (Zotero abstract → MCP) | Medium | Düşük (V0'da) | G bölümü | Untrusted-content işaretleme | MCP çıktısında sınır etiketi |

---

## K. `CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md`'nin denetimi

Kullanıcı bu prompta güvenmediğini söyledi. Haklıydı. Bulgular:

**K1 — Var olmayan dizinleri inceleme kapsamına alıyor (satır 69, 71, 73):**
- `planning/commissioning/09_OPERATIONS/` → gerçekte `09_EXPERIENCE_OBSERVABILITY/`
- `planning/commissioning/11_DECOMMISSION/` → gerçekte `11_DAY2_OPERATIONS/`
- `planning/commissioning/13_CHANGE_CONTROL/` → **hiç yok**

Yani prompt, planın gerçek yapısı okunmadan yazılmış. Bir reviewer bu listeyi
harfiyen izlerse üç bölümü "MISSING" raporlar ve iki gerçek bölümü hiç incelemez.

**K2 — Boş dizinleri inceleme hedefi olarak listeliyor (satır 119-125):**
`services/`, `workflows/`, `agents/`, `infra/`, `policy/` — hepsi boş ve git'te yok
(C3). Prompt, olması *istenen* yapıya göre yazılmış, olan yapıya göre değil.

**K3 — Rapor formatı bulguları gömüyor (satır 262-272):**
130 satırlık WP matrisi + 40 satırlık ACC matrisi istiyor. Bu matrisin ~160
satırı aynı şeyi söyleyecek (`DOCUMENTED_ONLY`, kanıt: "dosya var, kod yok").
Gerçek 10-15 bulgu bu tablonun içinde kaybolur. **Rapor formatı titizlik
gösteriyor, aksiyon üretmiyor.**

**K4 — Çalıştırılması istenen komut hatalı (satır 205):**
`python -m unittest discover -s airl_bridge_api/tests -q` — repo kökünden
çalışmaz; `pythonpath=["src"]` yalnız pytest konfigürasyonunda tanımlı
(`pyproject.toml:32`). `unittest` `ModuleNotFoundError` verir.

**K5 — Sorulmayan asıl soru:**
Prompt "ne kadarı kuruldu?" diye 6 kez soruyor ama şunu hiç sormuyor:
**"Bu plan bu organizasyon tarafından yürütülebilir mi?"** — C1 ve C2, promptun
körlüğünde kalan ve aslında en pahalı olan iki bulgu.

**K6 — İyi yanları (korunmalı):** Kanıt sınıflandırması (`IMPLEMENTED`/`PARTIAL`/
`DOCUMENTED_ONLY`/`CONTRADICTED`/`BLOCKED`), "dosya varlığı kanıt değildir" kuralı,
"SILBO'yu framework ile karıştırma" kuralı ve salt-okunur kısıtı — bunlar doğru
ve bu raporda uygulandı.

**Öneri:** Promptu düzeltin (K1, K2, K4) ve rapor formatını değiştirin:
130 satırlık matris yerine **"durumu `DOCUMENTED_ONLY` olmayan paketler"** tablosu
+ bir özet dağılım. Geri kalanı zaten varsayılan.

---

## L. Gerçekçi uygulama sırası

Her adım `implementable` (kod/config değişir) veya `document-only` (karar/metin)
olarak işaretli. Sıra bağımlılığa göre; **atlanamaz**.

---

### Step 0 — Kapsam kararı `document-only` 🔴 BLOKE EDİCİ

**Amaç:** C2'yi çözmek. 130 paket / 73 owner / 114 verifier modeli bu organizasyon
için geçersiz; hangi modelle devam edileceği yazılı olmadan kod yazmak boşa emek.
**Ön koşul:** Yok. **Bu ilk iş.**
**Değişecek:** `00_PROGRAM/` altına yeni `12_ORGANIZASYON_VE_BAGIMSIZLIK_MODELI.md`;
`04_ROL_VE_SORUMLULUK_MATRISI.md` revizyonu.
**İçerik:** (a) kapsam: hangi WP'ler `IN_SCOPE` / `DEFERRED`; (b) bağımsızlık:
SILBO sealed-review + exact-quorum protokolünün framework verifier'ı olarak
resmileştirilmesi (farklı model ailesi, sealed context, exact target SHA).
**Kanıt:** Doküman + `ai_research_framework_current_status_and_roadmap.md`
değişiklik günlüğü satırı.
**Rollback:** Doküman geri alınır. **Tamamlanma:** WP kataloğundaki her paketin
`IN_SCOPE`/`DEFERRED` etiketi var ve verifier tanımı yazılı.

---

### Step 1 — Interim Evidence Policy (WP-000) `document-only` 🔴 BLOKE EDİCİ

**Amaç:** C1'i çözmek. WP-026 gelene kadar geçerli kanıt deposu tanımı.
**Ön koşul:** Step 0.
**Değişecek:** `00_PROGRAM/WP-000_interim_evidence_policy.md`;
`05_DEFINITION_OF_READY_DONE.md`'ye "geçici kanıt" maddesi;
`delivery/EVIDENCE_LEDGER.md` (append-only) oluşturulur.
**Format:** `delivery/WP-xxx/evidence-manifest.json` →
`{target_git_sha, command, exit_code, artifacts:[{path, sha256}], produced_at, producer, verifier}`.
**Kanıt:** Politika dokümanı + ilk manifest örneği.
**Rollback:** Doküman geri alınır. **Tamamlanma:** Bir paket bu politikayla
`ACCEPTED` olabiliyor (Step 3'te test edilir).

---

### Step 2 — CI temeli `implementable` (H5, ve 4 bulguyu birden kapatır)

**Amaç:** Kanıt üretimini otomatikleştirmek.
**Ön koşul:** Step 1 (kanıt formatı belli olmalı).
**Değişecek:** `.github/workflows/ci.yml`, `pyproject.toml` (`[tool.ruff]`),
`scripts/check_readonly_boundary.py`, `scripts/check_plan_integrity.py`.
**İçerik:** `uv sync --extra dev` → `ruff check` → `pytest -q` →
Zotero write statik kontrolü (H3) → `sha256sum -c SHA256SUMS` (M4/M11).
**Kanıt:** Yeşil workflow run URL'i + `evidence-manifest.json`.
**Rollback:** Workflow dosyasını silmek. **Tamamlanma:** Her push'ta 5 kontrol yeşil.

---

### Step 3 — Read-only sınırının gerçek testi `implementable` (H3)

**Amaç:** Framework'ün en güçlü güvenlik iddiasını gerçekten kanıtlamak. **Bu aynı
zamanda Step 1'in pilotu**: ilk `evidence-manifest.json` bu adımda üretilir.
**Ön koşul:** Step 2.
**Değişecek:** `tests/test_readonly_boundary.py` (yeni);
`src/airl_bridge/models.py:65` ve `main.py:62` (sahte alanı kaldır);
`scripts/acceptance_v0.py:41,77` (totolojik kontrolü çıkar).
**Test:** `MockTransport` handler'ı `request.method != "GET"` ise `AssertionError`
fırlatsın; tüm `sync()` akışı bu transport ile koşsun.
**Kanıt:** Test çıktısı + manifest. **Rollback:** Commit revert.
**Tamamlanma:** Testi kırmak için `zotero.py`'a bir `POST` eklemek gerekiyor
(ve eklendiğinde CI kırmızı oluyor — bir kez deneyip geri alın, bu da kanıt).

---

### Step 4 — Sayfalayan iterator (M9) `implementable` — **H1'den ÖNCE**

**Amaç:** 10.000 sessiz kesmesini kaldırmak. H1'den önce yapılmalı, aksi halde
H1 düzeltmesi aktif veri kaybı yolu açar.
**Ön koşul:** Step 2.
**Değişecek:** `database.py` (`iter_sources()`), `service.py:42`, `main.py:114`.
**Kanıt:** 15.000 satırlık fixture ile projeksiyon testi (tümü projekte ediliyor,
`removed_stale == 0`). **Rollback:** Commit revert.
**Tamamlanma:** Kodda `limit=10_000` kalmadı.

---

### Step 5 — Zotero sayfalama + incremental sync (H1) `implementable`

**Ön koşul:** Step 4.
**Değişecek:** `zotero.py` (`start` döngüsü, `Total-Results` okuması,
`since=` desteği), `database.py` (`sync_runs.library_version`), `service.py`,
`cli.py:68` (limit choices kaldır), `main.py:126,136`,
`deploy/airl-bridge-sync.service`.
**Kanıt:** 250 kayıtlık mock kütüphane → 250 fetched; `fetched < total` durumunda
run `PARTIAL`. **Rollback:** Commit revert + `library_version` migration geri alma.
**Tamamlanma:** Gerçek kütüphanede `source_count == Zotero Total-Results`.

---

### Step 6 — Silme reconciliation + tombstone (H2) `implementable`

**Ön koşul:** Step 5 (`since=` altyapısı).
**Değişecek:** `zotero.py` (`/deleted?since=`), `database.py`
(`sources.status`, `withdrawn_at`, migration + `schema_version` **okuması**),
`service.py`, `obsidian.py` (WITHDRAWN'ı projekte etme).
**Kanıt:** Test: kaynak silindi → `status=WITHDRAWN`, Obsidian dosyası kalktı,
DB satırı korundu. **Rollback:** Migration geri alma scripti (önceden yazılacak).
**Tamamlanma:** WP-067'nin V0 karşılığı çalışıyor.

---

### Step 7 — API sertleştirme (M1) `implementable`

**Ön koşul:** Step 2.
**Değişecek:** `main.py` (`TrustedHostMiddleware`, token dependency),
`config.py` (`AIRL_API_TOKEN`), `.env` (chmod 600), `.env.example` (placeholder),
`deploy/airl-bridge-sync.service` (header), `docs/OPERATIONS.md`.
**Kanıt:** Test: token'sız POST → 401; yanlış Host → 400.
**Rollback:** Middleware'i kaldır. **Tamamlanma:** L1 ve M1 kapalı.

---

### Step 8 — Sync transaction/compensation + audit (M6) `implementable`

**Ön koşul:** Step 6.
**Değişecek:** `database.py` (`sync_runs`'a projeksiyon sütunları),
`service.py:45`, `models.py`.
**Kanıt:** Test: projeksiyon hatası → run `PARTIAL`, hata kaydedilmiş, registry
tutarlı. **Tamamlanma:** WP-038'in V0 karşılığı.

---

### Step 9 — Plan tek kanonik kopyaya indirgeme (M4, M11) `implementable`

**Ön koşul:** Step 2 (CI drift kontrolü için).
**Değişecek:** `planning/commissioning/` kaldırılır (veya symlink);
`scripts/mirror_plan.py` (kanonik → vault üretimi); `scripts/check_plan_drift.py`;
`SHA256SUMS` kanonik kopyanın yanına; cockpit + status + review prompt güncellenir.
**Kanıt:** CI'da drift kontrolü yeşil; `sha256sum -c` OK.
**Rollback:** Silme yerine `90 - Archive`'a taşıyın, sonra geri.
**Tamamlanma:** Plan tek yerde, üretilmiş ayna, CI doğrulamalı.

---

### Step 10 — Contract çekirdeğini bağla (H4) `implementable`

**Ön koşul:** Step 3, Step 9.
**Değişecek:** `zotero.py:104` (`content_hash` formatı → çıplak hex + `hash_algo`),
migration scripti, `zotero.py:83` (`Identity` üzerinden `airl_id`),
`schemas/*.json` (gerçek JSON Schema), `contracts.py` (`jsonschema` ile valide et),
CI'da şema uyumluluk kontrolü.
**Kanıt:** `grep airl_framework src/airl_bridge/` en az 2 sonuç; şema testi;
migration dry-run + geri alma denemesi.
**Tamamlanma:** WP-011/014/020 gerçekten `TECH_COMPLETE` — ve Step 0'daki verifier
modeliyle `ACCEPTED` olabilir.

---

### Step 11 — Beyanları gerçeğe çek `document-only`

**Ön koşul:** Step 10.
**Değişecek:** `implementation_log.md` (WP-022 → `NOT_STARTED`, C3 açıklaması),
`ai_research_framework_current_status_and_roadmap.md` (test sayısı 20; SILBO
satırlarını ayrı tabloya al), `docs/ARCHITECTURE_V0.md` (M10 yol düzeltmeleri),
`deploy/*.service|timer` (SILBO adlandırması), `README.md:110` (L3),
`docs/review/CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md` (K1, K2, K4).
**Kanıt:** `scripts/check_docs.py` yeşil. **Tamamlanma:** Dokümanda doğrulanamayan
tek bir yol/sayı kalmadı.

---

### Step 12 — İlk gerçek ACC senaryosu `implementable`

**Amaç:** 40 ACC'den birini gerçekten otomatikleştirmek. Aday: **ACC-22
(obsidian_human_edit)** — mevcut `test_obsidian.py:72` zaten yarısını yapıyor,
ve tam olarak sizin en kritik veri kaybı riskinizi kapatıyor.
**Ön koşul:** Step 1 (kanıt formatı), Step 2 (CI).
**Değişecek:** `tests/acceptance/test_acc_22.py`,
`delivery/ACC-22/evidence-manifest.json`, ACC-22 dosyasına "mevcut otomasyon" satırı.
**Kanıt:** CI'da geçen ACC testi + imzalı manifest.
**Tamamlanma:** 40 ACC'den 1'i `IMPLEMENTED`. Bu, programın gerçekten
başlayabildiğinin ilk kanıtı olur.

---

**Step 12'den sonra:** Faz C (WP-013/016/017 contract'ları), sonra WP-061-074
literatür platformu. Ama önce Step 0 ve Step 1 — onlar olmadan geri kalanı
"kabul edilemez kod" üretmeye devam eder.

---

## M. Final verdict — 6 soruya doğrudan cevap

**1. Framework'ün ne kadarı gerçekten kurulmuş?**
Kabaca **%2-3**'ü. Ölçüt: 130 WP'nin 0'ı `ACCEPTED`, 9'u `PARTIAL`. Çalışan kod
1.509 satır. Kurulan şey tek bir dikey dilim: read-only literatür köprüsü.
Kurulmayan şey: control plane, event backbone, execution fabric, evidence ledger,
observability, security platform — yani mimarinin 6 düzleminden 5'i.

**2. Hangi kısımlar yalnızca planlanmış?**
119/130 WP ve 40/40 ACC. Somut olarak: Temporal, NATS, PostgreSQL, MLflow,
Kubernetes, gVisor, SPIFFE/Vault, OPA, LiteLLM, LangGraph, Neo4j/pgvector,
Langfuse, Grafana, cost ledger, clean-room reproduction, claim/evidence ledger,
blind review, publication package. **Hiçbiri için tek satır kod yok.**

**3. En kritik üç engel?**
(a) **C1** — kanıt zinciri bootstrap deadlock'u: WP-001 bile kabul edilemez.
(b) **C2** — 73 owner/114 verifier varsayımı vs 1 kişilik organizasyon.
(c) **H3+M2+M3** — kanıt üretim mekanizmasının kendisi bozuk; "yeşil" gördüğünüz
üç artifact hiçbir şey doğrulamıyor. Bu üçü çözülmeden her ilerleme sahte
ilerleme olur.

**4. Şu an güvenle çalıştırılabilecek gerçek dikey dilim?**
Literature Bridge V0: `Zotero (read-only) → SQLite → Obsidian → Hermes MCP`.
33 kaynak ölçeğinde güvenli, idempotent, insan notlarını koruyor, yerel.
**Sınır: kütüphane 100 kaynağı geçtiği an sessizce eksik senkron eder (H1).**
Bunu bugün not edin; büyüdüğünüzde fark edilmesi çok zor.

**5. Bir sonraki uygulama adımı tam olarak nedir?**
Kod değil. **Step 0**: `00_PROGRAM/12_ORGANIZASYON_VE_BAGIMSIZLIK_MODELI.md`
yazın — hangi WP'ler `IN_SCOPE`, ve tek kişilik organizasyonda "bağımsız verifier"
ne demek. Hemen ardından **Step 1**: `WP-000_interim_evidence_policy.md`.
Bu ikisi olmadan yazacağınız kod, planın kendi kurallarına göre kabul edilemez.

**6. Hangi kanıtlar eksik olduğu için "tamamlandı" denemez?**
- Zotero read-only sınırının **davranışsal** testi (H3)
- Assert eden bir MCP doğrulaması (M2)
- Veriden bağımsız, tekrar üretilebilir acceptance (M3)
- Tekrarlanabilir, otomatik test çalıştırma kanıtı — CI (H5)
- Üretici-bağımsız verifier kararı (C2) — hiçbir paket için yok
- İmzalı EvidenceManifest ve immutable store (C1) — mekanizma yok
- Rollback/compensation denemesi (DoD zorunlu) — hiçbir paket için yapılmamış
- Negative security testleri (L4) — savunma yollarının hiçbiri test edilmemiş
- WP-022 teslimatı (C3) — repoda yok

---

## N. Kanıt eki

### Çalıştırılan komutlar ve sonuçlar

> **Not:** Bu komutlar denetim anındaki dizin yapısına göre çalıştırıldı
> (`airl_bridge_api/` alt dizini). Denetimden sonra repo kökü
> `AI_RESEARCH_FRAMEWORK/` seviyesine düzleştirildi; yollar buna göre okunmalıdır.

| Komut | Exit | Sonuç |
|---|---:|---|
| `.venv/bin/python -m pytest -q` | 0 | **20 passed**, 1 warning (pydantic_settings forward-ref) |
| `curl -s http://127.0.0.1:8765/health` | 0 | `{"status":"ok","version":"0.1.0",...,"zotero_write_enabled":false}` |
| `curl -s http://127.0.0.1:8765/ready` | 0 | `{"status":"ready","zotero":"reachable","obsidian_vault":true,"source_count":33}` |
| `systemctl --user is-active airl-bridge.service airl-bridge-sync.timer` | 0 | `active` / `active`; son sync 8 dk önce |
| `sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt` | 0 | **184/184 OK**, 0 FAILED |
| `sqlite3 data/airl_bridge.sqlite3` (Python) | 0 | 33 sources, 25 sync_runs, son 8'i `SUCCEEDED` |
| `git -C airl_bridge_api log --oneline` | 0 | 21 commit, HEAD `6c849bd`, `origin/main` ile 0/0 |
| `git -C airl_bridge_api ls-files \| grep -E '^(services\|workflows\|agents\|infra\|policy\|delivery)/'` | 1 | **Çıktı yok** → C3 |
| `diff -rq vault_baseline "$VAULT"` | 1 | Yalnız `.obsidian/` config + boş `2026_08_21.md` + `Zotero Sources/` |
| `diff -rq planning/commissioning planning/commissioning` | 1 | **12 dosya farklı** → M4 |
| `diff .env .env.example` | 0 | **Bayt-bayt aynı** → L1 |
| `diff deploy/*.service ~/.config/systemd/user/*.service` | 1 | Yalnız trailing newline — **gerçek drift değil** |
| Wikilink tarayıcı (Python) | 0 | 246 not, 103 wikilink, **0 kırık**, 2 duplicate basename |
| Markdown link tarayıcı (Python) | 0 | Her üç plan kopyasında 1011 link, **0 kırık** |
| Plan tutarlılık analizi (Python) | 0 | 130/130 WP dosya+CSV eşleşiyor, **döngü yok**, ileri bağımlılık **0** |
| Boilerplate analizi (Python) | 0 | WP'lerde **%59,2** tekrar; ACC'lerde **%48,8** |
| WP↔ACC çapraz kontrol (Python) | 0 | **39/40 tutarsız**; 62/130 WP hiç ACC referansı almıyor |
| Rol analizi (CSV) | 0 | **73 owner**, **114 verifier**, efor: 83 L / 42 M / 5 S |
| `ls .github Makefile ruff.toml mypy.ini .pre-commit-config.yaml` | 2 | **Hiçbiri yok** → H5 |
| `gh api repos/furkanhanilci/AI-Research-Framework` | 0 | `private=true`, `default_branch=main`, `pushed_at=2026-08-21T20:21:35Z` |

### Taranan hacim

| Alan | Sayı |
|---|---:|
| Plan dosyası (kanonik ağaç) | 186 (184 md + 1 csv + 1 txt) |
| Plan kelime sayısı (yalnız WP'ler) | 87.971 |
| Python kaynak satırı (`src/`) | 1.509 |
| Test satırı (`tests/`) | 381 |
| Test sayısı | 20 (16 pytest + 4 unittest tarzı) |
| API endpoint | 10 (7 GET, 3 POST) |
| MCP tool | 5 (hepsi read-only) |
| Obsidian notu (gerçek vault) | 246 |
| Vault baseline dosyası | 211 |
| Git takipli dosya | 434 |
| Zotero kaynağı | 33 |

### Doğrulanamayan alanlar (BLOCKED)

| Alan | Neden |
|---|---|
| SILBO FIX-004 / FIX-005a / FIX-005 kabul zinciri | Ayrı repository (`/home/otonom/silbo-fix-00*`), bu review'un kapsamı dışı; iddialar doğrulanmadı |
| Hermes `tools.include` beş-araç kısıtı | Hermes konfigürasyon dosyası repo dışında; `README.md:130` ve `OPERATIONS.md` iddiası doğrulanmadı |
| GitHub branch protection / required checks | `gh api` ile repo metadata alındı, koruma kuralları sorgulanmadı (salt-okunur sınır) |
| `acceptance_v0.py` çalıştırma | Canlı servise POST/GET yapıyor ve kişisel veriye bağımlı; okunup değerlendirildi, çalıştırılmadı |
| Zotero Local API'nin gerçek toplam kayıt sayısı | Doğrudan Zotero sorgulanmadı; `source_count=33` Bridge üzerinden alındı |

---

## Kapanış notu

Sert olmam istendi, oldum. Ama tespit edilmesi gereken şey şu: **buradaki asıl
problem yetersiz çalışma değil.** Kod kalitesi, atomik yazım, manifest-sahipli
silme, systemd hardening, plan bütünlüğü — bunlar iyi mühendislik.

Problem, **planın ölçeğiyle organizasyonun ölçeği arasındaki uçurum** ve bu
uçurumun kanıt üretim mekanizmasını sahteleştirmeye başlaması. `zotero_write_enabled
is False` testi, `mcp_smoke.py`'ın exit 0'ı ve WP-022'nin boş dizinleri — üçü de
aynı baskının belirtisi: 130 paketlik bir programda ilerliyor görünme ihtiyacı.

Step 0 ve Step 1, o baskıyı kaldırır. Kapsamı dürüstçe kesin, kanıt kuralını
uygulanabilir yapın; ondan sonra bu ekip (bir kişi) gerçekten `ACCEPTED`
paketler üretebilir. Şu anda üretemez — ve bu, planın kusuru, sizin değil.
