# AIRL-OS — Rol → Model Atama Kararı

| Alan | Değer |
|---|---|
| Belge tipi | Mimari karar (ADR adayı) |
| Kapsam | Hangi rolü kim yürütür: insan / model / deterministik kod |
| Kardeş belgeler | `AIRL_OS_IDEAL_STRUCTURE.md` (Bölüm D) · `AIRL_OS_SKILL_LAYER.md` |
| Tarih | 2026-08-22 |
| Durum | **Öneri — uygulanmadan önce insan onayı gerekir** |

---

## 0. Önce: mimariyi bozan bir bulgu

`AIRL-OS-Architecture.md` şu alanları taşıyor:

```yaml
model_profile: "Claude-Sonnet-5-Qualified-20260801"
model_snapshot: "Claude Sonnet 5 20260801"
```

**Bu kimlikler mevcut değil.** Güncel nesil Claude modellerinin tarih ekli tam
kimliği yoktur — takma ad *kimliğin kendisidir*:

| Model | Kimlik | Tarih ekli tam kimlik |
|---|---|---|
| Claude Fable 5 | `claude-fable-5` | **yok** |
| Claude Opus 5 | `claude-opus-5` | **yok** |
| Claude Opus 4.8 | `claude-opus-4-8` | **yok** |
| Claude Sonnet 5 | `claude-sonnet-5` | **yok** |
| Claude Haiku 4.5 | `claude-haiku-4-5` | `claude-haiku-4-5-20251001` |

> **Sonuç:** Hosted Claude modelleri için **tarih bazlı snapshot pinning
> yapılamaz.** `ExperimentRun.model_snapshot` alanı, güncel nesil modellerle
> doldurulamaz.

Ve bu, doğrudan **İnvariant 4**'ü kırar:

> *"G7 clean-room run, frozen manifest ile tanımlı toleransı üretir."*

Frozen manifest bir model snapshot'ı işaret edemiyorsa, G7a (deterministik
reproduction) hosted modelle **yapısal olarak imkânsızdır.** Bu bir tercih
değil, bir kısıttır.

### Ne yapılabilir — üç katmanlı ikame

| Katman | Ne pinlenir | Neyi garanti eder |
|---|---|---|
| **1. Capability fingerprint** | `GET /v1/models/{id}` → `max_input_tokens`, `max_tokens`, `capabilities` ağacı; hash'lenip manifest'e yazılır | Model yüzeyinin değişmediğini; **davranışın aynı kaldığını değil** |
| **2. Tam I/O kaydı** | İstek gövdesi + yanıt + `response.model` + `usage` (Langfuse) | Ne sorulduğu ve ne cevaplandığı denetlenebilir; **yeniden üretilebilir değil** |
| **3. Yerel open-weight** | GGUF dosyasının **SHA-256**'sı + çalıştırma parametreleri | **Gerçek determinizm.** Ağırlıklar sizde. |

> **Karar:** `R3` claim üreten hiçbir koşu hosted modelle yapılamaz.
> Katman 3 zorunludur. R1/R2 için katman 1+2 yeterlidir ve `model_snapshot`
> alanı `capability_fingerprint` olarak yeniden adlandırılmalıdır.

Elinizdeki 2×RTX A5000 (48 GB toplam VRAM) bu yüzden opsiyonel bir tercih
değil, **R3'ün önkoşuludur**.

---

## 1. Bağımsızlığın dürüst tanımı

`IndependenceMatrix`'in `Model Lineage` boyutu bugün şöyle işliyor:
*"farklı sağlayıcı / temel model / snapshot / fine-tune"*.

**Kritik ayrım — bu kademe eşit değildir:**

| Ayrım | Gerçek bağımsızlık değeri |
|---|---|
| Aynı ailede farklı kademe (Sonnet 5 ↔ Opus 5) | **Düşük.** Ortak eğitim soyu, ortak RLHF konvansiyonları, korelasyonlu hata |
| Farklı sağlayıcı ailesi (Anthropic ↔ OpenAI ↔ Google) | **Orta.** Hâlâ örtüşen web korpusu, ama farklı eğitim hattı |
| Model yargısı ↔ **mekanik doğrulama** | **Yüksek.** Tek gerçek bağımsız eksen |

> **Kural:** `R2` ve `R3`'te reviewer **farklı sağlayıcı ailesinden** olmak
> zorundadır. Opus 5'in Sonnet 5'i review etmesi bağımsız review **değildir**;
> `self_check` olarak kaydedilir.

