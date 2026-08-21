# AIRL-OS — İdeal Yapı Önerisi, Katkılar ve Mimari Review

| Alan | Değer |
|---|---|
| Belge tipi | Mimari katkı + tasarım denetimi |
| Girdi | `AIRL-OS-Architecture.md` v1.0 (3.434 satır), `planning/commissioning/` (186 dosya), `obra/superpowers` |
| Kardeş belge | [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer|AIRL-OS Skill Layer]] — operasyonel skill katmanı (Superpowers tam entegrasyonu) |
| Yazan | Claude Opus 5 (bağımsız) |
| Tarih | 2026-08-22 |
| Durum | Öneri — insan kararı bekliyor |

> **Okuma sırası:** Bölüm C (7. Düzlem) ve Bölüm D (rol→model) bu belgenin
> omurgasıdır. Bölüm A/B katkı kataloğu, Bölüm G mevcut tasarımın denetimidir.
> Aceleniz varsa: **C → D → G.**

---

## 0. Bu belge ne yapıyor

Mevcut `AIRL-OS-Architecture.md` **güçlü bir mimari**. Otorite bölüşümü doğru,
Temporal/LangGraph ayrımı doğru, Tool Broker deseni doğru, re-anchoring state
machine'i nadir görülen kalitede.

Bu belge üç şey yapıyor:

1. **Ekliyor** — gerçek araştırma organizasyonlarında var olan ama planınızda
   olmayan roller, review mekanizmaları ve araçlar.
2. **Yapısal bir eksik öneriyor** — mevcut mimari *araştırmayı* ölçüyor;
   *laboratuvarın kendi doğruluk üretme kapasitesini* ölçmüyor. Bunun için
   7. bir düzlem öneriyorum.
3. **Denetliyor** — ideal yapıya göre mevcut tasarımın boşluklarını çıkarıyor.

**Temel tez:** Model tarafından yürütülen bir laboratuvarda, "bağımsız review"
bir *varsayım* olamaz. **Ölçülen bir büyüklük** olmak zorunda.

---

# BÖLÜM A — Eklenen roller

Mevcut yapınız: 6 kalıcı fonksiyon + geçici proje hücresi (Decision Owner,
Scientific Owner, Evidence Lead, Engineering Owner, Assurance Lead, Safety/Data
Owner).

Gerçek araştırma organizasyonlarında var olup sizde olmayan roller:

## A1. Statistical Methods Owner (İstatistiksel Yöntem Sahibi) — 🔴 kritik

**Gerçek dünya karşılığı:** Klinik araştırmada biyoistatistikçi. **SAP**
(Statistical Analysis Plan) yazar ve unblinding'den önce kilitler. SAP
kilitlenmeden veri açılmaz. Bu rol **bloke edici**dir.

**Neden sizde eksik:** `ProtocolManifest`'inizde `uncertainty`,
`confidence_target: 0.95`, `exclusion_rules` ve `stop_rules` var — hepsi
istatistiksel kararlar. Ama bunların **sahibi yok**. Scientific Owner protokolü
yazıyor, kimse istatistiksel geçerliliği imzalamıyor.

**AIRL-OS'ta:**
- G2'de **ProtocolManifest'ten ayrı bir `AnalysisPlanManifest`** üretir ve kilitler.
- G4 baseline'da güç analizi (power) ve minimum tespit edilebilir etki büyüklüğü verir.
- G6'da `statistical_validity` boyutunu **bloke edebilir**.
- **Exploratory / Confirmatory ayrımının sahibi.** Ön-kayıtta olmayan her analiz
  `exploratory` etiketiyle raporlanır; `confirmatory` iddia üretemez.

**Kritik ek:** `AnalysisPlanManifest`, `ProtocolManifest`'ten **ayrı**
kilitlenmeli. Sebep: protokol "ne ölçeceğiz", analiz planı "nasıl karar
vereceğiz". İkisini birleştirmek, sonuçları gördükten sonra karar kuralını
değiştirme kapısını açık bırakır.

---

## A2. Research Integrity Officer (Araştırma Bütünlüğü Sorumlusu) — 🔴 kritik

**Gerçek dünya karşılığı:** ABD'de ORI düzenlemeleri (42 CFR Part 93) uyarınca
her kurumda zorunlu RIO. FFP (Fabrication, Falsification, Plagiarism)
iddialarını yönetir. Araştırma hattından **bağımsız** raporlama çizgisi vardır.

**Neden sizde eksik:** G6 non-waivable blocker listenizde
*"Fabrication/tamper şüphesi (reviewer tarafından)"* var. Ama:
- Şüpheyi **kim** araştırıyor?
- Süreç ne? Şüpheli çalışma durur mu, devam eder mi?
- Sonuç nereye kaydedilir?
- Yanlış suçlama nasıl kapanır?

Hiçbiri tanımlı değil. Bir AI laboratuvarında bu risk **artar**, azalmaz —
uydurma alıntı ve uydurma sayı, LLM'lerin en bilinen hata modu.

**AIRL-OS'ta:**
- **Her gate'i durdurma yetkisi**, Assurance Lead'den bağımsız raporlama.
- `IntegrityCase` nesnesi: `ALLEGED → TRIAGED → INVESTIGATING → SUBSTANTIATED / UNSUBSTANTIATED → CLOSED`
- Mekanik tetikleyiciler (aşağıda B7 — istatistiksel adli kontroller) doğrudan
  `IntegrityCase` açar; insan yorumu beklemez.
- Sonuç `SUBSTANTIATED` ise: ilgili claim'ler `RETRACTED`, üreten model profili
  `SUSPENDED`, tüm geçmiş çıktıları taranır.

---

## A3. Data Steward (Veri Yöneticisi)

**Gerçek dünya karşılığı:** FAIR ilkelerinin (Findable, Accessible,
Interoperable, Reusable) sahibi. Fon veren kurumların zorunlu tuttuğu **DMP**
(Data Management Plan) yazarı. Kütüphaneciden farklı bir meslek.

**Neden sizde eksik:** `Evidence Lead` bibliyografik yönetim yapıyor. Ama bir
araştırma laboratuvarı **veri seti üretir** — ve sizin mimaride üretilen
datasetlerin yaşam döngüsü sahibi yok. `SourceEntity.source_type` içinde
`'dataset'` var ama dataset *üretimi* modellenmemiş.

**AIRL-OS'ta:**
- G1'de `DataManagementPlan` üretir: hangi veri üretilecek, nerede saklanacak,
  ne kadar süreyle, kim erişecek, nasıl atıf alacak.
- Üretilen her dataset için **Croissant** (MLCommons) metadata + DOI (Zenodo).
- Retention/legal hold politikasının sahibi.
- D0–D4 sınıflandırmasını Safety/Data Owner ile birlikte uygular.

---

## A4. Research Software Engineer (RSE)

**Gerçek dünya karşılığı:** Artık ayrı bir meslek (Society of RSE, US-RSE).
Bilimsel kod kalitesi, sürdürülebilirlik ve *paketlenebilir tekrar
üretilebilirlik* sahibi. Data engineer veya platform engineer değil.

**Neden sizde eksik:** `Engineering Owner` üç işi birden yapıyor: kod yazmak,
altyapı kurmak, deney yürütmek. Gerçek laboratuvarlarda bunlar ayrılır çünkü
teşvikleri çelişir — deneyi yürütmek isteyen kişi, kodu tekrar üretilebilir
paketlemek istemez.

**AIRL-OS'ta:**
- G7 reproduction paketinin sahibi: `RO-Crate` + `CITATION.cff` + `CodeMeta`.
- **ACM artifact badge seviyesini** atar (bkz. B4).
- Ortam determinizminden sorumlu: Nix/Apptainer, digest-pinned image, seed kontrolü.
- Engineering Owner **üretir**, RSE **paketlenebilir kılar** — ayrı teşvik.

---

## A5. Scientific Editor / Claims Discipline (Bilimsel Editör)

**Gerçek dünya karşılığı:** Dergi editörü + kurum içi teknik yazım. Görevi:
metnin verinin izin verdiğinden fazlasını söylememesi.

**Neden bu bir AI laboratuvarında kritik:** LLM'lerin en tutarlı hatası
**aşırı genelleme**. Sizin ReviewVerdict örneğinizde bile
`claim_scope_assessment: "Overstated in places"` var — yani bunu zaten
gözlemlemişsiniz.

**AIRL-OS'ta — ve bu mekanik olarak zorlanabilir:**

> **Scope Conformance Check:** G9 yayın metnindeki her iddia cümlesi, Claim
> Ledger'daki bir `ClaimVersion`'a eşlenmek zorundadır ve o cümlenin kapsamı
> `ClaimVersion.scope_qualification`'ı aşamaz. Eşlenemeyen cümle → yayın BLOCKED.

