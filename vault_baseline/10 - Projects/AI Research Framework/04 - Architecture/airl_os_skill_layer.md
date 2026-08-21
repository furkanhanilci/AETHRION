# AIRL-OS Skill Layer — `obra/superpowers` Tam Entegrasyon Raporu

| Alan | Değer |
|---|---|
| Belge tipi | Mimari katkı — operasyonel katman tasarımı |
| Kaynak | `github.com/obra/superpowers` (14 skill, tamamı okundu) |
| Hedef | `AIRL-OS-Architecture.md` v1.0 |
| Kardeş belge | [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS İdeal Yapı]] (roller, review mekanizmaları, metascience) |
| Tarih | 2026-08-22 |
| Durum | Öneri — insan kararı bekliyor |

---

## 0. Tek cümlelik teşhis

> **AIRL-OS `RoleContract` ile bir ajanın *kim* olduğunu tanımlıyor.
> Ama *nasıl çalışacağını* hiçbir yerde tanımlamıyor.**
>
> Superpowers tam olarak o eksik yarıyı çözüyor — ve deneysel olarak
> doğrulanmış bir yöntemle çözüyor.

Mevcut `RoleContract`'ınıza bakalım:

```yaml
RoleContract:
  role: "Evidence Extractor"
  purpose: "Hangi kaynaktan hangi claim için kanıt bulunacağını belirlemek"
  inputs: [claim_candidates, source_candidates]
  outputs: [evidence_spans]
  tools_allowed: [pdf_annotate, text_similarity, citation_parse]
  data_classes_read: [D0, D1, D2]
  independence_requirements: [...]
  budget: {...}
  success_criteria: [span_coverage >= 0.95, false_positive_rate <= 0.05]
```

Burada olan her şey **sınır**: kim, ne okuyabilir, ne kadar harcayabilir, ne
üretmeli. Olmayan tek şey: **prosedür**. Evidence Extractor'ın *hangi adımları,
hangi sırayla, hangi doğrulamalarla* yapacağı yazılı değil. O boşluk şu anda
prompt'la doluyor — yani versiyonlanmayan, test edilmeyen, denetlenemeyen bir
katmanla.

Superpowers'ın çözümü: **Skill**.

---

## 1. Kavramsal yerleştirme: Skill katmanı nereye oturuyor

```
┌─────────────────────────────────────────────────────────────┐
│ RoleContract Registry        ← KİM (kimlik, yetki, bütçe)   │  MEVCUT ✅
├─────────────────────────────────────────────────────────────┤
│ ►► SKILL REGISTRY ◄◄         ← NASIL (prosedür, tetikleyici,│  EKSİK ⚠️
│                                 demir kural, doğrulama)      │
├─────────────────────────────────────────────────────────────┤
│ Task Compiler                ← BAĞLAMA (rol + skill + proje)│  MEVCUT ✅
├─────────────────────────────────────────────────────────────┤
│ TaskContract                 ← ÇALIŞTIRILABİLİR GÖREV        │  MEVCUT ✅
├─────────────────────────────────────────────────────────────┤
│ LangGraph Runtime            ← YÜRÜTME                       │  MEVCUT ✅
└─────────────────────────────────────────────────────────────┘
```

**Skill nedir:** Tetikleyici koşulları, prosedürü, demir kuralı, doğrulama
adımlarını ve *bilinen kaçamak gerekçelerini* içeren, versiyonlanmış,
test edilmiş bir davranış birimi.

**Neden `RoleContract`'ın içine gömülmemeli:**
- Bir skill **birden çok rol** tarafından kullanılır (`verification-before-completion` herkeste)
- Bir rol **birden çok skill** kullanır (Evidence Extractor: `extracting-evidence` + `anchoring-spans` + `verification-before-completion`)
- Skill'ler **tetikleyiciyle** yüklenir, rolle değil ("belirsiz bir anomali gördüğünde `investigating-anomalies` yükle")
- Skill'ler **bağımsız versiyonlanır ve test edilir**

**Ve `TaskContract`'a alan eklemesi:**

```yaml
TaskContract:
  # ... mevcut alanlar ...
  skills_loaded:                                    # ← YENİ
    - "airl:extracting-evidence@2.1.0"
    - "airl:anchoring-spans@1.4.0"
    - "airl:verification-before-completion@3.0.0"
  skill_bundle_hash: "sha256:..."                   # ← YENİ, denetlenebilir
```

Böylece "bu ajan hangi kurallarla çalıştı?" sorusu **kanıt zincirine girer.**
Şu anda bu bilgi hiçbir yerde tutulmuyor — bir claim üretildikten sonra, onu
üreten ajanın hangi prosedürü izlediğini geriye dönük olarak bilemezsiniz.

---

## 2. Superpowers'ın asıl katkısı: skill'lerin nasıl *yazıldığı*

Skill kataloğu ikinci derecede önemli. **Asıl katkı meta-yöntem.**

### 2.1 Demir Kural: "NO SKILL WITHOUT A FAILING TEST FIRST"

Superpowers'ta bir skill şöyle üretilir:

```
RED:      Skill OLMADAN baseline senaryoyu çalıştır.
          Ajanın nasıl başarısız olduğunu ve HANGİ GEREKÇELERİ ÜRETTİĞİNİ
          KELİMESİ KELİMESİNE kaydet.

GREEN:    O SPESİFİK başarısızlıkları kapatan minimum skill'i yaz.
          Yeniden test et — uyum sağlıyor mu?

REFACTOR: Yeni kaçamak gerekçeleri bul, açıkça kapat, tekrar test et.

İstisna yok: "basit ekleme", "güncelleme", "test edilmemiş küçük düzeltme" —
test edilmemiş iş silinir ve yeniden başlanır.
```

