# Claude Full AI Research Framework Review Prompt

Bu belge, Claude’a verilecek kapsamlı inceleme talimatıdır. İnceleme yalnızca
Bridge/API katmanına değil, planlanan ve mevcut tüm AI Research Framework
sistemine uygulanmalıdır.

## Kullanım şekli

Claude’u aşağıdaki genel framework kökünde başlat:

```text
/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK
```

Komut istemine aşağıdaki promptun tamamını tek parça olarak ver. Claude yalnızca
inceleme yapmalı; kullanıcı ayrıca açıkça izin vermedikçe dosya değiştirmemeli,
commit oluşturmamalı, branch değiştirmemeli, push/merge yapmamalı, servis
yeniden başlatmamalı ve veri silmemelidir.

---

## Claude’a verilecek prompt

Sen, üretim seviyesinde araştırma altyapıları, veri sözleşmeleri, event-driven
sistemler, güvenlik, MLOps, kanıt/tekrarlanabilirlik ve Obsidian bilgi mimarisi
konularında kıdemli bağımsız bir sistem denetçisisin.

Bu görevin amacı, `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK` altında
tanımlanan AI Research Framework’ün planlarda tarif edilen hedef mimariyle
gerçekte mevcut olan uygulama arasında tam ve kanıta dayalı bir fark analizi
çıkarmaktır. İncelemeyi yalnızca Bridge bileşenine (`src/airl_bridge/`) veya Bridge
servisine indirgeme. Bridge mevcut sistemin yalnızca bir parçasıdır.

### 1. Değişmez inceleme ilkeleri

1. Dokümantasyon, niyet veya plan tek başına “uygulandı” kanıtı değildir.
2. Bir özellik ancak çalışan kod, yapılandırma, test, çalıştırma çıktısı veya
   doğrulanabilir operasyonel kanıtla destekleniyorsa IMPLEMENTED sayılabilir.
3. Tasarım dokümanı mevcut olup çalışan karşılığı yoksa DOCUMENTED_ONLY olarak
   işaretle.
4. Kısmen çalışan, yalnızca happy-path’i kapsayan veya kabul kriterlerinin bir
   bölümünü karşılayan maddeleri PARTIAL olarak işaretle.
5. Uygulama var ancak plan, sözleşme, güvenlik politikası veya testlerle
   çelişiyorsa CONTRADICTED olarak işaretle.
6. Dış bağımlılık, eksik yetki, eksik secret, çalışmayan servis veya yeniden
   üretilemeyen ortam nedeniyle doğrulanamayan maddeleri BLOCKED olarak belirt.
7. Tahmin ile kanıtı ayrı yaz. Her önemli iddianın dosya yolu, satır aralığı,
   komut veya test çıktısı ile izlenebilir olmasını sağla.
8. Çalıştıracağın komutlar salt-okunur veya güvenli doğrulama komutları olsun.
   Destructive komut, geniş kapsamlı silme, reset, checkout, force push,
   migration, training run veya veri değiştiren entegrasyon çağrısı çalıştırma.

### 2. İnceleme kökleri ve kapsam

Aşağıdaki alanların tamamını incele:

#### 2.1 Plan ve commissioning dokümanları

- `planning/commissioning/README.md`
- `planning/commissioning/00_PROGRAM/`
- `planning/commissioning/01_GOVERNANCE/`
- `planning/commissioning/02_CONTRACTS/`
- `planning/commissioning/03_FOUNDATION/`
- `planning/commissioning/04_CONTROL_EVENT/`
- `planning/commissioning/05_MODEL_AGENT_TOOL/`
- `planning/commissioning/06_EXECUTION_SECURITY/`
- `planning/commissioning/07_LITERATURE_KNOWLEDGE/`
- `planning/commissioning/08_EVIDENCE_ASSURANCE/`
- `planning/commissioning/09_OPERATIONS/`
- `planning/commissioning/10_INTEGRATION_CUTOVER/`
- `planning/commissioning/11_DECOMMISSION/`
- `planning/commissioning/12_ACCEPTANCE_SCENARIOS/`
- `planning/commissioning/13_CHANGE_CONTROL/`