Bu, "false rigor"a karşı en ucuz ve en etkili mekanik kontrollerden biri.
`DecisionRecord.obligations` alanınız (*"Publication must include scope
restriction"*) zaten bunu istiyor ama **denetleyen bir mekanizma yok**.

---

## A6. Red Team Lead (Kalıcı fonksiyon)

**Gerçek dünya karşılığı:** İstihbarat analizinde "Team B" ve yapılandırılmış
analitik teknikler. Kalıcı, göreve bağlı değil.

**Neden sizde eksik:** `Adversarial Reviewer` bir **task rolü**. Yani proje
başına atanıyor ve o projenin bağlamında çalışıyor. Kalıcı bir kırmızı takım
farklı bir şey yapar: **laboratuvarın sistematik kör noktalarını** bulur, tek
tek projelerin değil.

**AIRL-OS'ta:**
- Proje bazlı değil, **portföy bazlı**. "Son 10 projede hangi hata tipi tekrar ediyor?"
- **Pre-mortem** yürütür (bkz. B8) — G4'ten önce.
- Kontrol enjeksiyonunun sahibi (bkz. C4) — ve bunu ajanlardan gizli tutar.
- WP-060'taki *güvenlik* saldırı paketinden ayrıdır; bu **bilimsel** kırmızı takım.

---

## A7. Knowledge Steward (Kurumsal Hafıza)

**Gerçek dünya karşılığı:** İnsan laboratuvarlarında bu rol *örtük* olarak
kıdemli araştırmacılarda bulunur — "bunu 2019'da denedik, çalışmadı."

**Neden bir AI laboratuvarında açık bir rol olmak zorunda:** Modellerin
kurumsal hafızası yok. Her proje sıfırdan başlar. On projeden sonra aynı ölü
sokağa onuncu kez girersiniz.

**AIRL-OS'ta:**
- **Projeler arası claim çelişki tespiti**: yeni bir `ClaimVersion` üretildiğinde,
  Claim Ledger'da `refutes` ilişkisi kurulabilecek eski claim var mı?
- **Negatif sonuç kataloğu**: `ACC-39` senaryonuz negatif sonucu test ediyor ama
  hiçbir yerde *aranabilir* hale getirilmiyor.
- **Yöntem yeniden kullanımı**: `ProtocolManifest`'ler arası benzerlik; "bu
  protokol daha önce kullanıldı, sonuçları şunlardı."
- Neo4j burada gerçekten değer üretir — sizin de belirttiğiniz gibi türev bir
  görünüm, ama bu sorgular için doğru araç.

---

## A8. Rol kataloğu — özet

| Rol | Durum | Tip | Bloke edebilir |
|---|---|---|---|
| Project Decision Owner | mevcut | **insan** | G8, G9 |
| Scientific Owner | mevcut | insan + model destekli | G2 |
| Evidence Lead | mevcut | insan + model destekli | G3 |
| Engineering Owner | mevcut | insan + model destekli | G4, G5 |
| Assurance Lead | mevcut | insan + model destekli | G6, G7 |
| Safety/Data Owner | mevcut | insan | tümü (veri sınıfı) |
| **Statistical Methods Owner** | **eklendi** | insan + model | **G2, G4, G6** |
| **Research Integrity Officer** | **eklendi** | **insan** | **tümü** |
| **Data Steward** | **eklendi** | insan + model | G1, G9 |
| **Research Software Engineer** | **eklendi** | model + insan onayı | G7 |
| **Scientific Editor** | **eklendi** | model + mekanik kontrol | **G9** |
| **Red Team Lead** | **eklendi** | insan + model | G4 (pre-mortem) |
| **Knowledge Steward** | **eklendi** | model + mekanik | G0 (duplicate) |
| **Metascience Lead** | **eklendi** | insan + mekanik | — (ölçer, bloke etmez) |

---

# BÖLÜM B — Eklenen review mekanizmaları

Mevcut mekanizmalarınız: mechanical, blind, adversarial, citation audit,
security, arbitration, reproduction. İyi bir set. Eksik olanlar:

## B1. Stage-1 Registered Report kabulü — 🔴 en yüksek etkili ekleme

**Gerçek dünya:** Registered Reports formatında protokol, **veri toplanmadan
önce** hakem değerlendirmesinden geçer ve kabul edilirse (*in-principle
acceptance*) yayın **sonuçtan bağımsız olarak** garanti edilir. Yayın
yanlılığını (publication bias) kökten öldüren tek mekanizma.

**Sizde neden eksik:** G2'de protokol donduruluyor ✅ ama G8'de karar **sonuçlara
bakılarak** veriliyor. Yani:

```
G2: protokol donduruldu
G5: sonuç çıktı — negatif
G8: Decision Owner "REJECT" diyebilir
→ negatif sonuç yayınlanmaz → yayın yanlılığı korunur
```

`ACC-39 — Negative Research Result` senaryonuz bu riski *test ediyor* ama
mimaride bunu *engelleyen* bir mekanizma yok.

**AIRL-OS'ta:**

> **G2'de `InPrincipleAcceptance` üretilir.** Protokol + analiz planı bağımsız
> olarak kabul edildiyse, G8 kararı yalnız şu eksende olabilir: *"protokol
> uygulandı mı?"* — *"sonuç hoşuma gitti mi?"* değil.
>
> G8'in `REJECT` verebileceği tek durum: protokol ihlali, bütünlük sorunu veya
> G7 reproduction başarısızlığı. **Sonucun yönü gerekçe olamaz.**

Bu tek değişiklik, laboratuvarınızın bilimsel güvenilirliğini diğer tüm
mekanizmaların toplamından fazla artırır.

---

## B2. Blinded Analysis (Körleştirilmiş analiz)

**Gerçek dünya:** Parçacık fiziğinde standart. Analist, analiz kilitlenene kadar
gerçek sonucu göremez — veri "tuzlanır" (salting), etiketler karıştırılır veya
sinyal bölgesi maskelenir. LIGO kör enjeksiyon kullandı.

**Sizde neden eksik:** Sizin "blind review"unuz **reviewer'ı** kör ediyor
(producer'ın trace'ini görmüyor). Ama **analistin kendisi** sonucu görerek
analiz yapıyor. Asıl serbestlik derecesi orada.

**AIRL-OS'ta:**
- G5 çıktısı, analiz ajanına **koşul etiketleri maskelenmiş** olarak verilir.
- Analiz pipeline'ı `AnalysisPlanManifest`'e göre kilitlenir.
- Kilit sonrası unblinding; kilitten sonra yapılan her değişiklik `exploratory`.
- Uygulanabilirlik: her deney tipinde mümkün değil — R2/R3'te **zorunlu**,
  R1'de opsiyonel.

---

## B3. Multi-Analyst + Multiverse Analysis — 🔴 AI laboratuvarı için ideal

**Gerçek dünya:** Silberzahn ve ark. (2018) aynı veri setini 29 bağımsız ekibe
verdi; etki büyüklükleri geniş bir aralığa yayıldı ve bazıları zıt yönlüydü.
Aynı veri, aynı soru, farklı savunulabilir analiz yolları → farklı sonuç.
Buna **analitik serbestlik dereceleri** denir.

**Neden bu tam olarak sizin sisteminiz için:** İnsan laboratuvarları bunu
yapamaz — 29 ekip pahalıdır. **Sizin laboratuvarınız yapabilir.** N bağımsız
analiz ajanı çalıştırmak ucuzdur.

**AIRL-OS'ta:**

```
G5 sonuç → N bağımsız analiz ajanı (farklı model ailesi, aynı AnalysisPlan)
        → sonuç dağılımı
        → dağılım dar mı? claim sağlam.
        → dağılım geniş mi? claim'in confidence'ı DÜŞER ve
          scope_qualification zorunlu hale gelir.
```

Ve **specification curve / multiverse**: tek bir analiz yolu yerine tüm
savunulabilir yolları (dışlama kuralları, dönüşümler, kovaryatlar) çalıştırıp
sonucun **dağılımını** raporlayın. p-hacking'e karşı doğrudan savunma.

**Bu, `reproducibility` confidence boyutunuza gerçek bir ölçüm temeli verir.**

---

## B4. ACM Artifact Badge seviyeleri — terminoloji düzeltmesi

**Sorun:** Dokümanınız `repeatability, reproducibility, replication` üçlüsünü
girişte anıyor ama hiçbir yerde tanımlamıyor. Ve G7 metodolojinizde
*"farklı solver (Gurobi vs CPLEX), farklı seed"* deyip `±2%` eşleşme bekliyor —
bu **replication**, reproduction değil.

**Hazır ve yerleşik çözüm — ACM/NISO rozet vokabüleri:**

| Seviye | Anlamı | AIRL-OS gate |
|---|---|---|
| **Artifacts Available** | Artifact kalıcı bir arşivde, DOI'li | G9 |
| **Artifacts Evaluated — Functional** | Belgelenmiş, tutarlı, tam, çalışıyor | G5 sonu |
| **Artifacts Evaluated — Reusable** | Yukarıdakiler + yeniden kullanılabilir kalitede | G7 (RSE) |
| **Results Reproduced** | **Farklı ekip, aynı artifact** ile sonuç elde edildi | **G7** |
| **Results Replicated** | **Farklı ekip, farklı artifact** ile sonuç elde edildi | **G7+ / bağımsız** |

Ve NASEM tanımı: *reproducibility* = aynı veri + aynı kod → aynı sonuç
(**deterministik**, tolerans ≈ 0); *replicability* = yeni veri/yeni uygulama →
tutarlı sonuç (**istatistiksel**, tolerans dağılım karşılaştırmasıyla).

**Sonuç:** Sizin G7'niz aslında **iki ayrı gate** olmalı:

- **G7a — Reproduction:** aynı manifest, aynı seed, aynı image digest → **bit
  düzeyinde veya `< %0,1`**. Tolerans yok. Model yargısı yok. Ya tutar ya tutmaz.
- **G7b — Replication:** farklı seed, farklı uygulama, farklı ortam → **dağılım
  karşılaştırması** (CI örtüşmesi / eşdeğerlik testi), tek bir `%` değil.

Mevcut `±2% / >=95% / >5%` üçlü çelişkisi bu ayrımla kendiliğinden çözülür.

---

## B5. Delphi konsensüsü (tek hakem yerine)

**Gerçek dünya:** RAND'ın Delphi yöntemi. Çok turlu, **anonim**, kontrollü geri
beslemeli uzlaşma. Ankraj etkisini ve baskın görüşün diğerlerini sürüklemesini
engellemek için tasarlandı.

**Sizde neden eksik:** `DisagreementCase` → tek bir `arbiter`. Tek hakem tek
hata noktasıdır ve modelse kendi yanlılıklarını taşır.

**AIRL-OS'ta:**
```
Tur 1: N reviewer bağımsız verdict + gerekçe (birbirini görmez)
Tur 2: anonimleştirilmiş gerekçe özeti dağıtılır; herkes verdict'ini
       revize edebilir — DEĞİŞTİRİRSE GEREKÇE ZORUNLU
Tur 3: hâlâ uzlaşma yoksa → insan arbiter, ve arbiter TÜM turları görür
```
Yakınsama ölçülür: turlar arası verdict değişim oranı. Çok hızlı yakınsama =
sürü etkisi şüphesi, ayrı bir sinyal.

---

## B6. Analysis of Competing Hypotheses (ACH)

**Gerçek dünya:** Richards Heuer, CIA. Yapılandırılmış analitik teknik.
Mantığı ters çevirir: *"hangi hipotezi destekliyor?"* değil,
**"hangi hipotezleri ELİYOR?"**

Mekanik:
1. Tüm makul hipotezleri listele (favori olanı değil)
2. Tüm kanıtı listele
3. Her kanıt × her hipotez matrisi: tutarlı / tutarsız / ilgisiz
4. **Tanısallık (diagnosticity)**: bir kanıt tüm hipotezlerle tutarlıysa
   **değersizdir** — ayırt etmiyor
5. En çok *tutarsızlığa* sahip hipotezleri ele; kalanı sırala

**Neden Claim Ledger'ınıza mükemmel oturuyor:** `EvidenceSpan.support_type`
zaten `supports | contradicts | qualifies | contextualizes` — ACH matrisinin
hücresi bu. Eksik olan tek şey **tanısallık skoru**: bu kanıt rakip hipotezleri
ayırt ediyor mu?

**Bu, "çok kanıt topladık" ile "ayırt edici kanıt topladık" arasındaki farkı
ölçen tek mekanizma.** Ve `PR-12 False Rigor`'un tam panzehri.

---

## B7. Mekanik istatistiksel adli kontroller — 🔴 ucuz, otomatik, yüksek getirili

Bunlar **model yargısı gerektirmez**. Deterministik, hızlı, otomatik. E1
katmanında (mekanik), pahalı model review'undan **önce** çalışır.

| Kontrol | Ne yapar | Nerede |
|---|---|---|
| **statcheck** | Raporlanan test istatistiği ile p-değerinin iç tutarlılığını kontrol eder | G6 mekanik |
| **GRIM** | Bildirilen ortalamanın N ve ölçüm granülerliğiyle **mümkün olup olmadığını** kontrol eder | G6 mekanik |
| **GRIMMER** | Aynısını standart sapma için yapar | G6 mekanik |
| **SPRITE** | Verilen ortalama+SD+N ile olası veri dağılımlarını yeniden kurar | Integrity Case |
| **Benford analizi** | Sayı dağılımı anomalisi | Integrity Case |
| **Alıntı entailment** | Her alıntının kaynak span'ini gerçekten desteklediğini kontrol | G6 (WP-080) |
| **Scope conformance** | Yayın metni ↔ ClaimVersion kapsam eşlemesi (A5) | G9 |
| **Hash/manifest** | Artifact bütünlüğü | tüm gate'ler |

**Kritik ilke:** Bunların hepsi model kararı olmadan `IntegrityCase` veya
`GATE_BLOCKED` üretebilir. LLM'in uydurduğu bir sayı GRIM'den geçemez.

---

## B8. Pre-mortem (G4 öncesi)

**Gerçek dünya:** Gary Klein. Proje başlamadan önce: *"Bir yıl geçti, proje
tamamen başarısız oldu. Neden?"* Prospektif geriye dönük bakış, gelecek zaman
kipinden geçmiş zaman kipine geçerek savunmacılığı kırar.

**AIRL-OS'ta:** G4 (Baseline & Budget) onayından önce Red Team, `ProtocolManifest`
ve `AnalysisPlanManifest` üzerinde pre-mortem yürütür. Çıktı, `falsification_plan`'a
**yeni maddeler ekler**. Maliyeti bir saat, getirisi büyük.

---

## B9. Severity Assessment (Ciddiyet değerlendirmesi)

**Gerçek dünya:** Deborah Mayo'nun hata istatistiği. Bir test **ciddidir** ancak
ve ancak: iddia yanlış olsaydı, bu test bunu **büyük olasılıkla yakalardı**.

**Sizde neden eksik:** `falsification_plan`'ınız *"eğer consensus < 90%: yöntem
başarısız"* diyor. Ama sormuyor: **"yöntem gerçekten başarısız olsaydı, bu test
onu yakalar mıydı?"** — yani testin **gücü**.

Güçsüz bir test geçmek, kanıt değildir. Bu, "çok test yaptık" ile "zorlu test
yaptık" arasındaki farktır.

**AIRL-OS'ta:** her `ClaimVersion` için `severity_assessment`:
`{test_id, would_detect_if_false: probability, basis}` — Statistical Methods
Owner tarafından imzalanır.

---

## B10. Adversarial Collaboration (gerçek uyuşmazlıklar için)

**Gerçek dünya:** Kahneman'ın önerisi. Anlaşamayan iki taraf, anlaşmazlığı
çözecek deneyi **birlikte tasarlar** ve hangi sonucun ne anlama geleceğini
**önceden** kabul eder.

**AIRL-OS'ta:** `DisagreementCase` arbitration ile kapanmazsa, otomatik hakem
kararı yerine: iki taraf birlikte yeni bir `ProtocolManifest` üretir, önceden
karar kuralını yazar, deney çalışır. Ucuz olmayan ama kesin çözüm.
R3'te `arbitration_failed` durumunun varsayılan yolu bu olmalı.

---

## B11. Review mekanizmaları — özet

| Mekanizma | Durum | Gate | Model mi, mekanik mi? |
|---|---|---|---|
| Mekanik doğrulama (hash, manifest) | mevcut | tümü | **mekanik** |
| Blind review | mevcut | G6 | model |
| Adversarial review | mevcut | G6 | model |
| Citation/entailment audit | mevcut | G6 | mekanik + model |
| Security review | mevcut | G6 | mekanik + model |
| Arbitration | mevcut | G6 | insan |
| Reproduction | mevcut | G7 | **mekanik** |
| **Stage-1 in-principle acceptance** | **eklendi** | **G2** | model + insan |
| **Blinded analysis** | **eklendi** | **G5→G6** | mekanik |
| **Multi-analyst / multiverse** | **eklendi** | **G6** | model (N adet) |
| **ACM badge seviyelendirme** | **eklendi** | **G7a/G7b** | mekanik |
| **Delphi konsensüs** | **eklendi** | **G6** | model (N tur) |
| **ACH + tanısallık** | **eklendi** | **G6** | model + mekanik matris |
| **statcheck/GRIM/GRIMMER/SPRITE** | **eklendi** | **G6 mekanik** | **mekanik** |
| **Pre-mortem** | **eklendi** | **G4** | model + insan |
| **Severity assessment** | **eklendi** | **G2, G6** | insan imzalı |
| **Adversarial collaboration** | **eklendi** | **G6 escalation** | insan + model |
| **Scope conformance** | **eklendi** | **G9** | **mekanik** |

---

# BÖLÜM C — 7. Düzlem: Metascience & Calibration

## C0. Neden yeni bir düzlem gerekiyor

Mevcut altı düzleminiz **araştırmayı** yönetiyor. Hiçbiri şu soruyu sormuyor:

> **"Bu laboratuvar doğru sonuç üretiyor mu? Nereden biliyoruz?"**

Bir insan laboratuvarında bu soru dolaylı yollarla cevaplanır: itibar,
atıflar, replikasyonlar, zaman. Bir **model tarafından yürütülen** laboratuvarda
bu yollar yok — ve olmadığı için ölçülmek zorunda.

Ve şu ampirik gerçek meseleyi zorunlu kılıyor:

> **Farklı model ailesi kullanmak, bağımsızlık garantisi vermez.**
> Frontier modeller büyük ölçüde örtüşen korpuslarda eğitiliyor. Aynı hatayı
> aynı güvenle yapabilirler. İki reviewer'ın hemfikir olması, hata korelasyonu
> ölçülmediği sürece kanıt değeri taşımaz.

Sizin `IndependenceMatrix`'iniz Model Lineage'ı **non-compensable değil** olarak
işaretlemiş — bu doğru sezgi. Ama o zaman geriye kalan tek gerçek bağımsızlık
ekseni **mekanik doğrulama**dır, ve bunun ölçülmesi gerekir.

---

## C1. Agreement Calibration — bağımsızlığın ölçülmesi

**Mekanizma:**

```
Kalıcı bir "agreement calibration set" tutulur:
  - Doğru cevabı bilinen N adet review görevi
  - Her nitelikli model profili periyodik olarak bu seti işler
  - Ölçülen:
      * doğruluk (accuracy)
      * ikili hata korelasyonu (pairwise error correlation)
      * şansı aşan uyum (Fleiss' κ / Krippendorff's α)
```

**Ve karar kuralı:**

> İki model profilinin **hata korelasyonu** `ρ` eşiğin üzerindeyse, ikisi birden
> aynı claim'in bağımsızlık kotasına sayılamaz. Independence Matrix'in
> `Model Lineage` boyutu artık **beyan değil, ölçüm**.

Bu, WP-007'yi kağıt üzerinde bağımsızlıktan gerçek bağımsızlığa çeviren tek
mekanizmadır. Ve ölçmek ucuzdur.

**Ek sinyal:** Uyumun *çok* yüksek olması da alarmdır — κ ≈ 1,0 bağımsız
yargıçlarda beklenmez; ya görev trivialdir ya da yargıçlar bağımsız değildir.

---

## C2. Confidence Calibration — 7 skalanın kurtarılması

**Sorun:** `ClaimVersion` yedi confidence boyutu taşıyor
(`identity_confidence`, `entailment`, `method_validity`, `independence`,
`reproducibility`, `scope_fit`, `currency`) — hepsi `0.0–1.0`, iki-üç haneli
hassasiyetle.

**Bu sayılar bugün hiçbir şey ifade etmiyor**, çünkü:
- Üreticileri (LLM'ler) kalibre değil
- Birleştirme kuralı tanımlı değil
- Doğrulukla karşılaştırılmıyor

`0.95` ile `0.87` arasındaki fark, ölçülmediği sürece **süslemeden ibarettir.**
Ve bu tam olarak sizin `PR-12 — False Rigor` riskinizin tanımıdır.

**Çözüm — üç adım:**

1. **Ölç.** Her tahmin edilen confidence, sonunda bir sonuçla eşleşir
   (claim G7'de doğrulandı mı? G10'da hayatta kaldı mı?). **Brier skoru** ve
   kalibrasyon eğrisi hesaplanır.
2. **Yeniden kalibre et.** Ham model skorları → izotonik regresyon veya Platt
   ölçekleme ile kalibre edilmiş olasılığa çevrilir. `ClaimVersion` **ikisini de**
   saklar: `raw_confidence` ve `calibrated_confidence`.
3. **Kalibre değilse gösterme.** Bir boyut için yeterli sonuç verisi yoksa,
   sayı yerine `UNCALIBRATED` gösterilir. **Sahte hassasiyet yasaktır.**

**Ve birleştirme kuralı:** Çarpmayın, ortalamayı almayın. Bu boyutlar bağımsız
değil ve farklı şeyleri ölçüyor. Önerim: **en zayıf halka kuralı** —
`claim_strength = min(dimensions)` + hangi boyutun bağladığı açıkça gösterilir.
Bir claim en zayıf kanıt boyutu kadar güçlüdür.

---

## C3. Gate Yield — hangi kapı gerçekten işe yarıyor?

**Ölçüm:** Her gate için: kaç madde girdi, kaç tanesi bloklandı/revize edildi,
ve o bulgular sonradan **gerçek** çıktı mı?

```
gate_yield(G6-adversarial) = onaylanan bulgu / toplam bulgu
false_positive_rate(G6-adversarial) = reddedilen bulgu / toplam bulgu
maliyet(G6-adversarial) = token + wall-clock + insan dakikası
```

**Neden kritik:** Assurance'ın bir maliyeti var ve sonsuz derinlik mümkün değil.
Hangi kapının gerçekten hata yakaladığını bilmezseniz, assurance **ritüele**
dönüşür — çok artifact, az koruma. Bu, `PR-04` (verification backlog) ve
`PR-12`'nin ortak kökü.

Düşük yield'li bir gate ya kaldırılır ya yeniden tasarlanır. Yüksek yield'li
gate derinleştirilir.

---

## C4. Kontrol enjeksiyonu — laboratuvarın kendi hata oranı — 🔴

**Gerçek dünya:** Genomik ve epidemiyolojide standart — pozitif kontrol
(cevabı bilinen), negatif kontrol (etki olmaması gereken, ör. permüte edilmiş
veri). Pipeline karıştırılmış veride "etki bulursa" pipeline bozuktur.

**AIRL-OS'ta:**

> Projelerin küçük bir oranı (**ör. %5–10**) *tohumlanmış* olarak açılır:
> - **Pozitif kontrol:** cevabı önceden bilinen bir soru
> - **Negatif kontrol:** null veri / permüte edilmiş veri — bulunacak etki yok
>
> Bunlar gerçek projelerden **ayırt edilemez** olmalı ve **ajanlardan gizli**
> tutulmalıdır (Red Team Lead ve Metascience Lead bilir).
>
> Ölçülen: laboratuvarın **yanlış pozitif oranı** ve **yanlış negatif oranı**.

**Bu, laboratuvarın tek gerçek doğruluk ölçüsüdür.** Diğer her şey süreç
metriğidir; bu sonuç metriğidir.

Ve bu, daha önce belirttiğim "laboratuvarın kendi eval harness'ı yok" boşluğunun
somut çözümü. MLE-bench/PaperBench dışarıdan ölçer; kontrol enjeksiyonu
**canlı hatta, gerçek koşullarda** ölçer.

---

## C5. İnsan dikkat bütçesi ve rubber-stamping tespiti

**Sorun:** `PR-11 — Human rubber-stamping` sizin kendi risk register'ınızda.
Ama mimaride buna karşı bir mekanizma yok — yalnız SLA var, ve SLA baskısı
rubber-stamping'i **artırır**.

Ve bir model laboratuvarında bu risk yapısaldır: modeller insandan çok daha
hızlı üretir; insan darboğaz olur; darboğaz olan insan onaylamaya başlar.

**Mekanizma:**

```yaml
HumanAttentionBudget:
  max_g8_decisions_per_week: 5          # SERT KOTA, SLA değil
  min_evidence_view_seconds: <pakete göre hesaplanır>
  mandatory_disagreement_exposure: true  # açık uyuşmazlık gizlenemez
  
  ölçülen:
    decision_time_distribution      # çok kısa = alarm
    evidence_sections_actually_opened
    reversal_rate_at_G10            # G8'de kabul, G10'da geri alınan oranı
    dissent_override_rate           # adversarial REJECT'e rağmen ACCEPT oranı
```

**Kota dolduğunda ne olur:** Kuyruk **bekler**. Auto-approve yok, SLA
uzatılmaz, "hızlı gözden geçirme" modu yok. Laboratuvarın çıktı hızı, insan
karar kapasitesiyle sınırlıdır — ve bu bir hata değil, **tasarım**.

---

## C6. Claim Survival — laboratuvarın nihai skoru

**Ölçüm:** G8'de kabul edilen claim'lerin 6/12/24 ay sonra durumu.

```
survival_rate = RECONFIRMED / (RECONFIRMED + REVISED + SUPERSEDED + RETRACTED)
```

G10 `ImpactCase` altyapınız bu veriyi **zaten üretiyor**. Toplanması gereken tek
şey, bunu bir zaman serisi olarak takip etmek.

Ve bu, tüm sistemin gerçek KPI'sıdır. Diğer her metrik ara metriktir.
Survival rate düşüyorsa, hangi gate'in yield'i düştüğü C3 ile bulunur.

---

## C7. Metascience Plane — özet

| Ölçüm | Cevapladığı soru | Girdi | Sıklık |
|---|---|---|---|
| **Agreement calibration** (κ, ρ) | Reviewer'larım gerçekten bağımsız mı? | calibration set | aylık |
| **Confidence calibration** (Brier) | Confidence sayıları anlamlı mı? | claim sonuçları | çeyreklik |
| **Gate yield** | Hangi kapı gerçekten hata yakalıyor? | bulgu → doğrulama | çeyreklik |
| **Kontrol enjeksiyonu** | Laboratuvarın FP/FN oranı ne? | tohumlanmış projeler | sürekli |
| **Dikkat bütçesi** | İnsan gerçekten karar veriyor mu? | karar telemetrisi | haftalık |
| **Claim survival** | Ürettiğimiz bilgi ayakta kalıyor mu? | G10 ImpactCase | sürekli |

**Kritik kural:** Metascience düzlemi **hiçbir gate'i bloke etmez.** Ölçer ve
raporlar. Bloke etme yetkisi verilirse, ölçülen şeyi optimize etme baskısı
doğar (Goodhart yasası) ve ölçüm bozulur. Tek istisna: kontrol enjeksiyonunda
**negatif kontrolde etki bulunması** — bu pipeline bozukluğudur ve hattı durdurur.

---

# BÖLÜM D — Rol → Model atama mimarisi

> **Karara bağlandı:** Somut model havuzu, gate→aktör tablosu, effort→R sınıfı
> eşlemesi ve snapshot pinning kısıtı ayrı belgede: [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_role_model_assignment|Rol → Model Atama]]

## D1. Atama ilkesi: doğrulama asimetrisi

Her gate için tek soru:

> **Bu adımda mekanik bir doğrulama mümkün mü?**
> - **Evet** → mekanik önce çalışır, **model onu geçersiz kılamaz**
> - **Hayır** → model üretir, ama çıktısı *yanlışlanabilir* olmak zorunda

**Model, hipotez üreticisidir; verifier değildir.** Modelin çıktısı,
mekanik olarak kontrol edilebilen bir forma indirgenemiyorsa, o çıktı kanıt
değil, öneridir.

## D2. Gate → aktör matrisi

| Gate | Mekanik (deterministik) | Model | İnsan |
|---|---|---|---|
| **G0 Intake** | duplicate arama (Neo4j + embedding) | triage, benzerlik özeti | greenlight (5 dk) |
| **G1 Charter** | `RiskProfile → AssuranceClass` (**policy engine, model değil**) | charter taslağı, risk vektörü önerisi | **karar sorusunu yazar**, onaylar |
| **G2 Protocol** | şablon tamlık kontrolü | protokol taslağı, pre-mortem, Stage-1 review (farklı aile) | Scientific Owner + Stat Owner **imzalar** |
| **G2b Analysis Plan** | — | analiz planı taslağı, güç analizi | **Stat Methods Owner kilitler** |
| **G3 Literature** | GROBID çıkarım, DOI çözümü, dedup, hash | keşif, sorgu planı, tarama (aktif öğrenme) | Evidence Lead **dondurur** |
| **G4 Baseline** | baseline koşusu (deterministik) | compute planı, red-team pre-mortem | budget onayı (FinOps + Eng) |
| **G5 Execute** | **deney koşusunun kendisi** | — *(model deneyin konusu değilse döngüde yok)* | — |
| **G6-0 Mekanik** | statcheck, GRIM/GRIMMER, entailment, hash, manifest | — | — |
| **G6-1 Blind** | ReviewPacketBuilder (**program**, prompt değil) | N reviewer, **ölçülmüş bağımsız** aileler | — |
| **G6-2 Adversarial** | — | adversarial + ACH tanısallık matrisi | — |
| **G6-3 Disagreement** | verdict karşılaştırma | Delphi turları | arbiter (**yalnız yakınsamazsa**) |
| **G7a Reproduction** | **aynı manifest, aynı seed → deterministik** | — | — |
| **G7b Replication** | farklı seed/uygulama → **dağılım testi** | — | RSE badge atar |
| **G8 Decision** | kanıt paketi bütünlüğü | **öneri üretebilir, karar veremez** | **YALNIZ İNSAN** (kotalı) |
| **G9 Publish** | **scope conformance** (mekanik), RO-Crate, hash | metin taslağı | Decision Owner + Editor |
| **G10 Monitor** | feed'ler (Crossref/Retraction Watch/CVE) | sinyal triyajı, materiality önerisi | material sinyalde karar |

**Üç kural:**
1. G5'te model yoksa (deney modelin kendisi değilse), sonuç **model
   yanlılığından arınmıştır**. Bu, laboratuvarın en temiz katmanıdır — koruyun.
2. G7a'da model **hiç yok**. Ya tutar ya tutmaz.
3. G8'de model **yalnız öneri** üretir. Bu sizde zaten non-waivable ✅.

## D3. Model havuzu ve kota mimarisi

```yaml
ModelPool:
  producer_tier:      # üretim: hız + maliyet dengeli
  reviewer_tier:      # review: producer'dan ÖLÇÜLMÜŞ bağımsız (C1)
  adversarial_tier:   # en yetenekli; reddetme oranıyla ödüllendirilir
  arbiter_tier:       # yalnız uyuşmazlıkta; her iki tarafı da görür
  local_tier:         # open-weight, YEREL — R3 ve G7 için ZORUNLU

Kurallar:
  - Bir claim'in producer'ı ve final reviewer'ı aynı profil OLAMAZ
  - Aynı claim'de hata korelasyonu ρ > eşik olan iki profil bağımsızlık
    kotasına birlikte sayılamaz          # C1 çıktısı
  - Adversarial reviewer'ın metriği REDDETME kalitesidir, onay hızı değil
  - R3 claim üreten koşu YEREL/open-weight model kullanır  # bkz. D4
```

## D4. Model snapshot saklama — G7 için yapısal zorunluluk

> **Sorun:** `ExperimentRun.model_snapshot: "Claude Sonnet 5 20260801"` ve
> Reproducibility **non-waivable**. Ama hosted sağlayıcılar snapshot'ları
> süresiz saklamaz. 6 ay sonra G7a çalıştırdığınızda o snapshot yoksa,
> "frozen manifest ile tekrar üret" garantisi çöker.

**Kaçınılmaz sonuç:**

| Assurance sınıfı | Model politikası | Gerekçe |
|---|---|---|
| R1 | hosted OK | Repro toleransı düşük kritiklikte |
| R2 | hosted OK + **tam I/O kaydı** (Langfuse) | Snapshot gidince en azından giriş/çıkış kanıtı kalır |
| **R3** | **yerel / open-weight ZORUNLU** (GGUF + SHA-256) | Ağırlıklar sizde; G7a gerçekten mümkün |

Elinizdeki 2×RTX A5000 + yerel GGUF altyapısı bu yüzden **opsiyonel bir tercih
değil, R3'ün önkoşulu.** SILBO tarafında zaten yaptığınız
`system_fingerprint` dondurma pratiği tam olarak doğru refleks — bunu
framework seviyesine taşıyın.

---

# BÖLÜM E — `obra/superpowers`'tan alınacak operasyonel mekanikler

Superpowers bir *kodlama* metodolojisi, ama çözdüğü problem sizinkiyle aynı:
**bir ajanın ürettiği işe nasıl güvenilir.** Ve sizin mimarinizde **kavramsal
olarak var ama operasyonel olarak eksik** olan şeyleri operasyonelleştirmiş.

## E1. Bilgi asimetrisinin dosya seviyesinde tanımlanması

Superpowers'ta implementer ve reviewer'ın **tam olarak hangi dosyaları gördüğü**
tanımlı:

| | Implementer görür | Reviewer görür |
|---|---|---|
| Task brief | ✅ | ✅ |
| Önceki task'ların *arayüzleri* | ✅ | ✅ (global constraints) |
| Implementer'ın raporu | yazar | ✅ |
| Kod diff'i | üretir | ✅ |
| **Implementer'ın iç muhakemesi** | — | ❌ **asla** |
| Oturum geçmişi | ❌ | ❌ |

Sizin `ReviewPacket.excluded_from_packet` listeniz aynı fikirde ✅. Ama
Superpowers bir adım daha ileri gidiyor: **"No context pasting — hand artifacts
as files, not inline text."**

**Alınacak:** `ReviewPacketBuilder` bir **program** olmalı, bir prompt değil.
Allowlist kodda, ACL'de ve testte tanımlı. Reviewer'a inline metin geçilmez;
yalnız dosya yolu ve hash verilir. Böylece "reviewer ne gördü" sorusunun cevabı
**denetlenebilir** olur — `evidence_packet_hash` alanınız zaten bunu istiyor.

## E2. "Implementer asla subagent dispatch etmez" — 🔴 kritik kural

> *"the implementer never dispatches subagents — not helpers, and never a reviewer."*

**Sizin mimarinizde bu kural yok.** `Assurance Lead` reviewer atıyor ✅ ama
hiçbir yerde **producer'ın kendi yardımcılarını çağırmasını yasaklayan** bir
kural yok. Yasak yoksa şu olur:

```
Producer agent → "yardımcı" ajan çağırır → yardımcı işin bir kısmını yapar
→ yardımcı fiilen ortak yazar → ama bağımsızlık defterinde görünmüyor
→ IndependenceMatrix yanlış PASS veriyor
```

**Alınacak — Independence Matrix'e 8. boyut:**

```yaml
- dimension: "Delegation Boundary"
  description: "Producer kendi doğrulayıcısını veya yardımcısını çağırabildi mi?"
  controls:
    - "Producer cannot spawn sub-agents"
    - "Reviewer assignment only by Assurance Lead / Task Compiler"
    - "All agent invocations recorded in the correlation chain"
  R1_requirement: "PASS"
  R2_requirement: "PASS"
  R3_requirement: "PASS (hard block)"
  non_compensable_for: [R1, R2, R3]
```

Bu boyut **tüm sınıflarda non-compensable** olmalı — çünkü ihlal edilirse diğer
altı boyutun ölçümü de geçersiz hale gelir.

## E3. Sınırlı eskalasyon merdiveni + "the breaker"

Superpowers'ın uyuşmazlık çözümü:

```
Tur 1–3: aynı implementer, bağlam korunur, bulgular VERBATIM iletilir
Tur 4–5: TAZE implementer, DAHA YETENEKLİ model,
         açık çerçeveleme: "önceki N kez denedi, artık senin"
Tur 5 sonu hâlâ açıksa → BREAKER:
         dispatch DURUR, insan her açık bulguyu tek tek adjudicate eder
         her hüküm deftere yazılır — SESSİZ İSKARTA YASAK
```

**Sizin `DisagreementCase`'inizde eksik olan:** sınır yok. Kaç tur? Ne zaman
insana gider? Model değişir mi? Ve en önemlisi: **açık bulguların sessizce
kaybolmaması** garantisi yok.

**Alınacak:** `DisagreementCase`'e `round`, `escalation_tier`,
`max_rounds` ve **`FindingLedger`** ekleyin. Her açık bulgu ya çözülür ya
`PARKED` + gerekçe + sahip + süre alır. `06_KANIT_VE_KABUL_STRATEJISI.md`'deki
finding yaşam döngünüz doğru, ama **turlu eskalasyona bağlı değil.**

## E4. Sınıflandırma önce + "şüphedeyken ağır olanı seç"

> *"when in doubt between two paths, take the heavier one"*

**Sizin `determine_assurance_class` fonksiyonunuz tam tersini yapıyor:**

```python
    # ...
    return R1     # ← fallthrough default = EN HAFİF
```

Bu **fail-open**. Eksik veya belirsiz bir `RiskProfile` alanı, projeyi en
düşük assurance sınıfına düşürür.

**Alınacak:**
```python
if not risk_profile.is_complete():
    return R3            # eksik bilgi = en ağır yol
# ...
return R2                # fallthrough default R1 değil R2
```

## E5. Yol yükseltme (mid-project risk reclassification)

> *"Hidden complexity discovered mid-task requires path escalation — stop,
> announce the upgrade, restart at the heavier level."*

**Sizin mimarinizde bu yok.** R1 olarak başlayan bir proje G5'te D3 veriye
dokunduğunu keşfederse ne olur? Doküman sessiz.

**Alınacak:** `RiskReclassificationEvent`. Yükselme olduğunda:
- Workflow **pause**
- Yeni sınıfın gate derinliği uygulanır
- **Daha hafif sınıfta geçilmiş gate'ler yeniden değerlendirilir**
- Düşürme (R3 → R2) yalnız Safety/Data Owner + Assurance Lead ortak kararıyla

## E6. İnsan onayına gitmeden önce zorunlu öz-review

> *"Specs must pass a self-review (checking for placeholders, contradictions,
> scope drift) before user review."*