Ve bu kural bile geçicidir — kalıcı olan `measuring-agreement` ile ölçülen
ikili hata korelasyonudur.

---

## 2. Model havuzu

Fiyatlar 1M token başına (giriş / çıkış).

| Tier | Model | Fiyat | Bağlam | Neden bu |
|---|---|---|---|---|
| **local** | Open-weight GGUF (yerel) | donanım | — | **R3 zorunlu.** Tek gerçek determinizm |
| **bulk** | `claude-haiku-4-5` | $1 / $5 | 200K | Hacimli tarama, span çıkarımı, kalibrasyon seti |
| **producer** | `claude-sonnet-5` | $3 / $15 | 1M | Ana üretim tier'ı; kodlama/agentic'te Opus'a yakın |
| **producer+** | `claude-opus-5` | $5 / $25 | 1M | Zor agentic iş, çok dosyalı refactor |
| **adversarial** | `claude-fable-5` | $10 / $50 | 1M | En yetenekli; karşı-tez ve final review |
| **reviewer** | **Anthropic dışı** | — | — | **Bağımsızlık için zorunlu** |
| **arbiter** | Üçüncü aile | — | — | İki tarafı da görür, ikisinden de farklı |

**Sizde hazır olanlar:** Claude (bu oturum), Codex (kullandınız) → en az iki
sağlayıcı ailesi mevcut. Yerel tier için 48 GB VRAM.

### Fiyat notları

- Sonnet 5 için **2026-08-31'e kadar tanıtım fiyatı** $2/$10 — bugün en iyi
  fiyat/performans oranı burada
- **Batch API %50 indirim** — kalibrasyon seti ve multi-analyst koşuları
  latency-duyarsız; batch'te çalıştırın
- **Prompt caching** ~%90 tasarruf: ReviewPacket'ın dondurulmuş öneki
  cache-dostudur. Opus 5'te minimum önek **512 token** (Opus 4.8'de 1024)

### İki operasyonel kısıt

1. **Fable 5, 30 gün veri saklama gerektirir; ZDR altında kullanılamaz.**
   D3/D4 veri için sıfır saklama istiyorsanız Fable 5 kapsam dışıdır.
2. **Fable 5 ve Opus 5 güvenlik sınıflandırıcıları isteği reddedebilir**
   (`stop_reason: "refusal"`, kategori `"cyber"` / `"bio"` vb.). Güvenlik veya
   yaşam bilimleri araştırması yapıyorsanız bu **operasyonel bir gerçektir**:
   `fallbacks: "default"` ile ele alın, ve `content[0]` okumadan önce
   **her zaman `stop_reason` kontrol edin.**

---

## 3. Rol → aktör tablosu

**Gösterim:** 👤 insan · 🤖 model · ⚙️ deterministik kod · ⬜ ertelendi

### 3.1 Kalıcı fonksiyonlar

| Rol | Aktör | Model | Not |
|---|---|---|---|
| Project Decision Owner | 👤 | — | **Asla model değil.** G8/G9 imzası |
| Safety / Data Owner | 👤 | — | Veri sınıfı kararı insan kalır |
| **Research Integrity Officer** | 👤 + ⚙️ | mekanik tetikleyiciler | statcheck/GRIM otomatik açar, hüküm insanın |
| Scientific Owner | 👤 + 🤖 taslak | `claude-opus-5` | Karar sorusunu insan yazar |
| **Statistical Methods Owner** | 👤 + 🤖 | `claude-opus-5` @ `high` | Analiz planını insan kilitler |
| Evidence Lead | 👤 + 🤖 | `claude-sonnet-5` | Freeze kararı insanın |
| Engineering Owner | 🤖 + 👤 onay | `claude-opus-5` @ `xhigh` | Kod üretimi |
| Assurance Lead | 👤 + ⚙️ | — | Reviewer ataması; **model değil** |
| **Research Software Engineer** | 🤖 + 👤 onay | `claude-sonnet-5` | RO-Crate, Nix, badge |
| **Data Steward** | 🤖 + 👤 onay | `claude-sonnet-5` | Croissant, DOI |
| **Scientific Editor** | ⚙️ + 🤖 | `claude-sonnet-5` | Kapsam kontrolü **mekanik** |
| **Red Team Lead** | 🤖 + 👤 | `claude-fable-5` @ `xhigh` | Pre-mortem, kontrol enjeksiyonu |
| **Knowledge Steward** | ⚙️ + 🤖 | `claude-haiku-4-5` | Çelişki taraması |
| **Metascience Lead** | 👤 + ⚙️ | — | Ölçer; **bloke etmez** |