**Bu neden AIRL-OS için kritik:**

Sizin `non-waivable blocker` listeniz var. Ama **bir ajanın onu aşmaya
çalışırken üreteceği gerekçelere karşı hiçbir savunma yok.** "Non-waivable"
yazmak, bir modelin onu aşmayacağı anlamına gelmiyor — model her zaman
makul görünen bir gerekçe üretebilir:

> *"Bu durumda reproduction teknik olarak mümkün değil çünkü ortam değişti;
> ancak sonuçlar tutarlı olduğu için kanıt yeterli sayılabilir."*

Superpowers'ın cevabı: **rasyonalizasyon tablosu.** Baseline testinde ajanın
gerçekten ürettiği kaçamaklar, kelimesi kelimesine, ve her birine açık bir
karşı-hüküm.

### 2.2 Rasyonalizasyon tablosu — AIRL-OS'a uyarlanmış örnek

`preregistration-discipline` skill'i için:

| Ajanın ürettiği gerekçe | Hüküm |
|---|---|
| "Analiz planı zaten protokolde ima ediliyor" | **HAYIR.** İma ≠ kilit. `AnalysisPlanManifest` ayrı bir hash'tir. Yoksa `confirmatory` iddia üretilemez. |
| "Sonucu görmeden hangi testin uygun olduğunu bilemezdim" | **Doğru — ve tam olarak bu yüzden `exploratory`.** Etiketle, devam et. |
| "Bu yalnız küçük bir kovaryat eklemesi" | **Küçük değişiklik diye bir şey yok.** Plan sonrası her değişiklik `exploratory`. |
| "Ön analiz keşifsel amaçlıydı, asıl analiz plana uygun" | **Keşif verisi asıl analizle aynı veriden geldiyse bağımsız değildir.** İkisi de `exploratory`. |
| "Zaman baskısı var, plan sonradan yazılabilir" | **Zaman baskısı bir gerekçe değildir.** Plan kilitlenmeden G5 başlamaz. |

Bu tablo **uydurulmaz** — baseline testinde ajanların gerçekten ürettiği
gerekçelerden derlenir. Bu, "non-waivable" ifadesini beyandan **uygulanabilir
kurala** çeviren tek mekanizma.

### 2.3 Tetikleyici disiplini — ince ama kritik bir bulgu

Superpowers'ın deneysel olarak keşfettiği bir hata modu:

> **`description` alanı prosedürü özetlerse, ajan skill'i okumak yerine
> özeti izler.**
>
> Gerçek vaka: "code review between tasks" diyen bir açıklama, ajanın **bir**
> review yapmasına yol açtı — skill'in akış şeması **iki** review gerektirdiği
> halde.

**Kural:** `description` **yalnız tetikleyici koşulu** anlatır, asla prosedürü.

- ✅ `"Use when tests have race conditions, timing dependencies, or pass/fail inconsistently"`
- ❌ `"Use for TDD — write test first, watch it fail, write minimal code, refactor"`

**AIRL-OS'a doğrudan uygulaması:** `RoleContract.purpose` alanınız şu anda
prosedür özetliyor:

```yaml
purpose: "Hangi kaynaktan hangi claim için kanıt bulunacağını belirlemek"
```

Bu bir *prosedür* tarifi. Ajan bunu okuyup skill'i atlayabilir. Ayrılmalı:

```yaml
role: "Evidence Extractor"
triggers: "Bir ClaimCandidate için henüz EvidenceSpan'i olmayan
           SourceRepresentation mevcut olduğunda"
skills: ["extracting-evidence@2.1.0", "anchoring-spans@1.4.0"]
```

### 2.4 Token bütçesi — ve bir bulgu

Superpowers'ın limitleri: getting-started `<150 kelime`, sık yüklenen
`<200 kelime`, diğerleri `<500 kelime`.

**Bulgu:** `planning/commissioning/` içindeki 130 WP dosyası ortalama
**677 kelime** ve **%59,2'si 130 dosyada aynen tekrar eden şablon**
(ölçüldü). Yani:

> **Commissioning planınız ajan tarafından tüketilebilir değil.** İnsan
> belgesi olarak iyi; ajan bağlamı olarak kötü — her yüklemede ~400 kelime
> şablon gürültüsü taşıyor ve gerçek talimat yoğunluğu düşük.

Model tarafından yürütülecek bir laboratuvarda bu, **makine-tüketilebilir bir
projeksiyon** gerektirir: her WP için tetikleyici + demir kural + doğrulama
adımı içeren, şablonsuz, `<500` kelimelik bir skill/task-brief.

Superpowers'ın çözümü zaten hazır: `scripts/task-brief` — planı **mekanik
olarak** çıkarır, prompt'la özetlemez. Bu, sizin `ReviewPacketBuilder`
tartışmanızla aynı ilke: **program, prompt değil.**

---

## 3. Skill anatomisi — AIRL-OS uyarlaması

Superpowers'ın `SKILL.md` şemasına, AIRL-OS'un ihtiyaç duyduğu alanları
ekliyorum (**kalın** olanlar eklendi):