Ucuz mekanik kapı, pahalı insan kapısından önce. Sizin E0–E5 kanıt katmanı
modeliniz zaten bu felsefede ✅ ama **G8'e giden pakette uygulanmıyor**.

**Alınacak:** `DecisionRequest` insan kuyruğuna girmeden önce otomatik kontrol:
placeholder var mı, çelişkili verdict var mı, kapsam kayması var mı, eksik
zorunlu alan var mı. Geçemezse insan zamanı harcanmaz.

## E7. Defter tabanlı kurtarma (ledger-driven recovery)

Superpowers'ta bağlam sıkışırsa `progress.md` tamamlanan işleri, git de
commit'leri verir. **Deterministik kurtarma.**

Sizin `implementation_log.md`'niz aynı fikirde ama **makine-okunur değil** —
serbest metin. Bir ajan bunu güvenilir şekilde ayrıştıramaz.

**Alınacak:** İnsan-okunur log yanında `progress.jsonl` (append-only):
`{step_id, wp_ids, status, target_sha, evidence_manifest, timestamp}`.

## E8. Superpowers'ın bağımsız olarak doğruladığı kararlarınız

Bunlar sizin doğru olduğunuzun teyidi — iki bağımsız tasarım aynı sonuca varmış:

| Superpowers | AIRL-OS | Ortak içgörü |
|---|---|---|
| "Approval ceremony scales, the gate never disappears" | "Oturumlar birleşebilir, gate kayıtları ayrılmalı" (Karar #4) | Ritüel esner, kayıt esnemez |
| Final whole-branch review, en yetenekli model | *(sizde yok)* | Parça review ≠ bütün review |
| Fresh subagent per task, oturum geçmişi yok | Context Isolation (non-compensable R2/R3) | Bağlam kirliliği bağımsızlığı öldürür |
| TDD: testten önce yazılan kod **silinir** | *(sizde yok)* | Sıra tersine dönerse kanıt geçersiz |

**Son satır özellikle önemli.** TDD'nin araştırmadaki karşılığı:

> **Ön-kayıttan (G2b Analysis Plan) önce hesaplanmış sonuçlar, `confirmatory`
> kanıt olarak kullanılamaz.** Yalnız `exploratory` olarak raporlanır.

Ve `E8-2`: G9'da **bütün yayın paketi üzerinde** en yetenekli modelle tek bir
final review — parça parça claim review'undan ayrı. Parçaları geçen bir bütün,
bütün olarak tutarsız olabilir.

---

# BÖLÜM F — Araç yığını

Fonksiyon bazlı. **Kalın** olanlar mevcut tasarımda yok ve doğrudan bir boşluğu kapatıyor.

## F1. Literatür ve kanıt

| Araç | Görev | Neden |
|---|---|---|
| **GROBID** | PDF → yapılandırılmış TEI XML | pdfplumber'dan **çok daha iyi** bölüm/referans/koordinat çıkarımı — span anchoring kalitenizi doğrudan artırır |
| **OpenAlex** | Atıf ağı, kapsam | Crossref'ten geniş, ücretsiz, tam açık |
| Crossref + Retraction Watch | Retraction feed | G10 — zaten planınızda |
| **Semantic Scholar / S2ORC** | Tam metin, alıntı bağlamı | Alıntı niyeti sınıflandırması |
| **Unpaywall** | Açık erişim tam metin | Yasal PDF erişimi (`PR-14` lisans riski) |
| **ASReview** | Aktif öğrenmeli tarama | **WP-071 screening/inclusion tam karşılığı — hazır ve açık kaynak** |
| **anystyle** | Referans ayrıştırma | Kaynakça normalizasyonu |
| **Nougat / PDFFigures2** | Şekil/tablo çıkarımı | Şekildeki veriyi kanıta bağlamak |
| PaperQA2 | Alıntı-doğrulamalı QA | Entailment denetimi için referans uygulama |

## F2. Kanıt standartları ve provenance

| Araç/standart | Görev | Neden |
|---|---|---|
| W3C Web Annotation | Span anchoring | Zaten kullanıyorsunuz ✅ |
| **W3C PROV-O** | Lineage modeli | Kendi lineage şemanız yerine standarda hizalayın — araç ekosistemi hazır |
| **Nanopublications** | Atomik, atıf alabilir claim + provenance | **`ClaimVersion`'ınız neredeyse birebir nanopub** — hizalarsanız dışa aktarım ve birlikte çalışabilirlik bedava gelir |
| **CiTO (SPAR)** | Atıf tipleme ontolojisi | `support_type` enum'unuzun standart karşılığı: `cito:supports`, `cito:disputes`, `cito:extends` |
| RO-Crate | Yayın paketi | WP-090'da zaten var ✅ |
| **Croissant (MLCommons)** | ML dataset metadata | Data Steward (A3) için |
| CITATION.cff + CodeMeta | Yazılım atıfı | RSE (A4) için |
| Zenodo / Software Heritage | Kalıcı arşiv + DOI | "Artifacts Available" rozeti |

## F3. İstatistiksel disiplin ve adli kontrol

| Araç | Görev | Katman |
|---|---|---|
| **statcheck** | Rapor edilen istatistiklerin iç tutarlılığı | **G6 mekanik** |
| **GRIM / GRIMMER / SPRITE** | Ortalama/SD'nin N ile mümkün olup olmadığı | **G6 mekanik** |
| **specr / multiverse / boba** | Specification curve, multiverse analizi | **G6 (B3)** |
| **DABEST** | Etki büyüklüğü + CI (p-değeri yerine) | G6 raporlama |
| PyMC / Stan | Bayesçi belirsizlik | Statistical Methods Owner |
| **p-curve / z-curve** | Bulgu kümesinin kanıtsal değeri | Metascience (C3) |
| scikit-learn `calibration` | İzotonik / Platt kalibrasyonu | **Metascience (C2)** |
| statsmodels / pingouin | Genel istatistik | G6 |

## F4. Tekrar üretilebilirlik

| Araç | Görev |
|---|---|
| **Nix veya Apptainer** | Gerçek bit-düzeyi ortam determinizmi — Docker digest yeterli değil |
| DVC / lakeFS | Veri versiyonlama |
| MLflow | Run registry — planınızda var ✅ |
| **marimo** | Reaktif, git-dostu, deterministik notebook — Jupyter'ın tekrar üretilemezlik problemini çözer |
| sigstore/cosign + in-toto | Artifact imzalama — planınızda var ✅ |
| **Quarto** | Literate publishing, çapraz referans, çok formatlı — **G9 PublicationPackage için ideal** |

## F5. Görselleştirme (özellikle istediğiniz alan)

| Araç | Ne için | Neden bu |
|---|---|---|
| **Vega-Lite** | Tüm istatistiksel grafikler | **Grafik = spec + veri hash'i.** Spec JSON, versiyonlanabilir, diff'lenebilir, tekrar üretilebilir. Mimarinizin manifest felsefesine tam oturur |
| **Observable Framework** | Statik, veri-yönlendirmeli dashboard | Build-time veri, runtime bağımlılığı yok; artifact olarak dondurulabilir |
| **Cytoscape.js / Sigma.js** | Claim–evidence–source grafiği | Ana bilgi görselleştirmeniz bu olacak |
| **Great Tables** | Yayın kalitesinde tablo | G9 |
| **Mermaid** | Mimari/akış diyagramları | Metin tabanlı, git-dostu, Obsidian yerel destekliyor |
| **Kroki** | Çok formatlı diyagram render servisi | Tek servis, birçok diyagram dili |
| **Label Studio** | Evidence span doğrulama arayüzü | **İnsanın span'i onayladığı yer — şu an mimaride bu arayüz yok** |
| **Argilla** | LLM çıktısı review/annotation | Reviewer verdict'lerinin insan kontrolü |
| Perfetto / Jaeger | Trace görselleştirme | OTel korelasyon zinciri |
| Grafana | Operasyonel dashboard | Planınızda var ✅ |

**Görselleştirme için mimari kural önerisi:**

> Her figür bir **artifact**'tır: `{spec_hash, data_hash, renderer_version}`.
> Yayındaki hiçbir figür, manifest'te bu üçlüye sahip olmadan yer alamaz.
> Böylece "figürdeki eğri veriden mi geliyor?" sorusu mekanik olarak
> cevaplanır. `figure_1_digest` alanınız zaten var — bunu spec+data ayrımıyla
> genişletin.

## F6. Model ve ajan altyapısı

| Araç | Görev |
|---|---|
| LiteLLM | Model gateway — planınızda var ✅ |
| **vLLM / llama.cpp** | Yerel open-weight sunum — **R3 için zorunlu (D4)** |
| **Instructor / Outlines** | Yapılandırılmış çıktı zorlaması — serbest metin parse etmeyi bırakın |
| **Inspect (UK AISI)** | Titiz model değerlendirme çerçevesi — **Capability Registry qualification için** |
| **DSPy** | Metrik güdümlü prompt optimizasyonu | Prompt'u elle değil ölçerek iyileştirin |
| promptfoo / DeepEval | Eval pipeline | Golden set (WP-043) |
| Langfuse | LLM trace — planınızda var ✅ |
| **Ragas** | Retrieval kalitesi | G3 kapsam analizi |

## F7. Güvenlik

| Araç | Görev |
|---|---|
| gVisor | Sandbox — planınızda var ✅ |
| **Kata Containers / Firecracker** | Critical profil için gerçek VM izolasyonu (dokümanınız zaten "container değil VM" diyor) |
| **Falco** | Runtime davranış izleme — sandbox kaçış tespiti (ACC-15) |
| **Presidio** | PII tespiti | DLP (ACC-32 secret-in-trace) |
| Trivy / Grype | SBOM + zafiyet | WP-059 |
| **Kyverno** | K8s admission policy | OPA'ya alternatif/tamamlayıcı |
| Vault + SPIFFE/SPIRE | Kimlik — planınızda var ✅ |
| **mitmproxy / Squid+ICAP** | Egress denetimi | WP-057 |

---

# BÖLÜM G — İdeal yapıya göre review: mevcut mimarinin boşlukları

Bölüm A–F'de tanımlanan ideal yapıya göre, mevcut `AIRL-OS-Architecture.md`
v1.0'ın denetimi.

## G1. Kritik boşluklar

| # | Boşluk | Etki | Çözüm |
|---|---|---|---|
| **K1** | **Bağımsızlık ölçülmüyor, varsayılıyor** — `Model Lineage` beyan; hata korelasyonu hiç ölçülmüyor | Tüm G6 kanıt değeri temelsiz. Korelasyonlu iki model hemfikir olunca "bağımsız doğrulama" sayılıyor | **C1 Agreement Calibration** |
| **K2** | **7 confidence skalası ölçüm temelsiz** — üretici kalibre değil, birleştirme kuralı yok | `PR-12 False Rigor`'un tam tanımı. Sistemin en görünür çıktısı en zayıf temelli sayı | **C2 Confidence Calibration** + min-kuralı |
| **K3** | **Laboratuvarın kendi hata oranı bilinmiyor** | Hiçbir metrik "doğru sonuç üretiyor muyuz" sorusunu cevaplamıyor | **C4 Kontrol enjeksiyonu** |
| **K4** | **Yayın yanlılığı açık** — G2 dondurma var ama G8 sonuca bakarak reddedebiliyor | Negatif sonuçlar sistematik olarak kaybolur | **B1 In-principle acceptance** |
| **K5** | **Producer'ın kendi yardımcısını çağırması yasak değil** | IndependenceMatrix yanlış PASS verebilir; diğer 7 boyutun ölçümü geçersizleşir | **E2 Delegation Boundary boyutu** |
| **K6** | **R3 + hosted model = imkânsız G7** | Reproducibility "non-waivable" ama sağlanamaz | **D4 R3 → yerel/open-weight zorunlu** |
| **K7** | **`determine_assurance_class` fail-open** | Eksik risk profili → en hafif sınıf | **E4: eksikse R3, fallthrough R2** |
| **K8** | **Kim insan, kim model belirsiz** | Org chart insan tarif ediyor, RoleContract model. R3'te Human Identity non-compensable → tek kişilik operasyonda tüm R3 kalıcı BLOCKED | **Karar gerekli — A8 tablosu doldurulmalı** |

## G2. Yüksek öncelikli boşluklar

| # | Boşluk | Çözüm |
|---|---|---|
| **Y1** | Analiz planı protokolden ayrı kilitlenmiyor → sonucu görüp karar kuralı değiştirilebilir | **A1 + G2b `AnalysisPlanManifest`** |
| **Y2** | Analist kör değil (yalnız reviewer kör) | **B2 Blinded analysis** |
| **Y3** | `repeatability/reproducibility/replication` tanımsız; tolerans **3 farklı değerde** (±2% / ≥95% / >5%) | **B4 ACM badge + G7a/G7b ayrımı** |
| **Y4** | Fabrication şüphesinin süreci ve sahibi yok | **A2 Research Integrity Officer** |
| **Y5** | Uyuşmazlıkta tek hakem, tur sınırı yok, açık bulgu sessizce kaybolabilir | **B5 Delphi + E3 breaker + FindingLedger** |
| **Y6** | Rubber-stamping'e karşı mekanizma yok (`PR-11` register'da ama mimaride yok) | **C5 Dikkat bütçesi (kota, SLA değil)** |
| **Y7** | Reviewer yalnız aggregate görüyor → seçici dışlama denetlenemez | Dışlama kararları için **ayrı mekanik denetim**; `exclusion_rules` uygulaması hash'lenip pakete konur |
| **Y8** | Gate'lerin hangisinin işe yaradığı ölçülmüyor | **C3 Gate yield** |
| **Y9** | Proje ortasında risk yükseltme mekanizması yok | **E5 RiskReclassificationEvent** |
| **Y10** | Yayın metni ↔ claim kapsamı denetlenmiyor (`obligations` var, denetleyen yok) | **A5 + mekanik scope conformance** |
| **Y11** | Projeler arası hafıza yok | **A7 Knowledge Steward** |
| **Y12** | Zotero grup kütüphanesi = bulut egress; D2+ veri politikası tanımsız | Grup kütüphanesi veri sınıfı tavanı **açıkça** belirlenmeli (öneri: **≤ D1**) |