### 3.2 Gate → aktör

| Gate | ⚙️ Mekanik | 🤖 Model | 👤 İnsan |
|---|---|---|---|
| **G0** Intake | duplicate arama (embedding + Neo4j) | `haiku-4-5` triyaj | greenlight (5 dk) |
| **G1** Charter | **`RiskProfile → AssuranceClass` policy engine** | `opus-5` taslak | **karar sorusu + onay** |
| **G2** Protocol | şablon tamlık, placeholder taraması | `opus-5` taslak · `fable-5` pre-mortem · **farklı aile** Stage-1 review | Scientific + Stat Owner **imza** |
| **G2b** Analysis Plan | — | `opus-5` @ `high` | **Stat Methods Owner kilitler** |
| **G3** Literature | GROBID, DOI çözümü, dedup, hash | `sonnet-5` sorgu planı · `haiku-4-5` tarama | Evidence Lead **dondurur** |
| **G4** Baseline | baseline koşusu | `opus-5` plan · `fable-5` pre-mortem | bütçe onayı |
| **G5** Execute | **deneyin kendisi** | *(model deneyin konusu değilse yok)* | — |
| **G6-0** Mekanik | **statcheck, GRIM, GRIMMER, entailment, hash** | — | — |
| **G6-1** Blind | ReviewPacketBuilder (**program**) | **N reviewer, Anthropic dışı** | — |
| **G6-2** Adversarial | ACH matrisi | `fable-5` @ `xhigh` | — |
| **G6-3** Disagreement | verdict karşılaştırma | Delphi turları (aynı havuz) | arbiter **yalnız yakınsamazsa** |
| **G7a** Reproduction | **deterministik; model YOK** | — | — |
| **G7b** Replication | dağılım testi | — | RSE badge atar |
| **G8** Decision | paket bütünlüğü | **öneri üretir, karar vermez** | **YALNIZ İNSAN, kotalı** |
| **G9** Publish | **scope conformance**, RO-Crate, hash | `sonnet-5` taslak | Decision Owner + Editor |
| **G10** Monitor | Crossref/Retraction Watch/CVE | `haiku-4-5` triyaj | material sinyalde karar |

### 3.3 Üç değişmez

1. **G5'te model yoktur** (deney modelin kendisi değilse). Laboratuvarın en
   temiz katmanı budur — koruyun.
2. **G7a'da model yoktur.** Ya tutar ya tutmaz.
3. **G8'de model yalnız öneri üretir.** Zaten non-waivable ✅

---

## 4. Effort → assurance sınıfı eşlemesi

Effort ladder (`low` → `max`) doğrudan R sınıflarına bağlanır:

| Assurance | Producer effort | Reviewer effort | Adversarial | Reviewer kotası |
|---|---|---|---|---|
| **R1** | `medium` | `high` | — | 1 |
| **R2** | `high` | `high` | `xhigh` | 2, **farklı aile** |
| **R3** | `xhigh` | `xhigh` | `max` | 3, **farklı aile** + yerel repro |

**Not:** `low`/`medium` güncel modellerde beklenenden güçlü. R1 için `medium`
gerçekten yeterli; maliyet kaldıracınız burada.

**Adaptive thinking:** Opus 5'te varsayılan **açık**. `thinking` alanını atlamak
düşünmeyi kapatmaz. Ve `max_tokens` düşünme + yanıtı **birlikte** sınırlar —
kısa `max_tokens` ile gelen bir prompt artık ortadan kesilebilir.

> ⚠️ **Düşünmeyi kapatmayın.** `thinking: {type: "disabled"}` Opus 5'te iki
> sessiz hata modu doğurur: araç çağrısı **düz metin olarak** yazılabilir
> (çağrı hiç çalışmaz, hata da vermez) ve `<thinking>` etiketleri yanıta
> sızabilir. Maliyet için `effort` düşürün, düşünmeyi kapatmayın.

---

## 5. Bağımsızlık kotası — uygulanabilir kural