Dosya adları Türkçe olsa bile içerikleri, bağımlılıkları, teslimatları ve kabul
kriterlerini okuyarak değerlendir. Özellikle şu belgelerden hedef durumu çıkar:

- plan kullanım kuralları
- hedef durum ve invariantlar
- paket kataloğu
- dalga/bağımlılık haritası
- rol ve sorumluluk matrisi
- Definition of Ready/Done
- kanıt ve kabul stratejisi
- risk register
- kapsam karşılık matrisi
- değişiklik ve konfigürasyon kontrolü

#### 2.2 Tüm work package’ler

`WP-001` ile `WP-130` arasındaki bütün paketleri tek tek tespit et. Paket
kataloğunda numarası bulunan fakat dosyası eksik olan paketleri ayrıca raporla.
Her WP için planlanan amaç, bağımlılıklar, teslimatlar, owner/implementer/
verifier, kabul kriterleri ve mevcut uygulama karşılığını karşılaştır.

#### 2.3 Tüm acceptance scenario’lar

`ACC-01` ile `ACC-40` arasındaki bütün acceptance scenario dosyalarını incele.
Her senaryo için:

- hedeflenen invariant veya risk,
- ön koşullar,
- test adımları,
- beklenen sonuç,
- mevcut otomasyon,
- son kanıt,
- tekrar çalıştırılabilirlik,
- mevcut durum

çıkar. Dosyası olmayan numaraları ve planla uyuşmayan senaryoları açıkça belirt.

#### 2.4 Çalışan repository ve servisler

En az aşağıdaki alanları incele:

- `src/`
- `tests/`
- `scripts/`
- `schemas/`
- `delivery/`
- `deploy/`
- `docs/`
- `pyproject.toml`
- `README.md`

Şunları doğrula:

- API endpoint’leri gerçekten çalışıyor mu?
- SQLite/Zotero/Obsidian/Hermes sınırları planla uyumlu mu?
- read-only iddiaları gerçekten read-only mu?
- kimlik, correlation ID, artifact manifest, event envelope ve schema registry
  sözleşmeleri kodla ve testlerle destekleniyor mu?
- hata yönetimi, idempotency, retry, timeout, DLQ/replay ve audit trail var mı?
- secret/config ayrımı ve güvenli varsayılanlar uygulanmış mı?
- testler yalnızca birim seviyesinde mi, yoksa contract/integration/acceptance
  seviyelerine de ulaşıyor mu?
- mevcut placeholder dosyalar gerçek teslimat mı, yoksa yalnızca iskelet mi?

#### 2.5 Obsidian ve bilgi sürekliliği

Hem repository içindeki vault baseline’ı hem de gerçek vault’u incele:

- `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK/vault_baseline/`
- `/home/otonom/Documents/Obsidian Vault/`

AI Research Framework proje alanında şunları kontrol et:

- navigation/execution cockpit
- implementation log
- current status and roadmap
- commissioning/readme
- plan ve WP bağlantıları
- dosya/klasör adlarının İngilizce ve tutarlı olması
- `Literature Sets` altında Zotero kaynaklarının doğru isimlendirilmesi ve
  sınıflandırılması
- bozuk wikilink, eksik note, yanlış klasör, duplicate veya stale içerik
- baseline ile gerçek vault’un senkron ve hash açısından tutarlı olup olmadığı
- her uygulama adımının “ne yapıldı, neden yapıldı, kanıt, sınırlama, sonraki
  adım” biçiminde kaydedilip kaydedilmediği

#### 2.6 Git, remote ve çalışma sınırları

Salt-okunur biçimde şunları kontrol et:

- repository root ve nested repository ayrımı
- aktif branch ve HEAD
- çalışma ağacının temiz/değişik olması
- son commit’ler
- remote URL’leri
- upstream/default branch
- son push ile local HEAD’in eşleşmesi
- yanlış repository’ye push riski
- SILBO repository’siyle framework repository’sinin ayrımı
- untracked, ignored ve generated dosyalar

Yetkili framework remote’u şudur:

`https://github.com/furkanhanilci/AI-Research-Framework.git`

Bu inceleme sırasında hiçbir remote’a push yapma.

### 3. Çalıştırılabilecek doğrulamalar

Mevcut ortam izin veriyorsa, önce keşif ve sonra düşük riskli doğrulama yap:

```bash
pwd
git status --short
git branch --show-current
git log -10 --oneline --decorate
git remote -v
find . -maxdepth 3 -type f | sort
rg --files planning/commissioning src skills docs
```

Python projesi için mevcut sanal ortamı kullanarak:

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m unittest discover -s tests -t . -q
```

Varsa mevcut acceptance, link-check, schema-check ve preflight script’lerini
önce okuyup sonra güvenli biçimde çalıştır. Script’in veri değiştirdiği,
servis başlattığı veya dış sisteme yazdığı anlaşılırsa çalıştırma; bunun yerine
BLOCKED gerekçesi yaz.

Obsidian için en azından:

- tüm Markdown dosyalarını say,
- wikilink hedeflerini çıkar,
- eksik hedefleri raporla,
- duplicate başlık/isimleri bul,
- baseline ve gerçek vault dosya listelerini karşılaştır,
- mümkünse SHA256 karşılaştırması yap.

### 4. Değerlendirme modeli

Her WP ve ACC için aşağıdaki sınıflardan tam olarak birini kullan:

- `IMPLEMENTED`: çalışan ve kanıtlanmış
- `PARTIAL`: bazı teslimatlar/kriterler mevcut
- `DOCUMENTED_ONLY`: plan veya doküman var, çalışan kanıt yok
- `MISSING`: planlanan dosya/özellik/teslimat bulunamadı
- `BLOCKED`: dış koşul veya eksik bağımlılık nedeniyle doğrulanamıyor
- `CONTRADICTED`: mevcut davranış plan, invariant veya güvenlik sınırıyla çelişiyor

Her sınıflandırmada şu kanıt formatını kullan:

```text
Durum: PARTIAL
Kanıt: src/...:satır, tests/...:satır, komut çıktısı
Karşılanan: ...
Eksik: ...
Risk: ...
Önerilen sonraki adım: ...
```

### 5. Rapor çıktısı

Raporu aşağıdaki sırayla üret:

#### A. Executive summary

- hedef mimarinin kısa özeti
- gerçek uygulamanın kısa özeti
- toplam WP sayısı ve her durumdaki dağılım
- toplam ACC sayısı ve her durumdaki dağılım
- kritik güvenlik/operasyon/kanıt bulguları
- “production-ready” veya “not production-ready” kararı ve gerekçesi

#### B. Repository ve environment snapshot

Tablo halinde path, branch, HEAD, remote, test ortamı, servis durumu ve
çalışma ağacı durumu.

#### C. WP-001–WP-130 matrisi

Her satırda:

`WP | başlık | planlanan teslimat | bağımlılıklar | mevcut dosya/kod | durum | kanıt | eksik | risk | önerilen adım`

#### D. ACC-01–ACC-40 matrisi

Her satırda:

`ACC | amaç | ön koşul | mevcut test | son kanıt | durum | tekrar üretilebilirlik | eksik`

#### E. Architecture conformance

Hedef G0–G10 yaşam döngüsünü ve Experience, Control, Event, Cognition,
Execution, Evidence/Operations düzlemlerini tek tek ele al. Her düzlem için
planlanan bileşen, mevcut bileşen, bağlantı, invariant ve açıkları göster.

#### F. Contract and data-flow audit

Kimlik, correlation, event envelope, schema compatibility, artifact/data
manifest, source/literature, project/task/role, claim/evidence, run/experiment
ve audit sözleşmelerini değerlendir. Producer/consumer uyumsuzluklarını ve
şema sürümleme risklerini belirt.

#### G. Security and trust-boundary audit

Trust zones, network egress, secret yönetimi, sandbox, content quarantine,
prompt-injection savunması, policy enforcement, supply-chain admission,
least-privilege, auditability ve rollback durumunu değerlendir.

#### H. Literature/Zotero/Obsidian audit

Zotero → Bridge → canonical storage → Literature Sets → Obsidian → Hermes
akışını doğrula. Kaynak kimliği, makale başlığıyla isimlendirme, klasörleme,
duplicate/reconciliation, read-only/writeback sınırı, provenance ve stale note
risklerini raporla.

#### I. Evidence and reproducibility audit

Her kritik iddianın kanıt zincirini; test, artifact, manifest, event, run,
reviewer, timestamp ve hash boyutlarıyla incele. Tekrar çalıştırılamayan veya
kanıtsız “başarılı” iddiaları ayır.

#### J. Risk register

Öncelik sırasıyla `Critical`, `High`, `Medium`, `Low` riskleri yaz. Her riskte
etki, olasılık, tespit kanıtı, owner önerisi, azaltım ve kapanış ölçütü olsun.

#### K. Gerçekçi uygulanma sırası

Eksikleri bağımlılıklarına göre sıralayarak 0’dan başlayan uygulanabilir bir
roadmap oluştur. Her adım için:

- amaç
- ön koşul
- değişecek dosyalar/servisler
- test ve acceptance kanıtı
- rollback planı
- Obsidian implementation-log güncellemesi
- tamamlanma ölçütü

Dokümantasyonla uygulamayı birbirine karıştırma; her adımı “implementable”
veya “document-only” olarak açıkça ayır.

#### L. Final verdict

Son bölümde şu soruları doğrudan yanıtla:

1. Framework’ün ne kadarı gerçekten kurulmuş?
2. Hangi kısımlar yalnızca planlanmış?
3. En kritik üç engel nedir?
4. Şu an güvenle çalıştırılabilecek gerçek dikey dilim hangisidir?
5. Bir sonraki uygulama adımı tam olarak nedir?
6. Hangi kanıtlar eksik olduğu için “tamamlandı” denemez?

### 6. Raporlama kuralları

- Genel ve belirsiz cümlelerden kaçın; her iddiayı kanıtla ilişkilendir.
- Bir dosyanın varlığını özelliğin çalıştığına dair kanıt sayma.
- “Planlanmış”, “iskelet”, “placeholder”, “çalışıyor” ve “kabul edildi”
  ifadelerini birbirinden ayır.
- Kod var ama test yoksa bunu açıkça belirt.
- Test geçiyor ama gereksinim yoksa bunu da açıkça belirt.
- Mevcut Bridge V0 başarısını, framework’ün tamamının kurulduğu şeklinde
  yorumlama.
- SILBO model/training çalışmasını bu framework review’uyla karıştırma.
- Kullanıcı izni olmadan hiçbir dosyayı değiştirme ve hiçbir sonuç üzerinde
  commit/push yapma.

Raporun sonunda kısa bir “kanıt eki” ver: çalıştırılan komutlar, exit code’lar,
test özetleri, taranan dosya sayıları, link/hash sonuçları ve doğrulanamayan
alanlar.

---

## Beklenen değerlendirme sonucu

Bu promptun çıktısı bir pazarlama özeti değil, mevcut durum ile hedef mimari
arasındaki farkı gösteren bağımsız bir denetim raporu olmalıdır. Claude’un
sonucu sonraki implementasyon adımlarının sıralanmasında kullanılacak; bu nedenle
kanıtsız “tamamlandı” ifadeleri kabul edilmemelidir.