## G3. Orta öncelikli boşluklar

| # | Boşluk | Çözüm |
|---|---|---|
| **O1** | ExecutionProfile Light için gVisor çelişkisi (§2 "optional" ↔ §9 `gvisor-kvm`) | Tek otoriteli tablo; öneri: **her zaman gVisor**, fark yalnız seccomp profilinde |
| **O2** | `determine_assurance_class` içinde ulaşılamaz kod (`downstream_user_count` bloğu fonksiyon dışında) | Fonksiyona alın |
| **O3** | Stokastik deneyde nokta tahmini % ile karşılaştırılıyor | **Dağılım karşılaştırması** (CI örtüşmesi / eşdeğerlik testi) |
| **O4** | Testin *gücü* sorgulanmıyor | **B9 Severity assessment** |
| **O5** | Kanıtın *tanısallığı* sorgulanmıyor — çok kanıt ≠ ayırt edici kanıt | **B6 ACH matrisi** |
| **O6** | Tek analiz yolu; analitik serbestlik dereceleri ölçülmüyor | **B3 Multi-analyst / multiverse** |
| **O7** | `ReviewPacketBuilder` prompt mu program mı belirsiz | **E1: program, testli allowlist** |
| **O8** | Bütün yayın paketi üzerinde final review yok | **E8-2: en yetenekli modelle whole-package review** |
| **O9** | Üretilen dataset'lerin yaşam döngüsü sahibi yok | **A3 Data Steward + Croissant + DOI** |
| **O10** | Figürlerin tekrar üretilebilirliği tanımsız | **F5: figür = spec_hash + data_hash + renderer_version** |
| **O11** | pdfplumber span anchoring için zayıf | **GROBID** |
| **O12** | Ön-kayıt öncesi hesaplanan sonucun statüsü tanımsız | **E8: `confirmatory` olamaz, `exploratory` olarak raporlanır** |