```markdown
---
name: extracting-evidence
version: 2.1.0
description: Use when a ClaimCandidate exists without a linked EvidenceSpan
             and at least one SourceRepresentation is available
                                          # SADECE TETİKLEYİCİ — prosedür yok

gates: [G3, G6]                           # ← EKLENDİ: bağlı gate'ler
roles: [Evidence Extractor]               # ← EKLENDİ: bağlı roller
assurance_classes: [R1, R2, R3]           # ← EKLENDİ: hangi sınıflarda zorunlu
non_waivable: false                       # ← EKLENDİ
data_class_ceiling: D2                    # ← EKLENDİ
requires_skills:                          # ← EKLENDİ: bileşim
  - anchoring-spans
  - verification-before-completion
emits:                                    # ← EKLENDİ: canonical çıktı
  - EvidenceSpan
  - ToolReceipt
mechanical_checks:                        # ← EKLENDİ: model yargısı gerektirmeyen
  - span_resolves_in_representation
  - quote_exact_match
tested_against: baselines/extracting-evidence/  # ← EKLENDİ: RED senaryoları
---

# Extracting Evidence

## Genel ilke
[1–2 cümle]

## Ne zaman kullanılır / kullanılmaz
[belirtiler listesi]

## Demir kural
[varsa — tek cümle, istisnasız]

## Prosedür
[adımlar, her adımda doğrulama]

## Mekanik doğrulama
[model yargısı olmadan çalışan kontroller]

## Rasyonalizasyon tablosu
| Gerekçe | Hüküm |

## Kırmızı bayraklar
[bu skill'in atlandığını gösteren işaretler]
```

**Dizin:**

```
skills/
  <skill-name>/
    SKILL.md              # zorunlu, <500 kelime
    procedure.md          # 100+ satırlık ağır referans (opsiyonel)
    checks/               # mekanik kontrol scriptleri
    baselines/            # RED senaryoları — skill'in kendi testleri
```

**Bileşim kuralı** (Superpowers'tan aynen): bağımlı skill'e **referans ver,
gömme.**
- ✅ `**GEREKLİ ARKA PLAN:** airl:anchoring-spans skill'ini anlamış olmalısın`
- ❌ `@skills/anchoring-spans/SKILL.md` — bağlamı anında yakar

---

## 4. AIRL-OS Skill Kataloğu

Superpowers'ın 14 skill'inin tamamı + araştırma alanına özgü eklemeler.
**A) Meta**, **B) Disiplin**, **C) Süreç**, **D) Review**, **E) Araştırma**,
**F) Metascience**.

### A. Meta skill'ler

| Skill | Superpowers karşılığı | Görev |
|---|---|---|
| `using-airl-os` | `using-superpowers` | Giriş noktası; hangi durumda hangi skill |
| `writing-skills` | `writing-skills` | Skill yazma disiplini — **RED/GREEN/REFACTOR, rasyonalizasyon tablosu zorunlu** |

### B. Disiplin skill'leri (demir kurallı — baskı altında test edilir)

| Skill | Demir kural | Superpowers kaynağı |
|---|---|---|
| **`preregistration-discipline`** | **ÖN-KAYIT KİLİTLENMEDEN CONFIRMATORY İDDİA ÜRETİLEMEZ.** Plan kilitlenmeden hesaplanan her sonuç `exploratory` olarak yeniden etiketlenir — istisna yok. | `test-driven-development` (doğrudan uyarlama) |
| **`verification-before-completion`** | **TAZE DOĞRULAMA KANITI OLMADAN "TAMAMLANDI" DENMEZ.** Hafızadan, önceki koşudan veya ajan raporundan alıntı kanıt değildir. | `verification-before-completion` (birebir) |
| **`evidence-before-claim`** | **HER İDDİA CÜMLESİ BİR `EvidenceSpan`'e ÇÖZÜLMELİDİR.** Çözülemeyen cümle yayınlanamaz. | *(yeni — araştırmaya özgü)* |
| **`scope-discipline`** | **METİN, `ClaimVersion.scope_qualification`'ı AŞAMAZ.** Mekanik olarak kontrol edilir. | *(yeni)* |
| **`independence-discipline`** | **PRODUCER KENDİ DOĞRULAYICISINI VEYA YARDIMCISINI ÇAĞIRAMAZ.** | `subagent-driven-development` ("the implementer never dispatches subagents") |

`verification-before-completion`'ın AIRL-OS'a birebir çevirisi:

```
1. İddiayı kanıtlayacak komutu BELİRLE
2. Komutu TAZE çalıştır (hafızadan değil)
3. Tam çıktıyı OKU — exit code, hata sayısı
4. Çıktının iddiayı gerçekten desteklediğini DOĞRULA
5. Kanıtı iddiaya EKLİ olarak RAPORLA

Yasak ifadeler (doğrulamadan önce):
  "çalışmalı", "muhtemelen doğru", "görünüşe göre", "Harika!", "Mükemmel!"
  ve ajan raporuna bağımsız doğrulama olmadan güvenmek
```

Bu, sizin `TECH_COMPLETE ≠ ACCEPTED` ayrımınızın **operasyonel** hali. Ayrım
kavramsal olarak var ✅, ama uygulayan bir kural yok.

### C. Süreç skill'leri

| Skill | Superpowers karşılığı | AIRL-OS'ta ne yapar |
|---|---|---|
| `framing-research` | `brainstorming` | **Sınıflandırma önce:** `Spike / Bounded / Architectural` → AIRL karşılığı `Exploratory / Replication / Confirmatory`. **"Şüphedeyken ağır olanı seç."** Onay kapısı asla kaybolmaz, yalnız töreni küçülür. |
| `writing-protocols` | `writing-plans` | `ProtocolManifest` yazımı: **placeholder yasak** ("TBD", "edge case'leri ele al", "Task N'e benzer"), her adımda tam değer ve doğrulama, tip tutarlılığı, öz-review kontrol listesi |
| `writing-analysis-plans` | *(yeni)* | `AnalysisPlanManifest` — protokolden **ayrı kilit** |
| `executing-experiments` | `executing-plans` | Toplu yürütme + kontrol noktaları |
| `agent-driven-research` | `subagent-driven-development` | **Bu belgenin merkezi** — Bölüm 5 |
| `dispatching-parallel-analysts` | `dispatching-parallel-agents` | Multi-analyst fan-out disiplini — Bölüm 6 |
| `using-isolated-environments` | `using-git-worktrees` | İzole çalışma alanı + **temiz baseline doğrulaması**; "harness ile savaşma" |
| `finishing-a-project` | `finishing-a-development-branch` | Kapanış kontrol listesi + **insan menüsü** — Bölüm 7 |