```yaml
independence_quota:
  R1: {reviewers: 1, family_rule: "any"}
  R2: {reviewers: 2, family_rule: "producer_family_excluded"}
  R3: {reviewers: 3, family_rule: "producer_family_excluded",
       extra: "reproduction on local open-weight"}

hard_rules:
  - producer profili ve final reviewer profili AYNI OLAMAZ
  - R2/R3'te reviewer producer'ın SAĞLAYICI AİLESİNDEN olamaz
  - ölçülmüş ikili hata korelasyonu ρ > eşik olan iki profil
    aynı kotaya birlikte sayılmaz          # measuring-agreement çıktısı
  - producer hiçbir ajanı çağıramaz         # independence-discipline
  - adversarial reviewer metriği REDDETME kalitesidir
```

**Advisor tool uyarısı:** Anthropic'in advisor tool'u executor↔advisor
eşleştirmesi yapar — ama Opus 5 advisor sonucu **şifreli** döner
(`advisor_redacted_result`), istemci okuyamaz. **Her şeyi denetleyen bir
laboratuvarda okunamayan bir tavsiye kanalı kabul edilemez.** Advisor tool'u
G6 review hattında kullanmayın.

---

## 6. Maliyet zarfı — kaba tahmin

Bir R2 confirmatory projesi için (kaynak: 200 aday → 40 dahil, 12 senaryo,
3 reviewer):

| Aşama | Model | Tahmini token | Yaklaşık maliyet |
|---|---|---|---|
| G3 tarama | `haiku-4-5` batch | ~2M giriş | ~$1 |
| G3 span çıkarımı | `haiku-4-5` | ~1M | ~$1 |
| G2 protokol + analiz planı | `opus-5` @ high | ~300K | ~$5 |
| G5 analiz (multi-analyst ×3) | `sonnet-5` | ~1.5M | ~$8 |
| G6 blind review ×2 | **Anthropic dışı** | ~600K | sağlayıcıya göre |
| G6 adversarial | `fable-5` @ xhigh | ~200K | ~$12 |
| G9 metin + scope | `sonnet-5` | ~200K | ~$3 |
| **Toplam (Anthropic tarafı)** | | | **~$30** |

Prompt caching ve batch ile bu rakam yarıya iner. **Asıl maliyet model değil,
insan karar kapasitesidir** — dikkat bütçesi (haftada 5 G8 kararı) gerçek
darboğazdır.

---

## 7. Uygulama sırası

| # | İş | Bloke ettiği |
|---|---|---|
| 1 | `model_snapshot` → `capability_fingerprint` alan değişimi + `GET /v1/models` snapshot'ı | İnvariant 4 |
| 2 | R3 → yerel open-weight zorunluluğunu ADR'ye yaz | G7a |
| 3 | Reviewer havuzuna **Anthropic dışı** en az bir sağlayıcı bağla | R2/R3 bağımsızlık |
| 4 | `stop_reason == "refusal"` + `fallbacks: "default"` her çağrıda | Üretim dayanıklılığı |
| 5 | Effort → R sınıfı eşlemesini policy engine'e koy | Gate derinliği |
| 6 | Batch API'yi kalibrasyon seti ve multi-analyst için bağla | Metascience maliyeti |
| 7 | `measuring-agreement` calibration set kur | K1 — ölçülmüş bağımsızlık |

---

## 8. Açıkça ertelenenler

| Rol / bileşen | Neden |
|---|---|
| Advisor tool | Şifreli sonuç — denetlenemez |
| Fable 5 (D3/D4 işlerde) | 30 gün saklama zorunluluğu, ZDR yok |
| Managed Agents | Kendi orkestrasyonunuz Temporal; iki kontrol düzlemi istemezsiniz |
| Ayrı `arbiter` sağlayıcı ailesi | Üçüncü aile erişimi gerekir; şimdilik insan arbiter |

---

## 9. Bu kararın sınırı

Bu atama **ölçülmemiş bir varsayıma dayanıyor**: farklı sağlayıcı ailelerinin
hata korelasyonunun aynı aile içindeki kademelerden düşük olduğu.

Bu makul ama **kanıtlanmış değil.** `measuring-agreement` calibration set
kurulduğunda ölçülecek ve bu tablo o ölçüme göre revize edilecek.

> Bir laboratuvar kendi bağımsızlık varsayımını ölçmeden çalıştırıyorsa,
> ürettiği "bağımsız doğrulama" bir varsayımın tekrarıdır.