## G4. Mevcut tasarımın korunması gereken güçlü yanları

Bunlara dokunmayın:

1. **Agent niyet üretir, Broker etki üretir** — yetki genişlemesini mimari kapatıyor
2. **RoleContract ≠ model** — "farklı modeller yürütsün" hedefinin doğru temeli
3. **Re-anchoring cascade** (RELOCATED/AMBIGUOUS/NEEDS_REANCHOR/ORPHANED) — nadir kalitede
4. **412 → reconciliation, körlemesine retry yok** — insan verisini gerçekten koruyor
5. **G10 = Schedule, workflow değil** — replay tuzağından kaçınmış
6. **Child workflow bağımsız versiyonlama** — aynı sebep
7. **Timeout asla auto-approve değil** — fail-closed
8. **Adversarial Reviewer ayrı rol** — çoğu sistemde yok
9. **Neo4j canonical değil, türev** — rebuild edilebilir
10. **Oturumlar birleşebilir, gate kayıtları ayrılır** — Superpowers'ın bağımsız olarak doğruladığı karar
11. **ExecutionProfile 4 eksenli** — "D0 = hafif sandbox" yanılgısını reddetmiş
12. **`SourceRepresentation` versiyonlama + eski hash immutable** — eski kanıt hep doğrulanabilir