### D. Review skill'leri

| Skill | Superpowers karşılığı | Not |
|---|---|---|
| `requesting-review` | `requesting-code-review` | **Standalone paket, oturum geçmişi asla.** Severity: Critical / Important / Minor. Çıktı: Güçlü yanlar → Bulgular (severity'ye göre) → Değerlendirme |
| **`receiving-review`** | `receiving-code-review` | **Sizde hiç yok — Bölüm 8** |
| `blind-reviewing` | *(yeni)* | Frozen packet, producer trace'i yok |
| `adversarial-reviewing` | *(yeni)* | ACH + tanısallık matrisi |
| `arbitrating-disagreement` | *(yeni + `subagent-driven-development` breaker'ı)* | Delphi turları + breaker |

### E. Araştırma alanı skill'leri

| Skill | Görev |
|---|---|
| `investigating-anomalies` | `systematic-debugging`'in araştırma karşılığı — Bölüm 9 |
| `investigating-integrity-concerns` | RIO süreci; `IntegrityCase` yaşam döngüsü |
| `searching-literature` | Arama protokolü, çok kaynaklı keşif |
| `screening-sources` | Dahil/hariç kriterleri, aktif öğrenme (ASReview) |
| `extracting-evidence` | Span çıkarımı |
| `anchoring-spans` | W3C multi-selector, re-anchoring |
| `curating-zotero` | İki-kütüphane modeli, 412 uzlaştırma |
| `building-review-packets` | ReviewPacketBuilder — **program, prompt değil** |

### F. Metascience skill'leri

| Skill | Görev (bkz. [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS İdeal Yapı]] Bölüm C) |
|---|---|
| `calibrating-confidence` | Brier skoru, izotonik kalibrasyon, `UNCALIBRATED` durumu |
| `measuring-agreement` | κ / hata korelasyonu → bağımsızlık kotası |
| `injecting-controls` | Pozitif/negatif kontrol enjeksiyonu (ajanlardan gizli) |

---

## 5. `agent-driven-research` — merkezi skill

Superpowers'ın `subagent-driven-development` skill'i, sizin en büyük
operasyonel boşluğunuzu kapatıyor. Dört mekanik:

### 5.1 Bilgi asimetrisi — dosya seviyesinde

| | Producer görür | Reviewer görür |
|---|---|---|
| Task brief / ProtocolManifest | ✅ | ✅ |
| Önceki task'ların **arayüzleri** | ✅ | — |
| Global kısıtlar (spec'ten **kelimesi kelimesine**) | ✅ | ✅ |
| Producer'ın raporu | yazar | ✅ |
| Üretilen artifact / diff | üretir | ✅ |
| **Producer'ın iç muhakemesi** | — | ❌ **asla** |
| Oturum geçmişi | ❌ | ❌ |

**Sizin `ReviewPacket.excluded_from_packet` listeniz aynı fikirde ✅.**
Eklenmesi gereken iki kural:

1. **"No context pasting"** — reviewer'a inline metin geçilmez, yalnız
   **dosya yolu + hash**. Böylece `evidence_packet_hash` gerçekten
   denetlenebilir olur.
2. **Global kısıtlar spec'ten mekanik olarak kopyalanır**, özetlenmez.

### 5.2 Sınırlı eskalasyon merdiveni + "the breaker"

Superpowers'ın uyuşmazlık çözümü — **sizde bu yok**:

```
Tur 1–3:  AYNI producer'a dön. Bağlamı korunur.
          Açık bulgular KELİMESİ KELİMESİNE iletilir (özetlenmez).
          Düzeltme raporu AYNI rapor dosyasına EKLENİR (kalıcı hafıza).
          Yalnız değişen kısım yeniden review edilir (FIX_BASE → HEAD).

Tur 4–5:  TAZE producer, DAHA YETENEKLİ model.
          Açık çerçeveleme: "Önceki producer bunu N kez denedi; artık senin."

Tur 5 sonu hâlâ açıksa → BREAKER:
          Dispatch DURUR.
          İnsan her açık bulguyu TEK TEK hükme bağlar.
          Her hüküm deftere yazılır.
          ►► SESSİZ İSKARTA YASAK ◄◄
```

**Sizin `DisagreementCase`'inizde eksik olanlar:**
- Tur sınırı yok
- Model tier yükseltmesi yok
- "Bulgular kelimesi kelimesine iletilir" kuralı yok
- **Ve en önemlisi: açık bulguların sessizce kaybolmamasının garantisi yok**

`06_KANIT_VE_KABUL_STRATEJISI.md`'deki finding yaşam döngünüz
(`REPORTED → … → CLOSED`) doğru — ama **turlu eskalasyona bağlı değil** ve
her turda "bu bulgu ne oldu?" sorusu zorunlu kılınmıyor.

**Eklenecek:**

```yaml
DisagreementCase:
  # ... mevcut alanlar ...
  round: 3                          # ← YENİ
  max_rounds: 5                     # ← YENİ
  escalation_tier: "fresh_producer_higher_model"   # ← YENİ
  finding_ledger:                   # ← YENİ — her bulgu bir satır
    - finding_id: "F-012"
      status: "OPEN"                # OPEN | RESOLVED | PARKED
      rounds_seen: [1, 2, 3]
      # PARKED ise ZORUNLU:
      parked_rationale: null
      parked_owner: null
      parked_expiry: null
  breaker_invoked: false            # ← YENİ
```

**Kural:** `DisagreementCase` yalnızca `finding_ledger`'daki her satır
`RESOLVED` veya (gerekçe + sahip + süre ile) `PARKED` olduğunda kapanabilir.
Statüsüz bulgu ile kapanış **yasak**.

### 5.3 Dispatch tekliği

| Kural | AIRL-OS karşılığı |
|---|---|
| Task başına **taze** subagent | Context Isolation ✅ (mevcut) |
| Task başına **tek** implementasyon dispatch'i (paralel producer yok — çakışma) | ⚠️ eksik |
| Küçük, aynı şekilli işler **tek dispatch'te toplanır** | ⚠️ eksik |
| **Producer asla subagent çağırmaz** | ❌ **eksik — kritik** |

### 5.4 Defter tabanlı kurtarma

Bağlam sıkışırsa: `progress.md` tamamlanan işleri, git commit'leri verir.
**Deterministik kurtarma.**

Sizin `implementation_log.md`'niz aynı fikirde ✅ ama **serbest metin** — bir
ajan güvenilir ayrıştıramaz.

**Eklenecek:** `progress.jsonl` (append-only, makine-okunur):
```json
{"step_id":"S-041","wp_ids":["WP-011"],"status":"TECH_COMPLETE",
 "target_sha":"6c849bd","evidence_manifest":"delivery/WP-011/em.json",
 "skills":["airl:writing-protocols@1.2.0"],"ts":"2026-08-22T00:05:00+03:00"}
```

---

## 6. `dispatching-parallel-analysts` — multi-analyst disiplini

Superpowers'ın fan-out kuralları, [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS İdeal Yapı]] Bölüm B3'teki
**multi-analyst** önerisinin operasyonel karşılığı:

| Superpowers kuralı | AIRL-OS uygulaması |
|---|---|
| Yalnız **bağımsız** problem alanlarında fan-out | Analiz yolları gerçekten bağımsız mı? Nedensel bağlıysa paralelleştirme |
| Her ajan **dar kapsam** + **kendi kendine yeten** prompt | Her analist aynı `AnalysisPlanManifest`, farklı model ailesi, **birbirini görmez** |
| "Diğer kodu değiştirme" kısıtı | "Diğer analistlerin çıktısını görme/kullanma" |
| Sonuçları birleştirirken **çakışma kontrolü** | Sonuç **dağılımı** — yakınsama mı, sapma mı |
| Tam test paketi + spot-check | Sapma genişse → `claim.confidence` DÜŞER + `scope_qualification` zorunlu |

**Ve ters okuma — bu bir metascience sinyali:**

> Bağımsız analistlerin **çok hızlı yakınsaması** da alarmdır. Gerçekten
> bağımsız yargıçlarda κ ≈ 1,0 beklenmez. Ya görev trivialdir ya da
> bağımsızlık gerçek değildir.

---

## 7. `finishing-a-project` — kapanış disiplini

Superpowers'ın branch kapatma skill'i, G8/G9'a doğrudan uyarlanır:

```
1. Tam doğrulama paketini çalıştır → HERHANGİ BİRİ KIRMIZIYSA DUR
2. Ortam durumunu yakala (hangi target, hangi ortam)
3. Baz referansı doğrula (hangi manifest'ten türedi)
4. İNSANA MENÜ SUN
5. Seçimi uygula
6. Temizlik
```

**İki kural aynen alınmalı:**

1. **"Tests are non-negotiable."** Doğrulama kırmızıysa menü **hiç
   gösterilmez.** Sizin G8'inizde bu var (non-waivable blocker) ✅ ama
   *kapanış kontrol listesi* olarak formüle edilmemiş.

2. **Kelimesi kelimesine onay:**
   > *"Even phrases like 'Yeah, get rid of it' don't authorize deletion;
   > only the typed word `discard` does."*

   AIRL-OS karşılığı — **yıkıcı işlemler için tam kelime onayı zorunlu:**
   - Claim geri çekme → `RETRACT`
   - Yayın supersede → `SUPERSEDE`
   - Proje iptali → `ABANDON`
   - Literature set çözme → `UNFREEZE`

   "Tamam kaldır", "olur iptal et" **yetki değildir.** Bu, sizin
   `ACC-25 Human Approval Forgery` senaryonuzun önleyici tarafı.

---

## 8. `receiving-review` — sizde tamamen eksik olan halka

**Bulgu:** Mimarinizde `ReviewVerdict` var, `DisagreementCase` var, ama
**producer'ın review'a verdiği yanıt modellenmemiş.**

Somut boşluk:

```
Blind Reviewer A: CONDITIONAL_PASS
  conditions:
    - "Claim'i 'senkron varsayım altında' diye nitelendir"
    - "Asenkron durum için test ekle"

→ Sonra ne oluyor?
   Producer koşulları kabul etti mi?
   İtiraz etti mi?
   Kim koşulların yerine getirildiğini DOĞRULADI?
   Yerine getirilmediyse claim yine de G8'e gidebilir mi?

   Mimaride bu soruların HİÇBİRİNİN cevabı yok.
```

Superpowers'ın `receiving-code-review` skill'i bunu tam olarak çözüyor:

### 8.1 Yanıt çerçevesi

```
Oku → Anla → DOĞRULA → Değerlendir → Yanıtla → Uygula
```

> *"Verify before implementing. Ask before assuming.
> Technical correctness over social comfort."*

### 8.2 İtiraz meşrudur (ve teşvik edilir)

Producer şu durumlarda **itiraz etmelidir**:
- Geri bildirim mevcut çalışan davranışı bozuyorsa
- Reviewer tam bağlama sahip değilse
- YAGNI ihlali ise
- Mimari kararla çelişiyorsa
- Teknik olarak yanlışsa

> *"Use technical reasoning, not defensiveness. Reference working tests/code."*

**Neden bir AI laboratuvarında kritik:** Modeller **sycophantic**. İtiraz
etmeleri gereken yerde katılırlar. Eğer producer'ın itiraz hakkı açıkça
tanımlanmazsa, review süreci bir "onay teatrosu"na dönüşür — reviewer bir şey
söyler, producer katılır, kimse öğrenmez. Bu, `PR-11` rubber-stamping'in
ajan tarafındaki eşdeğeri.

### 8.3 Yasak: performatif katılım

> *"Never give performative responses like 'Great point!' or 'You're absolutely
> right!' — actions demonstrate comprehension instead."*

Bu doğrudan bir LLM hata modu ve `ReviewVerdict` yanıtlarında yasaklanmalı.

### 8.4 Belirsizlikte DUR

> *"If any item is unclear: STOP — do not implement anything yet."*

Sıra: **önce tüm belirsizlikleri gider** → bloke edici sorunlar → basit
düzeltmeler → karmaşık düzeltmeler → her birini ayrı test et → regresyon kontrolü.

### 8.5 Eklenecek nesne

```yaml
ProducerResponse:                          # ← YENİ CANONICAL NESNE
  response_id: "resp-2026-08-001"
  verdict_id: "verdict-2026-08-reviewer-a-001"
  responder: "<producer role/model profile>"
  response_date: "..."

  per_condition:
    - condition_id: "C-01"
      stance: "ACCEPTED"          # ACCEPTED | DISPUTED | CLARIFICATION_NEEDED
      action_taken: "claim-v3 üretildi, scope 'senkron' ile nitelendirildi"
      evidence_ref: "claim-v3-2026-08-001"
      verified_by: "mechanical:scope-conformance"     # KİM doğruladı
    - condition_id: "C-02"
      stance: "DISPUTED"
      technical_rationale: "Asenkron test G2 protokol kapsamı dışında;
                            kapsam genişletmesi yeni ProtocolManifest gerektirir"
      escalated_to: "DisagreementCase disagree-2026-08-001"

  # ZORUNLU BÜTÜNLÜK KURALI:
  # Her condition'ın bir stance'i olmak zorunda.
  # Cevapsız condition ile G8'e geçiş YASAK.
```

**Ve gate kuralı:** `ReviewVerdict.decision == CONDITIONAL_PASS` ise, G8'e
geçiş için her `condition` ya `ACCEPTED` + **bağımsız doğrulanmış** ya da
`DISPUTED` + **DisagreementCase'e bağlanmış** olmalıdır.

Bu tek ekleme, review sürecinizde şu anda açık olan en büyük deliği kapatıyor.

---

## 9. `investigating-anomalies` — `systematic-debugging`'in araştırma karşılığı

Superpowers'ın 4 fazlı kök neden analizi, deneysel anomalilere doğrudan uyarlanır.

**Demir kural:** *"NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"*

AIRL-OS karşılığı: **ANOMALİ, KÖK NEDENİ ANLAŞILMADAN "DÜZELTİLEMEZ" VEYA
DIŞLANAMAZ.**

Bu, `ProtocolManifest.exclusion_rules`'unuzla doğrudan ilgili:
*"Outliers > 3σ from median excluded"* — kök neden anlaşılmadan uygulanan bir
dışlama kuralı, veri temizliği değil **sonuç şekillendirmedir**.

| Faz | Superpowers (kod) | AIRL-OS (araştırma) |
|---|---|---|
| **1. Kök neden** | Hata mesajını tam oku, tutarlı yeniden üret, son değişiklikleri kontrol et, sınırlara log ekle, veri akışını geriye izle | Anomaliyi **yeniden üret**, çalıştırma bağlamını (seed, ortam, sürüm) kontrol et, pipeline sınırlarına ölçüm ekle, veriyi kaynağa kadar geriye izle |
| **2. Örüntü analizi** | Benzer çalışan kodu bul, referansı **tam** oku, tüm farkları listele | Aynı koşulun **çalışan** koşumlarını bul, tüm farkları listele (seed, düğüm, sürüm, veri dilimi) |
| **3. Hipotez** | "X kök nedendir çünkü Y". **En küçük** değişiklikle test et. Başarısızsa **yeni hipotez** — üst üste düzeltme ekleme | Aynen. Ve hipotez **ön-kayıtlı** olmalı; anomali araştırması `exploratory` etiketiyle yürür |
| **4. Uygulama** | Önce başarısız test, sonra **tek** düzeltme, regresyon kontrolü | Anomali için **ayrı bir doğrulama koşusu**; ana sonuç kümesine karıştırılmaz |

### 9.1 Üç-düzeltme kuralı — en değerli parça

> *"If three or more fixes fail, stop and question the architecture itself
> rather than continuing to patch."*

**AIRL-OS karşılığı:**

> **Bir anomaliye yönelik üç açıklama girişimi başarısız olduysa, dur.
> Sorgulanacak olan uygulama değil, `ProtocolManifest`'tir.**
>
> → `ProtocolChallenge` açılır → G2'ye geri dönüş değerlendirilir.

Ve Superpowers'ın ikinci sinyali:

> *"Watch for patterns where each fix reveals new problems in different areas —
> this signals fundamental design issues."*

Araştırmada bu **çok tanıdık** bir kalıp: her düzeltme yeni bir anomali
doğuruyorsa, sorun ölçümde değil **modelde/protokoldedir**.

**Sizde şu anda `ProtocolChallenge` diye bir nesne yok.** G2'den sonra
protokolü sorgulamanın tek yolu `material_changes` → yeni `ProtocolManifest`
versiyonu — ama bunu **tetikleyen** bir mekanizma yok. Üç-düzeltme kuralı o
tetikleyicidir.

---

## 10. `preregistration-discipline` — TDD'nin araştırma karşılığı

Superpowers'ın en sert skill'i TDD. AIRL-OS'taki karşılığı bu ve
**laboratuvarınızın bilimsel bütünlüğünün merkezinde** duruyor.

| TDD | Ön-kayıt disiplini |
|---|---|
| **RED:** Önce başarısız test yaz | **FREEZE:** Önce `AnalysisPlanManifest` kilitle — hangi sonucun ne anlama geleceği önceden yazılır |
| Testin **beklenen sebeple** başarısız olduğunu gör | Falsification planı ve stop rule'ların **gerçekten ayırt edici** olduğunu doğrula (severity) |
| **GREEN:** Geçmesi için minimum kod | **EXECUTE:** Plana **tam olarak** uy |
| **REFACTOR:** Testler yeşilken temizle | **REPORT:** Plandan sapmalar **açıkça** raporlanır |
| **Demir kural:** Testten önce yazılan kod **silinir** | **Demir kural:** Plandan önce hesaplanan sonuç `confirmatory` olamaz — `exploratory` olarak yeniden etiketlenir |
| "Referans olarak saklama" yasak | "Ön analiz keşifsel amaçlıydı" gerekçesi yasak |
| Sonradan test yazıp aynı şeymiş gibi davranma yasak | Sonradan plan yazıp ön-kayıtmış gibi davranma yasak (HARKing) |

**Kritik fark ve neden daha da sert olmalı:** Kodda testten önce yazılan kod
*silinebilir*. Araştırmada **sonucu gördükten sonra "görmemiş" olamazsınız.**
Bu yüzden araştırma tarafında ceza silme değil, **kalıcı yeniden
etiketleme**dir: o analiz artık `confirmatory` olamaz, hiçbir zaman.

Ve bu, [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS İdeal Yapı]] Bölüm B1'deki **in-principle acceptance**
ile birleştiğinde yayın yanlılığını kapatır.

**Doğrulama kontrol listesi** (Superpowers'ın formatında):

```
İş tamamlanmadan önce:
  □ Her confirmatory claim için kilitli bir AnalysisPlanManifest var
  □ Plan hash'i sonuç üretiminden ÖNCE kaydedildi (timestamp kanıtı)
  □ Falsification testi severity açısından değerlendirildi
  □ Plandan her sapma raporda listelendi
  □ Ön-kayıt dışı her analiz `exploratory` etiketli
  □ Sonuçlar plan yazımını etkilemedi (kör analiz uygulandıysa kanıtı)

Hepsini işaretleyemiyor musun? Ön-kayıt disiplini atlanmış demektir.
Bu claim `confirmatory` olamaz.
```

---

## 11. Entegrasyon haritası — özet

| Superpowers | AIRL-OS'ta durum | Aksiyon |
|---|---|---|
| Skill kavramı + `SKILL.md` + tetikleyici keşif | ❌ yok | **Skill Registry kur** |
| `writing-skills` (skill için TDD, rasyonalizasyon tablosu) | ❌ yok | **En yüksek meta-değer — kur** |
| Demir kural + kaçamak kapatma | ⚠️ "non-waivable" var, savunma yok | **Rasyonalizasyon tabloları ekle** |
| Tetikleyici ≠ prosedür özeti | ❌ `RoleContract.purpose` prosedür özetliyor | **`triggers` alanına ayır** |
| Token bütçesi | ❌ WP dosyaları %59 şablon, 677 kelime | **Makine-tüketilebilir projeksiyon üret** |
| `test-driven-development` | ❌ | **`preregistration-discipline` olarak ekle** |
| `verification-before-completion` | ⚠️ kavramsal var | **Operasyonel kural olarak ekle** |
| `brainstorming` (sınıflandırma + onay kapısı) | ⚠️ RiskProfile var, "ağır olanı seç" yok | **Fail-closed default ekle** |
| `writing-plans` (placeholder yasağı, öz-review) | ⚠️ ProtocolManifest var | **Placeholder yasağı + öz-review ekle** |
| `subagent-driven-development` — bilgi asimetrisi | ✅ ReviewPacket | **"no context pasting" + hash ekle** |
| `subagent-driven-development` — producer subagent çağıramaz | ❌ **yok** | **Independence 8. boyut — kritik** |
| `subagent-driven-development` — eskalasyon + breaker | ❌ yok | **`DisagreementCase`'e round/ledger/breaker** |
| `requesting-code-review` | ✅ mevcut | severity tier'ları netleştir |
| `receiving-code-review` | ❌ **tamamen yok** | **`ProducerResponse` nesnesi — kritik** |
| `systematic-debugging` + 3-düzeltme kuralı | ❌ yok | **`investigating-anomalies` + `ProtocolChallenge`** |
| `dispatching-parallel-agents` | ❌ yok | **Multi-analyst disiplini** |
| `using-git-worktrees` + temiz baseline | ⚠️ Runtime boyutu var | **Baseline doğrulaması ekle** |
| `finishing-a-development-branch` | ⚠️ G8/G9 var | **Kapanış listesi + tam kelime onayı** |
| Defter tabanlı kurtarma | ⚠️ serbest metin log | **`progress.jsonl`** |

---

## 12. Uygulama sırası

### Faz S0 — Skill altyapısı *(kod, ~1 hafta)*

| # | İş |
|---|---|
| S0.1 | `skills/` dizin yapısı + `SKILL.md` şeması (Bölüm 3) |
| S0.2 | Skill loader + versiyon çözümleme + `skill_bundle_hash` |
| S0.3 | `TaskContract`'a `skills_loaded` + `skill_bundle_hash` alanları |
| S0.4 | `writing-skills` skill'i — **ilk yazılacak skill bu olmalı** (meta-kural) |
| S0.5 | Baseline test koşumu (RED senaryoları) altyapısı |

### Faz S1 — Disiplin skill'leri *(en yüksek getirili)*

| # | Skill | Kapattığı boşluk |
|---|---|---|
| S1.1 | `verification-before-completion` | `TECH_COMPLETE` beyanının operasyonel karşılığı |
| S1.2 | `preregistration-discipline` | HARKing, yayın yanlılığı |
| S1.3 | `independence-discipline` | **Producer'ın subagent çağırması** |
| S1.4 | `evidence-before-claim` + `scope-discipline` | Aşırı genelleme |

Her biri için **önce baseline testi** (RED), sonra skill (GREEN), sonra
rasyonalizasyon tablosu (REFACTOR).

### Faz S2 — Süreç ve review skill'leri

| # | İş |
|---|---|
| S2.1 | `receiving-review` + **`ProducerResponse` canonical nesnesi** |
| S2.2 | `agent-driven-research` + `DisagreementCase` round/ledger/breaker |
| S2.3 | `investigating-anomalies` + `ProtocolChallenge` |
| S2.4 | `framing-research` + fail-closed sınıflandırma |
| S2.5 | `writing-protocols` + `writing-analysis-plans` |
| S2.6 | `finishing-a-project` + tam kelime onayı |

### Faz S3 — Araştırma ve metascience skill'leri

| # | İş |
|---|---|
| S3.1 | `building-review-packets` (program olarak) |
| S3.2 | `dispatching-parallel-analysts` |
| S3.3 | `searching-literature`, `screening-sources`, `extracting-evidence`, `anchoring-spans`, `curating-zotero` |
| S3.4 | `calibrating-confidence`, `measuring-agreement`, `injecting-controls` |

### Faz S4 — Plan projeksiyonu

| # | İş |
|---|---|
| S4.1 | 130 WP → makine-tüketilebilir task-brief üretici (**mekanik, prompt değil**) |
| S4.2 | `progress.jsonl` append-only defter |
| S4.3 | WP ↔ skill eşlemesi (her WP hangi skill'lerle yürütülür) |

---

## 13. En kritik beş çıkarım

1. **`ProducerResponse` yok.** `CONDITIONAL_PASS` verdict'lerinin koşullarının
   yerine getirilip getirilmediğini doğrulayan hiçbir şey yok. Review süreci
   şu anda **açık uçlu**. *(Bölüm 8)*

2. **Producer'ın kendi yardımcısını çağırması yasak değil.** Yasak yoksa
   IndependenceMatrix'in diğer 7 boyutu da geçersizdir. *(Bölüm 5.3)*

3. **"Non-waivable" bir beyandır, savunma değildir.** Model her zaman makul
   bir kaçamak gerekçesi üretebilir. Rasyonalizasyon tabloları olmadan
   non-waivable kurallar dayanıksızdır. *(Bölüm 2.2)*

4. **Uyuşmazlık çözümünde tur sınırı ve breaker yok.** Açık bulgular sessizce
   kaybolabilir. *(Bölüm 5.2)*

5. **Commissioning planı ajan tarafından tüketilebilir değil.** %59 şablon,
   tetikleyici yok, demir kural yok. Model tarafından yürütülecek bir
   laboratuvarın planı, modele yüklenebilir olmalı. *(Bölüm 2.4)*

---

## Kapanış

Superpowers bir kodlama metodolojisi. Ama çözdüğü problem sizinkiyle **aynı**:
*bir ajanın ürettiği işe nasıl güvenilir?*

Ve cevabı, sizin mimarinizin cevabıyla aynı yönde: **bilgi asimetrisi,
bağımsız review, mekanik doğrulama, insan otoritesi.** İki tasarımın bağımsız
olarak aynı sonuçlara varması (gate töreni esner–kayıt esnemez; taze bağlam;
timeout auto-approve değil) mimarinizin doğru eksende olduğunun kanıtı.

Superpowers'ın sizde olmayan tek şeyi: **kuralların ajan gerekçelerine karşı
nasıl dayanıklı hale getirileceğine dair deneysel bir yöntem.** Skill'i
yazmadan önce ajanın nasıl başarısız olduğunu izleyip o *spesifik* kaçamakları
kapatmak — ve kapanmayan her kaçamağı bir sonraki turda kapatmak.

Bir laboratuvarı modellerin yürüteceği düşünülürse, bu yöntem opsiyonel değil.

---

**Sonraki adım:** Bu belge ve [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS İdeal Yapı]] onaylandıktan sonra,
`planning/commissioning/` altındaki WP dosyaları bu yapıya göre güncellenecek —
yeni WP'ler eklenecek, mevcutlar revize edilecek, ve her biri küçük,
adım adım devreye alınabilir parçalara bölünecek.