---

# BÖLÜM H — Uygulama sırası

Bağımlılığa göre. Her adım `karar` / `mekanik` / `model` olarak işaretli.

## Faz 0 — Kararlar (kod yok, ama her şey buna bağlı)

| # | İş | Tip |
|---|---|---|
| 0.1 | **A8 rol tablosunu doldurun**: her rol insan mı, model mi, mekanik mi, ertelendi mi | `karar` |
| 0.2 | **Model roster'ı**: hangi profil hangi tier'da (D3) | `karar` |
| 0.3 | **R3 kapsamı**: tek kişilik operasyonda R3 mümkün mü? Değilse hangi projeler R3 olabilir? | `karar` |
| 0.4 | **D4 kabulü**: R3 → yerel/open-weight zorunlu | `karar` |
| 0.5 | **B1 kabulü**: G8 sonucun yönüne göre reddedemez | `karar` |
| 0.6 | Grup kütüphanesi veri sınıfı tavanı (öneri ≤ D1) | `karar` |

## Faz 1 — Ucuz mekanik kazançlar (model gerekmez, hemen değer üretir)

| # | İş | Kapattığı |
|---|---|---|
| 1.1 | statcheck + GRIM/GRIMMER pipeline'ı | B7, K2'nin bir kısmı |
| 1.2 | Scope conformance kontrolü (yayın metni ↔ ClaimVersion) | A5, Y10 |
| 1.3 | `ReviewPacketBuilder` programa çevrilir + allowlist testi | E1, O7 |
| 1.4 | `determine_assurance_class` fail-closed + ulaşılamaz kod düzeltmesi | K7, O2 |
| 1.5 | Delegation Boundary boyutu Independence Matrix'e eklenir | **K5** |
| 1.6 | G7a/G7b ayrımı + ACM badge vokabüleri; tolerans çelişkisi çözülür | **Y3** |
| 1.7 | `progress.jsonl` makine-okunur defter | E7 |

## Faz 2 — Ön-kayıt disiplini

| # | İş | Kapattığı |
|---|---|---|
| 2.1 | `AnalysisPlanManifest` ayrı nesne + ayrı kilit | **Y1** |
| 2.2 | `InPrincipleAcceptance` (G2 Stage-1) | **K4** |
| 2.3 | exploratory / confirmatory etiketlemesi zorunlu | O12, E8 |
| 2.4 | Severity assessment alanı | O4 |
| 2.5 | Pre-mortem G4 öncesi zorunlu | B8 |

## Faz 3 — Metascience düzlemi

| # | İş | Kapattığı |
|---|---|---|
| 3.1 | Agreement calibration set + κ/ρ ölçümü | **K1** |
| 3.2 | Confidence kalibrasyonu: raw + calibrated + `UNCALIBRATED` durumu | **K2** |
| 3.3 | Kontrol enjeksiyonu (pozitif/negatif, ajanlardan gizli) | **K3** |
| 3.4 | İnsan dikkat bütçesi + telemetri | **Y6** |
| 3.5 | Gate yield ölçümü | Y8 |
| 3.6 | Claim survival zaman serisi (G10 verisinden) | C6 |

## Faz 4 — Gelişmiş review mekanizmaları

| # | İş | Kapattığı |
|---|---|---|
| 4.1 | Delphi turları + FindingLedger + breaker | **Y5** |
| 4.2 | Multi-analyst (N bağımsız analiz ajanı) | O6 |
| 4.3 | ACH tanısallık matrisi | O5 |
| 4.4 | Blinded analysis | **Y2** |
| 4.5 | Multiverse / specification curve | O6 |
| 4.6 | Whole-package final review | O8 |

## Faz 5 — Roller ve süreç

| # | İş |
|---|---|
| 5.1 | Research Integrity Officer + `IntegrityCase` yaşam döngüsü (**Y4**) |
| 5.2 | Statistical Methods Owner yetkileri (**A1**) |
| 5.3 | Data Steward + Croissant + DOI (**O9**) |
| 5.4 | RSE + RO-Crate + Nix/Apptainer (**A4**) |
| 5.5 | Knowledge Steward + projeler arası çelişki tespiti (**Y11**) |
| 5.6 | `RiskReclassificationEvent` (**Y9**) |

---

## Kapanış

Mevcut mimariniz, AI ile yürütülen bir araştırma laboratuvarı için gördüğüm en
eksiksiz yönetişim tasarımlarından biri. Otorite bölüşümü, broker deseni ve
re-anchoring cascade'i gerçekten iyi.

Eksik olan tek şey **dönüşlülük** (reflexivity): sistem araştırmayı denetliyor
ama kendini denetlemiyor. Ve model tarafından yürütülen bir laboratuvarda bu,
isteğe bağlı bir ekleme değil — **çünkü bağımsız insan hakemin yerini alan şey,
korelasyonlu olabilecek modellerdir ve bu korelasyon ölçülmediği sürece tüm
kanıt zinciri varsayıma dayanır.**

7. düzlem (Bölüm C) bunu kapatır. Faz 1'deki yedi mekanik kazanç ise model
gerektirmez, ucuzdur ve hemen değer üretir — oradan başlayın.

---

**Devamı:** Bu belge *ne* eklenmesi gerektiğini tanımlar. Bunların ajanlar
tarafından *nasıl* yürütüleceği — skill katmanı, demir kurallar, rasyonalizasyon
tabloları, eskalasyon merdiveni ve `ProducerResponse` — kardeş belgede:
[[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer|AIRL-OS Skill Layer]]
